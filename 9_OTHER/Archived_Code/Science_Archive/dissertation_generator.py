import logging
import os
from typing import Dict, Any
from utils import generate_llm_response, save_file, load_file, get_api_key
from config import DEFAULT_CONFIG

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('FieldSHIFT-2')

def generate_dissertation_outline(shifted_domain_content: str, prompt_template: str, llm_params: Dict[str, Any]) -> str:
    """
    Generate a dissertation outline based on the shifted domain and prompt template.

    Args:
        shifted_domain_content (str): The shifted domain content.
        prompt_template (str): The template for the dissertation outline prompt.
        llm_params (Dict[str, Any]): LLM parameters from config.

    Returns:
        str: The generated dissertation outline.
    """
    logger.info("Generating dissertation outline...")

    prompt = f"""
    {prompt_template}

    {shifted_domain_content}

    Ensure that the Dissertation outline is coherent, long with many chapters and sub-sections, comprehensive, well-structured, covers all key aspects/implications of the shifted domain, and ensure the output is professional Markdown formatted.
    """

    try:
        outline = generate_llm_response(prompt, llm_params)
        logger.info("Dissertation outline generated successfully.")
        return outline
    except Exception as e:
        logger.error(f"Error generating dissertation outline: {str(e)}")
        raise

def process_dissertation_generation(input_dir: str, output_dir: str, prompt_template_path: str, llm_params: Dict[str, Any]) -> None:
    """
    Process dissertation generation for all shifted domain files in the input directory.

    Args:
        input_dir (str): Path to the input directory containing shifted domain files.
        output_dir (str): Directory to save the generated dissertation outlines.
        prompt_template_path (str): Path to the dissertation prompt template file.
        llm_params (Dict[str, Any]): LLM parameters from config.
    """
    try:
        logger.info("Starting dissertation generation processing")
        # Load the dissertation prompt template
        prompt_template = load_file(prompt_template_path)

        # Iterate over all files in the input directory
        for input_file in os.listdir(input_dir):
            input_file_path = os.path.join(input_dir, input_file)
            
            # Load the shifted domain content
            shifted_domain_content = load_file(input_file_path)
            
            # Generate the dissertation outline
            outline = generate_dissertation_outline(shifted_domain_content, prompt_template, llm_params)
            
            # Prepare the output file name
            output_file_name = f"Dissertation_Outline_{os.path.splitext(os.path.basename(input_file))[0]}.md"
            save_file(outline, output_dir, output_file_name)
            
            logger.info(f"Dissertation outline saved: {output_file_name}")

        logger.info("Dissertation generation processing completed successfully.")
    except Exception as e:
        logger.error(f"Error in process_dissertation_generation: {str(e)}")
        raise

if __name__ == "__main__":
    logger.info("Starting script execution")
    
    # Define the input directory and output directory
    input_dir = "/home/tet/Documents/Github/Active_InferAnts/ActiveInferAnts/1_PREPARE/Methods/Research/FieldSHIFT-2/Inputs_and_Outputs/Shifted_Domain"
    output_dir = "/home/tet/Documents/Github/Active_InferAnts/ActiveInferAnts/1_PREPARE/Methods/Research/FieldSHIFT-2/Inputs_and_Outputs/Shifted_Domain_Dissertation_Outline"
    
    # Define the path to the dissertation prompt template
    prompt_template_path = "/home/tet/Documents/Github/Active_InferAnts/ActiveInferAnts/1_PREPARE/Methods/Research/FieldSHIFT-2/Inputs_and_Outputs/Prompts/FieldSHIFT-2_Write_Dissertation.md"
    
    # Prepare LLM parameters
    api_key = get_api_key()
    if not api_key:
        raise ValueError("API key not found or invalid")
    llm_params = {**DEFAULT_CONFIG['llm_params'], 'api_key': api_key}
    
    # Process the dissertation generation
    process_dissertation_generation(input_dir, output_dir, prompt_template_path, llm_params)
    
    logger.info("Script execution completed")