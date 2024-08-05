import logging
import os
import time
from utils import load_file, save_file, generate_llm_response, get_api_key
from config import USER_CONFIG

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def perform_domain_shift(input_file: str, output_dir: str, llm_params: dict) -> None:
    """
    Perform a domain shift on a single domain file, send it to LLM, and save the response.

    Args:
        input_file (str): Path to the input domain file.
        output_dir (str): Directory to save the shifted domain.
        llm_params (dict): Parameters for the language model.
    """
    try:
        logger.info(f"Processing file: {input_file}")
        
        # Load domain content
        domain_content = load_file(input_file)
        
        # Generate the shifted domain using LLM
        shifted_domain, _ = generate_llm_response(domain_content, llm_params)
        
        # Prepare the output file name
        output_file_name = os.path.basename(input_file).replace('concatenated_', 'shifted_')
        save_file(shifted_domain, output_dir, output_file_name)
        
        logger.info(f"Shifted domain saved: {output_file_name}")
    except Exception as e:
        logger.error(f"Error processing file {input_file}: {str(e)}")

def process_domain_shift(input_file: str, output_dir: str, config: dict) -> None:
    """
    Process a domain shift on a specific domain file using the provided configuration.

    Args:
        input_file (str): Path to the input domain file.
        output_dir (str): Directory to save the shifted domain.
        config (dict): Configuration dictionary.
    """
    try:
        logger.info("Starting domain shift processing")
        
        # Get the API key using the get_api_key() function from config.py
        api_key = get_api_key()
        if not api_key:
            raise ValueError("API key not found or invalid")
        
        # Prepare LLM parameters
        llm_params = {**USER_CONFIG['llm_params'], 'api_key': api_key}
        
        # Prepare the output file name
        output_file_name = os.path.basename(input_file).replace('concatenated_', 'shifted_')
        output_file_path = os.path.join(output_dir, output_file_name)
        
        # Check if the output file already exists
        if os.path.exists(output_file_path):
            logger.info(f"Output file already exists: {output_file_name}. Skipping LLM request.")
        else:
            # Perform the domain shift
            start_time = time.time()
            perform_domain_shift(input_file, output_dir, llm_params)
            elapsed_time = time.time() - start_time
            logger.info(f"Elapsed time for processing {input_file}: {elapsed_time:.2f} seconds")
        
        logger.info("Domain shift processing completed successfully.")
    except Exception as e:
        logger.error(f"Error in process_domain_shift: {str(e)}")

if __name__ == "__main__":
    logger.info("Starting script execution")
    
    # Define the input file and output directory
    input_file = "/home/tet/Documents/Github/Active_InferAnts/ActiveInferAnts/1_PREPARE/Methods/Research/FieldSHIFT-2/Inputs_and_Outputs/Concatenated_Domain/concatenated_Synthetic_Fabric_to_Synthetic_Biology.md"
    output_dir = "/home/tet/Documents/Github/Active_InferAnts/ActiveInferAnts/1_PREPARE/Methods/Research/FieldSHIFT-2/Inputs_and_Outputs/Shifted_Domain"
    
    # Define the base directory for configuration
    base_dir = "/home/tet/Documents/Github/Active_InferAnts/ActiveInferAnts/1_PREPARE/Methods/Research/FieldSHIFT-2"
    
    # Create a configuration dictionary
    config = {
        'base_dir': base_dir,
        'output_dirs': {
            'Shifted_Domain': output_dir
        }
    }
    
    # Process the domain shift
    process_domain_shift(input_file, output_dir, config)
    
    logger.info("Script execution completed")