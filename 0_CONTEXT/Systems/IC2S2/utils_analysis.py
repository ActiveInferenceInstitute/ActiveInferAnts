import logging
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

logger = logging.getLogger(__name__)

def process_results_all_trials(results_all_trials, output_dir):
    logger.info("Processing all trial results")
    
    if results_all_trials.empty:
        logger.warning("No results to process. All trials may have failed.")
        return

    logger.info(f"Available columns: {results_all_trials.columns.tolist()}")

    trial_mean_fitness = results_all_trials.groupby('trial')['average_fitness'].mean().reset_index()

    plt.figure(figsize=(12, 6))
    sns.violinplot(x='network_type', y='average_fitness', data=results_all_trials)
    plt.title('Distribution of Average Fitness by Network Type')
    plt.savefig(os.path.join(output_dir, 'fitness_by_network_type_violin.png'))
    plt.close()

    pivot_columns = ['C_improvement_pref', 'learn_A_after_every_X_timesteps']
    if 'C_improvement_prefs' in results_all_trials.columns:
        pivot_columns[0] = 'C_improvement_prefs'

    try:
        pivot_table = results_all_trials.pivot_table(
            values='average_fitness', 
            index=['error_rate', 'p'], 
            columns=pivot_columns,
            aggfunc='mean'
        )
        plt.figure(figsize=(15, 10))
        sns.heatmap(pivot_table, annot=True, cmap='YlGnBu')
        plt.title('Average Fitness Heatmap')
        plt.savefig(os.path.join(output_dir, 'fitness_heatmap.png'))
        plt.close()
    except KeyError as e:
        logger.error(f"Error creating pivot table: {str(e)}")
        logger.info("Skipping heatmap creation due to KeyError")

    plt.figure(figsize=(12, 6))
    for network_type in results_all_trials['network_type'].unique():
        data = results_all_trials[results_all_trials['network_type'] == network_type]
        sns.lineplot(x='trial', y='average_fitness', data=data, label=network_type)
    plt.title('Average Fitness Over Trials by Network Type')
    plt.xlabel('Trial')
    plt.ylabel('Average Fitness')
    plt.legend()
    plt.savefig(os.path.join(output_dir, 'fitness_over_trials_by_network_type.png'))
    plt.close()

    plt.figure(figsize=(10, 8))
    sns.scatterplot(x='min_fitness', y='max_fitness', hue='network_type', data=results_all_trials)
    plt.title('Max Fitness vs Min Fitness by Network Type')
    plt.xlabel('Min Fitness')
    plt.ylabel('Max Fitness')
    plt.savefig(os.path.join(output_dir, 'max_vs_min_fitness_scatter.png'))
    plt.close()

    results_all_trials['fitness_improvement'] = results_all_trials['max_fitness'] - results_all_trials['min_fitness']
    plt.figure(figsize=(10, 6))
    sns.histplot(data=results_all_trials, x='fitness_improvement', hue='network_type', kde=True)
    plt.title('Distribution of Fitness Improvement by Network Type')
    plt.xlabel('Fitness Improvement')
    plt.savefig(os.path.join(output_dir, 'fitness_improvement_distribution.png'))
    plt.close()

    fitness_vars = ['average_fitness', 'max_fitness', 'min_fitness', 'fitness_improvement']
    corr_matrix = results_all_trials[fitness_vars].corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap of Fitness Variables')
    plt.savefig(os.path.join(output_dir, 'fitness_correlation_heatmap.png'))
    plt.close()

    logger.info("Completed processing all trial results")