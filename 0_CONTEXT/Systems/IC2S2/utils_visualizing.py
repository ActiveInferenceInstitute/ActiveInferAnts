import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from utils_math import create_nk_landscape, find_local_optima, string_to_bitstring
import logging
import os
import seaborn as sns

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Ensure the output directory exists
output_dir = './Output/Visualizations/'
os.makedirs(output_dir, exist_ok=True)

def plot_dist_animation(results, col):
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation
    from matplotlib import rc
    from IPython.display import HTML

    logging.info("Starting plot_dist_animation function")
    rc('animation', html='jshtml')
    all_data = []
    for i in range(len(results)):
        all_data.append(results.reset_index(drop=True)[col][i])
    fig, ax = plt.subplots()
    nbins = 15

    def animate(i):
        ax.clear()
        ax.hist(all_data[i], bins=nbins, density=False, range=(0,1))
        ax.set_title(f'Timestep: {i}')
        ax.set_ylabel('Count of agents')
        ax.set_xlabel(f'P(o=improvement|s=self) - {nbins} bins')
        ax.set_xlim(0,1)
        ax.set_ylim(0,len(all_data[i]))
        ax.set_xticks(np.arange(0,1.1,0.1))
        for x_val in np.arange(0,1.1,0.1):
          ax.axvline(x=x_val,color='gray', linestyle=':', alpha=0.3, zorder=0)

    ani = animation.FuncAnimation(fig, animate, frames=len(all_data), repeat=False, interval=200)

    # Convert the animation to HTML
    html_animation = HTML(ani.to_html5_video())
    plt.close()
    logging.info("Completed plot_dist_animation function")
    return html_animation

