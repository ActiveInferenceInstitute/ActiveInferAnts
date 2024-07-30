import numpy as np
from InferAnts import ActiveNestmate
from typing import List, Dict, Any, Tuple
from .configs.config import config
from .configs.metaconfig import metaconfig

class ColonyInitializer:
    def __init__(self, env_config: Dict[str, Any], ant_config: Dict[str, Any], meta_config: Dict[str, Any]):
        self.env_config = env_config
        self.ant_config = ant_config
        self.meta_config = meta_config

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
        return np.random.choice(self.env_config['NEST_POSITIONS'], size=agent_count, replace=False)

    def _initialize_single_nestmate(self, nest_id: int, nestmate_id: int, developmental_parameters: Dict[str, Any], position: Tuple[int, int]) -> ActiveNestmate:
        """
        Initialize a single ActiveNestmate agent.

        Args:
            nest_id (int): Identifier of the nest the agent belongs to.
            nestmate_id (int): Unique identifier for the agent within the nest.
            developmental_parameters (Dict[str, Any]): Parameters for agent development.
            position (Tuple[int, int]): Initial position of the agent.

        Returns:
            ActiveNestmate: An initialized ActiveNestmate agent.
        """
        influence_factor = self._select_influence_factor()
        agent_params = self._merge_parameters(developmental_parameters)
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

    def _generate_developmental_parameters(self) -> Dict[str, Any]:
        """
        Generate developmental parameters for an agent.

        Returns:
            Dict[str, Any]: A dictionary of developmental parameters.
        """
        return {
            'growth_rate': np.random.uniform(0.1, 1.0),
            'exploration_tendency': np.random.choice(['low', 'medium', 'high']),
            'learning_rate': np.random.uniform(0.01, 0.1),
            'adaptation_speed': np.random.uniform(0.5, 2.0),
        }
