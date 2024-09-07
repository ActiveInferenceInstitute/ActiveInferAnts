import logging
from FOIA_utils import setup_logging
import FOIA_calls
import FOIA_agency_year
import FOIA_to_Markdown
import FOIA_analyze

def main():
    setup_logging()
    logging.info("Starting FOIA script execution")

    try:
        # Execute FOIA_calls.py
        logging.info("Executing FOIA_calls.py")
        FOIA_calls.main()

        # Execute FOIA_agency_year.py
        logging.info("Executing FOIA_agency_year.py")
        FOIA_agency_year.main()

        # Execute FOIA_to_Markdown.py
        logging.info("Executing FOIA_to_Markdown.py")
        FOIA_to_Markdown.process_files("FOIA_Responses", "FOIA_Markdown")

        # Execute FOIA_analyze.py
        logging.info("Executing FOIA_analyze.py")
        FOIA_analyze.main()

    except Exception as e:
        logging.error(f"An error occurred during script execution: {str(e)}")
    
    logging.info("FOIA script execution completed")

if __name__ == "__main__":
    main()
