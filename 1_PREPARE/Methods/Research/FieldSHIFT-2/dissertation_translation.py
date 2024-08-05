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

# List of target languages
TARGET_LANGUAGES = [
    "Chinese-Mandarin", "Spanish", "English", "Hindi", "Arabic", "Sanskrit",
    "Bengali", "Portuguese", "Russian", "Japanese", "Punjabi", "Navajo",
    "German", "Javanese", "Hebrew", "Telugu", "Vietnamese", "Sami",
    "Korean", "French", "Marathi", "Tamil", "Urdu", "Tibetan"
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

def translate_dissertation(dissertation_content: str, target_language: str, llm_params: Dict[str, Any]) -> str:
    """
    Translate an existing dissertation to a target language while maintaining academic quality.

    Args:
        dissertation_content (str): The existing dissertation content.
        target_language (str): The language to translate the dissertation into.
        llm_params (Dict[str, Any]): LLM parameters from config.

    Returns:
        str: The translated dissertation.
    """
    logger.info(f"Translating dissertation to {target_language}...")

    # Define the prompt template
    prompt_template = """
    You are a world-class academic translator tasked with translating a PhD dissertation from its original language to {target_language}. Maintain the high academic quality, technical accuracy, and nuanced arguments of the original text.

    Please follow these guidelines:
    1. Preserve the original structure, headings, and formatting of the dissertation.
    2. Accurately translate all technical terms, ensuring consistency throughout the document.
    3. Maintain the academic tone and style appropriate for a PhD-level dissertation.
    4. Preserve any citations, references, or footnotes in their original format.
    5. Ensure that discipline-specific jargon is correctly translated or kept in its original form if more appropriate.
    6. Adapt idiomatic expressions to maintain their meaning in the target language.
    7. Preserve the logical flow and coherence of arguments across sections.
    8. Maintain the original paragraph structure as much as possible.
    9. If certain terms are best left untranslated, keep them in the original language and provide a brief explanation in parentheses if necessary.
    10. Ensure that any tables, figures, or diagrams are accurately translated, including captions and labels.

    Here's the dissertation to translate to {target_language}:

    {dissertation_content}

    Please provide a high-quality translation of this dissertation in {target_language}. Ensure the output retains the original Markdown formatting with proper headings, subheadings, paragraphs, and any existing lists or tables.
    """

    try:
        prompt = prompt_template.format(target_language=target_language, dissertation_content=dissertation_content)
        translated_dissertation = generate_llm_response(prompt, llm_params)
        logger.info(f"Dissertation translated to {target_language} successfully.")
        return translated_dissertation
    except Exception as e:
        logger.error(f"Error translating dissertation to {target_language}: {str(e)}")
        raise

def process_dissertation_translation(input_dir: str, output_base_dir: str, llm_params: Dict[str, Any]):
    """
    Process the translation of dissertations for all files in the input directory to multiple languages.

    Args:
        input_dir (str): Directory containing input files with existing dissertations.
        output_base_dir (str): Base directory to save the translated dissertations.
        llm_params (Dict[str, Any]): LLM parameters from config.
    """
    try:
        for input_file in os.listdir(input_dir):
            if input_file.endswith(".md"):
                input_file_path = os.path.join(input_dir, input_file)
                
                for target_language in TARGET_LANGUAGES:
                    # Prepare the output directory and file name
                    output_dir = os.path.join(output_base_dir, f"{target_language}_Dissertations")
                    os.makedirs(output_dir, exist_ok=True)
                    output_file_name = f"Translated_{os.path.splitext(os.path.basename(input_file))[0]}_{target_language}.md"
                    output_file_path = os.path.join(output_dir, output_file_name)
                    
                    # Check if the output file already exists
                    if os.path.exists(output_file_path):
                        logger.info(f"Output file already exists, skipping: {output_file_name}")
                        print(f"Output file already exists, skipping: {output_file_name}")
                        continue
                    
                    # Load the existing dissertation content
                    dissertation_content = load_file(input_file_path)
                    
                    # Translate the dissertation
                    start_time = time.time()
                    translated_dissertation = translate_dissertation(dissertation_content, target_language, llm_params)
                    end_time = time.time()
                    elapsed_time = end_time - start_time
                    logger.info(f"Dissertation translated to {target_language} in {elapsed_time:.2f} seconds.")
                    print(f"Dissertation translated to {target_language} in {elapsed_time:.2f} seconds.")
                    
                    # Ensure translated dissertation is a string
                    if isinstance(translated_dissertation, tuple):
                        translated_dissertation = ' '.join(map(str, translated_dissertation))

                    # Save the translated dissertation to a Markdown file
                    with open(output_file_path, 'w') as f:
                        f.write(translated_dissertation)
                    
                    logger.info(f"Translated dissertation saved: {output_file_name}")

        logger.info("Dissertation translation process completed successfully.")
    except Exception as e:
        logger.error(f"Error in process_dissertation_translation: {str(e)}")
        raise

if __name__ == "__main__":
    logger.info("Starting script execution")
    
    # Define the input directory and output directory
    input_dir = "/home/tet/Documents/Github/Active_InferAnts/ActiveInferAnts/1_PREPARE/Methods/Research/FieldSHIFT-2/Inputs_and_Outputs/Shifted_Dissertations_Improved_Once"
    output_base_dir = "/home/tet/Documents/Github/Active_InferAnts/ActiveInferAnts/1_PREPARE/Methods/Research/FieldSHIFT-2/Inputs_and_Outputs/Translated_Dissertations"
    
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
        # Process the dissertation translations
        process_dissertation_translation(input_dir, output_base_dir, llm_params)
    except Exception as e:
        logger.error(f"An error occurred during script execution: {str(e)}")
        raise
    
    logger.info("Script execution completed")