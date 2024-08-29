import numpy as np
import pymdp
import pandas as pd
import random
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import networkx as nx
import copy
import math
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_kl_divergence(P, Q):
    """
    Calculate the Kullback-Leibler divergence between two probability distributions.

    Args:
        P (numpy.ndarray): First probability distribution
        Q (numpy.ndarray): Second probability distribution

    Returns:
        float: KL divergence value
    """
    logging.info("Calculating KL divergence")
    # Add a small epsilon to avoid division by zero
    epsilon = 1e-10
    P = np.clip(P, epsilon, 1)
    Q = np.clip(Q, epsilon, 1)
    
    return np.sum(P * np.log(P / Q))

def calculate_entropy(P):
    """
    Calculate the entropy of a probability distribution.

    Args:
        P (numpy.ndarray): Probability distribution

    Returns:
        float: Entropy value
    """
    logging.info("Calculating entropy")
    # Add a small epsilon to avoid log(0)
    epsilon = 1e-10
    P = np.clip(P, epsilon, 1)
    
    return -np.sum(P * np.log(P))

def normalize_array(arr):
    """
    Normalize an array so that it sums to 1.

    Args:
        arr (numpy.ndarray): Input array

    Returns:
        numpy.ndarray: Normalized array
    """
    logging.info("Normalizing array")
    # Add a small epsilon to avoid division by zero
    epsilon = 1e-10
    return arr / (np.sum(arr) + epsilon)

def initialize_matrices():
    logging.info("Initializing matrices")
    # Initialize matrices A, B, C, D, E, and pA
    # These are placeholder values; adjust according to your specific needs
    A = np.random.rand(3, 3)
    B = np.random.rand(3, 3, 2)
    C = np.random.rand(3)
    D = np.random.rand(3)
    E = np.random.rand(2)
    pA = np.random.rand(3)
    
    return A, B, C, D, E, pA

def create_nk_landscape(N=10, K=5, max_fitness=100, initial_fitness_limit=20, seed=0):
    logging.info("Creating NK landscape")
    random.seed(seed) # Set seed for reproducibility
    N = N  # Number of elements
    K = K  # Interdependence parameter
    max_fitness = max_fitness
    initial_fitness_limit = initial_fitness_limit

    # Define the fitness function
    def get_fitness(bitstring, K):
        fitness = 0
        for i in range(N):
            # Get the indices of the K elements that influence the fitness contribution of element i
            indices = [i] + [(i+j+1) % N for j in range(1, K+1)]

            # Calculate the fitness contribution of element i based on its value and the values of the K influencing elements
            fitness_contribution = sum(bitstring[j] for j in indices)
            # Introduce randomness by multiplying with a random weight
            fitness_contribution *= random.uniform(0, 1)
            fitness += fitness_contribution
        return fitness

    # Generate all possible bitstrings of length N
    bitstrings = [list(map(int, list(np.binary_repr(i, N)))) for i in range(2**N)]

    # Calculate and store the fitness value for each bitstring
    fitness_values_original = [get_fitness(bitstring, K) for bitstring in bitstrings]
    # Normalize values
    min_val = min(fitness_values_original)
    max_val = max(fitness_values_original)
    fitness_values = [(val - min_val) / (max_val - min_val) * max_fitness for val in fitness_values_original]

    bitstrings_strings = [bitstring_to_string(bitstring) for bitstring in bitstrings]
    fitness_df = pd.DataFrame({'solution': bitstrings_strings, 'fitness': fitness_values}).reset_index(drop=True)  #note: ordering is based on bitstring similarity
    fitness_initial_df = fitness_df[fitness_df['fitness'] < initial_fitness_limit]
    fitness_initial_df['initial_fitness'] = fitness_initial_df['fitness']
    fitness_df = fitness_df.merge(fitness_initial_df, on = ['solution','fitness'], how = 'left')

    return fitness_df, fitness_initial_df

