import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx
import numpy as np
from collections import defaultdict
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def read_domain_analysis(file_path):
    logging.info(f"Reading domain analysis from {file_path}")
    with open(file_path, 'r') as file:
        content = file.read()
    
    sections = content.split('\n\n')
    data = {}
    
    logging.info("Parsing Basic Statistics")
    # Basic Statistics
    basic_stats = sections[1].split('\n')[1:]
    for line in basic_stats:
        key, value = line.split(': ')
        data[key] = int(value)
    
    logging.info("Parsing Pattern Type Distribution")
    # Pattern Type Distribution
    pattern_dist = sections[2].split('\n')[1:]
    for line in pattern_dist:
        pattern_type, count = line.split(': ')
        count, percentage = count.split(' ')
        data[f"{pattern_type}_count"] = int(count)
        data[f"{pattern_type}_percentage"] = float(percentage.strip('()%'))
    
    logging.info("Parsing Relationship Strength Analysis")
    # Relationship Strength Analysis
    strength_stats = sections[3].split('\n')[2:-2]
    for line in strength_stats:
        key, value = line.split()
        data[f"strength_{key}"] = float(value)
    
    logging.info("Parsing Network Analysis")
    # Network Analysis
    network_stats = sections[4].split('\n')[1:]
    for line in network_stats:
        if ':' in line:
            key, value = line.split(': ')
            if value != 'N/A':
                try:
                    data[key] = float(value) if '.' in value else int(value)
                except ValueError:
                    # Handle non-numeric values
                    data[key] = value  # Store as string if not numeric
    
    logging.info("Finished parsing domain analysis")
    return data

