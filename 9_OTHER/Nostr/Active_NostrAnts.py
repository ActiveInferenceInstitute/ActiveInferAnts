import numpy as np
from scipy.special import softmax
import matplotlib.pyplot as plt
from typing import List, Dict, Tuple, Optional, Any
import json
import time
import asyncio
from nostr.event import Event
from nostr.key import PrivateKey
from nostr.relay_manager import RelayManager
from nostr.filter import Filter, Filters
from nostr.message_type import ClientMessageType
from dataclasses import dataclass
import logging
from concurrent.futures import ThreadPoolExecutor
from collections import deque

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@dataclass
class SimulationConfig:
    num_ants: int
    num_actions: int
    num_observations: int
    num_steps: int
    relays: List[str]
    learning_rate: float
    discount_factor: float
    exploration_rate: float
    pheromone_evaporation_rate: float

class NostrAnt:
    def __init__(self, private_key: str, config: SimulationConfig):
        self.private_key = PrivateKey.from_nsec(private_key)
        self.public_key = self.private_key.public_key
        self.config = config
        
        # Initialize beliefs, preferences, and policies
        self.beliefs = np.ones(config.num_observations) / config.num_observations
        self.preferences = np.zeros(config.num_observations)
        self.policies = [np.random.randint(0, config.num_actions, size=5) for _ in range(10)]
        
        # Initialize transition and likelihood matrices
        self.A = np.ones((config.num_observations, config.num_actions, config.num_observations)) / config.num_observations
        self.B = np.ones((config.num_observations, config.num_actions)) / config.num_actions

        # Initialize pheromone levels and position
        self.pheromone = 100.0
        self.position = np.random.randint(0, config.num_observations)

        # Initialize relay manager
        self.relay_manager = RelayManager()
        for relay in config.relays:
            self.relay_manager.add_relay(relay)
        self.relay_manager.open_connections()

        # Initialize experience replay buffer
        self.experience_buffer = deque(maxlen=1000)

    def update_beliefs(self, observation: int):
        likelihood = self.B[observation, :]
        self.beliefs = self.beliefs * likelihood
        self.beliefs /= np.sum(self.beliefs)

    def infer_state(self) -> int:
        return np.argmax(self.beliefs)

    def calculate_expected_free_energy(self, policy: List[int]) -> float:
        G = 0
        beliefs = self.beliefs.copy()
        
        for action in policy:
            expected_obs = beliefs @ self.B[:, action]
            beliefs_given_obs = (self.A[:, action, :].T * beliefs[:, None]).T
            beliefs_given_obs /= np.sum(beliefs_given_obs, axis=0)
            
            kl_divergence = np.sum(beliefs_given_obs * np.log(beliefs_given_obs / beliefs[:, None]), axis=0)
            information_gain = np.sum(expected_obs * kl_divergence)
            
            expected_value = np.dot(expected_obs, self.preferences)
            
            G += information_gain + expected_value
            
            beliefs = beliefs @ self.A[:, action, :]
        
        return G

    def select_policy(self) -> List[int]:
        policy_values = [self.calculate_expected_free_energy(policy) for policy in self.policies]
        return self.policies[np.argmax(policy_values)]

    def act(self) -> int:
        if np.random.random() < self.config.exploration_rate:
            action = np.random.randint(0, self.config.num_actions)
        else:
            policy = self.select_policy()
            action = policy[0]
        
        self.pheromone -= 1.0  # Decrease pheromone level with each action
        self.position = (self.position + action) % self.config.num_observations  # Update position
        return action

    async def publish_action(self, action: int):
        content = json.dumps({
            "action": action,
            "position": self.position,
            "pheromone": self.pheromone,
        })
        event = Event(
            public_key=self.public_key.hex(),
            created_at=int(time.time()),
            kind=1000,  # Custom event kind for NostrAnt actions
            tags=[
                ["t", "nostr_ant_action"],
                ["d", f"ant_action_{int(time.time())}"]  # Unique identifier for the action
            ],
            content=content
        )
        event.sign(self.private_key.hex())
        await self.relay_manager.publish_event(event)

    async def observe_environment(self) -> Optional[int]:
        filters = Filters([Filter(kinds=[1001], tags=[["t", "nostr_environment_state"]])])
        subscription_id = self.relay_manager.add_subscription(filters)
        
        try:
            while True:
                event_msg = await self.relay_manager.receive_message()
                if event_msg.type == ClientMessageType.EVENT:
                    event = event_msg.event
                    if event.kind == 1001 and ["t", "nostr_environment_state"] in event.tags:
                        state_data = json.loads(event.content)
                        return state_data.get("state")
                elif event_msg.type == ClientMessageType.EOSE:
                    break
        finally:
            self.relay_manager.close_subscription(subscription_id)
        
        return None

    def update_experience(self, state: int, action: int, reward: float, next_state: int):
        self.experience_buffer.append((state, action, reward, next_state))

    def learn_from_experience(self):
        if len(self.experience_buffer) < 32:
            return

        batch = np.random.choice(self.experience_buffer, size=32, replace=False)
        states, actions, rewards, next_states = zip(*batch)

        current_q_values = self.B[states, actions]
        next_q_values = np.max(self.B[next_states], axis=1)
        target_q_values = rewards + self.config.discount_factor * next_q_values

        self.B[states, actions] += self.config.learning_rate * (target_q_values - current_q_values)

