import re
import subprocess
from typing import List, Dict, Optional

class GitHubRepoSecurity:
    """
    A class to encapsulate GitHub repository security utility functions.
    """

    @staticmethod
    def scan_for_sensitive_data(repo_path: str) -> List[Dict[str, str]]:
        """
        Scans the specified repository for sensitive data like API keys, passwords, etc.
        
        Parameters:
        - repo_path (str): The path to the GitHub repository.
        
        Returns:
        - list: A list of dictionaries with file names and lines potentially containing sensitive data.
        """
        sensitive_data_patterns = [
            r'\b[A-Za-z0-9+/]{40}\b',  # Generic API key pattern
            r'\b[0-9a-fA-F]{32}\b',  # Generic 32-character hexadecimal token
            r'\b[0-9a-fA-F]{64}\b',  # Generic 64-character hexadecimal token
        ]
        findings = []
        for root, dirs, files in os.walk(repo_path):
            for file in files:
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    for line_number, line in enumerate(f, 1):
                        if any(re.search(pattern, line) for pattern in sensitive_data_patterns):
                            findings.append({'file': file_path, 'line': line_number})
        return findings

    @staticmethod
    def enforce_branch_protection_rules(repo_name: str, branch_name: str = 'main') -> bool:
        """
        Enforces branch protection rules on the specified branch of a GitHub repository.
        
        Parameters:
        - repo_name (str): The name of the GitHub repository.
        - branch_name (str): The name of the branch to enforce protection rules on. Defaults to 'main'.
        
        Returns:
        - bool: True if enforcement was successful, False otherwise.
        """
        try:
            subprocess.run(['git', '-C', repo_name, 'branch', '--set-upstream-to', f'origin/{branch_name}', branch_name], check=True)
            subprocess.run(['git', '-C', repo_name, 'config', '--add', 'branch.' + branch_name + '.protection', 'true'], check=True)
            return True
        except subprocess.CalledProcessError:
            return False

    @staticmethod
    def audit_repository_access(repo_name: str) -> Dict[str, List[str]]:
        """
        Audits and reports on who has access to the specified GitHub repository.
        
        Parameters:
        - repo_name (str): The name of the GitHub repository.
        
        Returns:
        - dict: A dictionary with user roles as keys and lists of usernames with that role as values.
        """
        # Placeholder for actual implementation
        # This example assumes a function `get_repo_access_info` exists and returns access information
        access_info = get_repo_access_info(repo_name)
        access_audit = {}
        for user, role in access_info.items():
            if role in access_audit:
                access_audit[role].append(user)
            else:
                access_audit[role] = [user]
        return access_audit
