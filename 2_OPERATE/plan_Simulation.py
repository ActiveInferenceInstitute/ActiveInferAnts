import numpy as np
import logging
import config
import metaconfig
from typing import Dict, Any, Optional, List
from MetaInformAnt_Simulation import MetaInformAntSimulation
from computational_resources import estimate_computational_resources
from initialize_Nestmate_Colony import initialize_colony
from environment import Environment
from data_logging import DataLogger
from visualization import SimulationVisualizer
from performance_metrics import PerformanceTracker
from exception_handling import SimulationExceptionHandler
from multiprocessing import Pool
from tqdm import tqdm

# Configure logging to provide detailed insights during the simulation process
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class SimulationSetup:
    def __init__(self):
        self.simulation_environment = self.initialize_environment()
        self.agent_params = metaconfig.META_CONFIG['ANT_AND_COLONY']['AGENT_PARAMS']
        self.niche_params = metaconfig.META_CONFIG['ANT_AND_COLONY']['NICHE_PARAMS']
        self.parallel_execution = config.SIMULATION_SETTINGS['PARALLEL_EXECUTION']
        self.validate_parallel_execution_settings()
        self.colony = self.initialize_colony()
        self.computational_load = self.estimate_computational_load()
        self.data_logger = DataLogger()
        self.visualizer = SimulationVisualizer()
        self.performance_tracker = PerformanceTracker()
        self.exception_handler = SimulationExceptionHandler()

    def initialize_environment(self) -> Environment:
        """Initialize and return the simulation environment."""
        try:
            env_config = config.ENVIRONMENT_CONFIG
            env_config['random_seed'] = np.random.randint(0, 1000000)  # Add randomness for each run
            return Environment(**env_config)
        except Exception as e:
            logger.error(f"Failed to initialize environment: {e}", exc_info=True)
            raise

    def validate_parallel_execution_settings(self) -> None:
        """Validate parallel execution settings."""
        try:
            if not isinstance(self.parallel_execution['ENABLED'], bool):
                raise ValueError("Parallel execution 'ENABLED' setting must be a boolean.")
            if not isinstance(self.parallel_execution['WORKER_COUNT'], int) or self.parallel_execution['WORKER_COUNT'] <= 0:
                raise ValueError("Parallel execution 'WORKER_COUNT' must be a positive integer.")
            if self.parallel_execution['ENABLED'] and self.parallel_execution['WORKER_COUNT'] > config.SIMULATION_SETTINGS['AGENT_COUNT']:
                logger.warning("Worker count exceeds agent count. Adjusting worker count.")
                self.parallel_execution['WORKER_COUNT'] = config.SIMULATION_SETTINGS['AGENT_COUNT']
        except Exception as e:
            logger.error(f"Invalid parallel execution settings: {e}", exc_info=True)
            raise

    def initialize_colony(self) -> Any:
        """Initialize the colony with the given configuration."""
        try:
            return initialize_colony(
                nest_count=config.SIMULATION_SETTINGS['NEST_COUNT'],
                agent_count_per_nest=config.SIMULATION_SETTINGS['AGENT_COUNT'] // config.SIMULATION_SETTINGS['NEST_COUNT'],
                env_config=config.ENVIRONMENT_CONFIG,
                ant_config=config.ANT_AND_COLONY_CONFIG['NESTMATE'],
                meta_config=metaconfig.META_CONFIG
            )
        except Exception as e:
            logger.error(f"Failed to initialize colony: {e}", exc_info=True)
            raise

    def estimate_computational_load(self) -> Dict[str, Any]:
        """Estimate the computational resources required for the simulation."""
        try:
            return estimate_computational_resources(
                num_agents=config.SIMULATION_SETTINGS['AGENT_COUNT'],
                num_food_sources=config.SIMULATION_SETTINGS['FOOD_SOURCE_COUNT'],
                num_nests=config.SIMULATION_SETTINGS['NEST_COUNT'],
                max_steps=config.SIMULATION_SETTINGS['MAX_STEPS'],
                parallel_execution=self.parallel_execution
            )
        except Exception as e:
            logger.error(f"Failed to estimate computational load: {e}", exc_info=True)
            raise

    def prepare_simulation(self) -> MetaInformAntSimulation:
        """Prepare the simulation environment and log the estimated computational load."""
        logger.info("Preparing simulation with current configuration.")
        simulation = self.create_simulation_instance()
        logger.info(f"Estimated computational load: {self.computational_load}")
        return simulation

    def create_simulation_instance(self) -> MetaInformAntSimulation:
        """Create an instance of the simulation with the configured parameters."""
        return MetaInformAntSimulation(
            num_agents=config.SIMULATION_SETTINGS['AGENT_COUNT'],
            simulation_environment=self.simulation_environment,
            num_food_sources=config.SIMULATION_SETTINGS['FOOD_SOURCE_COUNT'],
            num_nests=config.SIMULATION_SETTINGS['NEST_COUNT'],
            agent_params=self.agent_params,
            niche_params=self.niche_params,
            colony=self.colony,
            data_logger=self.data_logger,
            visualizer=self.visualizer,
            performance_tracker=self.performance_tracker
        )

    def run_simulation(self, max_steps: Optional[int] = None) -> Dict[str, Any]:
        """Run the simulation and return the results."""
        simulation = self.prepare_simulation()
        max_steps = max_steps or config.SIMULATION_SETTINGS['MAX_STEPS']
        
        logger.info(f"Starting simulation for {max_steps} steps.")
        try:
            results = simulation.run(max_steps)
            logger.info("Simulation completed successfully.")
        except Exception as e:
            logger.error(f"Simulation failed: {e}", exc_info=True)
            results = self.exception_handler.handle_simulation_error(e)
        
        self.post_simulation_analysis(results)
        return results

    def post_simulation_analysis(self, results: Dict[str, Any]) -> None:
        """Perform post-simulation analysis and visualization."""
        self.data_logger.save_results(results)
        self.visualizer.create_summary_plots(results)
        performance_metrics = self.performance_tracker.calculate_metrics(results)
        logger.info(f"Performance metrics: {performance_metrics}")

    def run_multiple_simulations(self, num_simulations: int) -> List[Dict[str, Any]]:
        """Run multiple simulations and return a list of results."""
        if self.parallel_execution['ENABLED']:
            return self._run_parallel_simulations(num_simulations)
        else:
            return self._run_sequential_simulations(num_simulations)

    def _run_sequential_simulations(self, num_simulations: int) -> List[Dict[str, Any]]:
        """Run simulations sequentially."""
        all_results = []
        for i in tqdm(range(num_simulations), desc="Running simulations"):
            logger.info(f"Starting simulation {i+1} of {num_simulations}")
            results = self.run_simulation()
            all_results.append(results)
        return all_results

    def _run_parallel_simulations(self, num_simulations: int) -> List[Dict[str, Any]]:
        """Run simulations in parallel using multiprocessing."""
        with Pool(processes=self.parallel_execution['WORKER_COUNT']) as pool:
            all_results = list(tqdm(
                pool.imap(self._run_single_simulation, range(num_simulations)),
                total=num_simulations,
                desc="Running parallel simulations"
            ))
        return all_results

    def _run_single_simulation(self, simulation_index: int) -> Dict[str, Any]:
        """Helper method to run a single simulation (used for parallel execution)."""
        logger.info(f"Starting simulation {simulation_index + 1}")
        return self.run_simulation()

if __name__ == "__main__":
    setup = SimulationSetup()
    num_simulations = config.SIMULATION_SETTINGS.get('NUM_SIMULATIONS', 1)
    if num_simulations > 1:
        all_results = setup.run_multiple_simulations(num_simulations)
        logger.info(f"Completed {num_simulations} simulations.")
        # Perform analysis on all results
        setup.data_logger.save_multiple_results(all_results)
        setup.visualizer.create_comparative_plots(all_results)
        aggregate_metrics = setup.performance_tracker.calculate_aggregate_metrics(all_results)
        logger.info(f"Aggregate performance metrics: {aggregate_metrics}")
    else:
        results = setup.run_simulation()
        logger.info("Simulation completed.")
