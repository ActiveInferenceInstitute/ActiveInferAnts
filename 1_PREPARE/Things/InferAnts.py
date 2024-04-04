import numpy as np
import config
from typing import Dict, Any
from scipy.stats import entropy

class MatrixInitializer:
    """
    A class to efficiently initialize matrices based on configuration or default to zeros.
    """
    @staticmethod
    def initialize(config_key: str, agent_params: Dict[str, Any], *dims) -> np.ndarray:
        """
        Efficiently initializes a matrix based on a configuration key and agent parameters.

        :param config_key: Configuration key for the matrix.
        :param agent_params: Agent parameters containing configuration.
        :param dims: Dimensions for the matrix.
        :return: A numpy array representing the initialized matrix.
        """
        return agent_params.get(config_key, np.zeros(dims, dtype=np.float32))

class ActiveInferenceAgent:
    def __init__(self, position: np.ndarray, influence_factor: float, **agent_params: Dict[str, Any]):
        """
        Initializes an active inference agent with specified parameters and matrices.

        :param position: Initial position of the agent in a numpy array.
        :param influence_factor: Influence factor for agent's actions as a float.
        :param agent_params: Additional parameters for agent configuration as a dictionary.
        """
        self.position = position
        self.influence_factor = influence_factor
        self.agent_params = agent_params
        self.A_matrix = MatrixInitializer.initialize('A_matrix_config', agent_params, *agent_params.get('SENSORY_MODALITIES'), agent_params.get('OBSERVATION_DIM'))
        self.B_matrix = MatrixInitializer.initialize('B_matrix_config', agent_params, *agent_params.get('ACTION_MODALITIES'), agent_params.get('STATE_DIM'), agent_params.get('STATE_DIM'))
        self.C_matrix = MatrixInitializer.initialize('C_matrix_config', agent_params, agent_params.get('OBSERVATION_DIM'))
        self.D_matrix = MatrixInitializer.initialize('D_matrix_config', agent_params, agent_params.get('STATE_DIM'))

    def perceive(self, observations: np.ndarray):
        """
        Updates agent's beliefs based on new observations.

        :param observations: New sensory observations as a numpy array.
        """
        prediction_error = self.agent_params.get('perception_strategy', lambda obs, agent: obs - agent._predict_sensory_outcomes())(observations, self)
        self._update_beliefs(prediction_error)

    def _predict_sensory_outcomes(self) -> np.ndarray:
        """
        Predicts sensory outcomes based on the agent's current position.

        :return: A numpy array of predicted sensory outcomes.
        """
        return np.dot(self.A_matrix, self.position)

    def _update_beliefs(self, prediction_error: np.ndarray):
        """
        Updates the agent's position based on the prediction error.

        :param prediction_error: Prediction error as a numpy array.
        """
        self.position -= self.influence_factor * prediction_error

    def calculate_vfe(self, observation: np.ndarray) -> float:
        """
        Calculates the Variational Free Energy for a given observation.

        :param observation: Observation as a numpy array.
        :return: Variational Free Energy as a float.
        """
        qs = self._approximate_posterior(observation)
        expected_log_likelihood = np.sum(qs * np.log(self.A_matrix[:, observation]))
        kl_divergence = np.sum(qs * (np.log(qs) - np.log(self.position)))
        vfe = -(expected_log_likelihood - kl_divergence)
        return vfe

    def calculate_efe(self, action: np.ndarray, future_states: np.ndarray, preferences: np.ndarray, uncertainty: float) -> float:
        """
        Calculates the Expected Free Energy for a given action.

        :param action: Action as a numpy array.
        :param future_states: Future states as a numpy array.
        :param preferences: Preferences as a numpy array.
        :param uncertainty: Uncertainty as a float.
        :return: Expected Free Energy as a float.
        """
        pragmatic_value = np.sum(future_states * (np.log(future_states) - np.log(preferences)))
        epistemic_value = entropy(future_states)
        efe = pragmatic_value + uncertainty * epistemic_value
        return efe

    def decide_next_action(self) -> np.ndarray:
        """
        Decides the next action based on Expected Free Energy scores.

        :return: The chosen action as a numpy array.
        """
        possible_actions = self._generate_possible_actions()
        efe_scores = np.array([self.calculate_efe(action, self._predict_future_states(action), self.agent_params.get('preferences'), self.agent_params.get('uncertainty', 0.1)) for action in possible_actions])
        return possible_actions[np.argmin(efe_scores)]

    def update_internal_states(self, action: np.ndarray, observation: np.ndarray):
        """
        Updates the agent's internal states based on action and observation.

        :param action: Action taken by the agent as a numpy array.
        :param observation: New observation received as a numpy array.
        """
        self._update_action_model(action, observation)
        self._update_observation_model(observation)

    def _update_action_model(self, action: np.ndarray, observation: np.ndarray):
        """
        Updates the action model based on the taken action and new observation.

        :param action: Action taken by the agent as a numpy array.
        :param observation: New observation received as a numpy array.
        """
        self.B_matrix += np.outer(action, observation)

    def _update_observation_model(self, observation: np.ndarray):
        """
        Updates the observation model based on the new observation.

        :param observation: New observation received as a numpy array.
        """
        self.A_matrix += np.outer(observation, observation)

    def move(self, direction: np.ndarray):
        """
        Updates the agent's position based on the chosen direction.

        :param direction: Direction to move in as a numpy array.
        """
        self.position += direction

    def release_pheromone(self, type: str, rate: float):
        """
        Releases pheromone of a specified type at a specified rate.

        :param type: Type of pheromone as a string.
        :param rate: Rate of pheromone release as a float.
        """
        pass

    def produce_sound(self, type: str, intensity: float):
        """
        Produces sound of a specified type with a specified intensity.

        :param type: Type of sound as a string.
        :param intensity: Intensity of the sound as a float.
        """
        pass

class ActiveColony(ActiveInferenceAgent):
    def __init__(self, position: np.ndarray, influence_factor: float, **agent_params: Dict[str, Any]):
        super().__init__(position, influence_factor, **agent_params)
        self.colony_config = config.ANT_AND_COLONY_CONFIG['COLONY']

class ActiveNestmate(ActiveInferenceAgent):
    def __init__(self, position: np.ndarray, influence_factor: float, **agent_params: Dict[str, Any]):
        super().__init__(position, influence_factor, **agent_params)
        self.nestmate_config = config.ANT_AND_COLONY_CONFIG['NESTMATE']


