import sys
from utils_cognitive_sovereignty import generate_entity, save_entity_library, ensure_output_directory, STATES
import logging
from collections import Counter

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    logger.info("Generating entity library for cognitive sovereignty simulation")
    
    output_dir = "output"
    ensure_output_directory(output_dir)
    
    entities = [
        generate_entity("Government1", "government", 0.07, is_in_power=True),
        generate_entity("Government2", "government", 0.06),
        generate_entity("Government3", "government", 0.07),
        generate_entity("Corporation1", "corporation", 0.08),
        generate_entity("Corporation2", "corporation", 0.07),
        generate_entity("Corporation3", "corporation", 0.08),
        generate_entity("NGO1", "ngo", 0.06),
        generate_entity("NGO2", "ngo", 0.05),
        generate_entity("NGO3", "ngo", 0.06),
        generate_entity("Media1", "media", 0.08),
        generate_entity("Media2", "media", 0.07),
        generate_entity("Media3", "media", 0.08),
        generate_entity("CitizenGroup1", "citizen_group", 0.06),
        generate_entity("CitizenGroup2", "citizen_group", 0.05),
        generate_entity("CitizenGroup3", "citizen_group", 0.06)
    ]
    
    save_entity_library(entities, f"{output_dir}/entity_library.json")
    logger.info("Entity library generation completed successfully")

    # Count entity types
    entity_types = Counter(entity.entity_type for entity in entities)
    
    # Generate output
    logger.info(f"Total entities created: {len(entities)}")
    logger.info(f"Number of entity types: {len(entity_types)}")
    logger.info("Entity types and counts:")
    for entity_type, count in entity_types.items():
        logger.info(f"  - {entity_type}: {count}")
    
    logger.info("List of created entities:")
    for entity in entities:
        power_status = "in power" if entity.is_in_power else "not in power"
        logger.info(f"  - {entity.name} ({entity.entity_type}, {power_status})")
        logger.debug(f"    Current state: {STATES[entity.current_state]}")
        logger.debug(f"    Transition matrix:\n{entity.current_matrix}")

if __name__ == "__main__":
    main()