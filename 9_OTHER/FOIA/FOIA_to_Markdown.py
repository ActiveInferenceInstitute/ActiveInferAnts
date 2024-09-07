import json
import os
import logging
import xml.etree.ElementTree as ET
from collections import defaultdict

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def read_json_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except json.JSONDecodeError as e:
        logging.error(f"Error decoding JSON in file {file_path}: {str(e)}")
        return None
    except Exception as e:
        logging.error(f"Error reading file {file_path}: {str(e)}")
        return None

def parse_xml_string(xml_string):
    try:
        root = ET.fromstring(xml_string)
        return xml_to_dict(root)
    except ET.ParseError as e:
        logging.error(f"Error parsing XML: {str(e)}")
        return None
    except TypeError:
        # If xml_string is not a string (e.g., it's already a dict), return it as is
        return xml_string

def xml_to_dict(element):
    result = {}
    for child in element:
        child_data = xml_to_dict(child) if len(child) > 0 else child.text
        if child.tag in result:
            if isinstance(result[child.tag], list):
                result[child.tag].append(child_data)
            else:
                result[child.tag] = [result[child.tag], child_data]
        else:
            result[child.tag] = child_data
    return result

def dict_to_markdown(data, indent=0):
    md_content = ""
    if isinstance(data, dict):
        for key, value in data.items():
            md_content += "  " * indent + f"- **{key}**:"
            if isinstance(value, dict):
                md_content += "\n" + dict_to_markdown(value, indent + 1)
            elif isinstance(value, list):
                md_content += "\n"
                for item in value:
                    if isinstance(item, dict):
                        md_content += "  " * (indent + 1) + "- " + dict_to_markdown(item, indent + 2).lstrip()
                    else:
                        md_content += "  " * (indent + 1) + f"- {item}\n"
            else:
                md_content += f" {value}\n"
    elif isinstance(data, str):
        md_content += "  " * indent + data + "\n"
    return md_content

def generate_markdown(content, file_path):
    md_content = f"# Content of {os.path.basename(file_path)}\n\n"
    md_content += f"**File Path:** {file_path}\n\n"
    md_content += "## Content:\n\n"

    if isinstance(content, str):
        parsed_content = parse_xml_string(content)
    else:
        parsed_content = content

    if parsed_content:
        md_content += dict_to_markdown(parsed_content)
    else:
        md_content += f"```\n{str(content)[:1000]}...\n```\n"  # Show first 1000 characters if parsing fails

    return md_content

def process_files(input_dir, output_dir):
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.endswith(".json"):
                input_file_path = os.path.join(root, file)
                relative_path = os.path.relpath(input_file_path, input_dir)
                output_file_path = os.path.join(output_dir, os.path.splitext(relative_path)[0] + ".md")

                content = read_json_file(input_file_path)
                if content is not None:
                    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
                    markdown_content = generate_markdown(content, input_file_path)
                    with open(output_file_path, "w", encoding='utf-8') as md_file:
                        md_file.write(markdown_content)
                    logging.info(f"Processed {input_file_path} and saved Markdown to {output_file_path}")

def main():
    input_directory = "./FOIA_Responses"
    output_directory = "./FOIA_Markdown"
    process_files(input_directory, output_directory)
    logging.info("Processing complete. Markdown files have been created.")

if __name__ == "__main__":
    main()