import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import entropy
from typing import Dict, List, Any, Optional
import seaborn as sns
from collections import Counter
import logging
from dataclasses import dataclass, field

@dataclass
class SimulationEntity:
    energy: float = 0.0
    type: str = "default"
    lifespan: int = 0
    distance_traveled: float = 0.0
    food_collected: int = 0

@dataclass
class SimulationData:
    agents: List[SimulationEntity] = field(default_factory=list)
    food_sources: List[Dict[str, int]] = field(default_factory=list)
    nests: List[Dict[str, int]] = field(default_factory=list)
    simulation_steps: int = 0

class EnhancedSimulationSummary:
    def __init__(self, simulation_results: Dict[str, Any]):
        self.data = SimulationData(
            agents=[SimulationEntity(**agent) for agent in simulation_results.get('agents', [])],
            food_sources=simulation_results.get('food_sources', []),
            nests=simulation_results.get('nests', []),
            simulation_steps=simulation_results.get('simulation_steps', 0)
        )
        self.logger = logging.getLogger(__name__)

    def generate_summary(self) -> Dict[str, Any]:
        try:
            summary = {
                'total_agents': self._total_agents(),
                'total_food_sources': self._total_food_sources(),
                'total_nests': self._total_nests(),
                'average_agent_energy': self._average_agent_energy(),
                'total_food_collected': self._total_food_collected(),
                'simulation_steps': self.data.simulation_steps,
                'energy_statistics': self._energy_statistics(),
                'summary_by_agent_type': self._summary_by_agent_type(),
                'agents_entropy': self._agents_entropy(),
                'food_distribution': self._food_distribution(),
                'agent_lifespan': self._agent_lifespan(),
                'nest_efficiency': self._nest_efficiency(),
                'agent_movement': self._agent_movement()
            }
            return summary
        except Exception as e:
            self.logger.error(f"Error generating summary: {str(e)}")
            return {}

    def _total_agents(self) -> int:
        return len(self.data.agents)

    def _total_food_sources(self) -> int:
        return len(self.data.food_sources)

    def _total_nests(self) -> int:
        return len(self.data.nests)

    def _average_agent_energy(self) -> float:
        return np.mean([agent.energy for agent in self.data.agents]) if self.data.agents else 0.0

    def _total_food_collected(self) -> int:
        return sum(nest.get('food_collected', 0) for nest in self.data.nests)

    def _energy_statistics(self) -> Dict[str, float]:
        energies = [agent.energy for agent in self.data.agents]
        return {
            "mean_energy": np.mean(energies),
            "std_dev_energy": np.std(energies),
            "median_energy": np.median(energies),
            "min_energy": np.min(energies),
            "max_energy": np.max(energies)
        } if energies else {k: 0.0 for k in ["mean_energy", "std_dev_energy", "median_energy", "min_energy", "max_energy"]}

    def _summary_by_agent_type(self) -> Dict[str, Dict[str, Any]]:
        summary = {}
        for agent in self.data.agents:
            summary.setdefault(agent.type, {'energy': [], 'count': 0, 'food_collected': 0})
            summary[agent.type]['energy'].append(agent.energy)
            summary[agent.type]['count'] += 1
            summary[agent.type]['food_collected'] += agent.food_collected
        
        for agent_type, stats in summary.items():
            stats['average_energy'] = np.mean(stats['energy']) if stats['energy'] else 0
            stats['efficiency'] = stats['food_collected'] / stats['count'] if stats['count'] else 0
        return summary

    def _agents_entropy(self) -> float:
        energies = [agent.energy for agent in self.data.agents]
        return entropy(energies) if energies else 0

    def _food_distribution(self) -> Dict[str, float]:
        food_amounts = [source.get('amount', 0) for source in self.data.food_sources]
        return {
            'total_food': sum(food_amounts),
            'average_food_per_source': np.mean(food_amounts),
            'max_food_in_source': max(food_amounts),
            'min_food_in_source': min(food_amounts)
        } if food_amounts else {k: 0.0 for k in ['total_food', 'average_food_per_source', 'max_food_in_source', 'min_food_in_source']}

    def _agent_lifespan(self) -> Dict[str, float]:
        lifespans = [agent.lifespan for agent in self.data.agents]
        return {
            'average_lifespan': np.mean(lifespans),
            'max_lifespan': max(lifespans),
            'min_lifespan': min(lifespans)
        } if lifespans else {k: 0.0 for k in ['average_lifespan', 'max_lifespan', 'min_lifespan']}

    def _nest_efficiency(self) -> Dict[str, float]:
        efficiencies = [nest.get('food_collected', 0) / nest.get('agents', 1) for nest in self.data.nests]
        return {
            'average_efficiency': np.mean(efficiencies),
            'max_efficiency': max(efficiencies),
            'min_efficiency': min(efficiencies)
        } if efficiencies else {k: 0.0 for k in ['average_efficiency', 'max_efficiency', 'min_efficiency']}

    def _agent_movement(self) -> Dict[str, float]:
        movements = [agent.distance_traveled for agent in self.data.agents]
        return {
            'average_movement': np.mean(movements),
            'max_movement': max(movements),
            'min_movement': min(movements)
        } if movements else {k: 0.0 for k in ['average_movement', 'max_movement', 'min_movement']}

