import numpy as np
from typing import Dict, List, Tuple, Union

# General simulation parameters
SIMULATION_SETTINGS: Dict[str, Union[int, Dict]] = {
    'MAX_STEPS': 500,  # Maximum number of simulation steps.
    'AGENT_COUNT': 100,  # Total number of agents.
    'NEST_COUNT': 5,  # Number of nests.
    'PARALLEL_EXECUTION': {
        'ENABLED': True,
        'WORKER_COUNT': 4,
        'STRATEGY': 'distributed',  # Options: 'distributed', 'multithreading'
    },
    'COMPUTATION_SETTINGS': {
        'GPU_ACCELERATION': True,
        'GPU_PREFERENCE': 'high_performance',  # Options: 'high_performance', 'energy_saving'
        'DISTRIBUTED_COMPUTING': {
            'ENABLED': True,
            'CLUSTER_NODE_COUNT': 4,
            'COMMUNICATION_PROTOCOL': 'MPI',  # Options: 'MPI', 'TCP/IP', etc.
        },
    },
}

# Enhanced Active Inference configuration parameters for advanced pre-rendering and contextualization in shared intelligence ecosystems
ACTIVE_INFERENCE_CONFIG: Dict[str, Union[bool, List, Dict]] = {
    'ENABLED': True,
    'INFERENCE_MODELS': ['variational', 'predictive_coding', 'bayesian_filtering', 'deep_active_inference', 'ensemble_methods'],
    'EXPECTATION_FREE_ENERGY': True,
    'PLANNING_HORIZON': {
        'TYPE': 'adaptive',
        'BASE_VALUE': 15,
        'ADAPTATION_STRATEGY': 'contextual_complexity',
    },
    'TIME_RESOLUTION': 'continuous',
    'PRECISION_WEIGHTING': {
        'PERCEPTION': {'BASE': 0.8, 'ADAPTIVE': True},
        'ACTION': {'BASE': 0.2, 'ADAPTIVE': True},
    },
    'GENERALIZATION_DEPTH': 5,
    'ITERATION_LIMIT': 20,
    'ADAPTIVE_LEARNING': {
        'ENABLED': True,
        'LEARNING_RATE': 0.1,
        'FEEDBACK_SENSITIVITY': 'adaptive',
        'MODEL_UPDATING': 'online',
    },
    'CONTEXT_AWARENESS': {
        'ENABLED': True,
        'CONTEXT_TYPES': ['environmental', 'social', 'temporal', 'emotional', 'predictive'],
        'DYNAMIC_ADJUSTMENT': True,
        'PREDICTION': True,
    },
    'COGNITIVE_COMPLEXITY': {
        'ENABLED': True,
        'TYPES': ['simple', 'complex', 'hierarchical', 'emergent', 'adaptive'],
        'STRATEGY_ADAPTATION': True,
        'COMPLEXITY_MANAGEMENT': 'dynamic',
    },
    'SURPRISE_MINIMIZATION': True,
    'GOAL_ORIENTED_BEHAVIOR': {
        'ENABLED': True,
        'GOALS': ['survival', 'exploration', 'social_interaction'],
        'GOAL_PRIORITIZATION': 'adaptive',
    },
    'LEARNING_RATE': 0.1,
    'EFE_CALCULATION_PARAMS': {
        'DEFAULT': 0.5,
    },
    'META_LEARNING': {
        'ENABLED': True,
        'STRATEGIES': ['experience_replay', 'strategy_optimization'],
    },
    'MULTI_OBJECTIVE_DECISION_MAKING': {
        'ENABLED': True,
        'INTEGRATION_STRATEGY': 'weighted_sum',
    },
    'UNCERTAINTY_MANAGEMENT': {
        'ENABLED': True,
        'STRATEGIES': ['risk_averse', 'risk_neutral', 'risk_seeking'],
    },
    'COMMUNICATION': {
        'ENABLED': True,
        'MODES': ['direct', 'indirect', 'environmental_signaling'],
    },
    'LEARNING_MECHANISMS': {
        'ENABLED': True,
        'TYPES': ['reinforcement_learning', 'supervised_learning', 'unsupervised_learning'],
    },
}

