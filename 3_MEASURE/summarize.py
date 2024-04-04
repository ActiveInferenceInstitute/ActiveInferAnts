import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class SimulationSummary:
    def __init__(self, simulation_results):
        self.simulation_results = simulation_results
        self.total_agents = len(simulation_results['agents'])  # Store total agents count

    def generate_summary(self):
        summary_methods = [
            self._total_agents,
            self._total_food_sources,
            self._total_nests,
            self._average_agent_energy,
            self._total_food_collected,
            self._simulation_steps,
            self._energy_statistics,
            self._summary_by_agent_type
        ]
        summary = {method.__name__[1:]: method() for method in summary_methods}
        return summary

    def _total_agents(self):
        return self.total_agents

    def _total_food_sources(self):
        return len(self.simulation_results['food_sources'])

    def _total_nests(self):
        return len(self.simulation_results['nests'])

    def _average_agent_energy(self):
        total_energy = sum(agent['energy'] for agent in self.simulation_results['agents'])
        return total_energy / self.total_agents if self.total_agents > 0 else 0

    def _total_food_collected(self):
        return sum(nest['food_collected'] for nest in self.simulation_results['nests'])

    def _simulation_steps(self):
        return self.simulation_results['simulation_steps']

    def _energy_statistics(self):
        energies = [agent['energy'] for agent in self.simulation_results['agents']]
        return {
            "mean_energy": np.mean(energies),
            "std_dev_energy": np.std(energies),
            "median_energy": np.median(energies)
        }

    def _summary_by_agent_type(self):
        summary = {}
        for agent in self.simulation_results['agents']:
            agent_type = agent.get('type', 'default')
            summary.setdefault(agent_type, {'energy': [], 'count': 0})
            summary[agent_type]['energy'].append(agent['energy'])
            summary[agent_type]['count'] += 1
        for agent_type, stats in summary.items():
            summary[agent_type]['average_energy'] = np.mean(stats['energy'])
        return summary

def summarize_simulation(simulation_results):
    summary = SimulationSummary(simulation_results)
    return summary.generate_summary()

def save_summary_to_file(summary, file_path):
    with open(file_path, 'w') as file:
        for key, value in summary.items():
            file.write(f"{key}: {value}\n")

def save_summary_to_csv(summary, file_path):
    pd.DataFrame.from_records([summary]).to_csv(file_path, index=False)

def plot_agent_energy_distribution(agents, file_path):
    energies = [agent['energy'] for agent in agents]
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
