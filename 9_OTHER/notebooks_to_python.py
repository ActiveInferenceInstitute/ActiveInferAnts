import os
import nbformat
from nbconvert import PythonExporter, MarkdownExporter
from collections import defaultdict

class NotebookConverter:
    """
    A class to convert Jupyter Notebooks to either Python scripts or Markdown files.
    """
    
    def __init__(self, output_format: str = 'script'):
        self.output_format = output_format
        self.exporter = PythonExporter() if output_format == 'script' else MarkdownExporter()
    
    def convert(self, notebook_path: str) -> str:
        """
        Converts a single Jupyter Notebook to the specified format.
        
        Args:
            notebook_path (str): The path to the Jupyter Notebook.
        
        Returns:
            str: The path to the converted notebook.
        """
        output_path = notebook_path.replace(".ipynb", f".{self._get_extension()}")
        nb_node = self._load_notebook(notebook_path)
        output_content = self._export_notebook(nb_node)
        self._write_output(output_path, output_content)
        return output_path
    
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

class DirectoryNotebookConverter(NotebookConverter):
    """
    A class to convert all Jupyter Notebooks within a directory (and subdirectories) to the specified format.
    """
    
    def convert_directory(self, directory: str) -> None:
        """
        Converts all Jupyter Notebooks in the specified directory to the specified format.
        
        Args:
            directory (str): The root directory to search for Jupyter Notebooks.
        """
        conversion_summary = defaultdict(int)
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(".ipynb"):
                    notebook_path = os.path.join(root, file)
                    output_path = self.convert(notebook_path)
                    repo_name = self._extract_repo_name(root)
                    conversion_summary[repo_name] += 1
                    print(f"Converted {notebook_path} to {output_path}.")
            self._print_directory_summary(root, conversion_summary)
        self._print_overall_summary(conversion_summary)
    
    def _extract_repo_name(self, path: str) -> str:
        return path.split(os.sep)[-1]
    
    def _print_directory_summary(self, root: str, conversion_summary: defaultdict):
        repo_name = self._extract_repo_name(root)
        if repo_name in conversion_summary:
            print(f"Finished converting notebooks in {repo_name}. Total: {conversion_summary[repo_name]} notebook(s).")
    
    def _print_overall_summary(self, conversion_summary: defaultdict):
        print("\nOverall Conversion Summary per Repository:")
        for repo, count in conversion_summary.items():
            print(f"{repo}: {count} notebook(s) converted.")

if __name__ == "__main__":
    target_directory = input("Enter the target directory (default is 'repos/'): ").strip() or "repos/"
    output_format = input("Enter the output format ('script' for Python scripts or 'markdown' for Markdown files, default is 'script'): ").strip() or "script"
    converter = DirectoryNotebookConverter(output_format)
    converter.convert_directory(target_directory)

