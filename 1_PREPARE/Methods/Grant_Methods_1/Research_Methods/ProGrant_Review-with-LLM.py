import os
import openai
import logging
import time
from typing import List
import matplotlib.pyplot as plt

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

class GrantReviewer:
    def __init__(self, api_key: str = OPENAI_API_KEY, input_dir: str = "./Writing_Outputs/Written_ProGrants/", output_dir: str = "./Writing_Outputs/ProGrant_Reviews/"):
        self.api_key = api_key
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.model = "gpt-4o-mini"
        openai.api_key = self.api_key
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
        logging.info(f"Output directory set to '{self.output_dir}'")

    def send_request_to_openai(self, grant_content: str) -> str:
        logging.info(f"Sending request to OpenAI using {self.model}...")
        start_time = time.time()
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a professional grant review panel. Provide a comprehensive review of the grant proposal in light of the program goals."},
                {"role": "user", "content": f"Please review the following grant proposal:\n\n{grant_content}"}
            ],
            max_tokens=16000,
            n=1,
            temperature=0.3
        )
        end_time = time.time()
        generation_time = end_time - start_time
        logging.info(f"Received response from OpenAI ({self.model}). Generation time: {generation_time:.2f} seconds")
        print(f"Generation time for current request: {generation_time:.2f} seconds")
        return response.choices[0].message['content'].strip()

    def process_grants(self):
        grants = [f for f in os.listdir(self.input_dir) if f.endswith(".md")]
        
        for grant_file in grants:
            logging.info(f"Processing grant file: {grant_file}")
            output_filename = f"Review_{grant_file}"
            output_file = os.path.join(self.output_dir, output_filename)
            
            if os.path.exists(output_file):
                logging.info(f"Review file '{output_file}' already exists. Skipping.")
                continue
            
            with open(os.path.join(self.input_dir, grant_file), "r") as f:
                grant_content = f.read()
            
            logging.info(f"Sending grant to OpenAI for review: {grant_file}")
            start_time = time.time()
            review = self.send_request_to_openai(grant_content)
            end_time = time.time()
            generation_time = end_time - start_time
            logging.info(f"Received review for grant file: {grant_file}. Generation time: {generation_time:.2f} seconds")
            print(f"Generation time for {grant_file}: {generation_time:.2f} seconds")
            self.save_review(review, grant_file)

    def save_review(self, review: str, grant_file: str):
        output_filename = f"Review_{grant_file}"
        output_file = os.path.join(self.output_dir, output_filename)
        logging.info(f"Saving review to file: {output_file}")
        with open(output_file, "w") as f:
            f.write(f"Review generated using {self.model}\n\n")
            f.write(review)
        logging.info(f"Grant review saved to '{output_file}'")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
    logging.info("Initiating grant review program...")
    grant_reviewer = GrantReviewer()
    logging.info("GrantReviewer instance created")
    grant_reviewer.process_grants()
    logging.info("Grant review program completed.")