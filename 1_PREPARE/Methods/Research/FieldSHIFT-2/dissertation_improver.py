import logging
import os
import time
from typing import Dict, Any
from utils import generate_llm_response, save_file, load_file
from config import DEFAULT_CONFIG
from dotenv import load_dotenv  # Add this import
import openai

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('FieldSHIFT-2')

def get_api_key():
    load_dotenv()
    api_key = os.getenv('OPENAI_API_KEY')
    
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

def improve_dissertation(dissertation_content: str, llm_params: Dict[str, Any]) -> str:
    """
    Improve an existing dissertation by adding depth, creativity, and academic rigor.

    Args:
        dissertation_content (str): The existing dissertation content.
        llm_params (Dict[str, Any]): LLM parameters from config.

    Returns:
        str: The improved dissertation.
    """
    logger.info("Improving dissertation...")

    # Define the prompt template
    prompt_template = """
    You are a world-class academic writer tasked with improving an existing PhD dissertation. Using the provided dissertation, enhance its depth, creativity, and academic rigor while maintaining its original structure and core ideas.

    Please follow these guidelines:
    1. Maintain the existing structure and core arguments of the dissertation.
    2. Add depth and length to each section by incorporating additional unique explanations, salient creative questions, and advanced concepts.
    3. Introduce tables of alternative outcomes to showcase different perspectives or potential results.
    4. Formulate and include testable hypotheses that extend the research.
    5. Enhance the academic language and terminology where appropriate.
    6. Integrate new, cutting-edge theories or methodologies that complement the existing content.
    7. Propose innovative experiments or research directions that build upon the current work.
    8. Expand on the implications and applications of the research, considering interdisciplinary connections.
    9. Ensure improved coherence and flow between sections.
    10. Maintain and elevate the professional academic tone throughout the dissertation.

    Here's the dissertation to improve:

    {dissertation_content}

    Please generate an improved, more comprehensive version of this dissertation. Ensure the output retains the original Markdown formatting with proper headings, subheadings, paragraphs, and incorporate any necessary new lists or tables.
    """

    try:
        prompt = prompt_template.format(dissertation_content=dissertation_content)
        improved_dissertation = generate_llm_response(prompt, llm_params)
        logger.info("Dissertation improved successfully.")
        return improved_dissertation
    except Exception as e:
        logger.error(f"Error improving dissertation: {str(e)}")
        raise

def process_dissertation_improvement(input_dir: str, output_dir: str, llm_params: Dict[str, Any]):
    """
    Process the improvement of dissertations for all files in the input directory.

    Args:
        input_dir (str): Directory containing input files with existing dissertations.
        output_dir (str): Directory to save the improved dissertations.
        llm_params (Dict[str, Any]): LLM parameters from config.
    """
    try:
        for input_file in os.listdir(input_dir):
            if input_file.startswith("Written_Dissertation_Outline_"):
                input_file_path = os.path.join(input_dir, input_file)
                
                # Prepare the output file name
                output_file_name = f"Improved_{os.path.splitext(os.path.basename(input_file))[0]}.md"
                output_file_path = os.path.join(output_dir, output_file_name)
                
                # Check if the output file already exists
                if os.path.exists(output_file_path):
                    logger.info(f"Output file already exists, skipping: {output_file_name}")
                    print(f"Output file already exists, skipping: {output_file_name}")
                    continue
                
                # Load the existing dissertation content
                dissertation_content = load_file(input_file_path)
                
                # Improve the dissertation
                start_time = time.time()
                improved_dissertation = improve_dissertation(dissertation_content, llm_params)
                end_time = time.time()
                elapsed_time = end_time - start_time
                logger.info(f"Dissertation improved in {elapsed_time:.2f} seconds.")
                print(f"Dissertation improved in {elapsed_time:.2f} seconds.")
                
                # Ensure improved dissertation is a string
                if isinstance(improved_dissertation, tuple):
                    improved_dissertation = ' '.join(map(str, improved_dissertation))

                # Save the improved dissertation to a Markdown file
                with open(output_file_path, 'w') as f:
                    f.write(improved_dissertation)
                
                logger.info(f"Improved dissertation saved: {output_file_name}")

        logger.info("Dissertation improvement process completed successfully.")
    except Exception as e:
        logger.error(f"Error in process_dissertation_improvement: {str(e)}")
        raise

if __name__ == "__main__":
    logger.info("Starting script execution")
    
    # Define the input directory and output directory
    input_dir = "/home/tet/Documents/Github/Active_InferAnts/ActiveInferAnts/1_PREPARE/Methods/Research/FieldSHIFT-2/Inputs_and_Outputs/Shifted_Dissertations"
    output_dir = "/home/tet/Documents/Github/Active_InferAnts/ActiveInferAnts/1_PREPARE/Methods/Research/FieldSHIFT-2/Inputs_and_Outputs/Shifted_Dissertations_Improved_Once"
    
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
        # Process the dissertation improvement
        process_dissertation_improvement(input_dir, output_dir, llm_params)
    except Exception as e:
        logger.error(f"An error occurred during script execution: {str(e)}")
        raise
    
    logger.info("Script execution completed")