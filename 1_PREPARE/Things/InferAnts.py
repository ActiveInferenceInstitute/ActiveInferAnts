import numpy as np
import config
from typing import Dict, Any, Tuple, Callable, List, Optional
from scipy.stats import entropy
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class AgentConfig:
    """
    Data class for agent-specific configurations.
    """
    possible_actions: List[np.ndarray] = field(default_factory=list)
    pheromone_levels: Dict[str, float] = field(default_factory=dict)
    sounds: List[Dict[str, Any]] = field(default_factory=list)
    # Add other configuration parameters as needed

class ActiveInferenceAgent(ABC):
    def __init__(self, position: np.ndarray, influence_factor: float, **agent_params: Dict[str, Any]):
        """
        Initializes an active inference agent with specified parameters and matrices.

        Args:
            position (np.ndarray): Initial position of the agent.
            influence_factor (float): Influence factor for agent's actions.
            **agent_params (Dict[str, Any]): Additional parameters for agent configuration.
        """
        self.position = position
        self.influence_factor = influence_factor
        self.agent_params = agent_params
        self.initialize_matrices()
        self._initialize_specific_config()

    def initialize_matrices(self) -> None:
        """
        Initializes matrices based on agent parameters.
        """
        self.A_matrix = self._initialize_matrix('A_matrix_config', self.agent_params.get('SENSORY_MODALITIES', ()), self.agent_params.get('OBSERVATION_DIM', 0))
        self.B_matrix = self._initialize_matrix('B_matrix_config', self.agent_params.get('ACTION_MODALITIES', ()), self.agent_params.get('STATE_DIM', 0), self.agent_params.get('STATE_DIM', 0))
        self.C_matrix = self._initialize_matrix('C_matrix_config', self.agent_params.get('OBSERVATION_DIM', 0))
        self.D_matrix = self._initialize_matrix('D_matrix_config', self.agent_params.get('STATE_DIM', 0))
        self.pi_matrix = self._initialize_matrix('pi_matrix_config', self.agent_params.get('ACTION_MODALITIES', ()), self.agent_params.get('STATE_DIM', 0))

    def _initialize_matrix(self, config_key: str, *dims) -> np.ndarray:
        """
        Helper method to initialize a matrix based on a configuration key and dimensions.

        Raises:
            ValueError: If matrix dimensions are invalid.
        """
        matrix_config = self.agent_params.get(config_key, np.zeros(dims, dtype=np.float32))
        try:
            matrix = np.array(matrix_config(*dims) if callable(matrix_config) else matrix_config, dtype=np.float32)
        except Exception as e:
            logger.error(f"Error initializing matrix '{config_key}': {e}")
            raise ValueError(f"Invalid configuration for matrix '{config_key}'.") from e

        if matrix.shape != dims:
            logger.error(f"Matrix '{config_key}' has incorrect dimensions. Expected {dims}, got {matrix.shape}.")
            raise ValueError(f"Matrix '{config_key}' has incorrect dimensions.")
        
        logger.debug(f"Initialized matrix '{config_key}' with shape {matrix.shape}.")
        return matrix

    def perceive(self, observations: np.ndarray) -> None:
        """
        Updates agent's beliefs based on new observations.

        Args:
            observations (np.ndarray): New sensory observations.
        """
        perception_strategy = self.agent_params.get('perception_strategy', self._default_perception_strategy)
        prediction_error = perception_strategy(observations, self)
        self._update_beliefs(prediction_error)

    def _default_perception_strategy(self, observations: np.ndarray, agent: 'ActiveInferenceAgent') -> np.ndarray:
        """
        Default perception strategy.

        Args:
            observations (np.ndarray): New sensory observations.
            agent (ActiveInferenceAgent): The agent itself.

        Returns:
            np.ndarray: Prediction error.
        """
        return observations - agent._predict_sensory_outcomes()

    def _predict_sensory_outcomes(self) -> np.ndarray:
        """
        Predicts sensory outcomes based on the agent's current position.

        Returns:
            np.ndarray: Predicted sensory outcomes.
        """
        return np.dot(self.A_matrix, self.position)

    def _update_beliefs(self, prediction_error: np.ndarray) -> None:
        """
        Updates the agent's beliefs based on the prediction error.

        Args:
            prediction_error (np.ndarray): Prediction error.
        """
        self.position -= self.influence_factor * prediction_error

    def calculate_vfe(self, observation: np.ndarray) -> float:
        """
        Calculates the Variational Free Energy for a given observation.

        Args:
            observation (np.ndarray): Observation.

        Returns:
            float: Variational Free Energy.
        """
        qs = self._approximate_posterior(observation)
        expected_log_likelihood = np.sum(qs * np.log(np.clip(self.A_matrix[:, observation], 1e-10, None)))
        kl_divergence = np.sum(qs * (np.log(np.clip(qs, 1e-10, None)) - np.log(np.clip(self.position, 1e-10, None))))
        return -(expected_log_likelihood - kl_divergence)

    def calculate_efe(self, action: np.ndarray, future_states: np.ndarray, preferences: np.ndarray, uncertainty: float) -> float:
        """
        Calculates the Expected Free Energy for a given action.

        Args:
            action (np.ndarray): Action.
            future_states (np.ndarray): Future states.
            preferences (np.ndarray): Preferences.
            uncertainty (float): Uncertainty.

        Returns:
            float: Expected Free Energy.
        """
        pragmatic_value = np.sum(future_states * (np.log(np.clip(future_states, 1e-10, None)) - np.log(np.clip(preferences, 1e-10, None))))
        epistemic_value = entropy(future_states)
        return pragmatic_value + uncertainty * epistemic_value

    def decide_next_action(self) -> np.ndarray:
        """
        Decides the next action based on Expected Free Energy scores.

        Returns:
            np.ndarray: The chosen action.
        """
        possible_actions = self._generate_possible_actions()
        efe_scores = np.array([self.calculate_efe(
            action,
            self._predict_future_states(action),
            self.agent_params.get('preferences', np.zeros(self.position.shape)),
            self.agent_params.get('uncertainty', 0.1)
        ) for action in possible_actions])
        return possible_actions[np.argmin(efe_scores)]

    @abstractmethod
    def _generate_possible_actions(self) -> np.ndarray:
        """
        Generates possible actions for the agent.

        Returns:
            np.ndarray: Possible actions.
        """
        pass

    @abstractmethod
    def _predict_future_states(self, action: np.ndarray) -> np.ndarray:
        """
        Predicts future states based on a given action.

        Args:
            action (np.ndarray): Action.

        Returns:
            np.ndarray: Predicted future states.
        """
        pass

    @abstractmethod
    def _approximate_posterior(self, observation: np.ndarray) -> np.ndarray:
        """
        Approximates the posterior distribution given an observation.

        Args:
            observation (np.ndarray): Observation.

        Returns:
            np.ndarray: Approximated posterior.
        """
        pass

    def update_internal_states(self, action: np.ndarray, observation: np.ndarray) -> None:
        """
        Updates the agent's internal states based on action and observation.

        Args:
            action (np.ndarray): Action taken by the agent.
            observation (np.ndarray): New observation received.
        """
        self._update_action_model(action, observation)
        self._update_observation_model(observation)

    def _update_action_model(self, action: np.ndarray, observation: np.ndarray) -> None:
        """
        Updates the action model based on the taken action and new observation.

        Args:
            action (np.ndarray): Action taken by the agent.
            observation (np.ndarray): New observation received.
        """
        self.B_matrix += np.outer(action, observation)

    def _update_observation_model(self, observation: np.ndarray) -> None:
        """
        Updates the observation model based on the new observation.

        Args:
            observation (np.ndarray): New observation received.
        """
        self.A_matrix += np.outer(observation, observation)

    def move(self, direction: np.ndarray) -> None:
        """
        Updates the agent's position based on the chosen direction.

        Args:
            direction (np.ndarray): Direction to move in.
        """
        self.position += direction

    @abstractmethod
    def release_pheromone(self, pheromone_type: str, rate: float) -> None:
        """
        Releases pheromone of a specified type at a specified rate.

        Args:
            pheromone_type (str): Type of pheromone.
            rate (float): Rate of pheromone release.
        """
        pass

    @abstractmethod
    def produce_sound(self, sound_type: str, intensity: float) -> None:
        """
        Produces sound of a specified type with a specified intensity.

        Args:
            sound_type (str): Type of sound.
            intensity (float): Intensity of the sound.
        """
        pass

    def _get_specific_config(self) -> Dict[str, Any]:
        """
        Retrieves the specific configuration for the agent subclass.

        Returns:
            Dict[str, Any]: Configuration dictionary.
        """
        raise NotImplementedError("Subclasses must implement this method.")

    def _initialize_specific_config(self) -> None:
        """
        Initializes specific configuration sections ensuring required keys exist.
        """
        specific_config = self._get_specific_config()
        specific_config.possible_actions = specific_config.possible_actions or []
        specific_config.pheromone_levels = specific_config.pheromone_levels or {}
        specific_config.sounds = specific_config.sounds or []
        self.agent_params[self._config_key()] = specific_config
        logger.debug(f"Initialized specific config for {self._config_key()}: {specific_config}")

    @abstractmethod
    def _config_key(self) -> str:
        """
        Returns the configuration key for the agent subclass.

        Returns:
            str: Configuration key.
        """
        pass

    def release_pheromone(self, pheromone_type: str, rate: float) -> None:
        """
        Releases pheromone of a specified type at a specified rate.

        Args:
            pheromone_type (str): Type of pheromone.
            rate (float): Rate of pheromone release.
        """
        pheromone_levels = self._get_specific_config().pheromone_levels
        previous_level = pheromone_levels.get(pheromone_type, 0)
        pheromone_levels[pheromone_type] = previous_level + rate
        logger.info(f"Released pheromone '{pheromone_type}' at rate {rate}. Total level: {pheromone_levels[pheromone_type]}")

    def produce_sound(self, sound_type: str, intensity: float) -> None:
        """
        Produces sound of a specified type with a specified intensity.

        Args:
            sound_type (str): Type of sound.
            intensity (float): Intensity of the sound.
        """
        sound = {'type': sound_type, 'intensity': intensity}
        self._get_specific_config().sounds.append(sound)
        logger.info(f"Produced sound '{sound_type}' with intensity {intensity}.")