def plot_single_agent_inference_trial(T, prob_improve_self_list=None, prob_improve_neighbor_list=None, min_F_list=None, min_G_list=None, q_pi_explore_list=None, q_pi_exploit_list=None,
                                      explore_G_list=None, exploit_G_list=None, explore_F_list=None, exploit_F_list=None, obs_list=None, learning_indicator_list=None, is_learning=True, is_force_learn=False,
                                      force_neighbor_context=False, force_neighbor_context_at_t=None):
    logging.info("Starting plot_single_agent_inference_trial function")
    ylabel_size = 12
    # Create figure
    fig = plt.figure(figsize=(9, 6))
    # Create custom GridSpec with 6 rows
    gs = GridSpec(6, 1, figure=fig, height_ratios=[1, 3, 1, 3, 3, 1])
    # Create subplots with custom sizes and new order
    ax1 = fig.add_subplot(gs[0])  # Previously ax4
    ax2 = fig.add_subplot(gs[1], sharex=ax1)  # Unchanged
    ax3 = fig.add_subplot(gs[2], sharex=ax1)  # Previously ax6
    ax4 = fig.add_subplot(gs[3], sharex=ax1)  # Previously ax3
    ax5 = fig.add_subplot(gs[4], sharex=ax1)  # Previously ax1
    ax6 = fig.add_subplot(gs[5], sharex=ax1)  # Previously ax5

    # First subplot (ax1)
    improve_counter = 0
    no_improve_counter = 0
    dot_y_pos = 0
    for i, value in enumerate(obs_list):
        if value == 0:
            color = 'springgreen'
        elif value == 1:
            color = 'grey'
        elif value > 1:
            color = 'black'
        if improve_counter == 0 and value == 0:
            ax1.scatter(i, dot_y_pos, color=color, s=50, label='Improvement')
            improve_counter = 1
        elif no_improve_counter == 0 and value == 1:
            ax1.scatter(i, dot_y_pos, color=color, s=50, label='No improvement')
            no_improve_counter = 1
        else:
            ax1.scatter(i, dot_y_pos, color=color, s=50)
    ax1.set_ylabel('o_t', fontweight='bold', fontsize=ylabel_size)
    ax1.set_yticks([])  # Remove y-axis ticks
    ax1.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    # Second subplot (ax2)
    if min_F_list is not None:
        ax2.plot(range(T), min_F_list, color='pink', marker='o', linestyle='-', linewidth=7, alpha=0.8, markersize=4, label='F')
    if explore_F_list is not None:
        ax2.plot(range(T), explore_F_list, color='blue', marker='o', linestyle='-', linewidth=4, markersize=4, alpha=0.8, label='F_explore')
    if exploit_F_list is not None:
        ax2.plot(range(T), exploit_F_list, color='r', marker='o', linestyle='-', markersize=4, alpha=0.8, label='F_exploit')
    ax2.set_ylabel('F_t', fontweight='bold', fontsize=ylabel_size)
    ax2.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    # Third subplot (ax3)
    no_learning_indicator_counter = 0
    learning_indicator_counter = 0
    dot_y_pos = 0
    for i, value in enumerate(learning_indicator_list):
        if value == 0:
            color = 'white'
        elif value == 1:
            color = 'purple'
        elif value > 1:
            color = 'black'
        if no_learning_indicator_counter == 0 and value == 0:
            ax3.scatter(i, dot_y_pos, color=color, s=50, label='No learning at t')
            no_learning_indicator_counter = 1
        elif learning_indicator_counter == 0 and value == 1:
            ax3.scatter(i, dot_y_pos, color=color, s=50, label='Learning at t')
            learning_indicator_counter = 1
        else:
            ax3.scatter(i, dot_y_pos, color=color, s=50)
    ax3.set_ylabel('Learning', fontweight='bold', fontsize=ylabel_size)
    ax3.set_yticks([])  # Remove y-axis ticks
    ax3.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    # Fourth subplot (ax4)
    if min_G_list is not None:
        ax4.plot(range(T), min_G_list, color='pink', marker='o', linestyle='-', linewidth=7, alpha=0.8, markersize=4, label='G')
    if explore_G_list is not None:
        ax4.plot(range(T), explore_G_list, color='blue', marker='o', linestyle='-', linewidth=4, markersize=4, alpha=0.8, label='G_explore')
    if exploit_G_list is not None:
        ax4.plot(range(T), exploit_G_list, color='r', marker='o', linestyle='-', markersize=4, alpha=0.8, label='G_exploit')
    ax4.set_ylabel('G_t', fontweight='bold', fontsize=ylabel_size)
    ax4.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    # Fifth subplot (ax5)
    if q_pi_explore_list is not None:
        ax5.plot(range(T), q_pi_explore_list, color='blue', marker='o', linestyle='-', linewidth=4, markersize=4, alpha=0.8, label='q_pi_explore')
    if q_pi_exploit_list is not None:
        ax5.plot(range(T), q_pi_exploit_list, color='r', marker='o', linestyle='-', markersize=4, alpha=0.8, label='q_pi_exploit')
    ax5.set_ylabel('q_pi', fontweight='bold', fontsize=ylabel_size)
    ax5.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    # Sixth subplot (ax6)
    if prob_improve_self_list is not None:
        ax6.plot(range(T), prob_improve_self_list, color='blue', marker='o', linestyle='-', linewidth=4, markersize=4, alpha=0.8, label='P(o=improvement|s=self)')
    if prob_improve_neighbor_list is not None:
        ax6.plot(range(T), prob_improve_neighbor_list, color='r', marker='o', linestyle='-', markersize=4, alpha=0.8, label='P(o=improvement|s=neighbor)')
    ax6.set_ylabel('P(o|s)', fontweight='bold', fontsize=ylabel_size)
    ax6.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    # Add vertical lines for context changes and learning events
    for t in range(T):
        if t % 5 == 0:
            for ax in [ax1, ax2, ax3, ax4, ax5, ax6]:
                ax.axvline(x=t, color='black', linestyle=':', alpha=0.1)
    if is_learning == 'on':
        ax1.set_title(f'Free Energy Minimization with Likelihood (A) Learning every {learn_A_after_every_X_timesteps} steps', fontweight='bold', fontsize=12)
    elif is_force_learn != 'off':
        ax1.set_title(f'Free Energy Minimization with Likelihood (A) Learning at t={force_learn_at_t}', fontweight='bold', fontsize=12)
    else:
        ax1.set_title(f'Free Energy Minimization with Likelihood (A) without Learning', fontweight='bold', fontsize=12)

    ax6.set_xlabel('Timestep', fontweight='bold', fontsize=12)

    plt.tight_layout()
    plt.subplots_adjust(hspace=0.1)  # Adjust this value as needed
    output_path = os.path.join(output_dir, 'single_agent_inference_trial.png')
    plt.savefig(output_path)
    logging.info(f"Completed plot_single_agent_inference_trial function, saved to {output_path}")

