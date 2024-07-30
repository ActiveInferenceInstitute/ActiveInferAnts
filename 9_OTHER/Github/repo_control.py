import os
from collections import defaultdict
from typing import Dict, Tuple

def summarize_repo(directory: str = ".", depth: int = 2) -> None:
    """
    Summarizes and prints the statistics of folders, files, and size for each repository within the specified directory, 
    consolidating all statistics under .git, 2 levels deep by default.
    
    Parameters:
    directory (str): The root directory to search for cloned repositories. Defaults to the current directory.
    depth (int): The depth to search for statistics under each repository's .git directory.
    """

    def calculate_size(path: str) -> int:
        """
        Calculates the total size of files in a directory.
        
        Parameters:
        path (str): The path of the directory or file.
        
        Returns:
        int: The total size of the directory or file in bytes.
        """
        if os.path.isfile(path):
            return os.path.getsize(path)
        total_size = 0
        for root, dirs, files in os.walk(path):
            total_size += sum(os.path.getsize(os.path.join(root, name)) for name in files)
        return total_size

    def gather_stats(directory: str, stats: Dict[str, Dict[str, int]], depth: int, current_depth: int = 0) -> None:
        """
        Recursively gathers statistics for each repository, consolidating under .git, up to 2 levels deep by default.
        
        Parameters:
        directory (str): The current directory being searched.
        stats (Dict[str, Dict[str, int]]): The compiled statistics of repositories.
        depth (int): The depth to search for statistics under each repository's .git directory.
        current_depth (int): The current depth of the search.
        """
        for entry in os.scandir(directory):
            if entry.is_dir(follow_symlinks=False):
                if '.git' in os.listdir(entry.path):
                    repo_name = entry.name
                    repo_path = entry.path
                    stats[repo_name]["total_size"] = calculate_size(repo_path)
                    for root, dirs, files in os.walk(repo_path):
                        if root.count(os.sep) - repo_path.count(os.sep) <= depth:
                            stats[repo_name]["file_count"] += len(files)
                elif current_depth < depth:
                    gather_stats(entry.path, stats, depth, current_depth + 1)

    stats = defaultdict(lambda: {"file_count": 0, "total_size": 0})
    gather_stats(directory, stats, depth)

    print(f"Repository Statistics Summary (consolidated under .git, up to {depth} levels deep):")
    total_files, total_size = 0, 0
    for repo, details in stats.items():
        total_files += details["file_count"]
        total_size += details["total_size"]
        size_in_mb = details["total_size"] / (1024**2)
        print(f"- {repo}: {details['file_count']} files, {size_in_mb:.2f} MB")
    
    print(f"\nTotal across all repositories: {total_files} files, {total_size / (1024**2):.2f} MB")

if __name__ == "__main__":
    root_dir = input("Enter the root directory to search for cloned repositories: ") or "."
    depth = int(input("Enter the depth to search under each repository's .git directory (default is 2): ") or 2)
    summarize_repo(root_dir, depth)

