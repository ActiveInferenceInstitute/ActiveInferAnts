import logging
import os
import json
import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, Any, List
from all_pymdp_utils import (
    random_A_matrix, random_B_matrix, obj_array_zeros, obj_array_uniform,
    Agent, entropy
)

class SocialAgent:
    def __init__(self, id: int, num_states: List[int], num_obs: List[int], num_controls: List[int]):
        self.id = id
        self.A = random_A_matrix(num_obs, num_states)
        self.B = random_B_matrix(num_states, num_controls)
        self.C = obj_array_zeros(num_obs)
        self.D = obj_array_uniform(num_states)
        
        self.agent = Agent(A=self.A, B=self.B, C=self.C, D=self.D)
        self.qs = self.agent.D
        self.last_action = None

    def step(self, observation):
        self.qs = self.agent.infer_states(observation)
        q_pi, _ = self.agent.infer_policies()
        action = self.agent.sample_action(q_pi)
        self.last_action = action
        return action

    def update_model(self, observation):
        self.agent.update_A(observation)

def run_and_analyze_simulation(num_agents: int, num_steps: int, output_dir: str) -> Dict[str, Any]:
    num_states = [5, 5]
    num_obs = [5, 5]
    num_controls = [3, 3]

    agents = [SocialAgent(i, num_states, num_obs, num_controls) for i in range(num_agents)]
    results = {agent.id: [] for agent in agents}

    for step in range(num_steps):
        logging.info(f"Step {step + 1}/{num_steps}")
        
        observations = generate_observations(agents)

        for agent in agents:
            action = agent.step(observations[agent.id])
            results[agent.id].append(action)

        update_environment(agents)

        for agent in agents:
            agent.update_model(observations[agent.id])

    analysis = analyze_results(results)

    simulation_data = {
        "parameters": {
            "num_agents": num_agents,
            "num_steps": num_steps,
            "num_states": num_states,
            "num_obs": num_obs,
            "num_controls": num_controls
        },
        "results": results,
        "analysis": analysis
    }

    return simulation_data

def generate_observations(agents):
    observations = {}
    for agent in agents:
        observations[agent.id] = [np.random.randint(0, obs_dim) for obs_dim in agent.agent.num_obs]
    return observations

def update_environment(agents):
    # Placeholder for environment update logic
    pass

def analyze_results(results):
    analysis = {}
    for agent_id, actions in results.items():
        analysis[agent_id] = {
            "avg_action": sum(actions) / len(actions),
            "action_distribution": np.bincount(actions, minlength=3).tolist()
        }
    return analysis

def analyze_agent_behavior(results: Dict[int, Any]) -> None:
    for agent_id, actions in results.items():
        avg_action = sum(actions) / len(actions)
        logging.info(f"Agent {agent_id} average action: {avg_action:.2f}")
        action_counts = np.bincount(actions, minlength=3)
        logging.info(f"Agent {agent_id} action distribution: {action_counts}")

def visualize_results(results: Dict[int, List[int]], output_dir: str) -> None:
    for agent_id, actions in results.items():
        plt.figure(figsize=(10, 5))
        plt.plot(actions)
        plt.title(f"Agent {agent_id} Actions Over Time")
        plt.xlabel("Time Step")
        plt.ylabel("Action")
        plt.savefig(os.path.join(output_dir, f"agent_{agent_id}_actions.png"))
        plt.close()

def calculate_metrics(results: Dict[int, List[int]]) -> Dict[str, Any]:
    metrics = {}
    all_actions = [action for actions in results.values() for action in actions]
    metrics["global_action_entropy"] = entropy(np.bincount(all_actions))
    
    for agent_id, actions in results.items():
        metrics[f"agent_{agent_id}_action_entropy"] = entropy(np.bincount(actions))
    
    return metrics

def save_simulation_data(data: Dict[str, Any], output_dir: str) -> None:
    """Save simulation data to a JSON file."""
    file_path = os.path.join(output_dir, "simulation_data.json")
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)
    logging.info(f"Simulation data saved to {file_path}")

def setup_logging(output_dir: str) -> None:
    os.makedirs(output_dir, exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.FileHandler(os.path.join(output_dir, "simulation.log")),
            logging.StreamHandler()
        ]
    )

def main() -> None:
    # Default values
    num_agents = 5
    num_steps = 100
    output_dir = "output"

    setup_logging(output_dir)
    logger = logging.getLogger(__name__)
    
    try:
        logger.info("Starting social science simulation")
        simulation_data = run_and_analyze_simulation(num_agents, num_steps, output_dir)
        
        logger.info("Analyzing simulation results")
        analyze_agent_behavior(simulation_data["results"])
        
        logger.info("Saving simulation data")
        save_simulation_data(simulation_data, output_dir)
        
        logger.info("Generating additional visualizations")
        visualize_results(simulation_data["results"], output_dir)
        
        logger.info("Calculating advanced metrics")
        advanced_metrics = calculate_metrics(simulation_data["results"])
        logger.info(f"Advanced metrics: {advanced_metrics}")
        
        logger.info("Simulation and analysis completed successfully")
    except Exception as e:
        logger.error(f"An error occurred during the simulation: {str(e)}", exc_info=True)
    finally:
        logger.info("Simulation process finished")

if __name__ == "__main__":
    main()