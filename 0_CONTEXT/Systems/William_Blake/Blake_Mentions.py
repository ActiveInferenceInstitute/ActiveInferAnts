import re
import os
import logging

# Target terms to search for
TARGET_TERMS = ["System", "Urizen", "Los"]

def extract_term_mentions(input_file, output_dir):
    logging.info(f"Processing file: {input_file}")
    
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    os.makedirs(output_dir, exist_ok=True)

    for term in TARGET_TERMS:
        term_mentions = []
        pattern = rf'\b{term}(s)?\b'
        
        for i, line in enumerate(lines):
            if re.search(pattern, line, re.IGNORECASE):
                start = max(0, i - 3)
                end = min(len(lines), i + 4)
                snippet = ''.join(lines[start:end])
                term_mentions.append(snippet + '\n---\n')

        mention_count = len(term_mentions)
        logging.info(f"Found {mention_count} mentions for '{term}'")

        if term_mentions:
            output_file = os.path.join(output_dir, f'Blake_{term}_Mentions.md')
            with open(output_file, 'w', encoding='utf-8') as f:
                f.writelines(term_mentions)
            logging.info(f"Extracted mentions for '{term}' saved in {output_file}")
        else:
            logging.warning(f"No mentions found for '{term}'")

    # Log the contents of the output directory
    logging.info(f"Contents of {output_dir}:")
    for file in os.listdir(output_dir):
        logging.info(f"- {file}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    
    input_file = './William_Blake_Resources/Blake_Erdman.md'
    output_dir = 'Outputs'
    
    extract_term_mentions(input_file, output_dir)
    
    print("Extraction complete. Results saved in the Outputs directory.")