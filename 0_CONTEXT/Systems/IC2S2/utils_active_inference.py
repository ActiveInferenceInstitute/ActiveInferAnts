
import numpy as np
import random
import copy
import math
import pandas as pd
from pymdp import utils
from pymdp.agent import Agent
import logging
from datetime import datetime
import os
from utils_agents import create_agents_full_sweep, initialize_solutions, process_subnetwork_results

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Define Top_N and Bottom_N parameters
TOP_N_PERCENT = 25  # Top 25%
BOTTOM_N_PERCENT = 25  # Bottom 25%

def run_active_inference_loop(agents, T, fitness_df, learning, learn_A_after_every_X_timesteps, force_learn_at_t, force_neighbor_context, force_neighbor_context_at_t):
    logger.info(f"Starting active inference loop with {len(agents)} agents over {T} timesteps")

    time_steps = []
    min_fitness_list = []
    max_fitness_list = []
    average_fitness_list = []
    number_of_unique_solutions_list = []
    all_agent_actions_list = []
    all_agent_errors_list = []
    all_agents_A_explore_beliefs_list = []
    avg_efe_list = []
    avg_vfe_list = []
    avg_top_n_fitness_list = []
    avg_bottom_n_fitness_list = []
    learning_indicator_list = []

    unique_subnetworks = set(agent.subnetwork for agent in agents.values())
    subnetwork_dict_structure = {subnetwork: {
        'avg_all_agent_actions': [], 'number_of_unique_solutions': [], 'min_fitness': [], 'max_fitness': [],
        'avg_bottom_n_fitness': [], 'avg_top_n_fitness': [], 'average_fitness': [],
        'avg_all_agent_errors': [], 'all_agents_A_explore_beliefs': [], 'avg_efe': [], 'avg_vfe': []} for subnetwork in unique_subnetworks}
    subnetwork_dict = copy.deepcopy(subnetwork_dict_structure)

    all_solutions_start = [agent.current_solution for agent in agents.values()]
    all_fitnesses_start = [agent.current_fitness for agent in agents.values()]

    for t in range(T):
        if t % (0.1 * T) == 0:
            logger.info(f"Running time step {t}/{T}")

        try:
            all_solutions = [agent.current_solution for agent in agents.values()]
            all_fitnesses = [agent.current_fitness for agent in agents.values()]
            all_agent_actions_at_t = []
            all_agent_errors_at_t = []
            all_agents_A_explore_beliefs_at_t = []
            all_agents_efe_at_t = []
            all_agents_vfe_at_t = []

            subnetwork_dict_at_t = {subnetwork: {key: [] for key in subnetwork_dict_structure[subnetwork]} for subnetwork in unique_subnetworks}

            for agent_id, agent in agents.items():
                action_sampled_id = agent.sample_action()
                agent.update_free_energy()

                all_agent_actions_at_t.append(action_sampled_id)
                all_agent_errors_at_t.append(1 if action_sampled_id == 1 else 0)
                all_agents_A_explore_beliefs_at_t.append(agent.A[0][0][0])
                all_agents_efe_at_t.append(agent.G[0])
                all_agents_vfe_at_t.append(np.min(agent.F))

                subnetwork_i = agent.subnetwork
                subnetwork_dict_at_t[subnetwork_i]['avg_efe'].append(agent.G[0])
                subnetwork_dict_at_t[subnetwork_i]['avg_vfe'].append(np.min(agent.F))
                subnetwork_dict_at_t[subnetwork_i]['average_fitness'].append(agent.current_fitness)
                subnetwork_dict_at_t[subnetwork_i]['number_of_unique_solutions'].append(agent.current_solution)
                subnetwork_dict_at_t[subnetwork_i]['avg_all_agent_errors'].append(1 if action_sampled_id == 1 else 0)
                subnetwork_dict_at_t[subnetwork_i]['avg_all_agent_actions'].append(action_sampled_id)
                subnetwork_dict_at_t[subnetwork_i]['all_agents_A_explore_beliefs'].append(agent.A[0][0][0])
                subnetwork_dict_at_t[subnetwork_i]['min_fitness'].append(agent.current_fitness)
                subnetwork_dict_at_t[subnetwork_i]['max_fitness'].append(agent.current_fitness)

            # Process and append data for each subnetwork
            for subnetwork_i in unique_subnetworks:
                subnetwork_fitnesses = subnetwork_dict_at_t[subnetwork_i]['average_fitness']
                if subnetwork_fitnesses:
                    subnetwork_dict[subnetwork_i]['min_fitness'].append(min(subnetwork_fitnesses))
                    subnetwork_dict[subnetwork_i]['max_fitness'].append(max(subnetwork_fitnesses))
                    
                    sorted_fitnesses = sorted(subnetwork_fitnesses)
                    num_bottom_n = max(1, math.ceil(len(subnetwork_fitnesses) * BOTTOM_N_PERCENT / 100))
                    num_top_n = max(1, math.ceil(len(subnetwork_fitnesses) * TOP_N_PERCENT / 100))
                    
                    subnetwork_dict[subnetwork_i]['avg_bottom_n_fitness'].append(np.mean(sorted_fitnesses[:num_bottom_n]))
                    subnetwork_dict[subnetwork_i]['avg_top_n_fitness'].append(np.mean(sorted_fitnesses[-num_top_n:]))
                else:
                    subnetwork_dict[subnetwork_i]['min_fitness'].append(None)
                    subnetwork_dict[subnetwork_i]['max_fitness'].append(None)
                    subnetwork_dict[subnetwork_i]['avg_bottom_n_fitness'].append(None)
                    subnetwork_dict[subnetwork_i]['avg_top_n_fitness'].append(None)

                for key in subnetwork_dict[subnetwork_i]:
                    if key not in ['min_fitness', 'max_fitness', 'avg_bottom_n_fitness', 'avg_top_n_fitness']:
                        values = subnetwork_dict_at_t[subnetwork_i][key]
                        if values:
                            if isinstance(values[0], (int, float, np.number)):
                                subnetwork_dict[subnetwork_i][key].append(np.mean(values))
                            elif isinstance(values[0], str):
                                subnetwork_dict[subnetwork_i][key].append(', '.join(values))
                            else:
                                subnetwork_dict[subnetwork_i][key].append(', '.join(map(str, values)))
                        else:
                            subnetwork_dict[subnetwork_i][key].append(None)
                            logger.warning(f"Empty list for subnetwork {subnetwork_i}, key {key} at timestep {t}")

            time_steps.append(t)
            min_fitness_list.append(np.min(all_fitnesses))
            max_fitness_list.append(np.max(all_fitnesses))
            average_fitness_list.append(np.mean(all_fitnesses))
            number_of_unique_solutions_list.append(len(set(all_solutions)))
            all_agent_actions_list.append(np.mean(all_agent_actions_at_t))
            all_agent_errors_list.append(np.mean(all_agent_errors_at_t))
            all_agents_A_explore_beliefs_list.append(np.mean(all_agents_A_explore_beliefs_at_t))
            avg_efe_list.append(np.mean(all_agents_efe_at_t))
            avg_vfe_list.append(np.mean(all_agents_vfe_at_t))

            sorted_fitnesses = sorted(all_fitnesses)
            num_top_n = max(1, math.ceil(len(all_fitnesses) * TOP_N_PERCENT / 100))
            num_bottom_n = max(1, math.ceil(len(all_fitnesses) * BOTTOM_N_PERCENT / 100))
            avg_bottom_n_fitness_list.append(np.mean(sorted_fitnesses[:num_bottom_n]))
            avg_top_n_fitness_list.append(np.mean(sorted_fitnesses[-num_top_n:]))

            learning_indicator = 1 if learning == 'on' else 0
            learning_indicator_list.append(learning_indicator)

        except Exception as e:
            logger.error(f"Error at timestep {t}: {str(e)}", exc_info=True)
            continue

    logger.info("Active inference loop completed")

    all_solutions_final = [agent.current_solution for agent in agents.values()]
    all_fitnesses_final = [agent.current_fitness for agent in agents.values()]

    try:
        # Ensure all lists have the same length
        min_length = min(len(time_steps), len(max_fitness_list), len(min_fitness_list), len(average_fitness_list),
                         len(number_of_unique_solutions_list), len(all_agent_actions_list), len(all_agent_errors_list),
                         len(all_agents_A_explore_beliefs_list), len(avg_efe_list), len(avg_vfe_list),
                         len(avg_top_n_fitness_list), len(avg_bottom_n_fitness_list), len(learning_indicator_list))

        results = pd.DataFrame({
            'timestep': time_steps[:min_length],
            'max_fitness': max_fitness_list[:min_length],
            'min_fitness': min_fitness_list[:min_length],
            'average_fitness': average_fitness_list[:min_length],
            'number_of_unique_solutions': number_of_unique_solutions_list[:min_length],
            'all_agent_actions': all_agent_actions_list[:min_length],
            'all_agent_errors': all_agent_errors_list[:min_length],
            'all_agents_A_explore_beliefs': all_agents_A_explore_beliefs_list[:min_length],
            'avg_efe': avg_efe_list[:min_length],
            'avg_vfe': avg_vfe_list[:min_length],
            f'avg_top_{TOP_N_PERCENT}%_fitness': avg_top_n_fitness_list[:min_length],
            f'avg_bottom_{BOTTOM_N_PERCENT}%_fitness': avg_bottom_n_fitness_list[:min_length],
            'learning_indicator': learning_indicator_list[:min_length]
        })

        if results.empty:
            logger.warning("Results DataFrame is empty in run_active_inference_loop")
        else:
            logger.info("Results DataFrame successfully populated")

    except Exception as e:
        logger.error(f"Error creating results DataFrame: {str(e)}", exc_info=True)
        results = pd.DataFrame()  # Return an empty DataFrame if there's an error

    return results, all_solutions_final, all_fitnesses_final, all_solutions_start, all_fitnesses_start, subnetwork_dict

