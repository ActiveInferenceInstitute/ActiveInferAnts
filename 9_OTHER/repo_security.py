import os
import re
import subprocess
import logging
from typing import List, Dict, Optional, Tuple
from github import Github, GithubException
from dotenv import load_dotenv

class GitHubRepoSecurity:
    """
    A comprehensive class to manage and enhance GitHub repository security.
    """

    def __init__(self, github_token: Optional[str] = None):
        """
        Initialize the GitHubRepoSecurity class.

        Args:
            github_token (Optional[str]): GitHub API token for authentication. If not provided, it will attempt to load from environment variables.
        """
        load_dotenv()  # Load environment variables from .env file
        self.github_token = github_token or os.getenv('GITHUB_TOKEN')
        if not self.github_token:
            raise ValueError("GitHub token is required. Please provide it or set the GITHUB_TOKEN environment variable.")
        self.github = Github(self.github_token)
        self.logger = self._setup_logger()

    @staticmethod
    def _setup_logger() -> logging.Logger:
        """Set up and return a logger for the class."""
        logger = logging.getLogger('GitHubRepoSecurity')
        logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger

    def scan_for_sensitive_data(self, repo_path: str) -> List[Dict[str, str]]:
        """
        Scans the specified repository for sensitive data like API keys, passwords, etc.
        
        Args:
            repo_path (str): The path to the GitHub repository.
        
        Returns:
            List[Dict[str, str]]: A list of dictionaries with file names and lines potentially containing sensitive data.
        """
        sensitive_data_patterns = [
            (r'\b[A-Za-z0-9+/]{40}\b', 'Generic API key'),
            (r'\b[0-9a-fA-F]{32}\b', '32-character hexadecimal token'),
            (r'\b[0-9a-fA-F]{64}\b', '64-character hexadecimal token'),
            (r'(?i)password\s*=\s*["\']?[\w@#$%^&*()-+=]{8,}["\']?', 'Potential password'),
            (r'(?i)api[_-]?key\s*=\s*["\']?[\w-]{16,}["\']?', 'Potential API key'),
            (r'(?i)secret\s*=\s*["\']?[\w-]{16,}["\']?', 'Potential secret'),
            (r'(?i)access[_-]?token\s*=\s*["\']?[\w-]{16,}["\']?', 'Potential access token'),
        ]
        findings = []
        excluded_dirs = {'.git', 'node_modules', 'venv', '__pycache__'}
        
        for root, dirs, files in os.walk(repo_path):
            dirs[:] = [d for d in dirs if d not in excluded_dirs]
            for file in files:
                if file.endswith(('.py', '.js', '.ts', '.txt', '.env', '.json', '.yml', '.yaml', '.xml', '.properties')):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            for line_number, line in enumerate(f, 1):
                                for pattern, description in sensitive_data_patterns:
                                    if re.search(pattern, line):
                                        findings.append({
                                            'file': file_path,
                                            'line': line_number,
                                            'pattern': description,
                                            'content': line.strip()
                                        })
                                        break  # Avoid multiple detections of the same line
                    except Exception as e:
                        self.logger.warning(f"Error reading file {file_path}: {str(e)}")
        
        self.logger.info(f"Scan completed. Found {len(findings)} potential issues.")
        return findings

    def enforce_branch_protection_rules(self, repo_name: str, branch_name: str = 'main') -> bool:
        """
        Enforces branch protection rules on the specified branch of a GitHub repository using the GitHub API.
        
        Args:
            repo_name (str): The name of the GitHub repository.
            branch_name (str): The name of the branch to enforce protection rules on. Defaults to 'main'.
        
        Returns:
            bool: True if enforcement was successful, False otherwise.
        """
        try:
            repo = self.github.get_repo(repo_name)
            branch = repo.get_branch(branch_name)
            
            branch.edit_protection(
                required_approving_review_count=1,
                enforce_admins=True,
                dismiss_stale_reviews=True,
                require_code_owner_reviews=True,
                required_status_checks={
                    "strict": True,
                    "contexts": ["continuous-integration/travis-ci"]
                },
                restrictions=None
            )
            
            self.logger.info(f"Branch protection rules enforced on {branch_name} in {repo_name}")
            return True
        except GithubException as e:
            self.logger.error(f"Failed to enforce branch protection rules: {str(e)}")
            return False

    def audit_repository_access(self, repo_name: str) -> Dict[str, List[str]]:
        """
        Audits and reports on who has access to the specified GitHub repository using the GitHub API.
        
        Args:
            repo_name (str): The name of the GitHub repository.
        
        Returns:
            Dict[str, List[str]]: A dictionary with user roles as keys and lists of usernames with that role as values.
        """
        try:
            repo = self.github.get_repo(repo_name)
            collaborators = repo.get_collaborators()
            
            access_audit = {
                "admin": [],
                "write": [],
                "read": [],
                "none": []
            }
            
            for collaborator in collaborators:
                permissions = repo.get_collaborator_permission(collaborator)
                access_audit[permissions].append(collaborator.login)
            
            self.logger.info(f"Access audit completed for {repo_name}")
            return access_audit
        except GithubException as e:
            self.logger.error(f"Failed to audit repository access: {str(e)}")
            return {}

    def check_security_vulnerabilities(self, repo_name: str) -> List[Dict[str, Any]]:
        """
        Checks for security vulnerabilities in the repository using GitHub's security features.
        
        Args:
            repo_name (str): The name of the GitHub repository.
        
        Returns:
            List[Dict[str, Any]]: A list of dictionaries containing vulnerability information.
        """
        try:
            repo = self.github.get_repo(repo_name)
            vulnerabilities = repo.get_vulnerability_alert()
            
            vulnerability_info = []
            for vuln in vulnerabilities:
                vulnerability_info.append({
                    "package": vuln.package.name,
                    "severity": vuln.severity,
                    "description": vuln.description,
                    "affected_range": vuln.affected_range,
                    "fixed_in": vuln.fixed_in
                })
            
            self.logger.info(f"Vulnerability check completed for {repo_name}")
            return vulnerability_info
        except GithubException as e:
            self.logger.error(f"Failed to check security vulnerabilities: {str(e)}")
            return []

    def enable_security_features(self, repo_name: str) -> bool:
        """
        Enables various security features for the repository.
        
        Args:
            repo_name (str): The name of the GitHub repository.
        
        Returns:
            bool: True if all features were enabled successfully, False otherwise.
        """
        try:
            repo = self.github.get_repo(repo_name)
            
            # Enable Dependabot alerts
            repo.enable_vulnerability_alert()
            
            # Enable automated security fixes
            repo.enable_automated_security_fixes()
            
            # Enable code scanning alerts (requires GitHub Advanced Security)
            if repo.get_license() and repo.get_license().spdx_id != "UNLICENSED":
                repo.enable_code_scanning_default_setup()
            
            self.logger.info(f"Security features enabled for {repo_name}")
            return True
        except GithubException as e:
            self.logger.error(f"Failed to enable security features: {str(e)}")
            return False

    def generate_security_report(self, repo_name: str) -> Dict[str, Any]:
        """
        Generates a comprehensive security report for the repository.
        
        Args:
            repo_name (str): The name of the GitHub repository.
        
        Returns:
            Dict[str, Any]: A dictionary containing various security metrics and information.
        """
        report = {}
        
        # Gather all security-related information
        report['sensitive_data'] = self.scan_for_sensitive_data(repo_name)
        report['access_audit'] = self.audit_repository_access(repo_name)
        report['vulnerabilities'] = self.check_security_vulnerabilities(repo_name)
        
        # Add branch protection status
        repo = self.github.get_repo(repo_name)
        default_branch = repo.default_branch
        branch = repo.get_branch(default_branch)
        report['branch_protection'] = branch.protected
        
        # Add security feature status
        report['security_features'] = {
            'dependabot_alerts': repo.get_vulnerability_alert(),
            'automated_security_fixes': repo.get_automated_security_fixes(),
            'code_scanning': repo.get_code_scanning_default_setup()
        }
        
        self.logger.info(f"Security report generated for {repo_name}")
        return report

# Example usage:
# security = GitHubRepoSecurity()
# report = security.generate_security_report("owner/repo")
# print(json.dumps(report, indent=2))
