import json
import pandas as pd
import numpy as np
from scipy import stats
from collections import Counter
import networkx as nx
from typing import Dict, Any
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from wordcloud import WordCloud
import os
import sys

def load_data(json_path: str) -> Dict[str, Any]:
    """Load data from JSON file."""
    with open(json_path, 'r') as f:
        data = json.load(f)
    return data

def analyze_p3if_data(data: Dict[str, Any], output_dir: str, filename: str):
    """Comprehensive analysis of P3IF data."""
    
    # Convert relationships to DataFrame
    relationships_df = pd.DataFrame(data['relationships'])
    patterns_df = pd.DataFrame(data['patterns'])

    # Create domain-specific output directory
    domain_output_dir = os.path.join(output_dir, filename)
    os.makedirs(domain_output_dir, exist_ok=True)

    # Redirect stdout to a file
    original_stdout = sys.stdout
    with open(os.path.join(domain_output_dir, f"{filename}_analysis.txt"), 'w') as f:
        sys.stdout = f

        print(f"=== P3IF Data Analysis for {filename} ===\n")

        # Basic statistics
        print("1. Basic Statistics:")
        print(f"Total number of patterns: {len(patterns_df)}")
        print(f"Total number of relationships: {len(relationships_df)}")
        print(f"Number of unique properties: {relationships_df['property_id'].nunique()}")
        print(f"Number of unique processes: {relationships_df['process_id'].nunique()}")
        print(f"Number of unique perspectives: {relationships_df['perspective_id'].nunique()}")

        # Pattern type distribution
        pattern_types = patterns_df['type'].value_counts()
        print("\n2. Pattern Type Distribution:")
        for ptype, count in pattern_types.items():
            print(f"{ptype.capitalize()}: {count} ({count/len(patterns_df)*100:.2f}%)")

        # Visualize pattern type distribution
        plt.figure(figsize=(10, 6))
        pattern_types.plot(kind='bar')
        plt.title(f'Pattern Type Distribution - {filename}')
        plt.xlabel('Pattern Type')
        plt.ylabel('Count')
        plt.savefig(os.path.join(domain_output_dir, f"{filename}_pattern_type_distribution.png"))
        plt.close()

        # Relationship strength analysis
        print("\n3. Relationship Strength Analysis:")
        strength_stats = relationships_df['strength'].describe()
        print(strength_stats)
        
        # Visualize strength distribution
        plt.figure(figsize=(10, 6))
        sns.histplot(relationships_df['strength'], kde=True)
        plt.title(f'Distribution of Relationship Strengths - {filename}')
        plt.xlabel('Strength')
        plt.savefig(os.path.join(domain_output_dir, f"{filename}_strength_distribution.png"))
        plt.close()
        
        # Identify strongest and weakest relationships
        strongest = relationships_df.loc[relationships_df['strength'].idxmax()]
        weakest = relationships_df.loc[relationships_df['strength'].idxmin()]
        strongest_property = patterns_df.loc[patterns_df['id'] == strongest['property_id'], 'name'].values
        if strongest_property.size > 0:
            print(f"\nStrongest relationship (strength = {strongest['strength']:.4f}):")
            print(f"Property: {strongest_property[0]}")
        else:
            print(f"\nStrongest relationship (strength = {strongest['strength']:.4f}):")
            print("Property: Not found")
        
        strongest_process = patterns_df.loc[patterns_df['id'] == strongest['process_id'], 'name'].values
        if strongest_process.size > 0:
            print(f"Process: {strongest_process[0]}")
        else:
            print("Process: Not found")
        
        strongest_perspective = patterns_df.loc[patterns_df['id'] == strongest['perspective_id'], 'name'].values
        if strongest_perspective.size > 0:
            print(f"Perspective: {strongest_perspective[0]}")
        else:
            print("Perspective: Not found")
        
        weakest_property = patterns_df.loc[patterns_df['id'] == weakest['property_id'], 'name'].values
        if weakest_property.size > 0:
            print(f"\nWeakest relationship (strength = {weakest['strength']:.4f}):")
            print(f"Property: {weakest_property[0]}")
        else:
            print(f"\nWeakest relationship (strength = {weakest['strength']:.4f}):")
            print("Property: Not found")
        
        weakest_process = patterns_df.loc[patterns_df['id'] == weakest['process_id'], 'name'].values
        if weakest_process.size > 0:
            print(f"Process: {weakest_process[0]}")
        else:
            print("Process: Not found")
        
        weakest_perspective = patterns_df.loc[patterns_df['id'] == weakest['perspective_id'], 'name'].values
        if weakest_perspective.size > 0:
            print(f"Perspective: {weakest_perspective[0]}")
        else:
            print("Perspective: Not found")

        # Network analysis
        G = nx.Graph()
        for _, row in relationships_df.iterrows():
            if pd.notna(row['property_id']) and pd.notna(row['process_id']) and pd.notna(row['perspective_id']):
                G.add_edge(row['property_id'], row['process_id'], weight=row['strength'])
                G.add_edge(row['process_id'], row['perspective_id'], weight=row['strength'])
                G.add_edge(row['perspective_id'], row['property_id'], weight=row['strength'])

        print("\n4. Network Analysis:")
        print(f"Number of nodes: {G.number_of_nodes()}")
        print(f"Number of edges: {G.number_of_edges()}")

        if G.number_of_nodes() > 0:
            print(f"Average clustering coefficient: {nx.average_clustering(G):.4f}")
        else:
            print("Average clustering coefficient: N/A")

        if G.number_of_nodes() > 0:
            if nx.is_connected(G):
                print(f"Average shortest path length: {nx.average_shortest_path_length(G):.4f}")
                print(f"Diameter of the graph: {nx.diameter(G)}")
            else:
                print("Graph is not connected.")
        else:
            print("Graph is empty, cannot compute connectivity or path lengths.")

        # Centrality measures
        degree_centrality = nx.degree_centrality(G)
        betweenness_centrality = nx.betweenness_centrality(G)
        eigenvector_centrality = None  # Initialize to None
        if G.number_of_nodes() > 0:
            eigenvector_centrality = nx.eigenvector_centrality(G)
        else:
            print("Graph is empty, cannot compute centrality.")
        closeness_centrality = nx.closeness_centrality(G)

        print("\n5. Top 5 Patterns by Centrality Measures:")
        centrality_measures = {
            "Degree Centrality": degree_centrality,
            "Betweenness Centrality": betweenness_centrality,
            "Eigenvector Centrality": eigenvector_centrality,
            "Closeness Centrality": closeness_centrality
        }

        for measure_name, centrality in centrality_measures.items():
            print(f"\n{measure_name}:")
            if centrality is not None:
                for node, value in sorted(centrality.items(), key=lambda x: x[1], reverse=True)[:5]:
                    print(f"{patterns_df.loc[patterns_df['id'] == node, 'name'].values[0]}: {value:.4f}")
            else:
                print("Centrality measure not available.")

        # Correlation analysis
        print("\n6. Correlation Analysis:")
        property_strengths = relationships_df.groupby('property_id')['strength'].mean()
        process_strengths = relationships_df.groupby('process_id')['strength'].mean()
        perspective_strengths = relationships_df.groupby('perspective_id')['strength'].mean()

        correlation_matrix = pd.DataFrame({
            'Property': property_strengths,
            'Process': process_strengths,
            'Perspective': perspective_strengths
        }).corr()

        print("Correlation matrix of average strengths:")
        print(correlation_matrix)

        # Visualize correlation matrix
        plt.figure(figsize=(10, 8))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
        plt.title(f'Correlation Matrix of Average Strengths - {filename}')
        plt.savefig(os.path.join(domain_output_dir, f"{filename}_correlation_matrix.png"))
        plt.close()

        # Pattern name analysis
        print("\n7. Pattern Name Analysis:")
        all_words = ' '.join(patterns_df['name']).lower().split()
        word_freq = Counter(all_words)
        print("Top 10 most common words in pattern names:")
        for word, count in word_freq.most_common(10):
            print(f"{word}: {count}")

        # Generate and save word cloud
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_freq)
        plt.figure(figsize=(10, 5))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title(f'Word Cloud of Pattern Names - {filename}')
        plt.savefig(os.path.join(domain_output_dir, f"{filename}_pattern_name_wordcloud.png"))
        plt.close()

        # Cluster analysis
        print("\n8. Cluster Analysis:")
        X = relationships_df[['strength']].values
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        # Determine optimal number of clusters using elbow method
        inertias = []
        for k in range(1, 11):
            kmeans = KMeans(n_clusters=k, random_state=42)
            kmeans.fit(X_scaled)
            inertias.append(kmeans.inertia_)

        # Plot elbow curve
        plt.figure(figsize=(10, 6))
        plt.plot(range(1, 11), inertias, marker='o')
        plt.xlabel('Number of clusters (k)')
        plt.ylabel('Inertia')
        plt.title(f'Elbow Method for Optimal k - {filename}')
        plt.savefig(os.path.join(domain_output_dir, f"{filename}_elbow_curve.png"))
        plt.close()

        # Perform k-means clustering with optimal k
        optimal_k = 3  # This should be determined by analyzing the elbow curve
        kmeans = KMeans(n_clusters=optimal_k, random_state=42)
        relationships_df['cluster'] = kmeans.fit_predict(X_scaled)

        print(f"Performed k-means clustering with {optimal_k} clusters.")
        print("Cluster sizes:")
        print(relationships_df['cluster'].value_counts())

        # Visualize clusters
        if not relationships_df.empty:
            plt.figure(figsize=(10, 6))
            sns.scatterplot(data=relationships_df, x='property_id', y='process_id', hue='cluster', palette='deep')
            plt.title(f'Clusters of Relationships - {filename}')
            plt.xlabel('Property ID')
            plt.ylabel('Process ID')
            plt.savefig(os.path.join(domain_output_dir, f"{filename}_relationship_clusters.png"))
            plt.close()
        else:
            print("No relationships found, cannot visualize clusters.")

    # Reset stdout
    sys.stdout = original_stdout

if __name__ == "__main__":
    input_dir = "P3IF_export"
    output_dir = os.path.join(input_dir, "visualizations")
    os.makedirs(output_dir, exist_ok=True)

    for filename in os.listdir(input_dir):
        if filename.endswith(".json"):
            json_path = os.path.join(input_dir, filename)
            data = load_data(json_path)
            analyze_p3if_data(data, output_dir, os.path.splitext(filename)[0])