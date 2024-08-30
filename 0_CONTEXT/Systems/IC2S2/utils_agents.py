import logging
import numpy as np
import pandas as pd
from pymdp.agent import Agent
import networkx as nx
from datetime import datetime
import random  # Import the random module

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def initialize_matrices(N=5, M=5):
    """
    Initialize matrices A, B, C, D, E, and pA for the active inference model.

    Args:
        N (int): Number of rows for matrices
        M (int): Number of columns for matrices

    Returns:
        tuple: A, B, C, D, E, pA matrices
    """
    A = np.random.rand(N, M)
    A = A / A.sum(axis=0, keepdims=True)
    A = np.nan_to_num(A, nan=1.0/N)

    B = np.random.rand(N, M, 2)
    B = B / B.sum(axis=0, keepdims=True)

    C = np.random.rand(M)
    D = np.random.rand(N)
    D = D / D.sum()

    E = np.random.rand(N, M)
    pA = np.random.rand(N)
    pA = pA / pA.sum()

    return A, B, C, D, E, pA

class CustomAgent(Agent):
    def __init__(self, A, B, C, D, E, pA, inference_algo='MMP', policy_len=1, inference_horizon=1, sampling_mode='full', action_selection='stochastic'):
        super().__init__(A=A, B=B, C=C, D=D, pA=pA, inference_algo=inference_algo, policy_len=policy_len, inference_horizon=inference_horizon)
        self.E = E
        self.sampling_mode = sampling_mode
        self.action_selection = action_selection
        self.q_pi = None
        self.policies = None
        self.num_controls = B.shape[2] if B is not None and len(B.shape) > 2 else None
        if self.num_controls is None:
            logger.warning("num_controls is None. Make sure B matrix is properly initialized.")
        self.alpha = 1.0
        self.current_solution = None
        self.current_fitness = None  # Ensure current_fitness is initialized
        self.G = np.zeros((1,))  # Initialize G properly
        self.F = None  # Initialize F attribute
        self.subnetwork = 0

    def sample_action(self):
        """
        Sample an action based on the current policy.

        Returns:
            int: Sampled action
        """
        if self.num_controls is None:
            logger.error("num_controls is None. Cannot sample action.")
            return None
        self.q_pi = np.ones(self.num_controls) / self.num_controls
        return np.random.choice(self.num_controls)

    def update_free_energy(self):
        """
        Update the Variational Free Energy (F) of the agent.
        """
        # Placeholder for actual free energy calculation
        self.F = np.random.rand(1)  # Replace with actual calculation

def create_agents_full_sweep(fitness_df, fitness_initial_df, num_agents=10, num_neighbors=None, network_type='random', p=0.1, N=5, M=5, C_improvement_prefs=0.5, seed=42, inference_algo='MMP', inference_horizon=2, policy_len=1):
    """
    Create agents for a full sweep simulation.

    Args:
        fitness_df (pd.DataFrame): DataFrame containing fitness data
        fitness_initial_df (pd.DataFrame): DataFrame containing initial fitness data
        num_agents (int): Number of agents
        num_neighbors (int): Number of neighbors
        network_type (str): Type of network ('random' or 'small-world')
        p (float): Probability for network generation
        N (int): Number of rows for matrices
        M (int): Number of columns for matrices
        C_improvement_prefs (float): Improvement preferences
        seed (int): Random seed for reproducibility
        inference_algo (str): Inference algorithm
        inference_horizon (int): Inference horizon
        policy_len (int): Policy length

    Returns:
        tuple: agents_params, agents_list
    """
    np.random.seed(seed)
    if network_type == 'random':
        G = nx.erdos_renyi_graph(num_agents, p)
    elif network_type == 'small-world':
        G = nx.watts_strogatz_graph(num_agents, k=4, p=p)
    else:
        raise ValueError("Invalid network type. Choose 'random' or 'small-world'.")

    agents_list = []
    agents_params = {}

    for i in range(num_agents):
        try:
            A, B, C, D, E, pA = initialize_matrices(N, M)
            if not np.allclose(A.sum(axis=0), 1.0, atol=1e-6):
                logger.warning(f"A matrix for agent {i} is not normalized. Applying final normalization.")
                A = A / A.sum(axis=0, keepdims=True)
            if not np.allclose(A.sum(axis=0), 1.0, atol=1e-6):
                raise ValueError(f"A matrix for agent {i} could not be normalized.")

            agent = CustomAgent(A=A, B=B, C=C, D=D, E=E, pA=pA,
                                inference_algo=inference_algo, policy_len=policy_len,
                                inference_horizon=inference_horizon, sampling_mode='full',
                                action_selection='stochastic')
            agent.current_solution = random.choice(fitness_df['solution'].tolist())  # Ensure current_solution exists in fitness_df
            agent.current_fitness = fitness_df[fitness_df['solution'] == agent.current_solution]['fitness'].values[0]  # Initialize current_fitness
            agent.subnetwork = 0  # Assign all agents to subnetwork 0 for simplicity, or implement your own subnetwork assignment logic
            agents_list.append(agent)
            agents_params[i] = {'neighbors': list(G.neighbors(i)), 'C_improvement_pref': C_improvement_prefs}
        except Exception as e:
            logger.error(f"Error creating agent {i}: {str(e)}")
            raise

    return agents_params, agents_list

