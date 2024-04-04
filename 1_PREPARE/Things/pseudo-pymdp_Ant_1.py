import numpy as np
from typing import List, Optional, Dict, Any
from tabulate import tabulate  # Import tabulate for table formatting
from termcolor import colored  # Import termcolor for coloring text

class NestmateAgent:
    """
    An agent that employs active inference for decision-making within an ant colony, leveraging a comprehensive model of its environment and nestmate dynamics, based on a partially-observable Markov decision process.
    """
    def __init__(self, num_observations: List[int], num_states: List[int], num_actions: List[int], policy_length: int = 1, inference_depth: int = 1):
        """
        Initializes the NestmateAgent with dimensions for the environment, nestmate dynamics, and its preferences.
        """
        self.observation_model = [np.random.rand(num_obs, num_state) for num_obs, num_state in zip(num_observations, num_states)]
        self.transition_model = [np.random.rand(num_state, num_state) for num_state in num_states]
        self.preference_model = [np.eye(num_obs) for num_obs in num_observations]  # Identity matrices as placeholder preferences
        self.initial_state_distribution = [np.random.dirichlet(np.ones(num_state)) for num_state in num_states]
        
        self.policy_prior = np.random.rand(np.prod(num_actions) ** policy_length)
        
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

        self.posterior_states = self.initial_state_distribution
        self.policy_length = policy_length
        self.inference_depth = inference_depth
        self.controllable_factors = list(range(len(num_states)))
        self.possible_policies = self._generate_possible_policies(num_actions)

        self._output_variable_shapes()

    def _generate_possible_policies(self, num_actions: List[int]) -> np.ndarray:
        """
        Generates the set of feasible policies based on the agent's models.
        """
        num_policies = np.prod([action ** self.policy_length for action in num_actions])
        possible_policies = np.zeros((num_policies, self.policy_length, len(num_actions)), dtype=int)
        
        # Generate all possible policies
        for policy_index in range(num_policies):
            policy = np.unravel_index(policy_index, [action for action in num_actions] * self.policy_length)
            for time_step in range(self.policy_length):
                for factor_index, action in enumerate(policy[time_step * len(num_actions): (time_step + 1) * len(num_actions)]):
                    possible_policies[policy_index, time_step, factor_index] = action
        
        return possible_policies

    def _output_variable_shapes(self) -> None:
        """
        Outputs the shape/size of each instantiated variable to the terminal, including detailed descriptions of their roles and relationships, formatted as a table with coloring for readability.
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
        # Color coding for readability
        print(colored(tabulate(variable_shapes[:2], headers=headers, tablefmt="fancy_grid"), 'cyan'))  # Models in cyan
        print(colored(tabulate(variable_shapes[2:4], headers=headers, tablefmt="fancy_grid"), 'yellow'))  # Preferences and beliefs in yellow
        print(colored(tabulate(variable_shapes[4:], headers=headers, tablefmt="fancy_grid"), 'green'))  # Policies in green
        print(colored(f"Policy length: {self.policy_length}, representing the time horizon for policy inference.", 'magenta'))
        print(colored(f"Inference depth: {self.inference_depth}, indicating the depth of recursive inference for state estimation.", 'magenta'))

def main():
    # Instantiate variables with sizes appropriate for a Partially Observable Markov Decision Process (POMDP)
    num_observations = [10, 15]  # Example observation sizes for two modalities
    num_states = [5, 3]  # Example state sizes for two factors
    num_actions = [3, 2]  # Example action sizes for two factors
    policy_length = 4
    inference_depth = 3

    # Initialize the agent with the specified configurations
    agent = NestmateAgent(num_observations, num_states, num_actions, policy_length, inference_depth)

    # Output the shapes of the initialized variables
    agent._output_variable_shapes()

if __name__ == "__main__":
    main()

