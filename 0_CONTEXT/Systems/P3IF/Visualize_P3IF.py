import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
import pandas as pd
import numpy as np
import json
import os
from typing import Dict, Any, List
from mpl_toolkits.mplot3d import Axes3D

def load_data(json_path: str) -> Dict[str, Any]:
    """Load data from JSON file."""
    with open(json_path, 'r') as f:
        data = json.load(f)
    print(f"Loaded data keys: {list(data.keys())}")  # Debug print
    return data

def visualize_3d_scatter(data: Dict[str, Any], output_file: str):
    """Create a 3D scatter plot of relationships."""
    if 'relationships' not in data:
        print("Error: 'relationships' key not found in the data. Skipping 3D scatter plot.")
        return

    relationships = pd.DataFrame(data['relationships'])
    patterns = {p['id']: p for p in data['patterns']}

    fig = plt.figure(figsize=(12, 10))
    ax = fig.add_subplot(111, projection='3d')

    properties = {id: p['name'] for id, p in patterns.items() if p['type'] == 'property'}
    processes = {id: p['name'] for id, p in patterns.items() if p['type'] == 'process'}
    perspectives = {id: p['name'] for id, p in patterns.items() if p['type'] == 'perspective'}

    x = relationships['property_id'].map(lambda i: list(properties.keys()).index(i) if i and i in properties else -1)
    y = relationships['process_id'].map(lambda i: list(processes.keys()).index(i) if i and i in processes else -1)
    z = relationships['perspective_id'].map(lambda i: list(perspectives.keys()).index(i) if i and i in perspectives else -1)
    colors = relationships['strength']

    scatter = ax.scatter(x, y, z, c=colors, cmap='viridis', s=50)

    ax.set_xlabel('Properties')
    ax.set_ylabel('Processes')
    ax.set_zlabel('Perspectives')

    ax.set_xticks(range(len(properties)))
    ax.set_yticks(range(len(processes)))
    ax.set_zticks(range(len(perspectives)))

    ax.set_xticklabels(list(properties.values()), rotation=45, ha='right')
    ax.set_yticklabels(list(processes.values()), rotation=45, ha='right')
    ax.set_zticklabels(list(perspectives.values()), rotation=45, ha='right')

    plt.colorbar(scatter, label='Relationship Strength')
    fig.suptitle('3D Scatter Plot of Relationships between Properties, Processes, and Perspectives', fontsize=16, y=0.95)
    fig.subplots_adjust(left=0.2, right=0.8, top=0.85, bottom=0.2)
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.close()

def visualize_network(data: Dict[str, Any], output_file: str):
    """Create a network visualization of relationships."""
    if 'relationships' not in data:
        print("Warning: 'relationships' key not found in the data. Skipping network visualization.")
        return

    relationships = pd.DataFrame(data['relationships'])
    patterns = {p['id']: p for p in data['patterns']}

    G = nx.Graph()
    for _, row in relationships.iterrows():
        prop = patterns[row['property_id']]['name'] if pd.notna(row['property_id']) and row['property_id'] in patterns else 'N/A'
        proc = patterns[row['process_id']]['name'] if pd.notna(row['process_id']) and row['process_id'] in patterns else 'N/A'
        pers = patterns[row['perspective_id']]['name'] if pd.notna(row['perspective_id']) and row['perspective_id'] in patterns else 'N/A'
        G.add_edge(f"P:{prop}", f"Pr:{proc}", weight=row['strength'])
        G.add_edge(f"Pr:{proc}", f"Pe:{pers}", weight=row['strength'])
        G.add_edge(f"Pe:{pers}", f"P:{prop}", weight=row['strength'])

    plt.figure(figsize=(15, 17))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', 
            node_size=500, font_size=8, font_weight='bold')
    edge_weights = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_weights)
    plt.title('Network Visualization of Relationships between Properties, Processes, and Perspectives', fontsize=16, y=1.02)
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.close()

def visualize_strength_distribution(data: Dict[str, Any], output_file: str):
    """Visualize the distribution of relationship strengths."""
    if 'relationships' not in data:
        print("Warning: 'relationships' key not found in the data. Skipping strength distribution visualization.")
        return

    relationships = pd.DataFrame(data['relationships'])
    plt.figure(figsize=(10, 8))
    sns.histplot(relationships['strength'], kde=True)
    plt.title('Distribution of Relationship Strengths across Properties, Processes, and Perspectives', fontsize=16)
    plt.xlabel('Strength')
    plt.ylabel('Count')
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.close()