def bitstring_to_string(bitstring):
    """
    Convert a bitstring (list of 0s and 1s) into a string.
    """
    return ''.join(map(str, bitstring))

def string_to_bitstring(string):
    """
    Convert a string into a bitstring (list of 0s and 1s).
    """
    return [int(char) for char in string]

def get_neighbors(bitstring):
    """
    Generate all neighbors of a given bitstring by flipping one bit at a time.

    Args:          bitstring (list): A list of 0s and 1s representing a bitstring.
    Returns:
        list: A list of bitstrings representing the neighbors.
    """
    neighbors = []
    for i in range(len(bitstring)):
        neighbor = bitstring.copy()
        neighbor[i] = 1 - neighbor[i]  # Flip the i-th bit
        neighbors.append(neighbor)
    return neighbors

def find_local_optima(fitness_df):
    """
    Find the local optima in the given fitness landscape.

    Args:
        fitness_df (pandas.DataFrame): A DataFrame containing the bitstrings and their fitness values.

    Returns:
        list: A list of bitstrings representing the local optima.
    """
    logging.info("Finding local optima")
    local_optima = []
    for _, row in fitness_df.iterrows():
        bitstring = string_to_bitstring(row['solution'])
        neighbors = [string_to_bitstring(neighbor) for neighbor in fitness_df['solution'].tolist() if sum(np.array(bitstring) != np.array(string_to_bitstring(neighbor))) == 1]
        neighbor_fitness = [fitness_df.loc[fitness_df['solution'] == bitstring_to_string(neighbor), 'fitness'].values[0] for neighbor in neighbors]
        is_local_optimum = True
        for neighbor_fit in neighbor_fitness:
            if row['fitness'] < neighbor_fit:
                is_local_optimum = False
                break
        if is_local_optimum:
            local_optima.append(bitstring_to_string(bitstring))
    local_optima_df = pd.DataFrame(local_optima, columns=['solution']).merge(fitness_df, on = 'solution', how = 'left')
    local_optima_df.loc[:,'local_optima_fitness'] = local_optima_df.loc[:,'fitness']
    local_optima_df = fitness_df.merge(local_optima_df[['solution','local_optima_fitness']], on = 'solution', how = 'left')
    return local_optima_df

