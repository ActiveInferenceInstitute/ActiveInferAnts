# IMPORT
import json
import os
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
from collections import Counter
from datetime import datetime
from wordcloud import WordCloud
import logging

class TheBrainExportAnalyzer:
    def __init__(self, export_directory):
        self.export_directory = export_directory
        self.thoughts = []
        self.links = []
        self.brain_details = None
        self.thought_df = None
        self.link_df = None
        self.figures_directory = "TheBrain_Figures"
        
        # Create the figures directory if it doesn't exist
        if not os.path.exists(self.figures_directory):
            os.makedirs(self.figures_directory)

        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger(__name__)

    # IMPORT THOUGHTS from thebrain_export folder
    def import_thoughts(self):
        for filename in os.listdir(self.export_directory):
            if filename == "thoughts.json":
                with open(os.path.join(self.export_directory, filename), 'r', encoding='utf-8-sig') as file:
                    self.thoughts = [json.loads(line.strip()) for line in file]
            elif filename == "links.json":
                with open(os.path.join(self.export_directory, filename), 'r', encoding='utf-8-sig') as file:
                    self.links = [json.loads(line) for line in file if line.strip()]
            elif filename == "brain_details.json":
                with open(os.path.join(self.export_directory, filename), 'r', encoding='utf-8-sig') as file:
                    self.brain_details = json.load(file)
    
        if self.brain_details is None:
            self.logger.warning("Brain details file not found. Some features may not work correctly.")
            self.brain_details = {"name": "Unknown", "homeThoughtId": None}
    
        self.thought_df = pd.DataFrame(self.thoughts).applymap(lambda x: x.strip() if isinstance(x, str) else x)
        self.link_df = pd.DataFrame(self.links).applymap(lambda x: x.strip() if isinstance(x, str) else x)

    # VERIFY ALL THOUGHTS ARE IMPORTED
    def verify_import(self):
        print(f"Total thoughts imported: {len(self.thoughts)}")
        print(f"Total links imported: {len(self.links)}")
        print("Columns in thought_df:", self.thought_df.columns.tolist())
        print("Columns in link_df:", self.link_df.columns.tolist())
        print("Sample thought data:", self.thoughts[0] if self.thoughts else "No thoughts found")
        print("\nSample link data:", self.links[0] if self.links else "No links found")

    # PRINT SUMMARY STATISTICS
    def print_summary_statistics(self):
        summary = {
            "Total Thoughts": len(self.thought_df),
            "Total Links": len(self.link_df),
            "Average Links per Thought": len(self.link_df) / len(self.thought_df) if len(self.thought_df) > 0 else 0,
            "Brain Name": self.brain_details['name'] if self.brain_details else "Unknown"
        }
        
        if 'creationDateTime' in self.thought_df.columns:
            summary["Earliest Creation"] = self.thought_df['creationDateTime'].min()
        if 'modificationDateTime' in self.thought_df.columns:
            summary["Latest Modification"] = self.thought_df['modificationDateTime'].max()
        
        print("\nSummary Statistics:")
        for key, value in summary.items():
            print(f"{key}: {value}")

    # VISUALIZE
    def visualize_data(self):
        fig, axs = plt.subplots(2, 3, figsize=(20, 15))
        self.visualize_thought_creation_over_time(axs[0, 0])
        self.visualize_thought_types_distribution(axs[0, 1])
        self.generate_label_word_cloud(axs[0, 2])
        self.visualize_thought_network(axs[1, 0])
        self.visualize_link_types(axs[1, 1])
        self.visualize_thought_depths(axs[1, 2])
        plt.tight_layout()
        plt.savefig(os.path.join(self.figures_directory, 'combined_visualization.png'))
        plt.close()

    def visualize_thought_creation_over_time(self, ax):
        creation_date_column = next((col for col in self.thought_df.columns if col.lower() == 'creationdatetime'), None)
        if not creation_date_column:
            print("Warning: 'CreationDateTime' column not found. Skipping thought creation visualization.")
            return

        thought_df = self.thought_df
        thought_df['creationDate'] = pd.to_datetime(thought_df[creation_date_column]).dt.date
        thought_creation = thought_df['creationDate'].value_counts().sort_index()

        thought_creation.plot(kind='line', ax=ax)
        ax.set_title('Thought Creation Over Time')
        ax.set_xlabel('Date')
        ax.set_ylabel('Number of Thoughts Created')

    def visualize_thought_types_distribution(self, ax):
        thought_type_mapping = {
            1: "Normal",
            2: "Type",
            3: "Event",
             4: "Tag",
            5: "System"
        }

        thought_df = pd.DataFrame([
            {'Kind': thought_type_mapping.get(thought['Kind'], f"Unknown ({thought['Kind']})"), 'Name': thought['Name']}
            for thought in self.thoughts
            if 'Kind' in thought and 'Name' in thought
        ])

        if not thought_df.empty:
            thought_types = thought_df['Kind'].value_counts()
            ax.pie(thought_types.values, labels=thought_types.index, autopct='%1.1f%%')
            ax.set_title('Distribution of Thought Types')
            ax.axis('equal')
        else:
            print("No data available for thought types visualization")

    def generate_label_word_cloud(self, ax):
        if 'label' in self.thought_df.columns:
            labels = ' '.join(self.thought_df['label'].dropna())
            wordcloud = WordCloud(width=800, height=400, background_color='white').generate(labels)
            
            ax.imshow(wordcloud, interpolation='bilinear')
            ax.axis('off')
            ax.set_title('Label Word Cloud')

    def visualize_thought_network(self, ax):
        G = nx.Graph()
        
        for thought in self.thoughts:
            G.add_node(thought['Id'], name=thought.get('Name', ''), kind=thought.get('Kind', 'Unknown'))
        
        for link in self.links:
            if 'ThoughtIdA' in link and 'ThoughtIdB' in link:
                G.add_edge(link['ThoughtIdA'], link['ThoughtIdB'])
            else:
                print(f"Warning: Skipping link due to missing ID fields: {link}")

        pos = nx.spring_layout(G)
        nx.draw(G, pos, node_size=20, node_color='lightblue', with_labels=False, ax=ax)
        
        high_degree_nodes = [node for node, degree in G.degree() if degree > 5]
        label_pos = {node: pos[node] for node in high_degree_nodes}
        nx.draw_networkx_labels(G, label_pos, {node: G.nodes[node].get('name', node) for node in high_degree_nodes}, font_size=8, ax=ax)

        ax.set_title('Thought Network Visualization')
        ax.axis('off')

    def visualize_link_types(self, ax):
        link_types = self.link_df['Kind'].value_counts()
        link_types.plot(kind='bar', ax=ax)
        ax.set_title('Distribution of Link Types')
        ax.set_xlabel('Link Type')
        ax.set_ylabel('Count')

    def visualize_thought_depths(self, ax):
        G = nx.Graph()
        for link in self.links:
            G.add_edge(link['ThoughtIdA'], link['ThoughtIdB'])

        home_thought_id = self.brain_details.get('homeThoughtId')
        if not home_thought_id:
            self.logger.warning("Home thought ID not found. Using the first thought as the starting point.")
            home_thought_id = self.thoughts[0]['Id'] if self.thoughts else None

        if not home_thought_id:
            self.logger.error("No thoughts found. Skipping thought depth visualization.")
            return

        try:
            depths = nx.single_source_shortest_path_length(G, home_thought_id)
            max_depth = max(depths.values())
            ax.hist(list(depths.values()), bins=range(max_depth + 2), align='left')
            ax.set_title('Distribution of Thought Depths')
            ax.set_xlabel('Depth')
            ax.set_ylabel('Count')
            self.logger.info("Thought depth visualization completed successfully.")
        except nx.NetworkXError as e:
            self.logger.error(f"An error occurred while analyzing thought depth: {e}")
            self.logger.error("This may be due to the home thought not being connected to the rest of the network.")
        except Exception as e:
            self.logger.error(f"An unexpected error occurred during thought depth visualization: {e}")

    def get_brain_details(self):
        brain_details_file = os.path.join(self.export_directory, "brain_details.json")
        if os.path.exists(brain_details_file):
            with open(brain_details_file, 'r', encoding='utf-8-sig') as file:
                return json.load(file)
        else:
            self.logger.error(f"Brain details file not found: {brain_details_file}")
            return None

    def run_analysis(self):
        self.import_thoughts()
        self.verify_import()
        self.print_summary_statistics()
        self.visualize_data()

if __name__ == "__main__":
    analyzer = TheBrainExportAnalyzer("TheBrain_export/")
    analyzer.run_analysis()