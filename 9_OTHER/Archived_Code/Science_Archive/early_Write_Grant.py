import os
import random
from typing import List, Dict, Optional
import logging
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class GrantWriter:
    def __init__(self):
        self.output_dir = "./Writing_Outputs/Grant_Prompts/"
        os.makedirs(self.output_dir, exist_ok=True)

    def write_grant(self) -> Optional[str]:
        logging.info("Initiating grant writing process...")
        
        entity = self.select_entity()
        grant_call = self.select_grant_call()
        catechism = self.select_catechism()

        if not grant_call:
            logging.error("No valid grant call found. Aborting grant writing process.")
            return None

        entity_content = self.load_entity_content(entity)
        catechism_content = self.load_catechism_content(catechism)
        grant_call_content = self.load_grant_call_content(grant_call)

        prompt = self.generate_grant(entity_content, catechism_content, grant_call_content)
        return prompt, entity, grant_call, catechism

    def select_entity(self) -> str:
        entities_dir = "../Entities/"
        entities = [d for d in os.listdir(entities_dir) if os.path.isdir(os.path.join(entities_dir, d))]
        logging.info(f"Discovered {len(entities)} potential entities:")
        for i, entity in enumerate(entities, 1):
            logging.info(f"  {i}. {entity}")
        selected = random.choice(entities)
        logging.info(f"\nSelected entity for proposal: {selected}")
        return selected

    def select_grant_call(self) -> Optional[str]:
        grants_dir = "../Grants/"
        grant_calls = []
        for root, dirs, files in os.walk(grants_dir):
            for file in files:
                if file.endswith(".md"):
                    grant_calls.append(os.path.join(os.path.relpath(root, grants_dir), file))
        
        if not grant_calls:
            logging.error("No grant calls found.")
            return None
        
        selected = random.choice(grant_calls)
        logging.info(f"Selected grant call: {selected}")
        return selected

    def select_catechism(self) -> str:
        catechisms_dir = "../Catechisms/"
        catechisms = [f for f in os.listdir(catechisms_dir) if f.endswith(".md")]
        logging.info(f"Available catechisms: {len(catechisms)}")
        for i, catechism in enumerate(catechisms, 1):
            logging.info(f"  {i}. {catechism}")
        selected = random.choice(catechisms)
        logging.info(f"\nSelected catechism framework: {selected}")
        return selected

    def load_entities_content(self, entities: List[str]) -> Dict[str, str]:
        entities_content = {}
        for entity in entities:
            entity_dir = os.path.join("../Entities/", entity)
            entity_files = [f for f in os.listdir(entity_dir) if f.endswith(".py")]
            logging.info(f"Loading {len(entity_files)} files for entity {entity}:")
            entity_content = ""
            for i, file in enumerate(entity_files, 1):
                with open(os.path.join(entity_dir, file), "r") as f:
                    content = f.read()
                    entity_content += content + "\n\n"
                logging.info(f"  {i}. {file} ({len(content)} characters)")
            entities_content[entity] = entity_content
            logging.info(f"Loaded {len(entity_content)} characters for entity {entity}")
        return entities_content

    def load_catechism_content(self, catechism: str) -> str:
        with open(f"../Catechisms/{catechism}", "r") as f:
            content = f.read()
        logging.info(f"Loaded catechism {catechism}: {len(content)} characters")
        return content

    def load_grant_call_contents(self, grant_calls: List[str]) -> Dict[str, str]:
        grant_call_contents = {}
        for grant_call in grant_calls:
            with open(f"../Grants/{grant_call}", "r") as f:
                content = f.read()
            grant_call_contents[grant_call] = content
            logging.info(f"Loaded grant call {grant_call}: {len(content)} characters")
        return grant_call_contents

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

if __name__ == "__main__":
    logging.info("Initiating grant writing program...")
    grant_writer = GrantWriter()
    result = grant_writer.write_grant()
    
    if result:
        prompt, entity, grant_call, catechism = result
        print("Generated Grant Proposal Prompt:")
        print(prompt)
        
        # Save the proposal to a file in the specified directory
        output_filename = f"{entity}_by_{os.path.basename(grant_call)}_by_{os.path.splitext(catechism)[0]}_prompt.md"
        output_file = os.path.join(grant_writer.output_dir, output_filename)
        with open(output_file, "w") as f:
            f.write(prompt)
        logging.info(f"Grant proposal prompt saved to '{output_file}'")
    else:
        logging.error("Failed to generate grant proposal.")
    
    logging.info("Grant writing program completed.")