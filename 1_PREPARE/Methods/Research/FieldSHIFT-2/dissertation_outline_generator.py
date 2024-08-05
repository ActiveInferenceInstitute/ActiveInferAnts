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

def generate_dissertation_outline(shifted_domain_content: str, llm_params: Dict[str, Any]) -> str:
    """
    Generate a dissertation outline based on the shifted domain content.

    Args:
        shifted_domain_content (str): The shifted domain content.
        llm_params (Dict[str, Any]): LLM parameters from config.

    Returns:
        str: The generated dissertation outline.
    """
    logger.info("Generating dissertation outline...")

    # Define the prompt template
    prompt_template = """
    You are a world-class academic advisor and domain expert tasked with creating a comprehensive and groundbreaking PhD dissertation plan for a newly Shifted Domain. This domain represents an innovative fusion of two previously distinct fields, offering unprecedented opportunities for research and impact. Your task is to craft a detailed, expansive, and intellectually rigorous dissertation plan that not only articulates the transformative potential of this Shifted Domain but also provides a clear roadmap for a doctoral candidate to make significant contributions to this emerging field.
    Using the provided Shifted Domain description, develop a massive, comprehensive PhD dissertation plan following this structure:

    # Executive Summary
    Provide a concise overview of the dissertation's scope, significance, and potential impact on the field.

    # Introduction
    ## Background of the Shifted Domain
    ## Significance and Novelty of the Research
    ## Overarching Research Questions and Objectives

    # Literature Review
    ## Historical Context of the Original Domains
    ## Current State of Knowledge in Both Fields
    ## Gaps and Opportunities Presented by the Shifted Domain

    # Theoretical Framework
    ## Foundational Theories from Original Domains
    ## New Theoretical Constructs Emerging from the Shift
    ## Proposed Integrated Theoretical Model

    # Methodology
    ## Research Design Overview
    ## Data Collection Methods
    ## Analytical Approaches
    ## Ethical Considerations

    # Core Chapters
    Expand each with multiple sub-sections, specific hypotheses, and proposed experiments.
    ## [Key Aspect 1 of Shifted Domain]
    ### Sub-section 1
    ### Sub-section 2
    ## [Key Aspect 2 of Shifted Domain]
    ### Sub-section 1
    ### Sub-section 2
    ## [Key Aspect 3 of Shifted Domain]
    ### Sub-section 1
    ### Sub-section 2
    ## [Key Aspect n of Shifted Domain]
    ### Sub-section 1
    ### Sub-section 2

    # Interdisciplinary Implications
    ## Impact on Original Domain A
    ## Impact on Original Domain B
    ## Potential for New Sub-disciplines or Fields

    # Practical Applications
    ## Industry Relevance
    ## Policy Implications
    ## Societal Impact

    # Future Research Directions
    ## Short-term Research Opportunities
    ## Long-term Research Agenda
    ## Potential Collaborations and Interdisciplinary Projects

    Ensure that the Dissertation outline is coherent, long with many chapters and sub-sections, comprehensive, well-structured, covers all key aspects/implications of the shifted domain, and ensure the output is professional Markdown formatted with proper line breaks and indentation.
    """

    try:
        prompt = f"{prompt_template}\n\n{shifted_domain_content}"
        outline = generate_llm_response(prompt, llm_params)
        logger.info("Dissertation outline generated successfully.")
        return outline
    except Exception as e:
        logger.error(f"Error generating dissertation outline: {str(e)}")
        raise

def process_dissertation_generation(input_dir: str, output_dir: str, llm_params: Dict[str, Any]):
    """
    Process the generation of dissertation outlines for all files in the input directory.

    Args:
        input_dir (str): Directory containing input files with shifted domain content.
        output_dir (str): Directory to save the generated dissertation outlines.
        llm_params (Dict[str, Any]): LLM parameters from config.
    """
    try:
        for input_file in os.listdir(input_dir):
            input_file_path = os.path.join(input_dir, input_file)
            
            # Prepare the output file name
            output_file_name = f"Dissertation_Outline_{os.path.splitext(os.path.basename(input_file))[0]}.md"
            output_file_path = os.path.join(output_dir, output_file_name)
            
            # Check if the output file already exists
            if os.path.exists(output_file_path):
                logger.info(f"Output file already exists, skipping: {output_file_name}")
                print(f"Output file already exists, skipping: {output_file_name}")
                continue
            
            # Load the shifted domain content
            shifted_domain_content = load_file(input_file_path)
            
            # Generate the dissertation outline
            start_time = time.time()
            outline = generate_dissertation_outline(shifted_domain_content, llm_params)
            end_time = time.time()
            elapsed_time = end_time - start_time
            logger.info(f"Dissertation outline generated in {elapsed_time:.2f} seconds.")
            print(f"Dissertation outline generated in {elapsed_time:.2f} seconds.")
            
            # Convert outline to string if it's not already one
            if not isinstance(outline, str):
                outline = ' '.join(map(str, outline))  # This assumes the tuple elements are stringable
            
            # Save the outline to a Markdown file
            with open(output_file_path, 'w') as f:
                f.write(outline)
            
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
    
    # Prepare LLM parameters
    api_key = get_api_key()
    if not api_key:
        raise ValueError("API key not found or invalid")
    
    # Set the API key explicitly in the OpenAI configuration
    openai.api_key = api_key
    
    llm_params = {**DEFAULT_CONFIG['llm_params'], 'api_key': api_key}
    
    # Process the dissertation generation
    process_dissertation_generation(input_dir, output_dir, llm_params)
    
    logger.info("Script execution completed")