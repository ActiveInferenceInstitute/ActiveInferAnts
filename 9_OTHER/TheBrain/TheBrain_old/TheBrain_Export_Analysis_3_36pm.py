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
        
        os.makedirs(self.figures_directory, exist_ok=True)

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

    def verify_import(self) -> None:
        self.logger.info(f"Total thoughts imported: {len(self.thoughts)}")
        self.logger.info(f"Total links imported: {len(self.links)}")
        self.logger.info(f"Columns in thought_df: {self.thought_df.columns.tolist()}")
        self.logger.info(f"Columns in link_df: {self.link_df.columns.tolist()}")
        self.logger.info(f"Sample thought data: {self.thoughts[0] if self.thoughts else 'No thoughts found'}")
        self.logger.info(f"Sample link data: {self.links[0] if self.links else 'No links found'}")

    def print_summary_statistics(self) -> None:
        summary = {
            "Total Thoughts": len(self.thought_df),
            "Total Links": len(self.link_df),
            "Average Links per Thought": len(self.link_df) / len(self.thought_df) if len(self.thought_df) > 0 else 0,
            "Brain Name": self.brain_details['name'] if self.brain_details else "Unknown"
        }
        
        for col in ['creationDateTime', 'modificationDateTime']:
            if col in self.thought_df.columns:
                summary[f"{'Earliest Creation' if col == 'creationDateTime' else 'Latest Modification'}"] = self.thought_df[col].max()
        
        self.logger.info("\nSummary Statistics:")
        for key, value in summary.items():
            self.logger.info(f"{key}: {value}")

    def visualize_data(self) -> None:
        visualization_functions = [
            self.visualize_thought_creation_over_time,
            self.visualize_thought_types_distribution,
            self.generate_label_word_cloud,
            self.visualize_thought_network,
            self.visualize_link_types,
            self.visualize_thought_depths
        ]
        
        # Generate individual visualizations
        for func in visualization_functions:
            fig, ax = plt.subplots(figsize=(10, 8))
            func(ax)
            plt.tight_layout()
            plt.savefig(os.path.join(self.figures_directory, f'{func.__name__}.png'), dpi=300)
            plt.close()
        
        # Generate combined visualization
        fig, axs = plt.subplots(2, 3, figsize=(20, 15))
        for ax, func in zip(axs.flatten(), visualization_functions):
            func(ax)
        
        plt.tight_layout()
        plt.savefig(os.path.join(self.figures_directory, 'combined_visualization.png'), dpi=300)
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
        ax.set_title('Thought Creation Over Time')
        ax.set_xlabel('Date')
        ax.set_ylabel('Number of Thoughts Created')
        ax.tick_params(axis='x', rotation=45)

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
            ax.pie(thought_types.values, labels=thought_types.index, autopct='%1.1f%%', colors=colors, startangle=90)
            ax.set_title('Distribution of Thought Types')
            ax.axis('equal')
        else:
            self.logger.warning("No data available for thought types visualization")

    def generate_label_word_cloud(self, ax: plt.Axes) -> None:
        if 'Name' in self.thought_df.columns:
            names = ' '.join(self.thought_df['Name'].dropna())
            wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='viridis').generate(names)
            
            ax.imshow(wordcloud, interpolation='bilinear')
            ax.axis('off')
            ax.set_title('Thought Names Word Cloud')
        else:
            self.logger.warning("'Name' column not found. Skipping word cloud generation.")

    def visualize_thought_network(self, ax: plt.Axes) -> None:
        G = nx.Graph()
        
        for thought in tqdm(self.thoughts, desc="Adding nodes"):
            G.add_node(thought['Id'], name=thought.get('Name', ''), kind=thought.get('Kind', 'Unknown'))
        
        for link in tqdm(self.links, desc="Adding edges"):
            if 'ThoughtIdA' in link and 'ThoughtIdB' in link:
                G.add_edge(link['ThoughtIdA'], link['ThoughtIdB'])
            else:
                self.logger.warning(f"Skipping link due to missing ID fields: {link}")

        pos = nx.spring_layout(G, k=0.5, iterations=50)
        nx.draw(G, pos, node_size=20, node_color='lightblue', with_labels=False, ax=ax)
        
        high_degree_nodes = [node for node, degree in G.degree() if degree > 5]
        label_pos = {node: pos[node] for node in high_degree_nodes}
        nx.draw_networkx_labels(G, label_pos, {node: G.nodes[node].get('name', node) for node in high_degree_nodes}, font_size=8, ax=ax)

        ax.set_title('Thought Network Visualization')
        ax.axis('off')

    def visualize_link_types(self, ax: plt.Axes) -> None:
        link_types = self.link_df['Kind'].value_counts()
        sns.barplot(x=link_types.index, y=link_types.values, ax=ax)
        ax.set_title('Distribution of Link Types')
        ax.set_xlabel('Link Type')
        ax.set_ylabel('Count')
        ax.tick_params(axis='x', rotation=45)

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
            ax.set_title('Distribution of Thought Depths')
            ax.set_xlabel('Depth')
            ax.set_ylabel('Count')
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
        self.visualize_data()

if __name__ == "__main__":
    analyzer = TheBrainExportAnalyzer("TheBrain_export/")
    analyzer.run_analysis()