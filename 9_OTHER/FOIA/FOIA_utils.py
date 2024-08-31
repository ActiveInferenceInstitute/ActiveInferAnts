import os
import requests
from dotenv import load_dotenv
import json
from datetime import datetime
import logging

# Load API key from .env file
load_dotenv()
api_key = os.getenv('FOIA_API_KEY')

# Base URL for the FOIA API
base_url = "https://api.foia.gov/api"

# Headers for API requests
headers = {
    "X-API-Key": api_key,
    "Content-Type": "application/json"
}

def save_json_response(data, filename_prefix):
    """Save JSON response to a file."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    directory = "FOIA_Responses"
    os.makedirs(directory, exist_ok=True)
    filename = os.path.join(directory, f"{filename_prefix}_{timestamp}.json")
    
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)
    
    print(f"Response saved to file: {filename}")

def get_agency_components():
    """Retrieve a list of agency components."""
    url = f"{base_url}/agency_components"
    params = {
        "fields[agency_component]": "title,abbreviation",
        "include": "agency",
        "fields[agency]": "name,abbreviation"
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()

def get_specific_component(component_id):
    """Retrieve information about a specific agency component."""
    url = f"{base_url}/agency_components/{component_id}"
    response = requests.get(url, headers=headers)
    return response.json()

def get_component_request_form(component_id):
    """Retrieve the FOIA request form for a specific component."""
    url = f"{base_url}/agency_components/{component_id}/request_form"
    response = requests.get(url, headers=headers)
    return response.json()

def get_annual_report_xml(agency_abbr, year):
    """Retrieve the annual report XML for a specific agency and year."""
    url = f"{base_url}/annual-report-xml/{agency_abbr}/{year}"
    response = requests.get(url, headers=headers)
    return response.text  # This returns XML, not JSON

def save_json_response_in_subfolder(response_data, subfolder, filename_prefix):
    # Create the main FOIA_Responses directory if it doesn't exist
    os.makedirs("FOIA_Responses", exist_ok=True)
    
    # Create the agency subfolder if it doesn't exist
    agency_subfolder = os.path.join("FOIA_Responses", subfolder)
    os.makedirs(agency_subfolder, exist_ok=True)
    
    # Convert response_data to JSON string
    json_data = json.dumps(response_data, indent=2)
    
    # Get the total number of characters in the JSON string
    char_count = len(json_data)
    
    # Append the character count to the filename
    filename = f"{filename_prefix}_{char_count}chars_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    
    # Save the response to a file in the subfolder
    file_path = os.path.join(agency_subfolder, filename)
    with open(file_path, "w") as f:
        f.write(json_data)
    
    print(f"Response saved to file: {file_path}")

def setup_logging():
    """Set up logging configuration."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
def fetch_and_save_annual_reports(agencies, start_year, end_year):
    logging.info(f"Fetching annual reports for {len(agencies)} agencies from {start_year} to {end_year}")
    for agency in agencies:
        agency_abbr = agency['abbreviation']
        for year in range(start_year, end_year + 1):
            try:
                xml_data = get_annual_report_xml(agency_abbr, year)
                if xml_data:
                    save_path = os.path.join('data', 'annual_reports', agency_abbr, f"{year}_annual_report.xml")
                    os.makedirs(os.path.dirname(save_path), exist_ok=True)
                    with open(save_path, 'w', encoding='utf-8') as f:
                        f.write(xml_data)
                    logging.info(f"Saved annual report for {agency_abbr} - {year}")
                else:
                    logging.warning(f"No annual report data for {agency_abbr} - {year}")
            except Exception as e:
                logging.error(f"Error fetching annual report for {agency_abbr} - {year}: {str(e)}")