# Consolidated Ant and Colony Configuration Parameters
ANT_AND_COLONY_CONFIG: Dict[str, Dict] = {
    'NESTMATE': {
        'ACTIVE_INFERENCE': {
            'BLANKET_STATES': {
                'ACTION': {
                    'MOVEMENT': [
                        (-1, -1), (0, -1), (1, -1),  # Up-left, Up, Up-right
                        (-1, 0), (0, 0), (1, 0),     # Left, Stay, Right
                        (-1, 1), (0, 1), (1, 1)      # Down-left, Down, Down-right
                    ],
                    'PHEROMONE_RELEASE': {
                        'TYPES': {
                            'lipid_based': {'id': 1, 'max_rate': 3},
                            'small_molecules': {'id': 2, 'max_rate': 5},
                            'proteinaceous': {'id': 3, 'max_rate': 4},
                            'volatile_compounds': {'id': 4, 'max_rate': 6}
                        },
                        'QUEEN_PHEROMONE': 'lipid_based',  # Identifier for queen pheromone
                    },
                    'SOUND_PRODUCTION': {
                        'TYPES': ['stridulation', 'sing', 'talk', 'grunt', 'tremble', 'waggle'],
                        'INTENSITY_LEVELS': 5,  # Levels of sound intensity
                    },
                },
                'SENSE': {
                    'OBSERVATIONS': {
                        'VISION': 3,  # Visual observation modalities
                        'WIDTH': 3,  # Width of the perceptual field
                        'HEIGHT': 3,  # Height of the perceptual field
                        'TOTAL_SIZE': np.prod((3, 3)),  # Total size, calculated from width and height
                    },
                },
            },
            'INTERNAL_STATES': {
                'COGNITIVE': {
                    'MEMORY_CAPACITY': 100,  # Max memories
                    'ATTENTION_SPAN': 5,  # Focusable items
                    'THEORY_OF_MIND': True,  # Theory of mind capabilities
                    'PROBLEM_SOLVING': True,  # Complex task solving
                    'EMOTIONAL_INTELLIGENCE': True,  # Emotional cue response
                },
                'META_COGNITIVE': {
                    'DECISION_STRATEGY': 'probabilistic',  # Decision making strategy
                    'LEARNING_RATE': 0.01,  # Experience learning rate
                    'ADAPTABILITY': True,  # Environment adaptability
                    'RISK_TAKING': 'moderate',  # Risk behavior
                    'CREATIVITY': 'medium',  # Problem-solving creativity
                    'SOCIAL_LEARNING': True,  # Learning from others
                },
                'SENSORY_PROCESSING': {
                    'VISUAL': True,  # Visual information processing
                    'AUDITORY': True,  # Auditory information processing
                    'TACTILE': True,  # Tactile information processing
                    'OLFACTORY': True,  # Olfactory information processing
                    'GUSTATORY': False,  # Gustatory information processing
                },
            },
        },
    },
    'COLONY': {
        'INITIAL_POSITIONS': {
            'XYZ': {'X': 20, 'Y': 30, 'Z': 5},  # Initial position in a 3D space
            'IVM': {'W': 10, 'X': 20, 'Y': 30, 'Z': 5},  # Initial position in Isotropic Vector Matrix (IVM) space
        },
        'INFLUENCE_FACTOR': 0.1,  # Influence factor for nest-related calculations
        'LIFE_STAGE': 'worker',  # Predominant life history stage within the colony
        'DEMOGRAPHICS': {
            'WORKERS': 300,  # Number of worker ants
            'QUEENS': 3,  # Number of queen ants
            'MALES': 50,  # Number of male ants
            'LARVAE': 500,  # Number of larvae
        },
        'STRUCTURE': 'subterranean',  # Type of nest structure
        'STORAGE': {
            'FOOD_CAPACITY': 1000,  # Maximum food storage capacity
            'WATER_SYSTEM': True,  # Presence of a water collection system
        },
        'DEFENSES': ['chemical', 'physical'],  # Defense mechanisms employed
        'FORAGING_STRATEGIES': ['random_search', 'pheromone_trail'],  # Foraging strategies
        'COMMUNICATION_METHODS': ['pheromones', 'tactile', 'auditory'],  # Communication methods within the colony
        'MORTALITY_RATES': {
            'WORKERS': 0.05,  # Mortality rate for workers
            'LARVAE': 0.1,  # Mortality rate for larvae
        },
        'RESOURCE_NEEDS': {
            'FOOD_CONSUMPTION': 500,  # Daily food consumption
            'WATER_CONSUMPTION': 200,  # Daily water consumption
        },
        'EXPANSION_STRATEGY': 'gradual',  # Colony expansion strategy
        'THREAT_RESPONSES': ['evacuation', 'defense', 'hide'],  # Threat responses
    },
}

