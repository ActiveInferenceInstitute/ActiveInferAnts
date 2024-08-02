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

class GrantWriter:
    def __init__(self, api_key: str = OPENAI_API_KEY, output_dir: str = "./Writing_Outputs/Written_Grants/", max_prompt_words: int = 10000):
        self.api_key = api_key
        self.output_dir = output_dir
        self.max_prompt_words = max_prompt_words
        self.model = "gpt-4o-mini" 
        openai.api_key = self.api_key
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
        logging.info(f"Output directory set to '{self.output_dir}'")

    def send_request_to_openai(self, prompt: str) -> str:
        logging.info(f"Sending request to OpenAI using {self.model}...")
        start_time = time.time()
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant that writes grant proposals."},
                {"role": "user", "content": prompt}
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
        prompt_dir = "./Writing_Outputs/Grant_Prompts/"
        prompts = [f for f in os.listdir(prompt_dir) if f.endswith(".md")]
        
        # Print histogram and ask for confirmation
        if not self.print_word_length_histogram(prompt_dir):
            logging.info("User chose to quit. Exiting program.")
            return
        
        for prompt_file in prompts:
            logging.info(f"Processing prompt file: {prompt_file}")
            output_filename = f"{os.path.splitext(prompt_file)[0]}_{self.model}_output.md"
            output_file = os.path.join(self.output_dir, output_filename)
            
            if os.path.exists(output_file):
                logging.info(f"Output file '{output_file}' already exists. Skipping.")
                continue
            
            with open(os.path.join(prompt_dir, prompt_file), "r") as f:
                prompt = f.read()
            word_count = len(prompt.split())
            if word_count <= self.max_prompt_words:
                logging.info(f"Sending prompt to OpenAI for file: {prompt_file}")
                start_time = time.time()
                response = self.send_request_to_openai(prompt)
                end_time = time.time()
                generation_time = end_time - start_time
                logging.info(f"Received response for prompt file: {prompt_file}. Generation time: {generation_time:.2f} seconds")
                print(f"Generation time for {prompt_file}: {generation_time:.2f} seconds")
                self.save_output(response, prompt_file)
            else:
                logging.warning(f"Prompt file {prompt_file} exceeds the maximum word limit. Word count: {word_count}")

    def save_output(self, output: str, prompt_file: str):
        output_filename = f"{os.path.splitext(prompt_file)[0]}_{self.model}_output.md"
        output_file = os.path.join(self.output_dir, output_filename)
        logging.info(f"Saving output to file: {output_file}")
        with open(output_file, "w") as f:
            f.write(f"Generated using {self.model}\n\n")
            f.write(output)
        logging.info(f"Grant proposal output saved to '{output_file}'")

    def print_word_length_histogram(self, prompt_dir: str) -> bool:
        word_counts = []
        for filename in os.listdir(prompt_dir):
            if filename.endswith(".md"):
                with open(os.path.join(prompt_dir, filename), 'r') as f:
                    word_counts.append(len(f.read().split()))
        
        plt.figure(figsize=(10, 6))
        plt.hist(word_counts, bins=20, edgecolor='black')
        plt.title('Histogram of Word Counts in Input Files')
        plt.xlabel('Word Count')
        plt.ylabel('Frequency')
        plt.savefig('word_count_histogram.png')
        plt.close()
        
        print("Word count histogram has been saved as 'word_count_histogram.png'")
        print(f"Word count statistics:")
        print(f"Minimum: {min(word_counts)}")
        print(f"Maximum: {max(word_counts)}")
        print(f"Average: {sum(word_counts) / len(word_counts):.2f}")
        
        # Calculate documents above and below max_prompt_words & Output to terminal
        docs_above = sum(1 for count in word_counts if count > self.max_prompt_words)
        docs_below = sum(1 for count in word_counts if count <= self.max_prompt_words)
        print(f"Documents above {self.max_prompt_words} words: {docs_above}")
        print(f"Documents below or equal to {self.max_prompt_words} words: {docs_below}")
        
        while True:
            user_input = input("Do you want to continue? (Yes/No): ").lower()
            if user_input in ['yes', 'y']:
                return True
            elif user_input in ['no', 'n']:
                return False
            else:
                print("Invalid input. Please enter Yes or No.")

if __name__ == "__main__":
    logging.info("Initiating grant writing program...")
    grant_writer = GrantWriter()
    logging.info("GrantWriter instance created")
    grant_writer.process_grants()
    logging.info("Grant writing program completed.")