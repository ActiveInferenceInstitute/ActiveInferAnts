from pymdp import inference, control, utils
import numpy as np
from typing import List, Optional, Dict, Any
from autograd import numpy as np_auto

class Thing:
    """
    A Thing class that utilizes active inference, leveraging the pymdp library for interaction with its environment.
    """
    def __init__(self, observation_model: np.ndarray, transition_model: np.ndarray, preference_model: np.ndarray, initial_state_distribution: np.ndarray, policy_prior: Optional[np.ndarray] = None, policy_length: int = 1, inference_depth: int = 1, controllable_factors: Optional[List[int]] = None, possible_policies: Optional[np.ndarray] = None):
        """
        Initializes the Thing with models of the environment, preferences, and initial states.
        """
        self.observation_model = utils.to_obj_array(observation_model)
        self.transition_model = utils.to_obj_array(transition_model)
        self.preference_model = preference_model
        self.initial_state_distribution = initial_state_distribution
        self.policy_prior = policy_prior if policy_prior is not None else self._initialize_policy_prior()
        self.policy_length = policy_length
        self.inference_depth = inference_depth
        self.controllable_factors = controllable_factors if controllable_factors is not None else self._identify_controllable_factors()
        self.possible_policies = possible_policies if possible_policies is not None else self._generate_possible_policies()

        self.generative_model = self._construct_generative_model()
        self.model_dimensions = self._calculate_model_dimensions()
        self.posterior_states = self.initial_state_distribution
        self.updated_policies = None

    def _construct_generative_model(self) -> Dict[str, Any]:
        """
        Constructs a generative model incorporating the Thing's environment and preferences.
        """
        return {
            'observation_model': self.observation_model,
            'transition_model': self.transition_model,
            'preference_model': self.preference_model,
            'initial_state_distribution': self.initial_state_distribution,
            'policy_prior': self.policy_prior
        }

    def _calculate_model_dimensions(self) -> Dict[str, Any]:
        """
        Calculates the dimensions of the generative model's components.
        """
        num_observations = [model.shape[0] for model in self.observation_model]
        num_states = [model.shape[0] for model in self.transition_model]
        return {
            'num_observations': num_observations,
            'num_states': num_states,
            'num_modalities': len(num_observations),
            'num_factors': len(num_states)
        }

    def _initialize_policy_prior(self) -> np.ndarray:
        """
        Initializes a policy prior based on the controllable factors and policy length.
        """
        return np.ones((self.policy_length, len(self.controllable_factors))) / self.policy_length

    def _identify_controllable_factors(self) -> List[int]:
        """
        Identifies controllable factors based on the transition model's dimensions.
        """
        return list(range(len(self.transition_model)))

    def _generate_possible_policies(self) -> np.ndarray:
        """
        Generates a set of possible policies based on the model dimensions and controllable factors.
        """
        return control.construct_policies(self.model_dimensions['num_states'], self.model_dimensions['num_factors'], self.policy_length, self.controllable_factors)

    def update_beliefs(self, observation: np.ndarray) -> None:
        """
        Updates the Thing's beliefs based on new observations.
        """
        self.posterior_states = inference.update_posterior_states(self.observation_model, observation, self.transition_model, self.posterior_states, self.policy_length, self.inference_depth)
        self.updated_policies, _ = control.update_posterior_policies(self.posterior_states, self.observation_model, self.transition_model, self.preference_model, self.possible_policies, self.policy_prior)

    def select_action(self) -> np.ndarray:
        """
        Selects an action based on the Thing's current beliefs and updated policies.
        """
        return control.sample_action(self.updated_policies, self.possible_policies, self.model_dimensions['num_factors'], self.controllable_factors)

    def step(self, observation: np.ndarray) -> np.ndarray:
        """
        Executes a decision-making cycle based on a new observation.
        """
        self.update_beliefs(observation)
        return self.select_action()
    
    def calculate_vfe(self, observation: np.ndarray) -> float:
        """
        Calculates the Variational Free Energy (VFE) given an observation.
        """
        qs = self.posterior_states
        obs_index = np_auto.argmax(observation)
        
        likelihood = self.observation_model[obs_index, :]
        prior = self.initial_state_distribution
        
        joint = likelihood * prior
        vfe = qs.dot(np_auto.log(qs) - np_auto.log(joint))
        
        return vfe

    def calculate_efe(self, policy: np.ndarray) -> float:
        """
        Calculates the Expected Free Energy (EFE) for a given policy.
        """
        future_states, future_observations = self.simulate_future(policy)
        
        preferences = self.preference_model
        
        efe = 0.0
        for obs in future_observations:
            for state in future_states:
                q_state = self.posterior_states[state]
                q_obs = future_observations[obs]
                p_desired = preferences[obs]
                
                efe_component = q_state * q_obs * (np_auto.log(q_state) - np_auto.log(p_desired))
                efe += efe_component
        
        return efe

    def simulate_future(self, policy: np.ndarray) -> (np.ndarray, np.ndarray):
        """
        Simulates future states and observations based on the given policy.
        """
        # Implementation to be defined based on transition_model and observation_model
        future_states = np.zeros(self.model_dimensions['num_states'])
        future_observations = np.zeros(self.model_dimensions['num_observations'])
        return future_states, future_observations