class ActiveColony(ActiveInferenceAgent):
    def __init__(self, position: np.ndarray, influence_factor: float, **agent_params: Dict[str, Any]):
        super().__init__(position, influence_factor, **agent_params)
        self.colony_config = AgentConfig(**config.ANT_AND_COLONY_CONFIG['COLONY'])
        logger.debug("Initialized ActiveColony with configuration.")

    def _config_key(self) -> str:
        return 'COLONY'

    def _get_specific_config(self) -> Dict[str, Any]:
        return self.colony_config

    def _generate_possible_actions(self) -> np.ndarray:
        """
        Generates possible actions based on colony behavior patterns.

        Returns:
            np.ndarray: Possible actions.
        """
        actions = self.colony_config.possible_actions
        logger.debug(f"ActiveColony possible actions: {actions}")
        return np.array(actions)

    def _predict_future_states(self, action: np.ndarray) -> np.ndarray:
        """
        Predicts future states using colony-specific state transition model.

        Args:
            action (np.ndarray): Action.

        Returns:
            np.ndarray: Predicted future states.
        """
        predicted_state = self.B_matrix @ action + self.position
        logger.debug(f"ActiveColony predicted future state: {predicted_state}")
        return predicted_state

    def _approximate_posterior(self, observation: np.ndarray) -> np.ndarray:
        """
        Approximates posterior using Bayesian update for colony.

        Args:
            observation (np.ndarray): Observation.

        Returns:
            np.ndarray: Approximated posterior.
        """
        posterior = self.position + self.C_matrix @ observation
        logger.debug(f"ActiveColony approximated posterior: {posterior}")
        return posterior

