import os
from typing import Dict, Any

def read_api_key(file_path: str) -> str:
    """
    Reads the API key from the specified file.

    Args:
        file_path (str): Path to the file containing the API key.

    Returns:
        str: The API key.

    Raises:
        ValueError: If the API key is not found in the file.
        FileNotFoundError: If the file does not exist.
    """
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if line.startswith("OPENAI_API_KEY"):
                    return line.split('=')[1].strip()
        raise ValueError("API key not found in the specified file")
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} does not exist")

# Get the directory of the current script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Path to the LLM_keys.key file
API_KEY_FILE = os.path.join(SCRIPT_DIR, 'LLM_keys.key')

# Ensure output directories exist
def ensure_directories(dirs: Dict[str, str]):
    """
    Ensures that the specified directories exist.

    Args:
        dirs (Dict[str, str]): Dictionary of directory paths.
    """
    for key, path in dirs.items():
        os.makedirs(path, exist_ok=True)

# User-configurable parameters
USER_CONFIG = {
    'domain_paths': [],  # List of paths to domain files
    'output_dirs': {
        'Domain': os.path.join(SCRIPT_DIR, 'Inputs_and_Outputs', 'Synthetic_Domain_Expressions'),
        'Pro-Shifted_Domain': os.path.join(SCRIPT_DIR, 'Inputs_and_Outputs', 'Pro-Shifted_Domain'),
        'Shifted_Domain': os.path.join(SCRIPT_DIR, 'Inputs_and_Outputs', 'Shifted_Domain'),
        'Shifted_Domain_Dissertation_Outline': os.path.join(SCRIPT_DIR, 'Inputs_and_Outputs', 'Shifted_Domain_Dissertation_Outline'),
        'Shifted_Domain_ProGrant': os.path.join(SCRIPT_DIR, 'Inputs_and_Outputs', 'Shifted_Domain_ProGrant'),
        'Analyses': os.path.join(SCRIPT_DIR, 'Inputs_and_Outputs', 'Analyses'),
        'Prompts': os.path.join(SCRIPT_DIR, 'Inputs_and_Outputs', 'Prompts')
    },
    'llm_params': {
        'model': 'gpt-4o-mini-2024-07-18',
        'max_tokens': 4096,
        'temperature': 0.5,
        'top_p': 1.0,
        'frequency_penalty': 0.0,
        'presence_penalty': 0.0,
        'n': 1,
        'stream': False,
        'stop': None,
        'api_key': read_api_key(API_KEY_FILE)  # Read the API key from the file
    },
    'analysis_params': {
        'linguistic_features': ['lexical_diversity', 'sentiment', 'readability'],
        'similarity_threshold': 0.7
    },
    'dissertation_params': {
        'num_chapters': 9,
        'min_sections_per_chapter': 3,
        'max_sections_per_chapter': 6
    },
    'pro_grant_params': {
        'sections': ['Abstract', 'Introduction', 'Objectives', 'Methodology', 'Expected Outcomes', 'Budget', 'Timeline'],
        'max_word_count': 5000
    }
}

# Ensure output directories exist
ensure_directories(USER_CONFIG['output_dirs'])

# Default configuration
DEFAULT_CONFIG = {
    'domain_paths': USER_CONFIG['domain_paths'],
    'prompts': {
        'pro_shift': "Generate a pro-shifted domain combining the following domains: {domains}",
        'domain_shift': "Shift the following domain: {domain}",
        'dissertation_outline': "Create a dissertation outline for the following shifted domain: {shifted_domain}",
        'pro_grant': "Prepare a grant proposal for exploring, characterizing, and applying the following shifted domain: {shifted_domain}"
    },
    'llm_params': USER_CONFIG['llm_params'],
    'output_dirs': USER_CONFIG['output_dirs'],
    'analysis_params': USER_CONFIG['analysis_params'],
    'dissertation_params': USER_CONFIG['dissertation_params'],
    'pro_grant_params': USER_CONFIG['pro_grant_params']
}