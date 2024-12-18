import time
import logging
from typing import List, Tuple, Callable, Optional, Dict, Any

from render_Simulation import SimulationRenderer
from situational_Antwareness import AgentVisualizer
from plan_Simulation import SimulationPlanner
from MetaInformAnt_Simulation import MetaInformAntSimulation
import config
import metaconfig
from data_logging import DataLogger
from performance_monitor import PerformanceMonitor
from error_handling import SimulationError, handle_simulation_error
from report_generator import ReportGenerator


class SimulationExecutor:
    """
    Executes and manages the simulation lifecycle, including initialization,
    execution, monitoring, and conclusion.
    """

    def __init__(
        self,
        visualization_interval: int = 100,
        pause_duration: float = 0.1,
        log_level: int = logging.INFO
    ):
        """
        Initializes the SimulationExecutor with default or specified parameters.

        Args:
            visualization_interval (int): Interval at which visualizations occur.
            pause_duration (float): Pause duration between simulation steps.
            log_level (int): Logging level.
        """
        self.simulation: Optional[MetaInformAntSimulation] = None
        self.renderer: Optional[SimulationRenderer] = None
        self.visualization_interval: int = visualization_interval
        self.pause_duration: float = pause_duration
        self.data_logger: DataLogger = DataLogger()
        self.performance_monitor: PerformanceMonitor = PerformanceMonitor()
        self.report_generator: ReportGenerator = ReportGenerator()
        self.configure_logging(log_level)

    def configure_logging(self, log_level: int) -> None:
        """
        Configures the logging settings.

        Args:
            log_level (int): The logging level to set.
        """
        logging.basicConfig(
            level=log_level,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(self.__class__.__name__)

    def initialize_simulation(self) -> None:
        """
        Initializes the simulation environment and related components.
        """
        try:
            planner = SimulationPlanner()
            self.simulation = planner.create_simulation()
            self.renderer = SimulationRenderer(*self.simulation.get_visualization_parameters())
            self.data_logger.initialize(self.simulation)
            self.performance_monitor.start()
            self.logger.info("Simulation initialized successfully.")
        except Exception as e:
            handle_simulation_error(e, "Simulation initialization failed")

    def initialize_environment(self) -> None:
        """
        Initializes the simulation environment safely.
        """
        self._safely_execute(
            self.renderer.initialize_environment,
            "Environment initialization"
        )

    def perform_simulation(self) -> None:
        """
        Executes the simulation steps with monitoring and parameter adjustments.
        """
        if not self.simulation:
            raise SimulationError("Simulation not initialized")

        max_steps: int = self.simulation.environment.max_steps
        self.logger.info(f"Simulation commencing for {max_steps} steps.")

        for step in range(max_steps):
            self._safely_execute(
                lambda: self._execute_simulation_step(step),
                f"Step {step} execution"
            )

            if self.performance_monitor.should_adjust_parameters(step):
                self._adjust_simulation_parameters()

            if self.simulation.should_terminate_early():
                self.logger.info(f"Early termination condition met at step {step}")
                break

    def _execute_simulation_step(self, step: int) -> None:
        """
        Executes a single simulation step.

        Args:
            step (int): The current simulation step number.
        """
        if not self.simulation or not self.renderer:
            raise SimulationError("Simulation or renderer not initialized")

        self.simulation.progress()
        self.data_logger.log_step(step, self.simulation)

        if step % self.visualization_interval == 0:
            self._optional_visualization(step)

        self.renderer.refresh_visualization(step)
        time.sleep(self.pause_duration)

    def _optional_visualization(self, step: int) -> None:
        """
        Performs optional visualization at specified intervals.

        Args:
            step (int): The current simulation step number.
        """
        self.logger.info(f"Optional data visualization at step {step}")
        for agent in self.simulation.agents:
            visualizer = AgentVisualizer(agent)
            visualizer.visualize()

    def _adjust_simulation_parameters(self) -> None:
        """
        Adjusts simulation parameters based on performance metrics.
        """
        if self.simulation:
            new_params: Dict[str, Any] = self.performance_monitor.suggest_parameter_adjustments()
            self.simulation.update_parameters(new_params)
            self.logger.info(f"Adjusted simulation parameters: {new_params}")

    def conclude_simulation(self) -> None:
        """
        Concludes the simulation by finalizing components and generating reports.
        """
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
        """
        Generates and saves the final simulation report.
        """
        report_data: Dict[str, Any] = {
            'simulation_data': self.data_logger.generate_report(),
            'performance_metrics': self.performance_monitor.get_metrics(),
            'simulation_parameters': self.simulation.get_parameters() if self.simulation else {},
            'environment_state': self.simulation.environment.get_state() if self.simulation else {}
        }
        report: str = self.report_generator.generate_report(report_data)
        self.logger.info("Final simulation report generated.")
        self._save_report(report)

    def _save_report(self, report: str) -> None:
        """
        Saves the simulation report to a file.

        Args:
            report (str): The report content to save.
        """
        report_file = 'simulation_report.txt'
        try:
            with open(report_file, 'w') as file:
                file.write(report)
            self.logger.info(f"Simulation report saved to {report_file}")
        except IOError as e:
            self.logger.error(f"Failed to save simulation report: {e}")

    def run(self) -> None:
        """
        Runs the complete simulation sequence.
        """
        self.logger.info("Simulation sequence initiation.")
        simulation_steps: List[Tuple[str, Callable[[], None]]] = [
            ("Simulation initialization", self.initialize_simulation),
            ("Environment initialization", self.initialize_environment),
            ("Simulation execution", self.perform_simulation),
            ("Simulation conclusion", self.conclude_simulation)
        ]

        for description, step_function in simulation_steps:
            self.logger.info(f"{description} in progress.")
            step_function()

    def _safely_execute(self, operation: Callable[[], None], description: str) -> None:
        """
        Executes a callable operation safely, handling exceptions.

        Args:
            operation (Callable[[], None]): The operation to execute.
            description (str): Description of the operation for error handling.
        """
        try:
            operation()
        except Exception as e:
            handle_simulation_error(e, f"{description} failed")


def main() -> None:
    """
    Entry point for executing the simulation.
    """
    executor = SimulationExecutor()
    try:
        executor.run()
    except SimulationError as se:
        logging.critical(f"Simulation failed: {se}", exc_info=True)
    except Exception as e:
        logging.critical(f"Unexpected error: {e}", exc_info=True)
    finally:
        # Perform necessary cleanup
        if executor.performance_monitor:
            executor.performance_monitor.stop()
        if executor.data_logger:
            executor.data_logger.finalize()


if __name__ == "__main__":
    main()
