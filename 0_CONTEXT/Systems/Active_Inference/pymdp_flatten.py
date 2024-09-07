import os
import ast
import sys

def extract_definitions(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        tree = ast.parse(content)
    
        definitions = []
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
                definitions.append(ast.get_source_segment(content, node))
    
    print(f"  Extracted {len(definitions)} definitions from {file_path}")
    return definitions

def process_package(package_path):
    print(f"Processing package at: {package_path}")

    all_definitions = []
    processed_files = 0

    for root, dirs, files in os.walk(package_path):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                try:
                    definitions = extract_definitions(file_path)
                    all_definitions.extend(definitions)
                    processed_files += 1
                except Exception as e:
                    print(f"Warning: Error processing {file_path}: {str(e)}")

    print(f"Processed {processed_files} files in total.")
    return all_definitions

def main():
    package_path = os.path.join(os.getcwd(), 'pymdp')
    output_file = 'pymdp_all_utils.py'

    if not os.path.exists(package_path):
        print(f"Error: {package_path} does not exist. Make sure pymdp_pull.py has been run.")
        sys.exit(1)

    all_definitions = process_package(package_path)

    if not all_definitions:
        print("No definitions were extracted. Check if the package is empty or if there were errors.")
        sys.exit(1)

    with open(output_file, 'w') as f:
        f.write(f"# All utility functions and classes from pymdp\n\n")
        f.write("\n\n".join(all_definitions))

    print(f"Extracted {len(all_definitions)} definitions to {output_file}")

if __name__ == "__main__":
    main()