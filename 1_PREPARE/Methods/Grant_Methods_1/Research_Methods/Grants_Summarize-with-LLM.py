import os
import openai
import logging
import time
from typing import List

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Load API key from LLM_keys.key file
api_key_path = os.path.join(os.path.dirname(__file__), 'LLM_keys.key')
OPENAI_API_KEY = None
with open(api_key_path, 'r') as key_file:
    for line in key_file:
        if line.startswith("OPENAI_API_KEY"):
            OPENAI_API_KEY = line.split('=')[1].strip().strip('"')
            break

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found in LLM_keys.key file")

class GrantSummarizer:
    def __init__(self, api_key: str = OPENAI_API_KEY, output_dir: str = "./Writing_Outputs/Summarized_Grants/"):
        self.api_key = api_key
        self.output_dir = output_dir
        self.model = "gpt-4o-mini"
        openai.api_key = self.api_key
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
        logging.info(f"Output directory set to '{self.output_dir}'")

    def send_request_to_openai(self, content: str) -> str:
        logging.info(f"Sending request to OpenAI using {self.model}...")
        start_time = time.time()
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are an expert assistant specialized in summarizing complex grant applications."},
                {"role": "user", "content": f"Please provide a detailed and well-structured summary of the following grant application. Ensure that all key information, including semantics, syntax, requirements, context, emphases, and topics, is retained. The summary should be between 750 and 1500 words:\n\n{content}"}
            ],
            max_tokens=16000,
            n=1,
            temperature=0.2
        )
        end_time = time.time()
        generation_time = end_time - start_time
        logging.info(f"Received response from OpenAI ({self.model}). Generation time: {generation_time:.2f} seconds")
        print(f"Generation time for current request: {generation_time:.2f} seconds")
        return response.choices[0].message['content'].strip()

    def summarize_grants(self):
        agencies_dir = "../Grants/"
        logging.info(f"Starting to summarize grants in directory: {agencies_dir}")
        for agency in os.listdir(agencies_dir):
            agency_path = os.path.join(agencies_dir, agency)
            if os.path.isdir(agency_path):
                logging.info(f"Processing agency: {agency}")
                for root, _, files in os.walk(agency_path):
                    for file in files:
                        if file.endswith(".md"):
                            logging.info(f"Processing grant file: {file} in agency: {agency}")
                            with open(os.path.join(root, file), "r") as f:
                                content = f.read()
                            logging.info(f"Sending content to OpenAI for file: {file}")
                            summary = self.send_request_to_openai(content)
                            logging.info(f"Received summary for grant file: {file}")
                            self.save_summary(summary, agency, root, file)
        logging.info("Completed summarizing all grants.")

    def save_summary(self, summary: str, agency: str, root: str, file: str):
        relative_path = os.path.relpath(root, f"../Grants/{agency}/")
        output_dir = os.path.join(self.output_dir, agency, relative_path)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        output_filename = f"LLM_Summary_{file}"
        output_file = os.path.join(output_dir, output_filename)
        logging.info(f"Saving summary to file: {output_file}")
        with open(output_file, "w") as f:
            f.write(summary)
        logging.info(f"Grant summary saved to '{output_file}'")

if __name__ == "__main__":
    logging.info("Initiating grant summarization program...")
    grant_summarizer = GrantSummarizer()
    logging.info("GrantSummarizer instance created")
    grant_summarizer.summarize_grants()
    logging.info("Grant summarization program completed.")