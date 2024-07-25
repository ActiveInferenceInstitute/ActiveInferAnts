import time
import logging
from typing import List, Tuple, Callable, Optional
from render_Simulation import SimulationRenderer
from situational_Antwareness import AgentVisualizer
from plan_Simulation import SimulationPlanner
from MetaInformAnt_Simulation import MetaInformAntSimulation
import config
import metaconfig
from data_logging import DataLogger
from performance_monitor import PerformanceMonitor
from error_handling import SimulationError, handle_simulation_error

class SimulationExecutor:
    def __init__(self, visualization_interval: int = 100, pause_duration: float = 0.1, log_level: int = logging.INFO):
        self.simulation: Optional[MetaInformAntSimulation] = None
        self.renderer: Optional[SimulationRenderer] = None
        self.visualization_interval: int = visualization_interval
        self.pause_duration: float = pause_duration
        self.data_logger: DataLogger = DataLogger()
        self.performance_monitor: PerformanceMonitor = PerformanceMonitor()
        self.configure_logging(log_level)
    
    def configure_logging(self, log_level: int) -> None:
        logging.basicConfig(level=log_level, format='%(asctime)s - %(levelname)s - %(message)s')
    
    def initialize_simulation(self) -> None:
        try:
            self.simulation = SimulationPlanner().create_simulation()
            self.renderer = SimulationRenderer(*self.simulation.get_visualization_parameters())
            self.data_logger.initialize(self.simulation)
            self.performance_monitor.start()
        except Exception as e:
            handle_simulation_error(e, "Simulation initialization failed")
    
    def initialize_environment(self) -> None:
        self._safely_execute(self.renderer.initialize_environment, "Environment initialization")
    
    def perform_simulation(self) -> None:
        if not self.simulation:
            raise SimulationError("Simulation not initialized")
        
        max_steps: int = self.simulation.environment.max_steps
        logging.info(f"Simulation commencing for {max_steps} steps.")
        
        for step in range(max_steps):
            self._safely_execute(lambda: self._execute_simulation_step(step), f"Step {step} execution")
            
            if self.performance_monitor.should_adjust_parameters(step):
                self._adjust_simulation_parameters()
            
            if self.simulation.should_terminate_early():
                logging.info(f"Early termination condition met at step {step}")
                break
    
    def _execute_simulation_step(self, step: int) -> None:
        if not self.simulation or not self.renderer:
            raise SimulationError("Simulation or renderer not initialized")
        
        self.simulation.progress()
        self.data_logger.log_step(step, self.simulation)
        
        if step % self.visualization_interval == 0:
            self._optional_visualization(step)
        
        self.renderer.refresh_visualization(step)
        time.sleep(self.pause_duration)
    
    def _optional_visualization(self, step: int) -> None:
        logging.info(f"Optional data visualization at step {step}")
        if self.simulation:
            for agent in self.simulation.agents:
                AgentVisualizer(agent).visualize()
    
    def _adjust_simulation_parameters(self) -> None:
        if self.simulation:
            new_params = self.performance_monitor.suggest_parameter_adjustments()
            self.simulation.update_parameters(new_params)
            logging.info(f"Adjusted simulation parameters: {new_params}")
    
    def conclude_simulation(self) -> None:
        if not self.simulation or not self.renderer:
            raise SimulationError("Simulation or renderer not initialized")
        
        self._safely_execute(
            lambda: self.renderer.visualize_post_simulation(self.simulation.aggregate_results()),
            "Simulation conclusion"
        )
        self.data_logger.finalize()
        self.performance_monitor.stop()
        self._generate_final_report()
    
    def _generate_final_report(self) -> None:
        report = self.data_logger.generate_report()
        performance_metrics = self.performance_monitor.get_metrics()
        logging.info("Generating final simulation report")
        # TODO: Implement report generation logic
    
    def run(self) -> None:
        logging.info("Simulation sequence initiation.")
        simulation_steps: List[Tuple[str, Callable[[], None]]] = [
            ("Simulation initialization", self.initialize_simulation),
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
            handle_simulation_error(e, f"{description} failed")

if __name__ == "__main__":
    executor = SimulationExecutor()
    try:
        executor.run()
    except SimulationError as se:
        logging.critical(f"Simulation failed: {se}", exc_info=True)
    except Exception as e:
        logging.critical(f"Unexpected error: {e}", exc_info=True)
    finally:
        # Perform any necessary cleanup
        if executor.performance_monitor:
            executor.performance_monitor.stop()
        if executor.data_logger:
            executor.data_logger.finalize()
