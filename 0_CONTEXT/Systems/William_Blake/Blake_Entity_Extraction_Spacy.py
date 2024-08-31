import os
import json
import re
import logging
import spacy
from collections import Counter

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load the English NLP model
nlp = spacy.load("en_core_web_sm")

def extract_entities(text):
    logging.info("Extracting entities from text")
    doc = nlp(text)
    entities = Counter()
    
    # Extract named entities recognized by spaCy
    for ent in doc.ents:
        if ent.label_ in ["PERSON", "ORG", "GPE", "LOC", "WORK_OF_ART"]:
            entities[ent.text] += 1
    
    # Extract capitalized words that might be Blake-specific entities
    for token in doc:
        if token.is_alpha and token.is_title and len(token.text) > 1:
            entities[token.text] += 1
    
    # Custom entities specific to Blake's work
    blake_entities = ["Urizen", "Los", "Orc", "Enitharmon", "Luvah", "Tharmas", "Vala"]
    for entity in blake_entities:
        count = len(re.findall(r'\b' + re.escape(entity) + r'\b', text, re.IGNORECASE))
        if count > 0:
            entities[entity] += count
    
    logging.info(f"Extracted {len(entities)} unique entities")
    return entities

def process_file(file_path):
    logging.info(f"Processing file: {file_path}")
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        entities = extract_entities(content)
        logging.info(f"Processed {file_path}: Found {len(entities)} entities")
        return entities
    except Exception as e:
        logging.error(f"Error processing {file_path}: {str(e)}")
        return Counter()

def compile_entities():
    resources_dir = 'William_Blake_Resources'
    all_entities = Counter()
    logging.info(f"Compiling entities from {resources_dir}")

    for root, dirs, files in os.walk(resources_dir):
        for file in files:
            file_path = os.path.join(root, file)
            entities = process_file(file_path)
            all_entities.update(entities)

    sorted_entities = sorted(all_entities.items(), key=lambda x: x[1], reverse=True)
    logging.info(f"Compiled {len(sorted_entities)} unique entities in total")
    return sorted_entities

def save_to_json(entities, filename='Blake_Entity_Spacy.json'):
    logging.info(f"Saving entities to {filename}")
    try:
        entity_dict = {entity: count for entity, count in entities}
        with open(filename, 'w', encoding='utf-8') as json_file:
            json.dump(entity_dict, json_file, indent=2)
        logging.info(f"Successfully saved {len(entities)} entities to {filename}")
    except Exception as e:
        logging.error(f"Error saving to {filename}: {str(e)}")

if __name__ == "__main__":
    logging.info("Starting William Blake entity extraction process")
    entities = compile_entities()
    save_to_json(entities)
    logging.info("Entity extraction process completed")