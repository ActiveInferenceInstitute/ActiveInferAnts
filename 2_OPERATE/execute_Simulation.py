import time
import logging
from render_Simulation import SimulationRenderer
from situational_Antwareness import visualize_agent_internals
from plan_Simulation import plan_simulation
import numpy as np
from MetaInformAnt_Simulation import MetaInformAntSimulation
import config
import metaconfig

class SimulationExecutor:
    def __init__(self, visualization_frequency=100, sleep_duration=0.1):
        self.simulation = plan_simulation()
        self.renderer = SimulationRenderer(*self.simulation.get_rendering_params())
        self.visualization_frequency = visualization_frequency
        self.sleep_duration = sleep_duration
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    
    def setup_environment(self):
        self._attempt_operation(self.renderer.setup_environment, "Environment setup initiated.")
    
    def execute_steps(self):
        logging.info(f"Executing simulation steps up to {self.simulation.simulation_environment.max_steps}.")
        for step in range(self.simulation.simulation_environment.max_steps):
            self._attempt_operation(lambda: self._simulation_step(step), f"Executing step {step}")
    
    def _simulation_step(self, step):
        self.simulation.update()
        if step % self.visualization_frequency == 0:
            self.optional_visualization(step)
        self.renderer.update_visualization(step)
        time.sleep(self.sleep_duration)
    
    def optional_visualization(self, step):
        logging.info(f"Optional visualization at step {step}")
        for agent in self.simulation.agents:
            visualize_agent_internals(agent)
    
    def post_simulation(self):
        self._attempt_operation(lambda: self.renderer.render_post_simulation(self.simulation.collect_results()), "Finalizing simulation.")
    
    def run(self):
        logging.info("Simulation execution sequence initiated.")
        operations = [("Environment setup", self.setup_environment), 
                      ("Simulation execution", self.execute_steps), 
                      ("Simulation finalization", self.post_simulation)]
        for description, operation in operations:
            logging.info(f"{description} started.")
            operation()
    
    def _attempt_operation(self, operation, description):
        try:
            operation()
        except Exception as e:
            logging.error(f"Failed during {description}: {e}", exc_info=True)

if __name__ == "__main__":
    SimulationExecutor().run()
