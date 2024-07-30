import json
import os
import pandas as pd
import matplotlib.pyplot as plt
from typing import List, Dict
from collections import Counter
from datetime import datetime, timedelta
import networkx as nx

class ThoughtDetailsProcessor:
    def __init__(self, data_directory: str):
        self.data_directory = data_directory
        self.thought_details: List[Dict] = []

    def load_thought_details(self):
        for filename in os.listdir(self.data_directory):
            if filename.startswith("thought_details_") and filename.endswith(".json"):
                with open(os.path.join(self.data_directory, filename), 'r') as file:
                    self.thought_details.append(json.load(file))

    def generate_summary_statistics(self):
        df = pd.DataFrame(self.thought_details)
        
        summary = {
            "Total Thoughts": len(df),
            "Unique Brain IDs": df['brainId'].nunique(),
            "Earliest Creation": df['creationDateTime'].min(),
            "Latest Modification": df['modificationDateTime'].max(),
            "Most Common Kind": df['kind'].mode().iloc[0],
            "Most Common Label": df['label'].mode().iloc[0] if 'label' in df.columns else "N/A"
        }

        print("Summary Statistics:")
        for key, value in summary.items():
            print(f"{key}: {value}")

    def visualize_data(self):
        df = pd.DataFrame(self.thought_details)

        # Thought creation over time
        df['creationDate'] = pd.to_datetime(df['creationDateTime']).dt.date
        thought_creation = df['creationDate'].value_counts().sort_index()
        plt.figure(figsize=(12, 6))
        thought_creation.plot(kind='line')
        plt.title('Thought Creation Over Time')
        plt.xlabel('Date')
        plt.ylabel('Number of Thoughts Created')
        plt.savefig('thought_creation_over_time.png')
        plt.close()

        # Thought kinds distribution
        kind_counts = df['kind'].value_counts()
        plt.figure(figsize=(10, 6))
        kind_counts.plot(kind='bar')
        plt.title('Distribution of Thought Kinds')
        plt.xlabel('Kind')
        plt.ylabel('Count')
        plt.savefig('thought_kinds_distribution.png')
        plt.close()

        # Label word cloud (if 'label' exists)
        if 'label' in df.columns:
            from wordcloud import WordCloud
            labels = ' '.join(df['label'].dropna())
            wordcloud = WordCloud(width=800, height=400, background_color='white').generate(labels)
            plt.figure(figsize=(10, 5))
            plt.imshow(wordcloud, interpolation='bilinear')
            plt.axis('off')
            plt.title('Label Word Cloud')
            plt.savefig('label_word_cloud.png')
            plt.close()

        # Gantt Chart
        self.create_gantt_chart(df)

        # GTD Visualization
        self.create_gtd_visualization(df)

    def create_gantt_chart(self, df):
        # Assuming 'kind' 2 represents tasks and we have 'startDate' and 'endDate' columns
        tasks = df[df['kind'] == 2].sort_values('startDate')
        fig, ax = plt.subplots(figsize=(15, 8))

        for idx, task in tasks.iterrows():
            start_date = pd.to_datetime(task['startDate'])
            end_date = pd.to_datetime(task['endDate'])
            ax.barh(task['name'], (end_date - start_date).days, left=start_date, height=0.5)

        ax.set_yticks(range(len(tasks)))
        ax.set_yticklabels(tasks['name'])
        ax.set_xlabel('Date')
        ax.set_title('Project Gantt Chart')
        plt.tight_layout()
        plt.savefig('gantt_chart.png')
        plt.close()

    def create_gtd_visualization(self, df):
        # Create a graph
        G = nx.DiGraph()

        # Add nodes and edges based on thought relationships
        for thought in self.thought_details:
            G.add_node(thought['id'], name=thought['name'], kind=thought['kind'])
            if 'parentId' in thought:
                G.add_edge(thought['parentId'], thought['id'])

        # Set node colors based on GTD categories
        color_map = []
        for node in G:
            if G.nodes[node]['kind'] == 1:
                color_map.append('lightblue')  # Projects
            elif G.nodes[node]['kind'] == 2:
                color_map.append('lightgreen')  # Next Actions
            elif G.nodes[node]['kind'] == 3:
                color_map.append('yellow')  # Reference
            else:
                color_map.append('lightgray')  # Other

        # Draw the graph
        plt.figure(figsize=(20, 20))
        pos = nx.spring_layout(G)
        nx.draw(G, pos, node_color=color_map, with_labels=True, node_size=3000, font_size=8)
        
        # Add a legend
        legend_elements = [plt.Line2D([0], [0], marker='o', color='w', label='Projects',
                                      markerfacecolor='lightblue', markersize=15),
                           plt.Line2D([0], [0], marker='o', color='w', label='Next Actions',
                                      markerfacecolor='lightgreen', markersize=15),
                           plt.Line2D([0], [0], marker='o', color='w', label='Reference',
                                      markerfacecolor='yellow', markersize=15),
                           plt.Line2D([0], [0], marker='o', color='w', label='Other',
                                      markerfacecolor='lightgray', markersize=15)]
        plt.legend(handles=legend_elements, loc='upper left')

        plt.title('GTD Thought Structure')
        plt.axis('off')
        plt.tight_layout()
        plt.savefig('gtd_visualization.png')
        plt.close()

    def process(self):
        self.load_thought_details()
        self.generate_summary_statistics()
        self.visualize_data()

if __name__ == "__main__":
    processor = ThoughtDetailsProcessor("path/to/your/data/directory")
    processor.process()
