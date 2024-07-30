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
        
        # Set up logging
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger(__name__)
        
        # Create the figures directory if it doesn't exist
        if not os.path.exists(self.figures_directory):
            os.makedirs(self.figures_directory)
            self.logger.info(f"Created figures directory: {self.figures_directory}")

    # IMPORT THOUGHTS from thebrain_export folder
    def import_thoughts(self):
        self.logger.info(f"Importing thoughts from {self.export_directory}")
        for filename in os.listdir(self.export_directory):
            file_path = os.path.join(self.export_directory, filename)
            try:
                if filename == "thoughts.json":
                    with open(file_path, 'r', encoding='utf-8-sig') as file:
                        self.thoughts = [json.loads(line.strip()) for line in file]
                    self.logger.info(f"Imported {len(self.thoughts)} thoughts")
                elif filename == "links.json":
                    with open(file_path, 'r', encoding='utf-8-sig') as file:
                        self.links = [json.loads(line) for line in file if line.strip()]
                    self.logger.info(f"Imported {len(self.links)} links")
                elif filename == "brain_details.json":
                    with open(file_path, 'r', encoding='utf-8-sig') as file:
                        self.brain_details = json.load(file)
                    self.logger.info("Imported brain details")
            except json.JSONDecodeError as e:
                self.logger.error(f"Error decoding JSON in {filename}: {str(e)}")
            except Exception as e:
                self.logger.error(f"Error importing {filename}: {str(e)}")
        
        self.thought_df = pd.DataFrame(self.thoughts).applymap(lambda x: x.strip() if isinstance(x, str) else x)
        self.link_df = pd.DataFrame(self.links).applymap(lambda x: x.strip() if isinstance(x, str) else x)
        self.logger.info("Created DataFrames for thoughts and links")

    # VERIFY ALL THOUGHTS ARE IMPORTED
    def verify_import(self):
        self.logger.info("=== Import Verification ===")
        self.logger.info(f"Total thoughts imported: {len(self.thoughts)}")
        self.logger.info(f"Total links imported: {len(self.links)}")
        self.logger.info(f"Thought DataFrame columns: {', '.join(self.thought_df.columns.tolist())}")
        self.logger.info(f"Link DataFrame columns: {', '.join(self.link_df.columns.tolist())}")
        self.logger.info(f"Sample thought data: {json.dumps(self.thoughts[0] if self.thoughts else 'No thoughts found', indent=2)}")
        self.logger.info(f"Sample link data: {json.dumps(self.links[0] if self.links else 'No links found', indent=2)}")

    # PRINT SUMMARY STATISTICS
    def print_summary_statistics(self):
        self.logger.info("=== Summary Statistics ===")
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
        
        for key, value in summary.items():
            self.logger.info(f"{key}: {value}")

    # VISUALIZE
    def visualize_data(self):
        self.visualize_thought_creation_over_time()
        self.visualize_thought_types_distribution()
        self.generate_label_word_cloud()
        self.visualize_thought_network()
        self.visualize_link_types()
        self.visualize_thought_depths()

    def visualize_thought_creation_over_time(self):
        creation_date_column = next((col for col in self.thought_df.columns if col.lower() == 'creationdatetime'), None)
        if not creation_date_column:
            print("Warning: 'CreationDateTime' column not found. Skipping thought creation visualization.")
            return

        thought_df = self.thought_df
        thought_df['creationDate'] = pd.to_datetime(thought_df[creation_date_column]).dt.date
        thought_creation = thought_df['creationDate'].value_counts().sort_index()

        plt.figure(figsize=(12, 6))
        thought_creation.plot(kind='line')
        plt.title('Thought Creation Over Time')
        plt.xlabel('Date')
        plt.ylabel('Number of Thoughts Created')
        plt.savefig(os.path.join(self.figures_directory, 'thought_creation_over_time.png'))
        plt.close()

    def visualize_thought_types_distribution(self):
        thought_df = pd.DataFrame([
            {'Kind': thought['Kind'], 'Name': thought['Name']}
            for thought in self.thoughts
            if 'Kind' in thought and 'Name' in thought
        ])

        if not thought_df.empty:
            thought_types = thought_df['Kind'].value_counts()
            plt.figure(figsize=(10, 6))
            plt.pie(thought_types.values, labels=thought_types.index, autopct='%1.1f%%')
            plt.title('Distribution of Thought Types')
            plt.axis('equal')
            plt.savefig(os.path.join(self.figures_directory, 'thought_types_distribution.png'))
            plt.close()
        else:
            print("No data available for thought types visualization")

    def generate_label_word_cloud(self):
        if 'label' in self.thought_df.columns:
            labels = ' '.join(self.thought_df['label'].dropna())
            wordcloud = WordCloud(width=800, height=400, background_color='white').generate(labels)
            
            plt.figure(figsize=(10, 5))
            plt.imshow(wordcloud, interpolation='bilinear')
            plt.axis('off')
            plt.title('Label Word Cloud')
            plt.savefig(os.path.join(self.figures_directory, 'label_word_cloud.png'))
            plt.close()

    def visualize_thought_network(self):
        G = nx.Graph()
        
        for thought in self.thoughts:
            G.add_node(thought['Id'], name=thought.get('Name', ''), kind=thought.get('Kind', 'Unknown'))
        
        for link in self.links:
            if 'ThoughtIdA' in link and 'ThoughtIdB' in link:
                G.add_edge(link['ThoughtIdA'], link['ThoughtIdB'])
            else:
                print(f"Warning: Skipping link due to missing ID fields: {link}")

        plt.figure(figsize=(20, 20))
        pos = nx.spring_layout(G, k=0.5, iterations=50)
        nx.draw(G, pos, node_size=20, node_color='lightblue', with_labels=False)
        
        high_degree_nodes = [node for node, degree in G.degree() if degree > 5]
        label_pos = {node: pos[node] for node in high_degree_nodes}
        nx.draw_networkx_labels(G, label_pos, {node: G.nodes[node].get('name', node) for node in high_degree_nodes}, font_size=8)

        plt.title('Thought Network Visualization')
        plt.axis('off')
        plt.tight_layout(pad=0.1)
        plt.savefig(os.path.join(self.figures_directory, 'thought_network.png'), dpi=300, bbox_inches='tight')
        plt.close()

    def visualize_link_types(self):
        link_types = self.link_df['Kind'].value_counts()
        plt.figure(figsize=(10, 6))
        link_types.plot(kind='bar')
        plt.title('Distribution of Link Types')
        plt.xlabel('Link Type')
        plt.ylabel('Count')
        plt.savefig(os.path.join(self.figures_directory, 'link_types_distribution.png'))
        plt.close()

    def visualize_thought_depths(self):
        G = nx.Graph()
        for link in self.links:
            G.add_edge(link['ThoughtIdA'], link['ThoughtIdB'])

        try:
            if self.brain_details is None:
                print("Warning: Brain details not available. Skipping thought depth visualization.")
                return

            home_thought_id = self.brain_details.get('homeThoughtId')
            if home_thought_id:
                depths = nx.single_source_shortest_path_length(G, home_thought_id)
                max_depth = max(depths.values())
                plt.figure(figsize=(10, 6))
                plt.hist(depths.values(), bins=range(max_depth + 2), align='left')
                plt.title('Distribution of Thought Depths')
                plt.xlabel('Depth')
                plt.ylabel('Count')
                plt.savefig(os.path.join(self.figures_directory, 'thought_depth_distribution.png'))
                plt.close()
            else:
                print("Warning: No home thought ID found in brain details. Skipping thought depth visualization.")
        except Exception as e:
            print(f"An error occurred while analyzing thought depth: {e}")

    def run_analysis(self):
        self.import_thoughts()
        self.verify_import()
        self.print_summary_statistics()
        self.visualize_data()

if __name__ == "__main__":
    analyzer = TheBrainExportAnalyzer("TheBrain_export/")
    analyzer.run_analysis()