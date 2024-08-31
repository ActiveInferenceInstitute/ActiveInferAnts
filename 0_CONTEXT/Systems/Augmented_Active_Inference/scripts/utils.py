import logging
import matplotlib.pyplot as plt
import numpy as np
from pymdp import Agent, Inference, Learning

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class SocialAgent(Agent):
    """
    A simple social agent using Active Inference principles.
    """
    def __init__(self, num_states, num_observations, num_actions, agent_id):
        super().__init__(num_states, num_observations, num_actions)
        self.beliefs = np.ones(num_states) / num_states
        self.agent_id = agent_id
        logger.info(f"Agent {self.agent_id} initialized with {num_states} states, {num_observations} observations, and {num_actions} actions")

    def infer_state(self, observation):
        """Infer the current state based on an observation."""
        logger.debug(f"Agent {self.agent_id} received observation: {observation}")
        old_beliefs = self.beliefs.copy()
        self.beliefs = Inference.update_posterior_states(self.beliefs, observation)
        logger.debug(f"Agent {self.agent_id} updated beliefs: {self.beliefs}")
        logger.debug(f"Agent {self.agent_id} belief change: {np.sum(np.abs(self.beliefs - old_beliefs))}")

    def take_action(self):
        """Choose an action based on current beliefs."""
        action = Learning.sample_action(self.beliefs)
        logger.info(f"Agent {self.agent_id} took action: {action}")
        return action

def run_simulation(num_agents, num_steps):
    """Run a simple social simulation with multiple agents."""
    logger.info(f"Starting simulation with {num_agents} agents for {num_steps} steps")
    agents = [SocialAgent(5, 3, 2, i) for i in range(num_agents)]
    
    results = {i: [] for i in range(num_agents)}
    
    for step in range(num_steps):
        logger.info(f"Simulation step: {step}")
        for agent in agents:
            observation = np.random.randint(0, 3)  # Simplified observation
            logger.debug(f"Generated observation {observation} for Agent {agent.agent_id}")
            agent.infer_state(observation)
            action = agent.take_action()
            results[agent.agent_id].append(action)
            logger.info(f"Step {step}, Agent {agent.agent_id}: Observation {observation}, Action {action}")
        
        logger.debug("Belief states at end of step:")
        for agent in agents:
            logger.debug(f"Agent {agent.agent_id} beliefs: {agent.beliefs}")
    
    return results

# Existing functions
def process_data(data):
    """
    Process input data for simulation use.
    
    Args:
        data (np.array): Raw input data
    
    Returns:
        np.array: Processed data
    """
    logging.info("Processing data")
    processed_data = np.array(data)  # Placeholder for actual processing
    return processed_data

def visualize_results(results):
    """
    Visualize simulation results.
    
    Args:
        results (dict): Simulation results
    """
    logging.info("Visualizing results")
    plt.figure(figsize=(10, 6))
    for agent, actions in results.items():
        plt.plot(actions, label=f"Agent {agent}")
    plt.xlabel("Time Step")
    plt.ylabel("Action")
    plt.title("Agent Actions Over Time")
    plt.legend()
    plt.savefig("simulation_results.png")
    logging.info("Results visualization saved as simulation_results.png")

def calculate_metrics(results):
    """
    Calculate metrics from simulation results.
    
    Args:
        results (dict): Simulation results
    
    Returns:
        dict: Calculated metrics
    """
    logging.info("Calculating metrics")
    metrics = {
        "mean_actions": np.mean([np.mean(actions) for actions in results.values()]),
        "std_actions": np.std([np.std(actions) for actions in results.values()])
    }
    logging.info(f"Calculated metrics: {metrics}")
    return metrics