import json
import random

# Load data from P3IF_Synthetic_Data.json
with open('../../../P3IF/P3IF_Synthetic_Data.json', 'r') as file:
    p3if_data = json.load(file)

# Define a function to generate 3R structured data
def generate_3r_data(p3if_data):
    domains = p3if_data['DOMAINS']
    output_data = {}

    for domain, details in domains.items():
        output_data[domain] = []
        properties = details.get('properties', [])
        processes = details.get('processes', [])
        perspectives = details.get('perspectives', [])

        for _ in range(10):  # Generate 10 sample records for each domain
            setting = random.choice(properties) if properties else "N/A"
            sub_domain = domain
            recognize = random.choice(processes) if processes else "N/A"
            remember = random.choice(perspectives) if perspectives else "N/A"
            respond = f"Handle {setting.lower()} with {recognize.lower()} by {remember.lower()}"

            output_data[domain].append({
                "Setting": setting,
                "Sub-domain": sub_domain,
                "Recognize": recognize,
                "Remember": remember,
                "Respond": respond
            })

    return output_data

# Generate the 3R data
generated_data = generate_3r_data(p3if_data)

# Save the generated data to 3R_from_P3IF.json
with open('3R_from_P3IF.json', 'w') as outfile:
    json.dump(generated_data, outfile, indent=4)
