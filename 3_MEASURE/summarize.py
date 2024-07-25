
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import entropy
from typing import Dict, List, Any
import seaborn as sns
from collections import Counter

class EnhancedSimulationSummary:
    def __init__(self, simulation_results: Dict[str, Any]):
        self.simulation_results = simulation_results
        self.agents = simulation_results.get('agents', [])
        self.food_sources = simulation_results.get('food_sources', [])
        self.nests = simulation_results.get('nests', [])
        self.simulation_steps = simulation_results.get('simulation_steps', 0)

    def generate_summary(self) -> Dict[str, Any]:
        summary = {
            'total_agents': self._total_agents(),
            'total_food_sources': self._total_food_sources(),
            'total_nests': self._total_nests(),
            'average_agent_energy': self._average_agent_energy(),
            'total_food_collected': self._total_food_collected(),
            'simulation_steps': self.simulation_steps,
            'energy_statistics': self._energy_statistics(),
            'summary_by_agent_type': self._summary_by_agent_type(),
            'agents_entropy': self._agents_entropy(),
            'food_distribution': self._food_distribution(),
            'agent_lifespan': self._agent_lifespan(),
            'nest_efficiency': self._nest_efficiency(),
            'agent_movement': self._agent_movement()
        }
        return summary

    def _total_agents(self) -> int:
        return len(self.agents)

    def _total_food_sources(self) -> int:
        return len(self.food_sources)

    def _total_nests(self) -> int:
        return len(self.nests)

    def _average_agent_energy(self) -> float:
        total_energy = sum(agent.get('energy', 0) for agent in self.agents)
        return total_energy / len(self.agents) if self.agents else 0

    def _total_food_collected(self) -> int:
        return sum(nest.get('food_collected', 0) for nest in self.nests)

    def _energy_statistics(self) -> Dict[str, float]:
        energies = [agent.get('energy', 0) for agent in self.agents]
        return {
            "mean_energy": np.mean(energies) if energies else 0,
            "std_dev_energy": np.std(energies) if energies else 0,
            "median_energy": np.median(energies) if energies else 0,
            "min_energy": np.min(energies) if energies else 0,
            "max_energy": np.max(energies) if energies else 0
        }

    def _summary_by_agent_type(self) -> Dict[str, Dict[str, Any]]:
        summary = {}
        for agent in self.agents:
            agent_type = agent.get('type', 'default')
            summary.setdefault(agent_type, {'energy': [], 'count': 0, 'food_collected': 0})
            summary[agent_type]['energy'].append(agent.get('energy', 0))
            summary[agent_type]['count'] += 1
            summary[agent_type]['food_collected'] += agent.get('food_collected', 0)
        
        for agent_type, stats in summary.items():
            stats['average_energy'] = np.mean(stats['energy']) if stats['energy'] else 0
            stats['efficiency'] = stats['food_collected'] / stats['count'] if stats['count'] else 0
        return summary

    def _agents_entropy(self) -> float:
        energies = [agent.get('energy', 0) for agent in self.agents]
        return entropy(energies) if energies else 0

    def _food_distribution(self) -> Dict[str, int]:
        food_amounts = [source.get('amount', 0) for source in self.food_sources]
        return {
            'total_food': sum(food_amounts),
            'average_food_per_source': np.mean(food_amounts) if food_amounts else 0,
            'max_food_in_source': max(food_amounts) if food_amounts else 0,
            'min_food_in_source': min(food_amounts) if food_amounts else 0
        }

    def _agent_lifespan(self) -> Dict[str, float]:
        lifespans = [agent.get('lifespan', 0) for agent in self.agents]
        return {
            'average_lifespan': np.mean(lifespans) if lifespans else 0,
            'max_lifespan': max(lifespans) if lifespans else 0,
            'min_lifespan': min(lifespans) if lifespans else 0
        }

    def _nest_efficiency(self) -> Dict[str, float]:
        efficiencies = [nest.get('food_collected', 0) / nest.get('agents', 1) for nest in self.nests]
        return {
            'average_efficiency': np.mean(efficiencies) if efficiencies else 0,
            'max_efficiency': max(efficiencies) if efficiencies else 0,
            'min_efficiency': min(efficiencies) if efficiencies else 0
        }

    def _agent_movement(self) -> Dict[str, float]:
        movements = [agent.get('distance_traveled', 0) for agent in self.agents]
        return {
            'average_movement': np.mean(movements) if movements else 0,
            'max_movement': max(movements) if movements else 0,
            'min_movement': min(movements) if movements else 0
        }

def summarize_simulation(simulation_results: Dict[str, Any]) -> Dict[str, Any]:
    summary = EnhancedSimulationSummary(simulation_results)
    return summary.generate_summary()

def save_summary_to_file(summary: Dict[str, Any], file_path: str) -> None:
    with open(file_path, 'w') as file:
        for key, value in summary.items():
            file.write(f"{key}: {value}\n")

def save_summary_to_csv(summary: Dict[str, Any], file_path: str) -> None:
    pd.DataFrame.from_dict(summary, orient='index').to_csv(file_path, header=False)

def plot_agent_energy_distribution(agents: List[Dict[str, Any]], file_path: str) -> None:
    energies = [agent.get('energy', 0) for agent in agents]
    plt.figure(figsize=(10, 6))
    sns.histplot(energies, kde=True, color='skyblue', edgecolor='black')
    plt.title('Agent Energy Distribution')
    plt.xlabel('Energy')
    plt.ylabel('Frequency')
    plt.grid(axis='y', alpha=0.75)
    plt.savefig(file_path)
    plt.close()

def plot_agent_types(agents: List[Dict[str, Any]], file_path: str) -> None:
    agent_types = [agent.get('type', 'default') for agent in agents]
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

def plot_food_distribution(food_sources: List[Dict[str, Any]], file_path: str) -> None:
    food_amounts = [source.get('amount', 0) for source in food_sources]
    plt.figure(figsize=(10, 6))
    sns.boxplot(y=food_amounts)
    plt.title('Food Distribution Across Sources')
    plt.ylabel('Food Amount')
    plt.savefig(file_path)
    plt.close()

# Example usage
# simulation_results = {
#     "agents": [{"energy": 10, "type": "worker", "lifespan": 100, "distance_traveled": 50},
#                {"energy": 12, "type": "scout", "lifespan": 120, "distance_traveled": 80}],
#     "food_sources": [{"amount": 100}, {"amount": 150}, {"amount": 80}],
#     "nests": [{"food_collected": 5, "agents": 10}, {"food_collected": 7, "agents": 8}],
#     "simulation_steps": 1000
# }
# summary = summarize_simulation(simulation_results)
# save_summary_to_file(summary, "simulation_summary.txt")
# save_summary_to_csv(summary, "simulation_summary.csv")
# plot_agent_energy_distribution(simulation_results['agents'], "agent_energy_distribution.png")
# plot_agent_types(simulation_results['agents'], "agent_types_distribution.png")
# plot_food_distribution(simulation_results['food_sources'], "food_distribution.png")
