import matplotlib.pyplot as plt
import matplotlib.animation as animation

class SimulationRenderer:
    def __init__(self, simulation_environment, nests, agents):
        self.simulation_environment = simulation_environment
        self.nests = nests
        self.agents = agents
        self.fig, self.ax = plt.subplots()
        self.setup_plot_environment()
    
    def setup_plot_environment(self):
        """Configure the plot environment for the simulation."""
        self.ax.set_xlim(0, self.simulation_environment.width)
        self.ax.set_ylim(0, self.simulation_environment.height)
        self.ax.set_title('Simulation Environment Setup')
    
    def plot_entities(self, entities, color, label):
        """Generic method to plot entities on the simulation environment."""
        positions = [(entity.x, entity.y) for entity in entities]
        if positions:
            self.ax.scatter(*zip(*positions), c=color, label=label)
    
    def refresh_environment(self, frame=None):
        """Refresh the environment for the next frame or step."""
        self.ax.clear()
        self.setup_plot_environment()
        if frame is not None:
            self.ax.set_title(f'Simulation Step: {frame}')
        self.plot_entities(self.nests, 'r', 'Nests')
        self.plot_entities(self.agents, 'b', 'Agents')
    
    def animate_simulation(self, steps):
        """Animate the simulation over a given number of steps."""
        animation.FuncAnimation(self.fig, self.refresh_environment, frames=steps, interval=100)
        plt.legend()
        plt.show()
    
    def render_post_simulation(self, simulation_results):
        """Visualize the results after the simulation has concluded."""
        self.refresh_environment()
        self.ax.set_title('Post-Simulation Analysis')
        # Extend with specific post-simulation visualization logic
        plt.show()
