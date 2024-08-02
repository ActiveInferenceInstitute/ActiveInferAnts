

Reformat this in concise professional Markdown, do not delete any material. 
Format things in sections, lists, tables, etc., as needed.

------------


The Entity is the person/organization with the technical/perspectival skills and capacities. 
The Agency is the granting body who would prefer to provide the Entity funding, conditional upon qualification and quantification.
The Catechism is a series of questions that the Entity answers comprehensively describing the project, "pitching a fastball" to the Agency in general and the specific grant program 


------------

Analyze the transcripts and related documents in the current folder for [ENTITY_NAME]. Extract key concepts, perspectives, and methodologies discussed by [ENTITY_NAME]. Then, update the ENTITY.py script to reflect this information accurately and concisely. 

I am interested in capturing the perspectives and character of the speaker, not 
Follow these guidelines

1. Maintain the existing structure of functions (e.g., worldview, implications, stances, beliefs).

2. Add or modify dictionary keys and values to capture nuanced views and concepts.

3. Ensure that values (boolean, categorical, quantitative) accurately represent [ENTITY_NAME]'s stance on various topics.

4. Create new functions or classes if necessary to represent complex ideas or methodologies.

5. Use descriptive variable names that reflect [ENTITY_NAME]'s terminology, ontology, metaphysics.

6. Include comments to explain any non-obvious concepts or relationships.

7. If applicable, implement methods that simulate or represent [ENTITY_NAME]'s described processes or theories.

8. Ensure that the script follows Python best practices, it can be pseudocode or config-like at places.

9. Prioritize accuracy and fidelity to [ENTITY_NAME]'s ideas over brevity. Feel free to include long specific quotes in strings, for example exact key phrases, memes, explanations, predictions, based upon the transcripts in the folder

Use the existing ENTITY.py structure as a starting point, but feel free to expand or modify it as needed to best represent [ENTITY_NAME]'s comprehensive worldview and parameterized stances (there is no need to include technical/statistical methods for implementing Active Inference or Free Energy Principle here - focus only on the ENTITY's worldview beliefs)'


---------------






# CO-STAR Prompt Framework for Entity Analysis

"""
Context: You are an expert in analyzing scientific and philosophical perspectives. You have access to transcripts and documents related to [ENTITY_NAME] in the current folder.

Objective: Comprehensively update the ENTITY.py script to accurately reflect [ENTITY_NAME]'s worldview, key concepts, and methodologies.

Style: Maintain a structured, analytical approach. Use Python-like syntax for clarity, but prioritize conceptual accuracy over strict code adherence.

Tone: Objective and precise, capturing the nuances of [ENTITY_NAME]'s thoughts.

Audience: Researchers and developers interested in modeling complex philosophical and scientific perspectives.

Response: Provide a detailed update to the ENTITY.py script, following the guidelines below.
"""

# Task Instructions
def analyze_and_update_entity():
    """
    1. Thoroughly examine all transcripts and documents related to [ENTITY_NAME].
    2. Extract and synthesize key concepts, perspectives, and methodologies.
    3. Update the ENTITY.py script with the following enhancements:

    a) Maintain and expand existing functions (worldview, implications, stances, beliefs).
    b) Add or modify dictionary keys and values to capture nuanced views.
    c) Use descriptive variable names reflecting [ENTITY_NAME]'s terminology and ontology.
    d) Create new functions or classes for complex ideas or methodologies if needed.
    e) Implement methods to represent [ENTITY_NAME]'s described processes or theories.
    f) Include specific quotes, key phrases, and predictions as string values.
    g) Add comments to explain non-obvious concepts or relationships.
    h) Ensure values (boolean, categorical, quantitative) accurately represent stances.
    i) Prioritize accuracy and fidelity to [ENTITY_NAME]'s ideas over brevity.
    j) Focus on worldview and beliefs, not technical implementations of theories.

    4. Follow Python best practices where applicable, but allow for pseudocode or config-like structures when necessary.
    5. Provide a brief explanation for significant changes or additions to the script.
    """

# Example Output Format
"""
class [ENTITY_NAME]Worldview:
    def __init__(self):
        self.name = "[ENTITY_NAME]"
        self.key_concepts = {
            "concept1": "Detailed explanation...",
            "concept2": "Detailed explanation...",
        }
        
    def worldview(self):
        return {
            "aspect1": value,
            "aspect2": value,
        }
        
    def implications(self):
        # ...

    def stances(self):
        return {
            "topic1": 0.7,  # Explanation for the value
            "topic2": 0.9,  # Explanation for the value
        }

    def beliefs(self):
        return {
            "belief1": "Detailed explanation...",
            "belief2": "Detailed explanation...",
        }

    # Additional methods as needed
"""

# Execute the analysis and provide the updated ENTITY.py script
analyze_and_update_entity()