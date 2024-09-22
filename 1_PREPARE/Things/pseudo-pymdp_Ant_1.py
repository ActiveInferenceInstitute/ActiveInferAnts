import numpy as np
from typing import List, Optional, Dict, Any, Tuple
from tabulate import tabulate
from termcolor import colored
import logging

class NestmateAgent:
    """
    An agent that employs active inference for decision-making within an ant colony,
    leveraging a comprehensive model of its environment and nestmate dynamics,
    based on a partially-observable Markov decision process (POMDP).
    """
    def __init__(self, num_observations: List[int], num_states: List[int], num_actions: List[int],
                 policy_length: int = 1, inference_depth: int = 1):
        """
        Initializes the NestmateAgent with dimensions for the environment, nestmate dynamics, and its preferences.

        Args:
            num_observations (List[int]): Number of possible observations for each modality.
            num_states (List[int]): Number of possible states for each factor.
            num_actions (List[int]): Number of possible actions for each factor.
            policy_length (int): The number of time steps to consider in each policy.
            inference_depth (int): The depth of recursive inference for state estimation.
        """
        self.observation_model = [self._normalize(np.random.rand(num_obs, num_state)) 
                                  for num_obs, num_state in zip(num_observations, num_states)]
        self.transition_model = [self._normalize(np.random.rand(num_state, num_state)) 
                                 for num_state in num_states]
        self.preference_model = [np.eye(num_obs) for num_obs in num_observations]
        self.initial_state_distribution = [np.random.dirichlet(np.ones(num_state)) 
                                           for num_state in num_states]
        
        self.policy_prior = self._normalize(np.random.rand(np.prod(num_actions) ** policy_length))
        
        self.generative_model = {
            'observation_model': self.observation_model,
            'transition_model': self.transition_model,
            'preference_model': self.preference_model,
            'initial_state_distribution': self.initial_state_distribution,
            'policy_prior': self.policy_prior
        }
        
        self.model_dimensions = {
            'num_observations': num_observations,
            'num_states': num_states,
            'num_modalities': len(num_observations),
            'num_factors': len(num_states)
        }

        self.posterior_states = self.initial_state_distribution.copy()
        self.policy_length = policy_length
        self.inference_depth = inference_depth
        self.controllable_factors = list(range(len(num_states)))
        self.possible_policies = self._generate_possible_policies(num_actions)

        self._setup_logging()
        self._output_variable_shapes()

    @staticmethod
    def _normalize(arr: np.ndarray) -> np.ndarray:
        """Normalize array so that each row sums to 1. Adds epsilon to prevent division by zero."""
        row_sums = arr.sum(axis=-1, keepdims=True)
        row_sums[row_sums == 0] = 1  # Prevent division by zero
        return arr / row_sums

    def _generate_possible_policies(self, num_actions: List[int]) -> np.ndarray:
        """
        Efficiently generates the set of feasible policies based on the agent's models.

        Args:
            num_actions (List[int]): Number of possible actions for each factor.

        Returns:
            np.ndarray: Array of all possible policies.
        """
        from itertools import product

        action_combinations = list(product(*[range(action) for action in num_actions]))
        policy_combinations = list(product(action_combinations, repeat=self.policy_length))
        possible_policies = np.array(policy_combinations).reshape(-1, self.policy_length, len(num_actions))
        
        return possible_policies

    def _setup_logging(self):
        """Set up logging for the agent with configurable log level."""
        log_level = logging.INFO
        logging.basicConfig(level=log_level, format='%(asctime)s - %(levelname)s - %(message)s',
                            handlers=[logging.StreamHandler()])
        self.logger = logging.getLogger(__name__)

    def _output_variable_shapes(self) -> None:
        """
        Outputs the shape/size of each instantiated variable to the terminal,
        including detailed descriptions of their roles and relationships,
        formatted as a table with coloring for readability.
        """
        headers = ["Variable", "Shape", "Description"]
        variable_shapes = [
            ['observation_model', [model.shape for model in self.observation_model], 'Maps each state to an observation for each modality.'],
            ['transition_model', [model.shape for model in self.transition_model], 'Describes state transitions for each factor.'],
            ['preference_model', [model.shape for model in self.preference_model], 'Represents the agent\'s preferences over observations.'],
            ['initial_state_distribution', [model.shape for model in self.initial_state_distribution], 'The initial beliefs about the state of the world.'],
            ['policy_prior', self.policy_prior.shape, 'The prior probabilities of each possible policy.'],
            ['possible_policies', self.possible_policies.shape, 'All feasible sequences of actions given the policy length.']
        ]
        print(colored(tabulate(variable_shapes[:2], headers=headers, tablefmt="fancy_grid"), 'cyan'))
        print(colored(tabulate(variable_shapes[2:4], headers=headers, tablefmt="fancy_grid"), 'yellow'))
        print(colored(tabulate(variable_shapes[4:], headers=headers, tablefmt="fancy_grid"), 'green'))
        print(colored(f"Policy length: {self.policy_length}, representing the time horizon for policy inference.", 'magenta'))
        print(colored(f"Inference depth: {self.inference_depth}, indicating the depth of recursive inference for state estimation.", 'magenta'))

    def update_beliefs(self, observation: List[np.ndarray]) -> None:
        """
        Update the agent's beliefs based on a new observation.

        Args:
            observation (List[np.ndarray]): The observed data for each modality.
        """
        # Implement belief update logic here
        self.logger.info("Updating beliefs based on new observation.")
        pass  # Placeholder for actual implementation

    def infer_states(self) -> List[np.ndarray]:
        """
        Perform state inference based on current beliefs and models.

        Returns:
            List[np.ndarray]: Inferred states for each factor.
        """
        # Implement state inference logic here
        self.logger.info("Performing state inference.")
        return self.posterior_states  # Placeholder for actual implementation

    def plan_actions(self) -> Tuple[np.ndarray, float]:
        """
        Plan actions based on current beliefs and preferences.

        Returns:
            Tuple[np.ndarray, float]: The chosen policy and its expected free energy.
        """
        # Implement action planning logic here
        self.logger.info("Planning actions.")
        return self.possible_policies[0], 0.0  # Placeholder for actual implementation

def main():
    # Instantiate variables with sizes appropriate for a Partially Observable Markov Decision Process (POMDP)
    num_observations = [10, 15]  # Example observation sizes for two modalities
    num_states = [5, 3]  # Example state sizes for two factors
    num_actions = [3, 2]  # Example action sizes for two factors
    policy_length = 4
    inference_depth = 3

    # Initialize the agent with the specified configurations
    agent = NestmateAgent(num_observations, num_states, num_actions, policy_length, inference_depth)

    # Simulate agent operation
    observation = [np.random.rand(num_obs) for num_obs in num_observations]
    agent.update_beliefs(observation)
    inferred_states = agent.infer_states()
    chosen_policy, expected_free_energy = agent.plan_actions()

    print("\nSimulation Results:")
    print(f"Inferred States: {[state.shape for state in inferred_states]}")
    print(f"Chosen Policy Shape: {chosen_policy.shape}")
    print(f"Expected Free Energy: {expected_free_energy}")

if __name__ == "__main__":
    main()
