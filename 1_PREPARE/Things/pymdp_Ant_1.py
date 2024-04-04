from pymdp import inference, control, utils
import numpy as np
from typing import List, Optional, Dict, Any

class AntAgent:
    """
    An agent that employs active inference for decision-making, based on a comprehensive model of its environment.
    """
    def __init__(self, observation_model: np.ndarray, transition_model: np.ndarray, preference_model: np.ndarray, initial_state_distribution: np.ndarray, policy_prior: Optional[np.ndarray] = None, policy_length: int = 1, inference_depth: int = 1, controllable_factors: Optional[List[int]] = None, possible_policies: Optional[np.ndarray] = None):
        """
        Initializes the AntAgent with detailed models of the environment and its preferences.

        :param observation_model (A): Maps observations to states (Sensory mapping, Likelihoods)
        :param transition_model (B): Describes state transitions (Dynamics, State evolution)
        :param preference_model (C): Encodes preferences over observations (Goals, Desires)
        :param initial_state_distribution (D): Prior beliefs about initial states (Starting point, Beliefs)
        :param policy_prior (E): Prior beliefs over policies (Action tendencies, Strategy preferences)
        :param policy_length: Consideration span of policies
        :param inference_depth: Depth of future state consideration
        :param controllable_factors: Indices of factors the agent can control
        :param possible_policies: Explicit set of policies to consider
        """
        # Define the components of the generative model with clear terminology
        self.observation_model = utils.to_obj_array(observation_model)  # Sensory mapping
        self.transition_model = utils.to_obj_array(transition_model)  # State dynamics
        self.preference_model = preference_model  # Goals
        initial_state_distribution = self._initialize_alternate_initial_state_distribution()  # Starting beliefs
        self.initial_state_distribution = initial_state_distribution
        policy_prior = self._introduce_policy_prior_modifications()  # Strategy preferences
        self.policy_prior = policy_prior
        
        self.generative_model = {
            'observation_model': self.observation_model,
            'transition_model': self.transition_model,
            'preference_model': self.preference_model,
            'initial_state_distribution': self.initial_state_distribution,
            'policy_prior': self.policy_prior
        }
        
        self.model_dimensions = self._calculate_model_dimensions()

        self.posterior_states = self.initial_state_distribution  # Initialize beliefs about states
        self.policy_length = policy_length
        self.inference_depth = inference_depth
        self.controllable_factors = controllable_factors or list(range(self.model_dimensions['num_factors']))
        self.possible_policies = possible_policies or self._define_possible_policies()

    def _calculate_model_dimensions(self) -> Dict[str, Any]:
        """
        Determines the dimensions of the models for subsequent operations.
        """
        num_observations = [model.shape[0] for model in self.observation_model]
        num_states = [model.shape[0] for model in self.transition_model]
        return {
            'num_observations': num_observations,
            'num_states': num_states,
            'num_modalities': len(num_observations),
            'num_factors': len(num_states)
        }

    def _define_possible_policies(self) -> np.ndarray:
        """
        Generates the set of feasible policies based on the agent's models.
        """
        return control.construct_policies(self.model_dimensions['num_states'], self.model_dimensions['num_factors'], self.policy_length, self.controllable_factors)

    def update_beliefs_about_states(self, observation: np.ndarray) -> None:
        """
        Revises the agent's beliefs regarding hidden states upon receiving new observations.
        """
        self.posterior_states = inference.update_posterior_states(self.observation_model, observation, self.transition_model, self.posterior_states, self.policy_length, self.inference_depth)

    def update_beliefs_about_policies(self) -> None:
        """
        Refines the agent's beliefs over policies, integrating current states and model insights.
        """
        updated_policies, _ = control.update_posterior_policies(self.posterior_states, self.observation_model, self.transition_model, self.preference_model, self.possible_policies, self.policy_prior)
        self.updated_policies = updated_policies

    def choose_action(self) -> np.ndarray:
        """
        Determines an action based on the agent's current policy beliefs.
        """
        return control.sample_action(self.updated_policies, self.possible_policies, self.model_dimensions['num_factors'], self.controllable_factors)

    def execute_step(self, observation: np.ndarray) -> np.ndarray:
        """
        Conducts a single action selection cycle based on a new observation.
        """
        self.update_beliefs_about_states(observation)  
        self.update_beliefs_about_policies()
        return self.choose_action()
