import os
import nbformat
from nbconvert import PythonExporter, MarkdownExporter
from collections import defaultdict
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
from typing import Dict, List, Tuple, Optional
import argparse

class NotebookConverter:
    # A class to convert Jupyter Notebooks to either Python scripts or Markdown files.
    
    def __init__(self, output_format: str = 'script', logger: Optional[logging.Logger] = None):
        self.output_format = output_format
        self.exporter = PythonExporter() if output_format == 'script' else MarkdownExporter()
        self.logger = logger or self._setup_logger()
    
    def convert(self, notebook_path: str) -> Tuple[str, bool]:
        # Converts a single Jupyter Notebook to the specified format.
        # 
        # Args:
        #     notebook_path (str): The path to the Jupyter Notebook.
        # 
        # Returns:
        #     Tuple[str, bool]: The path to the converted notebook and a boolean indicating success.
        try:
            output_path = notebook_path.replace(".ipynb", f".{self._get_extension()}")
            nb_node = self._load_notebook(notebook_path)
            output_content = self._export_notebook(nb_node)
            self._write_output(output_path, output_content)
            return output_path, True
        except Exception as e:
            self.logger.error(f"Error converting {notebook_path}: {str(e)}")
            return notebook_path, False
    
    def _get_extension(self) -> str:
        return "py" if self.output_format == 'script' else "md"
    
    def _load_notebook(self, notebook_path: str):
        with open(notebook_path, 'r', encoding='utf-8') as nb_file:
            return nbformat.read(nb_file, as_version=4)
    
    def _export_notebook(self, nb_node):
        output_content, _ = self.exporter.from_notebook_node(nb_node)
        return output_content
    
    def _write_output(self, output_path: str, output_content: str):
        with open(output_path, 'w', encoding='utf-8') as output_file:
            output_file.write(output_content)
    
    def _setup_logger(self) -> logging.Logger:
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger

class DirectoryNotebookConverter(NotebookConverter):
    # A class to convert all Jupyter Notebooks within a directory (and subdirectories) to the specified format.
    
    def __init__(self, output_format: str = 'script', max_workers: int = 4, logger: Optional[logging.Logger] = None):
        super().__init__(output_format, logger)
        self.max_workers = max_workers
    
    def convert_directory(self, directory: str) -> Dict[str, Dict[str, int]]:
        # Converts all Jupyter Notebooks in the specified directory to the specified format.
        # 
        # Args:
        #     directory (str): The root directory to search for Jupyter Notebooks.
        # 
        # Returns:
        #     Dict[str, Dict[str, int]]: A summary of conversions per repository.
        notebook_paths = self._find_notebooks(directory)
        conversion_summary = self._convert_notebooks(notebook_paths)
        self._print_overall_summary(conversion_summary)
        return conversion_summary
    
    def _find_notebooks(self, directory: str) -> List[str]:
        notebook_paths = []
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(".ipynb"):
                    notebook_paths.append(os.path.join(root, file))
        return notebook_paths
    
    def _convert_notebooks(self, notebook_paths: List[str]) -> Dict[str, Dict[str, int]]:
        conversion_summary = defaultdict(lambda: {'success': 0, 'failure': 0})
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            future_to_path = {executor.submit(self.convert, path): path for path in notebook_paths}
            for future in tqdm(as_completed(future_to_path), total=len(notebook_paths), desc="Converting notebooks"):
                path = future_to_path[future]
                repo_name = self._extract_repo_name(path)
                output_path, success = future.result()
                if success:
                    conversion_summary[repo_name]['success'] += 1
                    self.logger.info(f"Converted {path} to {output_path}.")
                else:
                    conversion_summary[repo_name]['failure'] += 1
                    self.logger.warning(f"Failed to convert {path}.")
        return conversion_summary
    
    def _extract_repo_name(self, path: str) -> str:
        return os.path.basename(os.path.dirname(path))
    
    def _print_overall_summary(self, conversion_summary: Dict[str, Dict[str, int]]):
        self.logger.info("\nOverall Conversion Summary per Repository:")
        for repo, counts in conversion_summary.items():
            self.logger.info(f"{repo}: {counts['success']} notebook(s) converted successfully, {counts['failure']} failed.")

def parse_arguments():
    parser = argparse.ArgumentParser(description="Convert Jupyter Notebooks to Python scripts or Markdown files.")
    parser.add_argument("directory", nargs="?", default="repos/", help="Target directory containing notebooks (default: repos/)")
    parser.add_argument("--format", choices=["script", "markdown"], default="script", help="Output format (default: script)")
    parser.add_argument("--workers", type=int, default=4, help="Number of worker threads (default: 4)")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    converter = DirectoryNotebookConverter(output_format=args.format, max_workers=args.workers)
    converter.convert_directory(args.directory)
