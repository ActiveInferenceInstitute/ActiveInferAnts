import os
import csv
import random
import json
from datetime import datetime, timezone

# Ensure the output folder exists
OUTPUT_FOLDER = "LegalData"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Load domains from JSON file
with open('3R_Domains.json', 'r') as f:
    domains = json.load(f)

# List of chosen domains (Education section)
CHOSEN_DOMAINS = ['Education', 'Hospitality', 'Environmental Monitoring', 'Chess Game']

def generate_synthetic_data(num_records: int) -> list:
    # Generates a synthetic dataset based on domains from JSON file.
    #
    # Parameters:
    # - num_records (int): The number of synthetic records to generate.
    #
    # Returns:
    # - list: A list of dictionaries representing the synthetic dataset.
    synthetic_data = []
    for _ in range(num_records):
        domain = random.choice(CHOSEN_DOMAINS)
        example = random.choice(domains[domain])
        example["UTC Timestamp"] = datetime.now(timezone.utc).isoformat()
        example["Recognizing Party"] = f"Party_{random.randint(1, 100)}"
        example["Remembering Party"] = f"Party_{random.randint(1, 100)}"
        example["Responding Party"] = f"Party_{random.randint(1, 100)}"
        example["Risk Score"] = random.randint(1, 100)
        synthetic_data.append(example)
    return synthetic_data

def save_synthetic_data_to_csv(data: list, file_path: str) -> None:
    # Saves the synthetic dataset to a CSV file.
    #
    # Parameters:
    # - data (list): The synthetic dataset to save.
    # - file_path (str): The path to the CSV file.
    fieldnames = ["Setting", "Sub-domain", "Recognize", "Remember", "Respond", "UTC Timestamp", "Recognizing Party", "Remembering Party", "Responding Party", "Risk Score"]
    with open(file_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    print(f"Synthetic dataset saved to {file_path}")

def main():
    # Main function to generate and save the synthetic dataset.
    num_records = 100  # Number of synthetic examples to generate
    synthetic_dataset = generate_synthetic_data(num_records)
    
    # Print the synthetic dataset to terminal
    for data in synthetic_dataset:
        print(data)
    
    # Save the synthetic dataset to a CSV file
    csv_file_path = os.path.join(OUTPUT_FOLDER, "synthetic_3R_data.csv")
    save_synthetic_data_to_csv(synthetic_dataset, csv_file_path)

if __name__ == "__main__":
    main()
