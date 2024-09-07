import os
import json
import logging
from collections import defaultdict

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def analyze_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        
        if isinstance(data, dict):
            if 'annual_report' in data:
                return summarize_annual_report(data['annual_report'])
            elif 'jsonapi' in data and 'data' in data:
                return summarize_api_response(data)
            else:
                return summarize_generic_dict(data)
        elif isinstance(data, str):
            return summarize_string_content(data)
        else:
            return summarize_generic_content(data)
    except json.JSONDecodeError:
        logging.error(f"Invalid JSON in file: {file_path}")
        with open(file_path, 'r') as file:
            return summarize_string_content(file.read())
    except Exception as e:
        logging.error(f"Error processing file {file_path}: {str(e)}")
        return None

def summarize_annual_report(annual_report):
    if isinstance(annual_report, dict):
        return {
            "type": "Annual Report",
            "year": annual_report.get("year", "Unknown"),
            "agency": annual_report.get("agency", "Unknown"),
            "total_requests": annual_report.get("total_requests", 0)
        }
    else:
        return summarize_string_content(str(annual_report))

def summarize_api_response(data):
    return {
        "type": "API Response",
        "api_version": data.get("jsonapi", {}).get("version", "Unknown"),
        "data_count": len(data.get("data", [])),
        "links": bool(data.get("links"))
    }

def summarize_generic_dict(data):
    return {
        "type": "Generic Dictionary",
        "keys": list(data.keys())[:5],  # List first 5 keys
        "total_keys": len(data)
    }

def summarize_string_content(content):
    return {
        "type": "String Content",
        "length": len(content),
        "preview": content[:100] if len(content) > 100 else content
    }

def summarize_generic_content(content):
    return {
        "type": "Generic Content",
        "content_type": str(type(content)),
        "preview": str(content)[:100] if len(str(content)) > 100 else str(content)
    }

def generate_markdown(summary, file_path):
    md_content = f"# Summary for {os.path.basename(file_path)}\n\n"
    md_content += f"**File Path:** {file_path}\n\n"
    md_content += f"**Content Type:** {summary['type']}\n\n"

    if summary['type'] == "Annual Report":
        md_content += f"**Year:** {summary['year']}\n"
        md_content += f"**Agency:** {summary['agency']}\n"
        md_content += f"**Total Requests:** {summary['total_requests']}\n"
    elif summary['type'] == "API Response":
        md_content += f"**API Version:** {summary['api_version']}\n"
        md_content += f"**Data Count:** {summary['data_count']}\n"
        md_content += f"**Has Links:** {summary['links']}\n"
    elif summary['type'] == "Generic Dictionary":
        md_content += f"**Total Keys:** {summary['total_keys']}\n"
        md_content += "**Sample Keys:**\n"
        for key in summary['keys']:
            md_content += f"- {key}\n"
    elif summary['type'] in ["String Content", "Generic Content"]:
        md_content += f"**Content Length:** {summary['length']}\n"
        md_content += f"**Preview:**\n```\n{summary['preview']}\n```\n"

    return md_content

def process_files(input_dir, output_dir):
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.endswith(".json"):
                input_file_path = os.path.join(root, file)
                relative_path = os.path.relpath(input_file_path, input_dir)
                output_file_path = os.path.join(output_dir, os.path.splitext(relative_path)[0] + ".md")

                summary = analyze_json_file(input_file_path)
                if summary:
                    os.makedirs(os.path.dirname(output_file_path), exist_ok=True)
                    markdown_content = generate_markdown(summary, input_file_path)
                    with open(output_file_path, "w") as md_file:
                        md_file.write(markdown_content)
                    logging.info(f"Processed {input_file_path} and saved Markdown to {output_file_path}")

def main():
    input_directory = "./FOIA_Responses"
    output_directory = "./FOIA_Markdown"
    process_files(input_directory, output_directory)
    logging.info("Processing complete. Markdown files have been created.")

if __name__ == "__main__":
    main()