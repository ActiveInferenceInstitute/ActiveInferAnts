import numpy as np
from InferAnts import ActiveNestmate
from typing import List, Dict, Any, Tuple, Optional
from .configs.config import config
from .configs.metaconfig import metaconfig
import logging
from dataclasses import dataclass

@dataclass
class DevelopmentalParameters:
    growth_rate: float
    exploration_tendency: str
    learning_rate: float
    adaptation_speed: float

    @staticmethod
    def generate() -> 'DevelopmentalParameters':
        return DevelopmentalParameters(
            growth_rate=np.random.uniform(0.1, 1.0),
            exploration_tendency=np.random.choice(['low', 'medium', 'high']),
            learning_rate=np.random.uniform(0.01, 0.1),
            adaptation_speed=np.random.uniform(0.5, 2.0),
        )

class InsufficientNestPositionsError(Exception):
    """Exception raised when there are not enough nest positions available."""
    pass

class ColonyInitializer:
    def __init__(self, env_config: Dict[str, Any], ant_config: Dict[str, Any], meta_config: Dict[str, Any], logger: Optional[logging.Logger] = None):
        self.env_config = env_config
        self.ant_config = ant_config
        self.meta_config = meta_config
        self.logger = logger or logging.getLogger(__name__)
        self._configure_logger()

    def _configure_logger(self):
        if not self.logger.hasHandlers():
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
            self.logger.setLevel(logging.DEBUG)

    def initialize_colony(self, nest_count: int, agent_count_per_nest: int) -> List[List[ActiveNestmate]]:
        """
        Initialize a colony with multiple nests and agents.

        Args:
            nest_count (int): Number of nests to initialize.
            agent_count_per_nest (int): Number of agents per nest.

        Returns:
            List[List[ActiveNestmate]]: A list of nests, each containing a list of ActiveNestmate agents.
        """
        return [self._initialize_nest(nest_id, agent_count_per_nest) for nest_id in range(nest_count)]

    def _initialize_nest(self, nest_id: int, agent_count: int) -> List[ActiveNestmate]:
        """
        Initialize a single nest with multiple agents.

        Args:
            nest_id (int): Unique identifier for the nest.
            agent_count (int): Number of agents to initialize in the nest.

        Returns:
            List[ActiveNestmate]: A list of initialized ActiveNestmate agents.
        """
        positions = self._select_positions(agent_count)
        return [
            self._initialize_single_nestmate(nest_id, nestmate_id, self._generate_developmental_parameters(), position)
            for nestmate_id, position in enumerate(positions)
        ]

    def _select_positions(self, agent_count: int) -> np.ndarray:
        """
        Select unique positions for agents within the nest.

        Args:
            agent_count (int): Number of positions to select.

        Returns:
            np.ndarray: Array of unique positions for agents.
        """
        available_positions = self.env_config.get('NEST_POSITIONS', [])
        if len(available_positions) < agent_count:
            self.logger.error("Not enough nest positions available.")
            raise InsufficientNestPositionsError("Insufficient nest positions for the number of agents.")
        return np.random.choice(available_positions, size=agent_count, replace=False)

    def _initialize_single_nestmate(self, nest_id: int, nestmate_id: int, developmental_parameters: DevelopmentalParameters, position: Tuple[int, int]) -> ActiveNestmate:
        """
        Initialize a single ActiveNestmate agent.

        Args:
            nest_id (int): Identifier of the nest the agent belongs to.
            nestmate_id (int): Unique identifier for the agent within the nest.
            developmental_parameters (DevelopmentalParameters): Parameters for agent development.
            position (Tuple[int, int]): Initial position of the agent.

        Returns:
            ActiveNestmate: An initialized ActiveNestmate agent.
        """
        influence_factor = self._select_influence_factor()
        agent_params = self._merge_parameters(vars(developmental_parameters))
        self.logger.debug(f"Initializing nestmate {nestmate_id} in nest {nest_id} at position {position} with params {agent_params}")
        return ActiveNestmate(
            nest_id=nest_id,
            nestmate_id=nestmate_id,
            position=position,
            influence_factor=influence_factor,
            **agent_params
        )

    def _select_influence_factor(self) -> float:
        """
        Select a random influence factor for an agent.

        Returns:
            float: A randomly selected influence factor within the configured range.
        """
        return np.random.uniform(*self.ant_config['INFLUENCE_FACTOR_RANGE'])

    def _merge_parameters(self, developmental_parameters: Dict[str, Any]) -> Dict[str, Any]:
        """
        Merge developmental parameters with active inference parameters.

        Args:
            developmental_parameters (Dict[str, Any]): Developmental parameters for the agent.

        Returns:
            Dict[str, Any]: Merged parameters for agent initialization.
        """
        return {**self.meta_config['ACTIVE_INFERENCE'], **developmental_parameters}

    def _generate_developmental_parameters(self) -> DevelopmentalParameters:
        self.logger.debug("Generating developmental parameters.")
        return DevelopmentalParameters.generate()