def create_network(num_agents=10, num_neighbors=None, network_type='random', p=1.0, seed=0, graph_details=True, N=6, M=5):
    """
    Create a network of agents.

    Args:
        num_agents (int): Number of agents in network (if 'random').
        num_neighbors (deprecated).
        network_type (str): 'random' for Erdos-Renyi random network; 'subgroups' for N subnetworks of M agents each.
        p (float): Probability for edge creation in random network.
        seed (int): Random seed for reproducibility.
        graph_details (bool): Whether to print graph details.
        N (int): Number of subnetworks.
        M (int): Number of nodes per subnetwork.

    Returns:
        tuple: A tuple containing all_connections and df_all_connections.
    """
    logging.info(f"Creating {network_type} network")
    np.random.seed(seed)
    if network_type == 'random':
        logging.info(f"Creating {network_type} network of {num_agents} agents with p={p}")
    if network_type == 'subgroups':
        logging.info(f"Creating {network_type} network of {N*M} split into {N} groups of {M}")

    def assign_group_indices(G):
        # Find connected components
        components = list(nx.connected_components(G))

        # Create a dictionary to map nodes to their group index
        node_to_group = {}
        for idx, component in enumerate(components):
            for node in component:
                node_to_group[node] = idx

        return node_to_group

    # OPTION 1: random (Erdos-Renyi) network
    if network_type == 'random':
        G = nx.erdos_renyi_graph(n=num_agents, p=p, seed=seed)  # Create a random Erdos-Renyi undirected graph
        node_to_group = assign_group_indices(G)  # Assign group indices

        all_connections = {}
        for i in range(num_agents):
            neighbors = list(G.neighbors(i))
            group_index = node_to_group[i]
            all_connections[i] = [neighbors, group_index]

        if graph_details:
            logging.info("all_connections:")
            logging.info(all_connections)

    # OPTION 2: Equal subgroups (subnetworks)
    if network_type == 'subgroups':
        G = nx.Graph()  # Create a new graph
        # Create N subnetworks of M nodes each
        node_dict = {}
        subnetwork_index = 0
        node_index = 0
        for i in range(N):
            subnetwork_nodes = list(range(node_index, node_index + M))
            G.add_nodes_from(subnetwork_nodes)

            # Add edges within the subnetwork
            for j in range(M):
                node = subnetwork_nodes[j]
                neighbors = [subnetwork_nodes[k] for k in range(M) if k != j]
                node_dict[node] = [neighbors, subnetwork_index]
                for neighbor in neighbors:
                    G.add_edge(node, neighbor)

            node_index += M
            subnetwork_index += 1
        all_connections = node_dict
        if graph_details:
            logging.info("all_connections:")
            logging.info(all_connections)

    # Create a df containing all neighbors structured as 'target'->'source' for networkx graph
    df_all_connections = pd.DataFrame()

    if network_type == 'random' or network_type == 'subgroups':
        for i in all_connections.keys():
            for neighbor in all_connections[i][0]:  # Iterate over the neighbors list directly
                subnetwork_index = all_connections[i][1]
                row = pd.DataFrame({'source': i, 'target': neighbor, 'subnetwork_index': subnetwork_index}, index=[0])
                df_all_connections = pd.concat([df_all_connections, row], ignore_index=True)

    for i in range(len(df_all_connections)):
        df_all_connections.loc[i, 'nsource'] = 'n' + str(df_all_connections.loc[i, 'source'])
        df_all_connections.loc[i, 'ntarget'] = 'n' + str(df_all_connections.loc[i, 'target'])
    if graph_details:
        with pd.option_context('display.max_rows', None):
            display(df_all_connections.head(5))

    neighbor_counts = pd.DataFrame(df_all_connections['source'].value_counts()).reset_index()
    if graph_details:
        logging.info(f"Neighbor count min-max = {neighbor_counts['count'].min()}-{neighbor_counts['count'].max()}")
    if graph_details:
        df = df_all_connections
        # Create a graph from the DataFrame
        G = nx.from_pandas_edgelist(df, source='nsource', target='ntarget', create_using=nx.DiGraph())
        # Draw and display the graph
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True)
        if network_type == 'fixed' or network_type == 'subgroups':
            edge_labels = nx.get_edge_attributes(G, 'weight')  # currently only compatible with OPTION 1
        nx.draw_networkx_edge_labels(G, pos)  # edge_labels=edge_labels)

        plt.axis('off')
        plt.show()

    return all_connections, df_all_connections

def create_agents_params(all_connections):
    logging.info("Creating agents parameters")
    agents_params = {}
    # For each agent:
    for agent_i in list(all_connections.keys()):
        # Initialize empty dictionary per agent (we will name each change 'n' + their index number, e.g, 'n0', 'n8')
        agents_params['n'+str(agent_i)] = {}
        agents_params['n'+str(agent_i)]['neighbors_idx'] = all_connections[agent_i][0]   # store all neighbors' index numbers
        agents_params['n'+str(agent_i)]['local_idx'] = [agent_i] + all_connections[agent_i][0]    # store all index numbers for neighbors and agent itself)
        agents_params['n'+str(agent_i)]['subnetwork'] = all_connections[agent_i][1]   # store which subnetwork agent is in if applicable
        agents_params['n'+str(agent_i)]['neighbors'] = ['n' + str(j) for j in list(all_connections[agent_i][0])]  #collect neighbors, adding 'n' prefix

        # Hidden states
        agents_params['n'+str(agent_i)]['attention_state_names'] = ['self'] + agents_params['n'+str(agent_i)]['neighbors'] #attention states: self and neighbors
        agents_params['n'+str(agent_i)]['num_states'] = [len(agents_params['n'+str(agent_i)]['attention_state_names'])] #store num of states in 'attention' hidden state factor
        agents_params['n'+str(agent_i)]['num_factors'] = len(agents_params['n'+str(agent_i)]['num_states']) #store num of hidden state factors

        # Observations
        agents_params['n'+str(agent_i)]['outcome_obs_names'] = ['improvement','no improvement','unobserved'] # outcome modality
        agents_params['n'+str(agent_i)]['attention_obs_names'] = ['self'] + agents_params['n'+str(agent_i)]['neighbors'] # attention modality (self + one per neighbor)
        agents_params['n'+str(agent_i)]['num_obs'] = [len(agents_params['n'+str(agent_i)]['outcome_obs_names']), len(agents_params['n'+str(agent_i)]['attention_obs_names'])]
        agents_params['n'+str(agent_i)]['num_modalities'] = len(agents_params['n'+str(agent_i)]['num_obs'])

        # Actions
        agents_params['n'+str(agent_i)]['action_names'] = ['explore'] + ['exploit_' + str(j) for j in agents_params['n'+str(agent_i)]['neighbors']]  # explore + exploit (per neighbor)
        agents_params['n'+str(agent_i)]['num_controls'] = len(agents_params['n'+str(agent_i)]['action_names'])

    return agents_params