def summarize_simulation(simulation_results: Dict[str, Any]) -> Dict[str, Any]:
    summary = EnhancedSimulationSummary(simulation_results)
    return summary.generate_summary()

def save_summary_to_file(summary: Dict[str, Any], file_path: str) -> None:
    try:
        with open(file_path, 'w') as file:
            for key, value in summary.items():
                file.write(f"{key}: {value}\n")
        logging.info(f"Summary saved to {file_path}")
    except IOError as e:
        logging.error(f"Error saving summary to file: {str(e)}")

def save_summary_to_csv(summary: Dict[str, Any], file_path: str) -> None:
    try:
        pd.DataFrame.from_dict(summary, orient='index').to_csv(file_path, header=False)
        logging.info(f"Summary saved to CSV: {file_path}")
    except Exception as e:
        logging.error(f"Error saving summary to CSV: {str(e)}")

def plot_agent_energy_distribution(agents: List[SimulationEntity], file_path: str) -> None:
    try:
        energies = [agent.energy for agent in agents]
        plt.figure(figsize=(10, 6))
        sns.histplot(energies, kde=True, color='skyblue', edgecolor='black')
        plt.title('Agent Energy Distribution')
        plt.xlabel('Energy')
        plt.ylabel('Frequency')
        plt.grid(axis='y', alpha=0.75)
        plt.savefig(file_path)
        plt.close()
        logging.info(f"Agent energy distribution plot saved to {file_path}")
    except Exception as e:
        logging.error(f"Error plotting agent energy distribution: {str(e)}")

def plot_agent_types(agents: List[SimulationEntity], file_path: str) -> None:
    try:
        agent_types = [agent.type for agent in agents]
        type_counts = Counter(agent_types)
        plt.figure(figsize=(10, 6))
        sns.barplot(x=list(type_counts.keys()), y=list(type_counts.values()))
        plt.title('Agent Types Distribution')
        plt.xlabel('Agent Type')
        plt.ylabel('Count')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(file_path)
        plt.close()
        logging.info(f"Agent types distribution plot saved to {file_path}")
    except Exception as e:
        logging.error(f"Error plotting agent types: {str(e)}")

def plot_food_distribution(food_sources: List[Dict[str, int]], file_path: str) -> None:
    try:
        food_amounts = [source.get('amount', 0) for source in food_sources]
        plt.figure(figsize=(10, 6))
        sns.boxplot(y=food_amounts)
        plt.title('Food Distribution Across Sources')
        plt.ylabel('Food Amount')
        plt.savefig(file_path)
        plt.close()
        logging.info(f"Food distribution plot saved to {file_path}")
    except Exception as e:
        logging.error(f"Error plotting food distribution: {str(e)}")

# Example usage
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    
    simulation_results = {
        "agents": [
            {"energy": 10, "type": "worker", "lifespan": 100, "distance_traveled": 50, "food_collected": 2},
            {"energy": 12, "type": "scout", "lifespan": 120, "distance_traveled": 80, "food_collected": 1}
        ],
        "food_sources": [{"amount": 100}, {"amount": 150}, {"amount": 80}],
        "nests": [{"food_collected": 5, "agents": 10}, {"food_collected": 7, "agents": 8}],
        "simulation_steps": 1000
    }
    
    summary = summarize_simulation(simulation_results)
    save_summary_to_file(summary, "simulation_summary.txt")
    save_summary_to_csv(summary, "simulation_summary.csv")
    plot_agent_energy_distribution(SimulationData(**simulation_results).agents, "agent_energy_distribution.png")
    plot_agent_types(SimulationData(**simulation_results).agents, "agent_types_distribution.png")
    plot_food_distribution(simulation_results['food_sources'], "food_distribution.png")
