import json
import logging
import argparse
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from typing import Dict, List, Any
from collections import defaultdict
import matplotlib.colors as mcolors

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

STATES = ["IN_POWER", "HIGH_POWER", "MEDIUM_POWER", "LOW_POWER", "HOMO_SACER"]

def load_config(config_file: str) -> Dict[str, Any]:
    """Load configuration from a JSON file."""
    with open(config_file, 'r') as f:
        return json.load(f)

def load_simulation_results(file_path: str) -> List[Dict[str, Any]]:
    """Load simulation results from a JSON file."""
    with open(file_path, 'r') as f:
        return json.load(f)

def calculate_state_percentages(results: List[Dict[str, Any]], before_crisis: int) -> Dict[str, Dict[str, Dict[str, float]]]:
    """Calculate the percentage of time each entity spends in each state before and after the crisis."""
    entity_states = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))
    total_steps = len(results)
    all_entities = set()

    for step, result in enumerate(results):
        period = "before" if step < before_crisis else "after"
        for entity in result['entities']:
            all_entities.add(entity['name'])
            entity_states[entity['name']][period][entity['state']] += 1

    percentages = {}
    for entity in all_entities:
        percentages[entity] = {}
        for period in ['before', 'after']:
            total = sum(entity_states[entity][period].values())
            if total > 0:
                percentages[entity][period] = {state: entity_states[entity][period][state] / total * 100 for state in STATES}
            else:
                percentages[entity][period] = {state: 0 for state in STATES}

    return percentages

def plot_state_percentages(percentages: Dict[str, Dict[str, Dict[str, float]]], output_file: str):
    """Create a grouped bar plot of state percentages for each entity before and after the crisis."""
    data = []
    for entity, periods in percentages.items():
        for period, states in periods.items():
            for state, percentage in states.items():
                data.append({'Entity': entity, 'Period': period, 'State': state, 'Percentage': percentage})

    df = pd.DataFrame(data)
    
    # Set up the plot
    plt.figure(figsize=(20, 10))
    
    # Define the width of each bar and the positions of the bars
    bar_width = 0.35
    entities = sorted(percentages.keys())
    n_entities = len(entities)
    n_states = len(STATES)
    
    # Create a color palette for the states
    colors = plt.cm.Set3(np.linspace(0, 1, n_states))
    
    # Create positions for each group of bars
    indices = np.arange(n_entities)
    
    # Plot bars for each state
    for i, state in enumerate(STATES):
        before_data = df[(df['Period'] == 'before') & (df['State'] == state)].set_index('Entity').reindex(entities)['Percentage'].fillna(0)
        after_data = df[(df['Period'] == 'after') & (df['State'] == state)].set_index('Entity').reindex(entities)['Percentage'].fillna(0)
        
        plt.bar(indices - bar_width/2, before_data, bar_width, label=f'{state} (Before)', color=colors[i], alpha=0.8)
        plt.bar(indices + bar_width/2, after_data, bar_width, label=f'{state} (After)', color=colors[i], alpha=0.5, hatch='//')
    
    # Customize the plot
    plt.xlabel('Entity', fontweight='bold', fontsize=12)
    plt.ylabel('Percentage', fontweight='bold', fontsize=12)
    plt.title('Entity State Percentages Before and After Crisis', fontweight='bold', fontsize=14)
    plt.xticks(indices, entities, rotation=45, ha='right')
    
    # Add a legend
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys(), title="States", 
               bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=10)
    
    # Add percentage labels on the bars
    for i, state in enumerate(STATES):
        before_data = df[(df['Period'] == 'before') & (df['State'] == state)].set_index('Entity').reindex(entities)['Percentage'].fillna(0)
        after_data = df[(df['Period'] == 'after') & (df['State'] == state)].set_index('Entity').reindex(entities)['Percentage'].fillna(0)
        
        for j, (before, after) in enumerate(zip(before_data, after_data)):
            if before > 0:
                plt.text(j - bar_width/2, before/2, f'{before:.1f}%', ha='center', va='center', fontsize=8)
            if after > 0:
                plt.text(j + bar_width/2, after/2, f'{after:.1f}%', ha='center', va='center', fontsize=8)
    
    plt.tight_layout()
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.close()

    logger.info(f"State percentages plot saved to {output_file}")

def calculate_state_volatility(results: List[Dict[str, Any]]) -> Dict[str, float]:
    """Calculate the state volatility for each entity."""
    entity_transitions = defaultdict(int)
    entity_total_steps = defaultdict(int)

    for i in range(1, len(results)):
        prev_result = results[i-1]
        curr_result = results[i]

        for prev_entity, curr_entity in zip(prev_result['entities'], curr_result['entities']):
            assert prev_entity['name'] == curr_entity['name']
            entity_name = prev_entity['name']
            entity_total_steps[entity_name] += 1
            if prev_entity['state'] != curr_entity['state']:
                entity_transitions[entity_name] += 1

    volatility = {entity: transitions / entity_total_steps[entity] 
                  for entity, transitions in entity_transitions.items()}
    return volatility

def main():
    parser = argparse.ArgumentParser(description="Analyze Cognitive Sovereignty simulation results")
    parser.add_argument("config", help="Path to configuration file")
    args = parser.parse_args()

    config = load_config(args.config)
    results = load_simulation_results(f"{config['output_dir']}/simulation_results.json")

    logger.info("Calculating state percentages...")
    percentages = calculate_state_percentages(results, config['before_crisis'])
    plot_state_percentages(percentages, f"{config['output_dir']}/state_percentages.png")

    logger.info("Calculating state volatility...")
    volatility = calculate_state_volatility(results)

    # Generate summary statistics
    logger.info("Generating summary statistics...")
    with open(f"{config['output_dir']}/analysis_summary.txt", 'w') as f:
        f.write("Cognitive Sovereignty Simulation Analysis Summary\n")
        f.write("===============================================\n\n")

        f.write("1. State Percentages\n")
        f.write("-------------------\n")
        for entity, periods in percentages.items():
            f.write(f"\n{entity}:\n")
            for period, states in periods.items():
                f.write(f"  {period.capitalize()} crisis:\n")
                for state, percentage in states.items():
                    f.write(f"    {state}: {percentage:.2f}%\n")

        f.write("\n2. Most Common States\n")
        f.write("---------------------\n")
        for entity, periods in percentages.items():
            f.write(f"\n{entity}:\n")
            for period, states in periods.items():
                most_common = max(states, key=states.get)
                f.write(f"  {period.capitalize()} crisis: {most_common} ({states[most_common]:.2f}%)\n")

        f.write("\n3. State Volatility\n")
        f.write("-------------------\n")
        for entity, vol in volatility.items():
            f.write(f"{entity}: {vol:.2f}\n")

    logger.info(f"Analysis summary saved to {config['output_dir']}/analysis_summary.txt")

if __name__ == "__main__":
    main()