def run_full_sweep_simulation(fitness_df, fitness_initial_df, SIMULATION_PARAMETERS, OUTPUT_DIR):
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

    results_all_trials = pd.DataFrame()
    subnetwork_dict_all_trials = {}

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
                            
                            # Convert agents_list to a dictionary
                            agents_dict = {i: agent for i, agent in enumerate(agents_list)}

                            # Run Active Inference loop for stage 1
                            logger.info("Running Active Inference loop for stage 1")
                            results_one, all_solutions_final_one, all_fitnesses_final_one, all_solutions_start_one, all_fitnesses_start_one, subnetwork_dict_1 = run_active_inference_loop(
                                agents_dict, 
                                SIMULATION_PARAMETERS["T"], 
                                fitness_df=fitness_df, 
                                learning=SIMULATION_PARAMETERS["learning"], 
                                learn_A_after_every_X_timesteps=learn_A_after_every_X_timesteps_i, 
                                force_learn_at_t=SIMULATION_PARAMETERS["force_learn_at_t"], 
                                force_neighbor_context=SIMULATION_PARAMETERS["force_neighbor_context"], 
                                force_neighbor_context_at_t=SIMULATION_PARAMETERS["force_neighbor_context_at_t"]
                            )
                            results_one['stage'] = 'First'

                            # Initialize solutions for stage 2
                            logger.info("Initializing solutions for stage 2")
                            agents_list = initialize_solutions(agents_list=agents_list, fitness_initial_df=fitness_initial_df, fitness_df=fitness_df, seed=0)
                            
                            # Convert agents_list to a dictionary again
                            agents_dict = {i: agent for i, agent in enumerate(agents_list)}

                            # Run ActInf loop for stage 2
                            logger.info("Running Active Inference loop for stage 2")
                            results_two, all_solutions_final_two, all_fitnesses_final_two, all_solutions_start_two, all_fitnesses_start_two, subnetwork_dict_2 = run_active_inference_loop(
                                agents_dict, 
                                SIMULATION_PARAMETERS["T"], 
                                fitness_df=fitness_df, 
                                learning=SIMULATION_PARAMETERS["learning"], 
                                learn_A_after_every_X_timesteps=learn_A_after_every_X_timesteps_i, 
                                force_learn_at_t=SIMULATION_PARAMETERS["force_learn_at_t"], 
                                force_neighbor_context=SIMULATION_PARAMETERS["force_neighbor_context"], 
                                force_neighbor_context_at_t=SIMULATION_PARAMETERS["force_neighbor_context_at_t"]
                            )
                            results_two['stage'] = 'Second'

                            # Combine results from both stages
                            results_combined = pd.concat([results_one, results_two], ignore_index=True)
                            
                            # Add trial-specific information
                            results_combined['trial'] = trial
                            results_combined['p'] = p
                            results_combined['error_rate'] = error_rate
                            results_combined['C_improvement_pref'] = C_improvement_pref
                            results_combined['learn_A_after_every_X_timesteps'] = learn_A_after_every_X_timesteps_i
                            results_combined['network_type'] = network_type

                            # Append to results_all_trials
                            results_all_trials = pd.concat([results_all_trials, results_combined], ignore_index=True)

                            # Process subnetwork results
                            try:
                                subnetwork_dict_combined = process_subnetwork_results(subnetwork_dict_1, subnetwork_dict_2, error_rate, p, C_improvement_pref, learn_A_after_every_X_timesteps_i, trial, network_type)
                                subnetwork_dict_all_trials[trial] = subnetwork_dict_combined
                            except Exception as e:
                                logger.error(f"Error processing subnetwork results for trial {trial}: {str(e)}", exc_info=True)

                            trial += 1

                        except Exception as e:
                            logger.error(f"Error in trial {trial}: {str(e)}", exc_info=True)
                            continue

    end_time = datetime.now()
    logger.info(f"Full sweep simulation completed. Start: {start_time}, End: {end_time}, Time difference: {end_time - start_time}")

    # Save results to CSV
    if not results_all_trials.empty:
        results_all_trials.to_csv(os.path.join(OUTPUT_DIR, 'results_all_trials.csv'), index=False)
        logger.info(f"Results saved to {os.path.join(OUTPUT_DIR, 'results_all_trials.csv')}")
    else:
        logger.warning("No results to save. results_all_trials is empty.")

    return results_all_trials, subnetwork_dict_all_trials
