import os
from dotenv import load_dotenv
from FOIA_utils import save_json_response, get_agency_components, get_specific_component, get_component_request_form, get_annual_report_xml

# Load API key from .env file
load_dotenv()
api_key = os.getenv('FOIA_API_KEY')

def main():
    # Get and save agency components
    components = get_agency_components()
    save_json_response(components, "agency_components")

    # Get and save a specific component (using OIP as an example)
    oip_id = "8216158f-8089-431d-b866-dc334e8d4758"  # Office of Information Policy ID
    oip_info = get_specific_component(oip_id)
    save_json_response(oip_info, "oip_info")

    # Get and save the request form for OIP
    oip_form = get_component_request_form(oip_id)
    save_json_response(oip_form, "oip_request_form")

    # Get and save the annual report XML for DOJ in 2021
    doj_report_2021 = get_annual_report_xml("DOJ", "2021")
    save_json_response({"annual_report": doj_report_2021}, "doj_annual_report_2021")

if __name__ == "__main__":
    main()