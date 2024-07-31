import os
import importlib.util
import logging
from collections import Counter
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import networkx as nx
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.metrics.pairwise import cosine_similarity

class GenerativeResearchMethods:
    def __init__(self, entities_path="../Entities", output_path="../Figures"):
        self.entities_path = entities_path
        self.output_path = output_path
        self.entity_scripts = {}
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info(f"Initialized GenerativeResearchMethods with entities_path: {self.entities_path} and output_path: {self.output_path}")

    def analyze_entities(self):
        """
        Analyze scientific entities and their cognitive models.
        """
        logging.info("Starting analysis of entities.")
        if os.path.exists(self.entities_path):
            logging.debug(f"Entities path exists: {self.entities_path}")
            for entity_folder in os.listdir(self.entities_path):
                entity_folder_path = os.path.join(self.entities_path, entity_folder)
                if os.path.isdir(entity_folder_path):
                    logging.info(f"Analyzing entity folder: {entity_folder}")
                    self._analyze_entity(entity_folder_path, entity_folder)
                else:
                    logging.warning(f"Entity folder path is not a directory: {entity_folder_path}")
        else:
            logging.warning(f"Entities path does not exist: {self.entities_path}")

    def _analyze_entity(self, entity_folder_path, entity_name):
        """
        Analyze an individual entity's cognitive model.
        """
        logging.info(f"Analyzing entity: {entity_name}")
        entity_script = os.path.join(entity_folder_path, f"{entity_name}.py")
        if os.path.exists(entity_script):
            logging.debug(f"Entity script exists: {entity_script}")
            try:
                with open(entity_script, 'r', encoding='utf-8') as f:
                    script_content = f.read()
                    logging.debug(f"Read content from {entity_script}")
                    self.entity_scripts[entity_name] = script_content
                    logging.debug(f"Stored script content for {entity_name}")
            except Exception as e:
                logging.error(f"Error reading {entity_script}: {str(e)}")
        else:
            logging.warning(f"Entity script does not exist: {entity_script}")

    def get_entity_scripts(self):
        """
        Return the concatenated scripts of all entities.
        """
        logging.info("Returning concatenated scripts of all entities.")
        return self.entity_scripts

    def generate_wordclouds(self):
        """
        Generate and save a faceted plot of word clouds for each entity.
        """
        logging.info("Generating word clouds for each entity.")
        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)
            logging.debug(f"Created output path: {self.output_path}")

        stopwords = set(STOPWORDS)
        stopwords.update([
            "True", "False", "None", "self", "import", "from", "class", "def", "return", "if", "else", "try", "except", 
            "with", "as", "for", "in", "os", "logging", "open", "read", "write", "join", "path", "exists", "isdir", 
            "listdir", "debug", "info", "warning", "error", "encoding", "utf-8", "and", "of", "the", "to", "a", "Active", 
            "in", "as", "True", "for", "with", "def"
        ])

        num_entities = len(self.entity_scripts)
        fig, axes = plt.subplots(nrows=(num_entities + 1) // 2, ncols=2, figsize=(16, 8 * ((num_entities + 1) // 2)))
        axes = axes.flatten()

        for ax, (entity_name, script_content) in zip(axes, self.entity_scripts.items()):
            wordcloud = WordCloud(width=800, height=400, background_color='white', stopwords=stopwords).generate(script_content)
            ax.imshow(wordcloud, interpolation='bilinear')
            ax.set_title(entity_name, fontsize=16)
            ax.axis('off')

        for ax in axes[len(self.entity_scripts):]:
            ax.axis('off')

        plt.tight_layout()
        output_file = os.path.join(self.output_path, 'faceted_wordclouds.png')
        plt.savefig(output_file)
        logging.info(f"Saved faceted word clouds to {output_file}")
        plt.close()

    def print_summaries(self):
        """
        Print summaries of the stored scripts, including total number of words and total number of unique words.
        """
        logging.info("Printing summaries of stored scripts.")
        for entity_name, script_content in self.entity_scripts.items():
            words = script_content.split()
            total_words = len(words)
            unique_words = len(set(words))
            logging.info(f"Entity: {entity_name}")
            logging.info(f"Total number of words: {total_words}")
            logging.info(f"Total number of unique words: {unique_words}")
            print(f"Entity: {entity_name}")
            print(f"Total number of words: {total_words}")
            print(f"Total number of unique words: {unique_words}")

    def generate_topic_term_heatmap(self, top_n_words=20):
        """
        Generate a heatmap of the top N words for each entity.
        """
        logging.info(f"Generating topic-term heatmap for top {top_n_words} words.")
        
        # Create a CountVectorizer to get word frequencies
        vectorizer = CountVectorizer(stop_words='english')
        
        # Prepare data for heatmap
        entity_word_freq = {}
        for entity, script in self.entity_scripts.items():
            word_freq = vectorizer.fit_transform([script]).toarray()[0]
            word_freq_dict = dict(zip(vectorizer.get_feature_names_out(), word_freq))
            top_words = sorted(word_freq_dict.items(), key=lambda x: x[1], reverse=True)[:top_n_words]
            entity_word_freq[entity] = {word: freq for word, freq in top_words if word not in STOPWORDS}
        
        # Create a DataFrame from the word frequencies
        df = pd.DataFrame(entity_word_freq).fillna(0)
        
        # Generate heatmap
        plt.figure(figsize=(12, 8))
        sns.heatmap(df, annot=True, cmap='YlOrRd', fmt='g')
        plt.title(f'Top {top_n_words} Words Heatmap Across Entities')
        plt.tight_layout()
        
        # Save the heatmap
        output_file = os.path.join(self.output_path, 'entity_word_heatmap.png')
        plt.savefig(output_file)
        logging.info(f"Saved topic-term heatmap to {output_file}")
        plt.close()

    def generate_comparative_word_usage_plots(self, words_to_compare):
        """
        Create line plots showing how the usage of specific words varies across different entities.
        """
        logging.info(f"Generating comparative word usage plots for words: {words_to_compare}")
        
        word_usage = {word: [] for word in words_to_compare}
        entities = []
        
        for entity, script in self.entity_scripts.items():
            entities.append(entity)
            words = script.split()
            total_words = len(words)
            for word in words_to_compare:
                word_usage[word].append(words.count(word) / total_words * 100)
        
        df = pd.DataFrame(word_usage, index=entities)
        
        plt.figure(figsize=(12, 6))
        df.plot(kind='line', marker='o')
        plt.title('Comparative Word Usage Across Entities')
        plt.xlabel('Entities')
        plt.ylabel('Word Usage (%)')
        plt.legend(title='Words')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        
        output_file = os.path.join(self.output_path, 'comparative_word_usage.png')
        plt.savefig(output_file)
        plt.close()
        logging.info(f"Saved comparative word usage plot to {output_file}")

    def generate_hierarchical_clustering_dendrogram(self):
        """
        Perform hierarchical clustering on the entities based on their word usage and visualize as a dendrogram.
        """
        logging.info("Generating hierarchical clustering dendrogram")
        
        # Create TF-IDF matrix
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(self.entity_scripts.values())
        
        # Perform hierarchical clustering
        linkage_matrix = linkage(tfidf_matrix.toarray(), method='ward')
        
        # Plot dendrogram
        plt.figure(figsize=(12, 8))
        dendrogram(linkage_matrix, labels=list(self.entity_scripts.keys()), leaf_rotation=90)
        plt.title('Hierarchical Clustering of Entities')
        plt.xlabel('Entities')
        plt.ylabel('Distance')
        plt.tight_layout()
        
        output_file = os.path.join(self.output_path, 'entity_clustering_dendrogram.png')
        plt.savefig(output_file)
        plt.close()
        logging.info(f"Saved hierarchical clustering dendrogram to {output_file}")

    def generate_topic_correlation_network(self, threshold=0.3):
        """
        Create a network graph showing correlations between entities based on their shared vocabulary.
        """
        logging.info("Generating topic correlation network")
        
        # Create TF-IDF matrix
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(self.entity_scripts.values())
        
        # Calculate cosine similarity
        cosine_sim = cosine_similarity(tfidf_matrix)
        
        # Create graph
        G = nx.Graph()
        entities = list(self.entity_scripts.keys())
        for i in range(len(entities)):
            for j in range(i+1, len(entities)):
                if cosine_sim[i][j] > threshold:
                    G.add_edge(entities[i], entities[j], weight=cosine_sim[i][j])
        
        # Plot graph
        plt.figure(figsize=(12, 12))
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color='lightblue', 
                node_size=1000, font_size=8, font_weight='bold')
        edge_weights = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_weights)
        plt.title('Topic Correlation Network')
        
        output_file = os.path.join(self.output_path, 'topic_correlation_network.png')
        plt.savefig(output_file)
        plt.close()
        logging.info(f"Saved topic correlation network to {output_file}")

# Usage
if __name__ == "__main__":
    logging.info("Starting GenerativeResearchMethods script.")
    grm = GenerativeResearchMethods()
    grm.analyze_entities()
    grm.generate_wordclouds()
    grm.generate_topic_term_heatmap()
    grm.generate_comparative_word_usage_plots(['important', 'word1', 'word2'])
    grm.generate_hierarchical_clustering_dendrogram()
    grm.generate_topic_correlation_network()
    logging.info("Completed all visualizations.")