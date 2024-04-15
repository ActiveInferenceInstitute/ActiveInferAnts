import time
import logging
from render_Simulation import SimulationRenderer
from situational_Awareness import AgentVisualizer
from plan_Simulation import SimulationPlanner
import numpy as np
from ActiveInferenceSimulation import ActiveInferenceSimulation
import config
import metaconfig

class SimulationExecutor:
    def __init__(self, visualization_interval=100, pause_duration=0.1, log_level=logging.INFO):
        self.simulation = SimulationPlanner().create_simulation()
        self.renderer = SimulationRenderer(*self.simulation.get_visualization_parameters())
        self.visualization_interval = visualization_interval
        self.pause_duration = pause_duration
        self.configure_logging(log_level)
    
    def configure_logging(self, log_level):
        logging.basicConfig(level=log_level, format='%(asctime)s - %(levelname)s - %(message)s')
    
    def initialize_environment(self):
        self._safely_execute(self.renderer.initialize_environment, "Environment initialization.")
    
    def perform_simulation(self):
        max_steps = self.simulation.environment.max_steps
        logging.info(f"Simulation commencing for {max_steps} steps.")
        for step in range(max_steps):
            self._safely_execute(lambda: self._execute_simulation_step(step), f"Step {step} execution")
    
    def _execute_simulation_step(self, step):
        self.simulation.progress()
        if step % self.visualization_interval == 0:
            self._optional_visualization(step)
        self.renderer.refresh_visualization(step)
        time.sleep(self.pause_duration)
    
    def _optional_visualization(self, step):
        logging.info(f"Optional data visualization at step {step}")
        for agent in self.simulation.agents:
            AgentVisualizer.visualize(agent)
    
    def conclude_simulation(self):
        self._safely_execute(lambda: self.renderer.visualize_post_simulation(self.simulation.aggregate_results()), "Simulation conclusion.")
    
    def run(self):
        logging.info("Simulation sequence initiation.")
        simulation_steps = [("Environment initialization", self.initialize_environment), 
                            ("Simulation execution", self.perform_simulation), 
                            ("Simulation conclusion", self.conclude_simulation)]
        for description, step_function in simulation_steps:
            logging.info(f"{description} in progress.")
            step_function()
    
    def _safely_execute(self, operation, description):
        try:
            operation()
        except Exception as e:
            logging.error(f"{description} error: {e}", exc_info=True)

if __name__ == "__main__":
    SimulationExecutor().run()
