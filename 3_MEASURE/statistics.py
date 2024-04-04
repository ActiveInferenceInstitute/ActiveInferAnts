import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class SimulationStatistics:
    def __init__(self, simulation_results):
        self.results = simulation_results
        self.data_frames = {key: pd.DataFrame(value) for key, value in simulation_results.items()}

    def summary_statistics(self):
        summary = {f'total_{key}': len(df) for key, df in self.data_frames.items() if key in ['agents', 'food_sources', 'nests']}
        summary['total_food_collected'] = self.data_frames['nests']['food_collected'].sum()
        summary['simulation_steps'] = self.results['simulation_steps']
        return summary

    def agent_type_statistics(self):
        return self.data_frames['agents'].groupby('type')['energy'].agg(['mean', 'median', 'min', 'max', 'std']).to_dict('index')

    def plot_agent_energy_distribution(self, file_path):
        sns.histplot(self.data_frames['agents']['energy'], bins=20, kde=True)
        plt.xlabel('Agent Energy')
        plt.ylabel('Count')
        plt.title('Agent Energy Distribution')
        plt.grid(axis='y', alpha=0.75)
        plt.savefig(file_path)
        plt.close()

# Example usage
# results = load_simulation_results(file_path)
# stats = SimulationStatistics(results)
# print(stats.summary_statistics())
# print(stats.agent_statistics())  
# print(stats.agent_type_statistics())
# stats.plot_agent_energy_distribution('energy_dist.png')
