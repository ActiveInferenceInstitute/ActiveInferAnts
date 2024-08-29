import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from utils_math import create_nk_landscape, find_local_optima
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

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
    ax3.set_ylabel('Learn', fontweight='bold', fontsize=ylabel_size)
    ax3.set_yticks([])  # Remove y-axis ticks
    ax3.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    # Fourth subplot (ax4)
    if min_G_list is not None:
        ax4.plot(range(T), min_G_list, color='purple', marker='o', linestyle='-', markersize=4, alpha=0.8, label='G')
    if explore_G_list is not None:
        ax4.plot(range(T), explore_G_list, color='blue', marker='o', linestyle='-', markersize=4, alpha=0.8, label='G_explore')
    if exploit_G_list is not None:
        ax4.plot(range(T), exploit_G_list, color='r', marker='o', linestyle='-', markersize=6, alpha=0.8, label='G_exploit')
    ax4.set_ylabel('G_t', fontweight='bold', fontsize=ylabel_size)
    ax4.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    # Fifth subplot (ax5)
    ax5.plot(range(T), prob_improve_self_list, color='brown', marker='o', linestyle='-', markersize=4, linewidth=4, alpha=0.7, label='P(o=improvement|s=self)')
    if prob_improve_neighbor_list is not None:
        ax5.plot(range(T), prob_improve_neighbor_list, color='darkorange', marker='o', linestyle='-', markersize=4, linewidth=4, alpha=0.7, label='P(o=improvement|s=neighbor)')
    if q_pi_explore_list is not None:
        ax5.plot(range(T), q_pi_explore_list, color='blue', marker='o', linestyle='-', markersize=4, alpha=0.7, label='q_pi Explore')
    if q_pi_exploit_list is not None:
        ax5.plot(range(T), q_pi_exploit_list, color='red', marker='o', linestyle='-', markersize=4, alpha=0.7, label='q_pi Exploit')
    ax5.set_ylabel('Probability', fontweight='bold', fontsize=ylabel_size)
    ax5.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    # Sixth subplot (ax6)
    explore_counter = 0
    exploit_counter = 0
    dot_y_pos = 0
    for i, value in enumerate(action_sampled_id_list):
        if value == 0:
            color = 'blue'
        elif value == 1:
            color = 'red'
        elif value > 1:
            color = 'black'
        if explore_counter == 0 and value == 0:
            ax6.scatter(i, dot_y_pos, color=color, s=50, label='Choose Explore for t+1')
            explore_counter = 1
        elif exploit_counter == 0 and value == 1:
            ax6.scatter(i, dot_y_pos, color=color, s=50, label='Choose Exploit for t+1')
            exploit_counter = 1
        else:
            ax6.scatter(i, dot_y_pos, color=color, s=50)
    ax6.set_ylabel('a_t+1', fontweight='bold', fontsize=ylabel_size)
    ax6.set_yticks([])  # Remove y-axis ticks
    ax6.legend(loc='center left', bbox_to_anchor=(1, 0.5))

    for ax in (ax1, ax2, ax3, ax4, ax5, ax6):
        ax.grid(axis='y', linestyle='--', alpha=0.7)
        ax.axvline(x=T*0.0, color='black', linestyle='-', label='Context=neighbor')
        if force_neighbor_context_at_t is not None and force_neighbor_context:
            ax.axvline(x=force_neighbor_context_at_t, color='black', linestyle='-', label='Context=neighbor')
        ax.axvline(x=int(T*0.25), color='purple', linestyle=':', label='Context=self')
        ax.axvline(x=int(T*0.5), color='black', linestyle='-')
        ax.axvline(x=int(T*0.75), color='purple', linestyle=':')
        for t in range(T):
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

