import os
import json
from datetime import datetime
from dotenv import load_dotenv
from FOIA_utils import save_json_response, fetch_and_save_annual_reports, save_json_response_in_subfolder, get_agency_components, get_specific_component, get_component_request_form, get_annual_report_xml
import logging

# Load API key from .env file
load_dotenv()
api_key = os.getenv('FOIA_API_KEY')

# Define the start and end year for fetching annual reports
START_YEAR = 2000 # FOIA was enacted in 1966
END_YEAR = 2025

# List of agencies to iterate over, structured into categories

# Major Departments
major_departments = [
    "DOJ", "DHS", "EPA", "HHS", "DOE", "DOD", "DOS", "DOT", "DOI", "USDA",
    "DOC", "DOL", "ED", "HUD", "VA", "SSA", "TREASURY"
]

# Some smaller agencies or sub-components might have their data included in their parent department's report rather than publishing separate reports.

# Independent Agencies
independent_agencies = [
    "NASA", "NSF", "NARA", "CIA", "ODNI", "USPS", "FCC", "SEC", "FTC", "FDA",
    "NIH", "CDC", "FEMA", "IRS", "NOAA", "USGS", "NPS", "FBI", "DEA", "ATF",
    "ICE", "CBP", "USCIS", "SBA", "OPM", "GSA", "EEOC", "CFPB", "CPSC", "NRC",
    "NLRB", "PBGC", "FERC", "FRB", "FDIC", "NCUA", "CFTC", "FEC", "FMC", "FHFA",
    "FLRA", "MSPB", "NTSB", "OSHRC", "USITC", "STB", "TVA", "USC", "USAF", "USN",
    "USMC", "USPTO", "USMS", "USSS", "USPP", "USCG", "USACE", "USCGR", "USCIS",
    "USCGA", "USCGB", "USCGR", "USCGAUX", "USCGB", "USCGR", "USCGAUX"
]

# Smaller Agencies and Commissions
smaller_agencies_commissions = [
    "ACL", "ACUS", "AID", "AMBC", "APHIS", "BBG", "BIA", "BLM", "BOP", "CBFO",
    "CCR", "CEQ", "CIS", "CMS", "CNS", "CO", "CSOSA", "DA", "DIA", "DNFSB",
    "EBSA", "EIB", "EOIR", "EOUSA", "ESA", "ETA", "FAA", "FCA", "FCSIC", "FLETC",
    "FMCS", "FMCSA", "FMSHRC", "FOMC", "FS", "FSA", "FSIS", "FWS", "IAF", "IMLS",
    "ITC", "JMD", "JWOD", "LSC", "MCC", "MSHA", "NCOC", "NEA", "NEH", "NIGC",
    "NMB", "NSA", "OA", "OCC", "OFHEO", "OGE", "OMB", "ONDCP", "OPIC", "ORO",
    "OSC", "OSHA", "PTO", "RRB", "SAMHSA", "SIPC", "SSS", "USTR"
]

# Additional agencies from the search results
additional_agencies = [
    "ABMC", "ARC", "BEP", "BOEM", "BSEE", "BTS", "BTFA", "CAU", "CISA", "CRS",
    "CNCS", "CAVC", "CIT", "DAU", "DARPA", "DISA", "DTRA", "EDA", "EIA", "ENRD",
    "FHFA", "FLC", "FLETC", "FMCS", "FMCSA", "FMSHRC", "FNS", "FSA", "FSIS",
    "HRSA", "IMLS", "IBWC", "IBC", "IJC", "JUSCANZ", "LLNL", "LOC", "MBDA",
    "NARA", "NCA", "NCHS", "NCD", "NCUA", "NED", "NGIA", "NHGRI", "NIAID",
    "NIBIB", "NIC", "NIEHS", "NIGMS", "NINR", "NIST", "NIDCD", "NIMHD", "NIH CC",
    "NRPC", "NREL", "NWRC", "NRCS", "ORNL", "OEM", "OFCCP", "OLMS", "OPE", "ORR",
    "OST", "OSMRE", "OSD", "USTR", "PFPA", "RFA", "RFE/RL", "SRNL", "TSA", "WAPA"
]

# Additional agencies not previously included
more_agencies = [
    "ACHP", "AFRH", "CEA", "CIGIE", "CSOSA", "DNDO", "EXIM", "FCSC", "FFIEC",
    "FRTIB", "IRSOB", "JMMFL", "MKUF", "MMC", "MWAA", "NCCB", "NCPC", "NIOSH",
    "NMIC", "NPS", "NRCS", "NTIA", "ONHIR", "OSTP", "PCLOB", "PRFOMB", "RATB",
    "SJI", "TRMC", "USADF", "USAGM", "USCAAF", "USCCR", "USCP", "USDA/AMS",
    "USDA/APHIS", "USDA/FNS", "USDA/FS", "USDA/FSIS", "USDA/NRCS", "USDA/RD",
    "USIBWC", "USNRC", "USTDA"
]

# Combine all agency lists
all_agencies = list(set(major_departments + independent_agencies + 
                        smaller_agencies_commissions + additional_agencies + 
                        more_agencies))

# Sort the combined list alphabetically
all_agencies.sort()

# Convert agency lists to dictionaries with 'abbreviation' key
def convert_to_dict(agency_list):
    return [{"abbreviation": agency} for agency in agency_list]

# Combine all categories into a single list
agencies = []

# Uncomment the categories you want to include
agencies += convert_to_dict(major_departments)
# agencies += convert_to_dict(independent_agencies)
# agencies += convert_to_dict(smaller_agencies_commissions)
# agencies += convert_to_dict(additional_agencies)

logging.info(f"Total number of agencies to process: {len(agencies)}")



def main():
    # Get and save agency components
    components = get_agency_components()
    save_json_response_in_subfolder(components, "general", "agency_components")

    # Get and save a specific component (using OIP as an example)
    oip_id = "8216158f-8089-431d-b866-dc334e8d4758"  # Office of Information Policy ID
    oip_info = get_specific_component(oip_id)
    save_json_response_in_subfolder(oip_info, "OIP", "oip_info")

    # Get and save the request form for OIP
    oip_form = get_component_request_form(oip_id)
    save_json_response_in_subfolder(oip_form, "OIP", "oip_request_form")

    # Fetch and save annual reports for specified agencies and year range
    fetch_and_save_annual_reports(agencies, START_YEAR, END_YEAR)

if __name__ == "__main__":
    main()