# ENVIRONMENT PARAMETERS (NON-ANT)
ENVIRONMENT_CONFIG: Dict[str, Union[Dict, List]] = {
    'GRID': {
        'WIDTH': 100,  # Grid width
        'HEIGHT': 100,  # Grid height
        'DIMENSIONS': (100, 100),  # Tuple representing grid dimensions
        'TOTAL_SIZE': 10000,  # Total grid size, explicitly calculated for clarity
    },
    'RESOURCE_ZONES': [
        {
            'TYPE': 'food',  # Type of resource
            'POSITION': {'X': 40, 'Y': 5},  # X and Y-axis positions of the resource zone
            'SIZE': {'WIDTH': 40, 'HEIGHT': 40},  # Width and height of the resource zone
            'DIMENSIONS': (40, 40),  # Tuple representing resource zone dimensions
            'TOTAL_SIZE': 1600,  # Total size of the resource zone, explicitly calculated for clarity
        },
        {
            'TYPE': 'water',  # Additional resource type for expanded environmental configuration
            'POSITION': {'X': 60, 'Y': 75},  # X and Y-axis positions of the water zone
            'SIZE': {'WIDTH': 20, 'HEIGHT': 20},  # Width and height of the water zone
            'DIMENSIONS': (20, 20),  # Tuple representing water zone dimensions
            'TOTAL_SIZE': 400,  # Total size of the water zone, explicitly calculated for clarity
        }
    ],
    'OBSTACLES': [
        {
            'TYPE': 'rock',  # Type of obstacle
            'POSITION': {'LEFT': 15, 'TOP': 10},  # Position of the obstacle (left-top corner)
            'SIZE': {'WIDTH': 10, 'HEIGHT': 10},  # Width and height of the obstacle
            'DIMENSIONS': (10, 10),  # Tuple representing obstacle dimensions
        },
        {
            'TYPE': 'tree',  # Additional obstacle type for expanded environmental configuration
            'POSITION': {'LEFT': 70, 'TOP': 20},  # Position of the tree (left-top corner)
            'SIZE': {'WIDTH': 10, 'HEIGHT': 10},  # Width and height of the tree
            'DIMENSIONS': (10, 10),  # Tuple representing tree dimensions
        }
    ],
    'ENVIRONMENTAL_GROUNDS': ['dirt', 'grass', 'stone', 'wood', 'sand'],  # Types of grounds in the environment
    'PHEROMONE_CONFIG': {
        'STIGMERGY_TYPES': ['stone', 'sand', 'silt', 'gel', 'air', 'pebble', 'molecular'],  # Types of stigmergy
        'MOLECULAR_STIGMERGY_TYPES': ['protein', 'fat', 'carbohydrate', 'other'],  # Types of molecular stigmergy
        'LEVEL_COUNT': 10,  # Total number of pheromone signal levels
        'DECAY_RATE': 0.01,  # Pheromone signal decay rate per time step
    },
}

# Additional configuration for advanced simulation features
ADVANCED_SIMULATION_CONFIG: Dict[str, Union[bool, Dict]] = {
    'DYNAMIC_ENVIRONMENT': {
        'ENABLED': True,  # Flag to enable/disable dynamic environment changes
        'WEATHER_EFFECTS': ['rain', 'wind', 'heat'],  # Weather effects that can influence the environment
        'SEASONAL_CHANGES': True,  # Flag to enable/disable seasonal changes
        'NATURAL_DISASTERS': ['flood', 'drought', 'fire'],  # Possible natural disasters
    },
    'INTER_COLONY_INTERACTIONS': {
        'ENABLED': True,  # Flag to enable/disable interactions between different colonies
        'TYPES': ['competition', 'cooperation', 'predation'],  # Types of inter-colony interactions
        'TERRITORY_OVERLAP': 0.2,  # Degree of territory overlap between colonies
    },
    'GENETIC_ALGORITHMS': {
        'ENABLED': True,  # Flag to enable/disable genetic algorithms for ant evolution
        'MUTATION_RATE': 0.01,  # Rate of genetic mutations
        'CROSSOVER_RATE': 0.7,  # Rate of genetic crossover
        'SELECTION_METHOD': 'tournament',  # Method for selecting individuals for reproduction
    },
    'ADVANCED_PATHFINDING': {
        'ALGORITHM': 'A*',  # Pathfinding algorithm used by ants
        'HEURISTIC': 'manhattan',  # Heuristic used in pathfinding
        'OBSTACLE_AVOIDANCE': True,  # Flag to enable/disable advanced obstacle avoidance
    },
    'MULTI_LAYER_PHEROMONE_SYSTEM': {
        'ENABLED': True,  # Flag to enable/disable multi-layer pheromone system
    }, 
}

def get_full_config() -> Dict[str, Union[int, Dict]]:
    """
    Returns a consolidated configuration dictionary for the whole simulation.

    This can later be extended to incorporate runtime overrides.

    Returns:
        Dict[str, Union[int, Dict]]: Consolidated configuration.
    """
    return {
        'SIMULATION_SETTINGS': SIMULATION_SETTINGS,
        'ACTIVE_INFERENCE_CONFIG': ACTIVE_INFERENCE_CONFIG,
        'ANT_AND_COLONY_CONFIG': ANT_AND_COLONY_CONFIG,
        'ENVIRONMENT_CONFIG': ENVIRONMENT_CONFIG,
        'ADVANCED_SIMULATION_CONFIG': ADVANCED_SIMULATION_CONFIG,
    } 
