import subprocess
import importlib
import logging
import os
import sys
import inspect

logging.basicConfig(level=logging.INFO)

def clone_pymdp_repo(repo_url='https://github.com/infer-actively/pymdp'):
    """
    Clone the pymdp repository if it doesn't exist.
    """
    repo_name = repo_url.split('/')[-1]
    if not os.path.exists(repo_name):
        try:
            subprocess.run(['git', 'clone', repo_url], check=True)
            logging.info(f"Successfully cloned repository from {repo_url}")
        except subprocess.CalledProcessError as e:
            logging.error(f"Error cloning repository: {e}")
            return False
    else:
        logging.info(f"Repository {repo_name} already exists. Skipping clone.")
    return True

def list_pymdp_methods():
    """
    List all methods available in the specified pymdp submodules,
    including their arguments and docstrings.

    Returns:
    - methods (list): A list of dictionaries containing method information.
    """
    pymdp_path = os.path.join(os.getcwd(), 'pymdp')
    if pymdp_path not in sys.path:
        sys.path.insert(0, pymdp_path)

    submodules = [
        'agent', 'algos', 'control', 'inference', 
        'learning', 'likelihoods', 'maths', 'task', 'utils'
    ]

    methods = []
    for submodule in submodules:
        try:
            module = importlib.import_module(f'pymdp.{submodule}')
            for attr_name in dir(module):
                attr = getattr(module, attr_name)
                if callable(attr) and not attr_name.startswith('_'):
                    try:
                        method_info = {
                            'name': f"pymdp.{submodule}.{attr_name}",
                            'args': str(inspect.signature(attr)),
                            'docstring': inspect.getdoc(attr)
                        }
                        methods.append(method_info)
                    except ValueError:
                        logging.warning(f"Skipping method without valid signature: pymdp.{submodule}.{attr_name}")
        except ModuleNotFoundError as e:
            logging.warning(f"Module pymdp.{submodule} not found: {e}")

    logging.info(f"Retrieved information for {len(methods)} methods from pymdp package")
    return methods

def write_methods_to_file(methods, filename='PyMDP_methods.md'):
    """
    Write the methods information to a markdown file.
    """
    with open(filename, 'w') as f:
        f.write("# PyMDP Methods\n\n")
        for method in methods:
            f.write(f"## {method['name']}\n\n")
            f.write(f"**Arguments:** {method['args']}\n\n")
            if method['docstring']:
                f.write(f"**Description:**\n{method['docstring']}\n\n")
            f.write("---\n\n")
    logging.info(f"Methods with details have been written to {filename}")

if __name__ == "__main__":
    if clone_pymdp_repo():
        methods = list_pymdp_methods()
        if methods:
            write_methods_to_file(methods)
        else:
            logging.error("Failed to retrieve methods")
            sys.exit(1)
    else:
        logging.error("Failed to clone repository")
        sys.exit(1)