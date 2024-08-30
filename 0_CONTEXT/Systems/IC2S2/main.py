from datetime import datetime 
import os
import sys
import logging
import pandas as pd
import random
from utils_math import initialize_matrices
from utils_visualizing import plot_single_agent_results, visualize_agent_variables, plot_variable_dynamics
from utils_agents import CustomAgent, output_agent_matrices
from utils_active_inference import run_active_inference_loop, run_full_sweep_simulation
from utils_data import initialize_solutions, initialize_fitness_dataframes
from utils_analysis import process_results_all_trials

# Set up logging
log_file = "log.txt"
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[
    logging.FileHandler(log_file),
    logging.StreamHandler()
])
logger = logging.getLogger(__name__)

# Add the parent directory of 'utils' to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

# Define constants at the top of the file
OUTPUT_DIR = "Output/"
SIMULATION_PARAMETERS = {
    "T": 10,
    "learning": "on",
    "learn_A_after_every_X_timesteps": 2,
    "force_learn_at_t": "off",
    "force_neighbor_context": False,
    "force_neighbor_context_at_t": None,
}

# Create Output directory if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)

def main():
    logger.info("Starting simulation")
    logger.info(f"Simulation parameters: {SIMULATION_PARAMETERS}")

    try:
        A, B, C, D, E, pA = initialize_matrices()
    except Exception as e:
        logger.error(f"Error initializing matrices: {e}")
        sys.exit(1)

    agent = CustomAgent(A=A, B=B, C=C, D=D, E=E, pA=pA,
                        inference_algo='MMP', policy_len=1,
                        inference_horizon=1, sampling_mode='full',
                        action_selection='stochastic')

    logger.info(f"Simulation parameters: T={SIMULATION_PARAMETERS['T']}, learning={SIMULATION_PARAMETERS['learning']}, learn_A_after_every_X_timesteps={SIMULATION_PARAMETERS['learn_A_after_every_X_timesteps']}")

    fitness_initial_df, fitness_df = initialize_fitness_dataframes()

    initial_solution = random.choice(fitness_initial_df['solution'].tolist())
    agent.current_solution = initial_solution
    agent.current_fitness = fitness_df[fitness_df['solution'] == initial_solution]['fitness'].values[0]

    matrices = output_agent_matrices(agent)
    logger.info(f"Agent Matrices: {matrices}")

    logger.info("Visualizing initial agent variables")
    visualize_agent_variables(agent, OUTPUT_DIR)

    logger.info("Running single agent inference")
    agent.current_solution = '0' * 10
    try:
        results = run_active_inference_loop(
            {0: agent},
            SIMULATION_PARAMETERS["T"], 
            fitness_df,
            SIMULATION_PARAMETERS["learning"],
            SIMULATION_PARAMETERS["learn_A_after_every_X_timesteps"],
            SIMULATION_PARAMETERS["force_learn_at_t"],
            SIMULATION_PARAMETERS["force_neighbor_context"],
            SIMULATION_PARAMETERS["force_neighbor_context_at_t"]
        )
        
        if results is not None and isinstance(results, pd.DataFrame) and not results.empty:
            logger.info("Plotting single agent results")
            plot_single_agent_results(SIMULATION_PARAMETERS["T"], results, SIMULATION_PARAMETERS["learning"], 
                                      SIMULATION_PARAMETERS["force_learn_at_t"], 
                                      SIMULATION_PARAMETERS["force_neighbor_context"], 
                                      SIMULATION_PARAMETERS["force_neighbor_context_at_t"], 
                                      output_dir=OUTPUT_DIR)
            
            logger.info("Plotting variable dynamics")
            plot_variable_dynamics(results, OUTPUT_DIR)
        else:
            logger.warning("Invalid or empty results. Skipping plot generation.")
    except Exception as e:
        logger.error(f"Error in single agent inference: {e}")

    # Run full sweep simulation
    logger.info("Starting full sweep simulation")
    try:
        results_all_trials, subnetwork_dict_all_trials = run_full_sweep_simulation(fitness_df, fitness_initial_df, SIMULATION_PARAMETERS, OUTPUT_DIR)
    except Exception as e:
        logger.error(f"Error in full sweep simulation: {e}")

    # Display results
    logger.info("Displaying results")
    if subnetwork_dict_all_trials:
        logger.info(f"Subnetwork dict for trial 0: {subnetwork_dict_all_trials.get(0, 'No data')}")
        logger.info(f"Number of successful trials: {len(subnetwork_dict_all_trials)}")
    else:
        logger.warning("No subnetwork data available. All trials may have failed.")

    # After the simulation loop, process the results
    logger.info("Processing all trial results")
    if results_all_trials.empty:
        logger.warning("No results to process. All trials may have failed.")
    else:
        process_results_all_trials(results_all_trials, output_dir=OUTPUT_DIR)

    logger.info("Visualizing final agent variables")
    visualize_agent_variables(agent, OUTPUT_DIR)

    logger.info("Simulation complete")

if __name__ == "__main__":
    main()
