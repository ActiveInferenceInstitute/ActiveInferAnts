import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import LinearSegmentedColormap
import numpy as np

class SimulationRenderer:
    def __init__(self, simulation_environment, nests, agents):
        self.simulation_environment = simulation_environment
        self.nests = nests
        self.agents = agents
        self.fig, self.ax = plt.subplots(figsize=(10, 8))
        self.colormap = self._create_custom_colormap()
        self._configure_plot_environment()
    
    def _create_custom_colormap(self):
        """Create a custom colormap for the simulation."""
        colors = ['#FFFFFF', '#ADD8E6', '#4169E1', '#000080']  # White to dark blue
        return LinearSegmentedColormap.from_list("custom_blue", colors, N=256)
    
    def _configure_plot_environment(self):
        """Set up the plot environment for the simulation."""
        self.ax.set_xlim(0, self.simulation_environment.width)
        self.ax.set_ylim(0, self.simulation_environment.height)
        self.ax.set_title('Ant Colony Optimization Simulation', fontsize=16)
        self.ax.set_xlabel('X Coordinate', fontsize=12)
        self.ax.set_ylabel('Y Coordinate', fontsize=12)
        self.ax.grid(True, linestyle='--', alpha=0.7)
    
    def _plot_entities(self, entities, color, label, marker='o'):
        """Plot entities on the simulation environment."""
        positions = [(entity.x, entity.y) for entity in entities if hasattr(entity, 'x') and hasattr(entity, 'y')]
        if positions:
            x, y = zip(*positions)
            self.ax.scatter(x, y, c=color, label=label, alpha=0.8, edgecolors='w', marker=marker, s=50)
    
    def _plot_pheromone_trails(self):
        """Plot pheromone trails as a heatmap."""
        pheromone_levels = self.simulation_environment.get_pheromone_levels()
        heatmap = self.ax.imshow(pheromone_levels, cmap=self.colormap, alpha=0.5, 
                                 extent=[0, self.simulation_environment.width, 0, self.simulation_environment.height])
        self.fig.colorbar(heatmap, ax=self.ax, label='Pheromone Intensity')
    
    def _refresh_environment(self, frame=None):
        """Refresh the environment for the next frame or step."""
        self.ax.clear()
        self._configure_plot_environment()
        self._plot_pheromone_trails()
        
        if frame is not None:
            self.ax.set_title(f'Ant Colony Optimization - Step: {frame}', fontsize=16)
        
        self._plot_entities(self.nests, 'red', 'Nests', marker='s')
        self._plot_entities(self.agents, 'black', 'Ants', marker='^')
        
        self.ax.legend(loc='upper right', fontsize=10)
    
    def animate_simulation(self, steps):
        """Animate the simulation over a given number of steps."""
        anim = animation.FuncAnimation(self.fig, self._refresh_environment, frames=steps, interval=200, blit=False)
        plt.tight_layout()
        plt.show()
        return anim
    
    def render_post_simulation(self, simulation_results):
        """Visualize the results after the simulation has concluded."""
        self._refresh_environment()
        self.ax.set_title('Post-Simulation Analysis', fontsize=16)
        
        # Implement specific post-simulation visualization logic based on simulation_results
        # For example, plot the best path found, convergence graph, etc.
        if 'best_path' in simulation_results:
            path = simulation_results['best_path']
            x, y = zip(*path)
            self.ax.plot(x, y, 'g-', linewidth=2, label='Best Path')
        
        if 'convergence' in simulation_results:
            convergence_data = simulation_results['convergence']
            ax2 = self.ax.twinx()
            ax2.plot(convergence_data, 'r--', label='Convergence')
            ax2.set_ylabel('Convergence Metric', color='r', fontsize=12)
            ax2.tick_params(axis='y', labelcolor='r')
        
        self.ax.legend(loc='upper left', fontsize=10)
        plt.tight_layout()
        plt.show()
