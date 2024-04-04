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
        return [self._initialize_nest(nest_id, agent_count_per_nest) for nest_id in range(nest_count)]

    def _initialize_nest(self, nest_id: int, agent_count: int) -> List[ActiveNestmate]:
        positions = np.random.choice(self.env_config['NEST_POSITIONS'], size=agent_count, replace=False)
        return [self._initialize_single_nestmate(nest_id, nestmate_id, self._generate_developmental_parameters(), position) for nestmate_id, position in enumerate(positions)]

    def _initialize_single_nestmate(self, nest_id: int, nestmate_id: int, developmental_parameters: Dict[str, Any], position: Tuple[int, int]) -> ActiveNestmate:
        influence_factor = np.random.uniform(*self.ant_config['INFLUENCE_FACTOR_RANGE'])
        agent_params = {**self.meta_config['ACTIVE_INFERENCE'], **developmental_parameters}
        return ActiveNestmate(position=position, influence_factor=influence_factor, **agent_params)

    def _generate_developmental_parameters(self) -> Dict[str, Any]:
        return {
            'growth_rate': np.random.uniform(0.1, 1.0),
            'exploration_tendency': np.random.choice(['low', 'medium', 'high']),
        }
