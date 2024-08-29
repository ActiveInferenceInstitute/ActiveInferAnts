
import numpy as np
import random
import copy
import math
import pandas as pd
from pymdp import utils
from pymdp.agent import Agent
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def initialize_matrices():
    # Define dimensions
    num_obs = 4  # number of possible observations
    num_states = 2  # number of hidden states
    num_actions = 2  # number of actions

    # Initialize A matrix (likelihood)
    A = np.random.rand(num_obs, num_states)
    A = A / A.sum(axis=0, keepdims=True)  # normalize columns

    # Initialize B matrix (transition)
    num_factors = 1  # Assuming a single factor for simplicity
    B = np.eye(num_states)[np.newaxis, :, :].repeat(num_actions, axis=0)
    B = B.transpose(1, 2, 0)  # Reshape to [num_states, num_states, num_actions]

    # Initialize C matrix (prior preferences)
    C = np.zeros(num_obs)

    # Initialize D matrix (initial state prior)
    D = np.ones(num_states) / num_states

    # Initialize E matrix (policy prior)
    E = np.ones(num_actions) / num_actions

    # Initialize pA (parameters of A)
    pA = np.ones_like(A)

    return A, B, C, D, E, pA


def set_pomdp_variables(agents_params, C_improvement_prefs=np.array([5, -1, 0]), show_details=False, add_pD=False):
      # Define A/B/C/D/E matrices per agent

  # define A per agent
  for agent_i in list(agents_params.keys()):
    # A matrix
    agents_params[agent_i]['A'] = utils.obj_array(agents_params[agent_i]['num_modalities'])
    # A[0] = outcomes modality
    agents_params[agent_i]['A'][0] = np.zeros( ( len(agents_params[agent_i]['outcome_obs_names']), len(agents_params[agent_i]['attention_state_names']) ) )
    for attention_state in range(len(agents_params[agent_i]['attention_state_names'])):
      agents_params[agent_i]['A'][0][:,attention_state] = utils.norm_dist(np.ones(shape=len(agents_params[agent_i]['outcome_obs_names'])))    # generate uniform distribution
    # A[1] = attention modality
    agents_params[agent_i]['A'][1] =np.zeros( ( len(agents_params[agent_i]['attention_obs_names']), len(agents_params[agent_i]['attention_state_names']) ) )
    for attention_state in range(len(agents_params[agent_i]['attention_state_names'])):
      agents_params[agent_i]['A'][1][attention_state,attention_state] = 1   # attention state levels and attention obs levels are parallel, so we can set prob to 1 to link self-self, nX-nX, etc.
      agents_params[agent_i]['A'][1][:,attention_state] = utils.norm_dist(agents_params[agent_i]['A'][1][:,attention_state])
    if show_details == True:
      if agent_i == 'n0':
        print(f"agents_params['n0']['num_modalities'] = {agents_params['n0']['num_modalities']}")
        print(f"agents_params['n0']['A'][1] = {agents_params['n0']['A'][1]}")
        for modality_i in range(agents_params[agent_i]['num_modalities']):
          print(f"utils.is_normalized(agents_params[{agent_i}]['A'][{modality_i}]) = {utils.is_normalized(agents_params[agent_i]['A'][modality_i])}")


  # define B per agent   --- **regardless of current state, if agent chooses 'exploit_nX', then next state is 'attend to nX', i.e. agent has full certainty over 'attention' state-action mappings
  for agent_i in list(agents_params.keys()):
    agents_params[agent_i]['B'] = utils.obj_array(agents_params[agent_i]['num_factors'])
    agents_params[agent_i]['B'][0] = np.zeros( ( len(agents_params[agent_i]['attention_state_names']), len(agents_params[agent_i]['attention_state_names']), len(agents_params[agent_i]['action_names']) ) )
    att_state_names_test = len(agents_params[agent_i]['attention_state_names'])
    action_names_test = len(agents_params[agent_i]['action_names'])

    for action_i in range(len(agents_params[agent_i]['action_names'])):
        agents_params[agent_i]['B'][0][:,:,action_i][action_i] = 1

    if show_details == True:
      if agent_i == 0:
        print(f"utils.is_normalized(agents_params[{agent_i}]['B'][0]) = {utils.is_normalized(agents_params[agent_i]['B'][0])}")

  # define C per agent
  for agent_i in list(agents_params.keys()):
    agents_params[agent_i]['C'] = utils.obj_array_zeros(agents_params[agent_i]['num_obs'])
    agents_params[agent_i]['C'][0] = utils.norm_dist(softmax(C_improvement_prefs))   # how much agents (dys)prefers 'improvement', 'no_improvement', 'unobserved'
    #agents_params[agent_i]['C'][1] = utils.norm_dist(np.random.uniform(size=len(agents_params[agent_i]['attention_obs_names'])))   # previous, changed 7/7/2024
    agents_params[agent_i]['C'][1] = utils.norm_dist(np.ones(shape=len(agents_params[agent_i]['attention_obs_names'])))
    if show_details == True:
      if agent_i == 0:
        print(agents_params[agent_i]['C'])
        print(f"agents_params[n0]['C'][1] = {agents_params[agent_i]['C'][1]}")
        for modality_i in range(agents_params[agent_i]['num_modalities']):
          print(f"utils.is_normalized(agents_params[{agent_i}]['C'][{modality_i}]) = {utils.is_normalized(agents_params[agent_i]['C'][modality_i])}")

  # define D per agent
  for agent_i in list(agents_params.keys()):
    agents_params[agent_i]['D'] = utils.obj_array(agents_params[agent_i]['num_factors'])
    agents_params[agent_i]['D'][0] = utils.norm_dist(np.ones(shape=agents_params[agent_i]['num_states'][0])) # new 7/7/2024

    if show_details == True:
      if agent_i == 0:
        print(f"utils.is_normalized(agents_params[{agent_i}]['D'][0]) = {utils.is_normalized(agents_params[agent_i]['D'][0])}")

  # define E per agent
  for agent_i in list(agents_params.keys()):
    agents_params[agent_i]['E'] = utils.norm_dist(np.ones(shape=agents_params[agent_i]['num_controls']))
    if show_details == True:
      if agent_i == 0:
        print(f"utils.is_normalized(agents_params[{agent_i}]['E']) = {utils.is_normalized(agents_params[agent_i]['E'])}")

    # learning A
    agents_params[agent_i]['pA'] = utils.dirichlet_like(agents_params[agent_i]['A'], scale = 0.5) # learning likelihood
    agents_params[agent_i]['pB'] = utils.dirichlet_like(agents_params[agent_i]['B'], scale = 1.0) # learning transitions
    agents_params[agent_i]['pD'] = utils.dirichlet_like(agents_params[agent_i]['D'], scale = 1.0) # learning priors over initial states

  return agents_params

