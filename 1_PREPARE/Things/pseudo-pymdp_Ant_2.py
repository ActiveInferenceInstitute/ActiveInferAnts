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
        Initializes the NestmateAgent with dimensions for the environment, nestmate dynamics, and its preferences,
        aligning with the constructs of an Active Inference POMDP.

        Args:
            num_observations (List[int]): Number of possible observations for each modality.
            num_states (List[int]): Number of possible states for each factor.
            num_actions (List[int]): Number of possible actions for each controllable factor.
            policy_length (int): Length of policies to consider.
            inference_depth (int): Depth of recursive inference for state estimation.
        """
        self.observation_model = self._initialize_dirichlet_model(num_observations, num_states)
        self.transition_model = self._initialize_dirichlet_model(num_states, num_states)
        self.preference_model = [np.eye(num_obs) for num_obs in num_observations]
        self.initial_state_distribution = [np.random.dirichlet(np.ones(num_state)) for num_state in num_states]
        self.policy_prior = np.log(np.random.dirichlet(np.ones(np.prod(num_actions) ** policy_length)))
        
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

        self.posterior_states = [np.copy(dist) for dist in self.initial_state_distribution]
        self.policy_length = policy_length
        self.inference_depth = inference_depth
        self.controllable_factors = list(range(len(num_states)))
        self.possible_policies = self._generate_possible_policies(num_actions)

        self._output_variable_shapes()

    @staticmethod
    def _initialize_dirichlet_model(num_outcomes: List[int], num_causes: List[int]) -> List[np.ndarray]:
        """
        Initialize a Dirichlet distribution model.

        Args:
            num_outcomes (List[int]): Number of possible outcomes for each factor.
            num_causes (List[int]): Number of possible causes for each factor.

        Returns:
            List[np.ndarray]: List of Dirichlet distributions.
        """
        return [np.random.dirichlet(np.ones(num_cause), num_outcome) 
                for num_outcome, num_cause in zip(num_outcomes, num_causes)]

    def _generate_possible_policies(self, num_actions: List[int]) -> np.ndarray:
        """
        Enumerates all possible policies, considering the action space and policy length,
        to summarize the total number of feasible policies.

        Args:
            num_actions (List[int]): Number of possible actions for each controllable factor.

        Returns:
            np.ndarray: Array of all possible policies.
        """
        action_combinations = [np.array(range(n)) for n in num_actions]
        policy_space = np.array(np.meshgrid(*action_combinations)).T.reshape(-1, len(num_actions))
        num_policies = np.prod([len(n) ** self.policy_length for n in action_combinations])
        possible_policies = np.array(np.meshgrid(*[policy_space for _ in range(self.policy_length)])).T.reshape(-1, self.policy_length, len(num_actions))

        logging.info(f"Total number of possible policies: {num_policies}")
        return possible_policies

    def _output_variable_shapes(self) -> None:
        """
        Outputs the shape/size of each instantiated variable to the terminal,
        including detailed descriptions of their roles, relationships, and generation methods,
        formatted as a table with coloring for readability.
        """
        headers = ["Variable", "Shape", "Description"]
        variable_shapes = [
            ('observation_model', [model.shape for model in self.observation_model], 'Dirichlet distributions representing the probability of observing each state for each observation modality.'),
            ('transition_model', [model.shape for model in self.transition_model], 'Dirichlet distributions representing the probability of transitioning from one state to another for each state factor.'),
            ('preference_model', [model.shape for model in self.preference_model], 'Identity matrices representing the agent\'s preferences over observations.'),
            ('initial_state_distribution', [model.shape for model in self.initial_state_distribution], 'Dirichlet distributions representing the agent\'s initial beliefs about the world.'),
            ('policy_prior', self.policy_prior.shape, 'Log probabilities representing the prior probabilities of each possible policy.'),
            ('possible_policies', self.possible_policies.shape, 'All feasible sequences of actions generated by enumerating all combinations of actions across the specified policy length.')
        ]
        
        self._print_formatted_table(variable_shapes[:2], headers, 'cyan', "Models")
        self._print_formatted_table(variable_shapes[2:4], headers, 'yellow', "Preferences and Beliefs")
        self._print_formatted_table(variable_shapes[4:], headers, 'green', "Policies")
        
        print(colored(f"Policy length: {self.policy_length}, representing the time horizon for policy inference, with each policy generated by considering all possible action sequences.", 'magenta'))
        print(colored(f"Inference depth: {self.inference_depth}, indicating the depth of recursive inference for state estimation, based on the generative model.", 'magenta'))

    @staticmethod
    def _print_formatted_table(data: List[Tuple], headers: List[str], color: str, title: str) -> None:
        """
        Print a formatted table with a title and colored text.

        Args:
            data (List[Tuple]): The data to be displayed in the table.
            headers (List[str]): The headers for the table columns.
            color (str): The color to use for the table text.
            title (str): The title of the table section.
        """
        print("=" * 60)
        print(colored(f"{title}:", color))
        print(colored(tabulate(data, headers=headers, tablefmt="fancy_grid"), color))

def main():
    # Define configurations for different scenarios
    scenarios = [
        ([1], [1], [2], 2),
        ([1], [1], [7], 2),
        # ([2], [1], [2], 1),
        # ([1], [2], [2], 1)
    ]

    for num_observations, num_states, num_actions, policy_length in scenarios:
        scenario_description = (
            f"In this scenario, the agent navigates an environment with "
            f"{len(num_observations)} observation modality(ies), "
            f"{len(num_states)} hidden state(s), "
            f"{len(num_actions)} affordance(s), and a "
            f"decision-making horizon of {policy_length} timestep(s). "
            f"This setup challenges the agent to infer the best course of action "
            f"given its understanding of the world and its preferences."
        )
        print(f"\n{scenario_description}")
        agent = NestmateAgent(num_observations, num_states, num_actions, policy_length, inference_depth=1)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    main()