def plot_nk_landscape(fitness_df, N, K, fitness_initial_df=None, local_optima_df=None, agents_list=None):
    logging.info("Starting plot_nk_landscape function")
    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(6, 4))
    # Plot the landscape
    ax.scatter(range(len(fitness_df)), fitness_df['fitness'], s=70, c='r', marker='o', alpha = 0.3, label = 'All solutions')
    if fitness_initial_df is not None:
        ax.scatter(range(len(fitness_df)), fitness_df['initial_fitness'], s=50, c='b', marker='o', alpha=0.3, label = 'Initial solutions')
    if local_optima_df is not None:
        ax.scatter(range(len(local_optima_df)), local_optima_df['local_optima_fitness'], s=30, c='green', marker = 'o', alpha=1.0, label = 'Local optimum')
    # Set axis labels and title
    ax.set_xlabel('Solution')
    ax.set_ylabel('Fitness')
    ax.set_title(f'NK Landscape with N={N}, K={K}: {len(fitness_df)} solutions total')
    # Set x-ticks with solution strings
    num_ticks = 5
    tick_indices = np.linspace(0, len(fitness_df)-1, num_ticks, dtype=int)
    ax.set_xticks(tick_indices)
    ax.set_xticklabels([fitness_df['solution'].iloc[i] for i in tick_indices], rotation=90)
    ax.legend()
    output_path = os.path.join(output_dir, 'nk_landscape.png')
    plt.savefig(output_path)
    logging.info(f"Completed plot_nk_landscape function, saved to {output_path}")

def create_and_plot_landscape(N=10, K=5, max_fitness=100, seed=0):
    logging.info("Starting create_and_plot_landscape function")
    initial_fitness_limit = max_fitness / 5
    fitness_df, fitness_initial_df = create_nk_landscape(N=N, K=K, max_fitness=max_fitness, initial_fitness_limit=initial_fitness_limit, seed=seed)
    local_optima_df = find_local_optima(fitness_df)
    plot_nk_landscape(fitness_df, N, K, fitness_initial_df=fitness_initial_df, local_optima_df=local_optima_df)
    logging.info("Completed create_and_plot_landscape function")
    return fitness_df, fitness_initial_df, local_optima_df

