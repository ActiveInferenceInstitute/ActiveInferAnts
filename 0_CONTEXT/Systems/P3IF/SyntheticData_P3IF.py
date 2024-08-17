import json
import random
import os
import logging

# Load the P3IF_Synthetic_Data.json file
with open('P3IF_Synthetic_Data.json', 'r') as f:
    DOMAINS = json.load(f)['DOMAINS']

def generate_synthetic_data(domain_name):
    domain = DOMAINS[domain_name]
    
    # Generate patterns
    patterns = []
    pattern_id = 1
    for item_type in ["property", "process", "perspective"]:
        plural_type = "properties" if item_type == "property" else "perspectives" if item_type == "perspective" else item_type + "es"
        for item in domain[plural_type]:
            pattern = {
                "id": pattern_id,
                "name": item,
                "description": f"Description for {item}",
                "type": item_type
            }
            patterns.append(pattern)
            pattern_id += 1

    # Generate relationships
    relationships = []
    relationship_id = 1
    num_relationships = 100  # Set the number of relationships to match p3if_export.json
    for _ in range(num_relationships):
        property_id = random.choice([p["id"] for p in patterns if p["type"] == "property"] + [None])
        process_id = random.choice([p["id"] for p in patterns if p["type"] == "process"] + [None])
        perspective_id = random.choice([p["id"] for p in patterns if p["type"] == "perspective"] + [None])
        
        # Ensure at least one of property_id, process_id, or perspective_id is not None
        while property_id is None and process_id is None and perspective_id is None:
            property_id = random.choice([p["id"] for p in patterns if p["type"] == "property"] + [None])
            process_id = random.choice([p["id"] for p in patterns if p["type"] == "process"] + [None])
            perspective_id = random.choice([p["id"] for p in patterns if p["type"] == "perspective"] + [None])
        
        relationship = {
            "id": relationship_id,
            "property_id": property_id,
            "process_id": process_id,
            "perspective_id": perspective_id,
            "strength": round(random.uniform(0, 1), 4)
        }
        relationships.append(relationship)
        relationship_id += 1

    # Create the final structure
    data = {
        "patterns": patterns,
        "relationships": relationships
    }

    return data

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    # Ensure the directory exists
    os.makedirs("P3IF_export", exist_ok=True)
    
    for domain in DOMAINS.keys():
        try:
            data = generate_synthetic_data(domain)
            
            # Write the data to a JSON file
            filename = f"P3IF_export/p3if_export_{domain.lower()}.json"
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
            
            logger.info(f"Generated synthetic data for {domain} domain: {filename}")
        except Exception as e:
            logger.error(f"Error generating data for {domain} domain: {str(e)}")

if __name__ == "__main__":
    main()