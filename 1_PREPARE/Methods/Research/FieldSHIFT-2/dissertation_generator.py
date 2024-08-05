import logging
import os
import time
from typing import Dict, Any
from utils import generate_llm_response, save_file, load_file
from config import DEFAULT_CONFIG
from dotenv import load_dotenv
import openai

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('FieldSHIFT-2')

def get_api_key():
    # Try to load from .env file
    load_dotenv()
    api_key = os.getenv('OPENAI_API_KEY')
    
    # If not found in .env, try to load from LLM_keys.key
    if not api_key:
        key_file_path = os.path.join(os.path.dirname(__file__), 'LLM_keys.key')
        if os.path.exists(key_file_path):
            with open(key_file_path, 'r') as key_file:
                for line in key_file:
                    if line.startswith('OPENAI_API_KEY'):
                        api_key = line.split('=')[1].strip()
                        break
    
    if api_key:
        logger.info(f"API key found: {api_key[:5]}...{api_key[-5:]}")
    else:
        logger.error("No API key found")
    
    return api_key

def generate_dissertation(outline_content: str, llm_params: Dict[str, Any]) -> str:
    """
    Generate a full dissertation based on the outline content.

    Args:
        outline_content (str): The dissertation outline content.
        llm_params (Dict[str, Any]): LLM parameters from config.

    Returns:
        str: The generated full dissertation.
    """
    logger.info("Generating full dissertation...")

    # Define the prompt template
    prompt_template = """
    You are a world-class academic writer tasked with expanding a PhD dissertation outline into a full, comprehensive dissertation. Using the provided outline, develop a detailed, well-researched, and intellectually rigorous dissertation that thoroughly explores each section and subsection.

    Please follow these guidelines:
    1. Maintain the structure provided in the outline.
    2. Greatly expand each section as relevant with relevant information, analysis, discussion.
    3. Include appropriate academic language and terminology.
    4. Provide in-depth explanations of concepts, theories, and methodologies. Highlight unique predictions, explanations, and experiments. 
    5. Discuss potential implications and applications of the research.
    6. Ensure coherence and flow between sections.
    7. Maintain a professional academic tone throughout the dissertation.

    Here's the outline to expand:

    {outline_content}

    Please generate a comprehensive, well-structured dissertation based on this outline. Ensure the output is professional Markdown formatted with proper headings, subheadings, paragraphs, and any necessary lists or tables.
    """

    try:
        prompt = prompt_template.format(outline_content=outline_content)
        dissertation = generate_llm_response(prompt, llm_params)
        logger.info("Full dissertation generated successfully.")
        return dissertation
    except Exception as e:
        logger.error(f"Error generating full dissertation: {str(e)}")
        raise

def process_dissertation_writing(input_dir: str, output_dir: str, llm_params: Dict[str, Any]):
    """
    Process the writing of full dissertations for all outline files in the input directory.

    Args:
        input_dir (str): Directory containing input files with dissertation outlines.
        output_dir (str): Directory to save the generated full dissertations.
        llm_params (Dict[str, Any]): LLM parameters from config.
    """
    try:
        for input_file in os.listdir(input_dir):
            if input_file.startswith("Dissertation_Outline_"):
                input_file_path = os.path.join(input_dir, input_file)
                
                # Prepare the output file name
                output_file_name = f"Written_{os.path.splitext(os.path.basename(input_file))[0]}.md"
                output_file_path = os.path.join(output_dir, output_file_name)
                
                # Check if the output file already exists
                if os.path.exists(output_file_path):
                    logger.info(f"Output file already exists, skipping: {output_file_name}")
                    print(f"Output file already exists, skipping: {output_file_name}")
                    continue
                
                # Load the dissertation outline content
                outline_content = load_file(input_file_path)
                
                # Generate the full dissertation
                start_time = time.time()
                dissertation = generate_dissertation(outline_content, llm_params)
                end_time = time.time()
                elapsed_time = end_time - start_time
                logger.info(f"Full dissertation generated in {elapsed_time:.2f} seconds.")
                print(f"Full dissertation generated in {elapsed_time:.2f} seconds.")
                
                # Ensure dissertation is a string
                if isinstance(dissertation, tuple):
                    dissertation = ' '.join(map(str, dissertation))

                # Save the dissertation to a Markdown file
                save_file(dissertation, output_file_path)  # Correct argument order
                logger.info(f"Full dissertation saved: {output_file_name}")

        logger.info("Dissertation writing process completed successfully.")
    except Exception as e:
        logger.error(f"Error in process_dissertation_writing: {str(e)}")
        raise

if __name__ == "__main__":
    logger.info("Starting script execution")
    
    # Define the input directory and output directory
    input_dir = "/home/tet/Documents/Github/Active_InferAnts/ActiveInferAnts/1_PREPARE/Methods/Research/FieldSHIFT-2/Inputs_and_Outputs/Shifted_Domain_Dissertation_Outline"
    output_dir = "/home/tet/Documents/Github/Active_InferAnts/ActiveInferAnts/1_PREPARE/Methods/Research/FieldSHIFT-2/Inputs_and_Outputs/Shifted_Dissertations"
    
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Prepare LLM parameters
    api_key = get_api_key()
    if not api_key:
        raise ValueError("API key not found or invalid")
    
    # Set the API key explicitly in the OpenAI configuration
    openai.api_key = api_key
    
    llm_params = {**DEFAULT_CONFIG['llm_params'], 'api_key': api_key}
    
    try:
        # Process the dissertation writing
        process_dissertation_writing(input_dir, output_dir, llm_params)
    except Exception as e:
        logger.error(f"An error occurred during script execution: {str(e)}")
        raise
    
    logger.info("Script execution completed")