def run_active_inference_loop(agents_list, agents_params, fitness_df, T=5, seed=0, error_rate=0, first_stage=False, learn_A_after_every_X_timesteps=1, error_monitoring=False):
    """
    Define Active Inference loop:

    agents_list : list of constructed active inference agents (list)
    agents_params : dictionary of agents' parameters (dict)
    fitness_df : DataFrame containing all solution and fitness pairings for an NK landscape (pandas DataFrame)
    T : duration (number of timesteps) to run the loop (int)
    seed : set seed for reproducibility (int)
    error_rate : set error-in-copying rate (float in range [0,1] inclusive)
    first_stage : True/False indicator for if the loop is being run as a first stage; determines if agents should be forced to 'explore' at t=1
    learn_A_after_every_X_timesteps : number of timesteps to pass before agent updates their A matrix (int)
    error_monitoring : True/False indicator for if error-related output should be printed to the console for debugging purposes
    """

    logger.info(f"Starting active inference loop with {len(agents_params)} agents over {T} timesteps")

    # Set lists for recording into results
    time_steps = []
    min_fitness_list = []
    max_fitness_list = []
    average_fitness_list = []
    number_of_unique_solutions_list = []
    n0_prev_fitness_list = []
    n0_action_list = []
    n0_new_fitness_list = []
    n0_solution_list = []
    n0_change_list = []
    n0_solution_outer_list = []
    n0_qs_list = []
    n0_q_pi_list = []
    n0_efe_list = []
    n0_A_explore_belief_list = []
    all_agent_actions_list = []
    all_agent_errors_list = []
    all_agents_A_explore_beliefs_list = []
    all_agents_A_explore_beliefs_dist_list = []
    avg_efe_list = []
    avg_vfe_list = []
    avg_top_50_fitness_list = []
    avg_bottom_50_fitness_list = []
    learning_indicator_list = []

    # Group-results initial dicts
    # Create a new nested dictionary with unique values as keys
    unique_subnetworks = set()
    for agent_i in agents_params.keys():      # result_dict.keys():
      print(agent_i)
      subnetwork = agents_params[agent_i].get('subnetwork', 0)  # Default to 0 if not present
      unique_subnetworks.add(subnetwork)
    print(f"unique_subnetworks = {unique_subnetworks}")
    subnetwork_dict_structure = {subnetwork: {
        'avg_all_agent_actions': [], 'number_of_unique_solutions' : [], 'min_fitness': [], 'max_fitness': [],
        'avg_bottom_50_fitness' : [], 'avg_top_50_fitness': [], 'average_fitness': [],
        'avg_all_agent_errors' : [],'all_agents_A_explore_beliefs' : [], 'avg_efe': [],'avg_vfe' : []} for subnetwork in unique_subnetworks}
    subnetwork_dict = copy.deepcopy(subnetwork_dict_structure)

    random.seed(seed)
    logger.debug(f"Random seed set to {seed}")

    # Initial observatons
    all_solutions_start = [agent.current_solution for agent in agents_list]  # collect all of agents' current solutions into a list
    all_fitnesses_start = [agent.current_fitness for agent in agents_list]   # collect all of agents' current fitnesses into a list
    logger.debug(f"Initial solutions and fitnesses collected")

    for t in range(T):
        if t % (0.1 * T) == 0:  # Check if t is a multiple of 10% of T
            logger.info(f"Running time step {t}/{T}")
        
        try:
            # Get all solutions, set agent's new fitnesses, and get all fitnesses at start of each timestep (remember to collect the final ones after the 'for t in range(T):' call)
            all_solutions = [agent.current_solution for agent in agents_list]
            all_fitnesses = [agent.current_fitness for agent in agents_list]
            all_agent_actions_at_t_list = []
            all_agent_errors_at_t_list = []
            all_agents_A_explore_beliefs_at_t_list = []
            all_agents_efe_at_t_list = []
            all_agents_vfe_at_t_list = []

            # Group-results initialize dict for time t
            subnetwork_dict_at_t = copy.deepcopy(subnetwork_dict_structure)


            for agent in agents_list:
                # Action selection
                if t == 0 and first_stage:
                    action_sampled_id = 0
                    logger.debug(f"First stage, forcing 'explore' for agent {agent}")
                else:
                    action_sampled = agent.sample_action()
                    action_sampled_id = int(action_sampled[0])
                
                # Explore
                if action_sampled_id == 0:
                    try:
                        agent_action = 0
                        all_agent_actions_at_t_list.append(agent_action)
                        prev_solution = agent.current_solution
                        prev_fitness = agent.current_fitness
                        new_solution = string_to_bitstring(agent.current_solution)   # MODIFIED/ADDED
                        mutation_index = random.randrange(len(new_solution))   #randomly choose one of the components in current solution
                        new_solution[mutation_index] = 1 - new_solution[mutation_index]  # Flip one bit (specifically the element in 'child' indexed at mutation_index); 1-0=1, 1-1=0
                        new_solution = bitstring_to_string(new_solution)  #ADDED
                        new_fitness = fitness_df[fitness_df['solution'].isin([new_solution])]['fitness'].values[0]
                        # If explored solution's fitness is better, keep as new solution
                        if new_fitness > prev_fitness:
                          agent.current_solution = new_solution
                          agent.current_fitness = new_fitness
                          obs = [0, 0]   # 'improvement' from attention to 'self'
                          if agent == 'n0':
                            n0_change = 'yes'
                        # Else keep previous solution and observe as no improvement
                        else:
                          obs = [1, 0]   # 'no_improvement' from attention to 'self'
                          if agent == 'n0':
                            n0_change = ''
                    except Exception as e:
                        logger.error(f"Explore error at {t}, agent {agent}: action_sampled_id = {action_sampled_id}, prev_solution = {prev_solution}, prev_fitness = {prev_fitness}, new_solution = {new_solution}, new_fitness = {new_fitness}")
                        continue
                    logger.debug(f"Agent {agent} exploring")
                
                # Exploit nX
                elif action_sampled_id != 0:
                    try:
                        agent_action = 1
                        all_agent_actions_at_t_list.append(agent_action)
                        prev_solution = agent.current_solution
                        prev_fitness = agent.current_fitness
                        local_solutions = [all_solutions[i] for i in agents_params[agent]['local_idx']]

                        attention_solution = copy.deepcopy(local_solutions[action_sampled_id])
                        new_solution = string_to_bitstring(prev_solution)
                        num_errors = 0
                        for i in range(len(attention_solution)):
                          random_val = random.random()
                          if random_val > error_rate:
                            new_solution[i] = attention_solution[i]
                          else:
                            num_errors += 1
                        all_agent_errors_at_t_list.append(num_errors)
                        new_solution = bitstring_to_string(new_solution)
                        new_fitness = fitness_df[fitness_df['solution'].isin([new_solution])]['fitness'].values[0]
                        if new_fitness > prev_fitness:
                          if agent == 'n0':
                            n0_change = 'yes'
                          agent.current_solution = copy.deepcopy(new_solution)
                          agent.current_fitness = new_fitness
                          obs = [0, action_sampled_id]    #agent sees improvement from exploiting particular neighbor
                          logger.info(f"Agent {agent} changed: prev_solution = {prev_solution}, prev_fitness = {prev_fitness}, new_solution = {new_solution}, new_fitness = {new_fitness}")
                        else:
                          if agent == 'n0':
                            n0_change = ''
                          obs = [1, action_sampled_id] # agent keeps previous solution if 'copied' solution has <= equivalent fitness
                    except Exception as e:
                        logger.error(f"Exploit error at {t}, agent {agent}: action_sampled_id = {action_sampled_id}, error {e}")
                        continue
                    logger.debug(f"Agent {agent} exploiting neighbor {action_sampled_id}")

                if agent == 'n0':
                    n0_new_fitness_list.append(agent.current_fitness)
                    n0_action_list.append(agents_params['n0']['action_names'][action_sampled_id])
                    n0_solution_list.append(agent.current_solution)
                    n0_change_list.append(n0_change)


                # Infer states
                try:
                  qs = agent.infer_states(obs)
                except Exception as e:
                  logger.error(f"Error at timestep {t}, agent {agent} infer_states(obs): {str(e)}", exc_info=True)
                # Learning
                try:
                  # learn after every X timesteps (must be numeric)
                  if isinstance(learn_A_after_every_X_timesteps, (int,float)):
                    if (t+1) % learn_A_after_every_X_timesteps == 0 and t != 0:
                      agent.qs = copy.deepcopy(qs[action_sampled_id][0])   # temporarily set agent's qs to specific posterior dist over states given action chosen for current timestep
                      agent.update_A(obs)
                      agent.qs = copy.deepcopy(qs)   # change qs back to the output of infer_states(obs)
                      learning_indicator = 1
                    else:
                      learning_indicator = 0
                  if agent == 'n0':
                    n0_A_explore_belief_list.append(agent.A[0][0][0])   # structure of A is [modality][observation][self/neighbor]
                  all_agents_A_explore_beliefs_at_t_list.append(agent.A[0][0][0])
                except Exception as e:
                  logger.error(f"Error at timestep {t}, agent {agent} update_A(obs): {str(e)}", exc_info=True)
                # Infer policies
                try:
                  q_pi, efe = agent.infer_policies()
                except Exception as e:
                  logger.error(f"Error at timestep {t}, agent {agent} infer_policies: {str(e)}", exc_info=True)
                if agent == 'n0':
                  n0_qs_list.append(qs)
                  n0_q_pi_list.append(q_pi)
                  n0_efe_list.append(efe)

                #Group-results : store individual agent's results by subnetwork into temp subnetwork_dict_at_t
                try:
                  for subnetwork_i in unique_subnetworks:
                    subnetwork = agents_params[agent].get('subnetwork', 0)  # Default to 0 if not present
                    if subnetwork == subnetwork_i:
                      subnetwork_dict_at_t[subnetwork_i]['avg_efe'].append(copy.deepcopy(agent.G*-1)[0])
                      subnetwork_dict_at_t[subnetwork_i]['avg_vfe'].append(np.min(copy.deepcopy(agent.F)))
                      subnetwork_dict_at_t[subnetwork_i]['average_fitness'].append(agent.current_fitness)  # used for computing min/max/avg/top 50/bottom 50 fitness metrics
                      subnetwork_dict_at_t[subnetwork_i]['number_of_unique_solutions'].append(agent.current_solution)
                      subnetwork_dict_at_t[subnetwork_i]['avg_all_agent_errors'].append(num_errors if action_sampled_id != 0 else 0)
                      subnetwork_dict_at_t[subnetwork_i]['avg_all_agent_actions'].append(0 if action_sampled_id == 0 else 1)
                      subnetwork_dict_at_t[subnetwork_i]['all_agents_A_explore_beliefs'].append(agent.A[0][0][0])
                except Exception as e:
                  logger.error(f"Error at timestep {t}, agent {agent} storing results by subnetwork: {str(e)}", exc_info=True)

            try:
                # store outputs for all agents at end of timestep
                all_solutions = [copy.deepcopy(agent.current_solution) for agent in agents_list]
                all_fitnesses = [agent.current_fitness for agent in agents_list]
                all_efe_min = [copy.deepcopy(agent.G*-1)[0] for agent in agents_list]  # multiply by -1 (infer_policies() returned negative G) and extract G for 'explore'
                all_vfe_min = [np.min(copy.deepcopy(agent.F)) for agent in agents_list]
                sorted_fitnesses = sorted(all_fitnesses)
                num_to_keep = math.ceil(len(all_fitnesses) * 0.5)   # num of fitnesses to keep for determining top/bottom 50% of fitness values
                avg_bottom_50_fitness_list.append(np.mean(sorted_fitnesses[:num_to_keep]))
                avg_top_50_fitness_list.append(np.mean(sorted_fitnesses[num_to_keep:]))
                avg_efe_list.append(np.mean(all_efe_min))
                avg_vfe_list.append(np.mean(all_vfe_min))
                learning_indicator_list.append(learning_indicator)

                max_fitness_list.append(np.max(all_fitnesses))
                min_fitness_list.append(np.min(all_fitnesses))
                average_fitness_list.append(np.mean(all_fitnesses))
                number_of_unique_solutions_list.append(len(set(x for x in all_solutions)))
                time_steps.append(t)
                all_agent_actions_list.append(np.mean(all_agent_actions_at_t_list))
                if len(all_agent_errors_at_t_list) == 0:
                  all_agent_errors_list.append(0)
                else:
                  all_agent_errors_list.append(np.mean(all_agent_errors_at_t_list))
                all_agents_A_explore_beliefs_list.append(np.mean(all_agents_A_explore_beliefs_at_t_list))
                all_agents_A_explore_beliefs_dist_list.append(all_agents_A_explore_beliefs_at_t_list)
                try:
                  #Group-results : append aggregated metrics from time t
                  for subnetwork_i in unique_subnetworks:
                    subnetwork_dict[subnetwork_i]['avg_efe'].append(np.mean(copy.deepcopy(subnetwork_dict_at_t[subnetwork_i]['avg_efe'])))
                    subnetwork_dict[subnetwork_i]['avg_vfe'].append(np.mean(copy.deepcopy(subnetwork_dict_at_t[subnetwork_i]['avg_vfe'])))
                    subnetwork_dict[subnetwork_i]['average_fitness'].append(np.mean(copy.deepcopy(subnetwork_dict_at_t[subnetwork_i]['average_fitness'])))
                    subnetwork_dict[subnetwork_i]['min_fitness'].append(np.min(copy.deepcopy(subnetwork_dict_at_t[subnetwork_i]['average_fitness'])))
                    subnetwork_dict[subnetwork_i]['max_fitness'].append(np.max(copy.deepcopy(subnetwork_dict_at_t[subnetwork_i]['average_fitness'])))
                    subnetwork_dict[subnetwork_i]['number_of_unique_solutions'].append(len(set(solution for solution in copy.deepcopy(subnetwork_dict_at_t[subnetwork_i]['number_of_unique_solutions']))))
                    subnetwork_dict[subnetwork_i]['avg_all_agent_actions'].append(np.mean(copy.deepcopy(subnetwork_dict_at_t[subnetwork_i]['avg_all_agent_actions'])))
                    subnetwork_dict[subnetwork_i]['all_agents_A_explore_beliefs'].append(np.mean(copy.deepcopy(subnetwork_dict_at_t[subnetwork_i]['all_agents_A_explore_beliefs'])))
                    num_to_keep = math.ceil(len(subnetwork_dict_at_t[subnetwork_i]['average_fitness']) * 0.5)
                    subnetwork_dict[subnetwork_i]['avg_bottom_50_fitness'].append(np.mean(sorted(copy.deepcopy(subnetwork_dict_at_t[subnetwork_i]['average_fitness'])[:num_to_keep])))
                    subnetwork_dict[subnetwork_i]['avg_top_50_fitness'].append(np.mean(sorted(copy.deepcopy(subnetwork_dict_at_t[subnetwork_i]['average_fitness'])[num_to_keep:])))
                    subnetwork_dict[subnetwork_i]['avg_all_agent_errors'].append(np.mean(copy.deepcopy(subnetwork_dict_at_t[subnetwork_i]['avg_all_agent_errors'])))
                except Exception as e:
                  logger.error(f"Error at timestep {t} appending aggregated metrics from time t: {str(e)}", exc_info=True)

            except Exception as e:
                logger.error(f"Error at timestep {t} storing outputs: {str(e)}", exc_info=True)

        except Exception as e:
            logger.error(f"Error at timestep {t}: {str(e)}", exc_info=True)
            continue

    logger.info("Active inference loop completed")
    
    all_solutions_final = copy.deepcopy(all_solutions)
    all_fitnesses_final = copy.deepcopy(all_fitnesses)
    results = pd.DataFrame({'timestep': time_steps, 'max_fitness' : max_fitness_list, 'min_fitness' : min_fitness_list, 'average_fitness' : average_fitness_list,
                            'number_of_unique_solutions' : number_of_unique_solutions_list,
                            'n0 action' : n0_action_list, 'n0 fitness' : n0_new_fitness_list, 'n0 solution' : n0_solution_list,'n0 change' : n0_change_list,
                            'n0 qs' : n0_qs_list, 'n0 q_pi' : n0_q_pi_list, 'n0 efe' : n0_efe_list, 'n0 A' : n0_A_explore_belief_list,
                            'avg_all_agent_actions' : all_agent_actions_list, 'avg_all_agent_errors' : all_agent_errors_list,
                             'all_agents_A_explore_beliefs' : all_agents_A_explore_beliefs_list, 'all_agents_A_explore_beliefs_dist' : all_agents_A_explore_beliefs_dist_list,
                            'avg_bottom_50_fitness' : avg_bottom_50_fitness_list, 'avg_top_50_fitness' : avg_top_50_fitness_list,
                            'avg_efe' : avg_efe_list, 'avg_vfe' : avg_vfe_list, 'learning_indicator' : learning_indicator_list
                            })
    return results, all_solutions_final, all_fitnesses_final, all_solutions_start, all_fitnesses_start, subnetwork_dict


def run_single_agent_inference(agent, T, fitness_df):
    # Create a single-element list for the agent
    agents_list = [agent]
    
    # Create a dictionary with default parameters for a single agent
    agents_params = {
        0: {
            'id': 0,
            'subnetwork': 0,  # Default subnetwork
            'neighbors': [],  # No neighbors for single agent
            'C_improvement_pref': 0.5,  # Default value
        }
    }
    
    # Run the active inference loop
    results, _, _, _, _, _ = run_active_inference_loop(
        agents_list, 
        agents_params, 
        fitness_df=fitness_df, 
        T=T,
        first_stage=True, 
        error_rate=0, 
        learn_A_after_every_X_timesteps=2, 
        error_monitoring=False
    )
    
    return results
