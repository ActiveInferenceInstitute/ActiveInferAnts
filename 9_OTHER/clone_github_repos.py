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
    
    # if isinstance(repo_urls, dict):
    #     repo_urls = list(repo_urls.values())
    
    # for git_url in repo_urls:
    #     clone_repo(git_url, target_dir)

# Enhanced cloning process with category-based organization
if __name__ == "__main__":
    repos_to_clone = {
        "TheBraj ": [
            "https://github.com/TheBrainTech/thebrain-api-quickstart-python"
        ]
    }
    
    target_dir = input("Enter the target directory (default is 'repos/'): ").strip() or "repos/"
    
    for category, urls in repos_to_clone.items():
        print(f"Cloning {category} repositories...")
        clone_repos(urls, os.path.join(target_dir, category))