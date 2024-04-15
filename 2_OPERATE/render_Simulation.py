import matplotlib.pyplot as plt
import matplotlib.animation as animation

class SimulationRenderer:
    def __init__(self, simulation_environment, nests, agents):
        self.simulation_environment = simulation_environment
        self.nests = nests
        self.agents = agents
        self.fig, self.ax = plt.subplots()
        self._configure_plot_environment()
    
    def _configure_plot_environment(self):
        """Internal method to set up the plot environment for the simulation."""
        self.ax.set_xlim(0, self.simulation_environment.width)
        self.ax.set_ylim(0, self.simulation_environment.height)
        self.ax.set_title('Simulation Environment Setup')
    
    def _plot_entities(self, entities, color, label):
        """Internal method to plot entities on the simulation environment."""
        positions = [(entity.x, entity.y) for entity in entities if hasattr(entity, 'x') and hasattr(entity, 'y')]
        if positions:
            self.ax.scatter(*zip(*positions), c=color, label=label, alpha=0.6, edgecolors='w')
    
    def _refresh_environment(self, frame=None):
        """Internal method to refresh the environment for the next frame or step."""
        self.ax.clear()
        self._configure_plot_environment()
        if frame is not None:
            self.ax.set_title(f'Simulation Step: {frame}')
        self._plot_entities(self.nests, 'r', 'Nests')
        self._plot_entities(self.agents, 'b', 'Agents')
    
    def animate_simulation(self, steps):
        """Animate the simulation over a given number of steps."""
        anim = animation.FuncAnimation(self.fig, self._refresh_environment, frames=steps, interval=100)
        plt.legend()
        plt.show()
        return anim
    
    def render_post_simulation(self, simulation_results):
        """Visualize the results after the simulation has concluded."""
        self._refresh_environment()
        self.ax.set_title('Post-Simulation Analysis')
        # Implement specific post-simulation visualization logic based on simulation_results
        plt.show()
