import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Dict, Any, List, Optional
from scipy import stats
from dataclasses import dataclass

@dataclass
class SimulationSummary:
    total_agents: int
    total_food_sources: int
    total_nests: int
    total_food_collected: float
    simulation_steps: int
    average_energy: float
    energy_std_dev: float
    energy_median: float
    energy_min: float
    energy_max: float

class EnhancedSimulationStatistics:
    def __init__(self, simulation_results: pd.DataFrame):
        """
        Initializes the EnhancedSimulationStatistics with simulation results.

        Parameters:
        - simulation_results (pd.DataFrame): A DataFrame containing the simulation results.
        """
        self.results = simulation_results if isinstance(simulation_results, pd.DataFrame) else pd.DataFrame(simulation_results)
        self._validate_data()

    def _validate_data(self) -> None:
        """
        Validates the input data to ensure it contains the required columns and data types.
        Raises ValueError if the data is invalid.
        """
        required_columns = ['category', 'type', 'energy', 'food_collected', 'simulation_steps']
        for col in required_columns:
            if col not in self.results.columns:
                raise ValueError(f"Missing required column: {col}")
        
        if not all(self.results['category'].isin(['agents', 'food_sources', 'nests'])):
            raise ValueError("Invalid categories in the data")

    def compute_summary_statistics(self) -> SimulationSummary:
        """
        Computes comprehensive summary statistics from the simulation results.

        Returns:
        - SimulationSummary: A dataclass containing summary statistics.
        """
        agents_data = self.results.query("category == 'agents'")
        nests_data = self.results.query("category == 'nests'")

        return SimulationSummary(
            total_agents=len(agents_data),
            total_food_sources=len(self.results.query("category == 'food_sources'")),
            total_nests=len(nests_data),
            total_food_collected=nests_data['food_collected'].sum(),
            simulation_steps=self.results['simulation_steps'].iloc[0],
            average_energy=agents_data['energy'].mean(),
            energy_std_dev=agents_data['energy'].std(),
            energy_median=agents_data['energy'].median(),
            energy_min=agents_data['energy'].min(),
            energy_max=agents_data['energy'].max()
        )

    def compute_agent_type_statistics(self) -> pd.DataFrame:
        """
        Computes detailed statistics for each agent type.

        Returns:
        - pd.DataFrame: A DataFrame containing statistics for each agent type.
        """
        agent_stats = self.results.query("category == 'agents'").groupby('type')['energy'].agg([
            'count', 'mean', 'median', 'min', 'max', 'std',
            lambda x: stats.skew(x),
            lambda x: stats.kurtosis(x)
        ])
        agent_stats.columns = ['count', 'mean', 'median', 'min', 'max', 'std', 'skewness', 'kurtosis']
        return agent_stats

    def visualize_agent_energy_distribution(self, file_path: str, agent_types: Optional[List[str]] = None) -> None:
        """
        Visualizes the distribution of agent energy, optionally for specific agent types.

        Parameters:
        - file_path (str): The file path to save the plot.
        - agent_types (Optional[List[str]]): List of agent types to include in the visualization.
        """
        agent_data = self.results.query("category == 'agents'")
        if agent_types:
            agent_data = agent_data[agent_data['type'].isin(agent_types)]

        plt.figure(figsize=(12, 8))
        sns.histplot(data=agent_data, x='energy', hue='type', kde=True, multiple="stack")
        plt.xlabel('Agent Energy', fontsize=14)
        plt.ylabel('Count', fontsize=14)
        plt.title('Agent Energy Distribution by Type', fontsize=16)
        plt.legend(title='Agent Type', title_fontsize='13', fontsize='11')
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.savefig(file_path, dpi=300)
        plt.close()

    def analyze_energy_trends(self) -> pd.DataFrame:
        """
        Analyzes energy trends over simulation steps.

        Returns:
        - pd.DataFrame: A DataFrame containing energy statistics for each simulation step.
        """
        energy_trends = self.results.query("category == 'agents'").groupby('simulation_steps')['energy'].agg([
            'mean', 'median', 'min', 'max', 'std'
        ])
        return energy_trends

    def visualize_energy_trends(self, file_path: str) -> None:
        """
        Visualizes energy trends over simulation steps.

        Parameters:
        - file_path (str): The file path to save the plot.
        """
        energy_trends = self.analyze_energy_trends()
        
        plt.figure(figsize=(12, 8))
        plt.plot(energy_trends.index, energy_trends['mean'], label='Mean Energy')
        plt.fill_between(energy_trends.index, 
                         energy_trends['mean'] - energy_trends['std'],
                         energy_trends['mean'] + energy_trends['std'],
                         alpha=0.3, label='Standard Deviation')
        plt.plot(energy_trends.index, energy_trends['median'], label='Median Energy', linestyle='--')
        plt.xlabel('Simulation Steps', fontsize=14)
        plt.ylabel('Energy', fontsize=14)
        plt.title('Agent Energy Trends Over Simulation', fontsize=16)
        plt.legend(fontsize=12)
        plt.grid(True, linestyle=':', alpha=0.7)
        plt.tight_layout()
        plt.savefig(file_path, dpi=300)
        plt.close()

    def generate_comprehensive_report(self, output_dir: str) -> None:
        """
        Generates a comprehensive report including all statistics and visualizations.

        Parameters:
        - output_dir (str): The directory to save the report files.
        """
        import os
        os.makedirs(output_dir, exist_ok=True)

        # Generate summary statistics
        summary = self.compute_summary_statistics()
        with open(os.path.join(output_dir, 'summary_statistics.txt'), 'w') as f:
            for field, value in summary.__dict__.items():
                f.write(f"{field}: {value}\n")

        # Generate agent type statistics
        agent_stats = self.compute_agent_type_statistics()
        agent_stats.to_csv(os.path.join(output_dir, 'agent_type_statistics.csv'))

        # Generate visualizations
        self.visualize_agent_energy_distribution(os.path.join(output_dir, 'agent_energy_distribution.png'))
        self.visualize_energy_trends(os.path.join(output_dir, 'energy_trends.png'))

        # Generate energy trends data
        energy_trends = self.analyze_energy_trends()
        energy_trends.to_csv(os.path.join(output_dir, 'energy_trends.csv'))

        print(f"Comprehensive report generated in {output_dir}")

# Example usage
# results = load_simulation_results(file_path)
# stats = EnhancedSimulationStatistics(results)
# stats.generate_comprehensive_report('simulation_report')