def plot_single_agent_results(T, results, learning, force_learn_at_t, force_neighbor_context, force_neighbor_context_at_t, output_dir):
    """
    Plot comprehensive results for a single agent's performance.

    Args:
    T (int): Total number of timesteps
    results (dict): Dictionary containing various result metrics
    learning (str): Learning mode ('on', 'off', or 'force')
    force_learn_at_t (int): Timestep at which forced learning occurs
    force_neighbor_context (bool): Whether neighbor context is forced
    force_neighbor_context_at_t (int): Timestep at which neighbor context is forced
    output_dir (str): Directory to save the output plot
    """
    logger.info("Starting plot_single_agent_results function")
    
    # Check if results is empty or not a DataFrame
    if results is None or not isinstance(results, pd.DataFrame) or results.empty:
        logger.warning("Results are empty or not in the expected format. Skipping plot generation.")
        return
    
    # Check if required columns exist
    required_columns = ['action_sampled_id', 'fitness', 'solution']
    if not all(col in results.columns for col in required_columns):
        logger.warning(f"Results DataFrame is missing one or more required columns: {required_columns}")
        logger.warning("Skipping plot generation.")
        return

    fig, axes = plt.subplots(4, 2, figsize=(20, 24))
    fig.suptitle("Single Agent Performance Over Time", fontsize=16)

    # Plot 1: Action Selection
    if 'action_sampled_id' in results:
        axes[0, 0].plot(results['action_sampled_id'], marker='o')
        axes[0, 0].set_ylabel('Action')
        axes[0, 0].set_title('Action Selection (0: Explore, 1: Exploit)')
        axes[0, 0].set_ylim(-0.1, 1.1)
        axes[0, 0].set_yticks([0, 1])
        axes[0, 0].set_yticklabels(['Explore', 'Exploit'])
    else:
        logger.warning("'action_sampled_id' not found in results")
        axes[0, 0].text(0.5, 0.5, 'Data not available', ha='center', va='center')

    # Plot 2: Fitness over time
    axes[0, 1].plot(results['fitness'], marker='o')
    axes[0, 1].set_ylabel('Fitness')
    axes[0, 1].set_title('Fitness Over Time')

    # Plot 3: Probability of improvement (self vs neighbor)
    axes[1, 0].plot(results['prob_improve_self'], label='Self', marker='o')
    axes[1, 0].plot(results['prob_improve_neighbor'], label='Neighbor', marker='o')
    axes[1, 0].set_ylabel('Probability')
    axes[1, 0].set_title('Probability of Improvement')
    axes[1, 0].legend()

    # Plot 4: Free Energy
    axes[1, 1].plot(results['vfe'], label='VFE', marker='o')
    axes[1, 1].plot(results['efe'], label='EFE', marker='o')
    axes[1, 1].set_ylabel('Free Energy')
    axes[1, 1].set_title('Variational and Expected Free Energy')
    axes[1, 1].legend()

    # Plot 5: Learning indicator
    axes[2, 0].plot(results['learning_indicator'], marker='o')
    axes[2, 0].set_ylabel('Learning')
    axes[2, 0].set_title('Learning Indicator (0: No Learning, 1: Learning)')
    axes[2, 0].set_ylim(-0.1, 1.1)
    axes[2, 0].set_yticks([0, 1])

    # Plot 6: Observation (improvement or not)
    axes[2, 1].plot(results['obs'], marker='o')
    axes[2, 1].set_ylabel('Observation')
    axes[2, 1].set_title('Observation (0: No Improvement, 1: Improvement)')
    axes[2, 1].set_ylim(-0.1, 1.1)
    axes[2, 1].set_yticks([0, 1])

    # Plot 7: Q-values for explore and exploit
    axes[3, 0].plot(results['q_pi_explore'], label='Explore', marker='o')
    axes[3, 0].plot(results['q_pi_exploit'], label='Exploit', marker='o')
    axes[3, 0].set_ylabel('Q-value')
    axes[3, 0].set_title('Q-values for Explore and Exploit')
    axes[3, 0].legend()

    # Plot 8: G values (min, explore, exploit)
    axes[3, 1].plot(results['min_G'], label='Min G', marker='o')
    axes[3, 1].plot(results['explore_G'], label='Explore G', marker='o')
    axes[3, 1].plot(results['exploit_G'], label='Exploit G', marker='o')
    axes[3, 1].set_ylabel('G Value')
    axes[3, 1].set_title('G Values (Min, Explore, Exploit)')
    axes[3, 1].legend()

    # Add vertical lines for context changes and learning events
    for ax in axes.flatten():
        ax.axvline(x=T*0.25, color='purple', linestyle=':', label='Context change')
        ax.axvline(x=T*0.5, color='black', linestyle='-', label='Major context change')
        ax.axvline(x=T*0.75, color='purple', linestyle=':', label='Context change')
        
        if force_neighbor_context and force_neighbor_context_at_t is not None:
            ax.axvline(x=force_neighbor_context_at_t, color='green', linestyle='--', label='Forced neighbor context')
        
        if learning == 'force' and force_learn_at_t is not None:
            ax.axvline(x=force_learn_at_t, color='red', linestyle='--', label='Forced learning')
        
        ax.set_xlabel('Timestep')
        ax.grid(True, which='both', linestyle='--', linewidth=0.5)

    # Remove duplicate labels
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    fig.legend(by_label.values(), by_label.keys(), loc='upper right')

    plt.tight_layout()
    output_path = os.path.join(output_dir, 'single_agent_results.png')
    plt.savefig(output_path)
    plt.close()

    logger.info(f"Completed plot_single_agent_results function, saved to {output_path}")

