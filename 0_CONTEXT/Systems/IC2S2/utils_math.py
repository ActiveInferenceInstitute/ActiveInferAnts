import numpy as np
import pandas as pd
import random
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
    epsilon = 1e-10
    return arr / (np.sum(arr) + epsilon)

def initialize_matrices():
    """
    Initialize matrices A, B, C, D, E, and pA for the active inference model.

    Returns:
        tuple: A, B, C, D, E, pA matrices
    """
    logging.info("Initializing matrices")
    A = np.random.rand(3, 3)
    A = A / A.sum(axis=0, keepdims=True)
    A = np.nan_to_num(A, nan=1.0/A.shape[0])

    B = np.random.rand(3, 3, 2)
    B = B / B.sum(axis=0, keepdims=True)

    C = np.random.rand(3)
    D = np.random.rand(3)
    D = D / D.sum()

    E = np.random.rand(2)
    pA = np.random.rand(3)
    pA = pA / pA.sum()

    return A, B, C, D, E, pA

def create_nk_landscape(N=10, K=5, max_fitness=100, initial_fitness_limit=20, seed=0):
    """
    Create an NK fitness landscape.

    Args:
        N (int): Number of elements
        K (int): Interdependence parameter
        max_fitness (int): Maximum fitness value
        initial_fitness_limit (int): Initial fitness limit
        seed (int): Random seed for reproducibility

    Returns:
        tuple: fitness_df, fitness_initial_df
    """
    logging.info("Creating NK landscape")
    random.seed(seed)

    def get_fitness(bitstring, K):
        fitness = 0
        for i in range(N):
            indices = [i] + [(i+j+1) % N for j in range(1, K+1)]
            fitness_contribution = sum(bitstring[j] for j in indices) * random.uniform(0, 1)
            fitness += fitness_contribution
        return fitness

    bitstrings = [list(map(int, list(np.binary_repr(i, N)))) for i in range(2**N)]
    fitness_values_original = [get_fitness(bitstring, K) for bitstring in bitstrings]
    min_val, max_val = min(fitness_values_original), max(fitness_values_original)
    fitness_values = [(val - min_val) / (max_val - min_val) * max_fitness for val in fitness_values_original]

    bitstrings_strings = [''.join(map(str, bitstring)) for bitstring in bitstrings]
    fitness_df = pd.DataFrame({'solution': bitstrings_strings, 'fitness': fitness_values}).reset_index(drop=True)
    fitness_initial_df = fitness_df[fitness_df['fitness'] < initial_fitness_limit]
    fitness_initial_df['initial_fitness'] = fitness_initial_df['fitness']
    fitness_df = fitness_df.merge(fitness_initial_df, on=['solution', 'fitness'], how='left')

    return fitness_df, fitness_initial_df

def find_local_optima(fitness_df):
    """
    Find local optima in the NK fitness landscape.

    Args:
        fitness_df (pd.DataFrame): DataFrame containing fitness data

    Returns:
        pd.DataFrame: DataFrame containing local optima
    """
    logging.info("Finding local optima")
    local_optima = []
    for i in range(len(fitness_df)):
        current_fitness = fitness_df.iloc[i]['fitness']
        neighbors = fitness_df.iloc[max(0, i-1):min(len(fitness_df), i+2)]
        if all(current_fitness >= neighbors['fitness']):
            local_optima.append(fitness_df.iloc[i])
    return pd.DataFrame(local_optima)

def string_to_bitstring(string):
    """
    Convert a string of '0's and '1's to a list of integers.

    Args:
        string (str): Input string

    Returns:
        list: List of integers
    """
    return [int(char) for char in string]