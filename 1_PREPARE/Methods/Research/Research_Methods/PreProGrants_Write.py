import os
import random
from typing import List, Dict, Optional
import logging
from dotenv import load_dotenv
import itertools

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class GrantWriter:
    def __init__(self):
        self.output_dir = "./Writing_Outputs/Grant_Prompts/"
        os.makedirs(self.output_dir, exist_ok=True)

    def write_grants(self):
        logging.info("Initiating grant writing process...")
        
        entities = self.get_all_entities()
        grant_calls = self.get_all_grant_calls()
        catechisms = self.get_all_catechisms()

        if not grant_calls:
            logging.error("No valid grant calls found. Aborting grant writing process.")
            return

        for entity, grant_call, catechism in itertools.product(entities, grant_calls, catechisms):
            entity_content = self.load_entity_content(entity)
            catechism_content = self.load_catechism_content(catechism)
            grant_call_content = self.load_grant_call_content(grant_call)

            prompt = self.generate_grant(entity_content, catechism_content, grant_call_content)
            self.save_prompt(prompt, entity, grant_call, catechism)

    def get_all_entities(self) -> List[str]:
        entities_dir = "../Entities/"
        entities = [d for d in os.listdir(entities_dir) if os.path.isdir(os.path.join(entities_dir, d))]
        logging.info(f"Discovered {len(entities)} potential entities:")
        for i, entity in enumerate(entities, 1):
            logging.info(f"  {i}. {entity}")
        return entities

    def get_all_grant_calls(self) -> List[str]:
        grants_dir = "../Grants/"
        grant_calls = []
        for root, dirs, files in os.walk(grants_dir):
            for file in files:
                if file.endswith(".md"):
                    grant_calls.append(os.path.join(os.path.relpath(root, grants_dir), file))
        
        if not grant_calls:
            logging.error("No grant calls found.")
            return []
        
        logging.info(f"Discovered {len(grant_calls)} grant calls")
        return grant_calls

    def get_all_catechisms(self) -> List[str]:
        catechisms_dir = "../Catechisms/"
        catechisms = [f for f in os.listdir(catechisms_dir) if f.endswith(".md")]
        logging.info(f"Available catechisms: {len(catechisms)}")
        for i, catechism in enumerate(catechisms, 1):
            logging.info(f"  {i}. {catechism}")
        return catechisms

    def load_entity_content(self, entity: str) -> str:
        entity_dir = os.path.join("../Entities/", entity)
        entity_files = [f for f in os.listdir(entity_dir) if f.endswith(".py")]
        logging.info(f"Loading {len(entity_files)} files for entity {entity}:")
        entity_content = ""
        for i, file in enumerate(entity_files, 1):
            with open(os.path.join(entity_dir, file), "r") as f:
                content = f.read()
                entity_content += content + "\n\n"
            logging.info(f"  {i}. {file} ({len(content)} characters)")
        logging.info(f"Loaded {len(entity_content)} characters for entity {entity}")
        return entity_content

    def load_catechism_content(self, catechism: str) -> str:
        with open(f"../Catechisms/{catechism}", "r") as f:
            content = f.read()
        logging.info(f"Loaded catechism {catechism}: {len(content)} characters")
        return content

    def load_grant_call_content(self, grant_call: str) -> str:
        with open(f"../Grants/{grant_call}", "r") as f:
            content = f.read()
        logging.info(f"Loaded grant call {grant_call}: {len(content)} characters")
        return content

    def generate_grant(self, entity_content: str, catechism_content: str, grant_call_content: str) -> str:
        logging.info("Preparing prompt for grant generation...")
        prompt = f"""
        As an expert grant writer, craft a compelling grant proposal that authentically represents the perspective of the given entity while addressing the specific requirements of the grant call. Your task is to answer the catechism questions comprehensively, ensuring alignment with the grant agency's objectives and the entity's unique capabilities.

        Entity (Technical/Perspectival Skills and Capacities):
        {entity_content}

        Catechism (Comprehensive Project Description):
        {catechism_content}

        Grant Call (Agency Requirements):
        {grant_call_content}

        Instructions:
        1. Carefully analyze the entity's content to understand their worldview, methodology, and unique perspective.
        2. Thoroughly review the grant call to identify all requirements, priorities, and evaluation criteria.
        3. For each question in the catechism:
           a. Provide a comprehensive answer that directly addresses the question.
           b. Incorporate relevant aspects of the entity's expertise and viewpoint.
           c. Align the response with the grant call requirements and agency objectives.
           d. Use specific language, terminology, and concepts from the entity's content to maintain authenticity.
        4. Ensure that the proposal:
           a. Demonstrates a deep understanding of the grant agency's goals and priorities.
           b. Highlights the unique value proposition of the entity in relation to the grant objectives.
           c. Presents quantifiable outcomes and measurable impacts wherever possible.
           d. Addresses potential challenges and provides mitigation strategies.
           e. Maintains a cohesive narrative throughout, connecting the entity's capabilities to the project goals and agency requirements.

        Your proposal should be well-structured, data-driven, and persuasive, showcasing the innovative potential of the project while remaining true to the entity's perspective and the grant agency's expectations.
        """

        logging.info("Generated grant proposal prompt")
        return prompt

    def save_prompt(self, prompt: str, entity: str, grant_call: str, catechism: str):
        output_filename = f"{entity}_by_{os.path.basename(grant_call)}_by_{os.path.splitext(catechism)[0]}_prompt.md"
        output_file = os.path.join(self.output_dir, output_filename)
        with open(output_file, "w") as f:
            f.write(prompt)
        logging.info(f"Grant proposal prompt saved to '{output_file}'")

if __name__ == "__main__":
    logging.info("Initiating grant writing program...")
    grant_writer = GrantWriter()
    grant_writer.write_grants()
    logging.info("Grant writing program completed.")