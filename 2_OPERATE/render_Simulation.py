import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import LinearSegmentedColormap
import numpy as np
from typing import List, Dict, Any, Optional
from dataclasses import dataclass

@dataclass
class Entity:
    x: float
    y: float

class SimulationRenderer:
    def __init__(self, simulation_environment: Any, nests: List[Entity], agents: List[Entity]):
        self.simulation_environment = simulation_environment
        self.nests = nests
        self.agents = agents
        self.fig, self.ax = plt.subplots(figsize=(12, 10))
        self.colormap = self._create_custom_colormap()
        self._configure_plot_environment()
        self.animation: Optional[animation.FuncAnimation] = None
    
    def _create_custom_colormap(self) -> LinearSegmentedColormap:
        """Create a custom colormap for the simulation."""
        colors = ['#FFFFFF', '#E6F3FF', '#ADD8E6', '#4169E1', '#000080']  # Enhanced gradient: White to dark blue
        return LinearSegmentedColormap.from_list("custom_blue", colors, N=256)
    
    def _configure_plot_environment(self) -> None:
        """Set up the plot environment for the simulation."""
        self.ax.set_xlim(0, self.simulation_environment.width)
        self.ax.set_ylim(0, self.simulation_environment.height)
        self.ax.set_title('Advanced Ant Colony Optimization Simulation', fontsize=18, fontweight='bold')
        self.ax.set_xlabel('X Coordinate', fontsize=14)
        self.ax.set_ylabel('Y Coordinate', fontsize=14)
        self.ax.grid(True, linestyle='--', alpha=0.7)
        self.ax.set_facecolor('#F0F0F0')  # Light gray background
    
    def _plot_entities(self, entities: List[Entity], color: str, label: str, marker: str = 'o', size: int = 50) -> None:
        """Plot entities on the simulation environment."""
        positions = [(entity.x, entity.y) for entity in entities]
        if positions:
            x, y = zip(*positions)
            self.ax.scatter(x, y, c=color, label=label, alpha=0.8, edgecolors='w', marker=marker, s=size)
    
    def _plot_pheromone_trails(self) -> None:
        """Plot pheromone trails as a heatmap with enhanced visualization."""
        pheromone_levels = self.simulation_environment.get_pheromone_levels()
        heatmap = self.ax.imshow(pheromone_levels, cmap=self.colormap, alpha=0.6, 
                                 extent=[0, self.simulation_environment.width, 0, self.simulation_environment.height],
                                 interpolation='gaussian')
        colorbar = self.fig.colorbar(heatmap, ax=self.ax, label='Pheromone Intensity', pad=0.02)
        colorbar.ax.tick_params(labelsize=10)
        colorbar.set_label('Pheromone Intensity', fontsize=12, fontweight='bold')
    
    def _refresh_environment(self, frame: Optional[int] = None) -> None:
        """Refresh the environment for the next frame or step."""
        self.ax.clear()
        self._configure_plot_environment()
        self._plot_pheromone_trails()
        
        if frame is not None:
            self.ax.set_title(f'Advanced Ant Colony Optimization - Step: {frame}', fontsize=18, fontweight='bold')
        
        self._plot_entities(self.nests, 'red', 'Nests', marker='s', size=80)
        self._plot_entities(self.agents, 'black', 'Ants', marker='^', size=60)
        
        legend = self.ax.legend(loc='upper right', fontsize=12, framealpha=0.9, edgecolor='black')
        legend.get_frame().set_facecolor('#F0F0F0')
    
    def animate_simulation(self, steps: int) -> animation.FuncAnimation:
        """Animate the simulation over a given number of steps."""
        self.animation = animation.FuncAnimation(self.fig, self._refresh_environment, frames=steps, interval=200, blit=False)
        plt.tight_layout()
        return self.animation
    
    def render_post_simulation(self, simulation_results: Dict[str, Any]) -> None:
        """Visualize the results after the simulation has concluded."""
        self._refresh_environment()
        self.ax.set_title('Post-Simulation Analysis', fontsize=18, fontweight='bold')
        
        if 'best_path' in simulation_results:
            path = simulation_results['best_path']
            x, y = zip(*path)
            self.ax.plot(x, y, 'g-', linewidth=3, label='Best Path', alpha=0.8)
        
        if 'convergence' in simulation_results:
            convergence_data = simulation_results['convergence']
            ax2 = self.ax.twinx()
            ax2.plot(convergence_data, 'r--', label='Convergence', linewidth=2)
            ax2.set_ylabel('Convergence Metric', color='r', fontsize=14, fontweight='bold')
            ax2.tick_params(axis='y', labelcolor='r', labelsize=10)
            ax2.spines['right'].set_color('r')
        
        if 'performance_metrics' in simulation_results:
            metrics = simulation_results['performance_metrics']
            text_box = f"Avg. Path Length: {metrics['avg_path_length']:.2f}\n"
            text_box += f"Solution Quality: {metrics['solution_quality']:.2f}\n"
            text_box += f"Convergence Time: {metrics['convergence_time']:.2f} steps"
            self.ax.text(0.02, 0.98, text_box, transform=self.ax.transAxes, fontsize=10,
                         verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
        
        handles, labels = self.ax.get_legend_handles_labels()
        handles2, labels2 = ax2.get_legend_handles_labels() if 'convergence' in simulation_results else ([], [])
        self.ax.legend(handles + handles2, labels + labels2, loc='upper left', fontsize=12, framealpha=0.9, edgecolor='black')
        
        plt.tight_layout()
        plt.show()
    
    def save_animation(self, filename: str, fps: int = 30, dpi: int = 200) -> None:
        """Save the animation to a file."""
        if self.animation:
            self.animation.save(filename, fps=fps, dpi=dpi, writer='ffmpeg')
        else:
            print("No animation to save. Run animate_simulation first.")
    
    def plot_performance_over_time(self, performance_data: Dict[str, List[float]]) -> None:
        """Plot various performance metrics over time."""
        fig, ax = plt.subplots(figsize=(12, 6))
        for metric, values in performance_data.items():
            ax.plot(values, label=metric.replace('_', ' ').title())
        
        ax.set_xlabel('Simulation Step', fontsize=14)
        ax.set_ylabel('Metric Value', fontsize=14)
        ax.set_title('Performance Metrics Over Time', fontsize=18, fontweight='bold')
        ax.legend(loc='best', fontsize=12)
        ax.grid(True, linestyle='--', alpha=0.7)
        plt.tight_layout()
        plt.show()