def process_subnetwork_results(subnetwork_dict_1, subnetwork_dict_2, error_rate, p, C_improvement_pref, learn_A_after_every_X_timesteps_i, trial, network_type):
    """
    Process subnetwork results.

    Args:
        subnetwork_dict_1 (dict): Subnetwork dictionary for stage 1
        subnetwork_dict_2 (dict): Subnetwork dictionary for stage 2
        error_rate (float): Error rate
        p (float): Probability for network generation
        C_improvement_pref (float): Improvement preferences
        learn_A_after_every_X_timesteps_i (int): Learning interval
        trial (int): Trial number
        network_type (str): Type of network

    Returns:
        dict: Processed subnetwork dictionary
    """
    logger.info("Processing subnetwork results with error_rate: %s, p: %s, C_improvement_pref: %s, learn_A_after_every_X_timesteps_i: %s, trial: %s, network_type: %s", 
                error_rate, p, C_improvement_pref, learn_A_after_every_X_timesteps_i, trial, network_type)
    
    for i in range(len(subnetwork_dict_1)):
        subnetwork_dict_1[i]['stage'] = ['First'] * len(subnetwork_dict_1[i]['avg_efe'])
        subnetwork_dict_2[i]['stage'] = ['Second'] * len(subnetwork_dict_2[i]['avg_efe'])

    subnetwork_dict = {key: {inner_key: subnetwork_dict_1[key][inner_key] + subnetwork_dict_2[key][inner_key] for inner_key in subnetwork_dict_1[key]} for key in subnetwork_dict_1}
    
    for i in range(len(subnetwork_dict)):
        subnetwork_dict[i]['error_rate'] = [error_rate] * len(subnetwork_dict[i]['avg_efe'])
        subnetwork_dict[i]['p'] = [p] * len(subnetwork_dict[i]['avg_efe'])
        subnetwork_dict[i]['C_improvement_prefs'] = [C_improvement_pref] * len(subnetwork_dict[i]['avg_efe'])
        subnetwork_dict[i]['learn_A_after_every_X_timesteps'] = [learn_A_after_every_X_timesteps_i] * len(subnetwork_dict[i]['avg_efe'])
        subnetwork_dict[i]['trial'] = [trial] * len(subnetwork_dict[i]['avg_efe'])
        subnetwork_dict[i]['network_type'] = [network_type] * len(subnetwork_dict[i]['avg_efe'])

    logger.info("Subnetwork results processed successfully")
    return subnetwork_dict

def initialize_solutions(agents_list, fitness_initial_df, fitness_df, seed=0):
    """
    Initialize solutions for agents.

    Args:
        agents_list (list): List of agents
        fitness_initial_df (pd.DataFrame): DataFrame containing initial fitness data
        fitness_df (pd.DataFrame): DataFrame containing all fitness data
        seed (int): Random seed for reproducibility

    Returns:
        list: Updated list of agents with initialized solutions
    """
    random.seed(seed)
    for agent in agents_list:
        initial_solution = random.choice(fitness_initial_df['solution'].tolist())
        agent.current_solution = initial_solution
        agent.current_fitness = fitness_df[fitness_df['solution'] == initial_solution]['fitness'].values[0]
    
    return agents_list

def output_agent_matrices(agent):
    """
    Output the ABCDE matrices of the given agent.

    Args:
        agent (CustomAgent): The agent whose matrices are to be output

    Returns:
        dict: Dictionary containing the matrices
    """
    matrices = {
        'A': agent.A,
        'B': agent.B,
        'C': agent.C,
        'D': agent.D,
        'E': agent.E
    }
    return matrices

def initialize_fitness_dataframes():
    """
    Initialize fitness_df and fitness_initial_df with sample data.

    Returns:
        tuple: fitness_initial_df, fitness_df
    """
    # Create sample data for fitness_initial_df
    initial_solutions = [''.join(random.choices('01', k=10)) for _ in range(10)]
    initial_fitnesses = [random.uniform(0, 1) for _ in range(10)]
    fitness_initial_df = pd.DataFrame({'solution': initial_solutions, 'fitness': initial_fitnesses})

    # Use the same solutions for fitness_df to ensure overlap
    all_fitnesses = [random.uniform(0, 1) for _ in range(100)]
    fitness_df = pd.DataFrame({'solution': initial_solutions * 10, 'fitness': all_fitnesses})

    return fitness_initial_df, fitness_df

