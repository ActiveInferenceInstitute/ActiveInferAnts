# IMPORT
import json
import os
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
from collections import Counter
from datetime import datetime
from wordcloud import WordCloud

class TheBrainExportAnalyzer:
    def __init__(self, export_directory):
        self.export_directory = export_directory
        self.thoughts = []
        self.links = []
        self.brain_details = None
        self.thought_df = None
        self.link_df = None

    # VERIFY
    def load_and_verify_data(self):
        self._load_raw_data()
        self._convert_to_dataframes()
        self._verify_columns()
        self._print_data_summary()

    def _load_raw_data(self):
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

    def _convert_to_dataframes(self):
        self.thought_df = pd.DataFrame(self.thoughts).applymap(lambda x: x.strip() if isinstance(x, str) else x)
        self.link_df = pd.DataFrame(self.links).applymap(lambda x: x.strip() if isinstance(x, str) else x)

    def _verify_columns(self):
        for df, name in [(self.thought_df, 'thought_df'), (self.link_df, 'link_df')]:
            if 'Kind' not in df.columns:
                df['Kind'] = 'Unknown'
            else:
                df['Kind'] = df['Kind'].fillna('Unknown')

    def _print_data_summary(self):
        print("Columns in thought_df:", self.thought_df.columns.tolist())
        print("Columns in link_df:", self.link_df.columns.tolist())
        print("Sample thought data:", self.thoughts[0] if self.thoughts else "No thoughts found")
        print("\nSample link data:", self.links[0] if self.links else "No links found")
        print(f"\nTotal thoughts: {len(self.thoughts)}")
        print(f"Total links: {len(self.links)}")

    # STATISTICS
    def generate_summary_statistics(self):
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
        
        print("Summary Statistics:")
        for key, value in summary.items():
            print(f"{key}: {value}")

    def analyze_link_patterns(self):
        link_types = self.link_df['Kind'].value_counts()
        print("\nLink Pattern Analysis:")
        print(f"Total unique link types: {len(link_types)}")
        print(f"Most common link type: {link_types.index[0]} (Count: {link_types.iloc[0]})")

    def analyze_thought_depth(self):
        G = nx.Graph()
        for link in self.links:
            G.add_edge(link['ThoughtIdA'], link['ThoughtIdB'])

        try:
            home_thought_id = self.brain_details.get('homeThoughtId')
            if home_thought_id:
                self.depths = nx.single_source_shortest_path_length(G, home_thought_id)
                max_depth = max(self.depths.values())
                avg_depth = sum(self.depths.values()) / len(self.depths)

                print("\nThought Depth Analysis:")
                print(f"Maximum thought depth: {max_depth}")
                print(f"Average thought depth: {avg_depth:.2f}")
            else:
                print("No home thought ID found in brain details")
        except Exception as e:
            print(f"An error occurred while analyzing thought depth: {e}")

    # VISUALIZE
    def visualize_thought_creation_over_time(self):
        if 'creationDateTime' not in self.thought_df.columns:
            print("Warning: 'creationDateTime' column not found. Skipping thought creation visualization.")
            return
    
        thought_df = self.thought_df
        thought_df['creationDate'] = pd.to_datetime(thought_df['creationDateTime']).dt.date
        thought_creation = thought_df['creationDate'].value_counts().sort_index()

        plt.figure(figsize=(12, 6))
        thought_creation.plot(kind='line')
        plt.title('Thought Creation Over Time')
        plt.xlabel('Date')
        plt.ylabel('Number of Thoughts Created')
        plt.savefig('thought_creation_over_time.png')
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
            plt.savefig('thought_types_distribution.png')
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
            plt.savefig('label_word_cloud.png')
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
        pos = nx.spring_layout(G)
        nx.draw(G, pos, node_size=20, node_color='lightblue', with_labels=False)
        
        high_degree_nodes = [node for node, degree in G.degree() if degree > 5]
        label_pos = {node: pos[node] for node in high_degree_nodes}
        nx.draw_networkx_labels(G, label_pos, {node: G.nodes[node].get('name', node) for node in high_degree_nodes}, font_size=8)

        plt.title('Thought Network Visualization')
        plt.axis('off')
        plt.tight_layout()
        plt.savefig('thought_network.png', dpi=300)
        plt.close()

    def visualize_link_types(self):
        link_types = self.link_df['Kind'].value_counts()
        plt.figure(figsize=(10, 6))
        link_types.plot(kind='bar')
        plt.title('Distribution of Link Types')
        plt.xlabel('Link Type')
        plt.ylabel('Count')
        plt.savefig('link_types_distribution.png')
        plt.close()

    def visualize_thought_depths(self):
        if hasattr(self, 'depths'):
            max_depth = max(self.depths.values())
            plt.figure(figsize=(10, 6))
            plt.hist(self.depths.values(), bins=range(max_depth + 2), align='left')
            plt.title('Distribution of Thought Depths')
            plt.xlabel('Depth')
            plt.ylabel('Count')
            plt.savefig('thought_depth_distribution.png')
            plt.close()

    def run_analysis(self):
        self.load_and_verify_data()
        self.generate_summary_statistics()
        self.analyze_link_patterns()
        self.analyze_thought_depth()
        self.visualize_thought_creation_over_time()
        self.visualize_thought_types_distribution()
        self.generate_label_word_cloud()
        self.visualize_thought_network()
        self.visualize_link_types()
        self.visualize_thought_depths()

if __name__ == "__main__":
    analyzer = TheBrainExportAnalyzer("TheBrain_export/")
    analyzer.run_analysis()