def inspect_agents(agents_params, agents=['n0','n1']):
    for agent in agents:
        logging.info(f"Inspecting agent {agent}")
        for key, value in agents_params[agent].items():
            logging.info(f"{key} : {value}")
        logging.info("")

def view_neighbors(agents_params):
    for agent_i in agents_params:
        logging.info(f"{[agent_i]}: {agents_params[agent_i]['neighbors']}")

def initialize_agents(agents_params, inference_horizon=1, inference_algo='MMP',policy_len=1, add_pD=True):   #sophisticated=False, save_belief_hist=True,
    logging.info("Initializing agents")
    # Initializing agents and storing into agents_list dict
    agents_list = {}
    for agent_i in list(agents_params.keys()):
        agents_list[agent_i] = Agent(A = agents_params[agent_i]['A'],
                                              B = agents_params[agent_i]['B'],
                                              C = agents_params[agent_i]['C'],
                                              D = agents_params[agent_i]['D'],
                                              E = agents_params[agent_i]['E'],
                                              pA = agents_params[agent_i]['pA'],  # added
                                              pB = agents_params[agent_i]['pB'],
                                              pD = agents_params[agent_i]['pD'],  # added
                                              inference_algo = inference_algo,
                                              policy_len=policy_len,
                                              inference_horizon=inference_horizon,
                                              sampling_mode = 'full', action_selection = 'stochastic')
        if add_pD == True:
            agents_list[agent_i].pD = agents_params[agent_i]['pD']

    return agents_list

def initialize_solutions(agents_list, fitness_initial_df, fitness_df, seed=0):
    logging.info("Initializing solutions for agents")
    # Initialize agents with solutions/fitness values (working but freezes on n28 fitness lookup)
    random.seed(seed)
    for agent_i in agents_list:
        agents_list[agent_i].current_solution = random.choice(fitness_initial_df['solution'].tolist()) # sample random row of initial solutions
        agents_list[agent_i].current_fitness = fitness_df[fitness_df['solution'].isin([agents_list[agent_i].current_solution])]['fitness'].values[0]
        logging.info(f"agent {agent_i} : {agents_list[agent_i].current_solution} with fitness {agents_list[agent_i].current_fitness}")

    return agents_list

