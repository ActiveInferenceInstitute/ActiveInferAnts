import numpy as np

class MetaConfig:
    def __init__(self):
        self.config = self._initialize_config()

    def _initialize_config(self):
        return {
            'SIMULATION': self._simulation_config(),
            'ACTIVE_INFERENCE': self._active_inference_config(),
            'ANT_AND_COLONY': self._ant_and_colony_config(),
        }

    def _simulation_config(self):
        return {
            'MAX_STEPS_RANGE': (100, 1000),
            'AGENT_COUNT_RANGE': (50, 500),
            'NEST_COUNT_RANGE': (1, 10),
            'PARALLEL_EXECUTION_OPTIONS': [True, False],
            'WORKER_COUNT_RANGE': (1, 8),
            'PARALLELIZATION_STRATEGIES': ['distributed', 'multithreading'],
            'COMPUTATION': self._computation_config(),
        }

    def _computation_config(self):
        return {
            'GPU_ACCELERATION_OPTIONS': [True, False],
            'GPU_PREFERENCE_OPTIONS': ['high_performance', 'energy_saving'],
            'DISTRIBUTED_COMPUTING_OPTIONS': [True, False],
            'CLUSTER_NODE_COUNT_RANGE': (2, 16),
            'COMMUNICATION_PROTOCOLS': ['MPI', 'TCP/IP'],
        }

    def _active_inference_config(self):
        return {
            'INFERENCE_MODEL_OPTIONS': ['variational', 'predictive_coding', 'bayesian_filtering', 'deep_active_inference', 'ensemble_methods'],
            'PLANNING_HORIZON': self._planning_horizon_config(),
            'ADAPTIVE_LEARNING': self._adaptive_learning_config(),
            'CONTEXT_AWARENESS': self._context_awareness_config(),
            'PRECISION_WEIGHTING': self._precision_weighting_config(),
            'TIME_RESOLUTION_OPTIONS': ['discrete', 'continuous'],
            'PRECISION_WEIGHTING_RANGE': (0.1, 1.0),
            'GENERALIZATION_DEPTH_RANGE': (1, 10),
            'ITERATION_LIMIT_RANGE': (10, 50),
            'LEARNING_RATE_RANGE': (0.01, 0.5),
            'FEEDBACK_SENSITIVITY_OPTIONS': ['fixed', 'adaptive'],
            'MODEL_UPDATING_OPTIONS': ['online', 'batch'],
            'CONTEXT_TYPES': ['environmental', 'social', 'temporal', 'emotional'],
            'COGNITIVE_COMPLEXITY_TYPES': ['simple', 'complex', 'hierarchical', 'emergent', 'adaptive'],
            'GOAL_TYPES': ['survival', 'exploration', 'social_interaction'],
            'EXPECTATION_FREE_ENERGY_OPTIONS': [True, False],
        }

    def _planning_horizon_config(self):
        return {
            'TYPE_OPTIONS': ['fixed', 'adaptive'],
            'FIXED_RANGE': (5, 30),
            'ADAPTIVE_STRATEGY_OPTIONS': ['contextual_complexity'],
        }

    def _adaptive_learning_config(self):
        return {
            'ENABLED': [True, False],
            'LEARNING_RATE_RANGE': (0.01, 0.5),
            'FEEDBACK_SENSITIVITY_OPTIONS': ['fixed', 'adaptive'],
            'MODEL_UPDATING_OPTIONS': ['online', 'batch'],
        }

    def _context_awareness_config(self):
        return {
            'ENABLED_OPTIONS': [True, False],
            'DYNAMIC_ADJUSTMENT_OPTIONS': [True, False],
            'PREDICTION': [True, False],
            'CONTEXT_INTEGRATION_STRATEGIES': ['multimodal', 'unimodal'],
        }

    def _precision_weighting_config(self):
        return {
            'PERCEPTION_RANGE': (0.1, 1.0),
            'ACTION_RANGE': (0.1, 1.0),
            'ADAPTIVE': [True, False],
        }

    def _ant_and_colony_config(self):
        return {
            'MOVEMENT_OPTIONS': [
                [(-1, -1), (0, -1), (1, -1), (-1, 0), (0, 0), (1, 0), (-1, 1), (0, 1), (1, 1)],
                [(-1, 0), (0, 0), (1, 0), (0, -1), (0, 1)],
            ],
            'PHEROMONE_TYPE_RANGE': (1, 10),
            'MAX_PHEROMONE_RELEASE_RATE_RANGE': (1, 10),
            'SOUND_PRODUCTION_TYPES': [['stridulation', 'sing', 'talk', 'grunt'], ['stridulation', 'sing']],
            'SOUND_INTENSITY_LEVEL_RANGE': (1, 10),
            'PERCEPTUAL_FIELD_SIZE_RANGE': (1, 7),
            'MEMORY_CAPACITY_RANGE': (50, 200),
            'ATTENTION_SPAN_RANGE': (3, 10),
            'DECISION_STRATEGY_OPTIONS': ['deterministic', 'probabilistic'],
            'RISK_TAKING_OPTIONS': ['low', 'moderate', 'high'],
            'COLONY_STRUCTURE_OPTIONS': ['subterranean', 'arboreal', 'mixed'],
            'FORAGING_STRATEGIES': ['random_search', 'pheromone_trail', 'visual_cues'],
            'COMMUNICATION_METHODS': ['pheromones', 'tactile', 'auditory', 'visual'],
            'DEFENSE_MECHANISMS': ['chemical', 'physical', 'camouflage'],
            'EXPANSION_STRATEGY_OPTIONS': ['gradual', 'rapid', 'steady'],
            'THREAT_RESPONSES': ['evacuation', 'defense', 'hide', 'counterattack'],
        }

META_CONFIG = MetaConfig().config