def visualize_agent_variables(agent, output_dir):
    """
    Visualize the A, B, C, D, E, F, G variables of the agent and save the plots.
    
    Args:
    agent (CustomAgent): The agent object containing the variables to visualize
    output_dir (str): Directory to save the output plots
    """
    logger.info("Visualizing agent variables")
    
    variables = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    
    for var_name in variables:
        if hasattr(agent, var_name):
            var = getattr(agent, var_name)
            
            if isinstance(var, np.ndarray):
                if var.dtype == object:  # Handle nested arrays
                    for i, sub_array in enumerate(var):
                        visualize_array(sub_array, f'Agent {var_name} Slice {i+1}', output_dir, f'agent_{var_name.lower()}_{i+1}')
                else:
                    visualize_array(var, f'Agent {var_name}', output_dir, f'agent_{var_name.lower()}')
            else:
                logger.warning(f"Cannot visualize {var_name}: not a numpy array")
    
    logger.info("Completed agent variable visualization")

def visualize_array(arr, title, output_dir, filename):
    plt.figure(figsize=(10, 8))
    
    if arr.ndim == 1:
        # For 1D arrays, use bar plot
        plt.bar(range(len(arr)), arr)
        plt.title(f'{title} Vector')
        plt.xlabel('Index')
        plt.ylabel('Value')
    elif arr.ndim == 2:
        # For 2D arrays, use heatmap
        sns.heatmap(arr, annot=True, cmap='viridis', fmt='.2f')
        plt.title(f'{title} Matrix')
    elif arr.ndim == 3:
        # For 3D arrays, plot each 2D slice
        n_slices = arr.shape[0]
        fig, axes = plt.subplots(1, n_slices, figsize=(5*n_slices, 4))
        if n_slices == 1:
            axes = [axes]
        for i, ax in enumerate(axes):
            sns.heatmap(arr[i], annot=True, cmap='viridis', fmt='.2f', ax=ax)
            ax.set_title(f'{title} Slice {i+1}')
    else:
        logger.warning(f"Cannot visualize array: unexpected shape {arr.shape}")
        return

    plt.tight_layout()
    output_path = os.path.join(output_dir, f'{filename}.png')
    plt.savefig(output_path)
    plt.close()
    
    logger.info(f"Saved visualization to {output_path}")

def plot_variable_dynamics(agent, T, output_dir):
    """
    Plot the dynamics of the A, B, C, D, E, F, G variables of the agent over time.
    
    Args:
    agent (CustomAgent): The agent object containing the variables to plot
    T (int): Total number of timesteps
    output_dir (str): Directory to save the output plots
    """
    logger.info("Plotting variable dynamics")
    
    variables = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    
    for var_name in variables:
        if hasattr(agent, var_name):
            var = getattr(agent, var_name)
            
            if var_name in ['A', 'B', 'C', 'D']:
                # For matrices, plot each row as a separate line
                plt.figure(figsize=(10, 8))
                for i in range(var.shape[0]):
                    plt.plot(range(T), var[:, i], label=f'Row {i+1}')
                plt.title(f'Agent {var_name} Matrix Dynamics')
                plt.xlabel('Timestep')
                plt.ylabel('Value')
                plt.legend()
            elif var_name in ['E', 'F', 'G']:
                # For vectors, plot the values over time
                plt.figure(figsize=(10, 8))
                plt.plot(range(T), var)
                plt.title(f'Agent {var_name} Vector Dynamics')
                plt.xlabel('Timestep')
                plt.ylabel('Value')
            
            plt.tight_layout()
            output_path = os.path.join(output_dir, f'agent_{var_name.lower()}_dynamics.png')
            plt.savefig(output_path)
            plt.close()
            
            logger.info(f"Saved dynamics plot of agent {var_name} to {output_path}")
    
    logger.info("Completed variable dynamics plotting")
