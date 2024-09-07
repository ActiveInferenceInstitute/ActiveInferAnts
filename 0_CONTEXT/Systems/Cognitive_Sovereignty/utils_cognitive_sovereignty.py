import numpy as np
import json
import logging
from typing import Dict, List, Any, Tuple, Optional
import matplotlib.pyplot as plt
import seaborn as sns
import random
import os
from dataclasses import dataclass, asdict, field

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

STATES = ["IN_POWER", "HIGH_POWER", "MEDIUM_POWER", "LOW_POWER", "HOMO_SACER"]

@dataclass
class Entity:
    """Represents an entity in the Cognitive Sovereignty simulation."""
    name: str
    entity_type: str
    influence: float
    is_in_power: bool = False
    current_state: int = field(init=False)
    current_matrix: np.ndarray = field(init=False)

    def __post_init__(self) -> None:
        """Initialize current_state and current_matrix after object creation."""
        self.current_state = 0 if self.is_in_power else 2  # IN_POWER or MEDIUM_POWER
        self.current_matrix = generate_transition_matrix('empowered' if self.is_in_power else 'baseline')

    def update_state(self) -> None:
        """Update the entity's state based on its current transition matrix."""
        self.current_state = np.random.choice(len(STATES), p=self.current_matrix[self.current_state])
        self.is_in_power = (self.current_state == 0)

    def to_dict(self) -> Dict[str, Any]:
        """Convert the Entity object to a dictionary for JSON serialization."""
        entity_dict = asdict(self)
        entity_dict['current_matrix'] = entity_dict['current_matrix'].tolist()
        return entity_dict

def generate_entity(name: str, entity_type: str, influence: float, is_in_power: bool = False) -> Entity:
    """Generate an Entity object with the given parameters."""
    return Entity(name, entity_type, influence, is_in_power)

def save_entity_library(entities: List[Entity], filename: str) -> None:
    """Save the list of entities to a JSON file."""
    with open(filename, 'w') as f:
        json.dump([entity.to_dict() for entity in entities], f, indent=2)
    logger.info(f"Entity library saved to {filename}")

def ensure_output_directory(output_dir: str) -> None:
    """Ensure that the output directory exists, creating it if necessary."""
    os.makedirs(output_dir, exist_ok=True)
    logger.info(f"Output directory ensured: {output_dir}")

class CognitiveSovereignty:
    """Main class for running the Cognitive Sovereignty simulation."""

    def __init__(self):
        self.entities: List[Entity] = []

    def add_entity(self, entity: Entity) -> None:
        """Add an entity to the simulation."""
        self.entities.append(entity)

    def select_new_power(self) -> Entity:
        """Select a random entity that is not currently in power."""
        non_power_entities = [e for e in self.entities if not e.is_in_power]
        if not non_power_entities:
            raise ValueError("No entities available to select as new power")
        return random.choice(non_power_entities)

    def run_simulation(self, before_crisis: int, after_crisis: int) -> List[Dict[str, Any]]:
        """Run the simulation for the specified number of steps before and after the crisis."""
        results = []
        total_steps = before_crisis + after_crisis

        for step in range(total_steps):
            step_result = {"step": step, "entities": [], "crisis": False}

            if step == before_crisis:
                # Crisis event
                step_result["crisis"] = True
                new_power = self.select_new_power()
                
                for entity in self.entities:
                    if entity == new_power:
                        entity.current_matrix = generate_transition_matrix('empowered')
                        entity.is_in_power = True
                    else:
                        entity.current_matrix = generate_transition_matrix('disempowered')
                        entity.is_in_power = False

            for entity in self.entities:
                entity.update_state()
                step_result["entities"].append({
                    "name": entity.name,
                    "state": STATES[entity.current_state],
                    "is_in_power": entity.is_in_power
                })
            results.append(step_result)
        return results

def generate_transition_matrix(matrix_type: str = 'baseline') -> np.ndarray:
    """Generate a transition matrix based on the specified type."""
    matrix = np.zeros((len(STATES), len(STATES)))
    
    if matrix_type == 'baseline':
        # Only transitions among HIGH, MEDIUM, and LOW POWER
        sub_matrix = np.random.rand(3, 3)
        sub_matrix /= sub_matrix.sum(axis=1, keepdims=True)
        matrix[1:4, 1:4] = sub_matrix
        
        # Keep IN_POWER and HOMO_SACER in their states
        matrix[0, 0] = 1.0
        matrix[4, 4] = 1.0
    
    elif matrix_type == 'empowered':
        # Always stay IN_POWER
        matrix[0, 0] = 1.0
        # For other states, transition to IN_POWER with probability 1
        matrix[1:, 0] = 1.0
    
    elif matrix_type == 'disempowered':
        # Transitions among HIGH, MEDIUM, LOW POWER, and HOMO_SACER
        sub_matrix = np.random.rand(4, 4)
        sub_matrix /= sub_matrix.sum(axis=1, keepdims=True)
        matrix[1:, 1:] = sub_matrix
        # Ensure IN_POWER state transitions to HIGH_POWER
        matrix[0, 1] = 1.0
    
    else:
        raise ValueError(f"Invalid matrix type: {matrix_type}")
    
    return matrix