def meta_analysis_p3if():
    logging.info("Starting meta-analysis for P3IF")
    base_path = 'P3IF_export/visualizations'
    domains = [d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d)) and d.startswith('p3if_export_')]
    
    all_data = {}
    for domain in domains:
        file_path = os.path.join(base_path, domain, f'{domain}_analysis.txt')
        if os.path.exists(file_path):
            logging.info(f"Processing domain: {domain}")
            all_data[domain] = read_domain_analysis(file_path)
    
    logging.info("Converting data to DataFrame")
    # Convert to DataFrame
    df = pd.DataFrame.from_dict(all_data, orient='index')
    
    logging.info("Starting visualizations")
    # Visualizations
    fig, axes = plt.subplots(4, 2, figsize=(20, 30))
    
    logging.info("Creating Pattern Type Distribution heatmap")
    # 1. Pattern Type Distribution across domains
    pattern_types = ['Property', 'Process', 'Perspective']
    pattern_data = df[[f"{pt}_percentage" for pt in pattern_types]]
    pattern_data.columns = pattern_types
    
    sns.heatmap(pattern_data, annot=True, cmap='YlGnBu', fmt='.1f', ax=axes[0, 0])
    axes[0, 0].set_title('Pattern Type Distribution Across Domains', fontsize=16, fontweight='bold')
    axes[0, 0].set_xlabel('Pattern Types', fontsize=12)
    axes[0, 0].set_ylabel('Domains', fontsize=12)
    cbar = axes[0, 0].collections[0].colorbar
    cbar.set_label('Percentage (%)', fontsize=12)
    
    logging.info("Creating Relationship Strength Statistics violin plot")
    # 2. Relationship Strength Statistics
    strength_cols = [col for col in df.columns if col.startswith('strength_')]
    strength_data = df[strength_cols]
    
    sns.violinplot(data=strength_data, ax=axes[0, 1])
    axes[0, 1].set_title('Relationship Strength Statistics Across Domains', fontsize=16, fontweight='bold')
    axes[0, 1].set_xlabel('Strength Metrics', fontsize=12)
    axes[0, 1].set_ylabel('Strength Value', fontsize=12)
    axes[0, 1].set_xticklabels(axes[0, 1].get_xticklabels(), rotation=45, ha='right')
    
    logging.info("Creating Domain Comparison boxplot")
    # 3. Domain Comparison boxplot
    metrics = ['Total number of patterns', 'Total number of relationships', 'Number of nodes', 'Number of edges']
    available_metrics = [m for m in metrics if m in df.columns]

    if available_metrics:
        df_melt = df[available_metrics].reset_index().melt(id_vars='index', var_name='Metric', value_name='Value')
        sns.boxplot(x='Metric', y='Value', data=df_melt, ax=axes[1, 0])
        axes[1, 0].set_title('Domain Comparison Across Key Metrics', fontsize=16, fontweight='bold')
        axes[1, 0].set_xlabel('Metrics', fontsize=12)
        axes[1, 0].set_ylabel('Value', fontsize=12)
        axes[1, 0].set_xticklabels(axes[1, 0].get_xticklabels(), rotation=45, ha='right')
    else:
        logging.warning("No metrics available for Domain Comparison boxplot")
        axes[1, 0].text(0.5, 0.5, "No data available for comparison", ha='center', va='center', fontsize=14)
    
    logging.info("Creating Total Patterns and Relationships bar plot")
    # 4. Total Patterns and Relationships
    total_data = df[['Total number of patterns', 'Total number of relationships']]
    
    total_data.plot(kind='bar', ax=axes[1, 1])
    axes[1, 1].set_title('Total Patterns and Relationships Across Domains', fontsize=16, fontweight='bold')
    axes[1, 1].set_xlabel('Domains', fontsize=12)
    axes[1, 1].set_ylabel('Count', fontsize=12)
    axes[1, 1].set_xticklabels(axes[1, 1].get_xticklabels(), rotation=45, ha='right')
    axes[1, 1].legend(title='Metric', title_fontsize='12', fontsize='10')
    
    logging.info("Creating Unique Patterns scatter plot")
    # 5. Unique Patterns scatter plot
    unique_patterns = df[['Number of unique properties', 'Number of unique processes', 'Number of unique perspectives']]
    unique_patterns.plot(kind='scatter', x='Number of unique properties', y='Number of unique processes', s=unique_patterns['Number of unique perspectives']*10, alpha=0.7, ax=axes[2, 0])
    axes[2, 0].set_title('Unique Patterns Across Domains', fontsize=16, fontweight='bold')
    axes[2, 0].set_xlabel('Number of Unique Properties', fontsize=12)
    axes[2, 0].set_ylabel('Number of Unique Processes', fontsize=12)
    
    logging.info("Creating Network Metrics bar plot")
    # 6. Network Metrics bar plot
    network_metrics = ['Average clustering coefficient', 'Number of nodes', 'Number of edges']
    available_network_metrics = [m for m in network_metrics if m in df.columns]

    if available_network_metrics:
        network_data = df[available_network_metrics]
        network_data.plot(kind='bar', ax=axes[2, 1])
        axes[2, 1].set_title('Network Metrics Across Domains', fontsize=16, fontweight='bold')
        axes[2, 1].set_xlabel('Domains', fontsize=12)
        axes[2, 1].set_ylabel('Value', fontsize=12)
        axes[2, 1].set_xticklabels(axes[2, 1].get_xticklabels(), rotation=45, ha='right')
        axes[2, 1].legend(title='Metric', title_fontsize='12', fontsize='10')
    else:
        logging.warning("Network metrics not available for some domains")
        axes[2, 1].text(0.5, 0.5, "No data available for network metrics", ha='center', va='center', fontsize=14)
    
    logging.info("Creating Relationship Strength Distribution histogram")
    # 7. Relationship Strength Distribution
    strength_data = df['strength_mean']
    sns.histplot(strength_data, kde=True, ax=axes[3, 0])
    axes[3, 0].set_title('Relationship Strength Distribution Across Domains', fontsize=16, fontweight='bold')
    axes[3, 0].set_xlabel('Mean Strength', fontsize=12)
    axes[3, 0].set_ylabel('Count', fontsize=12)

    logging.info("Creating Unique Patterns stacked bar plot")
    # 8. Unique Patterns stacked bar plot
    unique_patterns_data = df[['Number of unique properties', 'Number of unique processes', 'Number of unique perspectives']]
    unique_patterns_data.plot(kind='bar', stacked=True, ax=axes[3, 1])
    axes[3, 1].set_title('Unique Patterns Across Domains', fontsize=16, fontweight='bold')
    axes[3, 1].set_xlabel('Domains', fontsize=12)
    axes[3, 1].set_ylabel('Count', fontsize=12)
    axes[3, 1].set_xticklabels(axes[3, 1].get_xticklabels(), rotation=45, ha='right')
    axes[3, 1].legend(title='Pattern Type', title_fontsize='12', fontsize='10')

    plt.tight_layout()
    output_path = os.path.join('P3IF_export', 'visualizations', 'P3IF_meta_analysis.png')
    logging.info(f"Saving meta-analysis visualizations to {output_path}")
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"Meta-analysis visualizations saved as '{output_path}'")
    logging.info("Meta-analysis completed successfully")

if __name__ == "__main__":
    logging.info("Starting P3IF meta-analysis script")
    meta_analysis_p3if()
    logging.info("P3IF meta-analysis script completed")