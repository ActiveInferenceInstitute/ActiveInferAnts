import random
import pandas as pd

def initialize_solutions(agents_list, fitness_initial_df, fitness_df, seed=0):
    random.seed(seed)
    for agent in agents_list:
        initial_solution = random.choice(fitness_initial_df['solution'].tolist())
        agent.current_solution = initial_solution
        agent.current_fitness = fitness_df[fitness_df['solution'] == initial_solution]['fitness'].values[0]
    return agents_list

def initialize_fitness_dataframes():
    initial_solutions = [''.join(random.choices('01', k=10)) for _ in range(10)]
    initial_fitnesses = [random.uniform(0, 1) for _ in range(10)]
    fitness_initial_df = pd.DataFrame({'solution': initial_solutions, 'fitness': initial_fitnesses})
    all_fitnesses = [random.uniform(0, 1) for _ in range(100)]
    fitness_df = pd.DataFrame({'solution': initial_solutions * 10, 'fitness': all_fitnesses})
    return fitness_initial_df, fitness_df