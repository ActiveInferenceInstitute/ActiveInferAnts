from pymdp import inference, control, utils
import numpy as np
from typing import List, Optional, Dict, Any, Tuple
from autograd import numpy as np_auto
from scipy.stats import entropy
import logging

class Thing:
    """
    A sophisticated Thing class that employs active inference principles for decision-making and learning.
    
    This class leverages the pymdp library to implement Bayesian inference techniques and 
    information-theoretic measures for adaptive interaction with its environment. It maintains
    and updates complex internal models, allowing for nuanced perception and action selection.
    """

    def __init__(self, 
                 observation_model: np.ndarray, 
                 transition_model: np.ndarray, 
                 preference_model: np.ndarray, 
                 initial_state_distribution: np.ndarray, 
                 policy_prior: Optional[np.ndarray] = None, 
                 policy_length: int = 1, 
                 inference_depth: int = 1, 
                 controllable_factors: Optional[List[int]] = None, 
                 possible_policies: Optional[np.ndarray] = None, 
                 learning_rate: float = 0.1):
        """
        Initializes the Thing with comprehensive models of its environment and preferences.

        Args:
            observation_model (np.ndarray): Likelihood mapping from hidden states to observations.
            transition_model (np.ndarray): Dynamics model describing state transitions.
            preference_model (np.ndarray): Encoded preferences over observations.
            initial_state_distribution (np.ndarray): Prior beliefs about initial states.
            policy_prior (Optional[np.ndarray]): Prior beliefs over policies.
            policy_length (int): Temporal horizon for policy consideration.
            inference_depth (int): Depth of recursive inference for state estimation.
            controllable_factors (Optional[List[int]]): Indices of controllable state factors.
            possible_policies (Optional[np.ndarray]): Set of feasible policies to consider.
            learning_rate (float): Rate of model updates based on experience.
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
        self.learning_rate = learning_rate

        self.generative_model = self._construct_generative_model()
        self.model_dimensions = self._calculate_model_dimensions()
        self.posterior_states = self.initial_state_distribution.copy()
        self.updated_policies = None
        self.action_history = []
        self.observation_history = []

        self.logger = self._setup_logger()

    def _setup_logger(self) -> logging.Logger:
        """
        Configures and returns a logger for the Thing instance.

        Returns:
            logging.Logger: Configured logger object.
        """
        logger = logging.getLogger(f"{__name__}.{id(self)}")
        logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger

    def _construct_generative_model(self) -> Dict[str, Any]:
        """
        Assembles the generative model from component parts.

        Returns:
            Dict[str, Any]: Comprehensive generative model of the environment.
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
        Computes the dimensions of various model components.

        Returns:
            Dict[str, Any]: Dimensions of observations, states, modalities, and factors.
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
        Initializes a uniform prior over policies.

        Returns:
            np.ndarray: Uniform policy prior.
        """
        return np.ones((self.policy_length, len(self.controllable_factors))) / self.policy_length

    def _identify_controllable_factors(self) -> List[int]:
        """
        Identifies controllable factors based on transition model structure.

        Returns:
            List[int]: Indices of controllable factors.
        """
        return [i for i, model in enumerate(self.transition_model) if np.any(model != model[0])]

    def _generate_possible_policies(self) -> np.ndarray:
        """
        Generates all possible policies given the model dimensions and controllable factors.

        Returns:
            np.ndarray: Array of possible policies.
        """
        return control.construct_policies(
            self.model_dimensions['num_states'], 
            self.model_dimensions['num_factors'], 
            self.policy_length, 
            self.controllable_factors
        )

    def update_beliefs(self, observation: np.ndarray) -> None:
        """
        Updates beliefs about hidden states and policies based on new observations.

        Args:
            observation (np.ndarray): New sensory observation.
        """
        self.logger.info("Updating beliefs based on new observation")
        self.posterior_states = inference.update_posterior_states(
            self.observation_model, observation, self.transition_model, 
            self.posterior_states, self.policy_length, self.inference_depth
        )
        self.updated_policies, _ = control.update_posterior_policies(
            self.posterior_states, self.observation_model, self.transition_model, 
            self.preference_model, self.possible_policies, self.policy_prior
        )
        self.observation_history.append(observation)

    def select_action(self) -> np.ndarray:
        """
        Selects an action based on current beliefs and updated policies.

        Returns:
            np.ndarray: Selected action.
        """
        self.logger.info("Selecting action based on current beliefs and policies")
        action = control.sample_action(
            self.updated_policies, self.possible_policies, 
            self.model_dimensions['num_factors'], self.controllable_factors
        )
        self.action_history.append(action)
        return action

    def step(self, observation: np.ndarray) -> np.ndarray:
        """
        Executes a full decision-making cycle: perception, action selection, and learning.

        Args:
            observation (np.ndarray): New sensory observation.

        Returns:
            np.ndarray: Selected action.
        """
        self.logger.info("Executing decision-making cycle")
        self.update_beliefs(observation)
        action = self.select_action()
        self._update_models()
        return action
    
    def calculate_vfe(self, observation: np.ndarray) -> float:
        """
        Calculates the Variational Free Energy (VFE) for a given observation.

        Args:
            observation (np.ndarray): Observed sensory data.

        Returns:
            float: Calculated VFE.
        """
        qs = self.posterior_states
        obs_index = np_auto.argmax(observation)
        
        likelihood = self.observation_model[obs_index, :]
        prior = self.initial_state_distribution
        
        joint = likelihood * prior
        vfe = qs.dot(np_auto.log(qs) - np_auto.log(joint))
        
        self.logger.debug(f"Calculated VFE: {vfe}")
        return vfe

    def calculate_efe(self, policy: np.ndarray) -> float:
        """
        Calculates the Expected Free Energy (EFE) for a given policy.

        Args:
            policy (np.ndarray): Policy to evaluate.

        Returns:
            float: Calculated EFE.
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
        
        self.logger.debug(f"Calculated EFE for policy: {efe}")
        return efe

    def simulate_future(self, policy: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """
        Simulates future states and observations based on a given policy.

        Args:
            policy (np.ndarray): Policy to simulate.

        Returns:
            Tuple[np.ndarray, np.ndarray]: Predicted future states and observations.
        """
        future_states = np.zeros(self.model_dimensions['num_states'])
        future_observations = np.zeros(self.model_dimensions['num_observations'])
        
        current_state = self.posterior_states
        for action in policy:
            next_state = np.dot(self.transition_model[action], current_state)
            future_states += next_state
            
            predicted_obs = np.dot(self.observation_model, next_state)
            future_observations += predicted_obs
            
            current_state = next_state
        
        return future_states, future_observations

    def _update_models(self) -> None:
        """
        Updates internal models based on recent experiences.
        """
        if len(self.observation_history) > 1:
            prev_obs = self.observation_history[-2]
            curr_obs = self.observation_history[-1]
            action = self.action_history[-1]
            
            self.transition_model[action] += self.learning_rate * (np.outer(curr_obs, prev_obs) - self.transition_model[action])
            self.observation_model += self.learning_rate * (np.outer(curr_obs, self.posterior_states) - self.observation_model)
            
            self.transition_model[action] /= np.sum(self.transition_model[action], axis=1, keepdims=True)
            self.observation_model /= np.sum(self.observation_model, axis=1, keepdims=True)

            self.logger.info("Updated internal models based on recent experiences")

    def calculate_information_gain(self, policy: np.ndarray) -> float:
        """
        Calculates the expected information gain for a given policy.

        Args:
            policy (np.ndarray): Policy to evaluate.

        Returns:
            float: Expected information gain.
        """
        prior_entropy = entropy(self.posterior_states)
        future_states, _ = self.simulate_future(policy)
        posterior_entropy = entropy(future_states)
        info_gain = prior_entropy - posterior_entropy
        self.logger.debug(f"Calculated information gain for policy: {info_gain}")
        return info_gain

    def calculate_complexity(self) -> float:
        """
        Calculates the complexity of the current internal model.

        Returns:
            float: Model complexity measure.
        """
        complexity = np.sum([np.sum(model * np.log(model)) for model in self.transition_model])
        self.logger.debug(f"Calculated model complexity: {complexity}")
        return complexity

    def adaptive_learning_rate(self) -> None:
        """
        Adapts the learning rate based on recent performance.
        """
        recent_vfe = [self.calculate_vfe(obs) for obs in self.observation_history[-10:]]
        if np.mean(recent_vfe) < 0.1:
            self.learning_rate *= 0.9
        else:
            self.learning_rate *= 1.1
        self.learning_rate = np.clip(self.learning_rate, 0.01, 1.0)
        self.logger.info(f"Adapted learning rate to: {self.learning_rate}")

    def reset(self) -> None:
        """
        Resets the Thing's internal state to initial conditions.
        """
        self.posterior_states = self.initial_state_distribution.copy()
        self.action_history.clear()
        self.observation_history.clear()
        self.updated_policies = None
        self.logger.info("Reset internal state to initial conditions")

    def get_state(self) -> Dict[str, Any]:
        """
        Returns a dictionary representation of the Thing's current state.

        Returns:
            Dict[str, Any]: Current state of the Thing.
        """
        return {
            'posterior_states': self.posterior_states,
            'action_history': self.action_history,
            'observation_history': self.observation_history,
            'learning_rate': self.learning_rate
        }

    def set_state(self, state: Dict[str, Any]) -> None:
        """
        Sets the Thing's state based on a provided dictionary.

        Args:
            state (Dict[str, Any]): State to set for the Thing.
        """
        self.posterior_states = state['posterior_states']
        self.action_history = state['action_history']
        self.observation_history = state['observation_history']
        self.learning_rate = state['learning_rate']
        self.logger.info("Set internal state from provided dictionary")
