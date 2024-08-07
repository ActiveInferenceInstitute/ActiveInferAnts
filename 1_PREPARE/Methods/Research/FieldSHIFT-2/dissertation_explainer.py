import logging
import os
import time
from typing import Dict, Any, List
from utils import generate_llm_response, save_file, load_file
from config import DEFAULT_CONFIG
from dotenv import load_dotenv
import openai

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('FieldSHIFT-2')

# List of target audiences
TARGET_AUDIENCES = [
    "curious 5-year-old",  "well-studied & highly motivated skeptical PhD student", "high school senior undecided on whether or where to go to college", "possible private donor", "advanced technical professional"
]

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

def explain_dissertation(dissertation_content: str, target_audience: str, llm_params: Dict[str, Any]) -> str:
    """
    Explain an existing dissertation to a target audience while maintaining accuracy.

    Args:
        dissertation_content (str): The existing dissertation content.
        target_audience (str): The audience to explain the dissertation to.
        llm_params (Dict[str, Any]): LLM parameters from config.

    Returns:
        str: The explained dissertation.
    """
    logger.info(f"Explaining dissertation to a {target_audience}...")

    # Define the prompt template
    prompt_template = """
    You are a world-class educator tasked with explaining a PhD dissertation to a {target_audience}. 
    Maintain integrity, mutual dignity, and accuracy while adapting the explanation to the audience's type of understanding and broader person-ness.

    Please follow these guidelines:
    1. Adjust the language and complexity to suit the {target_audience}.
    2. Use analogies and examples appropriate for the {target_audience}.
    3. Break down complex concepts into simpler terms when necessary.
    4. Maintain the overall structure of the dissertation, but simplify where needed.
    5. Explain technical terms in a way the {target_audience} can understand.
    6. Use visual or interactive explanations if appropriate for the {target_audience}.
    7. Preserve the main arguments and key points of the dissertation.
    8. Adapt the length of the explanation to suit the attention span of the {target_audience}.
    9. If certain concepts are too advanced, provide a simplified overview.
    10. Encourage curiosity and further learning where appropriate.

    Here's the dissertation to explain to a {target_audience}:

    {dissertation_content}

    Please provide a clear and engaging explanation of this dissertation for a {target_audience}. Ensure the output retains the original structure as much as possible while making it accessible to the target audience.
    """

    try:
        prompt = prompt_template.format(target_audience=target_audience, dissertation_content=dissertation_content)
        explained_dissertation = generate_llm_response(prompt, llm_params)
        logger.info(f"Dissertation explained for a {target_audience} successfully.")
        return explained_dissertation
    except Exception as e:
        logger.error(f"Error explaining dissertation for a {target_audience}: {str(e)}")
        raise

def process_dissertation_explanation(input_dir: str, output_base_dir: str, llm_params: Dict[str, Any]):
    """
    Process the explanation of dissertations for all files in the input directory to multiple target audiences.

    Args:
        input_dir (str): Directory containing input files with existing dissertations.
        output_base_dir (str): Base directory to save the explained dissertations.
        llm_params (Dict[str, Any]): LLM parameters from config.
    """
    try:
        for input_file in os.listdir(input_dir):
            if input_file.endswith(".md"):
                input_file_path = os.path.join(input_dir, input_file)
                
                for target_audience in TARGET_AUDIENCES:
                    # Prepare the output directory and file name
                    output_dir = os.path.join(output_base_dir, f"Explained_for_{target_audience}")
                    os.makedirs(output_dir, exist_ok=True)
                    output_file_name = f"Explained_{os.path.splitext(os.path.basename(input_file))[0]}_{target_audience}.md"
                    output_file_path = os.path.join(output_dir, output_file_name)
                    
                    # Check if the output file already exists
                    if os.path.exists(output_file_path):
                        logger.info(f"Output file already exists, skipping: {output_file_name}")
                        print(f"Output file already exists, skipping: {output_file_name}")
                        continue
                    
                    # Load the existing dissertation content
                    dissertation_content = load_file(input_file_path)
                    
                    # Explain the dissertation
                    start_time = time.time()
                    explained_dissertation = explain_dissertation(dissertation_content, target_audience, llm_params)
                    end_time = time.time()
                    elapsed_time = end_time - start_time
                    logger.info(f"Dissertation explained for a {target_audience} in {elapsed_time:.2f} seconds.")
                    print(f"Dissertation explained for a {target_audience} in {elapsed_time:.2f} seconds.")
                    
                    # Ensure explained dissertation is a string
                    if isinstance(explained_dissertation, tuple):
                        explained_dissertation = ' '.join(map(str, explained_dissertation))

                    # Save the explained dissertation to a Markdown file
                    with open(output_file_path, 'w') as f:
                        f.write(explained_dissertation)
                    
                    logger.info(f"Explained dissertation saved: {output_file_name}")

        logger.info("Dissertation explanation process completed successfully.")
    except Exception as e:
        logger.error(f"Error in process_dissertation_explanation: {str(e)}")
        raise

if __name__ == "__main__":
    logger.info("Starting script execution")
    
    # Define the input directory and output directory
    input_dir = "/home/tet/Documents/Github/Active_InferAnts/ActiveInferAnts/1_PREPARE/Methods/Research/FieldSHIFT-2/Inputs_and_Outputs/Shifted_Dissertations_Improved_Once"
    output_base_dir = "/home/tet/Documents/Github/Active_InferAnts/ActiveInferAnts/1_PREPARE/Methods/Research/FieldSHIFT-2/Inputs_and_Outputs/Explained_Dissertations"
    
    # Ensure the output base directory exists
    os.makedirs(output_base_dir, exist_ok=True)
    
    # Prepare LLM parameters
    api_key = get_api_key()
    if not api_key:
        raise ValueError("API key not found or invalid")
    
    # Set the API key explicitly in the OpenAI configuration
    openai.api_key = api_key
    
    llm_params = {**DEFAULT_CONFIG['llm_params'], 'api_key': api_key}
    
    try:
        # Process the dissertation explanations
        process_dissertation_explanation(input_dir, output_base_dir, llm_params)
    except Exception as e:
        logger.error(f"An error occurred during script execution: {str(e)}")
        raise
    
    logger.info("Script execution completed")