class NostrAntColony:
    def __init__(self, config: SimulationConfig):
        self.config = config
        self.ants = [NostrAnt(PrivateKey().nsec(), config) for _ in range(config.num_ants)]
        self.global_state = np.random.randint(0, config.num_observations)
        self.pheromone_map = np.zeros(config.num_observations)
        self.relay_manager = RelayManager()
        for relay in config.relays:
            self.relay_manager.add_relay(relay)
        self.relay_manager.open_connections()

    async def publish_state(self):
        content = json.dumps({
            "state": self.global_state,
            "pheromone_map": self.pheromone_map.tolist(),
        })
        event = Event(
            public_key=PrivateKey().public_key.hex(),
            created_at=int(time.time()),
            kind=1001,  # Custom event kind for environment state
            tags=[
                ["t", "nostr_environment_state"],
                ["d", f"environment_state_{int(time.time())}"]  # Unique identifier for the state update
            ],
            content=content
        )
        event.sign(PrivateKey().hex())
        await self.relay_manager.publish_event(event)

    async def step(self) -> List[int]:
        actions = await asyncio.gather(*[ant.act() for ant in self.ants])
        
        await asyncio.gather(*[ant.publish_action(action) for ant, action in zip(self.ants, actions)])
        
        self.global_state = (self.global_state + sum(actions)) % self.config.num_observations
        
        # Update pheromone map
        for ant in self.ants:
            self.pheromone_map[ant.position] += ant.pheromone / 100.0
        
        # Evaporate pheromones
        self.pheromone_map *= self.config.pheromone_evaporation_rate
        
        await self.publish_state()
        
        observations = [np.random.choice(self.config.num_observations, p=ant.B[:, action]) for ant, action in zip(self.ants, actions)]
        
        # Update ant beliefs and learn from experience
        for ant, action, observation in zip(self.ants, actions, observations):
            ant.update_beliefs(observation)
            reward = self.pheromone_map[ant.position]  # Use pheromone level as reward
            ant.update_experience(ant.position, action, reward, observation)
            ant.learn_from_experience()
        
        return observations

async def run_simulation(colony: NostrAntColony) -> Tuple[List[int], List[List[float]], List[np.ndarray]]:
    global_states = []
    ant_beliefs = [[] for _ in colony.ants]
    pheromone_maps = []
    
    for _ in range(colony.config.num_steps):
        observations = await colony.step()
        global_states.append(colony.global_state)
        for i, ant in enumerate(colony.ants):
            ant_beliefs[i].append(ant.beliefs.copy())
        pheromone_maps.append(colony.pheromone_map.copy())
    
    return global_states, ant_beliefs, pheromone_maps

def plot_results(global_states: List[int], ant_beliefs: List[List[float]], pheromone_maps: List[np.ndarray]):
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 18))
    
    # Plot global state
    ax1.plot(global_states, label='Global State')
    ax1.set_xlabel('Time Step')
    ax1.set_ylabel('State')
    ax1.set_title('Global State Evolution')
    ax1.legend()
    
    # Plot ant beliefs
    for i, beliefs in enumerate(ant_beliefs):
        ax2.plot(np.argmax(beliefs, axis=1), label=f'Ant {i} Belief')
    ax2.set_xlabel('Time Step')
    ax2.set_ylabel('Belief')
    ax2.set_title('Ant Beliefs Evolution')
    ax2.legend()
    
    # Plot pheromone map
    im = ax3.imshow(np.array(pheromone_maps).T, aspect='auto', cmap='viridis')
    ax3.set_xlabel('Time Step')
    ax3.set_ylabel('Position')
    ax3.set_title('Pheromone Map Evolution')
    plt.colorbar(im, ax=ax3, label='Pheromone Intensity')
    
    plt.tight_layout()
    plt.show()

async def main():
    config = SimulationConfig(
        num_ants=10,
        num_actions=3,
        num_observations=20,
        num_steps=100,
        relays=["wss://relay.damus.io", "wss://relay.nostr.info"],
        learning_rate=0.1,
        discount_factor=0.95,
        exploration_rate=0.1,
        pheromone_evaporation_rate=0.95
    )

    colony = NostrAntColony(config)
    global_states, ant_beliefs, pheromone_maps = await run_simulation(colony)

    plot_results(global_states, ant_beliefs, pheromone_maps)

if __name__ == "__main__":
    asyncio.run(main())
