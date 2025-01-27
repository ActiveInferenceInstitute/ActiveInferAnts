"""
Visualization utilities for Brainfuck Active Inference simulation.
"""
import matplotlib.pyplot as plt
import numpy as np
from typing import List, Dict
import seaborn as sns
import networkx as nx
from scipy import stats
from typing import Optional, Tuple
import pandas as pd

class ActiveInferenceVisualizer:
    def __init__(self):
        self.history = {
            'sensory_input': [],
            'prediction': [],
            'free_energy': [],
            'action': [],
            'uncertainty': [],
            'temporal_integration': [],
            'prediction_error': [],
            'complexity': []
        }
        self.graph = nx.DiGraph()
        
    def update(self, tape: List[int], cell_mapping: Dict[str, int]) -> None:
        """Update visualization history with current tape values."""
        self.history['sensory_input'].append(tape[cell_mapping['sensory_input']])
        self.history['prediction'].append(tape[cell_mapping['prediction']])
        self.history['free_energy'].append(tape[cell_mapping['free_energy']])
        self.history['action'].append(tape[cell_mapping['action']])
        self.history['uncertainty'].append(tape[cell_mapping['uncertainty']])
        self.history['temporal_integration'].append(tape[cell_mapping['temporal_integration']])

    def calculate_metrics(self) -> Dict[str, float]:
        """Calculate key metrics from the simulation history."""
        metrics = {
            'mean_free_energy': np.mean(self.history['free_energy']),
            'prediction_accuracy': self._calculate_prediction_accuracy(),
            'uncertainty_reduction': self._calculate_uncertainty_reduction(),
            'temporal_complexity': self._calculate_temporal_complexity()
        }
        return metrics
        
    def _calculate_prediction_accuracy(self) -> float:
        """Calculate prediction accuracy using correlation coefficient."""
        return stats.pearsonr(
            self.history['sensory_input'],
            self.history['prediction']
        )[0]
        
    def _calculate_uncertainty_reduction(self) -> float:
        """Calculate the rate of uncertainty reduction."""
        return (np.mean(self.history['uncertainty'][:10]) - 
                np.mean(self.history['uncertainty'][-10:])) / len(self.history['uncertainty'])
                
    def _calculate_temporal_complexity(self) -> float:
        """Calculate temporal complexity using sample entropy."""
        return stats.entropy(
            np.histogram(self.history['temporal_integration'], bins=20)[0]
        )

    def plot_simulation_results(self, save_path: Optional[str] = None) -> None:
        """Enhanced visualization with additional analysis plots."""
        plt.style.use('seaborn-darkgrid')
        fig = plt.figure(figsize=(20, 16))
        gs = fig.add_gridspec(4, 3)
        
        # Main time series plots
        ax1 = fig.add_subplot(gs[0, :])
        ax1.plot(self.history['sensory_input'], label='Sensory Input', alpha=0.7)
        ax1.plot(self.history['prediction'], label='Prediction', alpha=0.7)
        ax1.fill_between(
            range(len(self.history['uncertainty'])),
            np.array(self.history['prediction']) - np.array(self.history['uncertainty']),
            np.array(self.history['prediction']) + np.array(self.history['uncertainty']),
            alpha=0.2
        )
        ax1.set_title('Sensory Input vs Prediction with Uncertainty')
        ax1.legend()
        
        # Free energy and complexity
        ax2 = fig.add_subplot(gs[1, :2])
        ax2.plot(self.history['free_energy'], 'r-', label='Free Energy')
        ax2.plot(self.history['complexity'], 'b--', label='Complexity')
        ax2.set_title('Free Energy and Complexity')
        ax2.legend()
        
        # Phase space plot
        ax3 = fig.add_subplot(gs[1, 2])
        self._plot_phase_space(ax3)
        
        # Distribution plots
        ax4 = fig.add_subplot(gs[2, 0])
        self._plot_distributions(ax4)
        
        # Information theory metrics
        ax5 = fig.add_subplot(gs[2, 1:])
        self._plot_information_metrics(ax5)
        
        # Summary statistics
        ax6 = fig.add_subplot(gs[3, :])
        self._plot_summary_statistics(ax6)
        
        plt.tight_layout()
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()
        
    def _plot_phase_space(self, ax: plt.Axes) -> None:
        """Plot phase space with attractors."""
        scatter = ax.scatter(
            self.history['prediction'],
            self.history['free_energy'],
            c=range(len(self.history['prediction'])),
            cmap='viridis',
            alpha=0.6
        )
        ax.set_title('Phase Space Dynamics')
        plt.colorbar(scatter, ax=ax, label='Time')
        
    def _plot_distributions(self, ax: plt.Axes) -> None:
        """Plot probability distributions of key variables."""
        for name, data in [
            ('Prediction Error', self.history['prediction_error']),
            ('Free Energy', self.history['free_energy'])
        ]:
            sns.kdeplot(data=data, label=name, ax=ax)
        ax.set_title('Probability Distributions')
        ax.legend()
        
    def _plot_information_metrics(self, ax: plt.Axes) -> None:
        """Plot information theory metrics over time."""
        window_size = 20
        metrics = pd.DataFrame({
            'Entropy': [stats.entropy(self.history['prediction'][i:i+window_size])
                       for i in range(0, len(self.history['prediction'])-window_size)],
            'MI': self._calculate_mutual_information(window_size)
        })
        metrics.plot(ax=ax)
        ax.set_title('Information Theory Metrics')
        
    def _calculate_mutual_information(self, window_size: int) -> List[float]:
        """Calculate rolling mutual information between prediction and sensory input."""
        mi = []
        for i in range(0, len(self.history['prediction'])-window_size):
            x = self.history['prediction'][i:i+window_size]
            y = self.history['sensory_input'][i:i+window_size]
            mi.append(stats.mutual_info_score(
                pd.qcut(x, 5, labels=False),
                pd.qcut(y, 5, labels=False)
            ))
        return mi 