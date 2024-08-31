import os
import json
import logging
import matplotlib.pyplot as plt
from collections import Counter
from typing import Dict, List, Tuple
from Blake_Entity_Extraction_Simple import compile_entities
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk import pos_tag

# Configure logging
log_dir = 'Analysis'
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, 'blake_analysis.log')
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[
    logging.FileHandler(log_file),
    logging.StreamHandler()
])

def load_entities(filename: str = 'Blake_Entity.json') -> Dict[str, int]:
    logging.info(f"Loading entities from {filename}")
    try:
        with open(filename, 'r', encoding='utf-8') as json_file:
            entities = json.load(json_file)
        logging.info(f"Successfully loaded {len(entities)} entities from {filename}")
        return entities
    except Exception as e:
        logging.error(f"Error loading from {filename}: {str(e)}")
        return {}

def analyze_entity_frequencies(entities: Dict[str, int]) -> List[Tuple[str, int]]:
    logging.info("Analyzing entity frequencies")
    sorted_entities = sorted(entities.items(), key=lambda x: x[1], reverse=True)
    for entity, count in sorted_entities:
        logging.info(f"Entity: {entity}, Count: {count}")
    return sorted_entities

def find_entities_by_threshold(entities: Dict[str, int], threshold: int, comparison: str) -> Dict[str, int]:
    logging.info(f"Finding entities with {comparison} threshold of {threshold}")
    filtered_entities = {entity: count for entity, count in entities.items() 
                         if (count >= threshold if comparison == 'above' else count <= threshold)}
    logging.info(f"Found {len(filtered_entities)} entities")
    return filtered_entities

def analyze_entities_by_resource(resources_dir: str = 'William_Blake_Resources') -> Dict[str, Dict[str, int]]:
    resource_analysis = {}
    logging.info(f"Analyzing entities by resource in {resources_dir}")

    for root, _, files in os.walk(resources_dir):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    text = f.read()
                entities = compile_entities(text)
                resource_analysis[file] = entities
            except Exception as e:
                logging.error(f"Error processing file {file_path}: {str(e)}")

    logging.info(f"Completed analysis by resource")
    return resource_analysis

def analyze_texts_by_resource(resources_dir: str = 'William_Blake_Resources') -> Dict[str, Dict[str, any]]:
    resources_dir = 'William_Blake_Resources'
    text_analysis = {}
    logging.info(f"Analyzing texts by resource in {resources_dir}")

    for root, dirs, files in os.walk(resources_dir):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                text = f.read()
                tokens = word_tokenize(text)
                tokens = [word for word in tokens if word.isalpha()]
                stop_words = set(stopwords.words('english'))
                filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
                freq_dist = FreqDist(filtered_tokens)
                pos_tags = pos_tag(filtered_tokens)
                text_analysis[file] = {
                    'word_count': len(tokens),
                    'unique_words': len(set(tokens)),
                    'most_common_words': freq_dist.most_common(10),
                    'pos_tags': pos_tags
                }

    logging.info(f"Completed text analysis by resource")
    return text_analysis

def save_summary_statistics(entities: Dict[str, int], common_entities: Dict[str, int], rare_entities: Dict[str, int]):
    summary_file = os.path.join(log_dir, 'summary_statistics.json')
    summary_data = {
        'total_entities': len(entities),
        'common_entities': len(common_entities),
        'rare_entities': len(rare_entities)
    }
    with open(summary_file, 'w', encoding='utf-8') as f:
        json.dump(summary_data, f, indent=4)
    logging.info(f"Summary statistics saved to {summary_file}")

def save_visualizations(entities: Dict[str, int]):
    # Pie chart for top 10 entities
    top_entities = dict(Counter(entities).most_common(10))
    plt.figure(figsize=(10, 6))
    plt.pie(top_entities.values(), labels=top_entities.keys(), autopct='%1.1f%%', startangle=140)
    plt.title('Top 10 Entities Distribution')
    pie_chart_file = os.path.join(log_dir, 'top_10_entities_distribution.png')
    plt.savefig(pie_chart_file)
    plt.close()
    logging.info(f"Top 10 entities distribution pie chart saved to {pie_chart_file}")

    # Histogram for entity frequency distribution
    plt.figure(figsize=(10, 6))
    plt.hist(entities.values(), bins=50, edgecolor='black')
    plt.xlabel('Frequency')
    plt.ylabel('Number of Entities')
    plt.title('Entity Frequency Distribution')
    histogram_file = os.path.join(log_dir, 'entity_frequency_histogram.png')
    plt.savefig(histogram_file)
    plt.close()
    logging.info(f"Entity frequency distribution histogram saved to {histogram_file}")

def main():
    logging.info("Starting William Blake entity analysis process")
    try:
        entities = load_entities()
        analyze_entity_frequencies(entities)
        common_entities = find_entities_by_threshold(entities, 5, 'above')
        rare_entities = find_entities_by_threshold(entities, 1, 'below')
        resource_analysis = analyze_entities_by_resource()
        text_analysis = analyze_texts_by_resource()
        save_summary_statistics(entities, common_entities, rare_entities)
        save_visualizations(entities)
        logging.info("Entity analysis process completed successfully")
    except Exception as e:
        logging.error(f"Error in entity analysis process: {str(e)}")

if __name__ == "__main__":
    main()
