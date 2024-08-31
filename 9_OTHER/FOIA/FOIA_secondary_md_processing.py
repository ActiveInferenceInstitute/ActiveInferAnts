import os
import re
import logging
from pathlib import Path
import markdown
import sys

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

try:
    from bs4 import BeautifulSoup
except ImportError:
    logging.error("BeautifulSoup4 is not installed. Installing it now...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "beautifulsoup4"])
    from bs4 import BeautifulSoup

def process_markdown(content):
    # Convert markdown to HTML
    html = markdown.markdown(content)
    soup = BeautifulSoup(html, 'html.parser')

    # Remove redundant whitespace
    for tag in soup.find_all(text=True):
        if tag.parent.name not in ['pre', 'code']:
            tag.replace_with(re.sub(r'\s+', ' ', tag.strip()))

    # Simplify headers
    for header in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
        header.string = header.text.strip()

    # Convert back to markdown
    processed_content = soup.prettify()
    processed_content = re.sub(r'<[^>]+>', '', processed_content)
    processed_content = re.sub(r'\n\s*\n', '\n\n', processed_content)

    return processed_content.strip()

def process_files(input_dir, output_dir):
    for root, _, files in os.walk(input_dir):
        for file in files:
            if file.endswith('.md'):
                input_path = Path(root) / file
                relative_path = input_path.relative_to(input_dir)
                output_path = Path(output_dir) / relative_path

                logging.info(f"Processing: {input_path}")

                with open(input_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                processed_content = process_markdown(content)

                output_path.parent.mkdir(parents=True, exist_ok=True)
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(processed_content)

                logging.info(f"Saved processed file: {output_path}")

if __name__ == "__main__":
    input_directory = "./FOIA_Markdown/"
    output_directory = "./FOIA_Secondary_Markdowns/"

    logging.info("Starting secondary markdown processing")
    process_files(input_directory, output_directory)
    logging.info("Secondary markdown processing completed")
