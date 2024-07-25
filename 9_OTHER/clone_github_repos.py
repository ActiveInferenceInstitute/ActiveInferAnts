import subprocess
import sys
import os
from typing import Union, List, Dict, Any

def execute_command(command: List[str]) -> None:
    """
    Executes a given command using subprocess and handles errors.
    
    Parameters:
    - command (List[str]): The command to execute as a list of strings.
    """
    try:
        subprocess.run(command, check=True, capture_output=True)
    except subprocess.CalledProcessError as e:
        error_msg = e.stderr.decode()
        print(f"Command execution failed with error: {error_msg}", file=sys.stderr)
        sys.exit(1)

def clone_repo(git_url: str, target_dir: str) -> None:
    """
    Clones a single GitHub repository into the specified target directory.
    
    Parameters:
    - git_url (str): The GitHub repository URL to clone.
    - target_dir (str): The directory to clone the repository into.
    """
    repo_name = git_url.split('/')[-1]  # Extracts repo name from URL
    full_path = os.path.join(target_dir, repo_name)
    clone_command = ["git", "clone", git_url, full_path]
    
    execute_command(clone_command)
    print(f"Successfully cloned {git_url} into {full_path}.")

def clone_repos(repo_urls: Union[List[str], Dict[str, str]], target_dir: str = "repos/") -> None:
    """
    Clones a list or dictionary of GitHub repositories into the specified target directory.
    If no target directory is specified, it clones into the 'repos/' directory.
    
    Parameters:
    - repo_urls (Union[List[str], Dict[str, str]]): A list or dictionary of GitHub repository URLs to clone.
    - target_dir (str, optional): The directory to clone the repositories into.
    """
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    if isinstance(repo_urls, dict):
        repo_urls = list(repo_urls.values())
    
    for git_url in repo_urls:
        clone_repo(git_url, target_dir)

# Enhanced cloning process with category-based organization
if __name__ == "__main__":
    repos_to_clone = {
        "ActiveInference": [
            "https://github.com/infer-actively/pymdp",
        ],
        
        "Nostr": [
            "https://github.com/nostr-protocol/nostr",
            "https://github.com/fiatjaf/nostr-tools",
            "https://github.com/limina1/indextr-client",
            "https://github.com/fiatjaf/quill-asciidoc",
            "https://github.com/fiatjaf/svelte-asciidoc",
            "https://github.com/github-tijlxyz/wikinostr",
            "https://github.com/aljazceru/awesome-nostr",
            "https://github.com/nostr-connect/connect"
        ]
        # ,
        # "Synergetics": [
        #     "https://github.com/4dsolutions/MartianMath",
        #     "https://github.com/4dsolutions/m4w",
        #     "https://github.com/4dsolutions/python_camp",
        #     "https://github.com/4dsolutions/School_of_Tomorrow",
        #     "https://github.com/4dsolutions/DigitalMathematics",
        #     "https://github.com/4dsolutions/Curriculum_Development"
        # ],
        # "Ants": [
        #     "https://github.com/Social-Insect-Genomics/",
        #     "https://github.com/johnssproul/Insect_REs",
        #     "https://github.com/pbfrandsen/insect_genome_assemblies",
        #     "https://github.com/PeterMulhair/DToL_insects",
        #     "https://github.com/fohebert/GenomeAnnotation",
        #     "https://github.com/guillemylla/Crickets_Genome_Annotation",
        # ]
    }
    target_dir = input("Enter the target directory (default is 'repos/'): ").strip() or "repos/"
    
    for category, urls in repos_to_clone.items():
        print(f"Cloning {category} repositories...")
        clone_repos(urls, os.path.join(target_dir, category))
