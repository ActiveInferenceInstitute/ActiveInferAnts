import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Dict, Any

class EnhancedSimulationStatistics:
    def __init__(self, simulation_results: pd.DataFrame):
        """
        Initializes the EnhancedSimulationStatistics with simulation results.

        Parameters:
        - simulation_results (pd.DataFrame): A DataFrame containing the simulation results.
        """
        self.results = simulation_results if isinstance(simulation_results, pd.DataFrame) else pd.DataFrame(simulation_results)

    def compute_summary_statistics(self) -> Dict[str, Any]:
        """
        Computes summary statistics from the simulation results.

        Returns:
        - Dict[str, Any]: A dictionary containing summary statistics.
        """
        summary_keys = ['agents', 'food_sources', 'nests']
        summary = {f'total_{key}': self.results[key].count() for key in summary_keys if key in self.results}
        summary['total_food_collected'] = self.results.query("category == 'nests'")['food_collected'].sum()
        summary['simulation_steps'] = self.results['simulation_steps'].iloc[0]
        summary['average_energy'] = self.results.query("category == 'agents'")['energy'].mean()
        return summary

    def compute_agent_type_statistics(self) -> pd.DataFrame:
        """
        Computes statistics for each agent type.

        Returns:
        - pd.DataFrame: A DataFrame containing statistics for each agent type.
        """
        agent_stats = self.results.query("category == 'agents'").groupby('type')['energy'].agg(['mean', 'median', 'min', 'max', 'std'])
        return agent_stats

    def visualize_agent_energy_distribution(self, file_path: str) -> None:
        """
        Visualizes the distribution of agent energy.

        Parameters:
        - file_path (str): The file path to save the plot.
        """
        agent_energy = self.results.query("category == 'agents'")['energy']
        plt.figure(figsize=(10, 6))
        sns.histplot(agent_energy, bins=20, kde=True, color='skyblue', edgecolor='black')
        plt.xlabel('Agent Energy', fontsize=14)
        plt.ylabel('Count', fontsize=14)
        plt.title('Agent Energy Distribution', fontsize=16)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.savefig(file_path)
        plt.close()

# Example usage
# results = load_simulation_results(file_path)
# stats = EnhancedSimulationStatistics(results)
# print(stats.compute_summary_statistics())
# print(stats.compute_agent_type_statistics())
# stats.visualize_agent_energy_distribution('energy_dist.png')