class ActiveNestmate(ActiveInferenceAgent):
    def __init__(self, position: np.ndarray, influence_factor: float, **agent_params: Dict[str, Any]):
        super().__init__(position, influence_factor, **agent_params)
        self.nestmate_config = AgentConfig(**config.ANT_AND_COLONY_CONFIG['NESTMATE'])
        logger.debug("Initialized ActiveNestmate with configuration.")

    def _config_key(self) -> str:
        return 'NESTMATE'

    def _get_specific_config(self) -> Dict[str, Any]:
        return self.nestmate_config

    def _generate_possible_actions(self) -> np.ndarray:
        """
        Generates possible actions based on nestmate behavior patterns.

        Returns:
            np.ndarray: Possible actions.
        """
        actions = self.nestmate_config.possible_actions
        logger.debug(f"ActiveNestmate possible actions: {actions}")
        return np.array(actions)

    def _predict_future_states(self, action: np.ndarray) -> np.ndarray:
        """
        Predicts future states using nestmate-specific state transition model.

        Args:
            action (np.ndarray): Action.

        Returns:
            np.ndarray: Predicted future states.
        """
        predicted_state = self.B_matrix @ action + self.position
        logger.debug(f"ActiveNestmate predicted future state: {predicted_state}")
        return predicted_state

    def _approximate_posterior(self, observation: np.ndarray) -> np.ndarray:
        """
        Approximates posterior using Bayesian update for nestmate.

        Args:
            observation (np.ndarray): Observation.

        Returns:
            np.ndarray: Approximated posterior.
        """
        posterior = self.position + self.C_matrix @ observation
        logger.debug(f"ActiveNestmate approximated posterior: {posterior}")
        return posterior