def visualize_heatmap(data: Dict[str, Any], output_file: str):
    """Create heatmaps of relationship strengths for all combinations of dimensions."""
    if 'relationships' not in data:
        print("Warning: 'relationships' key not found in the data. Skipping heatmap visualization.")
        return

    relationships = pd.DataFrame(data['relationships'])
    patterns = {p['id']: p for p in data['patterns']}

    # Create a mapping of IDs to names for each dimension
    property_names = {id: p['name'] for id, p in patterns.items() if p['type'] == 'property'}
    process_names = {id: p['name'] for id, p in patterns.items() if p['type'] == 'process'}
    perspective_names = {id: p['name'] for id, p in patterns.items() if p['type'] == 'perspective'}

    # Replace IDs with names
    relationships['property'] = relationships['property_id'].map(property_names)
    relationships['process'] = relationships['process_id'].map(process_names)
    relationships['perspective'] = relationships['perspective_id'].map(perspective_names)

    # Create pivot tables for each combination
    pivot_tables = {
        'Property vs Process': relationships.pivot_table(values='strength', index='property', columns='process', aggfunc='mean'),
        'Property vs Perspective': relationships.pivot_table(values='strength', index='property', columns='perspective', aggfunc='mean'),
        'Process vs Perspective': relationships.pivot_table(values='strength', index='process', columns='perspective', aggfunc='mean')
    }

    # Create a figure with constrained layout
    fig, axs = plt.subplots(3, 1, figsize=(12, 26), constrained_layout=True)

    # Plot heatmaps
    for ax, (title, pivot_table) in zip(axs, pivot_tables.items()):
        if pivot_table.empty:
            print(f"Warning: Pivot table for {title} is empty. Skipping heatmap visualization.")
            continue
        sns.heatmap(pivot_table, annot=False, cmap='YlOrRd', ax=ax)
        ax.set_title(f'Heatmap of Relationship Strengths: {title}')
        ax.set_xlabel(title.split(' vs ')[1])
        ax.set_ylabel(title.split(' vs ')[0])

    # Save the figure
    fig.suptitle('Heatmaps of Relationship Strengths', fontsize=16, y=0.95)
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.close()

def visualize_dimension_comparison(data: Dict[str, Any], output_file: str):
    """Create a multi-subplot comparison of dimensions."""
    if 'relationships' not in data:
        print("Warning: 'relationships' key not found in the data. Skipping dimension comparison visualization.")
        return

    relationships = pd.DataFrame(data['relationships'])
    patterns = {p['id']: p for p in data['patterns']}

    fig, axs = plt.subplots(2, 2, figsize=(20, 22), constrained_layout=True)
    fig.suptitle('Multi-dimensional Comparison of Properties, Processes, and Perspectives', fontsize=16, y=0.95)

    # Property vs Process
    axs[0, 0].scatter(relationships['property_id'], relationships['process_id'], 
                      c=relationships['strength'], cmap='viridis')
    axs[0, 0].set_xlabel('Properties')
    axs[0, 0].set_ylabel('Processes')
    axs[0, 0].set_title('Property vs Process')

    # Property vs Perspective
    axs[0, 1].scatter(relationships['property_id'], relationships['perspective_id'], 
                      c=relationships['strength'], cmap='viridis')
    axs[0, 1].set_xlabel('Properties')
    axs[0, 1].set_ylabel('Perspectives')
    axs[0, 1].set_title('Property vs Perspective')

    # Process vs Perspective
    axs[1, 0].scatter(relationships['process_id'], relationships['perspective_id'], 
                      c=relationships['strength'], cmap='viridis')
    axs[1, 0].set_xlabel('Processes')
    axs[1, 0].set_ylabel('Perspectives')
    axs[1, 0].set_title('Process vs Perspective')

    # Strength Distribution
    sns.histplot(relationships['strength'], kde=True, ax=axs[1, 1])
    axs[1, 1].set_title('Strength Distribution')

    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.close()

def process_domain(json_file: str):
    """Process a single domain JSON file and create visualizations."""
    data = load_data(json_file)
    domain_name = os.path.splitext(os.path.basename(json_file))[0]
    output_dir = f"P3IF_export/visualizations/{domain_name}"
    os.makedirs(output_dir, exist_ok=True)

    visualize_3d_scatter(data, f"{output_dir}/3d_scatter.png")
    visualize_network(data, f"{output_dir}/network.png")
    visualize_strength_distribution(data, f"{output_dir}/strength_dist.png")
    visualize_heatmap(data, f"{output_dir}/heatmap.png")
    visualize_dimension_comparison(data, f"{output_dir}/dimension_comparison.png")

def process_all_domains(export_dir: str):
    """Process all JSON files in the export directory."""
    for json_file in os.listdir(export_dir):
        if json_file.endswith('.json'):
            print(f"Processing {json_file}...")
            process_domain(os.path.join(export_dir, json_file))

if __name__ == "__main__":
    export_dir = "P3IF_export"
    process_all_domains(export_dir)
    print("All domains processed.")