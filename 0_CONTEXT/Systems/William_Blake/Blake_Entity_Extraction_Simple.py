import os
import json
import re
import logging
from collections import Counter
# Custom words to ignore
CUSTOM_WORDS_TO_IGNORE = [
    "And", "The", "In", "But", "He", "To", "They", "For", "Of", "That", "With", "Then", "His", "It", "She", "If", 
    "When", "All", "My", "As", "On", "What", "This", "Where", "From", "Who", "So", "Is", "We", "Or", "Mr", "Why", 
    "No", "Like", "There", "Into", "Let", "Dear Sir", "How", "Such", "These", "By", "Upon", "Nor", "Till", "You", 
    "Thou", "Thy", "Are", "While", "Which", "Every", "Her", "Over", "Go", "Can", "Ah", "Among", "At", "Their", 
    "Here", "Tho", "Lo", "Your", "Ed", "Not", "Each", "Dagw", "Before", "Thro", "May", "Was", "Come", "Will", 
    "Shall", "Yet", "Our", "Some", "Whose", "Within", "Sir", "And Los", "An", "Give"
]
# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def extract_entities(text):
    logging.info("Extracting entities from text")
    # Regex pattern: Matches capitalized words (single or pairs), including those at line starts
    entities = re.findall(r'(?:^|\s)([A-Z][a-z]+(?:\s[A-Z][a-z]+)?)', text, re.MULTILINE)
    
    # Process entities
    entity_counts = Counter()
    for entity in entities:
        clean_entity = entity.strip()
        if clean_entity not in CUSTOM_WORDS_TO_IGNORE:
            entity_counts[clean_entity] += 1
    
    logging.info(f"Extracted {len(entity_counts)} unique entities")
    return entity_counts

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

def save_to_json(entities, filename='Blake_Entity.json'):
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