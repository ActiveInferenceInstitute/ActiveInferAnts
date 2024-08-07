import os
import re
import nltk
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.decomposition import PCA, TruncatedSVD
from sklearn.manifold import TSNE
from wordcloud import WordCloud
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import numpy as np

nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

class GrantPromptMetaAnalysis:
    def __init__(self, prompt_dir='Writing_Outputs/Grant_Prompts/', output_dir='Writing_Outputs/Grant_Prompt_MetaAnalysis/'):
        self.prompt_dir = prompt_dir
        self.output_dir = output_dir
        self.files = self._get_files()
        self.texts = self._read_files()
        self.stop_words = set(stopwords.words('english'))
        self.stop_words.update(['index', 'jsp', 'div', 'True', 'will', 'may'])
        self._ensure_output_dir_exists()

    def _get_files(self):
        return [f for f in os.listdir(self.prompt_dir) if f.endswith('.md')]

    def _read_files(self):
        texts = {}
        for file in self.files:
            with open(os.path.join(self.prompt_dir, file), 'r', encoding='utf-8') as f:
                texts[file] = f.read()
        return texts

    def _ensure_output_dir_exists(self):
        os.makedirs(self.output_dir, exist_ok=True)
        os.makedirs(os.path.join(self.output_dir, 'WordClouds'), exist_ok=True)
        os.makedirs(os.path.join(self.output_dir, 'Clustering'), exist_ok=True)
        os.makedirs(os.path.join(self.output_dir, 'Heatmaps'), exist_ok=True)
        os.makedirs(os.path.join(self.output_dir, 'Projections'), exist_ok=True)

    def _preprocess_text(self, text):
        text = re.sub(r'[^\w\s]', '', text.lower())
        tokens = word_tokenize(text)
        return ' '.join([word for word in tokens if word not in self.stop_words])

    def generate_word_clouds(self):
        for file, text in self.texts.items():
            wordcloud = WordCloud(width=1600, height=800, background_color='white').generate(text)
            plt.figure(figsize=(20, 10))
            plt.imshow(wordcloud, interpolation='bilinear')
            plt.axis('off')
            plt.title(f'Word Cloud for {file}', fontsize=24, pad=20)
            plt.tight_layout(pad=2)
            plt.savefig(os.path.join(self.output_dir, 'WordClouds', f'wordcloud_{file}.png'), dpi=300)
            plt.close()

    def perform_tfidf_analysis(self):
        vectorizer = TfidfVectorizer(stop_words='english')
        tfidf_matrix = vectorizer.fit_transform([self._preprocess_text(text) for text in self.texts.values()])
        feature_names = vectorizer.get_feature_names_out()
        
        df = pd.DataFrame(tfidf_matrix.toarray(), columns=feature_names, index=self.texts.keys())
        df = df[~df.index.duplicated(keep='first')]  # Remove duplicate index values
        top_terms = df.apply(lambda x: x.nlargest(10).index.tolist(), axis=1)
        
        return top_terms, tfidf_matrix

    def cluster_documents(self, n_clusters=3):
        _, tfidf_matrix = self.perform_tfidf_analysis()
        
        # K-means clustering
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        kmeans_labels = kmeans.fit_predict(tfidf_matrix)
        
        # Hierarchical clustering
        hierarchical = AgglomerativeClustering(n_clusters=n_clusters)
        hierarchical_labels = hierarchical.fit_predict(tfidf_matrix.toarray())
        
        # Dimensionality reduction for visualization
        pca = PCA(n_components=2, random_state=42)
        tsne = TSNE(n_components=2, random_state=42, perplexity=5)
        svd = TruncatedSVD(n_components=2, random_state=42)
        
        pca_coords = pca.fit_transform(tfidf_matrix.toarray())
        tsne_coords = tsne.fit_transform(tfidf_matrix.toarray())
        svd_coords = svd.fit_transform(tfidf_matrix)
        
        # Plotting functions
        def plot_clusters(coords, labels, title, filename, method):
            plt.figure(figsize=(16, 12))
            scatter = plt.scatter(coords[:, 0], coords[:, 1], c=labels, cmap='viridis', s=100)
            plt.colorbar(scatter, label='Cluster')
            for i, file in enumerate(self.texts.keys()):
                plt.annotate(file, (coords[i, 0], coords[i, 1]), fontsize=8, alpha=0.7)
            plt.title(title, fontsize=24, pad=20)
            plt.xlabel(f'{method} Component 1', fontsize=14)
            plt.ylabel(f'{method} Component 2', fontsize=14)
            plt.tight_layout(pad=3)
            plt.savefig(os.path.join(self.output_dir, 'Clustering', filename), dpi=300, bbox_inches='tight')
            plt.close()
        
        # Generate plots
        plot_clusters(pca_coords, kmeans_labels, 'K-means Clustering (PCA)', 'kmeans_pca_clustering.png', 'PCA')
        plot_clusters(tsne_coords, kmeans_labels, 'K-means Clustering (t-SNE)', 'kmeans_tsne_clustering.png', 't-SNE')
        plot_clusters(svd_coords, kmeans_labels, 'K-means Clustering (SVD)', 'kmeans_svd_clustering.png', 'SVD')
        plot_clusters(pca_coords, hierarchical_labels, 'Hierarchical Clustering (PCA)', 'hierarchical_pca_clustering.png', 'PCA')
        
        # Silhouette analysis
        from sklearn.metrics import silhouette_score
        silhouette_kmeans = silhouette_score(tfidf_matrix, kmeans_labels)
        silhouette_hierarchical = silhouette_score(tfidf_matrix.toarray(), hierarchical_labels)
        
        print(f"K-means Silhouette Score: {silhouette_kmeans:.4f}")
        print(f"Hierarchical Clustering Silhouette Score: {silhouette_hierarchical:.4f}")

        # Visualization methods for dimensional projections
        self.visualize_projections(pca_coords, 'PCA')

    def visualize_projections(self, coords, method):
        entities = [file.split('_by_')[0] for file in self.files]
        grants = [file.split('_by_')[1].split('.md')[0] for file in self.files]
        catechisms = [file.split('_by_')[2].split('.md')[0] if len(file.split('_by_')) > 2 else 'None' for file in self.files]

        def plot_projection(color_by, title):
            plt.figure(figsize=(16, 12))
            unique_items = list(set(color_by))
            color_map = plt.cm.get_cmap('tab10')
            colors = [color_map(i/len(unique_items)) for i in range(len(unique_items))]
            color_dict = dict(zip(unique_items, colors))
            
            for i, item in enumerate(color_by):
                plt.scatter(coords[i, 0], coords[i, 1], c=[color_dict[item]], s=100, label=item if item not in plt.gca().get_legend_handles_labels()[1] else "")
                plt.annotate(self.files[i], (coords[i, 0], coords[i, 1]), fontsize=8, alpha=0.7)
            
            plt.legend(title=title.split(' by ')[1], loc='center left', bbox_to_anchor=(1, 0.5))
            plt.title(title, fontsize=24, pad=20)
            plt.xlabel(f'{method} Component 1', fontsize=14)
            plt.ylabel(f'{method} Component 2', fontsize=14)
            plt.tight_layout(pad=3)
            plt.savefig(os.path.join(self.output_dir, 'Projections', f'{method}_projection_by_{title.split(" by ")[1]}.png'), dpi=300, bbox_inches='tight')
            plt.close()

        plot_projection(entities, f'{method} Projection by Entity')
        plot_projection(grants, f'{method} Projection by Grant')
        plot_projection(catechisms, f'{method} Projection by Catechism')

    def entity_grant_catechism_analysis(self):
        entities = list(set())
        grants = list(set())
        catechisms = list(set())
        
        for file in self.files:
            parts = file.split('_by_')
            if len(parts) >= 2:
                entities.append(parts[0])
                grants.append(parts[1].split('.md')[0])
                if len(parts) >= 3:
                    catechisms.append(parts[2].split('.md')[0])
        
        print(f"Entities: {entities}")
        print(f"Grants: {grants}")
        print(f"Catechisms: {catechisms}")
        
        # Create a heatmap of entity-grant combinations
        matrix = pd.DataFrame(index=entities, columns=grants, data=0)
        for file in self.files:
            parts = file.split('_by_')
            if len(parts) >= 2:
                entity = parts[0]
                grant = parts[1].split('.md')[0]
                matrix.loc[entity, grant] += 1
        
        plt.figure(figsize=(20, 16))
        sns.heatmap(matrix, annot=True, cmap='YlOrRd', fmt='d', cbar_kws={'label': 'Number of Combinations'})
        plt.title('Entity-Grant Combination Heatmap', fontsize=24, pad=20)
        plt.xlabel('Grants', fontsize=18)
        plt.ylabel('Entities', fontsize=18)
        plt.xticks(rotation=45, ha='right', fontsize=10)
        plt.yticks(rotation=0, fontsize=10)
        plt.tight_layout(pad=3)
        plt.savefig(os.path.join(self.output_dir, 'Heatmaps', 'entity_grant_heatmap.png'), dpi=300, bbox_inches='tight')
        plt.close()

    def run_analysis(self):
        print("Performing TF-IDF analysis...")
        top_terms, _ = self.perform_tfidf_analysis()
        print("Top terms for each document:")
        print(top_terms)
        
        print("Clustering documents...")
        self.cluster_documents()
        
        print("Analyzing entity-grant-catechism combinations...")
        self.entity_grant_catechism_analysis()
        
        print("Generating word clouds...")
        self.generate_word_clouds()

if __name__ == "__main__":
    analyzer = GrantPromptMetaAnalysis()
    analyzer.run_analysis()