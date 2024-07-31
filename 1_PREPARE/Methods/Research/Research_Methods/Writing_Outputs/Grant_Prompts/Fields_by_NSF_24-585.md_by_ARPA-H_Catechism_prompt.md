
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
        NSF 24-585: Privacy-Preserving Data Sharing in Practice (PDaSP)
Program Solicitation
Document Information
Document History
Posted: June 26, 2024
Download the solicitation (PDF, 0.9mb)
View the program page
NSF Logo		
National Science Foundation
Directorate for Technology, Innovation and Partnerships
     Innovation and Technology Ecosystems
Directorate for Computer and Information Science and Engineering
     Division of Computer and Network Systems

DOTFHWA logo		
U.S. Department of Transportation, Federal Highway Administration

INTC logo		
Intel Corporation

VMware logo		
VMware LLC

NIST logo		
National Institute of Standards and Technology

Full Proposal Deadline(s) (due by 5 p.m. submitting organization's local time):

     September 27, 2024

Table Of Contents
Summary of Program Requirements

Introduction
Program Description
Award Information
Eligibility Information
Proposal Preparation and Submission Instructions
Proposal Preparation Instructions
Budgetary Information
Due Dates
Research.gov/Grants.gov Requirements
NSF Proposal Processing and Review Procedures
Merit Review Principles and Criteria
Review and Selection Process
Award Administration Information
Notification of the Award
Award Conditions
Reporting Requirements
Agency Contacts
Other Information
Important Information And Revision Notes
Any proposal submitted in response to this solicitation should be submitted in accordance with the NSF Proposal & Award Policies & Procedures Guide (PAPPG) that is in effect for the relevant due date to which the proposal is being submitted. The NSF PAPPG is regularly revised and it is the responsibility of the proposer to ensure that the proposal meets the requirements specified in this solicitation and the applicable version of the PAPPG. Submitting a proposal prior to a specified deadline does not negate this requirement.

Summary Of Program Requirements
General Information
Program Title:

Privacy-Preserving Data Sharing in Practice (PDaSP)

Synopsis of Program:

In today's hyperconnected and device-rich world, increasing computational power and the explosive growth of data present us with tremendous opportunities to enable data-driven, evidence-based decision-making capabilities to accelerate scientific discovery and innovation. However, to be able to responsibly leverage the insights from and power of data, such as for training powerful artificial intelligence (AI) models, it is important to have practically deployable and scalable technologies that allow data sharing in a privacy-preserving manner. While there has been significant research progress in privacy-related areas, privacy-preserving data sharing technologies remain at various levels of maturity in terms of practical deployment.

The goals of the PDaSP program are aligned with the Executive Order on the Safe, Secure, and Trustworthy Development and Use of Artificial Intelligence (AI EO), which emphasizes the role for privacy-enhancing technologies (PETs) in a responsible and safe AI future. The EO directs NSF to, "where feasible and appropriate, prioritize research — including efforts to translate research discoveries into practical applications — that encourage the adoption of leading-edge PETs solutions for agencies' use." It also tasks NSF with "developing and helping to ensure the availability of testing environments, such as testbeds, to support the development of safe, secure, and trustworthy AI technologies, as well as to support the design, development, and deployment of associated PETs." In addition to meeting these directives in the AI EO, the PDaSP program strives to address key recommendations made in the National Strategy to Advance Privacy Preserving Data Sharing and Analytics (PPDSA). In particular, the program strives to advance the strategy's priority to "Accelerate Transition to Practice," which includes efforts to "promote applied and translational research and systems development," develop "tool repositories, measurement methods, benchmarking, and testbeds," and "improve usability and inclusiveness of PPDSA solutions."

The PDaSP program welcomes proposals from qualified researchers and multidisciplinary teams in the following tracks with expected funding ranges for proposals as shown below.

Track 1: Advancing key technologies to enable practical PPDSA solutions:

Track 1 projects are expected to be budgeted in the $500K - $1M range for up to 2 years
Track 2: Integrated and comprehensive solutions for trustworthy data sharing in application settings:

Track 2 projects are expected to be budgeted in the $1M - $1.5M range for up to 3 years
Track 3: Usable tools, and testbeds for trustworthy sharing of private or otherwise confidential data.

Track 3 projects are expected to be budgeted in the $500K - $1.5M range for up to 3 years
The PDaSP program represents the collaborative efforts of the NSF Technology, Innovation and Partnerships (TIP) and Computer and Information Science and Engineering (CISE) directorates, Intel Corporation and VMware LLC as industry partners, and the U.S. Department of Transportation Federal Highway Administration (FHWA) and the U.S. Department of Commerce National Institute of Standards and Technology (NIST) as federal agency partners.

This solicitation includes partners from both industry and the federal government, and welcomes new partners from both public and private sectors ahead of the proposal submission deadline. PIs will be given the option of having their proposals considered for new partner co-funding based on matching areas of interest.

Cognizant Program Officer(s):

Please note that the following information is current at the time of publishing. See program website for any updates to the points of contact.

James Joshi, TIP/ITE, telephone: (703) 292-8450, email: jjoshi@nsf.gov
Anna Squicciarini, CISE/CNS, telephone: (703) 292-5177, email: asquicci@nsf.gov
Xiaogang Wang, CISE/CNS, telephone: (703) 292-2812, email: xiawang@nsf.gov
Questions regarding this program can be emailed to, telephone: (please use email), email: TIP-PDaSP-Ask@nsf.gov

Applicable Catalog of Federal Domestic Assistance (CFDA) Number(s):

20.200 --- Highway Research and Development Program
47.070 --- Computer and Information Science and Engineering
47.084 --- NSF Technology, Innovation and Partnerships
Award Information
Anticipated Type of Award: Standard Grant or Continuing Grant

Estimated Number of Awards: 26

NSF anticipates making up to 12 Track 1 awards; up to 7 Track 2 awards; and up to 7 Track 3 awards, depending on the quality of submissions and the availability of funds.

Anticipated Funding Amount: $23,000,000

$23M, subject to availability of funds

Eligibility Information
Who May Submit Proposals:

Proposals may only be submitted by the following:

Institutions of Higher Education (IHEs) - Two- and four-year IHEs (including community colleges) accredited in, and having a campus located in the U.S., acting on behalf of their faculty members.
Non-profit, non-academic organizations: Independent museums, observatories, research laboratories, professional societies and similar organizations located in the U.S. that are directly associated with educational or research activities.
U.S.-based small businesses, as defined by SBA's small business size regulations 13 CFR Part 121, with strong capabilities in scientific or engineering research or education and a passion for innovation. NSF SBIR/STTR recipients are especially encouraged to submit, though NSF welcomes proposals from all interested and qualifying small business concerns, including those funded by other agency SBIR/STTR programs.
Who May Serve as PI:

The PI, co-PIs, or any other senior/key personnel must hold an appointment at an organization that is eligible to submit as described under "Who May Submit Proposals."
Researchers with primary appointments at overseas branch campuses of U.S. institutions of higher education are not eligible.
Researchers from foreign academic institutions who contribute essential expertise to the project may participate as senior/key personnel or collaborators but may not receive NSF support.
Individuals affiliated with a partner involved in this solicitation, notably those who are currently employed by, consulting for, or on an active agreement to provide services for the partner, may NOT participate in proposals to the program.
Limit on Number of Proposals per Organization:

There are no restrictions or limits.

Limit on Number of Proposals per PI or co-PI: 2

An individual can participate as PI, co-PI, or senior/key personnel in no more than TWO PDaSP proposals submitted in response to this solicitation. If an individual exceeds this limit, the first TWO proposals received within the deadline will be accepted based on the earliest date and time of proposal submission. No exceptions will be made.

Proposal Preparation and Submission Instructions
A. Proposal Preparation Instructions

Letters of Intent: Not required
Preliminary Proposal Submission: Not required
Full Proposals:
Full Proposals submitted via Research.gov: NSF Proposal and Award Policies and Procedures Guide (PAPPG) guidelines apply. The complete text of the PAPPG is available electronically on the NSF website at: https://www.nsf.gov/publications/pub_summ.jsp?ods_key=pappg.
Full Proposals submitted via Grants.gov: NSF Grants.gov Application Guide: A Guide for the Preparation and Submission of NSF Applications via Grants.gov guidelines apply (Note: The NSF Grants.gov Application Guide s available on the Grants.gov website and on the NSF website at: https://www.nsf.gov/publications/pub_summ.jsp?ods_key=grantsgovguide).
B. Budgetary Information

Cost Sharing Requirements:
Inclusion of voluntary committed cost sharing is prohibited.

Indirect Cost (F&A) Limitations:
Not Applicable

Other Budgetary Limitations:
Other budgetary limitations apply. Please see the full text of this solicitation for further information.

C. Due Dates

Full Proposal Deadline(s) (due by 5 p.m. submitting organization's local time):
     September 27, 2024

Proposal Review Information Criteria
Merit Review Criteria:

National Science Board approved criteria. Additional merit review criteria apply. Please see the full text of this solicitation for further information.

Award Administration Information
Award Conditions:

Additional award conditions apply. Please see the full text of this solicitation for further information.

Reporting Requirements:

Additional reporting requirements apply. Please see the full text of this solicitation for further information.

I. Introduction
Data plays a central role in our increasingly digital world, where technological innovations allow for the generation, collection, sharing, analysis and seamless flow of large amounts of privacy-sensitive information. These advances, including the explosive growth and rapid adoption of AI, provide unprecedented opportunities to derive value from data to enable better-informed, data-driven decision-making capabilities, accelerate scientific innovation, and enable societal progress. These advances, however, also raise significant concerns related to privacy and possible harm to individuals, enterprises, and society at large. To unleash a future in which the power of data is leveraged for the benefit of all, it is important to develop practical and easily deployable privacy-preserving data sharing and analytics (PPDSA) technologies.

The Privacy-preserving Data Sharing in Practice (PDaSP) program seeks to foster innovative, use-inspired and translational research to mature and scale existing models, methodologies, or constructs in order to accelerate the development and deployment of practical privacy-preserving data sharing solutions. Through this program, NSF, in partnership with industry funding partners and other federal agencies, aims to accelerate efforts to develop practical and deployable solutions that enable data sharing and analytics in a privacy-preserving manner.

The solicitation addresses key recommendations from the National Strategy to Advance Privacy Preserving Data Sharing and Analytics. In particular, it seeks to advance the priority defined in the strategy to "Accelerate Transition to Practice," which includes efforts to "promote applied and translational research and systems development," develop "tool repositories, measurement methods, benchmarking, and testbeds," and "improve usability and inclusiveness of PPDSA solutions." The goals of the PDaSP program are also aligned with the Executive Order on the Safe, Secure, and Trustworthy Development and Use of Artificial Intelligence(AI EO), which emphasizes the role for privacy-enhancing technologies (PETs) in a responsible and safe AI future. The EO directs NSF to, "where feasible and appropriate, prioritize research — including efforts to translate research discoveries into practical applications — that encourage the adoption of leading-edge PETs solutions for agencies' use." It also tasks NSF with "developing and helping to ensure the availability of testing environments, such as testbeds, to support the development of safe, secure, and trustworthy AI technologies, as well as to support the design, development, and deployment of associated PETs." This solicitation also aligns with the research objective to "enhance trustworthiness of Cyberspace by minimizing privacy risk and harm's "emphasized in the Federal Cybersecurity R&D Strategic Plan; and the objective to advance R&D that reinforces "security, privacy and resilience of digital assets" highlighted in the National Objectives for Digital Assets R&D.

The PDaSP program combines the expertise of NSF's Technology, Innovation and Partnerships (TIP) and Computer and Information Science and Engineering (CISE) directorates in developing and managing use-inspired and translational PPDSA research. NSF has a long history of supporting privacy R&D through programs such as Secure and Trustworthy Cyberspace (SaTC), and PDaSP aims to provide a path to transition innovative ideas into real-world deployment. The TIP directorate is charged with accelerating use-inspired and translational research and development (R&D) to advance U.S. competitiveness in key technology focus areas.

II. Program Description
The explosive growth of data enabled by technological advances, and the proliferation of data protection and privacy laws and regulations in various states throughout the U.S. as well as around the globe over the last few years show the urgency of strengthening data privacy and minimizing privacy harms to people and communities. They also add significant challenges to developing practical technological and socio-technical PPDSA solutions that are easy-to-use, and compliant with regulations within the interconnected multi-jurisdictional environments where privacy-sensitive data is shared and used.

While there are promising initial real-world deployments of various PPDSA techniques such as differential privacy, secure multi-party computation, and trusted execution environments (TEEs), to name a few, broad adoption of such technologies has been slow due to challenges related to inadequate understanding of privacy risks and harms, limited access to technical expertise, trust and transparency among participants with regard to data collection and use, uncertainty about legal compliance, financial costs, and technical maturity or deployment readiness of solutions.

This solicitation seeks to foster innovative use-inspired and translational research to mature and scale existing models, methodologies, or constructs at the intersection of privacy goals and socio-economic or policy challenges. Of particular interest is innovation and translation of technologies that empowers data subjects, owners/curators, and other stakeholders to control how privacy-sensitive data is shared and used in order to maximize the utility of data while minimizing potential harms.

It is expected that proposers will consider opportunities and gaps that extend across the computing stack, across development and operations, and across the span of modern deployment scenarios including technologies that may be operated by untrusted parties (e.g., private cloud, public cloud, edge computing).

A central element of this solicitation is to apply, mature, and scale the use of both hardware and software foundations for sharing data while preserving privacy and appropriate use of that data. In that spirit, this solicitation seeks proposals related to maturing PPDSA technologies to increase the utility of data, accompanied by clear plans for relevant demonstration of the viability of the proposed solutions for one or more identified use-cases and/or application contexts. Proposers in academia, non-profit organizations and firms qualifying as small businesses, are welcome. Proposals will be accepted into three tracks as described below.

Track 1: Advancing key technologies to enable practical PPDSA solutions

This track is focused on maturing an individual PPDSA technology, or a combination of technologies, driven by a specific use-case or application area. Illustrative examples are maturing homomorphic encryption to support privacy-preserving analytics over shared data; or attribute-based encryption to enforce privacy-aware access control and data use policies to support a chosen application (e.g., in healthcare, finance, or transportation) in an edge-cloud environment. Similarly, examples of innovative combinations of specific PPDSA technologies may include combining a cryptographic technique (e.g., multi-party computation) with a statistical disclosure limitation technique (e.g., differential privacy) to enable privacy-preserving collaborative machine learning over distributed datasets for real-world applications (e.g., detection of financial fraud; public health prediction).

It is expected that proposing teams will include relevant expertise representing the use-case or application domain selected, and/or collaboration with a potential adopter of the developed solution. The solutions developed should consider clear and relevant threat models, well-understood risks and harms, and practical privacy-utility trade-offs with verifiable privacy guarantees.

Track 2: Integrated and comprehensive solutions for trustworthy data sharing in application settings

This track is focused on advancing integrated and comprehensive privacy management to enable trustworthy data sharing through the development of holistic system architectures that support end-to-end privacy protection and establish verifiable chain of trust considering the deployment context (e.g., meeting requirements for regulatory compliance, and use by diverse user base). In particular, the integrated solutions are expected to empower data subjects and/or owners to be able to control and manage their privacy-sensitive data with respect to access to, sharing of, and use of their data.

The proposed solutions should show promise for enhancing, extending, and creating new opportunities for using data. As such, they should consider ecosystem challenges such as cross-organizational and cross-jurisdictional issues, economic incentives, regulatory environments, open-source ecosystems, and open standards.

Proposals in this track should emphasize customization or maturing of integrative PPDSA solutions that tackle challenges related to specific use-cases and application contexts. These application contexts could include various technological (e.g., Internet of Things-Edge-Cloud continuum) and regulatory/legal contexts (e.g., GDPR, CCPA, HIPAA); incentives for sharing; or one or more of the emerging application domains where integrative PPDSA solutions are or will be critical, such as healthcare (e.g., personalized medicine, genomics), transportation (e.g., autonomous driving, urban planning, smart city infrastructure, and traffic management), disaster management and public health (e.g., pandemic predication), immersive technologies, and digital assets or finance (e.g., anti-money laundering, or combating terrorist financing).

The projects funded under this track are expected to demonstrate the viability of solutions in specific application settings, ensuring usability, and verifiable and acceptable primetime-trade-off guarantees. One technology that demonstrates significant promise for addressing end-to-end protection and the trade-offs between usability and verifiable privacy is confidential computing. Confidential computing is a hardware-based security paradigm that has shown (potentially, in combination with other PPDSA technologies) significant promise as an element of effective comprehensive privacy management. Industry partners Intel and VMware have special interest in the use of confidential computing or equivalent to create a verifiable chain of trust related to privacy protection.

Track 3: Usable tools and testbeds for trustworthy sharing of private or otherwise confidential data

This track emphasizes and recognizes the urgent need to develop tools and testbeds to support and accelerate adoption of PPDSA technologies. There exists a high barrier to adoption for PPDSA technologies, including more mature approaches, due to a lack of effective and easy-to-use tools that help data owners and other stakeholders in the data ecosystem who need to make privacy protection decisions. Effective and easy-to-use tools that support privacy auditing, help assess privacy disclosure risks, improve trust and transparency, facilitate decision-making, and assist in managing privacy parameters, are critical components needed to help us extract value from of data.

Innovative proposals that focus on developing practical tools that enhance capabilities of users (e.g., research community, citizen scientists, data subjects, and data administrators) to foster and democratize PPDSA solutions are encouraged. Proposals should include an application area or use-case that will serve as the demonstration for the effectiveness of the proposed tools and make the tool publicly available.

This track also emphasizes testbeds that support assessment, comparative analysis, vulnerability or threat analysis, privacy risk assessments, and privacy-utility trade-off analysis. Curated datasets relevant to different use-cases can be essential parts of testbeds. The track also welcomes work related to creating sandboxes to enable experiments on PPDSA technologies and to help address policy challenges in controlled environments.

PARTNERSHIP AND COLLABORATION

The PDaSP program is catalyzed by partnerships with industry and other federal agencies. Current partners for this solicitation include: (1) Intel Corporation; (2) VMware LLC; (3) Federal Highway Administration (FHWA), U.S. Department of Transportation; and (4) National Institute of Standards and Technology (NIST), U.S. Department of Commerce. These four partners' specific areas of interest and nature of collaboration for the PDaSP program are described below.

NSF may enter into partnerships with other agencies, foundations, and organizations interested in co-funding projects submitted to this solicitation up to one month prior to the proposal submission deadline. Potential partners from industry and other federal agencies may reach out to TIP-PDaSP-Ask@nsf.gov for more details.

Industry Partnerships:

Intel Corporation: Intel will provide funding and limited access to relevant hardware resources for PDaSP awards. Intel Corporation has a shared belief in the importance of making progress in use-inspired and translational research related to PPDSA. As part of this partnership, the following has been agreed:

Intel's funding contribution will primarily support projects in Track 2. In particular, Intel would like to support comprehensive privacy-preserving data sharing solutions that use confidential computing.
Upon request, Intel will provide limited access to hardware resources to projects mainly in Track 2, but also in other tracks where the use of confidential computing is justified. The key resource made available will be Intel-hosted virtual machines that support modern confidential computing technologies such as Intel Software Guard Extensions (SGX) or Intel Trust Domain Extensions (TDX). Proposers are required to include a request in the proposal for such resource access and justify the need. Intel will make decisions based on the merit of such requests.
VMware LLC: VMware is interested in providing funding mainly to Track 2 and Track 3 awards, but will also consider proposals that focus on confidential computing and other privacy techniques and technologies that are relevant in the context of AI applications.

Agency Partnerships:

Federal Highway Administration (FHWA): FHWA partnership includes co-funding of projects relevant to FHWA. In particular, FHWA will consider co-funding of projects in Track 1 or Track 2 that are aligned with the following interest area(s).

Naturalistic Traffic Studies in Privacy Preserving manner. The highway transportation research community increasingly is using naturalistic data to understand traffic behavior, which includes both the study of drivers and the study of other road users such as pedestrians or bicyclists. Data collection may involve use of on and in vehicle sensors, roadside sensors, and mobile devices that obtain different modes of data including inertial, radar, LIDAR, visible image, thermal, audio, and GPS location. Such data can provide information that would disclose or allow inference of the identity of people and information about their behavior. FHWA is interested in supporting methods/approaches that would allow secure and privacy-preserving sharing of such data to improve the safety, mobility, and convenience of travel that balances access for research purposes and public benefits. Such proposed methods should include integration of technical approaches and administrative controls. FHWA would expect proposals to include investigators with experience in transportation research, data science, and privacy coming from different disciplines including civil engineering, systems engineering, computer or information science, applied psychology, organizational psychology, or other relevant social sciences. An example of a naturalistic study data is located at https://insight.shrp2nds.us/home. The proposals aligned with this area is expected to be in either Track 1 or Track 2. Information on current Highway Safety Information System data is located at https://highways.dot.gov/research/safety/hsis.

For proposals that are directed to FHWA and are selected for co-funding, FHWA requires a minimum 20 percent funding match for the FHWA portion of funding. The funding match may be in kind based on the value of equipment, materials, data, or labor. This requirement will not be included as a condition of the NSF award. Additional information will be provided by FHWA, and the cost match will be reported to and managed by the FHWA.

National Institute of Standards and Technologies (NIST): NIST is building a PETs testbed initially focused on a privacy-preserving federated learning (PPFL) model environment. The project aims to provide open-source software to run locally and a cloud environment that simulates a central server connected to a set of data silos. The initial deployment of the environment focuses on genomic data and providing input and output privacy protections.

Participants in this funding opportunity are welcome to use NIST software or to potentially collaborate with NIST – this may include enhancing the PPML environment design and broadening its use; adding modular components to support its expansion; contributing benchmark datasets (create and share) for different use-cases (especially beyond genomics); and conducting privacy, security, efficiency, and accuracy research on existing resources. PIs interested in exploring NIST collaboration can reach out to the NIST team at privacyeng@nist.gov.

ADDITIONAL PARTNERSHIP OPPORTUNITIES FOR THIS SOLICITATION

NSF may enter into partnerships with other interested agencies, foundations, and organizations interested in co-funding projects submitted to this solicitation up to one month prior to the proposal submission deadline. PIs on proposals that meet the general eligibility requirements of one or more of these new partners may be contacted by the cognizant NSF Program Officer following submission of their proposals and be given the option of having their proposals considered jointly by NSF and the new partner(s).

Any industry partner that joins after the solicitation has been released is expected to:

Make co-funding contributions at a level that at least matches those from the current industry partners mentioned in this solicitation, which can be discussed when the potential partnership is explored; and
Agree to the "public dedication" approach to intellectual property, publishing and licensing discussed in the "Award Conditions" section of this solicitation.
PIs have the option to accept or decline to be considered for co-funding from the new partners and the sharing of proposals with them in the pre-award phase. Any partner who joins after the solicitation has been released will be included in the "Updates and Announcements" section of the PDaSP program page. PIs are encouraged to check this webpage frequently for news of additional partner involvement.

ACCESS TO EXPERIMENTAL RESEARCH INFRASTRUCTURE

PIs may consider utilizing NSF-supported research infrastructure (such as the Platforms for Advanced Wireless Research, FABRIC, Chameleon, CloudLab) when formulating their research plans and submitting proposals. Descriptions of the capabilities of each system and their availability can be found at their websites: https://advancedwireless.org/, https://fabric-testbed.net/, https://www.chameleoncloud.org/, https://cloudlab.us/.

III. Award Information
Anticipated Type of Award: Standard Grant or Continuing Grant

Estimated Number of Awards:

NSF anticipates making up to 12 Track 1 awards; up to 7 Track 2 awards; and up to 7 Track 3 awards, depending on the quality of submissions and the availability of funds.

Anticipated Funding Amount:

$23M, subject to availability of funds

Estimated program budget, number of awards and average award size/duration are subject to the availability of funds.

IV. Eligibility Information
Who May Submit Proposals:

Proposals may only be submitted by the following:

Institutions of Higher Education (IHEs) - Two- and four-year IHEs (including community colleges) accredited in, and having a campus located in the U.S., acting on behalf of their faculty members.
Non-profit, non-academic organizations: Independent museums, observatories, research laboratories, professional societies and similar organizations located in the U.S. that are directly associated with educational or research activities.
U.S.-based small businesses, as defined by SBA's small business size regulations 13 CFR Part 121, with strong capabilities in scientific or engineering research or education and a passion for innovation. NSF SBIR/STTR recipients are especially encouraged to submit, though NSF welcomes proposals from all interested and qualifying small business concerns, including those funded by other agency SBIR/STTR programs.
Who May Serve as PI:

The PI, co-PIs, or any other senior/key personnel must hold an appointment at an organization that is eligible to submit as described under "Who May Submit Proposals."
Researchers with primary appointments at overseas branch campuses of U.S. institutions of higher education are not eligible.
Researchers from foreign academic institutions who contribute essential expertise to the project may participate as senior/key personnel or collaborators but may not receive NSF support.
Individuals affiliated with a partner involved in this solicitation, notably those who are currently employed by, consulting for, or on an active agreement to provide services for the partner, may NOT participate in proposals to the program.
Limit on Number of Proposals per Organization:

There are no restrictions or limits.

Limit on Number of Proposals per PI or co-PI: 2

An individual can participate as PI, co-PI, or senior/key personnel in no more than TWO PDaSP proposals submitted in response to this solicitation. If an individual exceeds this limit, the first TWO proposals received within the deadline will be accepted based on the earliest date and time of proposal submission. No exceptions will be made.

V. Proposal Preparation And Submission Instructions
A. Proposal Preparation Instructions
Full Proposal Preparation Instructions: Proposers may opt to submit proposals in response to this Program Solicitation via Research.gov or Grants.gov.

Full Proposals submitted via Research.gov: Proposals submitted in response to this program solicitation should be prepared and submitted in accordance with the general guidelines contained in the NSF Proposal and Award Policies and Procedures Guide (PAPPG). The complete text of the PAPPG is available electronically on the NSF website at: https://www.nsf.gov/publications/pub_summ.jsp?ods_key=pappg. Paper copies of the PAPPG may be obtained from the NSF Publications Clearinghouse, telephone (703) 292-8134 or by e-mail from nsfpubs@nsf.gov. The Prepare New Proposal setup will prompt you for the program solicitation number.
Full proposals submitted via Grants.gov: Proposals submitted in response to this program solicitation via Grants.gov should be prepared and submitted in accordance with the NSF Grants.gov Application Guide: A Guide for the Preparation and Submission of NSF Applications via Grants.gov. The complete text of the NSF Grants.gov Application Guide is available on the Grants.gov website and on the NSF website at: (https://www.nsf.gov/publications/pub_summ.jsp?ods_key=grantsgovguide). To obtain copies of the Application Guide and Application Forms Package, click on the Apply tab on the Grants.gov site, then click on the Apply Step 1: Download a Grant Application Package and Application Instructions link and enter the funding opportunity number, (the program solicitation number without the NSF prefix) and press the Download Package button. Paper copies of the Grants.gov Application Guide also may be obtained from the NSF Publications Clearinghouse, telephone (703) 292-8134 or by e-mail from nsfpubs@nsf.gov.
In determining which method to utilize in the electronic preparation and submission of the proposal, please note the following:

Collaborative Proposals. All collaborative proposals submitted as separate submissions from multiple organizations must be submitted via Research.gov. PAPPG Chapter II.E.3 provides additional information on collaborative proposals.

See PAPPG Chapter II.D.2 for guidance on the required sections of a full research proposal submitted to NSF. Please note that the proposal preparation instructions provided in this program solicitation may deviate from the PAPPG instructions.

Proposal Preparation:

Cover Sheet:

Title: Proposal titles should begin with "PDaSP: Track X:" then the title (where X is 1, 2, or 3)

Project Description:

In addition to the content specified in the PAPPG, including the requirement for a separate section labeled "Broader Impacts", the Project Description should contain specific additional sections with the following titles required, as indicated, and described in the above Sections I and II:

Project Justification: Include a section on Project Justification articulating:
How the proposed work aligns with the focus on the use-inspired and translational research, and not basic research; and
How the proposed work addresses the Solicitation Specific criteria
Overall Project Management and Collaboration: describe why the project team is appropriate to realize the project's goals and how the team will assure effective collaboration in the co-design and implementation process. A compelling rationale must be presented for a multi-expertise and multi-organization structure of the project team.
Letters of Collaboration:

Letters of collaboration should follow the recommended format specified in the PAPPG. Proposers must not include letters of collaboration from any of the participating organizations listed in this solicitation. Any proposal that deviates from these guidelines will be returned without review.

Single Copy Documents (if applicable):

Proposers may wish to include proprietary or privileged information as part of their proposals in the Additional Single Copy Documents section of the proposal. This information is for "NSF Use Only" and will not be shared with reviewers or partner representatives. Per the PAPPG, NSF defines such information as "patentable ideas, trade secrets, privileged or confidential commercial or financial information, disclosure of which may harm the proposer."

B. Budgetary Information
Cost Sharing:

Inclusion of voluntary committed cost sharing is prohibited.

Other Budgetary Limitations:

Cost Sharing Requirements for awards made with FHWA

For proposals that are selected by FHWA for co-funding with NSF, FHWA requires a minimum 20 percent funding match for the FHWA portion of funding. The funding match may be in kind based on the value of equipment, materials, data, or labor. Additional information will be provided by FHWA to those selected projects, and the match will be reported to and managed by FHWA.

C. Due Dates
Full Proposal Deadline(s) (due by 5 p.m. submitting organization's local time):
     September 27, 2024

D. Research.gov/Grants.gov Requirements
For Proposals Submitted Via Research.gov:

To prepare and submit a proposal via Research.gov, see detailed technical instructions available at: https://www.research.gov/research-portal/appmanager/base/desktop?_nfpb=true&_pageLabel=research_node_display&_nodePath=/researchGov/Service/Desktop/ProposalPreparationandSubmission.html. For Research.gov user support, call the Research.gov Help Desk at 1-800-381-1532 or e-mail rgov@nsf.gov. The Research.gov Help Desk answers general technical questions related to the use of the Research.gov system. Specific questions related to this program solicitation should be referred to the NSF program staff contact(s) listed in Section VIII of this funding opportunity.

For Proposals Submitted Via Grants.gov:

Before using Grants.gov for the first time, each organization must register to create an institutional profile. Once registered, the applicant's organization can then apply for any federal grant on the Grants.gov website. Comprehensive information about using Grants.gov is available on the Grants.gov Applicant Resources webpage: https://www.grants.gov/applicants. In addition, the NSF Grants.gov Application Guide (see link in Section V.A) provides instructions regarding the technical preparation of proposals via Grants.gov. For Grants.gov user support, contact the Grants.gov Contact Center at 1-800-518-4726 or by email: support@grants.gov. The Grants.gov Contact Center answers general technical questions related to the use of Grants.gov. Specific questions related to this program solicitation should be referred to the NSF program staff contact(s) listed in Section VIII of this solicitation.

Submitting the Proposal: Once all documents have been completed, the Authorized Organizational Representative (AOR) must submit the application to Grants.gov and verify the desired funding opportunity and agency to which the application is submitted. The AOR must then sign and submit the application to Grants.gov. The completed application will be transferred to Research.gov for further processing.

The NSF Grants.gov Proposal Processing in Research.gov informational page provides submission guidance to applicants and links to helpful resources including the NSF Grants.gov Application Guide, Grants.gov Proposal Processing in Research.gov how-to guide, and Grants.gov Submitted Proposals Frequently Asked Questions. Grants.gov proposals must pass all NSF pre-check and post-check validations in order to be accepted by Research.gov at NSF.

When submitting via Grants.gov, NSF strongly recommends applicants initiate proposal submission at least five business days in advance of a deadline to allow adequate time to address NSF compliance errors and resubmissions by 5:00 p.m. submitting organization's local time on the deadline. Please note that some errors cannot be corrected in Grants.gov. Once a proposal passes pre-checks but fails any post-check, an applicant can only correct and submit the in-progress proposal in Research.gov.

Proposers that submitted via Research.gov may use Research.gov to verify the status of their submission to NSF. For proposers that submitted via Grants.gov, until an application has been received and validated by NSF, the Authorized Organizational Representative may check the status of an application on Grants.gov. After proposers have received an e-mail notification from NSF, Research.gov should be used to check the status of an application.

VI. NSF Proposal Processing And Review Procedures
Proposals received by NSF are assigned to the appropriate NSF program for acknowledgement and, if they meet NSF requirements, for review. All proposals are carefully reviewed by a scientist, engineer, or educator serving as an NSF Program Officer, and usually by three to ten other persons outside NSF either as ad hoc reviewers, panelists, or both, who are experts in the particular fields represented by the proposal. These reviewers are selected by Program Officers charged with oversight of the review process. Proposers are invited to suggest names of persons they believe are especially well qualified to review the proposal and/or persons they would prefer not review the proposal. These suggestions may serve as one source in the reviewer selection process at the Program Officer's discretion. Submission of such names, however, is optional. Care is taken to ensure that reviewers have no conflicts of interest with the proposal. In addition, Program Officers may obtain comments from site visits before recommending final action on proposals. Senior NSF staff further review recommendations for awards. A flowchart that depicts the entire NSF proposal and award process (and associated timeline) is included in PAPPG Exhibit III-1.

A comprehensive description of the Foundation's merit review process is available on the NSF website at: https://www.nsf.gov/bfa/dias/policy/merit_review/.

Proposers should also be aware of core strategies that are essential to the fulfillment of NSF's mission, as articulated in Leading the World in Discovery and Innovation, STEM Talent Development and the Delivery of Benefits from Research - NSF Strategic Plan for Fiscal Years (FY) 2022 - 2026. These strategies are integrated in the program planning and implementation process, of which proposal review is one part. NSF's mission is particularly well-implemented through the integration of research and education and broadening participation in NSF programs, projects, and activities.

One of the strategic objectives in support of NSF's mission is to foster integration of research and education through the programs, projects, and activities it supports at academic and research institutions. These institutions must recruit, train, and prepare a diverse STEM workforce to advance the frontiers of science and participate in the U.S. technology-based economy. NSF's contribution to the national innovation ecosystem is to provide cutting-edge research under the guidance of the Nation's most creative scientists and engineers. NSF also supports development of a strong science, technology, engineering, and mathematics (STEM) workforce by investing in building the knowledge that informs improvements in STEM teaching and learning.

NSF's mission calls for the broadening of opportunities and expanding participation of groups, institutions, and geographic regions that are underrepresented in STEM disciplines, which is essential to the health and vitality of science and engineering. NSF is committed to this principle of diversity and deems it central to the programs, projects, and activities it considers and supports.

A. Merit Review Principles and Criteria
The National Science Foundation strives to invest in a robust and diverse portfolio of projects that creates new knowledge and enables breakthroughs in understanding across all areas of science and engineering research and education. To identify which projects to support, NSF relies on a merit review process that incorporates consideration of both the technical aspects of a proposed project and its potential to contribute more broadly to advancing NSF's mission "to promote the progress of science; to advance the national health, prosperity, and welfare; to secure the national defense; and for other purposes." NSF makes every effort to conduct a fair, competitive, transparent merit review process for the selection of projects.

1. Merit Review Principles

These principles are to be given due diligence by PIs and organizations when preparing proposals and managing projects, by reviewers when reading and evaluating proposals, and by NSF program staff when determining whether or not to recommend proposals for funding and while overseeing awards. Given that NSF is the primary federal agency charged with nurturing and supporting excellence in basic research and education, the following three principles apply:

All NSF projects should be of the highest quality and have the potential to advance, if not transform, the frontiers of knowledge.
NSF projects, in the aggregate, should contribute more broadly to achieving societal goals. These "Broader Impacts" may be accomplished through the research itself, through activities that are directly related to specific research projects, or through activities that are supported by, but are complementary to, the project. The project activities may be based on previously established and/or innovative methods and approaches, but in either case must be well justified.
Meaningful assessment and evaluation of NSF funded projects should be based on appropriate metrics, keeping in mind the likely correlation between the effect of broader impacts and the resources provided to implement projects. If the size of the activity is limited, evaluation of that activity in isolation is not likely to be meaningful. Thus, assessing the effectiveness of these activities may best be done at a higher, more aggregated, level than the individual project.
With respect to the third principle, even if assessment of Broader Impacts outcomes for particular projects is done at an aggregated level, PIs are expected to be accountable for carrying out the activities described in the funded project. Thus, individual projects should include clearly stated goals, specific descriptions of the activities that the PI intends to do, and a plan in place to document the outputs of those activities.

These three merit review principles provide the basis for the merit review criteria, as well as a context within which the users of the criteria can better understand their intent.

2. Merit Review Criteria

All NSF proposals are evaluated through use of the two National Science Board approved merit review criteria. In some instances, however, NSF will employ additional criteria as required to highlight the specific objectives of certain programs and activities.

The two merit review criteria are listed below. Both criteria are to be given full consideration during the review and decision-making processes; each criterion is necessary but neither, by itself, is sufficient. Therefore, proposers must fully address both criteria. (PAPPG Chapter II.D.2.d(i). contains additional information for use by proposers in development of the Project Description section of the proposal). Reviewers are strongly encouraged to review the criteria, including PAPPG Chapter II.D.2.d(i), prior to the review of a proposal.

When evaluating NSF proposals, reviewers will be asked to consider what the proposers want to do, why they want to do it, how they plan to do it, how they will know if they succeed, and what benefits could accrue if the project is successful. These issues apply both to the technical aspects of the proposal and the way in which the project may make broader contributions. To that end, reviewers will be asked to evaluate all proposals against two criteria:

Intellectual Merit: The Intellectual Merit criterion encompasses the potential to advance knowledge; and
Broader Impacts: The Broader Impacts criterion encompasses the potential to benefit society and contribute to the achievement of specific, desired societal outcomes.
The following elements should be considered in the review for both criteria:

What is the potential for the proposed activity to
Advance knowledge and understanding within its own field or across different fields (Intellectual Merit); and
Benefit society or advance desired societal outcomes (Broader Impacts)?
To what extent do the proposed activities suggest and explore creative, original, or potentially transformative concepts?
Is the plan for carrying out the proposed activities well-reasoned, well-organized, and based on a sound rationale? Does the plan incorporate a mechanism to assess success?
How well qualified is the individual, team, or organization to conduct the proposed activities?
Are there adequate resources available to the PI (either at the home organization or through collaborations) to carry out the proposed activities?
Broader impacts may be accomplished through the research itself, through the activities that are directly related to specific research projects, or through activities that are supported by, but are complementary to, the project. NSF values the advancement of scientific knowledge and activities that contribute to achievement of societally relevant outcomes. Such outcomes include, but are not limited to: full participation of women, persons with disabilities, and other underrepresented groups in science, technology, engineering, and mathematics (STEM); improved STEM education and educator development at any level; increased public scientific literacy and public engagement with science and technology; improved well-being of individuals in society; development of a diverse, globally competitive STEM workforce; increased partnerships between academia, industry, and others; improved national security; increased economic competitiveness of the United States; and enhanced infrastructure for research and education.

Proposers are reminded that reviewers will also be asked to review the Data Management and Sharing Plan and the Mentoring Plan, as appropriate.

Additional Solicitation Specific Review Criteria

Each track has its specific additional review criteria, as follows.

For Track 1

Proposals that are submitted to this track will be evaluated based on the following criteria, in addition to general Merit Review criteria:

Does the proposal address a significant translational research gap in transitioning theory to practice for the key PPDSA technique(s) considered?
Do the expected outcomes show promise of broader deployment or adoption of the PPDSA solution(s) proposed considering factors such as scalability, efficiency, and privacy-utility trade-offs, as appropriate, for the identified use-cases or applications, while addressing practically relevant threat models?
Are the expect outcomes easily generalizable, or customizable to use-cases or applications not specifically considered in the proposal?
Does the project plan adequately address system development and implementation milestones and evaluation? Does the project team include appropriate expertise to ensure success of the project? As applicable, the project plan should include clear description of collaboration with any partnering organizations that would act as data provider, use-case provider, and/or early adopter.
For Track 2

Proposals that are submitted to this track will be evaluated based on the following criteria, in addition to general Merit Review criteria:

Does the proposal address a significant translational research gap in transitioning theory to practice considering an integrative, systems approach and end-to-end privacy protection?
Does the proposal comprehensively address the challenges of privacy preserving data sharing and use within specific data sharing community context, or application, considering the needs of all stakeholders, and relevant threat models?
Does the proposal adequately justify the practical challenges of integrating various technologies across computing stack (i.e., they are not trivial) to enable privacy-preserving data sharing?
Is the integrated solution justifiably more scalable, and more mature than comparable existing solutions, or does the proposal demonstrate significant promise for increased adoption or deployment of the proposed integrative solution?
Does the project plan adequately address system development and implementation milestones and evaluation? Does the project team include appropriate expertise to ensure success of the project? As applicable, the project plan should include clear description of collaboration with any partnering organizations that would act as data provider, use-case provider, and/or early adopter.
For Track 3

Proposals that are submitted to this track will be evaluated based on the following criteria, in addition to general Merit Review criteria:

Does the proposal adequately justify that the proposed tools and/or testbeds are novel, show promise to fulfill a significant need, and help promote PPDSA adoption?
Are the proposed tools easy to use and deployable, or can they be easily integrated in targeted system environments?
Does the proposed testbed show promise for effectively supporting experimentation, testing and evaluation, and/or validation of PPDSA solutions? Is the proposed testbed applicable for a specific set of PPDSA solutions, data sharing communities or applications, or are they generalized?
Is there a clear and convincing plan for integrating and/or sustaining the proposed tools or and testbeds within the broader PPDSA ecosystem (e.g., in open-source ecosystems).
B. Review and Selection Process
Proposals submitted in response to this program solicitation will be reviewed by Ad hoc Review and/or Panel Review.

Partner Pre-award Engagement: Prior to the award, industry partners will not participate in nor observe the merit review of proposals. Federal agency partners may be invited as observers to attend the review panels where the relevant proposals are discussed. After the completion of the merit review process, NSF may share with representatives of industry and agency partners a subset of proposals aligned with their areas of interest along with corresponding unattributed reviews and panel summaries. NSF will take into consideration the input of the partners prior to making final funding decisions. A partner may decline to provide feedback on proposals. Proprietary or privileged information provided by the PI in the separate Additional Single Copy Documents section of the proposal will not be shared with reviewers or partner representatives.

NSF will take into consideration the input of partners prior to making final funding decisions but will retain final authority for making all award decisions. Proposals selected for partner co-funding will be awarded by NSF using funds transferred from the partner to NSF.

Reviewers will be asked to evaluate proposals using two National Science Board approved merit review criteria and, if applicable, additional program specific criteria. A summary rating and accompanying narrative will generally be completed and submitted by each reviewer and/or panel. The Program Officer assigned to manage the proposal's review will consider the advice of reviewers and will formulate a recommendation.

After scientific, technical and programmatic review and consideration of appropriate factors, the NSF Program Officer recommends to the cognizant Division Director whether the proposal should be declined or recommended for award. NSF strives to be able to tell proposers whether their proposals have been declined or recommended for funding within six months. Large or particularly complex proposals or proposals from new recipients may require additional review and processing time. The time interval begins on the deadline or target date, or receipt date, whichever is later. The interval ends when the Division Director acts upon the Program Officer's recommendation.

After programmatic approval has been obtained, the proposals recommended for funding will be forwarded to the Division of Grants and Agreements or the Division of Acquisition and Cooperative Support for review of business, financial, and policy implications. After an administrative review has occurred, Grants and Agreements Officers perform the processing and issuance of a grant or other agreement. Proposers are cautioned that only a Grants and Agreements Officer may make commitments, obligations or awards on behalf of NSF or authorize the expenditure of funds. No commitment on the part of NSF should be inferred from technical or budgetary discussions with a NSF Program Officer. A Principal Investigator or organization that makes financial or personnel commitments in the absence of a grant or cooperative agreement signed by the NSF Grants and Agreements Officer does so at their own risk.

Once an award or declination decision has been made, Principal Investigators are provided feedback about their proposals. In all cases, reviews are treated as confidential documents. Verbatim copies of reviews, excluding the names of the reviewers or any reviewer-identifying information, are sent to the Principal Investigator/Project Director by the Program Officer. In addition, the proposer will receive an explanation of the decision to award or decline funding.

VII. Award Administration Information
A. Notification of the Award
Notification of the award is made to the submitting organization by an NSF Grants and Agreements Officer. Organizations whose proposals are declined will be advised as promptly as possible by the cognizant NSF Program administering the program. Verbatim copies of reviews, not including the identity of the reviewer, will be provided automatically to the Principal Investigator. (See Section VI.B. for additional information on the review process.)

B. Award Conditions
An NSF award consists of: (1) the award notice, which includes any special provisions applicable to the award and any numbered amendments thereto; (2) the budget, which indicates the amounts, by categories of expense, on which NSF has based its support (or otherwise communicates any specific approvals or disapprovals of proposed expenditures); (3) the proposal referenced in the award notice; (4) the applicable award conditions, such as Grant General Conditions (GC-1)*; or Research Terms and Conditions* and (5) any announcement or other NSF issuance that may be incorporated by reference in the award notice. Cooperative agreements also are administered in accordance with NSF Cooperative Agreement Financial and Administrative Terms and Conditions (CA-FATC) and the applicable Programmatic Terms and Conditions. NSF awards are electronically signed by an NSF Grants and Agreements Officer and transmitted electronically to the organization via e-mail.

*These documents may be accessed electronically on NSF's Website at https://www.nsf.gov/awards/managing/award_conditions.jsp?org=NSF. Paper copies may be obtained from the NSF Publications Clearinghouse, telephone (703) 292-8134 or by e-mail from nsfpubs@nsf.gov.

More comprehensive information on NSF Award Conditions and other important information on the administration of NSF awards is contained in the NSF Proposal & Award Policies & Procedures Guide (PAPPG) Chapter VII, available electronically on the NSF Website at https://www.nsf.gov/publications/pub_summ.jsp?ods_key=pappg.

Administrative and National Policy Requirements

Build America, Buy America

As expressed in Executive Order 14005, Ensuring the Future is Made in All of America by All of America's Workers (86 FR 7475), it is the policy of the executive branch to use terms and conditions of Federal financial assistance awards to maximize, consistent with law, the use of goods, products, and materials produced in, and services offered in, the United States.

Consistent with the requirements of the Build America, Buy America Act (Pub. L. 117-58, Division G, Title IX, Subtitle A, November 15, 2021), no funding made available through this funding opportunity may be obligated for infrastructure projects under an award unless all iron, steel, manufactured products, and construction materials used in the project are produced in the United States. For additional information, visit NSF's Build America, Buy America webpage.

Special Award Conditions:

Each proposing organization that is new to NSF, or has not had an active NSF assistance award within the previous five years, or has only received SBIR/STTR funding from NSF should be prepared to submit basic organization and management information and certifications, when requested, to the applicable award-making division within the Office of Budget, Finance & Award Management (BFA). The requisite information is described in the NSF Prospective New Awardee Guide (https://www.nsf.gov/publications/pub_summ.jsp?ods_key=pnag). The information contained in this Guide will assist the organization in preparing documents which NSF requires to conduct administrative and financial reviews of the organization. This Guide also serves as a means of highlighting the accountability requirements associated with Federal awards.

Partner Post-award Engagement

NSF will administer awards under the PDaSP program in accordance with standard NSF policies and procedures. All awards will be subject to standard NSF terms and conditions. A partner may arrange to fund their own personnel as researchers to directly participate, part-time or full-time, with recipient project personnel. These arrangements will be optional and based upon the mutual consent of the partner and the respective recipient team and/or organizations. No recipient will be required to accept an industry or agency partner researcher.

As in the arrangement with Intel and NIST, a partner may make available specific resources to all funded projects based on appropriateness of requests. Any update to such resource sharing will be updated in the "Updates and Announcements" section of the PDaSP program page.

A partner may attend annual PI meetings. The PI meetings if held, would be inclusive of all the active PDaSP projects. A partner may also host the event, sponsor all or some components of the event, including but not limited to participant travel, e.g., those not supported by the project such as post-docs, students, etc.

Acknowledgement of Support:

Recipients will be required to include appropriate acknowledgment of NSF and Funding Partner(s) support in reports and/or publications on work performed under an award. An example of such an acknowledgement would be: "This material is based upon work supported by the National Science Foundation under grant no. (NSF grant number) and is supported in part by funds from federal agency and industry funding partners as specified in the Privacy-Preserving Data Sharing in Practice (PDaSP) program."

PDaSP PI Meetings:

The PDaSP program plans to host a kick-off meeting in Fall of 2025 with a goal to foster networking among teams and the partners as well as other selected stakeholder communities. There will also be annual PI Meetings at a time, to be determined, when projects are at a more mature phases of implementation. These meetings will be a community-wide event with representatives from partnering organizations as well as other federal agencies, academia, industry, and international institutions. Principal investigators are expected to participate in these meetings.

For all awards, one or more project representatives (PI, co-PI, or senior/key personnel or NSF-approved replacement) must attend the first PI meeting held after the award date. For multi-organization projects, only one PI needs to attend, not one per organization (though this is welcomed).

PIs are expected to include travel budget items for to attend these meetings.

Intellectual property, publishing, and licensing:

PDaSP recipients will agree to dedicate to the public intellectual property resulting from the research funded as part of this program, and further:

the recipients will, with respect to software, offer such software through an open-source license under an Apache 2.0 license found at: https://opensource.org/licenses/apache2.0, the BSD license found at: http://www.opensource.org/licenses/bsd-license.php or the MIT License found at: http://www.opensource.org/licenses/mit-license.php; in the event the software already contains code licensed under GNU's General Public License (GPL), then the open source shall be through GPL version 3 found at http://www.gnu.org/licenses/gpl.html;
the recipients will submit for publication in openly available literature any results of the research funded as part of this program that are deemed to meet the standards for research publications in the field of study; and
the recipients will deposit all published manuscripts and juried conference papers in a public access-compliant repository in accordance with the guidelines set forth in NSF's Public Access Policy (see NSF Public Access Frequently Asked Questions at https://www.nsf.gov/publications/pub_summ.jsp?ods_key=nsf18041) no later than 12 months after initial publication.
he recipients do not need to dedicate to the public the right to any pre-existing background intellectual property relevant to the funded research or that is developed independently of or arising from activities not specifically conducted pursuant to the funded research described herein.

DOT/FHWA Award Administration and Conditions:

Proposals selected for funding by DOT will be awarded by NSF using funds transferred from DOT/FHWA, and will thus follow NSF's award conditions described above.

Independent of the NSF award, DOT/FHWA requires a minimum 20 percent funding match for the FHWA portion of funding. Additional information will be provided by FHWA to those selected projects, and the match will be reported to and managed by FHWA. This requirement will not be included as a condition of the NSF award.

C. Reporting Requirements
For all multi-year grants (including both standard and continuing grants), the Principal Investigator must submit an annual project report to the cognizant Program Officer no later than 90 days prior to the end of the current budget period. (Some programs or awards require submission of more frequent project reports). No later than 120 days following expiration of a grant, the PI also is required to submit a final annual project report, and a project outcomes report for the general public.

Failure to provide the required annual or final annual project reports, or the project outcomes report, will delay NSF review and processing of any future funding increments as well as any pending proposals for all identified PIs and co-PIs on a given award. PIs should examine the formats of the required reports in advance to assure availability of required data.

PIs are required to use NSF's electronic project-reporting system, available through Research.gov, for preparation and submission of annual and final annual project reports. Such reports provide information on accomplishments, project participants (individual and organizational), publications, and other specific products and impacts of the project. Submission of the report via Research.gov constitutes certification by the PI that the contents of the report are accurate and complete. The project outcomes report also must be prepared and submitted using Research.gov. This report serves as a brief summary, prepared specifically for the public, of the nature and outcomes of the project. This report will be posted on the NSF website exactly as it is submitted by the PI.

More comprehensive information on NSF Reporting Requirements and other important information on the administration of NSF awards is contained in the NSF Proposal & Award Policies & Procedures Guide (PAPPG) Chapter VII, available electronically on the NSF Website at https://www.nsf.gov/publications/pub_summ.jsp?ods_key=pappg.

NSF requires recipients to submit annual project reports and, at the completion of the award, a final annual project report. NSF will share these reports with the partners after they have been reviewed and accepted by the cognizant NSF Program Officer. The partner may opt to decline to receive these reports. Further, industry partners agree not to disclose any non-public information to any organization outside of the company.

VIII. Agency Contacts
Please note that the program contact information is current at the time of publishing. See program website for any updates to the points of contact.

General inquiries regarding this program should be made to:

James Joshi, TIP/ITE, telephone: (703) 292-8450, email: jjoshi@nsf.gov
Anna Squicciarini, CISE/CNS, telephone: (703) 292-5177, email: asquicci@nsf.gov
Xiaogang Wang, CISE/CNS, telephone: (703) 292-2812, email: xiawang@nsf.gov
Questions regarding this program can be emailed to, telephone: (please use email), email: TIP-PDaSP-Ask@nsf.gov

For questions related to the use of NSF systems contact:

NSF Help Desk: 1-800-381-1532
Research.gov Help Desk e-mail: rgov@nsf.gov
For questions relating to Grants.gov contact:

Grants.gov Contact Center: If the Authorized Organizational Representatives (AOR) has not received a confirmation message from Grants.gov within 48 hours of submission of application, please contact via telephone: 1-800-518-4726; e-mail: support@grants.gov.
IX. Other Information
The NSF website provides the most comprehensive source of information on NSF Directorates (including contact information), programs and funding opportunities. Use of this website by potential proposers is strongly encouraged. In addition, "NSF Update" is an information-delivery system designed to keep potential proposers and other interested parties apprised of new NSF funding opportunities and publications, important changes in proposal and award policies and procedures, and upcoming NSF Grants Conferences. Subscribers are informed through e-mail or the user's Web browser each time new publications are issued that match their identified interests. "NSF Update" also is available on NSF's website.

Grants.gov provides an additional electronic capability to search for Federal government-wide grant opportunities. NSF funding opportunities may be accessed via this mechanism. Further information on Grants.gov may be obtained at https://www.grants.gov.

About The National Science Foundation
The National Science Foundation (NSF) is an independent Federal agency created by the National Science Foundation Act of 1950, as amended (42 USC 1861-75). The Act states the purpose of the NSF is "to promote the progress of science; [and] to advance the national health, prosperity, and welfare by supporting research and education in all fields of science and engineering."

NSF funds research and education in most fields of science and engineering. It does this through grants and cooperative agreements to more than 2,000 colleges, universities, K-12 school systems, businesses, informal science organizations and other research organizations throughout the US. The Foundation accounts for about one-fourth of Federal support to academic institutions for basic research.

NSF receives approximately 55,000 proposals each year for research, education and training projects, of which approximately 11,000 are funded. In addition, the Foundation receives several thousand applications for graduate and postdoctoral fellowships. The agency operates no laboratories itself but does support National Research Centers, user facilities, certain oceanographic vessels and Arctic and Antarctic research stations. The Foundation also supports cooperative research between universities and industry, US participation in international scientific and engineering efforts, and educational activities at every academic level.

Facilitation Awards for Scientists and Engineers with Disabilities (FASED) provide funding for special assistance or equipment to enable persons with disabilities to work on NSF-supported projects. See the NSF Proposal & Award Policies & Procedures Guide Chapter II.F.7 for instructions regarding preparation of these types of proposals.

The National Science Foundation has Telephonic Device for the Deaf (TDD) and Federal Information Relay Service (FIRS) capabilities that enable individuals with hearing impairments to communicate with the Foundation about NSF programs, employment or general information. TDD may be accessed at (703) 292-5090 and (800) 281-8749, FIRS at (800) 877-8339.

The National Science Foundation Information Center may be reached at (703) 292-5111.

The National Science Foundation promotes and advances scientific progress in the United States by competitively awarding grants and cooperative agreements for research and education in the sciences, mathematics, and engineering.

To get the latest information about program deadlines, to download copies of NSF publications, and to access abstracts of awards, visit the NSF Website at https://www.nsf.gov

Location:
2415 Eisenhower Avenue, Alexandria, VA 22314

For General Information
(NSF Information Center):
(703) 292-5111

TDD (for the hearing-impaired):
(703) 292-5090

To Order Publications or Forms:
 
Send an e-mail to:

nsfpubs@nsf.gov

or telephone:

(703) 292-8134

To Locate NSF Employees:
(703) 292-5111

Privacy Act And Public Burden Statements
The information requested on proposal forms and project reports is solicited under the authority of the National Science Foundation Act of 1950, as amended. The information on proposal forms will be used in connection with the selection of qualified proposals; and project reports submitted by proposers will be used for program evaluation and reporting within the Executive Branch and to Congress. The information requested may be disclosed to qualified reviewers and staff assistants as part of the proposal review process; to proposer institutions/grantees to provide or obtain data regarding the proposal review process, award decisions, or the administration of awards; to government contractors, experts, volunteers and researchers and educators as necessary to complete assigned work; to other government agencies or other entities needing information regarding proposers or nominees as part of a joint application review process, or in order to coordinate programs or policy; and to another Federal agency, court, or party in a court or Federal administrative proceeding if the government is a party. Information about Principal Investigators may be added to the Reviewer file and used to select potential candidates to serve as peer reviewers or advisory committee members. See System of Record Notices, NSF-50, "Principal Investigator/Proposal File and Associated Records," and NSF-51, "Reviewer/Proposal File and Associated Records." Submission of the information is voluntary. Failure to provide full and complete information, however, may reduce the possibility of receiving an award.

An agency may not conduct or sponsor, and a person is not required to respond to, an information collection unless it displays a valid Office of Management and Budget (OMB) control number. The OMB control number for this collection is 3145-0058. Public reporting burden for this collection of information is estimated to average 120 hours per response, including the time for reviewing instructions. Send comments regarding the burden estimate and any other aspect of this collection of information, including suggestions for reducing this burden, to:

Suzanne H. Plimpton
Reports Clearance Officer
Policy Office, Division of Institution and Award Support
Office of Budget, Finance, and Award Management
National Science Foundation
Alexandria, VA 22314

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
        