def create_agents_full_sweep(fitness_df, fitness_initial_df, num_agents=10, num_neighbors=None, network_type='random', p=0.2, N=2, M=2, C_improvement_prefs=np.array([5, -1, 0]), seed=0, sophisticated=False, inference_algo='MMP', inference_horizon=1,policy_len=1,
                             show_details=False
                             #save_belief_hist=True):
                            ):
  all_connections, df_all_connections = create_network(num_agents=num_agents, num_neighbors=num_neighbors, network_type=network_type, p=p, N=N, M=M, seed=seed)
  agents_params = create_agents_params(all_connections=all_connections)
  agents_params = set_pomdp_variables(agents_params, C_improvement_prefs=C_improvement_prefs, show_details=False)
  agents_list = initialize_agents(agents_params, inference_horizon=inference_horizon, inference_algo=inference_algo,policy_len=policy_len)   #,sophisticated=sophisticated, save_belief_hist=save_belief_hist)
  agents_list = initialize_solutions(agents_list=agents_list, fitness_initial_df=fitness_initial_df, fitness_df=fitness_df, seed=0)
  return agents_params, agents_list

def inspect_agents(agents_params, agents=['n0','n1']):
  for agent in agents:
    print(f"agent {agent}:")
    for key, value in agents_params[agent].items():
      print(f"{key} : {value}")
    print("")

def view_neighbors(agents_params):
  for agent_i in agents_params:
    print(f"{[agent_i]}: {agents_params[agent_i]['neighbors']}")
    
def initialize_agents(agents_params, inference_horizon=1, inference_algo='MMP',policy_len=1, add_pD=True):   #sophisticated=False, save_belief_hist=True,
  # Initializing agents and storing into agents_list dict
  agents_list = {}
  for agent_i in list(agents_params.keys()):
    agents_list[agent_i] = Agent(A = agents_params[agent_i]['A'],
                                          B = agents_params[agent_i]['B'],
                                          C = agents_params[agent_i]['C'],
                                          D = agents_params[agent_i]['D'],
                                          E = agents_params[agent_i]['E'],
                                          pA = agents_params[agent_i]['pA'],  # added
                                          pB = agents_params[agent_i]['pB'],
                                          pD = agents_params[agent_i]['pD'],  # added
                                          inference_algo = inference_algo,
                                          policy_len=policy_len,
                                          #sophisticated = sophisticated,
                                          #save_belief_hist = save_belief_hist,
                                         inference_horizon=inference_horizon,
                                          sampling_mode = 'full', action_selection = 'stochastic')
    if add_pD == True:
      agents_list[agent_i].pD = agents_params[agent_i]['pD']

  return agents_list

def initialize_solutions(agents_list, fitness_initial_df, fitness_df, seed=0):
  # Initialize agents with solutions/fitness values (working but freezes on n28 fitness lookup)
  random.seed(seed)
  for agent_i in agents_list:
    agents_list[agent_i].current_solution = random.choice(fitness_initial_df['solution'].tolist()) # sample random row of initial solutions
    agents_list[agent_i].current_fitness = fitness_df[fitness_df['solution'].isin([agents_list[agent_i].current_solution])]['fitness'].values[0]
    print(f"agent {agent_i} : {agents_list[agent_i].current_solution} with fitness {agents_list[agent_i].current_fitness}")

  return agents_list

def create_agents_full_sweep(fitness_df, fitness_initial_df, num_agents=10, num_neighbors=None, network_type='random', p=0.2, N=2, M=2, C_improvement_prefs=np.array([5, -1, 0]), seed=0, sophisticated=False, inference_algo='MMP', inference_horizon=1,policy_len=1,
                             show_details=False
                             #save_belief_hist=True):
                            ):
  all_connections, df_all_connections = create_network(num_agents=num_agents, num_neighbors=num_neighbors, network_type=network_type, p=p, N=N, M=M, seed=seed)
  agents_params = create_agents_params(all_connections=all_connections)
  agents_params = set_pomdp_variables(agents_params, C_improvement_prefs=C_improvement_prefs, show_details=False)
  agents_list = initialize_agents(agents_params, inference_horizon=inference_horizon, inference_algo=inference_algo,policy_len=policy_len)   #,sophisticated=sophisticated, save_belief_hist=save_belief_hist)
  agents_list = initialize_solutions(agents_list=agents_list, fitness_initial_df=fitness_initial_df, fitness_df=fitness_df, seed=0)
  return agents_params, agents_list
