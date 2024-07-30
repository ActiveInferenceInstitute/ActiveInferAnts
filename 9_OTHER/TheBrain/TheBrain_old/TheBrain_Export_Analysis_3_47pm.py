import json
import os
from typing import Dict, List, Any, Optional
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
from collections import Counter
from datetime import datetime
import seaborn as sns
from wordcloud import WordCloud
import logging
from tqdm import tqdm

class TheBrainExportAnalyzer:
    def __init__(self, export_directory: str):
        self.export_directory = export_directory
        self.thoughts: List[Dict[str, Any]] = []
        self.links: List[Dict[str, Any]] = []
        self.brain_details: Optional[Dict[str, Any]] = None
        self.thought_df: Optional[pd.DataFrame] = None
        self.link_df: Optional[pd.DataFrame] = None
        self.figures_directory = "TheBrain_Figures"
        self.graph: Optional[nx.Graph] = None
        
        os.makedirs(self.figures_directory, exist_ok=True)

        # Configure logging
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger(__name__)

    def import_thoughts(self) -> None:
        file_mapping = {
            "thoughts.json": ("thoughts", json.loads),
            "links.json": ("links", json.loads),
            "brain_details.json": ("brain_details", json.load)
        }

        for filename, (attr, parse_func) in file_mapping.items():
            file_path = os.path.join(self.export_directory, filename)
            try:
                with open(file_path, 'r', encoding='utf-8-sig') as file:
                    if attr in ["thoughts", "links"]:
                        setattr(self, attr, [parse_func(line.strip()) for line in file if line.strip()])
                    else:
                        setattr(self, attr, parse_func(file))
            except json.JSONDecodeError:
                self.logger.error(f"Error decoding JSON in file: {filename}")
            except Exception as e:
                self.logger.error(f"Error reading file {filename}: {str(e)}")
    
        if self.brain_details is None:
            self.logger.warning("Brain details file not found. Some features may not work correctly.")
            self.brain_details = {"name": "Unknown", "homeThoughtId": None}
    
        self.thought_df = pd.DataFrame(self.thoughts).applymap(lambda x: x.strip() if isinstance(x, str) else x)
        self.link_df = pd.DataFrame(self.links).applymap(lambda x: x.strip() if isinstance(x, str) else x)

        self.logger.info(f"Total thoughts imported: {len(self.thoughts)}")
        self.logger.info(f"Total links imported: {len(self.links)}")

    def verify_import(self) -> None:
        self.logger.info("Import Verification:")
        self.logger.info(f"Columns in thought_df: {', '.join(self.thought_df.columns.tolist())}")
        self.logger.info(f"Columns in link_df: {', '.join(self.link_df.columns.tolist())}")
        self.logger.info(f"Sample thought data: {self.thoughts[0] if self.thoughts else 'No thoughts found'}")
        self.logger.info(f"Sample link data: {self.links[0] if self.links else 'No links found'}")

    def print_summary_statistics(self) -> None:
        self.graph = nx.Graph()
        for link in self.links:
            self.graph.add_edge(link['ThoughtIdA'], link['ThoughtIdB'])

        summary = {
            "Total Thoughts": len(self.thought_df),
            "Total Links": len(self.link_df),
            "Average Links per Thought": len(self.link_df) / len(self.thought_df) if len(self.thought_df) > 0 else 0,
            "Brain Name": self.brain_details['name'] if self.brain_details else "Unknown",
            "Network Density": nx.density(self.graph),
            "Number of Connected Components": nx.number_connected_components(self.graph),
            "Average Clustering Coefficient": nx.average_clustering(self.graph),
        }

        largest_cc = max(nx.connected_components(self.graph), key=len)
        largest_cc_subgraph = self.graph.subgraph(largest_cc)

        summary.update({
            "Network Diameter": nx.diameter(largest_cc_subgraph),
            "Average Shortest Path Length": nx.average_shortest_path_length(largest_cc_subgraph),
        })

        summary.update({
            "Most Central Thought (Degree Centrality)": max(nx.degree_centrality(self.graph), key=nx.degree_centrality(self.graph).get),
            "Most Central Thought (Betweenness Centrality)": max(nx.betweenness_centrality(self.graph), key=nx.betweenness_centrality(self.graph).get),
            "Most Central Thought (Closeness Centrality)": max(nx.closeness_centrality(self.graph), key=nx.closeness_centrality(self.graph).get),
            "Number of Isolated Thoughts": len(list(nx.isolates(self.graph))),
            "Assortativity Coefficient": nx.degree_assortativity_coefficient(self.graph),
        })
        
        for col in ['creationDateTime', 'modificationDateTime']:
            if col in self.thought_df.columns:
                summary[f"{'Earliest Creation' if col == 'creationDateTime' else 'Latest Modification'}"] = self.thought_df[col].max()
        
        thought_types = self.thought_df['Kind'].value_counts()
        for thought_type, count in thought_types.items():
            summary[f"Number of {thought_type} Thoughts"] = count

        link_types = self.link_df['Kind'].value_counts()
        for link_type, count in link_types.items():
            summary[f"Number of {link_type} Links"] = count

        self.logger.info("\nSummary Statistics:")
        for key, value in summary.items():
            self.logger.info(f"{key}: {value}")

        # Additional statistics
        self.logger.info("\nTop 10 Thoughts by Degree:")
        degree_dict = dict(self.graph.degree())
        top_thoughts = sorted(degree_dict, key=degree_dict.get, reverse=True)[:10]
        for thought in top_thoughts:
            thought_name = self.thought_df[self.thought_df['Id'] == thought]['Name'].values[0]
            self.logger.info(f"Thought: {thought_name}, Degree: {degree_dict[thought]}")

        self.logger.info("\nThought Depth Distribution:")
        home_thought_id = self.brain_details.get('homeThoughtId') or (self.thoughts[0]['Id'] if self.thoughts else None)
        if home_thought_id:
            depths = nx.single_source_shortest_path_length(self.graph, home_thought_id)
            depth_distribution = Counter(depths.values())
            for depth, count in sorted(depth_distribution.items()):
                self.logger.info(f"Depth {depth}: {count} thoughts")

        self.logger.info("\nLink Type Distribution:")
        link_type_distribution = self.link_df['Kind'].value_counts()
        for link_type, count in link_type_distribution.items():
            self.logger.info(f"{link_type}: {count}")

    def visualize_data(self) -> None:
        visualization_functions = [
            self.visualize_thought_creation_over_time,
            self.visualize_thought_types_distribution,
            self.generate_label_word_cloud,
            self.visualize_thought_network,
            self.visualize_link_types,
            self.visualize_thought_depths
        ]
        
        for func in visualization_functions:
            fig, ax = plt.subplots(figsize=(12, 9))
            func(ax)
            plt.tight_layout()
            plt.savefig(os.path.join(self.figures_directory, f'{func.__name__}.png'), dpi=300, bbox_inches='tight')
            plt.close()
        
        fig, axs = plt.subplots(2, 3, figsize=(24, 18))
        for ax, func in zip(axs.flatten(), visualization_functions):
            func(ax)
        
        plt.tight_layout()
        plt.savefig(os.path.join(self.figures_directory, 'combined_visualization.png'), dpi=300, bbox_inches='tight')
        plt.close()

    def visualize_thought_creation_over_time(self, ax: plt.Axes) -> None:
        creation_date_column = next((col for col in self.thought_df.columns if col.lower() == 'creationdatetime'), None)
        if not creation_date_column:
            self.logger.warning("'CreationDateTime' column not found. Skipping thought creation visualization.")
            return

        thought_df = self.thought_df.copy()
        thought_df['creationDate'] = pd.to_datetime(thought_df[creation_date_column]).dt.date
        thought_creation = thought_df['creationDate'].value_counts().sort_index()

        sns.lineplot(x=thought_creation.index, y=thought_creation.values, ax=ax)
        ax.set_title('Thought Creation Over Time', fontsize=16)
        ax.set_xlabel('Date', fontsize=12)
        ax.set_ylabel('Number of Thoughts Created', fontsize=12)
        ax.tick_params(axis='x', rotation=45)
        ax.grid(True, linestyle='--', alpha=0.7)

    def visualize_thought_types_distribution(self, ax: plt.Axes) -> None:
        thought_type_mapping = {
            1: "Normal", 2: "Type", 3: "Event", 4: "Tag", 5: "System"
        }

        thought_df = pd.DataFrame([
            {'Kind': thought_type_mapping.get(thought['Kind'], f"Unknown ({thought['Kind']})"), 'Name': thought['Name']}
            for thought in self.thoughts
            if 'Kind' in thought and 'Name' in thought
        ])

        if not thought_df.empty:
            thought_types = thought_df['Kind'].value_counts()
            colors = sns.color_palette('pastel')[:len(thought_types)]
            wedges, texts, autotexts = ax.pie(thought_types.values, labels=thought_types.index, autopct='%1.1f%%', colors=colors, startangle=90)
            ax.set_title('Distribution of Thought Types', fontsize=16)
            ax.axis('equal')
            plt.setp(autotexts, size=10, weight="bold")
            plt.setp(texts, size=12)
            ax.legend(wedges, thought_types.index, title="Thought Types", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
        else:
            self.logger.warning("No data available for thought types visualization")

    def generate_label_word_cloud(self, ax: plt.Axes) -> None:
        if 'Name' in self.thought_df.columns:
            names = ' '.join(self.thought_df['Name'].dropna())
            wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='viridis', max_font_size=100, min_font_size=10).generate(names)
            
            ax.imshow(wordcloud, interpolation='bilinear')
            ax.axis('off')
            ax.set_title('Thought Names Word Cloud', fontsize=16)
        else:
            self.logger.warning("'Name' column not found. Skipping word cloud generation.")

    def visualize_thought_network(self, ax: plt.Axes) -> None:
        G = nx.Graph()
        
        thought_type_mapping = {
            1: "Normal", 2: "Type", 3: "Event", 4: "Tag", 5: "System"
        }
        
        for thought in tqdm(self.thoughts, desc="Adding nodes", leave=False):
            G.add_node(thought['Id'], name=thought.get('Name', ''), kind=thought_type_mapping.get(thought.get('Kind'), 'Unknown'))
        
        for link in tqdm(self.links, desc="Adding edges", leave=False):
            if 'ThoughtIdA' in link and 'ThoughtIdB' in link:
                G.add_edge(link['ThoughtIdA'], link['ThoughtIdB'])
            else:
                self.logger.warning(f"Skipping link due to missing ID fields: {link}")

        pos = nx.spring_layout(G, k=0.5, iterations=50)
        
        node_sizes = [G.degree(node) * 20 for node in G.nodes()]
        node_colors = [G.nodes[node]['kind'] for node in G.nodes()]
        
        color_map = {'Normal': 'lightblue', 'Type': 'lightgreen', 'Event': 'yellow', 'Tag': 'orange', 'System': 'red', 'Unknown': 'gray'}
        node_colors = [color_map[color] for color in node_colors]
        
        nx.draw(G, pos, node_size=node_sizes, node_color=node_colors, with_labels=False, ax=ax)
        
        labels = {node: G.nodes[node].get('name', node) for node in G.nodes()}
        nx.draw_networkx_labels(G, pos, labels, font_size=8, ax=ax)

        ax.set_title('Thought Network Visualization', fontsize=16)
        ax.axis('off')
        
        # Add legend
        legend_elements = [plt.Line2D([0], [0], marker='o', color='w', label=kind,
                          markerfacecolor=color, markersize=10)
                          for kind, color in color_map.items()]
        ax.legend(handles=legend_elements, title="Thought Types", loc="center left", bbox_to_anchor=(1, 0.5))

    def visualize_link_types(self, ax: plt.Axes) -> None:
        link_types = self.link_df['Kind'].value_counts()
        sns.barplot(x=link_types.index, y=link_types.values, ax=ax)
        ax.set_title('Distribution of Link Types', fontsize=16)
        ax.set_xlabel('Link Type', fontsize=12)
        ax.set_ylabel('Count', fontsize=12)
        ax.tick_params(axis='x', rotation=45)
        for i, v in enumerate(link_types.values):
            ax.text(i, v, str(v), ha='center', va='bottom')

    def visualize_thought_depths(self, ax: plt.Axes) -> None:
        G = nx.Graph()
        for link in self.links:
            G.add_edge(link['ThoughtIdA'], link['ThoughtIdB'])

        home_thought_id = self.brain_details.get('homeThoughtId') or (self.thoughts[0]['Id'] if self.thoughts else None)

        if not home_thought_id:
            self.logger.error("No thoughts found. Skipping thought depth visualization.")
            return

        try:
            depths = nx.single_source_shortest_path_length(G, home_thought_id)
            max_depth = max(depths.values())
            sns.histplot(list(depths.values()), bins=range(max_depth + 2), ax=ax, kde=True)
            ax.set_title('Distribution of Thought Depths', fontsize=16)
            ax.set_xlabel('Depth', fontsize=12)
            ax.set_ylabel('Count', fontsize=12)
            ax.grid(True, linestyle='--', alpha=0.7)
            self.logger.info("Thought depth visualization completed successfully.")
        except nx.NetworkXError as e:
            self.logger.error(f"An error occurred while analyzing thought depth: {e}")
            self.logger.error("This may be due to the home thought not being connected to the rest of the network.")
        except Exception as e:
            self.logger.error(f"An unexpected error occurred during thought depth visualization: {e}")

    def get_brain_details(self) -> Optional[Dict[str, Any]]:
        brain_details_file = os.path.join(self.export_directory, "brain_details.json")
        if os.path.exists(brain_details_file):
            with open(brain_details_file, 'r', encoding='utf-8-sig') as file:
                return json.load(file)
        else:
            self.logger.error(f"Brain details file not found: {brain_details_file}")
            return None

    def run_analysis(self) -> None:
        self.import_thoughts()
        self.verify_import()
        self.print_summary_statistics()
        self.logger.info("\nGenerating visualizations...")
        self.visualize_data()
        self.logger.info("Analysis complete. Visualizations saved in the 'TheBrain_Figures' directory.")

if __name__ == "__main__":
    analyzer = TheBrainExportAnalyzer("TheBrain_export/")
    analyzer.run_analysis()