import os
import sys
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Add the parent directory of 'utils' to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

# Import necessary modules
import numpy as np
import pymdp
from pymdp.maths import softmax
import copy
import math
import random
from IPython.display import display
import pandas as pd
from datetime import datetime

# Import all functions from custom utils
from utils_math import *
from utils_visualizing import *
from utils_agents import *
from utils_active_inference import *

# Initialize dataframe and dictionary for storing results
results_all_trials = pd.DataFrame()
subnetwork_dict_all_trials = {}

# Create Outputs directory if it doesn't exist
output_dir = "Outputs/"
os.makedirs(output_dir, exist_ok=True)

if __name__ == "__main__":
    logger.info("Starting simulation")

    # Initialize matrices
    logger.info("Initializing matrices")
    A, B, C, D, E, pA = initialize_matrices()

    # Create a custom agent
    logger.info("Creating custom agent")
    agent = CustomAgent(A=A, B=B, C=C, D=D, E=E, pA=pA,
                        inference_algo='MMP', policy_len=1,
                        inference_horizon=2, sampling_mode='full',
                        action_selection='stochastic')

    # Simulation parameters
    T = 30
    learning = 'on'
    learn_A_after_every_X_timesteps = 2
    force_learn_at_t = 'off'
    force_neighbor_context = False
    force_neighbor_context_at_t = None

    logger.info(f"Simulation parameters: T={T}, learning={learning}, learn_A_after_every_X_timesteps={learn_A_after_every_X_timesteps}")

    # Create and plot landscape
    logger.info("Creating and plotting landscape")
    fitness_df, fitness_initial_df, local_optima_df = create_and_plot_landscape()

    # Run single agent inference
    logger.info("Running single agent inference")
    results = run_single_agent_inference(agent, T, fitness_df)
    
    # Plot results
    logger.info("Plotting single agent results")
    plot_single_agent_results(T, results, learning, force_learn_at_t, force_neighbor_context, force_neighbor_context_at_t, output_dir=output_dir)

    # Run two-stage simulation
    logger.info("Running two-stage simulation")
    two_stage_results = run_two_stage_simulation()
    plot_two_stage_results(two_stage_results, output_dir=output_dir)

    # Run full sweep simulation
    logger.info("Starting full sweep simulation")
    start_time = datetime.now()
    
    # Define simulation parameters
    p_rates = [0.1, 0.5, 0.9]
    error_rates = [0.1, 0.3, 0.5]
    C_improvement_prefs = [0.1, 0.5, 0.9]
    learn_A_after_every_X_timesteps = [1, 2, 5]
    network_types = ['random', 'small-world']
    num_agents = 10
    N = 5
    M = 5
    seed = 42
    inference_algo = 'MMP'
    inference_horizon = 2
    policy_len = 1

    logger.info(f"Simulation parameters: p_rates={p_rates}, error_rates={error_rates}, C_improvement_prefs={C_improvement_prefs}")
    logger.info(f"learn_A_after_every_X_timesteps={learn_A_after_every_X_timesteps}, network_types={network_types}")
    logger.info(f"num_agents={num_agents}, N={N}, M={M}, seed={seed}")
    logger.info(f"inference_algo={inference_algo}, inference_horizon={inference_horizon}, policy_len={policy_len}")

    # Run full sweep simulation
    trial = 0
    for p in p_rates:
        for error_rate in error_rates:
            for C_improvement_pref in C_improvement_prefs:
                for learn_A_after_every_X_timesteps_i in learn_A_after_every_X_timesteps:
                    for network_type in network_types:
                        logger.info(f"Trial {trial}: C_improvement_prefs={C_improvement_pref}, error_rate={error_rate}, p={p}, learn_A_after_every_X_timesteps={learn_A_after_every_X_timesteps_i}, network_type={network_type}")
                        try:
                            # Run full sweep given parameters
                            logger.info("Creating agents for full sweep")
                            agents_params, agents_list = create_agents_full_sweep(fitness_df, fitness_initial_df, num_agents=num_agents, num_neighbors=None, network_type=network_type, p=p, N=N, M=M, C_improvement_prefs=C_improvement_pref, seed=seed,
                                                                                  inference_algo=inference_algo, inference_horizon=inference_horizon, policy_len=policy_len)
                            
                            # Run Active Inference loop for stage 1
                            logger.info("Running Active Inference loop for stage 1")
                            results_one, all_solutions_final_one, all_fitnesses_final_one, all_solutions_start_one, all_fitnesses_start_one, subnetwork_dict_1 = run_active_inference_loop(agents_list, agents_params, fitness_df=fitness_df, T=T,
                                                                                                                                                                first_stage=True, error_rate=error_rate, learn_A_after_every_X_timesteps=learn_A_after_every_X_timesteps_i, error_monitoring=False)
                            results_one['stage'] = 'First'

                            # Initialize solutions for stage 2
                            logger.info("Initializing solutions for stage 2")
                            agents_list = initialize_solutions(agents_list=agents_list, fitness_initial_df=fitness_initial_df, fitness_df=fitness_df, seed=0)
                            
                            # Run ActInf loop for stage 2
                            logger.info("Running Active Inference loop for stage 2")
                            results_two, all_solutions_final_two, all_fitnesses_final_two, all_solutions_start_two, all_fitnesses_start_two, subnetwork_dict_2 = run_active_inference_loop(agents_list, agents_params, fitness_df=fitness_df, T=T,
                                                                                                                                                                first_stage=False, error_rate=error_rate, learn_A_after_every_X_timesteps=learn_A_after_every_X_timesteps_i, error_monitoring=False)
                            results_two['stage'] = 'Second'

                            # Combine results
                            logger.info("Combining results")
                            results = pd.concat([results_one, results_two], ignore_index=True)
                            results['error_rate'] = error_rate
                            results['p'] = p
                            results['C_improvement_prefs'] = str(C_improvement_pref)
                            results['learn_A_after_every_X_timesteps'] = str(learn_A_after_every_X_timesteps_i)
                            results['trial'] = trial
                            results['network_type'] = network_type

                            # Process subnetwork results
                            logger.info("Processing subnetwork results")
                            subnetwork_dict = process_subnetwork_results(subnetwork_dict_1, subnetwork_dict_2, error_rate, p, C_improvement_pref, learn_A_after_every_X_timesteps_i, trial, network_type)

                            results_all_trials = pd.concat([results_all_trials, results]).reset_index(drop=True)
                            subnetwork_dict_all_trials[trial] = subnetwork_dict
                            trial += 1

                        except Exception as e:
                            logger.error(f"Error in trial {trial}: {e}")
                            pass

    end_time = datetime.now()
    time_diff = end_time - start_time
    logger.info(f"Simulation completed. Start: {start_time}, End: {end_time}, Time difference: {time_diff}")

    # Display results
    logger.info("Displaying results")
    logger.info(f"Subnetwork dict for trial 1: {subnetwork_dict_all_trials[1]}")
    logger.info(f"Length of subnetwork dict for trial 1: {len(subnetwork_dict_all_trials[1])}")

    # After the simulation loop, process the results
    logger.info("Processing all trial results")
    from utils_visualizing import process_results_all_trials
    process_results_all_trials(results_all_trials, output_dir=output_dir)

    logger.info("Simulation complete")