def save_results(results: List[Dict[str, Any]], file_path: str) -> None:
    """Save simulation results to a JSON file."""
    with open(file_path, 'w') as f:
        json.dump(results, f, indent=2)
    logger.info(f"Results saved to {file_path}")

def load_entity_library(filename: str) -> List[Entity]:
    """Load entity library from a JSON file."""
    with open(filename, 'r') as f:
        data = json.load(f)
    entities = []
    for entity_data in data:
        current_state = entity_data.pop('current_state', None)
        current_matrix = entity_data.pop('current_matrix', None)
        
        entity = Entity(**entity_data)
        
        if current_state is not None:
            entity.current_state = current_state
        if current_matrix is not None:
            entity.current_matrix = np.array(current_matrix)
        
        entities.append(entity)
    return entities

def visualize_simulation(results: List[Dict[str, Any]], output_file: str, before_crisis: int) -> None:
    """Create a stacked area chart showing the state distribution over time."""
    entity_names = [entity['name'] for entity in results[0]['entities']]
    time_steps = [result['step'] for result in results]
    state_counts = {state: [0] * len(time_steps) for state in STATES}

    for step, result in enumerate(results):
        for entity in result['entities']:
            state_counts[entity['state']][step] += 1

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.stackplot(time_steps, state_counts.values(),
                 labels=state_counts.keys(), alpha=0.8)
    
    ax.set_title('Entity State Changes Over Time')
    ax.set_xlabel('Time Step')
    ax.set_ylabel('Number of Entities')
    ax.legend(loc='upper left')
    ax.set_xlim(0, len(time_steps) - 1)
    ax.set_ylim(0, len(entity_names))

    ax.axvline(x=before_crisis, color='r', linestyle='--', label='Crisis')
    
    plt.tight_layout()
    plt.savefig(output_file)
    plt.close()

    logger.info(f"Visualization saved to {output_file}")

def visualize_entity_traces(results: List[Dict[str, Any]], output_file: str, before_crisis: int) -> None:
    """Create a line plot showing the state trace of each entity over time."""
    entity_names = [entity['name'] for entity in results[0]['entities']]
    time_steps = [result['step'] for result in results]
    
    # Create a dictionary to store the state history of each entity
    entity_states = {name: [] for name in entity_names}
    
    # Populate the state history
    for result in results:
        for entity in result['entities']:
            entity_states[entity['name']].append(STATES.index(entity['state']))
    
    # Create the plot
    fig, ax = plt.subplots(figsize=(12, 8))
    
    for name, states in entity_states.items():
        ax.plot(time_steps, states, label=name, alpha=0.7)
    
    ax.set_title('Entity State Traces Over Time')
    ax.set_xlabel('Time Step')
    ax.set_ylabel('State')
    ax.set_yticks(range(len(STATES)))
    ax.set_yticklabels(STATES)
    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    ax.grid(True, which='both', linestyle='--', linewidth=0.5)
    ax.set_xlim(0, len(time_steps) - 1)
    ax.set_ylim(-0.5, len(STATES) - 0.5)

    ax.axvline(x=before_crisis, color='r', linestyle='--', label='Crisis')
    
    plt.tight_layout()
    plt.savefig(output_file, bbox_inches='tight')
    plt.close()

    logger.info(f"Entity trace visualization saved to {output_file}")

def visualize_transition_matrices(entities: List[Entity], output_file: str) -> None:
    """Create a faceted plot showing the transition matrices for each entity under different conditions."""
    n_entities = len(entities)
    fig, axes = plt.subplots(n_entities, 3, figsize=(15, 5 * n_entities))
    fig.suptitle('Transition Matrices for Each Entity', fontsize=16)
    
    conditions = ['baseline', 'empowered', 'disempowered']
    
    for i, entity in enumerate(entities):
        for j, condition in enumerate(conditions):
            matrix = generate_transition_matrix(condition)
            ax = axes[i, j] if n_entities > 1 else axes[j]
            sns.heatmap(matrix, annot=True, fmt='.2f', cmap='YlGnBu', ax=ax, cbar=False)
            ax.set_title(f"{entity.name} - {condition.capitalize()}")
            ax.set_xlabel('To State')
            ax.set_ylabel('From State')
            ax.set_xticklabels(STATES, rotation=45, ha='right')
            ax.set_yticklabels(STATES, rotation=0)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.savefig(output_file, bbox_inches='tight')
    plt.close()

    logger.info(f"Transition matrices visualization saved to {output_file}")