def plot_results_stacked(results, fontsize=10):
    logging.info("Starting plot_results_stacked function")
    max_fitness_idx_1 = results[results['stage'] == 'First']['max_fitness'].idxmax()
    max_fitness_idx_2 = results[results['stage'] == 'Second']['max_fitness'].idxmax()
    # Find the row index where stage changes from 'First' to 'Second'
    stage_change_idx = results[results['stage'] == 'Second'].index[0]
    # Create a figure with 1 row and 5  columns of subplots
    fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(12, 6))

    axes[0,0].plot(results['avg_all_agent_actions'])
    axes[0,0].set_title("Explore-Exploit Action \nRatio", fontsize=fontsize)
    axes[0,0].set_xlabel('Timestep')
    axes[0,0].set_ylabel('Explore-Exploit \n(explore=0, exploit=1)')
    axes[0,0].axvline(x=max_fitness_idx_1, color='r', linestyle='--', label=f'Max at t={max_fitness_idx_1}')
    axes[0,0].axvline(x=max_fitness_idx_2, color='r', linestyle='--', label=f'Max at t={max_fitness_idx_2}')
    axes[0,0].axvline(x=stage_change_idx, color='black', linewidth=3, label=f'Stage 2 at t={stage_change_idx}')
    axes[0,0].grid()

    axes[0,1].plot(results['number_of_unique_solutions'])
    axes[0,1].set_title("Number of \nunique solutions", fontsize=fontsize)
    axes[0,1].set_xlabel('Timestep')
    axes[0,1].set_ylabel('Count')
    axes[0,1].axvline(x=max_fitness_idx_1, color='r', linestyle='--', label=f'Max at t={max_fitness_idx_1}')
    axes[0,1].axvline(x=max_fitness_idx_2, color='r', linestyle='--', label=f'Max at t={max_fitness_idx_2}')
    axes[0,1].axvline(x=stage_change_idx, color='g', linewidth=3, label=f'Stage 2 at t={stage_change_idx}')
    axes[0,1].grid()

    axes[0,2].plot(results['min_fitness'], color='purple', label='min')
    axes[0,2].plot(results['max_fitness'], color='orange', label='max')
    axes[0,2].plot(results['avg_bottom_50_fitness'], color = 'grey', label='Bottom 50%')
    axes[0,2].plot(results['avg_top_50_fitness'], color = 'grey', label='Top 50%')
    axes[0,2].plot(results['average_fitness'], color = 'blue', label='Average')
    axes[0,2].set_title("Fitness", fontsize=fontsize)
    axes[0,2].set_xlabel('Timestep')
    axes[0,2].set_ylabel('fitness')
    axes[0,2].legend()
    axes[0,2].grid()
    axes[0,2].set_title("Min and Max \nFitness", fontsize=fontsize)
    axes[0,2].set_xlabel('Timestep')
    axes[0,2].set_ylabel('Fitness')
    axes[0,2].axvline(x=max_fitness_idx_1, color='r', linestyle='--', label=f'Max at t={max_fitness_idx_1}')
    axes[0,2].axvline(x=max_fitness_idx_2, color='r', linestyle='--', label=f'Max at t={max_fitness_idx_2}')
    axes[0,2].axvline(x=stage_change_idx, color='black', linewidth=3, label=f'Stage 2 at t={stage_change_idx}')
    #axes[0,2].legend(loc='lower right')
    axes[0,2].legend(loc=(1.1,0.1))  #17/30, 300/600
    axes[0,2].grid()

    axes[1,0].plot(results['all_agents_A_explore_beliefs'])
    axes[1,0].set_title("Average belief in \nexplore-improve", fontsize=fontsize)
    axes[1,0].set_xlabel('Timestep')
    axes[1,0].set_ylabel('Probability')
    axes[1,0].axvline(x=max_fitness_idx_1, color='r', linestyle='--', label=f'Max at t={max_fitness_idx_1}')
    axes[1,0].axvline(x=max_fitness_idx_2, color='r', linestyle='--', label=f'Max at t={max_fitness_idx_2}')
    axes[1,0].axvline(x=stage_change_idx, color='black', linewidth=3, label=f'Stage 2 at t={stage_change_idx}')
    axes[1,0].grid()

    axes[1,1].plot(results['avg_all_agent_errors'])
    axes[1,1].set_title("Average number \nof errors", fontsize=fontsize)
    axes[1,1].set_xlabel('Timestep')
    axes[1,1].set_ylabel('Count')
    axes[1,1].axvline(x=max_fitness_idx_1, color='r', linestyle='--', label=f'Max at t={max_fitness_idx_1}')
    axes[1,1].axvline(x=max_fitness_idx_2, color='r', linestyle='--', label=f'Max at t={max_fitness_idx_2}')
    axes[1,1].axvline(x=stage_change_idx, color='black', linewidth=3, label=f'Stage 2 at t={stage_change_idx}')
    axes[1,1].grid()

    axes[1,2].plot(results['avg_efe'], color = 'orange', label = 'EFE_explore')
    axes[1,2].plot(results['avg_vfe'], color = 'purple', label = 'VFE_min')
    axes[1,2].set_title("Free Energy", fontsize=fontsize)
    axes[1,2].set_xlabel('Timestep')
    axes[1,2].set_ylabel('free energy')
    axes[1,2].axvline(x=max_fitness_idx_1, color='r', linestyle='--', label=f'Max at t={max_fitness_idx_1}')
    axes[1,2].axvline(x=max_fitness_idx_2, color='r', linestyle='--', label=f'Max at t={max_fitness_idx_2}')
    axes[1,2].axvline(x=stage_change_idx, color='black', linewidth=3, label=f'Stage 2 at t={stage_change_idx}')
    axes[1,2].legend(loc=(1.1,0.4))  #17/30, 300/600
    axes[1,2].grid()

    #if annotation_text:
    fig.suptitle(f"""
    Trial {results.iloc[0]['trial']}
    Network Type '{results.iloc[0]['network_type']}'
    p = {results.iloc[0]['p']}, e = {results.loc[0]['error_rate']},
    C_improvement_prefs = {results.loc[0]['C_improvement_prefs']},
    Average Explore Belief
    Start-End Difference = {round(results.iloc[len(results)-1]['all_agents_A_explore_beliefs'] - results.iloc[0]['all_agents_A_explore_beliefs'], 2)}
    Learn A every X timesteps = {results.iloc[0]['learn_A_after_every_X_timesteps']}""",
                 fontsize=11, x=0.9, y=0.2, ha='left')
    # fig.suptitle(f"Trial {results.iloc[0]['trial']}", fontsize=14, x=0.1, y=0.5, ha='left')
    plt.subplots_adjust(wspace=0.3, hspace=0.5) # Adjust the spacing between subplots


def process_results_all_trials(results_all_trials):
    for trial in results_all_trials['trial'].unique():
        print(f"Trial {trial} results -------------------------------------------------")
        plot_results_stacked(results_all_trials[results_all_trials['trial'] == trial].reset_index(drop=True))
        
        # Plot results per subnetwork
        for trial in range(len(subnetwork_dict_all_trials)):
            for subnetwork_i in range(len(subnetwork_dict_all_trials[trial])):
                print(f"Trial {trial}: subnetwork {subnetwork_i}")
                plot_results_stacked(pd.DataFrame(subnetwork_dict_all_trials[trial][subnetwork_i]))
                print(f"--------------------------------------------------------------")
        
        print(len(subnetwork_dict_all_trials))

def plot_dist_animation(results, col):
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation
    from matplotlib import rc
    from IPython.display import HTML

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
    return html_animation
