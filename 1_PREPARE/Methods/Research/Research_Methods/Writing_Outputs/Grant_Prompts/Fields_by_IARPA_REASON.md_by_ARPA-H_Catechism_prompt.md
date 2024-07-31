
        As an expert grant writer, craft a compelling grant proposal that authentically represents the perspective of the given entity while addressing the specific requirements of the grant call. Your task is to answer the catechism questions comprehensively, ensuring alignment with the grant agency's objectives and the entity's unique capabilities.

        Entity (Technical/Perspectival Skills and Capacities):
        import os
import logging
from typing import Dict, List, Any, Tuple
import numpy as np

class FieldsWorldView:
    def __init__(self):
        self.name = "Chris Fields"
        self.description = "A physicist and interdisciplinary researcher focusing on the foundations of cognition, consciousness, and reality from an information-theoretic perspective"
        
    def worldview(self) -> Dict[str, Any]:
        return {
            "information_theory": {
                "importance": 10,
                "description": "The fundamental basis for understanding reality, perception, and cognition",
                "quote": "Information is more fundamental than matter or energy; it's the currency of reality."
            },
            "active_inference": {
                "importance": 10,
                "description": "A framework explaining how all systems, including minds, interact with and model their environment",
                "quote": "Active inference isn't just a theory of brain function; it's a theory of life itself."
            },
            "quantum_mechanics": {
                "importance": 9,
                "description": "A theory providing insights into the nature of reality, information, and potentially consciousness",
                "quote": "Quantum mechanics isn't just about particles; it's about how reality itself is structured."
            },
            "free_energy_principle": {
                "importance": 10,
                "description": "A unifying principle explaining the behavior of all self-organizing systems",
                "quote": "The free energy principle is not just a theory of brain function, but a fundamental principle of self-organizing systems."
            },
            "holographic_principle": {
                "importance": 8,
                "description": "A concept suggesting reality might be encoded on a lower-dimensional boundary",
                "quote": "The holographic principle might apply not just to physics, but to cognition itself."
            },
            "interdisciplinary_approach": {
                "importance": 10,
                "description": "The necessity of integrating insights from multiple fields to understand complex phenomena",
                "quote": "Understanding the mind requires insights from physics, biology, computer science, and philosophy."
            },
            "observer_dependence": {
                "importance": 10,
                "description": "The idea that reality is fundamentally shaped by the act of observation",
                "quote": "The world is not 'out there' waiting to be observed; it is constructed by observation."
            },
            "information_realism": {
                "importance": 10,
                "description": "The view that information is the most fundamental aspect of reality",
                "quote": "The universe is not just described by information; it is information."
            },
            "semantic_information": {
                "importance": 9,
                "description": "The idea that information is inherently meaningful and relational",
                "quote": "Reality is not made of stuff, but of semantics - meaningful relationships between bits of information."
            },
            "quantum_darwinism": {
                "importance": 8,
                "description": "A theory explaining the emergence of classical reality from quantum substrates",
                "quote": "Quantum Darwinism shows us how the classical world we experience emerges from the quantum realm through a process of information selection."
            },
            "embodied_cognition": {
                "importance": 9,
                "description": "The view that cognitive processes are deeply rooted in the body's interactions with the world",
                "quote": "Cognition isn't just in the head; it's a process that involves the entire body and its environment."
            },
            "consciousness": {
                "importance": 10,
                "description": "A fundamental aspect of reality, potentially intrinsic to information processing",
                "quote": "Consciousness is not something the brain does; it's something the brain participates in."
            },
            "measurement_problem": {
                "importance": 9,
                "description": "The fundamental issue in quantum mechanics regarding the nature of measurement and observation",
                "quote": "The hard problem of consciousness and the measurement problem in quantum mechanics may be two sides of the same coin."
            },
            "context_dependence": {
                "importance": 10,
                "description": "The crucial role of context in determining meaning and reality",
                "quote": "Context isn't just important; it's everything. Without context, information has no meaning."
            },
            "cognitive_illusions": {
                "importance": 8,
                "description": "Phenomena that reveal fundamental truths about perception and reality",
                "quote": "Cognitive illusions aren't errors; they're windows into the fundamental nature of perception and reality."
            },
            "thermodynamics_of_cognition": {
                "importance": 8,
                "description": "The energetic costs and constraints of information processing in cognitive systems",
                "quote": "The costs of information processing aren't just practical constraints; they shape the very nature of cognition and reality."
            },
            "category_theory": {
                "importance": 7,
                "description": "A mathematical framework for describing structures and relationships",
                "quote": "Category theory provides a language for describing the deep structure of reality that transcends the limitations of set theory."
            },
            "predictive_processing": {
                "importance": 9,
                "description": "The idea that perception and cognition are fundamentally predictive processes",
                "quote": "The brain is not a passive receiver of information, but an active predictor constantly refining its models of the world."
            }
        }
    
    def implications(self) -> List[str]:
        return [
            "Reality is fundamentally informational and observer-dependent",
            "The boundary between observer and observed is fluid and context-dependent",
            "Consciousness and cognition are deeply intertwined with the physical world",
            "Perception is an active, predictive process rather than passive reception",
            "Quantum mechanics may play a crucial role in cognition and consciousness",
            "The self is a constructed model, not a fundamental entity",
            "Free will, in the libertarian sense, is likely an illusion",
            "Understanding cognition requires integrating insights from multiple disciplines",
            "The hard problem of consciousness may be resolved through information-theoretic approaches",
            "Reality might be understood as a unified information space",
            "The distinction between epistemology and ontology may be artificial",
            "Time and space are emergent properties of information flow",
            "Measurement creates reality rather than revealing pre-existing facts",
            "Consciousness might be an intrinsic aspect of information processing",
            "The universe can be understood as a vast network of semantic relationships",
            "Context is a fundamental aspect of information and meaning",
            "Cognitive illusions reveal deep truths about the nature of perception and reality",
            "The emergence of classical reality from quantum substrates can be understood through information-theoretic principles",
            "The costs of information processing have profound implications for cognition and physics",
            "The hard problem of consciousness and the measurement problem in quantum mechanics may be deeply related",
            "Category theory may provide a more fundamental language for describing reality than set theory",
            "The principles governing living systems, such as active inference, may apply to all self-organizing systems",
            "The holographic principle may apply not just to physics but to cognition and consciousness",
            "Quantum Darwinism may explain how the classical world emerges from quantum phenomena",
            "The observer-observed distinction may be an artifact of our cognitive architecture rather than a fundamental feature of reality"
        ]
    
    def stances(self) -> Dict[str, Any]:
        return {
            "physicalism": {
                "value": 5,
                "explanation": "While not rejecting physicalism outright, Fields emphasizes the fundamental role of information in reality"
            },
            "information_realism": {
                "value": 10,
                "explanation": "Information is seen as the most fundamental aspect of reality, possibly more fundamental than matter or energy"
            },
            "quantum_cognition": {
                "value": 9,
                "explanation": "Quantum mechanical principles are likely crucial for understanding cognition and consciousness"
            },
            "embodied_cognition": {
                "value": 10,
                "explanation": "Cognition is deeply intertwined with the body and its interactions with the environment"
            },
            "predictive_processing": {
                "value": 10,
                "explanation": "Perception and cognition are fundamentally predictive processes, aligning with the free energy principle"
            },
            "panpsychism": {
                "value": 7,
                "explanation": "While not explicitly endorsing panpsychism, Fields' views on information and consciousness are compatible with some forms of it"
            },
            "scientific_realism": {
                "value": 8,
                "explanation": "Advocates for a form of scientific realism, but one that acknowledges the observer-dependent nature of reality"
            },
            "emergence": {
                "value": 9,
                "explanation": "Many phenomena, including consciousness and spacetime, are seen as emergent properties of information processing"
            },
            "holism": {
                "value": 10,
                "explanation": "Emphasizes the interconnectedness of phenomena and the importance of studying systems as wholes"
            },
            "information_theoretic_semantics": {
                "value": 10,
                "explanation": "Meaning and semantics are fundamentally grounded in information-theoretic relationships"
            },
            "quantum_darwinism": {
                "value": 8,
                "explanation": "Supports the idea that classical reality emerges from quantum substrates through a process analogous to natural selection"
            },
            "contextual_realism": {
                "value": 9,
                "explanation": "Reality is fundamentally contextual, with the meaning and state of systems depending on their relationships and interactions"
            },
            "active_inference": {
                "value": 10,
                "explanation": "Sees active inference as a fundamental principle explaining the behavior of all self-organizing systems"
            },
            "free_energy_principle": {
                "value": 10,
                "explanation": "Views the free energy principle as a unifying framework for understanding cognition and self-organization"
            },
            "observer_dependent_reality": {
                "value": 10,
                "explanation": "Reality is fundamentally shaped by the act of observation and cannot be separated from the observer"
            },
            "information_thermodynamics": {
                "value": 8,
                "explanation": "The thermodynamic costs of information processing are seen as fundamental constraints on cognition and reality"
            },
            "category_theoretic_ontology": {
                "value": 7,
                "explanation": "Category theory is seen as a potentially more fundamental language for describing the structure of reality"
            }
        }
    
    def beliefs(self) -> Dict[str, bool]:
        return {
            "reality_is_observer_dependent": True,
            "information_is_fundamental": True,
            "consciousness_is_fundamental": True,
            "cognition_extends_beyond_brain": True,
            "quantum_effects_relevant_to_cognition": True,
            "free_will_is_illusion": True,
            "self_is_constructed": True,
            "perception_is_active_inference": True,
            "reality_is_unified_information_space": True,
            "measurement_creates_reality": True,
            "time_is_emergent": True,
            "space_is_emergent": True,
            "holographic_principle_applies_to_cognition": True,
            "hard_problem_of_consciousness_is_solvable": True,
            "observer_and_observed_are_inseparable": True,
            "reality_is_fundamentally_semantic": True,
            "quantum_decoherence_explains_classical_reality": True,
            "cognition_is_quantum_computational": True,
            "information_has_physical_consequences": True,
            "consciousness_is_intrinsic_to_information_processing": True,
            "context_is_fundamental_to_information": True,
            "cognitive_illusions_reveal_fundamental_truths": True,
            "quantum_darwinism_explains_classical_emergence": True,
            "thermodynamics_constrains_cognition": True,
            "category_theory_describes_deep_structure_of_reality": True,
            "active_inference_applies_to_all_self_organizing_systems": True,
            "free_energy_principle_is_universal": True,
            "reality_is_fundamentally_relational": True,
            "information_processing_has_intrinsic_cost": True,
            "observer_observed_distinction_is_artificial": True
        }
    
    def methodologies(self) -> List[str]:
        return [
            "Information theory",
            "Quantum mechanics",
            "Active inference",
            "Free energy principle",
            "Bayesian inference",
            "Category theory",
            "Cognitive neuroscience",
            "Philosophy of mind",
            "Computational modeling",
            "Interdisciplinary synthesis",
            "Quantum information theory",
            "Holographic models",
            "Graph theory",
            "Formal semantics",
            "Thermodynamics of computation",
            "Quantum cognition models",
            "Information-theoretic approaches to consciousness",
            "Predictive processing frameworks",
            "Quantum decoherence analysis",
            "Semantic network analysis",
            "Quantum Darwinism modeling",
            "Contextual analysis",
            "Cognitive illusion studies",
            "Information-theoretic cost analysis",
            "Holographic cognitive integration modeling",
            "Category-theoretic modeling of cognition",
            "Observer-dependent reality simulations",
            "Semantic information processing models",
            "Embodied cognition experiments",
            "Quantum measurement theory"
        ]
    
    def quotes(self) -> List[str]:
        return [
            "The world is not 'out there' waiting to be observed; it is constructed by observation.",
            "Consciousness is not something the brain does; it's something the brain participates in.",
            "The boundary between self and world is a matter of perspective, not ontology.",
            "Information is more fundamental than matter or energy; it's the currency of reality.",
            "Quantum mechanics isn't just about particles; it's about how reality itself is structured.",
            "Active inference isn't just a theory of brain function; it's a theory of life itself.",
            "The hard problem of consciousness is a symptom of our failure to understand the nature of information.",
            "To understand the mind, we must understand how it constructs and navigates reality.",
            "Measurement is a dialogue between observer and observed, not a one-way extraction of pre-existing facts.",
            "The self is not a thing, but a process - a continual act of self-measurement and self-modeling.",
            "Time and space are not containers for events, but emergent properties of information flow.",
            "Reality is not made of stuff, but of semantics - meaningful relationships between bits of information.",
            "The universe is not just described by information; it is information.",
            "Consciousness might be what information feels like when it's being processed.",
            "The hard problem of consciousness and the measurement problem in quantum mechanics may be two sides of the same coin.",
            "Every measurement, every observation, every interaction is a kind of computation.",
            "The observer-observed distinction is an artifact of our cognitive architecture, not a fundamental feature of reality.",
            "Quantum decoherence doesn't solve the measurement problem; it just pushes it back a step.",
            "The free energy principle is not just a theory of brain function, but a fundamental principle of self-organizing systems.",
            "Category theory provides a language for describing the deep structure of reality that transcends the limitations of set theory.",
            "Context isn't just important; it's everything. Without context, information has no meaning.",
            "Cognitive illusions aren't errors; they're windows into the fundamental nature of perception and reality.",
            "Quantum Darwinism shows us how the classical world we experience emerges from the quantum realm through a process of information selection.",
            "The costs of information processing aren't just practical constraints; they shape the very nature of cognition and reality.",
            "The hard problem of consciousness and the measurement problem in quantum mechanics are deeply connected. Solving one may solve the other.",
            "The brain doesn't create consciousness; it constrains it.",
            "Reality is not a collection of things, but a network of relationships.",
            "The distinction between epistemology and ontology breaks down at the quantum level.",
            "Information is physical, and physics is informational.",
            "The universe computes its own evolution."
        ]

    def key_papers(self) -> List[Dict[str, str]]:
        return [
            {
                "title": "If Physics Is an Information Science, What Is an Observer?",
                "description": "Explores the idea of observers as information-processing systems and its implications for physics and cognition."
            },
            {
                "title": "Conscious observation and the measurement problem in quantum mechanics",
                "description": "Discusses the role of consciousness in quantum measurement and its implications for our understanding of reality."
            },
            {
                "title": "Some consequences of the thermodynamic cost of system identification",
                "description": "Examines the energetic costs of perception and cognition from an information-theoretic perspective."
            },
            {
                "title": "A holographic model of cognitive integration and quantum cognition",
                "description": "Proposes a model of cognition based on the holographic principle and quantum information theory."
            },
            {
                "title": "Decoherence and the theory of the subject",
                "description": "Explores the relationship between quantum decoherence and the emergence of classical reality and subjectivity."
            },
            {
                "title": "On the reality of cognitive illusions",
                "description": "Examines the nature of cognitive illusions from an information-theoretic perspective, challenging traditional notions of perception and reality."
            },
            {
                "title": "Quantum Darwinism as a darwinian process",
                "description": "Analyzes the concept of quantum Darwinism and its implications for the emergence of classical reality from quantum substrates."
            },
            {
                "title": "Context as information: A conceptual analysis",
                "description": "Explores the nature of context from an information-theoretic perspective, with implications for cognition and semantics."
            },
            {
                "title": "Autonomy all the way down: Systems and dynamics in quantum Bayesianism",
                "description": "Investigates the connections between quantum mechanics, Bayesian inference, and the autonomy of physical systems."
            },
            {
                "title": "The Measurement Problem in Quantum Mechanics: A Phenomenological Approach",
                "description": "Proposes a new perspective on the measurement problem in quantum mechanics, emphasizing the role of the observer and information."
            }
        ]

    def simulate_perception(self, sensory_input: Dict[str, Any]) -> Dict[str, Any]:
        """
        Simulates Fields' view of perception as active inference.
        This is a simplified, conceptual representation.
        """
        prior_beliefs = self.worldview()
        predicted_input = self._generate_prediction(prior_beliefs)
        prediction_error = self._calculate_prediction_error(sensory_input, predicted_input)
        updated_beliefs = self._update_beliefs(prior_beliefs, prediction_error)
        return updated_beliefs

    def _generate_prediction(self, beliefs: Dict[str, Any]) -> Dict[str, Any]:
        # Placeholder for prediction generation based on current beliefs
        return {}

    def _calculate_prediction_error(self, actual: Dict[str, Any], predicted: Dict[str, Any]) -> float:
        # Placeholder for calculating prediction error
        return 0.0

    def _update_beliefs(self, beliefs: Dict[str, Any], error: float) -> Dict[str, Any]:
        # Placeholder for belief update based on prediction error
        return beliefs

    def information_theoretic_semantics(self, concept: str) -> Dict[str, Any]:
        """
        Represents Fields' approach to understanding meaning through information theory.
        """
        # Placeholder implementation
        return {
            "concept": concept,
            "information_content": 0.0,
            "relational_structure": {},
            "contextual_dependencies": []
        }

    def quantum_cognitive_model(self, cognitive_state: Dict[str, Any]) -> Tuple[complex, Dict[str, Any]]:
        """
        Represents a simplified quantum model of cognition, as per Fields' theories.
        """
        # Placeholder implementation
        psi = complex(1.0, 0.0)  # Quantum state
        observables = {}  # Dictionary of observable operators
        return psi, observables

    def holographic_cognitive_integration(self, perceptual_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Models cognitive integration using a holographic approach, as suggested by Fields.
        """
        # Placeholder implementation
        integrated_representation = {}
        return integrated_representation

    def observer_dependent_reality(self, observer_state: Dict[str, Any], environment: Dict[str, Any]) -> Dict[str, Any]:
        """
        Models the observer-dependent nature of reality as described by Fields.
        """
        # Placeholder implementation
        constructed_reality = {}
        # Simulate the process of reality construction through observation
        return constructed_reality

    def information_to_matter_interface(self, information: Dict[str, Any]) -> Dict[str, Any]:
        """
        Represents Fields' ideas on how information interfaces with physical reality.
        """
        # Placeholder implementation
        physical_consequences = {}
        # Model the process by which information has physical effects
        return physical_consequences

    def semantic_network_of_reality(self, concepts: List[str]) -> Dict[str, List[str]]:
        """
        Generates a semantic network representing Fields' view of reality as a web of meaningful relationships.
        """
        # Placeholder implementation
        network = {concept: [] for concept in concepts}
        # Generate connections between concepts based on Fields' theories
        return network

def load_fields_entity():
    return FieldsWorldView()




        Catechism (Comprehensive Project Description):
        # Concept Summary - ARPA-H

## Instructions
- Begin with a terse one-liner on the most essential aspect of the work
- Keep the summary short (less than 250 words, ideally 200)
- Focus on key information, avoid fluff

## Primary Questions (Answer with 1-10 sentences per question)
1. What work will be performed?
2. What is the research question, opportunity, gap, or problem being addressed?
3. What is the objective, goal, or mission?
4. What is the approach being considered or used?
5. What are the broader implications of the work or idea?
6. What is unique about this work, idea, or team?
7. What talking points would help communicate the premise to others?
8. What are the implications if the problem goes unaddressed?
9. What is the timeline and key milestones?
10. Why are traditional methods inadequate?
11. Why should the reader care?
12. What are the most essential deliverables?
13. What are the core references, terms of art, and concepts used by the stakeholder?

## Secondary Question
- What is the stakeholder's announced mission?

## Style Requirements
- Word Count Limit: 250 words or less
- Plain text only
- No citations, footnotes, hyperlinks, or URLs


        Grant Call (Agency Requirements):
        # IARPA REASON Program

## U.S. ARMY RESEARCH OFFICE
In partnership with  
The Intelligence Advanced Research Projects Activity (IARPA)  
BROAD AGENCY ANNOUNCEMENT for  
Rapid Explanation, Analysis and Sourcing Online (REASON) Program  
W911NF-23-S-0007  
Amendment 1: 5 April 2023  
Issued by:  
US Army Contracting Command–Aberdeen Proving Ground  
Research Triangle Park Division  
P.O. Box 12211  
Research Triangle Park, NC 27709-2211

## Table of Contents
| Section | Title | Page |
| --- | --- | --- |
| I. | OVERVIEW OF THE FUNDING OPPORTUNITY | 4 |
| A. | Required Overview Content | 4 |
| 1. | Federal Agency Name(s) | 4 |
| 2. | Funding Opportunity Title: Rapid Explanation, Analysis and Sourcing Online (REASON) Program | 4 |
| 3. | Announcement Type | 4 |
| 4. | Research Opportunity Number: W911NF-23-S-0007 | 4 |
| 5. | Catalog of Federal Domestic Assistance (CFDA) Number | 4 |
| 6. | Response Dates | 4 |
| B. | Additional Overview Information | 4 |
| II. | DETAILED INFORMATION ABOUT THE FUNDING OPPORTUNITY | 5 |
| A. | Funding Opportunity Description | 5 |
| 1. | Program Summary | 5 |
| 2. | Technical Challenges and Objectives | 6 |
| 3. | Program Phases | 7 |
| 4. | Program Scope and Limitations | 9 |
| 5. | Program Data | 10 |
| 6. | Test and Evaluation (T&E) | 11 |
| 7. | Program Metrics | 12 |
| 8. | Program Waypoints, Milestones, and Deliverables | 14 |
| 9. | Meeting, Travel, and Publication Requirements | 18 |
| 10. | Period of Performance | 19 |
| 11. | Place of Performance | 19 |
| 12. | Security | 19 |
| 13. | Human Subjects Research | 19 |
| B. | Federal Award Information | 20 |
| C. | Eligibility Information | 21 |
| 1. | Eligible Applicants | 21 |
| 2. | Cost Sharing or Matching | 23 |
| 3. | Federally Funded Research and Development Centers and University Affiliated Research Centers | 23 |
| D. | Application and Submission Information | 23 |
| 1. | Addresses to View Broad Agency Announcement | 24 |
| 2. | Content and Form of Application Submission | 24 |
| 3. | Submission of Complete Research Proposals | 48 |
| 4. | Unique Entity Identifier and System for Award Management (SAM) | 49 |
| 5. | Intergovernmental Review | 50 |
| 6. | Funding Restrictions | 50 |
| 7. | Other Submission Requirements | 51 |
| E. | Proposal Review Information | 51 |
| 1. | Criteria | 51 |
| 2. | Review and Selection Process | 53 |
| 3. | Recipient Qualification | 54 |
| F. | Award Administration Information | 55 |
| 1. | Award Notices | 55 |
| 2. | Administrative and National Policy Requirements | 56 |
| 3. | Reporting | 57 |
| G. | Agency Contacts | 57 |
| H. | Other Information | 58 |
| 1. | Example of Technical Cover Sheet | 58 |
| 2. | Example of Academic Institution Acknowledgement Letter | 60 |
| 3. | Example of Technical SOW | 61 |
| 4. | Example of Team Organization Table | 62 |
| 5. | Example of Intellectual Rights Sheet | 63 |
| 6. | Example of Contract Deliverables Table | 64 |
| 7. | Example of Organizational Conflicts of Interest Certification Letter | 65 |
| 8. | Example of Three Chart Summary of the Proposal | 66 |
| 9. | Sample of the Research Data Management Plan | 67 |
| 10. | Cover Sheet – Cost Proposal | 69 |
| 11. | Example of Prime Contractor/Subcontract Cost Element Sheet for Volume 2: Cost Proposal | 70 |
| 12. | Example of Travel Costs Trip Breakdown Sheet | 71 |
| 13. | Glossary of Acronyms | 72 |
| 14. | References | 73 |

## I. OVERVIEW OF THE FUNDING OPPORTUNITY

### A. Required Overview Content

1. Federal Agency Name(s)  
   U.S. Army Research Office  
   Issuing Acquisition Office  
   U.S. Army Contracting Command-Aberdeen Proving Ground, Research Triangle Park Division (ACC-APG-RTP Division)  

2. Funding Opportunity Title: Rapid Explanation, Analysis and Sourcing Online (REASON) Program

3. Announcement Type  
   Full Announcement

4. Research Opportunity Number: W911NF-23-S-0007

5. Catalog of Federal Domestic Assistance (CFDA) Number  
   12.431 – Basic Scientific Research

6. Response Dates  
   BAA release: March 20th, 2023  
I. OVERVIEW OF THE FUNDING OPPORTUNITY ................................................................. 4  
A. Required Overview Content..........................................................................................................4  
1. Federal Agency Name(s) ..............................................................................................................................4  
2. Funding OpportunityTitle: Rapid Explanation, Analysis and Sourcing Online (REASON) Program..4  
3. Announcement Type ...................................................................................................................................4  
4. Research Opportunity Number: W911NF-23-S-0007..........................................................................4  
5. Catalog of Federal Domestic Assistance (CFDA) Number ......................................................................4  
6. Response Dates............................................................................................................................................4  
B. Additional Overview Information ......................................................................................................4  
II. DETAILED INFORMATION ABOUT THE FUNDING OPPORTUNITY................................. 5  
A. Funding Opportunity Description..................................................................................................5  
1. Program Summary ........................................................................................................................................5  
2. Technical Challenges and Objectives ...........................................................................................................6  
3. Program Phases.............................................................................................................................................7  
3. Recommended Team Expertise ....................................................................................................................9  
4. Program Scope and Limitations....................................................................................................................9  
5. Program Data............................................................................................................................................10  
6. Test and Evaluation (T&E).....................................................................................................................11  
7. Program Metrics.......................................................................................................................................12  
8. Program Waypoints, Milestones, and Deliverables............................................................................14  
9. Meeting, Travel, and Publication Requirements..........................................................................................18  
10. Period of Performance.............................................................................................................................19  
11. Place of Performance...............................................................................................................................19  
12. Security......................................................................................................................................................19  
13. Human Subjects Research ..........................................................................................................................19  
B. Federal Award Information..............................................................................................................20  
C. Eligibility Information...................................................................................................................21  
1. Eligible Applicants: ....................................................................................................................................21  
2. Cost Sharing or Matching:..........................................................................................................................23  
3. Federally Funded Research and Development Centers and University Affiliated Research Centers:........23  
D. Application and Submission Information....................................................................................23  
1. Addresses to View Broad Agency Announcement.....................................................................................24  
2. Content and Form of Application Submission............................................................................................24  
Volume 1 – Technical & Management Proposal..................................................................................................25  
Volume 2 – Cost Proposal....................................................................................................................................39  
3. Submission of Complete Research Proposals.............................................................................................48  
4. Unique Entity Identifier and System for Award Management (SAM) .......................................................49  
4. Submission Dates and Times:.....................................................................................................................50  
5. Intergovernmental Review:.........................................................................................................................50  
6. Funding Restrictions:..................................................................................................................................50  
7. Other Submission Requirements:................................................................................................................51  
E. Proposal Review Information:......................................................................................................51  
iii  
1. Criteria: .......................................................................................................................................................51  
2. Review and Selection Process: ...................................................................................................................53  
3. Recipient Qualification ...............................................................................................................................54  
F. Award Administration Information:............................................................................................55  
1. Award Notices: ...........................................................................................................................................55  
2. Administrative and National Policy Requirements:....................................................................................56  
3. Reporting: ...................................................................................................................................................57  
G. Agency Contacts:............................................................................................................................57  
H. Other Information: ........................................................................................................................58  
1. Example of Technical Cover Sheet.............................................................................................................58  
2. Example of Academic Institution Acknowledgement Letter......................................................................60  
3. Example of Technical SOW .......................................................................................................................61  
4. Example of Team Organization Table ........................................................................................................62  
5. Example of Intellectual Rights Sheet..........................................................................................................63  
6. Example of Contract Deliverables Table ....................................................................................................64  
7. Example of Organizational Conflicts of Interest Certification Letter.........................................................65  
8. Example of Three Chart Summary of the Proposal ....................................................................................66  
9. Sample of the Research Data Management Plan ........................................................................................67  
10. Cover Sheet – Cost Proposal.......................................................................................................................69  
11. Example of Prime Contractor/Subcontract Cost Element Sheet for Volume 2: Cost Proposal ..................70  
12. Example of Travel Costs Trip Breakdown Sheet........................................................................................71  
13. Glossary of Acronyms: ...............................................................................................................................72  
14. References...................................................................................................................................................73  

## I. OVERVIEW OF THE FUNDING OPPORTUNITY

### A. Required Overview Content

1. Federal Agency Name(s)  
   U.S. Army Research Office  
   Issuing Acquisition Office  
   U.S. Army Contracting Command-Aberdeen Proving Ground, Research Triangle Park Division (ACC-APG-RTP Division)  
i
U.S. ARMY RESEARCH OFFICE
In partnership with
The Intelligence Advanced Research Projects Activity (IARPA)
BROAD AGENCY ANNOUNCEMENT for
Rapid Explanation, Analysis and Sourcing Online (REASON) Program
W911NF-23-S-0007
Amendment 1: 5 April 2023
Issued by:
US Army Contracting Command–Aberdeen Proving Ground
Research Triangle Park Division
P.O. Box 12211
Research Triangle Park, NC 27709-2211
ii
I. OVERVIEW OF THE FUNDING OPPORTUNITY ................................................................. 4
A. Required Overview Content..........................................................................................................4
1. Federal Agency Name(s) ..............................................................................................................................4
2. Funding OpportunityTitle: Rapid Explanation, Analysis and Sourcing Online (REASON) Program..4
3. Announcement Type ...................................................................................................................................4
4. Research Opportunity Number: W911NF-23-S-0007..........................................................................4
5. Catalog of Federal Domestic Assistance (CFDA) Number ......................................................................4
6. Response Dates............................................................................................................................................4
B. Additional Overview Information ......................................................................................................4
II. DETAILED INFORMATION ABOUT THE FUNDING OPPORTUNITY................................. 5
A Funding Opportunity Description..................................................................................................5
1. Program Summary ........................................................................................................................................5
2. Technical Challenges and Objectives ...........................................................................................................6
3. Program Phases.............................................................................................................................................7
3. Recommended Team Expertise ....................................................................................................................9
4. Program Scope and Limitations....................................................................................................................9
5. Program Data............................................................................................................................................10
6. Test and Evaluation (T&E).....................................................................................................................11
7. Program Metrics.......................................................................................................................................12
8. Program Waypoints, Milestones, and Deliverables............................................................................14
9. Meeting, Travel, and Publication Requirements..........................................................................................18
10. Period of Performance.............................................................................................................................19
11. Place of Performance...............................................................................................................................19
12. Security......................................................................................................................................................19
13. Human Subjects Research ..........................................................................................................................19
B. Federal Award Information..............................................................................................................20
C. Eligibility Information...................................................................................................................21
1. Eligible Applicants: ....................................................................................................................................21
2. Cost Sharing or Matching:..........................................................................................................................23
3. Federally Funded Research and Development Centers and University Affiliated Research Centers:........23
D. Application and Submission Information....................................................................................23
1. Addresses to View Broad Agency Announcement.....................................................................................24
2. Content and Form of Application Submission............................................................................................24
Volume 1 – Technical & Management Proposal..................................................................................................25
Volume 2 – Cost Proposal....................................................................................................................................39
3. Submission of Complete Research Proposals.............................................................................................48
4. Unique Entity Identifier and System for Award Management (SAM) .......................................................49
4. Submission Dates and Times:.....................................................................................................................50
5. Intergovernmental Review:.........................................................................................................................50
6. Funding Restrictions:..................................................................................................................................50
7. Other Submission Requirements:................................................................................................................51
E. Proposal Review Information:......................................................................................................51
iii
1. Criteria: .......................................................................................................................................................51
2. Review and Selection Process: ...................................................................................................................53
3. Recipient Qualification ...............................................................................................................................54
F. Award Administration Information:............................................................................................55
1. Award Notices: ...........................................................................................................................................55
2. Administrative and National Policy Requirements:....................................................................................56
3. Reporting: ...................................................................................................................................................57
G. Agency Contacts:............................................................................................................................57
H. Other Information: ........................................................................................................................58
1. Example of Technical Cover Sheet.............................................................................................................58
2. Example of Academic Institution Acknowledgement Letter......................................................................60
3. Example of Technical SOW .......................................................................................................................61
4. Example of Team Organization Table ........................................................................................................62
5. Example of Intellectual Rights Sheet..........................................................................................................63
6. Example of Contract Deliverables Table ....................................................................................................64
7. Example of Organizational Conflicts of Interest Certification Letter.........................................................65
8. Example of Three Chart Summary of the Proposal ....................................................................................66
9. Sample of the Research Data Management Plan ........................................................................................67
10. Cover Sheet – Cost Proposal.......................................................................................................................69
11. Example of Prime Contractor/Subcontract Cost Element Sheet for Volume 2: Cost Proposal ..................70
12. Example of Travel Costs Trip Breakdown Sheet........................................................................................71
13. Glossary of Acronyms: ...............................................................................................................................72
14. References...................................................................................................................................................73
4
I. OVERVIEW OF THE FUNDING OPPORTUNITY
A. Required Overview Content
1. Federal Agency Name(s)
U.S. Army Research Office
Issuing Acquisition Office
U.S. Army Contracting Command-Aberdeen Proving Ground, Research Triangle Park
Division (ACC-APG-RTP Division)
2. Funding OpportunityTitle: Rapid Explanation, Analysis and Sourcing Online
(REASON) Program
3. Announcement Type
Full Announcement
4. Research Opportunity Number: W911NF-23-S-0007
5. Catalog of Federal Domestic Assistance (CFDA) Number
12.431 – Basic Scientific Research
6. Response Dates
BAA release: March 20th, 2023
Questions must be submitted by: April 3rd, 2023 5:00 PM Eastern Time to:
dni-iarpa-baa-w911nf-23-s-0007@iarpa.gov
Response to questions expected by: April 14th, 2023
Proposals due by: 5:00 PM Eastern Time on May 8th, 2023
See Section II.D. for additional information.
B. Additional Overview Information
This Broad Agency Announcement (BAA), which sets forth research areas of interest to the Army
Research Laboratory-Army Research Office (ARL-ARO) and the Intelligence Advanced Research
Projects Activity (IARPA), is issued under paragraph 6.102(d)(2) of the Federal Acquisition
Regulation (FAR), and 10 USC 4001 which provides for the competitive selection of basic
research proposals. Proposals submitted in response to this BAA and selected for award are
considered to be the result of full and open competition and in full compliance with the provision
of Public Law 98-369, “The Competition in Contracting Act of 1984” and subsequent
amendments.
The Department of Defense (DoD) agencies involved in this Program reserve the right to select for
award either all, some, or none of the proposals submitted in response to this announcement. The
participating DoD agencies will provide no funding for direct reimbursement of proposal
development costs. Technical and cost proposals (or any other material) submitted in response to
5
this BAA will not be returned. It is the policy of participating DoD agencies to treat all proposals
as sensitive, competitive information and to disclose their contents only for the purposes of
evaluation.
This BAA makes frequent use of the terms “Offeror” and “Performer”. They are not
interchangeable. An Offeror is an entity who submits a proposal. Statements referring to Offeror
or Offerors are therefore directed at those preparing a proposal. A Performer designates an entity
engaged in Program work and provides here a useful point of view when describing expected
activities of the Program. Statements referring to Performer(s) are thus intended to inform Offerors
about the kinds and pace of work those engaged in the Program would be expected to undertake;
they are not intended to set or imply requirements for the proposal.
II. DETAILED INFORMATION ABOUT THE FUNDING
OPPORTUNITY
A Funding Opportunity Description
1. Program Summary
The Rapid Explanation, Analysis, and Sourcing Online (REASON) Program aims to develop
technology that will enable intelligence analysts to substantially increase the quality of
argumentation in their analytic reports through more effective use of evidence and reasoning. In
the context of an analytic report, evidence is information that supports or opposes a judgment,
while reasoning is the stated justification for the judgment. Furthermore, strong reasoning is
reasoning that logically substantiates the judgments while weak reasoning is reasoning that either
fails to substantiate the judgments or contains logical flaws. The technology developed by the
REASON Program will automatically produce comments (feedback and recommendations) on a
draft report, highlighting additional relevant evidence, and identify strengths and weaknesses in
the draft’s reasoning. Analysts can use the comments to improve their reports.
Argumentation is central to the Intelligence Community (IC) Analytic Standards, which are listed
in Intelligence Community Directive (ICD) 2031
. The standards are intended to guide IC analysis
and analytic production. The Analytic Tradecraft Standards focus on several aspects of evidence
and reasoning, including sourcing, explaining uncertainty, distinguishing between underlying
information and assumptions, and logical argumentation. Because evidence and reasoning are
crucial components of every analytic report, REASON will have broader application than previous
research efforts aimed at helping the IC make accurate forecasts.
Currently, intelligence analysts are encouraged to use structured analytic techniques to boost the
quality of argumentation in their reports.2,3
 Many of these methods require substantial additional
quantities of analysts’ time and are therefore not widely used. As contrasted with current
applications of structured analytic techniques, REASON technology will automatically produce
comments with no additional effort from analysts, who can use any comments they find valuable.
1 https://www.dni.gov/files/documents/ICD/ICD%20203%20Analytic%20Standards.pdf. 2 https://www.cia.gov/static/955180a45afe3f5013772c313b16face/Tradecraft-Primer-apr09.pdf 3 https://www.dia.mil/FOIA/FOIA-Electronic-Reading-Room/FileId/161442/
6
Some of these comments might be based on the automated application of effective structured
analytic techniques, along with additional innovations.
By making specific comments on draft analytic reports, REASON technology will fit into the
existing intelligence analysts’ workflow. The comments will be analogous to those made by
automated spelling and grammar checks, except that REASON’s comments will focus on
improving argumentation instead of writing.
Offerors shall address all three technical Task Areas (TAs) to meet REASON’s goal of developing
automated methods to produce comments on draft analytic reports that enable analysts to
substantially increase the report’s quality of argumentation:
• Task Area 1 (TA1) – Identify Additional Evidence: Automatically find relevant
supporting and contrary evidence in addition to the evidence used in a draft report.
• Task Area 2 (TA2) – Identify Reasoning Strengths and Weaknesses: Automatically
find strengths and weaknesses in the reasoning of a draft report.
• Task Area 3 (TA3) – Produce Comments to Increase Quality of Argumentation:
Based in part on the output of TA1 and TA2, automatically produce comments that enable
analysts to substantially improve the argumentation in their reports.
Offerors must propose novel approaches to each of these three TAs, and if selected as a Performer,
will be required to create an end-to-end technology that incorporates software components from
each TA. Developed capabilities must be compatible with a provided Application Programming
Interface (API) to facilitate assessment by independent test and evaluation (T&E) according to
program metrics described in Section II.A.7, Program Metrics.
2. Technical Challenges and Objectives
Offerors shall address the following technical challenges and objectives to meet the REASON
goals.
Identify Additional Evidence (TA1): The goal of TA1 is to develop technology that
automatically identifies additional supporting and contrary evidence when such evidence exists.
Successful approaches will produce, in response to a draft analytic report and a corpus of source
documents, a prioritized list of up to eight items of additional evidence contained in the corpus but
not mentioned in the draft report. (Only the first eight items will be scored). Performer systems
will need to determine whether a piece of information is relevant evidence bearing on the analytic
question addressed in the draft report and whether it is additional (non-redundant) to the
information used in the draft report. Performer systems should identify (where appropriate)
contrary as well as supporting evidence, determined by the relationship of the evidence to either
the draft’s conclusion or the evidence and reasoning within the draft. When there is no nonredundant additional evidence, performer systems should report that.
Identify Reasoning Strengths and Weaknesses (TA2): The goal of TA2 is to develop technology
that automatically finds strengths and weaknesses in the reasoning of a draft analytic report. This
means that the system will be able to identify reasoning elements in the draft report. For each draft 
7
report, the system will identify up to eight strengths and weaknesses. (Only the first eight items
will be scored). Each strength or weakness will point to the appropriate section of the draft report
and shall be accompanied by a brief explanation of why it is strong or weak reasoning. A successful
system must distinguish between apparent and real strengths and weaknesses in reasoning. If the
reasoning in the draft analytic report is sound, the system will report that.
Produce Comments to Increase Quality of Argumentation (TA3): The goal of TA3 is to
develop a software application that, with input from TA1 and TA2, automatically produces
comments on draft analytic reports that enable analysts to substantially increase the quality of
argumentation in the report. TA1 and TA2 provide evidence and reasoning improvement as inputs
to TA3, and TA3 builds on these to present useful comments to the analyst. Successful approaches
must identify key areas where a draft report can be improved and generate comments based on
those, presented in a manner that prompts analysts to use them effectively. The comments may
concern individual issues or the overall draft report, including the correctness of the conclusion or
the appropriateness of cited evidence; they may address the content or the communication of the
report’s argument.
The TA3 REASON application deliverable must be compatible with analyst authoring
applications, typically Microsoft Word. TA3 encompasses both the software development and the
research necessary to draw on TA1 and TA2 inputs and effectively communicate
recommendations to the analyst so that they improve the argumentation in their draft report. The
TA3 REASON application is the only portion of REASON that analysts will interact with.
REASON will provide comments to analysts in a timely manner once the analyst requests
them. There is no formal milestone for response time. However, delays in response times will
likely result in less use by test participants and intelligence analysts.
3. Program Phases
The REASON Program is a 42-month effort, comprising two phases. Proposers must submit to
both phases or else they will be considered to be non-compliant. Because the goal of the REASON
Program is to increase the quality of reports produced on classified systems, deliverables produced
by proposers must offer a minimum of Government Purpose Rights that grant the Government
intellectual property (IP) rights sufficient to allow the Government to modify and deploy
deliverables on classified networks.
In Phase 1 performer systems will be tested comprehensively on unclassified data consisting of
draft analytic reports and news reports. In parallel, the REASON independent T&E team will
retrain and evaluate performer systems on classified draft analytic reports and source reports. In
Phase 2 performer systems will be tested on classified data consisting of draft analytic reports and
classified source reports. In each phase performers will develop and be tested on techniques for
addressing TA1, TA2, and TA3. Each phase will contain several testing cycles; each cycle will
contain approximately 20 challenge problems consisting of an analytic question and a draft report.
Challenge problems will become increasingly difficult over the course of a phase.
In each phase TA1 will be evaluated by measuring the performer system’s ability to automatically
find and rank-order additional evidence. TA2 will be evaluated by measuring the performer 
8
system’s ability to automatically find and explain strengths and weaknesses in reasoning. TA3 will
be evaluated in two ways:
1. T&E raters will evaluate the comments produced by performer systems – on correctness,
appropriateness, and clarity.
2. Final Exam: Human participants will be assigned to use a performer system or to be in a
control group. Participants will produce draft reports on assigned analytic questions and
have opportunities to revise the reports. The same analytic questions will be posed to
experimental conditions using Performer systems and control conditions. The analytic
questions will be drawn from a wide variety of topic areas, including political, military,
social, economic, environmental, or diplomatic topics. The form in which the analytic
question is posed will vary and will emulate the type of taking that is given to IC analysts.
Participants assigned to a performer system will work for a set duration to produce a report.
During that time, each participant will see the comments that the system produces and may
use any of the comments in revising their report. T&E will measure the argumentative
quality of finished reports, comparing those produced with the aid of a performer system
to those produced by participants in control groups.
Phase 1
Phase 1 shall have a duration of 24 months. The goal of Phase 1 is to develop novel systems to
enable analysts working with unclassified data to produce analytic reports of substantially higher
quality. Performer research will focus on developing automated methods for processing
argumentation (evidence and reasoning) accurately, producing comments that human users find
explainable and helpful.
Performer systems’ TA1 and TA2 capabilities will be tested over three cycles each, where each
cycle includes both unclassified and classified testing. Cycles will become increasingly difficult
during the phase: it will become more challenging to find additional evidence and strengths and
weaknesses in the reasoning. Performer systems’ TA3 capabilities will be tested in one cycle (with
unclassified and classified testing) and one final exam using unclassified data. Each of the TA3
cycles will measure systems’ ability to produce comments that are correct, appropriate, and clear.
The final exam will measure the effect of the system’s automatically produced comments on the
quality of reports written by human users who produced the draft and can view the comments. The
human users will include undergraduate or graduate students in disciplines such as intelligence
analysis or international relations.
All Performer work will be unclassified. Performer systems will be tested by cleared T&E
personnel on classified data but Performers will not be able to review that classified data. T&E
will provide Performers with unclassified summary results from classified testing. In classified
testing, Performer systems, operated by cleared T&E personnel in an automated fashion, will need
to search, identify, and process textual documents containing classified data. These documents
will differ from the unclassified news and opinion documents in several ways. In addition to
containing new information, the classified data will have distinctive stylistic features, including
classification markings and IC-specific jargon and abbreviations. Some unclassified examples
with these stylistic features will be provided at Program Kickoff. 
9
Phase 2
Phase 2 shall have a duration of 18 months. The goal of Phase 2 is to refine the capabilities of the
methods developed in Phase 1 so that they function effectively on classified data and produce
substantially larger effects. Performers will refine their systems to process the content and style of
the IC’s source reports using unclassified examples, but they will not have access to classified
data. Performers will receive actionable summary level unclassified feedback from the
independent cleared T&E that they can use to refine the capabilities of their methods and systems.
Performer systems’ TA1 and TA2 capabilities will be tested over one cycle each. Performer
systems’ TA3 capabilities will be tested over two cycles and one final exam, using cleared
intelligence analysts as participants.
3. Recommended Team Expertise
Collaborative efforts and teaming among Offerors are highly encouraged. It is anticipated that
teams will be multidisciplinary and may include expertise in one or more of the disciplines listed
below. This list is included only to provide guidance for Offerors; satisfying all the areas of
technical expertise below is not a requirement for selection, and unconventional or innovative team
expertise may be needed based on the proposed research. Proposals should include a description
and the mix of skills and staffing that the Offeror determines will be necessary to carry out the
proposed research and achieve Program metrics.
• Applied epistemology
• Argumentation
• Cognitive psychology
• Experimental design
• Informal logic
• Judgment and decision making
• Linguistics
• Natural language processing
• Philosophy of language
• Psychometrics
• Rationality
• Software engineering
• Systems engineering
• Systems integration
4. Program Scope and Limitations
Proposals shall explicitly address all the following:
• Underlying Theory: Proposed strategies to meet Program-specified metrics must have
firm theoretical bases that are described with enough detail that reviewers will be able to
assess the viability of the approaches. Proposals shall properly describe and reference
previous work upon which their approach is founded. 
10
• R&D Approach: Proposals shall describe the technical approach to meeting Program
metrics.
• Technical Risks: Proposals shall identify technical risks and proposed mitigation
strategies for each.
• Software Development: Proposals shall describe the approach to software architecture
and integration.
The following areas of research are out of scope for the REASON Program:
• Purely automated production of analytic reports.
• Approaches that process non-textual inputs such as:
o Images
o Video
o Audio
o Structured data sources
o However, it is permissible to use textual clues (e.g., image captions) to locate and
retrieve non-textual items
• Approaches aimed at processing text in languages other than English.
• Approaches that require Performer access to classified information or data. All Performer
research will be strictly unclassified.
5. Program Data
The REASON program will use both data provided by the Government Team and data provided
by Performers. Proposals must specify the data needed to carry out the proposed research and what
data characteristics are necessary for the Proposer’s approach(es) to be successful at meeting
program objectives. These details should be provided for using Government-provided data as well
as Performer-provided data.
a. Government-Provided Data
The Government will obtain data as a corpus of source documents and make it available to
Performers via a T&E testbed. At the beginning of Phase 1 this will be a corpus of unclassified
news articles and analytic reports. At the beginning of each phase the Government team will also
provide access to a small sample of unclassified draft reports similar in form to the classified draft
reports that will be used in T&E testing in that phase.
The unclassified data provided by the Government for training and testing REASON systems is
intended to serve as a surrogate for the intelligence items that would be considered by an IC
analyst. For planning purposes, Performers may assume that this corpus of data will include at
least 25 years of output from at least 20 major reputable media outlets. The type of information
contained in the unclassified corpus will be diverse, matching the breadth of textual information
types available to analysts on classified networks. In addition to news reports, the corpus will
include analysis and opinion articles and reference materials.
11
The data to be used in classified tuning and testing of Performer systems will not be directly visible
to Performers. The data will reside on a classified testbed and will consist of source reports and
analytic products covering the same time period as the unclassified corpus.
At the beginning of the program the history available in both corpora will extend back at least 25
years. The corpora will be kept up to date as the REASON Program progresses.
In addition to the bulk corpora described above, Performers will be provided with annotated
examples for 5 Challenge Problems each for TA1, TA2, and TA3 REASON Comment Quality.
These annotated examples will include Challenge Problems, example solutions, and evaluation of
these solutions. Performers will not be provided with any annotations for data beyond these
example Challenge Problems.
b. Performer-Provided Data
Each Performer is expected to have a unique technical solution to the REASON challenges and
may require additional data for model training, model running, internal evaluation, or other
research needs. Proposals must present a dataset development plan detailing how the team intends
to obtain the data required. This documentation should account for any other associated labor to
curate and facilitate use of data that are acquired.
As part of their proposal, each team shall prepare a REASON Privacy Plan Version 1.0 that
comprehensively describes the efforts the team will take to protect personally identifiable
information and safeguard the security of any personal data collected or services involved in
collection, transmission, processing, and storage of these data. Any claims that data are anonymous
must be based on evidence and supported with sufficient information regarding how the data have
been anonymized.
This version 1.0 of the REASON Privacy Plan shall be included in the Proposer’s proposal as
Attachment 6 that covers all external datasets to be leveraged as part of the proposed research
approaches. The REASON Privacy Plan shall be updated at the beginning of each Phase and when
new sources of data or datasets are proposed for use within a Performer’s REASON research
activities, including data used for either development or evaluation purposes.
6. Test and Evaluation (T&E)
T&E will be conducted by an independent team of contractor staff carrying out evaluation and
analyses of Performer research deliverables using program test datasets and protocols. In addition
to independent T&E, the program will regularly gauge interim progress of Performer research
activities towards REASON objectives and target metrics using T&E results measured and
reported by the Performer teams themselves.
The REASON Program will pursue rigorous and comprehensive T&E to ensure that research
outcomes are well characterized, deliverables are aligned with program objectives, and
performance is measured across the full range of conditions. T&E activities will inform IARPA
and Government stakeholders on REASON research progress and serve as invaluable feedback to
Performers to improve their research approaches, training practices, and system development.
12
Performers will have specific Deliverable Milestones driven by the REASON evaluation cycle
schedule at which all subcomponent and system algorithms and software will be delivered to
IARPA and its designated T&E Team. The T&E Team will then conduct independent evaluations
with the objective of characterizing the quality, functionality, and performance of the REASON
systems. In addition to quantitative measurements, T&E assessments will be carried out to
establish a thorough understanding of the progress, status, and limitations of the Performer’s
research.
For classified testing, the T&E Team will retrain Performer systems to classified data as necessary,
using scripts or processes provided by the Performers.
T&E results and feedback will be provided to Performers at regular intervals to keep them abreast
of current independent performance measurements and to inform and improve their R&D
approaches and methods. T&E will provide unclassified feedback summarizing the results of the
unclassified testing and the classified testing to Performers. T&E results from all Performers will
be shared with all teams to establish an understanding of the current state and progress of REASON
research; T&E results will also be shared with USG external stakeholders, including their
contractors, for Government purposes. IARPA may conduct other supplemental evaluations or
measurements at its sole discretion to evaluate the Performers’ research and Deliverables.
A notional evaluation cycle schedule is indicated as part of the overall REASON Program
Schedule in Figure 1. For each TA, an evaluation cycle will consist of approximately 25 Challenge
Problems developed by T&E. The format for Challenge Problems will vary across the TAs and
will be specified in the Phase 1 T&E Plan at Program Kickoff. Within an evaluation cycle each
Performer system will receive the same Challenge Problems. Challenge Problems will differ
across evaluation cycles. For TA1, TA2, and TA3 REASON Comment Quality evaluations, T&E
will provide 5 Practice Challenge Problems as examples prior to the first cycle for that type of
evaluation. The Practice Challenge Problems will include the inputs to Performer systems, an
emulated Performer system solution, and annotation of that solution according to the evaluation
procedure in the T&E plan.
7. Program Metrics
Achievement of metrics is a performance indicator under IARPA research contracts. IARPA has
defined REASON program metrics to evaluate effectiveness of the proposed solutions in achieving
the stated program goal and objectives, and to determine whether satisfactory progress is being
made. The metrics described in this BAA are shared with the intent to scope the effort, while
affording maximum flexibility, creativity, and innovation to Proposers proposing solutions to the
stated problem.
The REASON T&E protocols and evaluation methodology are currently under development;
further details will be provided at Program Kickoff in the Phase 1 REASON T&E Plan. Program
metrics may be refined during the various phases of the REASON program; if metrics change,
revised metrics will be communicated in a timely manner to Performers. The evaluation
methodology may be revised by the Government at any time during the program lifecycle to better
meet program needs. The preliminary program metrics and target scores are provided below.
The TA1 metric is a modified version of alpha normalized discounted cumulative gain (αnDCG),
which will use the union of the outputs (evidence items) from all Performers and combine it with 
13
the outputs of a manual search for evidence by the T&E team in order to approximate the ideal
results. The formula for αnDCG will be:
αnDCG = αDCG(Performer results)
max (αDCG(All Performer results ∪ T&E discovered items))
The scoring process will be:
1. T&E performs a manual search of the corpus for evidence at the time they create each TA1
Challenge Problem. Some of their search results will be cited in the draft report, which is
used as the input to Performer systems; others will be reserved but not cited.
2. The Performer systems produce a set of up to 8 ordered evidence items found in the corpus
as the output for the Challenge Problem.
3. The output evidence item result sets from the several Performer systems are combined with
the reserved evidence items from step 1. The same item may be returned by multiple
Performers or may match the T&E items.
4. Each of the items in the resulting set from step 3 are evaluated:
a. Is the item redundant to the cited evidence in the draft report?
b. What is the relevance of the item?
c. What category does the item belong to? For example, if the analysis report deals
with a potential military invasion, then one category might include evidence of
troop movements, another might include public statements by leaders, a third might
include previous examples of similar circumstances, etc. The categories will be
used to calculate the diversity of the cited evidence.
5. For each candidate subset of 8 items from the result set compiled in step 3 as assessed in
step 4, determine the α-DCG. Take the maximum value as the denominator for computing
α-nDCG.
The reason for including all Performer outputs as candidates for the denominator of the α-nDCG
metric is a recognition that T&E may not a priori find the maximal set of diverse, relevant evidence
for the Challenge Problem in the corpus. It is possible that Performer systems will identify
evidence not located in a manual search.
TA2 has two metrics: Reasoning Explanation Quality (REQ) and F1. REQ will assess the
explainability of the identified strengths and weaknesses. T&E raters will evaluate the correctness
and clarity of each explanation of a reasoning strength or weakness on a 1-4 scale. Details for
assigning REQ scores will be provided at Program Kickoff in the Phase 1 T&E Plan.
T&E will measure Performer system’s identification of strengths and weaknesses in reasoning of
draft report evaluated using F1 Score, which gives credit for two features:
• If the system says X is a strength or weakness, is the system correct (i.e. is the system
output a true positive?) or is it wrong (i.e. the system output is a false positive).
• If X is a strength or weakness, does the system says so? (If not, then the system output is
a false negative)
14
TA3 has two metrics. The first is REASON Comment Quality (RCQ). T&E raters will evaluate
the comments provided by the Performer TA3 system. RCQ scores will be based on correctness,
appropriateness, and clarity of the comments, using a 1 (poor) - 4 (excellent) scale. Details for
assigning RCQ scores will be provided at Program Kickoff in the Phase 1 T&E Plan.
The second TA3 metric applies to the final exam. The finished analytic reports produced by the
human participants will be evaluated by T&E raters using Report Quality Score (RQS). RQS is
based on scores of six of the IC Analytic Tradecraft Standards: sourcing, uncertainty, assumptions,
alternatives, logic, and accuracy. Each finished report will be graded on each standard, with a range
from 1 (poor) to 4 (excellent), so RQS values range from 6 to 24. Each performer system’s RQS
will be compared to the RQS for the control group.
A summary of metric targets by Phase is shown in Table 1; these are subject to change over the
course of the program. Final Phase 1 metrics will be presented at kickoff.
Table 1: REASON Program Target Metrics
Task Metric Phase 1 TargetPhase 2 Target
TA1: Identify Additional
Evidence 𝝰𝝰-nDCG > 0.25 > 0.40
TA2: Identify Reasoning
Strengths and
Weaknesses
Reasoning Explanation Quality
(REQ) > 2.75 > 3.5
F1 > 0.65 > 0.80
TA3: Produce Comments
to Increase Quality of
Argumentation
REASON Comment Quality (RCQ) > 2.75 > 3.5
Report Quality Score (RQS) ΔRQS > 1.5 ΔRQS > 3.0
8. Program Waypoints, Milestones, and Deliverables
Waypoints, Milestones, and Deliverables are established from the Program’s onset to ensure
alignment with REASON objectives, organize research activities in a logical and reportable
manner, and facilitate consistent and efficient communication among all stakeholders – IARPA,
REASON T&E, USG Stakeholders, and Research Performers. A schedule of key program
milestones and deliverables in shown in Figure 1. 
15
Figure 1. Schedule of Key Milestones and Deliverables
a. Program Milestone, Waypoint, and Deliverables Timeline
Phase Month Event Description Comment Deliverable
1-2 All Waypoint Monthly Status
Report
Due on 15th of each
month
MSR
1-2 All Waypoint Progress and Status
Meeting
Monthly
teleconference with
REASON PM
N/A
1 1 Waypoint Kickoff Meeting DC Metro Area Presentation
Materials
1 1 Waypoint Sample Data Provided as GFI N/A
1 4 Waypoint Site Visit Performer Site N/A
1 5 Deliverable TA 1 and 2, Cycle 1 Performer system
output and software
Software Container
1 10 Deliverable TA 1 and 2, Cycle 2 Performer system
output and software
Software Container
1 12 Waypoint Site Visit Performer Site N/A
1 13 Waypoint PI Meeting DC Metro Area Presentation
Materials
1 14 Deliverable TA 3, Cycle 1 Performer system
output and software
Software Container
1 16 Waypoint Site Visit Performer Site N/A
1 18 Deliverable TA 1 and 2, Cycle 3 Performer system
output and software
Software Container
1 19 Deliverable TA 3, Final Exam Performer system
output and software
Software Container
16
Phase Month Event Description Comment Deliverable
1 22 Waypoint Site Visit Performer Site N/A
1 24 Deliverable Phase 1 Final
Software Delivery
Performer system
output and final
Phase 1 software
Software Container
1 24 Deliverable Phase 1 Final Report Report
2 25 Waypoint Kickoff Meeting DC Metro Area N/A
2 25 Waypoint Sample Data Provided as GFI N/A
2 27 Deliverable TA 3, Cycle 2 Performer system
output and software
Software Container
2 28 Waypoint Site Visit Performer Site N/A
2 29 Deliverable TA 3, Cycle 4 Performer system
output and software
Software Container
2 31 Deliverable TA 1 and 2, Cycle 4 Performer system
output and software
Software Container
2 32 Waypoint PI Meeting DC Metro Area Presentation
Materials
2 33 Waypoint Site Visit Performer Site N/A
2 34 Deliverable TA 3, Cycle 3 Performer system
output and software
Software Container
2 38 Deliverable TA 3, Final Exam Performer system
output and software
Software Container
2 39 Waypoint Site Visit Performer Site N/A
2 41 Waypoint PI Meeting DC Metro Area Presentation
Materials
2 42 Deliverable Phase 2 Final
Software Delivery
Software Container
2 42 Deliverable Phase 2 Final Report Report
b. Software Deliverable Formatting
Performers will be required to provide algorithm and software deliverables (including source code
and executables) in a manner that conforms to a standardized industrial method or methods that
will be provided at Program Kickoff. To facilitate planning, Offerors may assume that the
standardized configuration will require the use of software containerization technology (e.g.,
Docker and a REST API). This means that the entirety of a Performer’s system for TA1, TA2, and
TA3 REASON Comment Quality evaluations, including pre- and post-processing, must be
included within the delivered software container. These systems must be able to accept inputs in
the form of Challenge Problems from an API to be developed by the T&E team and to submit
outputs to that API. All official evaluations performed by T&E will use the computational 
17
resources available on the testbeds to be developed by T&E. Performers are not required to
identify or estimate the costs for these resources.
For TA3 Final Exams, the portion of Performer software facing analysts will be required to run
within a word processing application. For planning purposes, Offerors may assume that this will
be a Microsoft Word 365 add-in. These TA3 components will be permitted to access containerized
TA1 and TA2 components running on the same testbed. They will not be permitted to access
resources outside of the testbed.
For software that includes models that require initial training, the expectation is for the initial
model training to occur on Performer systems, with the ability for the T&E Team to re-train and
test the model with the same and/or other data.
If Offerors plan to use cloud computing resources for model development and training, they should
include descriptions of these requirements in their technical approach descriptions. Retraining of
Performer systems for T&E purposes will be subject to limitations on system retraining time and
resources. Those limitations will be briefed at Program Kickoff. Offerors must specify the runtime
resources and services required for their delivered software in terms equivalent to a configuration
on either Amazon Web Services, Microsoft Azure, or Google Cloud.
Each team is required to include among their Key Personnel a Lead System Integrator (LSI) who
shall be responsible for preparing software deliverable subcomponents, modules, and systems,
performing quality control of deliverables, and integrating key components into the primary
REASON system(s). The LSI will also oversee communication and coordination across a
Performer’s research teams including subcontractors, if applicable, to ensure that research products
are functional, integrated and following software coding best practices (e.g., inline comments,
documentation). Additional team members and roles are dependent on the proposed research, as
such, there is no predetermined or required skill mix.
c. Program API
The REASON Program will use a standardized API for all software deliverables and evaluations.
The first version of the REASON API will be provided to Performers at the Phase 1 Kickoff
Meeting and updated periodically thereafter. The API will define function calls and data structures
for operating and evaluating REASON software in a standardized manner. The API will be
functionally identical for unclassified and classified testing. Specifically, the API will provide
access to the document corpus for automated, unsupervised retraining of Performer systems,
delivery of the Challenge Problems used in T&E evaluations, and submission of result sets for
Challenge Problems.
d. End of Phase Final Reports
At the end of each Program Phase Performers will be required to submit a comprehensive Final
Report that describes their efforts and results during the Phase. These reports shall include an
executive summary, a description of the technical approach taken, details on the results, findings,
and technical insights gained from the R&D effort, lessons learned, and suggested future research
directions. The Final Report shall also include high level system design documentation for the
final software deliverable. This design documentation shall include any hardware requirements 
18
and dependencies on third-party software libraries.
9. Meeting, Travel, and Publication Requirements
Performers are expected to assume responsibility for administration of their projects and to comply
with contractual and program requirements for reporting, attendance at program workshops, and
availability for site visits. The following paragraphs describe typical expectations for meetings and
travel for IARPA programs as well as the contemplated frequency and locations of such meetings.
In addition to ensuring that all necessary details of developed software, algorithm, and operational
instructions are clear and complete, each Performer will be required to be available for questions
and troubleshooting from the T&E Team via electronic mail or in periodic technical exchange
meetings.
a. Workshops
All Performer teams are expected to attend workshops, to include Key Personnel from prime and
subcontractor organizations.
The REASON Program intends to hold a program Kickoff Meeting workshop in the first month
of the program and first month of the subsequent program phase. In addition, the program will
hold a PI Review Meeting at the end of each phase and at the phase midpoint. Kickoff Meetings
and PI Review Meetings may be combined for logistical convenience.
Both types of meetings will likely be held in the Washington, D.C. metropolitan area, but IARPA
may opt to co-locate the meeting with a relevant external conference or workshop to increase
synergy with stakeholders. IARPA reserves the right to hold the meeting virtually for logistical or
health and safety reasons.
Kickoff Meetings will typically be one day in duration and will focus on plans for the coming
Phase, Performer planned research, and internal program discussions. PI Review Meetings will
typically be two days in duration and will have a greater focus on communicating program progress
and plans to USG stakeholders. These meetings will include additional time allocated to
presentation and discussion of research accomplishments.
In both cases, the workshops will focus on technical aspects of the program and on facilitating
open technical exchanges, interaction, and sharing among the various program participants.
Program participants will be expected to present the technical status and progress of their projects
to other participants and invited guests. Individual sessions for each Performer team with the
REASON Program Manager and the T&E Team may be scheduled to coincide with these
workshops. Non-proprietary information will be shared by Performers in the open meeting
sessions; proprietary information sharing shall occur during individual breakout sessions with the
REASON Program Manager and the T&E team.
b. Site Visits
Site visits by the Government Team will generally take place semiannually during the life of the
program. These visits will occur at the Performer’s facility and last no longer than two days.
Reports on technical progress, details of successes and issues, contributions to the program goals, 
19
and technology demonstrations will be expected at such site visits. IARPA reserves the right to
conduct additional site visits on an as-needed basis.
c. Publication Approval
It is anticipated that research funded under this program will be unclassified research that will not
require a pre-publication review. However, performers should note that pre-publication approval
of research information associated with IARPA may be required if it is determined that the release
of such information may result in the disclosure of sensitive information. Prior to public release, a
courtesy soft copy of any work submitted for publication must be provided to the IARPA Program
Manager and the Contracting Officer Representative (COR), as well as a copy of the publication.
10. Period of Performance
The REASON program is envisioned as a 42-month effort that is intended to begin November 1,
2023.
Phase 1 (Base Period): November 1, 2023 – October 31, 2025
Phase 2 (Option 1): November 1, 2025 - April 30, 2027
11. Place of Performance
Performance will be conducted at the Performers’ sites.
12. Security
Proposals must be entirely unclassified. If a proposer wishes to cite prior classified efforts, they
may only provide an unclassified summary of this work.
All Performer work will be unclassified. Performer systems will be tested using classified data,
but Performers will not be able to review that classified data. Performers will be provided with
unclassified summary results from classified testing. Even if a Performer has cleared personnel,
they will not receive additional classified feedback.
13. Human Subjects Research
Performer human subjects research for REASON is encouraged, but not required. Performers
planning on conducting human subjects research as part of their technical approach must identify
this in their proposal, along with plans for obtaining Institutional Review Board (IRB) approval.
IRB approval documents must be provided to the Government before commencing any internal
human subjects research. DFARS clause 252.235-7004 is applicable to this solicitation and will
be included in any resultant contract award that support research that includes or may include
human subjects research.
Performers are not responsible for obtaining IRB approval for official T&E evaluation events. For
these events the T&E organization will obtain the necessary approvals.
20
B. Federal Award Information
Anticipated awards will be made in the form of procurement contracts and are subject to the
availability of appropriations. Multiple awards are anticipated. Funding for the Option Period will
be contingent upon satisfactory performance and the availability of funds.
The BAA shall result in selection of proposals addressing all phases of REASON and awarding of
funds aligning with Phase 1 research activities. Funding for the Option Period shall depend upon
performance during the Base Period (and succeeding Option Period) against the program goals
and metrics, the availability of funding, and IARPA priorities. Funding of the Option Period is at
the sole discretion of the Government.
The Government reserves the right to select for negotiation all, some, one, or none of the proposals
received in response to this solicitation and to make awards without discussions with offerors. The
Government also reserves the right to conduct discussions if it is deemed necessary. Additionally,
the Government reserves the right to accept proposals in their entirety or to select only portions of
proposals for negotiations of award, in the event that the Government desires to award only
portions of a proposal.
Awards under this BAA shall be made to offerors on the basis of the Evaluation Criteria listed in
Section E.1 of the BAA, as well as program balance, and availability of funds. Proposals selected
for negotiation may result in a procurement contract.
The Government shall contact offerors whose proposals are selected for negotiations to obtain
additional information for award. The Government may establish a deadline for the close of factfinding and negotiations that allows a reasonable time for the award of a contract. Offerors that
are not responsive to Government deadlines established and communicated with the request will
be removed from award consideration. Offerors will also be removed from award consideration
should the parties fail to reach agreement within a reasonable time on contract terms, conditions,
and cost/price.
The ACC-APG RTP Division has the authority to award a variety of instruments on behalf of
ARL-ARO. The ACC-APG RTP Division reserves the right to use the type of instrument most
appropriate for the effort proposed. Applicants should familiarize themselves with these
instrument types and the applicable regulations before submitting a proposal. Following is a brief
description of the possible award instrument.
1. Procurement Contract. A legal instrument, consistent with 31 U.S.C. 6303, which reflects a
relationship between the Federal Government and a State Government, a local government, or
other entity/contractor when the principal purpose of the instrument is to acquire property or
services for the direct benefit or use of the Federal Government.
Contracts are primary governed by the following regulations:
a. Federal Acquisition Regulation (FAR) https://www.acquisition.gov/browse/index/far 
21
b. Defense Federal Acquisition Regulation Supplement (DFARS)
https://www.federalregister.gov/defense-federal-acquisition-regulation-supplementdfarsc. Army Federal Acquisition Regulation Supplement (AFARS)
https://www.acquisition.gov/afars
C. Eligibility Information
1. Eligible Applicants:
All responsible sources capable of satisfying the Government's needs may submit a proposal.
Eligible applicants under this BAA include Institutions of higher education (foreign and domestic),
nonprofit organizations, and for-profit concerns (large and small businesses). Proposals are
encouraged from Historically Black Colleges and Universities (as determined by the Secretary of
Education to meet requirements of Title III of the Higher Education Act of 1965, as amended (20
U.S.C. §1061) and from Minority Institutions defined as institutions “whose enrollment of a single
minority or a combination of minorities exceeds 50 percent of the total enrollment.” [20 U.S.C. §
1067k(3) and 10 U.S.C. § 4144]. However, no funds are specifically allocated for HBCU/MI
participation.
Other Government Agencies, Federally Funded Research and Development Centers, University
Affiliated Research Centers, Government-Owned, Contractor-Operated facilities, Government
Military Academies, and any other similar type of organization that have a special relationship
with the Government, that gives them access to privileged and/or proprietary information or access
to Government equipment or real property, are not eligible to submit proposals under this BAA or
participate as team members under proposals submitted by eligible entities. An entity of which
only a portion has been designated as a UARC may be eligible to submit a proposal or participate
as a team member, subject to an organizational conflict of interest review.
Foreign entities and/or individuals may participate to the extent that such participants comply with
any necessary Non-Disclosure Agreements, Security Regulations, and all U.S. Export Control
Laws and regulations, and other governing statutes applicable under the circumstances to include
the International Traffic in Arms Regulations (ITAR), 22 CFR Parts 120 through 130, the Export
Administration Regulations (EAR), 15 CFE Parts 730 through 799, as amended, in the
performance of any future contract. Offerors are expected to ensure that the efforts of foreign
participants do not either directly or indirectly compromise the laws of the United States, nor its
security interests. As such, both foreign and domestic Offerors should carefully consider the roles
and responsibilities of foreign participants as they pursue teaming arrangements.
In the absence of available license exemptions or exceptions, the offeror shall be responsible for
obtaining the appropriate licenses or other approvals, if required, for exports of (including deemed
exports) hardware, technical data, and software, or for the provision of technical assistance. The
offeror shall be responsible for obtaining export licenses, if required, before utilizing foreign
persons in the performance of any future contract, including instances where the work is to be
performed on-site at any Government installation (whether in or outside the United States), where
the foreign person will have access to export-controlled technologies, including technical data or
software. The offerorshall be responsible for all regulatory record keeping requirements associated 
22
with the use of licenses and license exemptions or exceptions. The offeror shall appropriately mark
all contract deliverables controlled by ITAR and/or EAR.
Proposals will be evaluated only if they are for fundamental scientific study and experimentation
directed towards advancing the scientific state of the art or increasing basic knowledge and
understanding. Proposals focused on specific devices or components are beyond the scope of this
BAA.
1.A.1 Organizational Conflict of Interest (OCI)
According to FAR 2.101 “Organizational Conflict of Interest” means that because of other
activities or relationships with other persons, a person is unable or potentially unable to render
impartial assistance or advice to the Government, or the person’s objectivity in performing the
contract work is or might be otherwise impaired, or a person has an unfair competitive advantage.
In accordance with FAR 9.5, Offerors are required to identify and disclose all facts relevant to
potential OCIs involving the Offeror’s organization and any proposed team member (sub awardee,
consultant). Under this Section, the Offeror is responsible for providing this disclosure with each
proposal submitted pursuant to the BAA. The disclosure must include the Offeror’s, and as
applicable, proposed team member’s OCI mitigation plan. The OCI mitigation plan must include
a description of the actions the Offeror has taken, or intends to take, to prevent the existence of
conflicting roles that might bias the Offeror’s judgment and to prevent the Offeror from having an
unfair competitive advantage. The OCI mitigation plan will specifically discuss the disclosed OCI
in the context of each of the OCI limitations outlined in FAR 9.505-1 through FAR 9.505-4.
IARPA generally prohibits contractors/Performers from concurrently providing Scientific
Engineering Technical Assistance (SETA), Advisory and Assistance Services (A&AS) or similar
support services and being a technical Performer. Therefore, as part of the FAR 9.5 disclosure
requirement above, address whether an Offeror or an Offeror’s team member (e.g., sub awardee,
consultant) is providing SETA, A&AS, or similar support (e.g., T&E services) to IARPA under:
(a) a current award or subaward; or (b) a past award or subaward.
If SETA, A&AS, or similar support is or was being provided to IARPA, the proposal must include:
• The name of the IARPA program or office receiving the support;
• The prime contract number;
• Identification of proposed team member (sub awardee, consultant) providing the support.
As part of their proposal, Offerors shall include either (a) a copy of their OCI notification including
mitigation plan or (b) a written certification that neither they nor their subcontractor teammates
have any potential conflicts of interest, real or perceived. A sample certification is provided in
II.H.7.
The Government will evaluate OCIs and potential OCIs to determine whether they can be avoided,
neutralized or mitigated and/or whether it is in the Government’s interest to grant a waiver. The
Government will make OCI determinations, as applicable, for proposals that are otherwise
selectable under the BAA Evaluation Factors. 
23
The Government may require Offerors to provide additional information to assist the Government
in evaluating OCIs and OCI mitigation plans.
If the Government determines that an Offeror failed to fully disclose an OCI; or failed to provide
the affirmation of IARPA support as described above; or failed to reasonably provide additional
information requested by the Government to assist in evaluating the Offeror’s OCI and proposed
OCI mitigation plan, the Government may reject the proposal and withdraw it from consideration
for award.
1.A.2 Multiple Submissions to the BAA
Organizations may participate as a prime or subcontractor in more than one submission to the
BAA. However, if multiple submissions to the BAA which include a common team member are
selected, such common team members shall not receive duplicative funding (i.e., no one entity can
be paid twice to perform the same task).
1.A.3 U.S. Academic Institutions
According to Executive Order 12333, as amended, paragraph 2.7, “Elements of the Intelligence
Community are authorized to enter into contracts or arrangements for the provision of goods or
services with private companies or institutions in the United States and need not reveal the
sponsorship of such contracts or arrangements for authorized intelligence purposes. Contracts or
arrangements with academic institutions may be undertaken only with the consent of appropriate
officials of the institution.”
Offerors must submit a completed and signed Academic Institution Acknowledgement Letter for
each U.S. academic institution that is a part of their team, whether the academic institution is
serving in the role of a prime, or a subcontractor or a consultant at any tier of their team with their
technical proposal. Each Letter must be signed by a senior official from the institution (e.g.,
President, Chancellor, Provost, or other appropriately designated official). A template of the
Academic Institution Acknowledgement Letter is enclosed in II.H.2 of this BAA. Note that IARPA
shall not enter into negotiations with an Offeror whose team includes a U.S. academic institution
until all required Academic Institution Acknowledgment Letters are received.
2. Cost Sharing or Matching:
There is no requirement for cost sharing, matching, or cost participation to be eligible for award
under this BAA. Cost sharing and matching is not an evaluation factor used under this BAA.
3. Federally Funded Research and Development Centers and University Affiliated
Research Centers:
Federally Funded Research & Development Centers (FFRDCs), including Department of Energy
National Laboratories, and University Affiliated Research Centers (UARCs) are not eligible to
receive awards, as primes or sub-awardees, under this BAA.
D. Application and Submission Information
24
1. Addresses to View Broad Agency Announcement
This BAA may be accessed from the following:
a. SAM (https://sam.gov)
b. ARL website (https://www.arl.army.mil/business/broad-agency-announcements/)
c. IARPA website (https://www.iarpa.gov)
Amendments, if any, to this BAA will be posted to these websites when they occur. Interested
parties are encouraged to periodically check these websites for updates and amendments.
The following information is for those wishing to respond to the BAA:
2. Content and Form of Application Submission
a. General Information
A proposal submitted under this BAA must address unclassified fundamental research.
Proposal submissions will be protected from unauthorized disclosure in accordance with
applicable laws and DoD regulations. Applicants are expected to appropriately mark each
page of their submission that contains proprietary information. The participating DoD and
other USG agencies will provide no funding for direct reimbursement of proposal
development costs. Technical and cost proposals (or any other material) submitted in
response to this BAA will not be returned. It is the policy of participating DoD agencies to
treat all proposals as sensitive, competitive information and to disclose their contents only
for the purposes of evaluation.
Post-Employment Conflict of Interest: There are certain post-employment restrictions on
former federal officers and employees, including special government employees (Section
207 of Title 18, U.S.C.). If an applicant believes a conflict of interest may exist, the
situation should be discussed with Point of Contact listed in Section G: Agency Contacts,
who will then coordinate with appropriate ARO/ARL legal personnel prior to having
applicant expend time and effort in preparing a proposal.
Equipment: Normally, title to equipment or other tangible property purchased with
Government funds vests with nonprofit institutions of higher education or with nonprofit
research organizations if vesting will facilitate scientific research performed for the
Government. For profit organizations are expected to possess the necessary plant and
equipment to conduct the proposed research. Deviations may be made on a case-by-case
basis to allow commercial organizations to purchase equipment but disposition instructions
must be followed.
b. Proposal Format
To facilitate the evaluation of the proposal, the government encourages the offerors to
submit proposals which: are clear and concise; limited to essential matters sufficient to
demonstrate a complete understanding of the Government’s requirements; include
sufficient detail for effective evaluation; and provide convincing rationale to address how 
25
the offeror intends to meet these requirements and objectives, rather than simply rephrasing
or restating the Government’s requirements and objectives.
All proposals shall be in the format given below. Non-compliant proposals may be rejected
without review. Proposals shall consist of “Volume 1 - Technical and Management
Proposal” and “Volume 2 - Cost Proposal.” All proposals shall be written in English.
Additionally, text should be black and paper size 8-1/2 by 11-inch, white in color with 1”
margins from paper edge to text or graphic on all sides. The Government desires Times
New Roman font with font size not smaller than 12-point. The Government desires that the
font size for figures, tables and charts not be smaller than 10-point. All contents shall be
clearly legible with the unaided eye. Excessive use of small font, for other than figures,
tables, and charts, or unnecessary use of figures, tables, and charts to present information
may render the proposal non-compliant. Front and backside of a single sheet are counted
as two (2) pages if both sides are printed upon. Foldout pages are not permitted. The page
limitation for full proposals includes all figures, tables, and charts. All pages should be
numbered. No other materials may be incorporated in any portion of the proposal by
reference, as a means to circumvent page count limitations. All information pertaining to a
volume shall be contained within that volume. Any information beyond the page
limitations will not be considered in the evaluation of offerors.
The Government anticipates proposals submitted under this BAA will be
UNCLASSIFIED.
The Technical and Management proposal submitted in response to this BAA shall consist
of the following:
Volume 1 – Technical & Management Proposal
Section 1 - Cover Sheet - Technical (see Section II.H) & Transmittal Letter (not included
in page count)
Section 2 – Summary of Proposal, not to exceed 5 pages
Section 3 – Detailed Proposal, not to exceed 30 pages
Section 4 – Attachments (Not included in page count of Volume 1, but numbered
appropriately for elements included. Templates are in Section II.H of this BAA.)
i. Academic Institution Acknowledgment Letter, if required
ii. IP Rights, estimated not to exceed 4 pages
iii. OCI Notification or Certification
iv. Bibliography
v. Relevant Papers (up to three)
vi. Consultant Letters of Commitment
vii. Human Use Documentation
viii. A Three Chart Summary of the Proposal
ix. Research Data Management Plan (RDMP), estimated not to exceed 3 pages
x. Privacy Plan, no page limit
xi. ARO BAA Forms
26
Volume 1: Technical and Management Proposal
Volume 1, Technical and Management Proposal, may include an attached bibliography of relevant
technical papers or research notes (published and unpublished) which document the technical ideas
and approach on which the proposal is based. Copies of not more than three relevant papers can
be included with the submission. The submission of other supporting materials along with the
proposal is strongly discouraged and shall not be considered for review.
Except for the cover sheet, transmittal letter, table of contents (optional), and the required
attachments stated in the BAA, Volume 1 shall not exceed 35 pages. Any pages exceeding this
limit shall be removed and not considered during the evaluation process. Full proposals should be
accompanied by an official transmittal letter, using contractor format. All full proposals shall be
written in English.
Section 1: Cover Sheet & Transmittal Letter
a. Cover Sheet: (See Section II.H for template)
b. Official Transmittal Letter
The transmittal letter shall include the following (not to exceed one page): Introduction of offeror
and team (subcontractors and consultants), the BAA number, IARPA program name, offerors’
Program name, the proposal validity period, the type of contract vehicle being requested
(procurement contract) with a short rationale, any non-negotiable conditions on which the offer is
based such as contract type (cost type, FFP), IP restrictions, etc., and the offeror’s points of contact
information including: name, email and phone number for both technical and administrative issues.
Note: Any information required elsewhere in the proposal must be included in the appropriate
section of the proposal (i.e., including the information in the transmittal letter alone may not be
sufficient). If there is a conflict between the transmittal letter and the proposal the proposal shall
control.
Section 2: Summary of Proposal (not to exceed 5 pages)
Section 2 shall provide an overview of the proposed work as well as introduce associated technical
and management issues. This section shall contain a technical description of technical approach to
the research as well as a succinct portrayal of the uniqueness and benefits of the proposed work. It
shall make the technical objectives clear and quantifiable and shall provide a project schedule with
definite decision points and endpoints.
Offerors shall address:
A. A technical overview of the proposed research and plan. This section is the centerpiece of
the proposal and shall succinctly describe the proposed approach and research. The
overview shall provide an intuitive understanding of the approach and design, technical
rationale, and constructive plan for accomplishment of technical objectives and deliverable
production. The approach shall be supported by basic, clear calculations. Additionally,
proposals shall clearly explain the innovative claims and technical approaches that shall be 
27
employed to meet or exceed each program metric and provide ample justification as to why
approaches are feasible. The use of non-standard terms and acronyms should be avoided.
This section shall be supplemented with a more detailed plan in Volume 1, Section 3 of the
proposal.
B. Summary of the products, transferable technology and deliverables associated with the
proposed research results. Define measurable deliverables that show progress toward
achieving the stated Program Milestones. All proprietary claims to the results, prototypes,
intellectual property, or systems supporting and/or necessary for the use of the research,
results, and/or prototype shall be detailed in Volume 1 - Section 4 - IP Rights. If there are
no proprietary claims, this should be stated. Should no proprietary claims be made,
Government rights shall be unlimited to any resultant IP.
C. Schedule and milestones for the proposed research. Summarize, in table form and clearly
legible for all activity, the schedule and milestones for the proposed research. Do not
include proprietary information with the milestones. If designed as a Gantt chart or large
table, a representative image of the information can be embedded as a small image,
referencing an appendix Excel file of the entire schedule and milestones list.
D. Related research. General discussion of other research in this area, comparing the
significance and plausibility of the proposed innovations against competitive approaches
to achieve Program objectives.
E. Project contributors. Include a clearly defined and clearly legible organizational chart of
all anticipated project participants, organized under functional roles for the effort, and also
indicating associated task number responsibilities with individuals.
F. Technical Resource Summary:
• Summarize total level of effort by labor category and technical discipline (i.e., research
scientist/chemist/physicist/engineer/administrative, etc.) and affiliation (prime/
subcontractor/consultant). Key Personnel shall be identified by name. Provide a brief
description of the qualifications for each labor category (i.e., education, certifications,
years of experience, etc.)
• Summarize level of effort by labor category and technical discipline for each major
task.
• Identify software and intellectual property required to perform, by affiliation (list each
item separately)
• Identify materials and equipment (such as IT) required to perform, by affiliation (list
each item separately)
• Identify any other resources required to perform (i.e., services, data sets, data set
repository, facilities, government furnished property, etc.), by affiliation (list each item
separately)
• Summarize level of effort required to prepare research data for public access.
• Estimated travel, including purpose of travel and number of personnel per trip, by
affiliation.
• The above information shall cross reference to the tasks set forth in the offerors
statement of work, and shall be supported by the detailed cost and pricing information
provided in the offeror's Volume 2 Cost Proposal. 
28
Section 3: Detailed Proposal Information (Up to 30 pages)
This section of the proposal shall provide the detailed, in-depth discussion of the proposed research
as well as supporting information about the offeror’s capabilities and resources. Specific attention
shall be given to addressing both the risks and payoffs of the proposed research and why the
proposed research is desirable for IARPA to pursue. This part shall provide:
A. Statement of Work (SOW) - In plain English, clearly define the technical tasks and subtasks
to be performed, their durations and the dependencies among them. A template will be
provided to assist in the development of consistent SOWs for all proposals. (See Section
II, H for an example). For each task and sub-task, provide:
• A general description of the objective;
• A detailed description of the approach to be taken, developed in an orderly progression
and in enough detail to establish the feasibility of accomplishing the goals of the task;
• Identification of the primary organization responsible for task execution (prime,
subcontractor, team member, etc.) by name;
• The exit criteria for each task/activity (i.e., a product, waypoint or milestone that
defines its completion); and
• Identification and definition of all deliverables (e.g., data (including public access),
reports, software, etc.) to be provided to the Government in support of the proposed
research tasks/activities.
Note: Do not include any proprietary information in the SOW.
At the end of this section of the proposal, provide a Gantt chart, showing all the tasks and
sub-tasks on the left with the performance period (in years/quarters) on the right. All
milestones shall be clearly labeled on the chart. If necessary, use multiple pages to ensure
legibility of all information.
B. A detailed description of the objectives, scientific relevance, technical approach and
expected significance of the work. The key elements of the proposed work should be
clearly identified and related to each other. Proposals should clearly detail the technical
methods and/or approaches that shall be used to meet or exceed each program milestone,
and should provide ample justification as to why the proposed methods/approaches are
feasible. Any anticipated risks should be described and possible mitigations proposed.
General discussion of the problem without detailed description of approaches, plausibility
of implementation, and critical metrics shall result in an unacceptable rating.
C. State-of-the-art. Comparison with other on-going research, highlighting the uniqueness of
the proposed effort/approach and differences between the proposed effort and the current
state-of-the-art. Identify advantages and disadvantages of the proposed work with respect
to potential alternative approaches. 
29
D. Data sources. Identification and description of data sources to be utilized in pursuit of the
project research goals.
Offerors proposing to use existing data sets shall provide written verification that all data
were obtained in accordance with U.S. laws and, where applicable, are in compliance with
End User License Agreements, Copyright Laws, Terms of Service, and laws and policies
regarding privacy protection of U.S. Persons. Offerors shall identify any restrictions on the
use or transfer of data sets being used, and, if there are any restrictions, the potential cost
to the Government to obtain at least Government Purpose Rights in such data sets.
Offerors proposing to obtain new data sets shall ensure that their plan for obtaining the data
complies with U.S. Laws and, where applicable, with End User License Agreement,
Copyright Laws, Terms of Service, and laws and policies regarding privacy protection of
U.S. Persons. Foreign offerors must ensure that their plan for obtaining the data complies
with the privacy protections applicable within the country that they are based in, as well.
While not necessary, if offerors propose using human samples they must include the
documentation required for Institutional Review Board (IRB) approval for use of Human
samples or declaration of why IRB approval is not necessary. Documentation must be well
written and logical; claims for exemptions from Federal regulations for human subject
protection must be accompanied by a strong defense of the claims. The Human Use
documentation and the written verification are not included in the total page count.
The Government reserves the right to reject a proposal if it does not appropriately address
all data issues.
E. Deliverables: Deliverables are identified in Section II of the BAA.
The Government requires, at a minimum, Government Purpose Rights for all deliverables
developed with mixed funding or that incorporate technical data or computer software
developed at private expense; anything less shall be considered a weakness in the proposal.
All other deliverables shall be delivered with unlimited rights in accordance with FAR
clause 52.227-14.
In the “Restrictions on Intellectual Property Rights” attachment of the proposal, offerors
shall describe the proposed approach to intellectual property for all deliverables, together
with a supporting rationale of why this approach is in the Government’s best interest. This
shall include all proprietary claims to the results, prototypes, intellectual property or
systems supporting and/or necessary for the use of the research, results and/or prototype,
and a brief explanation of how the offerors may use these materials in their program. To
the greatest extent feasible, offerors should not include background proprietary technical
data and computer software as the basis of their proposed technical approach.
If offerors (including their proposed teammates) desire to use in their proposed approach,
in whole or in part, technical data or computer software or both that is proprietary to the
offeror, any of its teammates, or any third party, in the “Restrictions on Intellectual
Property Rights” attachment they should: (1) clearly identify such data/software and its 
30
proposed particular use(s); (2) identify and explain any and all restrictions on the
Government’s ability to use, modify, reproduce, release, perform, display, or disclose
technical data, computer software, and deliverables incorporating such technical data and
computer software; (3) identify the potential cost to the Government to acquire GPR in all
deliverables that use the proprietary technical data or computer software the offeror intends
to use; (4) explain how the Government shall be able to reach its program goals (including
transition) within the proprietary model offered; and (5) provide possible nonproprietary
alternatives in any area in which a Government entity would have insufficient rights to
transfer, within the Government or to Government contractors in support of a Government
purpose, deliverables incorporating proprietary technical data or computer software, or that
might cause increased risk or cost to the Government under the proposed proprietary
solutions.
Offerors also shall identify all commercial technical data and/or computer software that
may be embedded in any noncommercial deliverables contemplated under the research
effort, along with any applicable restrictions on the Government’s use of such commercial
technical data and/or computer software. If offerors do not identify any restrictions, the
Government shall assume that there are no restrictions on the Government’s use of such
deliverables. Offerors shall also identify all noncommercial technical data and/or computer
software that it plans to generate, develop and/or deliver under any proposed award
instrument in which the Government shall acquire less than unlimited rights. If the offeror
does not submit such information, the Government shall assume that it has unlimited rights
to all such noncommercial technical data and/or computer software. Offerors shall provide
a short summary for each item (commercial and noncommercial) asserted with less than
unlimited rights that describes the nature of the restriction and the intended use of the
intellectual property in the conduct of the proposed research.
Additionally, if offerors propose the use of any open source or freeware, any conditions,
restrictions or other requirements imposed by that software shall also be addressed in the
“Restrictions on Intellectual Property Rights” attachment. Offerors should review the
example format, found in Section II.H for their response. The technical content of the
“Restrictions on Intellectual Property Rights” attachment shall include only the
information necessary to address the proposed approach to intellectual property; any other
technical discussion in the attachment shall not be considered during the evaluation
process. The attachment is estimated not to exceed 4 pages.
For this solicitation, the Government recognizes only the definitions of intellectual
property rights in accordance with the terms as set forth in the Federal Acquisition
Regulation (FAR) part 27, or as defined herein. If offerors propose intellectual property
rights that are not defined in FAR part 27 or herein, offerors shall clearly define such rights
in the “Restrictions on Intellectual Property Rights” attachment of their proposal. Offerors
are reminded of the requirement for prime contractors to acquire sufficient rights from
subcontractors to accomplish the program goals.
“Research data” is defined herein as “the digital recorded factual material commonly
accepted in the scientific community as necessary to validate research findings including 
31
data sets used to support scholarly publications, but does not include laboratory notebooks,
preliminary analyses, drafts of scientific papers, plans for future research, peer review
reports, communications with colleagues, or physical objects, such as laboratory
specimens.”
F. Cost, schedule, Milestones
Describe the cost, schedule, and milestones for the proposed research, including cost
estimates by cost element for base period, the option period(s) and the total program
summary, and company cost share, if any, as well as, costs by technical area(s) and tasks
(see tables below for sample format). The milestones shall not include proprietary
information (Offeror can use their own format for milestones).
SAMPLE FORMAT
Cost Element
(Burdened)
Phase 1 – Base
(24 Months)
Phase 2 – Option
(18 months)
Labor
Subcontracts/Consultant
Materials & Equipment
Travel
Other Direct Costs
(Cost Share, if any)
Total
G. Offeror’s previous accomplishments.
Discuss previous accomplishments and work in this or closely related research areas and
how these will contribute to and influence the current work.
H. Facilities.
Describe the facilities that shall be used for the proposed effort, including computational
and experimental resources.
I. Detailed Management Plan.
Provide the Management Plan that clearly identifies both organizations and individuals
within organizations that make up the team, and delineate the expected duties, relevant
capabilities, and task responsibilities of team members and expected relationships among
team members. Identify the expected levels of effort (percentage time, or fraction of an
FTE) for all Key Personnel and significant contributors. Additionally, include a description
of the technical, administrative, and business structure of the team along with an internal
communications plan. Describe project/function/sub-contractor relationships (including
formal teaming agreements), Government research interfaces, and planning, scheduling,
and control practices utilized, as well as the team leadership structure. Provide a brief
biography of all Key Personnel (including alternates, if desired) and significant
contributors who shall be involved in the research along with the amount of effort to be
expended by each person during the year. Participation by all Key Personnel and significant 
32
contributors is expected to exceed 25% of their time. A compelling explanation is required
for any variation from this figure.
If the team intends to use consultants, they shall also be included in the organizational chart
with an indication of whether the person shall be an “individual” or “organizational”
consultant (i.e., representing themselves or their organization), and organizational
affiliation.
See Section H for the recommended format.
J. Resource Share.
Include the type of support, if any, the Offeror might request from the Government, such
as facilities, equipment, materials, or any such resources the Offeror is willing to provide
at no additional cost to the Government to support the research effort. Cost sharing is not
required from Offerors and is not an evaluation criterion but is encouraged where there is
a reasonable probability of a potential commercial application related to the proposed
research and development effort.
K. The names of other federal, state or local agencies or other parties receiving the proposal
and/or funding the proposed effort.
If none, state “None”. Concurrent submission of the proposal to other organizations will
not prejudice its review but may impact IARPA’s decision to fund the effort.
L. Research Data Management Plan. (RDMP).
Submit a RDMP that outlines how they will manage and preserve the Research Data, as
defined below, collected or produced through the course of performance. The RDMP need
not require the preservation of all Research Data: Offerors shall consider the cost and
benefits of managing and preserving the Research Data in determining whether to preserve
it. At a minimum, all Research Data associated with a peer-reviewed manuscript or final
published article (hereinafter “Publications”) must be made publicly accessible by the
award recipient before, on or at a reasonable time after the publication date. The
Publications whose associated data must be covered by the RDMP are deliverables as
described in Section 1.
Research Data is defined herein as the digital recorded factual material commonly accepted
in the scientific community as necessary to validate research findings including data sets
used to support scholarly publications, but does not include laboratory notebooks,
preliminary analyses, drafts of scientific papers, plans for future research, peer review
reports, communications with colleagues, or physical objects, such as laboratory
specimens.
The RDMP must address the following:
• Describe the types of Research Data collected or produced in the course of the
project. Include standards to be used for Research Data and metadata content and 
33
format.
• A plan for making the Research Data that underlie Publications digitally accessible
to the public before or, at the time of publication or conference presentation, or
within a reasonable time after publication. The requirement could be met by
including the data as supplementary information to the Publication or by depositing
the Research Data in a searchable, machine-readable and digitally accessible form
suitable for repositories available to the public free of charge. Such repositories
could be discipline-specific repositories, general purpose research data repositories
or institutional repositories. The published article or conference paper should
indicate how the public may access Research Data underlying the paper’s results
and findings. Offerors should attempt to make the Research Data available for at
least three years after published article or conference. (NOTE: Offerors shall make
a best effort in identifying research data sets that may be used for Publications that
occur after contract end. The Offeror shall deliver these data sets to the Government
and make them available in repositories available to the public prior to the end of
the period of performance, if not included as supplementary information to
Publications.)
• Policies and provisions for sharing and preservation, including a) policies and
provisions for appropriate protection of privacy, confidentiality, security, and IP,
b) descriptions of tools, including software, needed to access and interpret the
Research Data, and c) policies and provisions for re-use, re-distribution, and
production of derivatives.
• If, for legitimate reasons (e.g., privacy, confidentiality, security, IP rights
considerations; size of data sets, cost; time), the Research Data underlying the
results of peer-reviewed publications or conference papers cannot be shared and
preserved, the plan must include a justification citing such reasons.
In addressing these elements (e.g., types of data to be shared and preserved, standards to
be used for data and metadata, repositories to be used for archiving data, timeframes for
sharing and preservation), the RDMP should reflect the best practices of the relevant
scientific discipline and research community. At a minimum, Research Data underlying
Publications and associated metadata shall include an acknowledgement of IARPA support
and a link to the associated Publication.
Section 4: Attachments
[Note: The attachments listed below shall be included with the proposal, under Volume 1, if
applicable, but do not count against the Volume 1 page limit. For attachments which are not
applicable, Offerors must still include a statement of “Attachment [X]: Not applicable”.]
A. Attachment 1: Signed Academic Institution Acknowledgement Letter(s) (if applicable). A
template is provided in Section II.H.
B. Attachment 2: IP Rights. A template is provided in Section II.H.
This attachment is estimated not to exceed 4 pages and shall address the following:
Representation as to Rights. An Offeror shall provide a good faith representation that they 
34
either own or have sufficient licensing rights to all IP that will be utilized under their
proposal. Program-Specific IP Approach. The Government requires sufficient rights to IP
developed or used in the conduct of the proposed research to ensure that the Government
can successfully: (a) manage the program and evaluate the technical output and
deliverables, (b) communicate program information across Government organizations, and
(c) support transition to and further use and development of the program results by
Intelligence community (IC) users and others. The Government anticipates that achieving
these goals for the REASON program may necessitate a minimum of Unlimited Rights in
all deliverables. However, there may be any number of other approaches to intellectual
property rights to achieve IARPA’s program goals. “Unlimited rights” means the rights of
the Government to use, disclose, reproduce, prepare derivative works, distribute copies to
the public, and perform publicly and display publicly, in any manner and for any purpose,
and to have or permit others to do so. In addressing their approach to IP rights, Offerors
should: (1) describe the intended use of patented invention(s) or data, including, technical
data and computer software, in the conduct of the proposed research; (2) describe the rights
being offered to the Government along with a justification if less than Unlimited Rights is
being offered; (3) explain how IARPA will be able to reach its program goals (including
transition) with the rights offered to the Government; (4) identify the cost to the
Government to acquire additional or alternative rights beyond those being offered, if
applicable; and (5) provide possible alternatives in any area in which the offered rights may
be insufficient for the Government to achieve its program goals (e.g., the possibility of
future licensing of privately-developed software to U.S. Government agencies at a
reasonable cost.)
Patented Inventions. Offerors shall include documentation using the format provided in
Section II.H, proving ownership of or sufficient rights to all inventions (or inventions for
which a patent application has been filed) that will be utilized under the proposal for the
IARPA program. If a patent application has been filed for an invention that the proposal
utilizes, but the application has not yet been made publicly available and contains
proprietary information, the Offeror may provide only the serial number, inventor
name(s), assignee names (if any), filing date, filing date of any related provisional
application, and a summary of the patent title, together with either: (1) a representation
that the Offeror owns the invention, or (2) proof of sufficient licensing rights in the
invention. Offerors shall also indicate their intention to incorporate patented technology
into any deliverable—i.e., if Offerors intend for any deliverable to embody any invention
covered by any patent or patent application the Offerors listed in Volume 1, Attachment
2, Offerors should also specify in the Attachment the deliverable into which the Offerors
expects to incorporate the invention. In doing so, the Government requests that Offerors
further specify any rights offered to the Government for inventions that shall be utilized
in the program (beyond the implied license that accompanies a patent owner’s sale of a
patented product).
Noncommercial Data. Offerors shall identify all noncommercial data, including technical
data and computer software, that it plans to generate, develop and/or deliver under any
proposed award instrument in which the Government shall acquire less than unlimited
rights. In doing so, Offerors must assert: (a) the specific restrictions the Government’s 
35
rights in those deliverables, (b) the basis for such restrictions, (c) the intended use of the
technical data and noncommercial computer software in the conduct of the proposed
research and development of applicable deliverables, and (d) a supporting rationale of why
the proposed approach to data rights is in the Government’s best interest (please see
program specific goals above). If no restrictions are intended, then the Offeror shall state
“NONE.”
Commercial Data. Offerors shall identify all commercial data, including technical data
and commercial computer software, that may be included in any deliverables
contemplated under the research effort and assert any applicable restrictions on the
Government’s use of such commercial data (please see program specific goals above). If
no restrictions are intended, then the Proposer shall state “NONE.”
Data Developed with Mixed Funding. If mixed funding is anticipated in data generated,
developed, and/or delivered under the research effort, the Government seeks at minimum
“Government Purpose Rights” (GPR) for all noncommercial data deliverables; offering
anything less shall be considered a weakness in the proposal. United States Government
purposes include any activity in which the United States Government is a party,
including cooperative agreements with international or multinational defense
organizations, or sales or transfers by the United States Government to foreign
governments or international organizations. Government purposes include competitive
procurement, but do not include the rights to use, modify, reproduce, release, perform,
display, or disclose technical data or computer software for commercial purposes or
authorize others to do so. Government Purpose Rights continue for a five-year period
upon execution of the contract, and upon expiration of the five-year period, the
Government obtains Unlimited Rights in the data.
Open Source. If Offerors propose the use of any open-source data or freeware, any
conditions, restrictions or other requirements imposed by that software shall also be
addressed. Offerors should leverage the format in Section II.H for their response.
Identification of Relevant Government Contracts. For all technical data and computer
software that an Offeror intends to deliver with other than unlimited rights that are
identical or substantially similar to technical data and computer software that the Offeror
has produced for, delivered to, or is obligated to deliver to the Government under any
contract or subcontract, the Offeror shall identify: (a) the contract number under which
the data, software, or documentation was produced; (b) the contract number under
which, and the name and address of the organization to whom, the data and software was
most recently delivered or shall be delivered; and (c) any limitations on the
Government’s rights to use or disclose the data and software, including, when
applicable, identification of the earliest date the limitations expire.
Definitions. For this solicitation, IARPA recognizes only the definitions of IP rights in
accordance with the terms as set forth in the Federal Acquisition Regulation (FAR) part
27 or as defined herein. If Offerors propose IP rights that are not defined in FAR part 27
or herein, Offerors shall clearly define such rights in the “Intellectual Property Rights” 
36
Attachment of their proposal. Offerors are reminded of the requirement for prime
contractors to acquire sufficient rights from subcontractors to accomplish the program
goals.
Evaluation. The Government may use the asserted data rights during the evaluation
process to evaluate the impact of any identified restrictions. The technical content of the
“Intellectual Property Rights” Attachment shall include only the information necessary
to address the proposed approach to IP; any other technical discussion in the attachment
shall not be considered during the evaluation process.
C. Attachment 3: OCI Notification or Certification Template provided in Section II.H.
D. Attachment 4: Bibliography. A brief bibliography of relevant technical papers and research
notes (published and unpublished) which document the technical ideas on which the
proposal is based.
E. Attachment 5: Relevant Papers. Copies of not more than three relevant papers may be
included in the submission. The Offerors shall include a one-page technical summary of
each paper provided, suitable for individuals who are not experts in the field.
F. Attachment 6: Consultant Commitment Letters.
G. Attachment 7: Human Use Documentation.
H. Attachment 8: A Three Chart Summary of the Proposal. A PowerPoint summary that
quickly and succinctly indicates the concept overview, key innovations, expected impact,
and other unique aspects of the proposal. The format for the summary slides is included in
Section II.H to this BAA and does not count against the page limit. Slide 1 should be a
self-contained, intuitive description of the technical approach and performance. These
slides may be used during the evaluation process to present a summary of the proposal
from the Offeror’s view.
I. Attachment 9: RDMP (estimated as 2 to 3 pages). Template provided in Section II.H.
J. Attachment 10: Privacy Plan.
K. Attachment 11: ARO Forms.
Templates for the requirements below can be found at
https://www.arl.army.mil/resources/baa-forms/, or other websites.
The following forms shall be included in the submission:
• Publicly Releasable Project Abstract
37
Unless otherwise instructed in this BAA, the Project Abstract shall include a
concise statement of work and basic approaches to be used in the proposed effort.
The abstract should include a statement of scientific objectives, methods to be
employed, and the significance of the proposed effort to the advancement of
knowledge.
The abstract should be no longer than one (1) page (maximum 4,000 characters).
The project abstract shall be marked by the applicant as publicly releasable. By
submission of the project abstract, the applicant confirms that the abstract is
releasable to the public.
• ARO Proposal Cover Page (ARO Form 51)
• Protection of Proprietary Information During Evaluation and After Award (for
Industrial Contractors) (ARO Form 52), if applicable
• Protection of Proprietary Information During Evaluation and After Award (for
Educational Institutions / Non-Profit Organizations) (ARO Form 52a), if applicable
• Biographical Sketch
This Section shall contain the biographical sketches for senior and key personnel
only.
Primary Principal Investigator: The “Primary” PI provides a single or initial point
of communication between the sponsoring agency(s) and the awardee
organization(s) about scientific matters. If not otherwise designated, the first PI
listed will serve as the “Primary” PI. This individual can be changed with approval
of the agency. The sponsoring agency(s) does not infer any additional scientific
stature to this role among collaborating investigators.
Co-Principal Investigators: The individual(s) a research organization designates as
having an appropriate level of authority and responsibility for the proper conduct
of the research and submission of required reports to the agency. When an
organization designates more than one PI, it identifies them as individuals who
share the authority and responsibility for leading and directing the research,
intellectually and logistically. The sponsoring agency(s) does not infer any
distinction among multiple PIs.
Key personnel: The individual(s) a research organization designates as having a
high level of technical expertise in the topics proposed to be researched and who
will both play an active role in the research and supervise the work of more junior
personnel on a daily basis.
The following information is required:
Relevant experience and employment history including a description of any prior
Federal employment within one year preceding the date of proposal submission.
38
List of up to three (3) publications most closely related to the proposed project and
up to three (3) other significant publications, including those being printed. Patents,
copyrights, or software systems developed may be substituted for publications.
List of persons, other than those cited in the publications list, who have collaborated
on a project or a book, article, report or paper within the last four (4) years. Include
pending publications and submissions. Otherwise, state "None."
Names of each investigator's own graduate or post graduate advisors and advisees.
The information provided in "c" and "d" is used to help identify potential conflicts
or bias in the selection of reviewers.
The time commitment of each senior or key person to this project.
For the personnel categories of postdoctoral associates, other professionals, and
students (research assistants), the proposal may include information on exceptional
qualifications of these individuals that merit consideration in the evaluation of the
proposal.
The biographical sketches are limited to three (3) pages per investigator and other
individuals that merit consideration.
• Current and Pending Support
All project support from whatever source must be listed. The list must include all
projects requiring a portion of the principal investigator's and other senior
personnel's time, even if they receive no salary support from the project(s)
including Cooperative Research and Development Agreements (CRADAs) or other
technology transfer agreements with federal labs. Funding provided under any
award resulting from this BAA may only be used in support of the effort funded by
that award, and not for any other project or purpose.
The information should include, as a minimum:
o the project/proposal title and brief description,
o the name and location of the organization or agency presently funding the
work or requested to fund such work,
o the award amount or annual dollar volume of the effort,
o the period of performance, and
o a breakdown of the time required of the principal investigator and/or other
senior personnel.
• Facilities, Equipment, and Other Resources
The offeror should include in the proposal a listing of facilities, equipment, and
other resources already available to perform the research proposed.
• Research and Related Senior/Key Person Profile and Research and Related
Personal Data form
39
To evaluate compliance with Title IX of the Education Amendments of 1972 {20
U.S.C. A§ 1681 Et. Seq.), the Department of Defense is collecting certain
demographic and career information to be able to assess the success rates of women
who are proposed for key roles in applications in STEM disciplines. To enable this
assessment, each application must also include the following forms completed as
indicated:
Research and Related Senior/Key Person Profile: The Degree Type and Degree
Year fields on the Research and Related Senior/Key Person Profile {Expanded}
form will be used by DoD as the source for career information. In addition to the
required fields on the form, applicants must complete these two fields for all
individuals that are identified as having the project role of PD/Pl or Co-PD/Pl on
the form. Additional senior/key persons can be added by selecting the "Next
Person" button.
Related Personal Data: This form will be used by DoD as the source of
demographic information, such as gender, race, ethnicity, and disability
information for the Project Director/Principal Investigator and all other persons
identified as Co-Project Director{s)/Co-Principal Investigator(s). Each application
must include this form with the name fields of the Project Director/Principal
Investigator and any Co-Project Director(s)/Co-Principal Investigator(s)
completed; however, provision of the demographic information in the form is
voluntary. If completing the form for multiple individuals, each Co-Project
Director/Co-Principal Investigator can be added by selecting the "Next Person"
button. The demographic information, if provided, will be used for statistical
purposes only and will not be made available to merit reviewers. Applicants who
do not wish to provide some or all of the information should check or select the
"Do not wish to provide" option.
• Research and Related Other Project Information
This form shall be completed by all organizations (both primes and proposed
subcontractors).
• Representation Under DoD Assistance Agreements: Appropriations Provisions on
Tax Delinquency and Felony Convictions
Note: The Estimated Cost Breakdown Template in Section H.10 replaces the requirement
for the Summary Proposal Budget (ARO Form 99)
Volume 2 – Cost Proposal
Below are the outlines of the informational requirements for a cost proposal.
Cost Proposal – (No Page Limit). The cost proposal shall contain sufficient factual information to
establish the Offeror’s understanding of the project, the perception of project risks, the ability to
organize and perform the work, and to support the realism and reasonableness of the proposed 
40
work, to the extent appropriate. The Government recognizes that undue emphasis on cost may
motivate offerors to offer low-risk ideas with minimum uncertainty and to staff the effort with
junior personnel in order to be in a more competitive posture. The Government discourages such
cost strategies. Cost reduction approaches that shall be received favorably include innovative
management concepts that maximize direct funding for technology and limit diversion of funds
into overhead.
Reasoning for Submitting a Strong Cost Proposal
The ultimate responsibility of the Contracting Officer is to ensure that all prices offered in a
proposal are fair and reasonable before contract award [FAR 15.4]. To establish the
reasonableness of the offered prices, the Contracting Officer may ask the offeror to provide various
supporting documentation that assists in this determination. The offeror’s ability to be responsive
to the Contracting Officer’s requests can expedite contract award. As specified in Section 808 of
Public Law 105-261, an offeror who does not comply with a requirement to submit information
for a contract or subcontract in accordance with paragraph (a)(1) of FAR 15.403-3 may be
ineligible for award.
DCAA-Accepted Accounting System
Before a contract can be awarded, the Contracting Officer must confirm that the offeror has a
DCAA-accepted accounting system in place for accumulating and billing costs under Government
contracts [FAR 53.209-1(f)]. If the offeror has DCAA correspondence, which documents the
acceptance of their accounting system, this should be provided to the Contracting Officer (i.e.,
attached or referenced in the proposal). Otherwise, the Contracting Officer will submit an inquiry
directly to the appropriate DCAA office and request a review of the offeror’s accounting system.
If an offeror does not have a DCAA-accepted accounting system in place, the DCAA review
process can take several months depending upon the availability of the DCAA auditors and the
offeror’s internal processes. This will cause a delay in contract award.
For more information about cost proposals and accounting standards, view the link titled
“Information for Contractors” on their website at: https://www.dcaa.mil/Guidance/Audit-ProcessOverview/.
Field Pricing Assistance
During the pre-award cost audit process, the Contracting Officer will solicit support from DCAA
to determine commerciality and price reasonableness of the proposal [FAR 15.404-2]. Any
proprietary information or reports obtained from DCAA field audits will be appropriately
identified and protected within the Government.
Volume 2 – Cost Proposal
Section 1 - Cover Sheet - Technical (see Section II.H)
Section 2 – Estimated Cost Breakdown
Section 3 – Supporting Information 
41
A. Section 1: Cover Sheet – Cost Proposal
The cover sheet shall include (see Section II.H for an example):
1. BAA number;
2. Technical area;
3. Lead Organization submitting proposal;
4. Type of business, selected among the following categories: “LARGE BUSINESS”,
“SMALL DISADVANTAGED BUSINESS”, “OTHER SMALL BUSINESS”,
“HBCU”, “MI”, “OTHER EDUCATIONAL”, OR “OTHER NONPROFIT”;
5. Contractor’s reference number (if any);
6. Other team members (if applicable) and type of business for each;
7. Proposal title;
8. Technical point of contact to include: salutation, last name, first name, street
address, city, state, zip code, telephone, fax (if available), electronic mail (if
available);
9. Administrative point of contact to include: salutation, last name, first name, street
address, city, state, zip code, telephone, fax (if available), and electronic mail (if
available);
10. Award instrument requested: cost-plus-fixed-free (CPFF), cost-contract—no fee,
cost sharing contract – no fee, or other type of procurement contract (specify).
11. Place(s) and period(s) of performance;
12. Total proposed cost separated by basic award and option(s) (if any);
13. Name, address, and telephone number of the proposer’s cognizant Defense
Contract Management Agency (DCMA) administration office (if known);
14. Name, address, and telephone number of the proposer’s cognizant Defense
Contract Audit Agency (DCAA) audit office (if known);
15. Date proposal was prepared;
16. DUNS number;
17. TIN number; and
18. Cage Code;
19. Subcontractor Information; and
20. Proposal validity period
21. Any Forward Pricing Rate Agreement, other such approved rate information, or
such other documentation that may assist in expediting negotiations (if available).
B. Section 2: Estimated Cost Breakdown
Each proposal must contain a budget for each Program Phase of support requested and a
cumulative budget for the full term of requested support. Locally produced versions may
be used, but you may not make substitutions in prescribed budget categories or alter or
rearrange the cost categories as they appear on the form. The proposal may request funds
under any of the categories listed so long as the item is considered necessary to perform
the proposed work and is not precluded by applicable cost principles. Additionally, a
budget by major proposed research tasks and sub-task using the same budget categories
must be included. An example is provided in Section II.H.
42
All cost data must be current and complete. Costs proposed must conform
to the following principles and procedures:
Educational Institutions: 2 CFR Part 200 (formerly OMB Circular A-21)
Nonprofit Organizations: 2 CFR Part 200 (formerly OMB Circular A-122*); and
Commercial Organizations: FAR Part 31, DFARS Part 231, FAR Subsection
15.403-5, and DFARS Subsection 215.403-5.
*For those nonprofit organizations specifically exempt from the provisions of 2 CFR
Part 230, FAR Part 31 and DFARS Part 231 shall apply.
Offerors shall submit numerical cost and pricing data using Microsoft Excel. The Excel
document, in the format provided in Section II.H, shall include intact formulas and shall
not be hard numbered. The base and option period cost data should roll up into a total cost
summary. The Excel files may be write-protected but shall not be password protected. The
Cost/Price Volume shall include the following:
i. Completed Cost/Price Template - Offerors shall submit a cost element breakdown
for the base period, each option period and the total program summary in the format
provided in Section II.H.
ii. Total cost broken down by major task.
iii. Major program tasks by fiscal year.
iv. A summary of projected funding requirements by month.
v. A summary table listing all labor categories used in the proposal and their
associated direct labor rates, along with escalation factors used for each base year
and option year.
vi. A summary table listing all indirect rates used in the proposal for each base year
and option year
Additional details regarding the cost proposal, including samples tables, can be found
further in this section.
C. Section 3: Supporting Information
In addition to the above, supporting cost and pricing information shall be provided in
sufficient detail to substantiate the Offeror’s cost estimates. Include a description of the
basis of estimate (BOE) in a narrative for each cost element and provide supporting
documentation, as applicable.
A signed summary budget page must be included. The documentation pages should be
titled "Budget Explanation Page" and numbered chronologically starting with the
budget form. The need for each item should be explained clearly.
Sample Elements of a Cost Proposal
To help guide offerors through the pre-award cost audit process, a sample cost proposal is detailed
below. This sample also allows the offeror to see exactly what the Government is looking for;
therefore, all cost and pricing back-up data can be provided to the Government in the first cost 
43
proposal submission. Review each cost element within the proposal and take note of the types of
documentation that the Contracting Officer will require from the offeror.
A. Direct Labor
The first cost element included in the cost proposal is Direct Labor. The DoD requires each
proposed employee to be listed by name and labor category.
Table 5: Example of Direct Labor Table Proposed by Sample Offeror
DIRECT LABOR YEAR 1 YEAR 2
Employee
Name
Labor
Category
Direct
Hourly
Rate
Hours Total Direct
Labor
Direct
Hourly
Rate
Hours Total Direct
Labor
Andy Smith Program
Manager $55.00 720.00 $39,600.00 $56.65 720.00 $40,788.00
Bryan
Andrew
Senior
Engineer $40.00 672.00 $26,880.00 $41.20 672.00 $27,686.40
Cindy
Thomas
Principal
Engineer $50.00 512.00 $25,600.00 $51.50 512.00 $26,368.00
David
Porter
Entry
Level
Engineer
$10.00 400.00 $4,000.00 $10.30 400.00 $4,120.00
Edward
Bean
Project
Administra
tor
$25.00 48.00 $1,200.00 $25.75 48.00 $1,236.00
Subtotal Direct Labor (DL) $97,280.00 $100,198.40
For this cost element, the Contracting Officer requires the offeror to provide adequate
documentation in order to determine that each labor rate for each employee/labor category is
fair and reasonable. The documentation will need to explain how these labor rates were
derived. For example, if the rates are DCAA-approved labor rates, provide the Contracting
Officer with copies of the DCAA documents stating the approval. This is the most acceptable
means of documentation to determine the rates fair and reasonable. Other types of supporting
documentation may include General Service Administration (GSA) contract price lists, actual
payroll journals, or Salary.com research. If an employee listed in a cost proposal is not a current
employee (maybe a new employee, or one contingent upon the award of this contract), a copy
of the offer letter stating the hourly rate - signed and accepted by the employee - may be
provided as adequate documentation. Sometimes the hourly rates listed in a proposal are
derived through subjective processes, i.e., blending of multiple employees in one labor
category, or averaged over the course of the year to include scheduled payroll increases, etc.
These situations should be clearly documented for the Contracting Officer.
Another cost element in Direct Labor is labor escalation, or the increase in labor rates from
Year 1 to Year 2. In the example above, the proposed labor escalation is 3% (ex., Andy Smith
increased from $55.00/hr in Year 1, by 3% to $56.65/hr in Year 2). Often times, an offeror
may not propose escalation on labor rates during a 24-month period. Whatever the proposed
escalation rate is, please be prepared to explain why it is fair and reasonable [ex., a sufficient
explanation for our sample escalation rate would be the Government’s General Schedule 
44
Increase and Locality Pay for the same time period (name FY) in the same location (name
location) was published as 3.5%, therefore a 3% increase is fair and reasonable]
B. Other Direct Costs (ODCs)
This section of the cost proposal includes all other directly related costs required in support of
the effort, i.e., materials, subcontractors, consultants, travel, etc. Any cost element that includes
various items will need to be detailed in a cost breakdown to the Contracting Officer.
Direct Material Costs: This subsection of the cost proposal will include any special tooling,
test equipment, and material costs necessary to perform the project. Items included in this
section will be carefully reviewed relative to need and appropriateness for the work proposed,
and must, in the opinion of the Contracting Officer, be advantageous to the Government and
directly related to the specific topic.
The Contracting Officer will require adequate documentation from the offeror to determine the
cost reasonableness for each material cost proposed. The following methods are ways in
which the Contracting Officer can determine this [FAR 15.403-1].
• Adequate Price Competition. A price is based on adequate price competition when the
offeror solicits and receives quotes from two or more responsible vendors for the same
or similar items or services. Based on these quotes, the offeror selects the vendor who
represents the best value to the Government. The offeror will be required to provide
copies of all vendor quotes received to the Contracting Officer. Note: Price
competition is not required for items at or below the micropurchase threshold ($10,000)
[FAR 15.403-1]. If an item’s unit cost is less than or equal to $10,000, price
competition is not necessary. However, if an item’s total cost over the period of
performance (unit cost * quantity is higher than $10,000, two or more quotes must be
obtained by the offeror.
• Commercial Prices. Commercial prices are those published on current price lists,
catalogs, or market prices. This includes vendors who have prices published on a GSAschedule contract. The offeror will be required to provide copies of such price lists to
the Contracting Officer.
• Prices set by law or regulation. If a price is mandated by the Government (i.e.
pronouncements in the form of periodic rulings, reviews, or similar actions of a
governmental body, or embodied in the laws) that is sufficient to set a price.
Table 6: Example of Direct Material Costs as Proposed by Sample Offeror
DIRECT MATERIAL COSTS: YEAR 1 YEAR 2
Raw Materials $35,000.00 $12,000.00
Computer for experiments $4,215.00 $0.00
Cable (item #12-3657, 300 ft) $1,275.00 $0.00
45
DIRECT MATERIAL COSTS: YEAR 1 YEAR 2
Software $1,825.00 $1,825.00
Subtotal Direct Materials Costs (DM): $42,315.00 $13,825.00
Raw Materials: This is a generic label used to group many material items into one cost item
within the proposal. The Contracts Officer will require a detailed breakout of all the items that
make up this cost. For each separate item over $10,000 (total for Year 1 + Year 2), the offeror
must be able to provide either competitive quotes received, or show that published pricing was
used.
Computer for experiments: Again, this item is most likely a grouping of several components
that make up one system. The Contracts Officer will require a detailed breakout of all the
items that make up this cost. For each separate item over $10,000 (total for Year 1 + Year 2),
the offeror must be able to provide either competitive quotes received, or show that published
pricing was used.
Cable: Since this item is under the simplified acquisition threshold of $10,000, competitive
quotes or published pricing are not required. Simply provide documentation to show the
Contracting Officer where this price came from.
Software: This cost item could include either one software product, or multiple products. If
this includes a price for multiple items, please provide the detailed cost breakdown. Note: The
price for Year 1 ($1,825) is below the simplified acquisition threshold; however, in total (Year
1 + Year 2) the price is over $10,000, so competitive quotes or published pricing
documentation must be provided.
Due to the specialized types of products and services necessary to perform these projects, it
may not always be possible to obtain competitive quotes from more than one reliable source.
Each cost element over the simplified acquisition threshold ($10,000) must be substantiated.
There is always an explanation for HOW the cost of an item was derived; show us how you
came up with that price!
When it is not possible for an offeror to obtain a vendor price through competitive quotes or
published price lists, a Contracting Officer may accept other methods to determine cost
reasonableness. Below are some examples of other documentation, which the Contracting
Officer may accept to substantiate costs:
a. Evidence that a vendor/supplier charged another offeror a similar price for similar
services. Has the vendor charged someone else for the same product? (Two (2) to three
(3) invoices from that vendor to different customers may be used as evidence.)
b. Previous contract prices. Has the offeror charged the Government a similar price under
another Government contract for similar services? If the Government has already paid
a certain price for services, then that price may already be considered fair and
reasonable. (Provide the contract number, and billing rates for reference.) 
46
c. DCAA approved. Has DCAA already accepted or verified specific cost items included
in your proposal? (Provide a copy of DCAA correspondence that addressed these
costs.)
Table 7: Example of ODCs, Including Equipment, as Proposed by Example Offeror
OTHER DIRECT COSTS: YEAR 1 YEAR 2
Equipment Rental for Analysis $5,500.00 $5,600.00
Subcontractor – Widget, Inc. $25,000.00 $0.00
Consultant: John Bowers $0.00 $12,000.00
Travel $1,250.00 $1,250.00
Subtotal ODCs: $31,750.00 $18,850.00
Equipment Rental for Analysis: The offeror explains that the Year 1 cost of $5,500 is based
upon 250 hours of equipment rental at an hourly rate of $22.00/hr. One (1) invoice from the
vendor charging another vendor the same price for the same service is provided to the
Contracting Officer as evidence.
Subcontractor – Widget, Inc.: The offeror provides a copy of the subcontractor quote to the
Contracting Officer in support of the $25,000 cost. This subcontractor quote must include
sufficient detailed information (equivalent to the data included in the prime’s proposal to the
Government), so that the Contracting Officer can make a determination of cost reasonableness.
a. As stated in Section 3.5(c)(6) of the DoD Cost Proposal guidance, “All subcontractor
costs and consultant costs must be detailed at the same level as prime contractor costs
in regards to labor, travel, equipment, etc. Provide detailed substantiation of
subcontractor costs in your cost proposal.”
b. In accordance with FAR 15.404-3, “the Contracting Officer is responsible for the
determination of price reasonableness for the prime contract, including subcontracting
costs”. This means that the subcontractor’s quote/proposal may be subject to the same
scrutiny by the Contracting Officer as the cost proposal submitted by the prime. The
Contracting Officer will need to determine whether the subcontractor has an accepted
purchasing system in place and/or conduct appropriate cost or price analyses to
establish the reasonableness of proposed subcontract prices. Due to the proprietary
nature of cost data, the Subcontractor may choose to submit their pricing information
directly to the Contracting Officer and not through the prime. This is understood and
encouraged.
c. When a subcontractor is selected to provide support under the prime contract due to
their specialized experience, the Contracting Officer may request sole source
justification from the offeror.
Consultant – John Bowers: Again, the offeror shall provide a copy of the consultant’s quote
to the Contracting Officer as evidence. In this example, the consultant will be charging an
hourly rate of $125 an hour for 96 hours of support. The offeror indicates to the Contracting
Officer that this particular consultant was used on a previous contract with the Government
(provide contract number), and will be charging the same rate. A copy of the consultant’s 
47
invoice to the offeror under the prior contract is available as supporting evidence. Since the
Government has paid this price for the same services in the past, determination has already
been made that the price is fair.
Travel: The Contracting Officer will require a detailed cost breakdown for travel expenses to
determine whether the total cost is reasonable based on Government per diem and mileage
rates. This breakdown shall include the number of trips, the destinations, and the number of
travelers. It will also need to include the estimated airfare per round trip, estimated car rental,
lodging rate per trip, tax on lodging, and per diem rate per trip. The lodging and per diem rates
must coincide with the Joint Travel Regulations. Please see the following website to determine
the appropriate lodging and per diem rates: https://www.travel.dod.mil/. Additionally, the
offeror must provide why the airfare is fair and reasonable as well. Sufficient back up for both
airfare and car rental would include print outs of online research at the various travel search
engines (Expedia, Travelocity, etc.) documenting the prices for airfare and car rentals thus
proving why your chosen rate is fair and reasonable.
Table 8: Example of Travel Cost Breakout from ODCs by Example Offeror
TRAVEL Trips Travelers Nights Days Unit Cost Total
Travel
Airfare per
roundtrip 1 1 $996.00 $996.00
Lodging per day 1 1 1 $75.00 $75.00
Tax on
Lodging
(12%)
per day 1 1 1 $9.00 $9.00
Per Diem per day 1 1 2 $44.00 $88.00
Automobile
Rental per day 1 1 2 $41.00 $82.00
Subtotal
Travel $1,250.00
C. Indirect Rates
Indirect rates include elements such as Fringe Benefits, General & Administrative (G&A), Overhead,
and Material Handling costs. The offeror shall indicate in the cost proposal both the indirect rates (as
a percentage) as well as how those rates are allocated to the costs in the proposal.
Table 9: Example of Indirect Rates by Example Offeror
INDIRECTS YEAR 1 YEAR 2
Subtotal Direct Labor (DL): $97,280.00 $100,198.40
Fringe Benefits, if not included in Overhead, rate
(15.0000 %) X DL =
$14,592.00 $15,029.76
Labor Overhead (rate 45.0000 %) X (DL + Fringe) = $50,342.40 $51,852.67
Total Direct Labor (TDL): $162,214.40 $167,080.83
48
In this example, the offeror includes a Fringe Benefit rate of 15.00% that it allocated to the
Direct Labor costs. They also propose a Labor Overhead rate of 45.00% that is allocated to the
Direct Labor costs plus the Fringe Benefits.
All indirect rates and the allocation methods of those rates must be verified by the Contracting
Officer. In most cases, DCAA documentation supporting the indirect rates and allocation
methods can be obtained through a DCAA field audit or proposal review. Many offerors have
already completed such reviews and have this documentation readily available. If an offeror is
unable to participate in a DCAA review to substantiate indirect rates, the Contracting Officer
may request other accounting data from the offeror to make a determination.
D. Cost of Money (COM)
If Cost of Money (an imputed cost that is not a form of interest on borrowings (see FAR
31.205-20); an “incurred cost” for cost-reimbursement purposes under applicable costreimbursement contracts and for progress payment purposes under fixed-price contracts; and
refers to: (1) Facilities capital cost of money (48 CFR 9904.414); and (2) Cost of money as an
element of the cost of capital assets under construction (48 CFR 9904.417)) is proposed in
accordance with FAR 31.205-10, a DD Form 1861 is required to be completed and submitted
with the contractor’s proposal.
E. Fee/Profit
The proposed fee percentage will be analyzed in accordance with DFARS 215.404, the
Weighted Guidelines Method.
3. Submission of Complete Research Proposals
Proposals must be submitted through the offeror’s organizational office having responsibility
for Government business relations. All signatures must be that of an official authorized to
commit the organization in business and financial affairs. Proposals must be submitted
electronically using the following format:
Proposals shall be submitted electronically through the IARPA Distribution and Evaluation
System (IDEAS). Offerors interested in providing a submission in response to this BAA shall
first register by electronic means in accordance with the instructions provided on the
following web site: https://iarpa-ideas.gov. Offerors who plan to submit proposals for
evaluation are strongly encouraged to register at least one week prior to the due date for the
first round of proposals. Offerors who do not register in advance do so at their own risk, and
the Government shall not extend the due date to accommodate such Offerors. Failure to
register as stated shall prevent the Proposer’s submittal of documents.
After registration has been approved, Offeror’s should upload a proposal, scanned
certifications and permitted additional information in ‘pdf’ format, or as otherwise directed
(Excel, PowerPoint, etc.). Offerors are responsible for ensuring a compliant and timely
submission of their proposals to meet the BAA submittal deadlines. Time management to 
49
upload and submit is wholly the responsibility of the Offeror. Note: IDEAS will require
Offerors to complete a proposal cover sheet within IDEAS at the time that the Volume 1
– Technical and Management Proposal is submitted. This is separate and distinct from
the Technical and Cost Volume cover sheets referenced in II.D.2 (also provided in Section
H). Information requested within IDEAS will include basic cost information (Total funds
requested from IARPA, proposed costs by option period and validity period).
Upon completing the proposal submission, the Offeror shall receive an automated
confirmation email from IDEAS. Please forward that automated message to dni-iarpa-baaw911nf-23-s-0007@iarpa.gov. The Government strongly suggests that the Offeror document
the submission of their proposal package by printing the electronic receipt (time and date
stamped) that appears on the final screen following compliant submission of a proposal to the
IDEAS website.
Proposals submitted by any means other than IDEAS (e.g., hand-carried, postal service,
commercial carrier and email) shall not be considered unless the Offeror attempted electronic
submittal but was unsuccessful and notified the Government using the following procedure.
The Offeror shall send an e-mail to dni-iarpa-baa-w911nf-23-s-0007@iarpa.gov prior to the
proposal due date and time specified in the BAA and indicate that an attempt was made to
submit electronically, and that the submittal was unsuccessful. This e-mail shall include
contact information for the Offeror. Upon receipt of such notification, the Government will
provide additional guidance regarding submission.
The full proposal submission shall be submitted by the date and time specified in the BAA,
Application and Submission Information section, II.D.4 Submission Dates and Times in
order to be considered. Proposals received after this date are deemed to be late and will not
be reviewed. Failure to comply with the submission procedures may result in the submittal
not being evaluated.
All information uploaded into IDEAS shall be unclassified. Classified information is not
permitted.
4. Unique Entity Identifier and System for Award Management (SAM)
Each applicant (unless the applicant is an individual or Federal awarding agency that is exempt
from those requirements under 2 CFR §25.110(b) or (c), or has an exception approved by the
Federal awarding agency under 2 CFR §25.110(d)) is required to:
(i) Be registered in SAM before submitting its application;
(ii) Provide a valid unique entity identifier in its application; and
(iii) Continue to maintain an active SAM registration with current information at all times
during which it has an active Federal award or an application or plan under consideration
by a Federal awarding agency.
The Federal awarding agency may not make a Federal award to an applicant until the applicant
has complied with all applicable unique entity identifier and SAM requirements. If an applicant
has not fully complied with the requirements by the time the Federal awarding agency is ready 
50
to make a Federal award, the Federal awarding agency may determine that the applicant is not
qualified to receive a Federal award and use that determination as a basis for making a Federal
award to another applicant.
4. Submission Dates and Times:
Proposals:
Proposals transmitted to be considered for award must be submitted in IDEAS no later than
5:00 PM EDT on 8 MAY 2023.
Applicants are responsible for submitting electronic proposals in sufficient time to insure
IARPA IDEAS receives it by the time specified in this BAA. If the electronic proposal is
received by IARPA IDEAS after the exact time and date specified for receipt of offers, it will
be considered “late” and may not be considered for award. Acceptable evidence to establish
the time of receipt by IARPA IDEAS includes documentary evidence of receipt maintained by
IARPA IDEAS.
Because of potential problems involving the applicants’ own equipment, to avoid the
possibility of late receipt and resulting in ineligibility for award consideration, it is
strongly recommended that proposals be uploaded at least two business days before the
deadline established in the BAA.
If an emergency or unanticipated event interrupts normal Government processes so that
proposals cannot be received at IARPA IDEAS by the exact time specified in the solicitation,
and urgent Government requirements preclude amendment of the solicitation closing date, the
time specified for receipt of proposals will be deemed to be extended to the same time of day
specified in the solicitation on the first work day on which normal Government processes
resume.
Proposal Receipt Notices – The Government will receive an email confirming the successful
submission of a proposal to IARPA IDEAS within one (1) hour after submission, as long as
the proposal is submitted no later than 5 PM EDT on the due date.
5. Intergovernmental Review:
Other Government Agencies will be involved in the review process.
6. Funding Restrictions:
Multiple 42-month awards are anticipated. The actual amount of each award will be contingent
on availability of funds and the scope of the proposed work. Depending on the results of the
proposal evaluation, there is no guarantee that any of the proposals submitted in response to a
particular program goal will be recommended for funding. Proposals may be funded in part.
51
7. Other Submission Requirements:
Information to Be Requested from Successful Offerors - Offerors whose proposals are accepted
for funding will be contacted before award to provide additional information required for award.
The required information is normally limited to clarifying budget explanations, representations,
certifications, and some technical aspects.
Statement of Work (SOW) - prior to award the Contracting Officer may request that the contractor
submit an SOW for the effort to be performed, which will be incorporated into the contract at the
time of award.
An applicant may withdraw a proposal at any time before award by written notice or by email.
Notice of withdrawal shall be sent to the Contracting identified in Section II.G of this BAA.
Withdrawals are effective upon receipt of notice by the Contracting/Grants Officer.
E. Proposal Review Information:
1. Criteria:
The Government shall only review proposals against the evaluation criteria, and then against
program balance, and availability of funds, and shall not evaluate them against other proposals,
since they are not submitted in accordance with a common work statement. For evaluation
purposes, a proposal is the document described in Section II.D.2.b of the BAA. Other supporting
or background materials submitted with the proposal shall not be considered. Only Government
personnel shall make evaluation and award determinations under this BAA
The factors used to evaluate and select proposals for negotiation for this Program BAA are
described in the following paragraphs. Each proposal shall be evaluated on its own merits and its
relevance to the Program goals rather than against other proposals submitted in response to this
BAA. The proposals shall be evaluated based on technical, program, and funding availability
factors. These are of equal importance. Within the technical evaluation factor, the specific
technical criteria are in descending order of importance, as follows: Overall Scientific and
Technical Merit, Effectiveness of Proposed Work Plan, Contribution and Relevance to the
IARPA Mission and Program Goal, Relevant Experience and Expertise, and Resource Realism.
Specifics about the evaluation criteria are provided below.
Award(s) shall be made to an offeror on the basis of the technical, program, and funding
availability factors listed below, and subject to successful negotiations with the Government.
Offerors are cautioned that failure to follow submittal instructions may negatively impact their
proposal evaluation or may result in rejection of the proposal for non-compliance.
Overall Scientific and Technical Merit
Overall scientific and technical merit of the proposal is substantiated, including unique and
innovative methods, approaches, and/or concepts. The offeror clearly articulates an understanding
of the problem to be solved. The technical approach is credible and includes a clear assessment of
primary risks and a means to address them. The proposed research advances the state-of-the-art.
52
Effectiveness of Proposed Work Plan
The feasibility and likelihood that the proposed approach shall satisfy the Program’s milestones
and metrics are explicitly described and clearly substantiated along with risk mitigation strategies
for achieving stated milestones and metrics. The proposal reflects a mature and quantitative
understanding of the Program milestones and metrics, and the statistical confidence with which
they may be measured. Any offeror-proposed milestones and metrics are clear and well-defined,
with a logical connection to enabling offeror decisions and/or Government decisions. The schedule
to achieve the milestones is realistic and reasonable.
The roles and relationships of prime and sub-contractors is clearly delineated with all participants
fully documented. Work plans shall demonstrate the ability to provide full Government visibility
into and interaction with key technical activities and personnel, and a single point of responsibility
for contract performance. Work plans shall also demonstrate that key personnel have sufficient
time committed to the Program to accomplish their described Program roles.
The requirement and rationale for and the anticipated use or integration of Government resources,
including, but not limited to, all equipment, facilities, information, etc., is fully described including
dates when such Government Furnished Property (GFP), Government Furnished Equipment
(GFE), Government Furnished Information (GFI) or other similar Government-provided resources
shall be required.
The offeror’s RDMP is complete, addressing the types of data to be collected or produced,
describing how each type of data will be preserved and shared, including plans to provide public
access to peer reviewed publications and the underlying research data, or provides justifiable
rationale for not making this data available.
Contribution and Relevance to the IARPA and ARO Mission and Program Goals
The proposed solution meets the letter and intent of the stated program goals and all elements
within the proposal exhibit a comprehensive understanding of the problem. The offeror clearly
addresses how the proposed effort shall meet and progressively demonstrate the Program goals.
The offeror describes how the proposed solution contributes to IARPA’s mission to invest in highrisk/high-payoff research that can provide the U.S. with an overwhelming intelligence advantage.
The offeror’s proposed intellectual property and data rights are consistent with the Government’s
need to be able to effectively manage the program and evaluate the technical output and
deliverables, communicate program information across Government organizations and support
transition and further use and development of the program results to Intelligence Community users
at an acceptable cost. The proposed approach to intellectual property rights is in the Government’s
best interest.
The offeror’s proposed intellectual property and data rights are consistent with the Government’s
need to be able to effectively manage the program and evaluate the technical output and
deliverables, communicate program information across Government organizations and support
transition and further use and development of the program results to Intelligence Community users
at an acceptable cost. The proposed approach to intellectual property rights is in the Government’s
best interest. 
53
Relevant Experience and Expertise
The offeror’s capabilities, related experience, facilities, techniques, or unique combination of
these, which are integral factors for achieving the proposal's objectives as well as qualifications,
capabilities, and experience of the proposed principal investigator, team leader, and key personnel
critical in achieving the proposal objectives. Time commitments of key personnel must be
sufficient for their proposed responsibilities in the effort.
Resource Realism
The proposed resources demonstrate a clear understanding of the program, a perception of the risks
and the ability to organize and perform the work. The labor hours and mix are consistent with the
technical and management proposal and are realistic for the work proposed. Material, equipment,
software, data collection and management, and travel, especially foreign travel, are well justified,
reasonable, and required for successful execution of the proposed work.
Program Balance
The Government will consider IARPA’s overall mission and program objectives, which may
include but are not limited to the following: broadening the variety of technical approaches to
enhance program outcomes, transitioning the technology to Government partners, developing
capabilities aligned with the priorities of the IC and national security.
Funding Availability Factor
Budget Constraints: The Government will seek to maximize the likelihood of meeting program
objectives within program budget constraints. This may involve awarding one or more contracts.
Note: If the Offeror has submitted the proposal to other federal, state or local agencies or other
parties that may fund the proposed effort, it may impact the Government’s decision to fund the
effort.
2. Review and Selection Process:
The Government conducts impartial, equitable, comprehensive proposal reviews to select the
source (or sources) whose offer meets the Government's technical, policy and programmatic
goals. For evaluation purposes, a proposal is the document described in Section D of the BAA.
Other supporting or background materials submitted with the proposal shall not be considered.
The contract award process for this BAA has two steps. The first step is selection for
negotiations and is made based on an integrated assessment of the evaluation factors (see BAA
Section II.E.1). The second step is negotiation and contract award. The Government’s decision to
negotiate with any one offeror is solely at the Government’s discretion. That negotiation may
not be offered to other offerors. Contract award is contingent on Contracting Officer’s
determination of a fair and reasonable cost/price and agreement on terms and conditions.
Selection for negotiation will be conducted through a peer or scientific review process led by the
REASON IARPA Program Manager (PM). This process entails establishing a Scientific Review
Panel (SRP) made up of qualified Government personnel who will review and assess each
proposal’s strengths, weaknesses and risks against the technical evaluation criteria. If necessary, 
54
non-Government technical experts with specialized expertise may advise Government panel
members and the PM. However, only Government personnel will make selection
recommendations and decisions under this BAA.
Proposals will be reviewed individually and will not be compared against each other as they are
not submitted in accordance with a common SOW. When SRP reviews are complete, the IARPA
PM will prepare a recommendation to the IARPA Scientific Review Official (SRO) identifying
proposals as recommended, recommended with modifications, or not recommended for
negotiation based on consideration of all stated factors in Section II.E.1 (technical, program
balance, and funding availability factors). The SRO will make the final decision as to selection
for negotiations. At this point, Offerors will be notified in writing by the Contracting Officer as
to whether or not they have been selected for negotiation.
NOTE: A proposal may be handled for administrative purposes by support contractors. These
support contractors are prohibited from competing on BAA proposals and are bound by
appropriate non-disclosure requirements.
The Government may use Non-Government contractors who are employees of Booz Allen
Hamilton, Whitney, Bradley & Brown, Inc. (WBB), Serco, Inc., Airlin Technologies, Bluemont
Technology and Research, Navstar, Crimson Phoenix, Northwood Global Solutions, Onts &
Quants, Inc., or Tarragon Solutions to provide expert advice regarding portions of the proposals
submitted to the Government and to provide logistical support in carrying out the evaluation
process. In addition to supporting evaluations, the following entities: Johns Hopkins Applied
Physics Laboratory and MITRE Corporation will be supporting T&E activities for contracts
awarded under this program and should be considered as part of an Offeror’s OCI disclosure.
These personnel shall have signed and are subject to the terms and conditions of non-disclosure
agreements. By submission of its proposal, an offeror agrees that its proposal information may be
disclosed to employees of these organizations for the limited purpose stated above. Offerors who
object to this arrangement shall provide clear notice of their objection as part of their transmittal
letter. If offerors do not send notice of objection to this arrangement in their transmittal letter, the
Government shall assume consent to the use of contractor support personnel in assisting the review
of submittal(s) under this BAA.
Only Government personnel shall make evaluation and award determinations under this BAA.
3. Recipient Qualification
a. For CONTRACT Proposals:
(i) Contracts shall be awarded to responsible prospective contractors only. See FAR
9.104-1 for a listing of the general standards against which an applicant will be assessed
to determine responsibility.
(ii) Applicants are requested to provide information with proposal submission to assist
the Contracting Officer’s evaluation of responsibility.
(iii) The Federal Awardee Performance and Integrity Information System (FAPIIS) will 
55
be checked prior to making an award. The web address is: https://cpars.gov. The
applicant representing the entity may comment in this system on any information about
the entity that the federal government official entered. The information in FAPIIS will
be used in making a judgement about the entity’s integrity, business ethics, and record of
performance under Federal awards that may affect the official’s determination that the
applicant is qualified to receive an award.
________________________________________________________________________
FAR 52.209-11: Representation by Corporations Regarding Delinquent Tax Liability or a
Felony Conviction under any Federal Law (Feb 2016)
(a) As required by sections 744 and 745 of Division E of the Consolidated and Further
Continuing Appropriations Act, 2015 (Pub. L 113-235), and similar provisions, if
contained in subsequent appropriations acts, the Government will not enter into a contract
with any corporation that--
(1) Has any unpaid Federal tax liability that has been assessed, for which all judicial and
administrative remedies have been exhausted or have lapsed, and that is not being paid in
a timely manner pursuant to an agreement with the authority responsible for collecting the
tax liability, where the awarding agency is aware of the unpaid tax liability, unless an
agency has considered suspension or debarment of the corporation and made a
determination that suspension or debarment is not necessary to protect the interests of the
Government; or
(2) Was convicted of a felony criminal violation under any Federal law within the
preceding 24 months, where the awarding agency is aware of the conviction, unless an
agency has considered suspension or debarment of the corporation and made a
determination that this action is not necessary to protect the interests of the Government.
(b) The Offeror represents that—
(1) It is [ ] is not [ ] a corporation that has any unpaid Federal tax liability that has been
assessed, for which all judicial and administrative remedies have been exhausted or have
lapsed, and that is not being paid in a timely manner pursuant to an agreement with the
authority responsible for collecting the tax liability; and
(2) It is [ ] is not [ ] a corporation that was convicted of a felony criminal violation under a
Federal law within the preceding 24 months.
F. Award Administration Information:
1. Award Notices:
Initial notification of selection of proposals for funding will be e-mailed by ARO to
successful offerors. Unsuccessful offerors will be notified shortly thereafter by ARO. 
56
The notification e-mail of selection for funding must not be regarded as an authorization
to commit or expend funds. The Government is not obligated to provide any funding until
a Government Contracting Officer signs the contract award document.
Applicants whose proposals are recommended for negotiation of award will be contacted
by a Contract Specialist to discuss additional information required for award. This may
include representations and certifications, revised budgets or budget explanations,
certificate of current cost or pricing data, subcontracting plan for small businesses, and
other information as applicable to the proposed award.
2. Administrative and National Policy Requirements:
a. Required Certifications
(i) Certifications Required for Contract Awards. Certifications and representations shall
be completed by successful offerors prior to award. Federal Acquisition Regulation
(FAR) Online Representations and Certifications are to be completed through SAM at
website https://www.SAM.gov. Defense FAR Supplement and contract specific
certification packages will be provided to the contractor for completion prior to award.
FAR 52.203-18, PROHIBITION ON CONTRACTING WITH ENTITIES THAT
REQUIRE CERTAIN CONFIDENTIALITY AGREEMENTS OR STATEMENTS—
REPRESENTATION (JAN 2017)
FAR 52.204-26, COVERED TELECOMMUNICATIONS EQUIPMENT OR
SERVICES – REPRESENTATION (OCT 2020)
b. Policy Requirements
(i) MILITARY RECRUITING: This is to notify potential offerors that each contract
awarded under this announcement to an institution of higher education shall include the
following clause: Federal Acquisition Regulation (FAR) clause 52.209-1,Reserve
Officer Training Corps and Military Recruiting on Campus.
(ii) SUBCONTRACTING: This section is applicable to contracts where the dollar
threshold is expected to exceed to $750,000.00. Pursuant to Section 8(d) of the Small
Business Act [15 U.S.C. 637(d)], it is the policy of the Government to enable small
business concerns to be considered fairly as subcontractors under all research
agreements awarded to prime contractors. The required elements of the Subcontracting
Plan are set forth by FAR 52.219-9 (DEVIATION 2013-O0014) and DFARS 252.219-
7003.
Subcontracting Plan Goals. Small business subcontracting goals are established on an
individual contract basis. The applicant is requested to consider, when appropriate, the
Governments’ subcontracting goals. When applied to R&D the small businesssubcontractor plan should result in the best mix of cost schedule and performance. 
57
(iii) EXPORT CONTROL LAWS: Applicants should be aware of and are responsible
for complying with all applicable export control laws , including all International
Traffic in Arms (ITAR) (22 CFR 120 et. Seq.) requirements. In some cases,
developmental items funded by the Department of Defense are now included on the
United States Munition List (USML) and are therefore subject to ITAR jurisdiction.
Applicants should address in their proposals whether ITAR restrictions apply or do not
apply, such as in the case when research products would have both civil and military
application, to the work they are proposing to perform for the Department of Defense.
The USML is available online at https://www.ecfr.gov/cgi-bin/textidx?node=pt22.1.121. Additional information regarding the President's Export Control
Reform Initiative can be found at http://export.gov/ecr/index.asp .

(iv) DRUG-FREE WORKPLACE: The appropriate clause(s) shall be added to the
award.

(v) DEBARMENT AND SUSPENSION: The appropriate clause(s) shall be added to
the award.
(vi) REPORTING SUBAWARDS AND EXECUTIVE COMPENSATION: The
appropriate clause(s) shall be added to the award.
3. Reporting:
Reports including number and types will be specified in the award document, but will include as
a minimum monthly technical and financial status reports. The reports shall be prepared and
submitted in accordance with the procedures contained in the award document and mutually agreed
upon before award. Reports and briefing material will also be required as appropriate to document
progress in accomplishing program metrics.
Service Contract Reporting (SCR): See FAR 52.204-14, SAM Users Guide and DoD Guidebook
for Service Contract Reporting in the System for Award Management at
https://dodprocurementtoolbox.com/cms/sites/default/files/resources/2020-
10/SCR%20Guidebook%2021%20October%202020.pdf.
G. Agency Contacts:
Questions of a technical nature or a programmatic nature shall be directed as specified below:
Technical Program Point of Contact:
IARPA Program Manager:
Dr. Steven Rieber
REASON Program Manager
IARPA/Analysis Office
Steven.Rieber@iarpa.gov
301-243-2087 
58
Questions of a business nature shall be directed to the contact info, as specified below:
Mr. Schon Zwakman
Army Contracting Command- Aberdeen Proving Ground- Research Triangle Park
Division (ACC-APG-RTP)
Schon.zwakman.civ@army.mil
Comments or questions submitted should be concise and to the point, eliminating any unnecessary
verbiage. In addition, the relevant part and paragraph of the Broad Agency Announcement (BAA)
should be referenced.
H. Other Information:
1. Example of Technical Cover Sheet
(1) BAA Number W911NF-22-S-0007
(2) Technical Area(s) – (TA)(s), if applicable
(3) Lead Organization Submitting Proposal
(4) Type of Business, Selected Among the Following Categories: “Large
Business”, “Small Disadvantaged Business”, “Other Small Business”,
“HBCU”, “MI”, “Other Educational”, or “Other Nonprofit”
(5) Contractor’s Reference Number (if any)
(6) Other Team Members (if applicable) and Type of Business for Each
(7) Proposal Title
(8) Technical Point of Contact to Include: Title, First Name, Last Name,
Street Address, City, State, Zip Code, Telephone, Fax (if available),
Electronic Mail (if available)
(9) Administrative Point of Contact to Include: Title, First Name, Last
Name, Street Address, City, State, Zip Code, Telephone, Fax (if available),
Electronic Mail (if available)
(10) Volume 1 no more than the specified page limit Yes/No
(11) Restrictions on Intellectual property rights details provided in
Appendix A format?
Yes/No
(12) Research Data Management Plan included? Yes/No
(13) OCI Waiver Determination, Notification or Certification [see Section 3
of the BAA] Included?
Yes/No
(13a) If No, is written certification included (Appendix A)? Yes/No
59
(14) Are one or more U.S. Academic Institutions part of your team? Yes/No
(14a) If Yes, are you including an Academic Institution Acknowledgment
Statement with your proposal for each U.S. Academic Institution that is part
of your team (Appendix A)?
Yes/No
(15) Total Funds Requested from IARPA and the Amount of Cost Share (if
any)
$
(16) Date of Proposal Submission
60
2. Example of Academic Institution Acknowledgement Letter
-- Please Place on Official Letterhead --
<Insert date>
To: Contracting Officer, ODNI/IARPA
Office of the Director of National Intelligence
Washington, D.C. 20511
Subject: Academic Institution Acknowledgment Letter Reference: Executive Order 12333, As
Amended, Para 2.7
This letter is to acknowledge that the undersigned is the responsible official of <insert name of
the academic institution>, authorized to approve the contractual relationship in support of the
Office of the Director of National Intelligence’s Intelligence Advanced Research Projects
Activity and this academic institution.
The undersigned further acknowledges that he/she is aware of the Intelligence Advanced
Research Projects Activity’s proposed contractual relationship with <insert name of institution>
through BAA# W911NF-23-S-0007 and is hereby approved by the undersigned official, serving
as the president, vice-president, chancellor, vice-chancellor, or provost of the institution.
61
3. Example of Technical SOW
I. Task 1
a. Sub Task 1.a
b. Sub Task 1.b
c. Waypoints/Milestones & Associated Metrics
d. Deliverables
II. Task 2
a. Sub Task 2.a
b. Sub Task 2.b
c. Waypoints/Milestones & Associated Metrics
d. Deliverables
III. Task 3
a. Sub Task 3.a
b. Sub Task 3.b
c. Waypoints/Milestones & Associated Metrics
d. Deliverables
IV. Travel Requirements
V. Period of Performance
VI. Place of Performance
VII. Research and Compliance Requirements
62
4. Example of Team Organization Table
Participants Org Role Unique, Relevant
Capabilities Role: Tasks Clearance
Level * Time
Jane Wake LMN
Univ.
PI/Key
Personnel
Electrical
Engineering
Program Mgr &
Electronics: 10 100%
John Weck, Jr. OPQ
Univ.
Key
Personnel
Mathematical
Physics Programming: 1-5 50%
Dan Wind RST
Univ.
Key
Personnel Physics Design, Fab, and
Integration: 6-8 90%
Katie Wool UVW
Univ. Contributor Quantum Physics Enhancement
witness design: 4 25%
Rachel Wade XYZ
Corp.
Co-PI/Key
Personnel Graph theory Architecture design:
6 55%
Chris West XYZ
Corp.
Significant
Contributor
EE & Signal
Processing
Implementation &
Testing: 8-9 60%
Julie Will JW
Cons.
Consultant
(Individual) Computer science Interface design: 10 200 hours
David Word A Corp. Consultant
(A. Corp.)
Operations
Research
Applications
Programming: 2-3 200 hours
*if applicable
63
5. Example of Intellectual Rights Sheet
[Please provide here your good faith representation of ownership or possession of appropriate
licensing rights to all IP that shall be utilized under the Program.]
Patents
PATENTS
Patent number
(or application
number)
Patent name Inventor name(s) Patent owner(s)
or assignee
Incorporation into
deliverable
(LIST) (LIST) (LIST) (LIST) (Yes/No; applicable
deliverable)
1) Intended use of the patented invention(s) listed above in the conduct of the proposed
research;
2) Description of license rights to make, use, offer to sell, or sell, if applicable, that are
being offered to the Government in patented inventions listed above;
3) How the offered rights will permit the Government to reach its program goals (including
transition) with the rights offered;
4) Cost to the Government to acquire additional or alternative rights, if applicable;
5) Alternatives, if any, that would permit IARPA to achieve program goals.
Data (including Technical Data and Computer Software)
1) Intended use of the data, including technical data and computer software, listed above in
the conduct of the proposed research;
2) Description of Asserted Rights Categories, specifying restrictions on Government’s
ability to use, modify, reproduce, release, perform, display, or disclose technical data,
computer software, and deliverables incorporating technical data and computer software
listed above;
3) How the offered rights will permit the Government to reach its program goals (including
transition) with the rights offered;
4) Cost to the Government to acquire additional or alternative rights; if applicable;
5) Alternatives, if any, that would permit IARPA to achieve program goals.
NONCOMMERCIAL or COMMERCIAL ITEMS
Technical Data,
Computer Software To
be Furnished With
Restrictions
Basis for Assertion Asserted Rights
Category
Name of Person Asserting
Restrictions
(LIST) (LIST) (LIST) (LIST)
64
6. Example of Contract Deliverables Table
Contract
Deliverables
SOW
TASK#
Deliverable Title Format Due Date Distribution/Copies
Continual
Monthly
Contract Status
Report Gov't Format
10th of each
month
Copy to PM, CO and
COTR
Continual
Monthly
Technical Status
Reports Gov't Format
10th of each
month Standard Distribution**
** Standard Distribution: 1 copy of the transmittal letter without the deliverable to the
Contracting Officer. 1 copy of the transmittal letter with the deliverable to the Primary PM and
COTR.
65
7. Example of Organizational Conflicts of Interest Certification Letter
(Month DD, YYYY)
U.S. Army Research Office and
Office of the Director of National Intelligence
Intelligence Advanced Research Projects Activity (IARPA) REASON Program
ATTN: Schon Zwakman, Contracting Officer
Subject: OCI Certification
Reference: <Insert Program Name>, BAA# W911NF-23-S-0007, (Insert assigned proposal ID#,
if received)
Dear ,
In accordance with IARPA Broad Agency Announcement # W911NF-23-S-0007, Organizational
Conflicts of Interest (OCI), and on behalf of (Offeror name) I certify that neither (Offeror name)
nor any of our subcontractor teammates has as a potential conflict of interest, real or perceived, as
it pertains to the REASON program. Please note the following subcontractors and their proposed
roles:
[Please list all proposed contractors by name with a brief description of their proposed
involvement.]
If you have any questions, or need any additional information, please contact (Insert name of
contact) at (Insert phone number) or (Insert e-mail address).
Sincerely,
(Insert organization name)
(Shall be signed by an official that has the authority to bind the organization)
(Insert signature)
(Insert name of signatory) (Insert title of signatory)
66
8. Example of Three Chart Summary of the Proposal
• Chart 1: Overview
o Self-contained, intuitive description of the technical approach and performance. Avoid
acronyms, especially those that are contractor specific.
• Chart 2: Key Innovations
o Suggested format is a two column chart with innovations listed on the left, supporting
graphics or data on the right.
• Chart 3: Expected Impact
o Deliverable 1: Performance and Impact
o Deliverable 2: Performance and Impact (continue for additional major deliverables)
o Unique aspects of the proposal 
67
9. Sample of the Research Data Management Plan
The Offeror must address each of the elements noted below.
The RDMP shall comply with the requirements stated in Section 4 of the
BAA. In doing so, it will support the objectives of the ODNI Public Access
Plan at https://www.iarpa.gov/index.php/research-programs/public-accessto-iarpa-research
1. Sponsoring IARPA Program (required):
2. Offeror (i.e., lead organization responding to BAA) (required):
3. Offeror point of contact (required):
The point of contact is the proposed principal investigator (PI) or his/her Designee.
a. Name and Position:
b. Organization:
c. Email:
d. Phone:
4. Research data types (required):
Provide a brief, high-level description of the types of data to be collected or
produced in the course of the project.
5. Standards for research data and metadata content and format (required):
Use standards reflecting the best practices of the relevant scientific
discipline and research community whenever possible.
6. Plans for making the research data that underlie the results in
peer-reviewed journal articles and conference papers digitally accessible
to the public at the time of publication/conference or within a reasonable time
thereafter (required):
The requirement could be met by including the data as supplementary
information to a peer reviewed journal article or conference paper or by
depositing the data in suitable repositories available to the public.
a. Anticipated method(s) of making research data publicly accessible:
Provide dataset(s) to publisher as supplementary information (if
publishers allow public access)
 Deposit dataset(s) in Data Repository
 Other (specify)
b. Proposed research data repository or repositories (for
dataset(s) not provided as supplementary information):
Suitable repositories could be discipline-specific repositories,
general purpose research data repositories, or institutional
repositories, as long as they are publicly accessible.
c. Retention period, at least three years after publication of
associated research results:
State the minimum length of time the data will remain publicly accessible.
d. Submittal of metadata to IARPA:
Offerors are required to make datasets underlying the results 
68
published in peer-reviewed journal or conferences digitally accessible
to the public to the extent feasible. Here, the Proposer should state a
commitment to submit metadata on such datasets to IARPA in a timely
manner. Note: This does not supersede any requirements for
deliverable data, as the award document may include metadata as a
deliverable item.
7. Policies and provisions for sharing and preservation (as applicable):
a. Policies and provisions for appropriate protection of privacy,
confidentiality, security, and intellectual property:
b. Descriptions of tools, including software, which may be
needed to access and interpret the data:
c. Policies and provisions for re-use, re-distribution, and
production of derivative works:
8. Justification for not sharing and/or preserving data underlying
the results of peer- reviewed publications (as applicable):
If, for legitimate reasons, the data cannot be shared and preserved,
the plan must include a justification detailing such reasons. Potential
reasons may include privacy, confidentiality, security, IP rights
considerations; size of data sets; cost of sharing and preservation; time
required to prepare the dataset(s) for sharing and preservation.
69
10. Cover Sheet – Cost Proposal
(1) BAA Number W911NF-23-S-0007
(2) Technical Area(s) (TA)(s)
(3) Lead organization submitting proposal
(4) Type of Business, Selected Among the Following Categories: “Large
Business”, “Small Disadvantaged Business”, “Other Small Business”,
“HBCU”, “MI”, “Other Educational”, or “Other Nonprofit”
(5) Contractor’s Reference Number (if any)
(6) Other Team Members (if applicable) and Type of Business for Each
(7) Proposal Title
(8) Technical Point of Contact to Include: Title, First Name, Last Name,
Street Address, City, State, Zip Code, Telephone, Fax (if available),
Electronic Mail (if available)
(9) Administrative Point of Contact to Include: Title, First Name, Last
Name, Street Address, City, State, Zip Code, Telephone, Fax (if
available), Electronic Mail (if available)
(10) Contract type/award Instrument Requested: specify
(11) Place(s) and Period(s) of Performance
(12) Total Proposed Cost Separated by Basic Award and Option(s) (if
any)
(13) Name, Address, Telephone Number of the Offeror’s Defense Contract
Management Agency (DCMA) Administration Office or Equivalent
Cognizant Contract Administration Entity, if Known
(14) Name, Address, Telephone Number of the Offeror’s Defense Contract
Audit Agency (DCAA) Audit Office or Equivalent Cognizant Contract
Audit Entity, if Known
(15) Date Proposal was Prepared
(16) DUNS Number
(17) TIN Number
(18) CAGE Code
(19) Proposal Validity Period [minimum of 180 days]
(20) Cost Summaries Provided (Appendix B)
(21) Size of Business in accordance with NAICS Code 541712
70
11. Example of Prime Contractor/Subcontract Cost Element Sheet for Volume 2: Cost
Proposal
Prime Contractor/Subcontractor Cost Element Sheet for Volume 2: Cost Proposal
Complete a Cost Element Sheet for the Base Period and each Option Period
COST ELEMENT BASE RATE AMT
DIRECT LABOR (List each labor category
separately. Identify all Key Personnel by
name.)
# of Hours $ $
TOTAL DIRECT LABOR $
FRINGE BENEFITS $ % $
TOTAL LABOR OVERHEAD $ % $
SUBCONTRACTORS, IOTS, CONSULTANTS
(List separately. See below table.)
$
MATERIALS & EQUIPMENT (List each
material and equipment item separately.)
Quantity $ unit price $
SOFTWARE & IP
(List separately. See table below.)
$ $ $
TOTAL MATERIALS & EQUIPMENT $
MATERIAL OVERHEAD $ % $
TRAVEL (List each trip separately.) # of travelers $ price per traveler $
TOTAL TRAVEL $
OTHER DIRECT COSTS (List each
item separately.)
Quantity $ unit price $
TOTAL ODCs $
G&A $ % $
SUBTOTAL COSTS $
COST OF MONEY $ % $
TOTAL COST $
PROFIT/FEE $ % $
TOTAL PRICE/COST $
GOVERNMENT SHARE, IF APPLICABLE $
RECIPIENT SHARE, IF APPLICABLE $
SUBCONTRACTORS/IOTs) & CONSULTANTS PRICE SUMMARY
A B C D E F
SUBCONTRACTOR
IOT &
CONSULTANT
NAME
SOW TASKS
PERFORMED
*
TYPE
OF
AWARD
SUBCONTRACTOR, IOT &
CONSULTA
NT
QUOTED
COST PROPOSED
BY PRIME FOR
SUBCONTRACTOR,
IOT &
CONSULTANT
DIFFERENCE
(Column D -
Column E)
IF
APPLICABL
E
TOTALS
*Identify Statement of Work, Milestone or Work Breakdown Structure paragraph, or provide a narrative
explanation as an addendum to this Table that describes the effort to be performed.
71
12. Example of Travel Costs Trip Breakdown Sheet
Trip
Breakdown
Base -
Phase I:
Trip # Month
of Trip
# of
Travelers
Name of
Traveler/Company
# of
Days
Location Purpose
of
Travel
Estimated
Cost
Option
Period -
Phase II:
Trip # Month
of Trip
# of
Travelers
Name of
Traveler/Company
# of
Days
Location Purpose
of
Travel
Estimated
Cost
Option
Period -
Phase
III:
Trip # Month
of Trip
# of
Travelers
Name of
Traveler/Company
# of
Days
Location Purpose
of
Travel
Estimated
Cost
72
13. Glossary of Acronyms:
Term Definition
α-nDCG Alpha-Normalized Discounted Cumulative Gain
API Application Programming Interface
CO Contracting Officer
COTR Contract Officer Technical Representative
F1 Harmonic Mean of Precision and Recall (Equally Weighted)
IC Intelligence Community
ICD Intelligence Community Directive
IP Intellectual Property
PM Program Manager
REASON Rapid Explanation, Analysis, and Sourcing Online
RCQ REASON Comment Quality
REQ REASON Explanation Quality
RQS REASON Quality Score
TA Task Area
T&E Test and Evaluation
73
14. References
• Intelligence Community Directive 203 Analytic Standards,
https://www.dni.gov/files/documents/ICD/ICD%20203%20Analytic%20Standards.pdf.
• Tradecraft Primer: Structured Analytic Techniques for Improving Intelligence Analysis,
https://www.cia.gov/static/955180a45afe3f5013772c313b16face/Tradecraft-Primerapr09.pdf
• A Tradecraft Primer: Basic Structured Analytic Techniques,
https://www.dia.mil/FOIA/FOIA-Electronic-Reading-Room/FileId/161442/

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
        