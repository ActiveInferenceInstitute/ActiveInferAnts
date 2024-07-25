import time
import logging
from typing import List, Tuple, Callable
from render_Simulation import SimulationRenderer
from situational_Awareness import AgentVisualizer
from plan_Simulation import SimulationPlanner
from ActiveInferenceSimulation import ActiveInferenceSimulation
import config
import metaconfig

class SimulationExecutor:
    def __init__(self, visualization_interval: int = 100, pause_duration: float = 0.1, log_level: int = logging.INFO):
        self.simulation: ActiveInferenceSimulation = SimulationPlanner().create_simulation()
        self.renderer: SimulationRenderer = SimulationRenderer(*self.simulation.get_visualization_parameters())
        self.visualization_interval: int = visualization_interval
        self.pause_duration: float = pause_duration
        self.configure_logging(log_level)
    
    def configure_logging(self, log_level: int) -> None:
        logging.basicConfig(level=log_level, format='%(asctime)s - %(levelname)s - %(message)s')
    
    def initialize_environment(self) -> None:
        self._safely_execute(self.renderer.initialize_environment, "Environment initialization")
    
    def perform_simulation(self) -> None:
        max_steps: int = self.simulation.environment.max_steps
        logging.info(f"Simulation commencing for {max_steps} steps.")
        for step in range(max_steps):
            self._safely_execute(lambda: self._execute_simulation_step(step), f"Step {step} execution")
    
    def _execute_simulation_step(self, step: int) -> None:
        self.simulation.progress()
        if step % self.visualization_interval == 0:
            self._optional_visualization(step)
        self.renderer.refresh_visualization(step)
        time.sleep(self.pause_duration)
    
    def _optional_visualization(self, step: int) -> None:
        logging.info(f"Optional data visualization at step {step}")
        for agent in self.simulation.agents:
            AgentVisualizer.visualize(agent)
    
    def conclude_simulation(self) -> None:
        self._safely_execute(
            lambda: self.renderer.visualize_post_simulation(self.simulation.aggregate_results()),
            "Simulation conclusion"
        )
    
    def run(self) -> None:
        logging.info("Simulation sequence initiation.")
        simulation_steps: List[Tuple[str, Callable[[], None]]] = [
            ("Environment initialization", self.initialize_environment),
            ("Simulation execution", self.perform_simulation),
            ("Simulation conclusion", self.conclude_simulation)
        ]
        for description, step_function in simulation_steps:
            logging.info(f"{description} in progress.")
            step_function()
    
    def _safely_execute(self, operation: Callable[[], None], description: str) -> None:
        try:
            operation()
        except Exception as e:
            logging.error(f"{description} error: {e}", exc_info=True)
            raise  # Re-raise the exception for higher-level error handling

if __name__ == "__main__":
    try:
        SimulationExecutor().run()
    except Exception as e:
        logging.critical(f"Simulation failed: {e}", exc_info=True)
