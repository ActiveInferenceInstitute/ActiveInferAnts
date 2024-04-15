import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import entropy

class EnhancedSimulationSummary:
    def __init__(self, simulation_results):
        self.simulation_results = simulation_results
        self.agents = simulation_results.get('agents', [])
        self.food_sources = simulation_results.get('food_sources', [])
        self.nests = simulation_results.get('nests', [])
        self.simulation_steps = simulation_results.get('simulation_steps', 0)

    def generate_summary(self):
        summary = {
            'total_agents': self._total_agents(),
            'total_food_sources': self._total_food_sources(),
            'total_nests': self._total_nests(),
            'average_agent_energy': self._average_agent_energy(),
            'total_food_collected': self._total_food_collected(),
            'simulation_steps': self.simulation_steps,
            'energy_statistics': self._energy_statistics(),
            'summary_by_agent_type': self._summary_by_agent_type(),
            'agents_entropy': self._agents_entropy()
        }
        return summary

    def _total_agents(self):
        return len(self.agents)

    def _total_food_sources(self):
        return len(self.food_sources)

    def _total_nests(self):
        return len(self.nests)

    def _average_agent_energy(self):
        total_energy = sum(agent.get('energy', 0) for agent in self.agents)
        return total_energy / len(self.agents) if self.agents else 0

    def _total_food_collected(self):
        return sum(nest.get('food_collected', 0) for nest in self.nests)

    def _energy_statistics(self):
        energies = [agent.get('energy', 0) for agent in self.agents]
        return {
            "mean_energy": np.mean(energies) if energies else 0,
            "std_dev_energy": np.std(energies) if energies else 0,
            "median_energy": np.median(energies) if energies else 0
        }

    def _summary_by_agent_type(self):
        summary = {}
        for agent in self.agents:
            agent_type = agent.get('type', 'default')
            summary.setdefault(agent_type, {'energy': [], 'count': 0})
            summary[agent_type]['energy'].append(agent.get('energy', 0))
            summary[agent_type]['count'] += 1
        for agent_type, stats in summary.items():
            stats['average_energy'] = np.mean(stats['energy']) if stats['energy'] else 0
        return summary

    def _agents_entropy(self):
        energies = [agent.get('energy', 0) for agent in self.agents]
        return entropy(energies) if energies else 0

def summarize_simulation(simulation_results):
    summary = EnhancedSimulationSummary(simulation_results)
    return summary.generate_summary()

def save_summary_to_file(summary, file_path):
    with open(file_path, 'w') as file:
        for key, value in summary.items():
            file.write(f"{key}: {value}\n")

def save_summary_to_csv(summary, file_path):
    pd.DataFrame.from_dict(summary, orient='index').to_csv(file_path, header=False)

def plot_agent_energy_distribution(agents, file_path):
    energies = [agent.get('energy', 0) for agent in agents]
    plt.hist(energies, bins=10, color='skyblue', edgecolor='black')
    plt.title('Agent Energy Distribution')
    plt.xlabel('Energy')
    plt.ylabel('Frequency')
    plt.grid(axis='y', alpha=0.75)
    plt.savefig(file_path)
    plt.close()

# Example usage
# simulation_results = {
#     "agents": [{"energy": 10}, {"energy": 12}],
#     "food_sources": [1, 2, 3],
#     "nests": [{"food_collected": 5}, {"food_collected": 7}],
#     "simulation_steps": 1000
# }
# summary = summarize_simulation(simulation_results)
# save_summary_to_file(summary, "simulation_summary.txt")
# save_summary_to_csv(summary, "simulation_summary.csv")
# plot_agent_energy_distribution(simulation_results['agents'], "agent_energy_distribution.png")
