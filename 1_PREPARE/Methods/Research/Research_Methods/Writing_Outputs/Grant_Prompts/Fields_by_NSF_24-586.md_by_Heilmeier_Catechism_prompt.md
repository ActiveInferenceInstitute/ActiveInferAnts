
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
        
• What are you trying to do? Articulate your objectives using absolutely no jargon.
• How is it done today, and what are the limits of current practice?
• What is new in your approach and why do you think it will be successful?
• Who cares? If you are successful, what difference will it make?
• What are the risks?
• How much will it cost?
• How long will it take?
• What are the mid-term and final "exams" to check for success?

        Grant Call (Agency Requirements):
        NSF 24-586: NSF National Quantum Virtual Laboratory - Quantum Testbeds (NQVL)
Quantum Science and Technology Demonstrations (QSTD): II. Design & Implementation
Program Solicitation
Document Information
Document History
Posted: June 27, 2024
Download the solicitation (PDF, 0.9mb)
View the program page
NSF Logo		
National Science Foundation
Directorate for Biological Sciences
Directorate for Computer and Information Science and Engineering
Directorate for STEM Education
Directorate for Engineering
Directorate for Mathematical and Physical Sciences
Directorate for Technology, Innovation and Partnerships

Full Proposal Target Date(s):

     April 01, 2025

NQVL:QSTD:Design

     April 07, 2026

NQVL:QSTD:Design

     April 07, 2026

NQVL:QSTD:Implementation

     April 06, 2027

NQVL:QSTD:Design

     April 06, 2027

NQVL:QSTD:Implementation

     April 04, 2028

NQVL:QSTD:Implementation

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
With this solicitation the Foundation is taking the next step in implementing the National Quantum Virtual Laboratory (NQVL) program by providing information regarding the QSTD:Design and QSTD:Implementation proposal submission and review process, thus completing the implementation of the Quantum Science and Technology Demonstration (QSTD) component of the NQVL program that started with the QSTD:Pilot phase introduced in the NSF 23-604 solicitation.

Any proposal submitted in response to this solicitation should be submitted in accordance with the NSF Proposal & Award Policies & Procedures Guide (PAPPG) that is in effect for the relevant due date to which the proposal is being submitted. The NSF PAPPG is regularly revised and it is the responsibility of the proposer to ensure that the proposal meets the requirements specified in this solicitation and the applicable version of the PAPPG. Submitting a proposal prior to a specified deadline does not negate this requirement.

Summary Of Program Requirements
General Information
Program Title:

NSF National Quantum Virtual Laboratory - Quantum Testbeds (NQVL)
Quantum Science and Technology Demonstrations (QSTD): II. Design & Implementation

Synopsis of Program:

The National Quantum Initiative (NQI) Act1 aims to ensure the continuing leadership of the United States (U.S.) in quantum information science and technology. In conformance with the NQI goals, an argument2, 3, 4, 5 was set forth for a renewed emphasis on identifying and fostering early adoption of quantum technologies to transform the field of Quantum Information Science and Engineering (QISE) and to accelerate broader impacts on society. A systematic approach to maturing quantum technology platforms by integrating end-users and potential customers from other fields of science and engineering and other sectors of the economy into cycles of research, development, and demonstration should lower the barriers for end-users to pioneer new applications. NSF support for use-inspired and translational research in QISE, combined with continued strong support of the underlying foundational research, is anticipated to accelerate development of a market for quantum technologies.

With this program solicitation, the Foundation is taking the next step in implementing the National Quantum Virtual Laboratory (NQVL) concept as an overarching shared infrastructure designed to facilitate the translation from basic science and engineering to the resultant technology, while at the same time emphasizing and advancing its scientific and technical value. The NQVL aims to develop and utilize use-inspired and application-oriented quantum technologies. In the process, NQVL researchers will explore quantum frontiers6, foster the development of QISE education and workforce development strategies, engage in outreach activities at all levels, and promote input and participation from the full spectrum of diverse talent in QISE, thereby lowering barriers at all entry points of the research enterprise. Engagement with all sectors of the United States (U.S.) QISE community will be necessary for this initiative to succeed, and, indeed, the project is designed to include participation from a full spectrum of organizations who have expertise to contribute. In particular, NSF recognizes that the involvement of industry partners is essential and will welcome these to be a part of the overall structure. Partnerships with other U.S. Federal agencies under the NQI umbrella are also encouraged.

While this solicitation lays out the vision for the entire NQVL program that includes Quantum Science and Technology Demonstration (QSTD) projects, support for enabling technologies through Transformative Advances in Quantum Systems (TAQS), as well as a central coordination hub, only proposals for Design- and Implementation-phase QSTDs are solicited at this time.

Submission of a QSTD:Design proposal is contingent upon the existence of a QSTD:Pilot project in the same topical area, and the positive recommendation from the Conceptual Design Review of the QSTD:Pilot project. The QSTD:Design project builds on progress made in the QSTD:Pilot phase.

Submission of a QSTD:Implementation proposal is contingent upon the existence of a QSTD:Design project in the same topical area, and the positive recommendation from the Preliminary Design Review of the QSTD:Design project. The QSTD:Implementation project builds on progress made in the QSTD:Design phase.

It is required that prospective PIs contact the NQVL Program Officer(s) as soon as possible, but not later than two weeks before submitting a proposal in response to this solicitation, to ascertain that the focus and budget of their proposal is appropriate for this solicitation.

1 H.R.6227 - National Quantum Initiative Act, https://www.congress.gov/bill/115th-congress/house-bill/6227

2 Accelerating Progress Towards Practical Quantum Advantage, A National Science Foundation Project Scoping Workshop (2022), https://arxiv.org/abs/2210.14757

3 Quantum Computer Systems for Scientific Discovery, PRX Quantum 2, 017001 (2021) https://doi.org/10.1103/PRXQuantum.2.017001

4 Development of Quantum InterConnects for Next-Generation Information Technologies, PRX Quantum 2, 017002 (2021) https://doi.org/10.1103/PRXQuantum.2.017002

5 Quantum Simulators: Architectures and Opportunities, PRX Quantum 2, 017003 (2021) https://doi.org/10.1103/PRXQuantum.2.017003

6 Quantum Frontiers: Report on Community Input to the Nation's Strategy for Quantum Information Science, https://www.quantum.gov/wp-content/uploads/2020/10/QuantumFrontiers.pdf

Cognizant Program Officer(s):

Please note that the following information is current at the time of publishing. See program website for any updates to the points of contact.

National Quantum Virtual Laboratory, telephone: (703) 292-8235, email: NQVL@nsf.gov
Bogdan Mihaila, MPS/PHY, telephone: (703) 292-8235, email: bmihaila@nsf.gov
Elizabeth Behrman, CISE/CCF, telephone: (703) 292-7049, email: ebehrman@nsf.gov
Almadena Y. Chtchelkanova, CISE/CCF, telephone: (703) 292-8910, email: achtchel@nsf.gov
Dominique M. Dagenais, ENG/ECCS, telephone: (703) 292-2980, email: ddagenai@nsf.gov
David Darwin, TIP/ITE, telephone: (703) 292-4728, email: ddarwin@nsf.gov
Pradeep P. Fulay, TIP/ITE, telephone: (703) 292-2445, email: pfulay@nsf.gov
Wu He, EDU/DRL, telephone: (703) 292-7593, email: wuhe@nsf.gov
Andrey Kanaev, CISE/OAC, telephone: (703) 292-2841, email: akanaev@nsf.gov
Matthew McCune, ENG/ECCS, telephone: (703) 292-2906, email: mamccune@nsf.gov
Engin Serpersu, BIO/MCB, telephone: (703) 292-7124, email: eserpers@nsf.gov
Applicable Catalog of Federal Domestic Assistance (CFDA) Number(s):

47.041 --- Engineering
47.049 --- Mathematical and Physical Sciences
47.070 --- Computer and Information Science and Engineering
47.074 --- Biological Sciences
47.076 --- STEM Education
47.084 --- NSF Technology, Innovation and Partnerships
Award Information
Anticipated Type of Award: Cooperative Agreement

Estimated Number of Awards: 14

The number of awards for each QSTD phase will be determined by separate review processes and will be based on quality of proposals, responsiveness to priorities of the NQVL program, and the availability of funds appropriated by Congress.

It is estimated that up to eight (8) QSTD Design awards will be granted in total over three competition rounds. It is estimated that up to six (6) QSTD Implementation awards will be granted in total over three competition rounds.

Anticipated Funding Amount: $32,000,000

This solicitation pertains to the Design and Implementation development phases of the QSTD projects part of the NQVL program. QSTD:Design awards may be funded at a level up to $2,000,000 per year for up to two years. QSTD:Implementation awards may be funded at a level up to $10,000,000 per year for six years.

NSF will support the Design phase of the NQVL:QSTD projects with a total budget of up to $32,000,000. Funding for the Implementation Phase will depend on progress made by the NQVL:QSTD teams and the availability of funds appropriated by Congress.

Estimated program budget, number of awards and average award size/duration are subject to the quality of the proposals and the availability of funds appropriated by Congress.

Eligibility Information
Who May Submit Proposals:

Proposals may only be submitted by the following:

The complete process for determining eligibility to submit to the Design and Implementation Phases is described in Section II, Program Description.

NQVL:QSTD:Design
Submission of a QSTD:Design proposal is contingent upon the existence of a QSTD:Pilot project in the same topical area, and the positive recommendation from the site visit panel that will review the QSTD:Pilot project nine-months into the QSTD:Pilot project. Transitioning from the QSTD:Pilot to the QSTD:Design phase, the Lead Organization and the Lead PI may change subject to the eligibility limits on number of proposals per organization and per PI or co-PI stated in this solicitation.

Following upon a clear and agreed-upon understanding of goals and objectives, the selection of a Lead Organization, and approval by the NSF to advance from the Pilot to the Design phase, QSTD:Pilot teams may choose to consolidate prior to submitting a QSTD:Design proposal to advance to the Design phase. There are no restrictions or limitations on the type of organization eligible to serve as Lead Organization on the proposal.

NQVL:QSTD:Implementation
Submission of a QSTD:Implementation proposal is contingent upon the existence of a QSTD:Design project in the same topical area, and the positive recommendation from the last annual site visit panel review of the QSTD:Design project. Transitioning from the QSTD:Design to the QSTD:Implementation phase, the Lead Organization and the Lead PI may change subject to the eligibility limits on number of proposals per organization and per PI or co-PI stated in this solicitation.

Following upon a clear and agreed-upon understanding of goals and objectives, the selection of a Lead Organization, and approval by the NSF to advance from the Design to the Implementation phase, QSTD:Design teams may choose to consolidate prior to submitting a QSTD:Implementation proposal to advance to the Implementation phase. There are no restrictions or limitations on the type of organization eligible to serve as Lead Organization on the proposal.

Who May Serve as PI:

There are no restrictions or limits.

Limit on Number of Proposals per Organization: 1

Up to one (1) QSTD Design or Implementation proposal may be submitted per Lead Organization.

Limit on Number of Proposals per PI or co-PI: 1

An individual may serve as PI or co-PI on no more than one (1) QSTD Design or Implementation proposal.

Proposal Preparation and Submission Instructions
A. Proposal Preparation Instructions

Letters of Intent: Not required
Preliminary Proposal Submission: Not required
Full Proposals:
Full Proposals submitted via Research.gov: NSF Proposal and Award Policies and Procedures Guide (PAPPG) guidelines apply. The complete text of the PAPPG is available electronically on the NSF website at: https://www.nsf.gov/publications/pub_summ.jsp?ods_key=pappg.
Full Proposals submitted via Grants.gov: NSF Grants.gov Application Guide: A Guide for the Preparation and Submission of NSF Applications via Grants.gov guidelines apply (Note: The NSF Grants.gov Application Guide is available on the Grants.gov website and on the NSF website at: https://www.nsf.gov/publications/pub_summ.jsp?ods_key=grantsgovguide).
B. Budgetary Information

Cost Sharing Requirements:
Inclusion of voluntary committed cost sharing is prohibited.

Indirect Cost (F&A) Limitations:
Not Applicable

Other Budgetary Limitations:
Not Applicable

C. Due Dates

Full Proposal Target Date(s):
     April 01, 2025

NQVL:QSTD:Design

     April 07, 2026

NQVL:QSTD:Design

     April 07, 2026

NQVL:QSTD:Implementation

     April 06, 2027

NQVL:QSTD:Design

     April 06, 2027

NQVL:QSTD:Implementation

     April 04, 2028

NQVL:QSTD:Implementation

Proposal Review Information Criteria
Merit Review Criteria:

National Science Board approved criteria. Additional merit review criteria apply. Please see the full text of this solicitation for further information.

Award Administration Information
Award Conditions:

Standard NSF award conditions apply.

Reporting Requirements:

Standard NSF reporting requirements apply.

I. Introduction
The translation from basic knowledge to new, scalable technologies that can provide solutions to real-world problems is a multi-step process that requires prototyping, validation, at-scale testing, and eventual full-scale demonstration. As an approach to achieving this goal for quantum-related technologies, NSF has instituted the National Quantum Virtual Laboratory (NQVL) concept. The overarching goal of the NQVL is the demonstration of practical quantum advantage, the actual application of the tools of Quantum Information Science and Engineering (QISE) to problems that will enable solutions that classical approaches can only solve much less efficiently or not at all.

The NQVL vision is to support a highly accessible shared research infrastructure framework that draws on the full spectrum of expertise throughout the Nation to rapidly translate QISE ideas formulated in the laboratory through prototyping, validation, at-scale testing, and eventual full-scale deployment. A co-design approach will facilitate the quick transfer of discoveries from one phase to the next, enable the rapid identification of gaps, and draw on the talent necessary to close these gaps. A key focus of the program will be to develop education and workforce development strategies that promote input and participation from the full spectrum of diverse talent in QISE by expanding access to state-of-the-art resources and prototypes to all parts of the U.S. research ecosystem. While the completed NQVL will consist of a set of primary nodes defined by the major Quantum Science and Technology Demonstration projects defined below, the overall structure is designed to serve as a resource for the community at large, facilitating the flow of talent and ideas through a central coordination body.

The successful translation of QISE research under the NQVL will require the integration of several layers, from fundamental principles to prototypes to applications, utilizing a convergent, systems engineering, and co-design approach. The co-design of enabling technologies (e.g., reliable materials fabrication, scalable device manufacturing, dependable quantum interconnects, or robust software stack) and sufficiently mature physical platforms will result in Quantum Science and Technology Demonstrations (QSTD) for scientific discovery that will be made available for use by the broad scientific community. Users will identify applications that can be co-designed with a rapid cycle of system upgrades, resulting in the transition of ideas that are still in the early conceptual stages into prototypes that are in level of readiness that they can be handed off to the private sector.

The NQVL is envisioned as having three components, though only the Design and Implementation phases of the first component below are the focus of this solicitation:

NQVL:QSTD – Quantum Science and Technology Demonstration projects. These projects will make up the scientific and engineering core of the activities that combine to form a federated NQVL infrastructure and are expected to pass through three phases: Pilot, Design, and Implementation. Given the project nature of the NQVL:QSTD activity it is expected that the participants will proceed through all three project development phases as listed in the eligibility requirements.
Each NQVL:QSTD project is expected to define a quantum advantage goal and a projected pathway for achieving that goal. It is expected that this pathway will have a focus on the design and integration of quantum systems co-designed with applications developed by the full spectrum of diverse talent of the user community. Through this process of systems design and prototyping, the project will connect the underlying basic scientific knowledge to an application that is identified by this end-user community and fostered by direct interactions between these users, the systems engineers, and the basic science developers. Those activities will be complemented by appropriately scaled education and workforce development plans for training diverse talent in the quantum workforce.

NQVL:TAQS – NSF aims to provide resources to support research and development of enabling technologies identified by the NQVL:QSTD projects as they mature through the various phases. NSF envisions doing this through the mechanism of the Transformative Advances in Quantum Systems (TAQS) program as an independent funding opportunity that will address critical needs of the NQVL infrastructure as well as contribute to expanding the access to the Laboratory to a wider community.
NQVL:Central – NQVL Planning and Coordination. NSF anticipates support for one NQVL Central Hub that will perform three distinct functions: i) promote collaboration and networking between the NQVL project teams; ii) promote engagement with the broad QISE community, partnerships with others and outreach activities to the general public; and iii) facilitate community oversight and the development of success metrics and benchmarks. The first function will enable the identification and potential exchange of component parts among the teams, especially in the Implementation phase. The other two functions recognize the need for greater accountability to the wider QISE community and to the public.
As such, NQVL:Central will be called upon to serve as the intellectual hub for the growing QISE academic community. The NQVL Central Hub will also facilitate connections between the units of the NQVL and the activities of other agencies as well as establish mechanisms for industrial participation in the QSTD goals. The NQVL Central Hub will connect with the Quantum Economic Development Consortium (QED-C) and professional societies whose membership includes existing and potential practitioners in QISE. The NQVL Central Hub will host workshops and scientific programs that foster connections and dissemination throughout the QISE community. Lastly, the NQVL Central Hub will be asked to develop and maintain a Strategic Plan for NQVL investments, a living community document designed to keep abreast with evolving trends in the field, progress toward community goals, management and coordination, and implementation of new directions.

The development of the NQVL is expected to take place over several years. The present solicitation concerns only the Design and Implementation phases of the QSTD project components of the NQVL. Separate solicitations will be issued for the other components of NQVL, depending on the progress in the QSTD phases. At every QSTD project development phase, it is critical to keep in mind the full project development as described below while formulating plans, especially as many of the general requirements will apply to each phase. Support for the QSTD-enabling technology development part of the NQVL program will be on an as-needed basis as the subject of future NSF funding opportunities.

The NQVL program is intended as a national, community-driven effort that supports the smooth integration and translation from fundamental science and engineering to use-inspired applications. Building on the continued and sustained support of fundamental research from existing NSF programs, the NQVL will draw together expertise and talent from a broad range of disciplines to enable the creation and application of functional quantum devices and systems. Coordination will be provided through a federated infrastructure that serves much like a laboratory, but without the physical co-location of all assets and infrastructure, to identify roles and resource needs and establish mechanisms to enable all members of this virtual laboratory to communicate and function together as one coordinated unit. The federated NQVL structure, which will be developed and led by the community, should enable anyone to become engaged and contribute to advances in QISE.

II. Program Description
Note: The full NQVL program is being implemented in multiple iterations, each with its own solicitation. The present solicitation applies only to the Design and Implementation phases of the Quantum Science and Technology Demonstration (QSTD) component. The full scope across all three phases of this component is outlined here to help prospective proposers decide on the scale and scope of their proposals to this solicitation within the context of anticipated future goals for the entire program.

The Quantum Science and Technology Demonstration (QSTD) projects form the scientific and technological core efforts the NQVL is designed to enable. Each QSTD project will have identified a technology goal that has the potential for demonstrating quantum advantage that could lead to translation in the near term. Each project will also have identified a potential pathway for achieving this goal, including the basic science from which the pathway derives, the participants and skill-sets critical for the success of the project, and the user community that will derive the benefit. The phase-wise development that is planned for each project recognizes that this is a fluid process. Plans proposed at the beginning will have to be modified as detailed design and then implementation proceeds. Challenges are to be expected and must be addressed in the time allowed. Additional members with special expertise may need to be included to address these gaps. Feedback from potential users may suggest modifications necessary to deliver a useful end product. And systems engineering steps along the way may dictate changes and/or suggest improvements that speed up the process. The NQVL infrastructure provides the framework through which these changes can be implemented smoothly and quickly. In addition, the NQVL infrastructure will foster essential collaboration, coordination, and cooperation between the various QSTD projects, which might have a different technology focus. This will help identify gaps that apply to more than just a single project, thus magnifying the impact of developments along the way. Activities in areas of common interest or capabilities that benefit more than one QSTD project may be supported separately to maximize synergies and optimize resource allocations. It is also possible that these supporting developments could in turn lead to their own applications independently of the quantum advantage goal. Support for the acquisition or development and implementation of research infrastructure may also be included. The QSTD projects will also develop effective strategies for education and workforce development.

The QSTD projects fall into the category of long-duration NSF investments that require substantial funding over multiple award cycles. They are expected to be developed in three phases: Pilot, Design, and Implementation. Each phase will evolve into the next as the projects are refined and increasingly focused on prototype development and future translation.

1. The Pilot phase is focused on the development of the conceptual design of the QSTD project. Completion of the Pilot phase is required for submission to the Design and Implementation phases. By the conclusion of the Pilot phase, the team will be expected to have completed the following:

Refine the science questions;
Define requirements and prioritize research objectives;
Identify enabling technologies and risks;
Identify critical partnerships and dependencies;
Develop top-down cost and contingency estimates;
Formulate initial risk assessment;
Draft initial Project Execution Plan; and
Draft initial Education and Workforce Development Plan.
Conceptual Design Review: Nine (9) months into the project, NSF will conduct a site visit panel review of each Pilot project. The purpose of the review would be to assess the progress made by the team, provide feedback, and evaluate the readiness of the team to advance to the Design phase of the QSTD development process.

The Pilot phase is complete when a package containing the QSTD Conceptual Design and the QISE Strategic Plan on the QSTD topic, together with the draft Project Execution Plan and Education and Workforce Development plan leading to a QSTD Preliminary Design, is received and reviewed by NSF.

2. The Design phase is focused on the preliminary design development of the QSTD project.

The NQVL program recommendation for advancement from the Pilot to the Design phase is required for a proposal submission to the QSTD:Design phase.

A successful Design proposal will incorporate the QSTD preliminary project design, demonstrate technical readiness, and include planning for the total anticipated QSTD project lifetime. Design proposals must also include an appropriately scaled Project Execution Plan (PEP) describing how the project will be managed, the scope of work in a Work Breakdown Structure (WBS) format along with a WBS dictionary, the budget estimate and basis of estimate for each WBS element, and the risk or uncertainty in the budget estimate accompanied by the methodology for risk and budget contingency estimation. A resource-loaded schedule may also be required to support the proposed QSTD system integration funding profile. Projection of implementation costs should be revisited in an updated plan for the implementation component of the QSTD project. The Design phase may take up to two years at a cost of up to $2,000,000 per year.

Specifically, the team will:

Develop enabling technology;
Update risk analysis, develop risk mitigation strategies;
Develop bottom-up cost and contingency estimates;
Develop preliminary operations cost;
Develop Project Management Control System;
Develop preliminary Project Execution Plan;
Develop preliminary Education and Workforce Development Plan; and
Identify key staff.
NSF requires that each Design team includes a professional Project Manager as part of the project leadership.

Preliminary Design Review: Nine (9) months into the project, NSF will conduct a site visit panel review of each Design project. The purpose of the review will be to assess the progress made by the team, provide feedback, and evaluate the readiness of the team to advance to the Implementation phase of the QSTD development process. The site visit will focus on the technical and project management review of the Design project.

The Design project is eligible for a second year of NSF support. Therefore, a second site visit panel review may be conducted twelve (12) months later.

The Design phase is complete when a package containing the QSTD Preliminary Design, together with the draft Project Execution Plan, Education and Workforce Development plan, and funding request leading to a QSTD Final Design, is received and reviewed by NSF.

3. The Implementation phase includes the final design of the first-generation QSTD system, followed by the system integration and subsequent operations of this initial prototype, while at the same time pursuing the development of the enabling technology for the next-generation QSTD system.

The NQVL program recommendation for advancement from the Design to the Implementation phase is required for a proposal submission to the QSTD:Implementation phase.

The Implementation phase includes two components: first-generation design completion, assembly, and operations (Gen-1) and next-generation technology development (Gen-n). The Gen-1 component will proceed in two stages, locking in the final design (Final Design stage), followed by developing the first prototype and assembling and enabling the first users, or operations (Operations stage). It is expected that the subsequent Gen-n phase will proceed simultaneously with the Operations stage as the developers build off the experience gained with actual use, as envisioned in the co-design approach.

For the Final Design stage, the QSTD proposal demonstrates that the enabling research and technology development for the first-generation QSTD system integration project is completed, and that bid packages for major contracts or acquisitions have been completed. The QSTD system integration budget estimate for the first-generation QSTD is refined so that it is based substantially on externally provided information rather than internal engineering estimates (vendor quotes, budgetary estimates, etc.) Key staff members needed to manage project activities are recruited and ready to commence system integration. Commitments from external partners in the activity are confirmed. The largest and most complex projects are encouraged to use appropriately scaled Earned Value Management reporting during system integration and should prepare an Earned Value Management System during this phase in readiness for system integration.

During the Final Design stage, with a duration of two years, the team will:

Harden key technologies;
Refine bottom-up cost and contingency estimates;
Finalize risk assessment and mitigation plan;
Finalize Project Management plan;
Develop Project Execution Plan (PEP);
Finalize Education and Workforce Development Plan (E&WDP); and
Complete recruitment of key staff.
During the Final Design stage, the team may have Monthly Oversight meetings with NSF program staff. The team may be required to submit Intermediate Reports monthly via Research.gov.

Final Design Review: NSF will conduct a site visit panel review of each Implementation project eighteen (18) months into the award period. The purpose of the review would be to assess the progress made by the team, provide feedback, and evaluate the readiness of the team to advance to the Operations stage of the QSTD Implementation phase.

The NQVL program recommendation is required for advancement from the Final Design stage to the Operations stage of the QSTD:Implementation phase.

During the Operations stage, the team activities will focus on:

System integration, testing, commissioning of the QSTD;
Operations and user support once a QSTD system is accepted by NSF; and
Development of the technology needed for and design for the next-generation QSTD.
During all activities in the Implementation phase, the team may have Monthly Oversight meetings with NSF program staff. The team will be required to submit Intermediate Reports quarterly via Research.gov.

NSF may conduct annual site visit panel reviews of each QSTD:Implementation project in the Operations stage. The purpose of the review would be to assess the progress made by the team and provide feedback.

QSTD awards for projects in the Implementation phase will be in the form of cooperative agreements that contain terms and conditions specific to the nature and risks associated with the project.

Each phase of the QSTD projects will follow on the previous phase and constitutes the next step in the refinement of the project. At each phase proposals will be invited only from those teams, or combinations thereof, who have participated in the previous phase. The Implementation phase can be expected to last for six years, with a possibility of one renewal, at a cost between $7,000,000 and $10,000,000 per year.

The following language applies to the technical review of all phases of all QSTD projects:

Scientific Review
Proposals are considered first based on their science goals and their potential of translation from laboratory to practice. Given the significant resources required to execute a QSTD project and the fact that a QSTD project will extend for more than a single award cycle, the scientific goals and the specific outcomes must be compelling and clearly articulated in the proposal. NSF proposal review panels will conduct a comparative review of all proposals submitted to the NQVL program in a given fiscal year. The review panels may be asked to consider the programmatic balance of investments across the full NQVL program.

Technical and Project Management Review
The feasibility of the proposed activities will be reviewed thoroughly. Given the scale and complexity of most large NSF investments a separate panel may assess the implementation plans outlined in the proposal. As QSTD proposals will likely include acquisition, technology development or fabrication activities, the proposal review may consider technical readiness, risk mitigation, project management plans, budgets, and schedules. For long-duration projects with a lifetime possibly exceeding a single award period, contingent on selection in a subsequent development phase, the technical review may also consider performance schedules and the planning for the total anticipated number of system integration and development cycles in the QSTD project, including possible operations. For renewal proposals, the record of success in achieving any previous set of milestones will be taken into consideration. As needed, these reviews may involve site visits. In all cases, the technical review panel will be asked to consider and provide guidance to the Program on the appropriate duration of the award and milestones needed to evaluate progress.

Education and Workforce Development Plan Review
The NQVL program seeks to identify and promote effective education and workforce development strategies that promote input and participation from the full spectrum of diverse talent in QISE thereby lowering barriers at all entry points of the research enterprise. All three phases of the QSTD project development process, i.e. the Conceptual, Preliminary, and the Final Designs of the QSTD project, are required to include appropriately scaled education and workforce development plans for training diverse talent in the workforce in QISE. Examples of activities as part of the Education and Workforce Development Plan (E&WDP) may include, but are not limited to: i) QISE-centric curricula (K through Graduate level); ii) opportunities for students to interact with industry partners, for example through collaboration on research projects, internships, fellowships or entrepreneurial activities; iii) effective and evidence based educational approaches leading to development of skilled and diverse talent in the QISE workforce through formal and informal education; or iv) up-skilling and re-skilling working professionals. A dedicated E&WDP review will be conducted at each stage of the QSTD project development process. The E&WDP implementation will be reviewed annually once the QSTD:Implementation project reaches the Operations stage. The Education and Workforce Development Plan is intended as a living document that will be updated as needed.

Award Oversight
QSTD awards beyond the Pilot phase will be made through cooperative agreements that contain terms and conditions specific to the nature and risks associated with the project. These may involve site visits or mid-term reviews, and NSF approval of changes in management or schedule. Oversight will include monitoring progress towards any milestones established during the technical review. The duration of support will be determined based on the scientific goals of the project with input from the technical review and will consider the financial burden on the NQVL program. Proposals for continued support may involve both scientific and technical review, as appropriate at the time of the proposal submission. Appropriate close-out should be planned. For the largest investments a close-out phase may be described in the cooperative agreement.

General Review Criteria

All QSTD proposals will be evaluated using the NSF merit review criteria concerning intellectual merit and broader impacts, as well as an assessment as to how well the proposed QSTD project will address the stated science goals and QSTD impacts. Consideration of all QSTD projects begins by evaluating and prioritizing the science goals within the NQVL, and by determining the feasibility of the implementation plan. For each of the relevant phases – Pilot, Design, and Implementation – the associated deliverables from the previous phase will be reviewed before advancing on to the next phase. At each phase of development, the NSF may choose to provide support through the next phase or end its involvement. At successive development phases, the reviews will be increasingly more detailed and will involve an increasing level of commitment from the NSF. Project planning must take into account the total project lifetime. The NSF investment in any one QSTD project is of finite duration.

NSF has as one of its over-arching principles the fostering of diverse talent across the scientific community. All QSTD proposals submitted through any of the solicitations issued as part of the NQVL program will be required to identify steps that will be taken to promote this goal and can expect to be reviewed as to how well this is being addressed.

Review of the QSTD proposal and subsequent oversight of QSTP awards will scale with the size and complexity of the proposed project as described in the 2021 Research Infrastructure Guide (RIG) NSF 21-107, or subsequent revisions in effect at time of proposal submission found at: https://www.nsf.gov/bfa/lfo/lfo_documents.jsp. Prospective PIs are strongly encouraged to familiarize with Chapter 5 of the Research Infrastructure Guide (RIG) for guidance on planning and oversight requirements relevant to QSTD projects. The guidelines listed here follow standard practices for activities of this scope.

The Design and Implementation phases of a QSTD project will be conducted in the following sequence:

Design phase: NSF aims to support up to eight (8) Design projects with a duration of up to two years, at the level of up to $2,000,000 per year. The number of awards will depend on the quality of the proposals and the availability of funds appropriated by Congress.

Submission of a QSTD:Design proposal is contingent upon the existence of a QSTD:Pilot project in the same topical area, and the positive recommendation from the Conceptual Design Review of the QSTD:Pilot project. Advancing from the QSTD:Pilot to the QSTD:Design phase, the Lead Organization and the Lead PI may change subject to the eligibility limits on number of proposals per organization and per PI or co-PI stated in this solicitation.

The QSTD Pilot teams are expected to collaborate, coordinate, and cooperate with each other and synergies are strongly encouraged. Following upon a clear and agreed-upon understanding of goals and objectives, the selection of a Lead Organization, and approval by the NSF to advance from the Pilot to the Design phase, QSTD Pilot teams may choose to consolidate prior to submitting a QSTD Design proposal to advance to the Design phase.

Implementation phase: NSF aims to support up to six (6) Implementation projects with a duration of six years. The level of NSF support for QSTD Implementation projects will scale with the complexity of the QSTD project but is expected to range between $7,000,000 to $10,000,000 per project per year. The number of awards will depend on the quality of the proposals and the availability of funds appropriated by Congress. The QSTD Implementation projects are eligible for a one-time six-year renewal, contingent upon the quality of a new proposal and the availability of funds appropriated by Congress.

Submission of a QSTD:Implementation proposal is contingent upon the existence of a QSTD:Design project in the same topical area, and the positive recommendation from the Preliminary Design Review of the QSTD:Design project. Advancing from the QSTD:Design to the QSTD:Implementation phase, the Lead Organization and the Lead PI may change subject to the eligibility limits on number of proposals per organization and per PI or co-PI stated in this solicitation.

The QSTD Design teams are expected to collaborate, coordinate, and cooperate with each other and synergies are strongly encouraged. Following upon a clear and agreed-upon understanding of goals and objectives, the selection of a Lead Organization, and approval by the NSF to advance from the Design to the Implementation phase, QSTD Design teams may choose to consolidate prior to submitting a QSTD Implementation proposal to advance to the Implementation phase.

NSF requires that the leadership of each Implementation team separates roles and responsibilities with respect to the scientific and project management components of the QSTD project. The Project Manager will be solely in charge of delivering each QSTD generation on time and on budget.

Each QSTD Implementation team will maintain the QISE Strategic Plans on the specific topic of the QSTD project. QISE community town hall meetings may be convened at annual intervals. Specific details may be project dependent and will be captured in the QSTD Community Outreach plan with the overarching goal of fostering an open scientific dialogue and ensuring the broad participation of the entire QISE community.

As indicated above, the QSTD Implementation teams are expected to collaborate, coordinate, and cooperate with each other. Synergies are strongly encouraged.

III. Award Information
Anticipated Type of Award: Cooperative Agreement

Estimated Number of Awards: 14

It is estimated that up to eight (8) QSTD Design awards will be granted in total over three competition rounds. It is estimated that up to six (6) QSTD Implementation awards will be granted in total over three competition rounds. The number of awards will depend on the quality of the proposals and the availability of funds appropriated by Congress.

Anticipated Funding Amount: $32,000,000

This solicitation pertains to the Design and Implementation development phases of the QSTD projects part of the NQVL program. QSTD:Design awards may be funded at a level up to $2,000,000 per year for up to two years. QSTD:Implementation awards may be funded at a level up to $10,000,000 per year for six years.

NSF will support the Design phase of the NQVL:QSTD projects with a total budget of up to $32,000,000. Funding for the Implementation Phase will depend on progress made by the NQVL:QSTD teams and the availability of funds appropriated by Congress.

Estimated program budget, number of awards and average award size/duration are subject to the quality of the proposals and the availability of funds appropriated by Congress.

IV. Eligibility Information
Who May Submit Proposals:

Proposals may only be submitted by the following:

The complete process for determining eligibility to submit to the Design and Implementation Phases is described in Section II, Program Description.
NQVL:QSTD:Design

Submission of a QSTD:Design proposal is contingent upon the existence of a QSTD:Pilot project in the same topical area, and the positive recommendation from the site visit panel that will review the QSTD:Pilot project nine-months into the QSTD:Pilot project. Transitioning from the QSTD:Pilot to the QSTD:Design phase, the Lead Organization and the Lead PI may change subject to the eligibility limits on number of proposals per organization and per PI or co-PI stated in this solicitation.

Following upon a clear and agreed-upon understanding of goals and objectives, the selection of a Lead Organization, and approval by the NSF to advance from the Pilot to the Design phase, QSTD:Pilot teams may choose to consolidate prior to submitting a QSTD:Design proposal to advance to the Design phase. There are no restrictions or limitations on the type of organization eligible to serve as Lead Organization on the proposal.

NQVL:QSTD:Implementation

Submission of a QSTD:Implementation proposal is contingent upon the existence of a QSTD:Design project in the same topical area, and the positive recommendation from the last annual site visit panel review of the QSTD:Design project. Transitioning from the QSTD:Design to the QSTD:Implementation phase, the Lead Organization and the Lead PI may change subject to the eligibility limits on number of proposals per organization and per PI or co-PI stated in this solicitation.

Following upon a clear and agreed-upon understanding of goals and objectives, the selection of a Lead Organization, and approval by the NSF to advance from the Design to the Implementation phase, QSTD:Design teams may choose to consolidate prior to submitting a QSTD:Implementation proposal to advance to the Implementation phase. There are no restrictions or limitations on the type of organization eligible to serve as Lead Organization on the proposal.

Who May Serve as PI:

There are no restrictions or limits.

Limit on Number of Proposals per Organization: 1

Up to one (1) QSTD Design or Implementation proposal may be submitted per Lead Organization.

Limit on Number of Proposals per PI or co-PI: 1

An individual may serve as PI or co-PI on no more than one (1) QSTD Design or Implementation proposal.

Additional Eligibility Info:

Organization Limit: Although an NQVL:QSTD project is expected to be multi-organizational, a single organization must serve as the lead and all other organizations as subawardees.

V. Proposal Preparation And Submission Instructions
A. Proposal Preparation Instructions
Full Proposal Preparation Instructions: Proposers may opt to submit proposals in response to this Program Solicitation via Research.gov or Grants.gov.

Full Proposals submitted via Research.gov: Proposals submitted in response to this program solicitation should be prepared and submitted in accordance with the general guidelines contained in the NSF Proposal and Award Policies and Procedures Guide (PAPPG). The complete text of the PAPPG is available electronically on the NSF website at: https://www.nsf.gov/publications/pub_summ.jsp?ods_key=pappg. Paper copies of the PAPPG may be obtained from the NSF Publications Clearinghouse, telephone (703) 292-8134 or by e-mail from nsfpubs@nsf.gov. The Prepare New Proposal setup will prompt you for the program solicitation number.
Full proposals submitted via Grants.gov: Proposals submitted in response to this program solicitation via Grants.gov should be prepared and submitted in accordance with the NSF Grants.gov Application Guide: A Guide for the Preparation and Submission of NSF Applications via Grants.gov. The complete text of the NSF Grants.gov Application Guide is available on the Grants.gov website and on the NSF website at: (https://www.nsf.gov/publications/pub_summ.jsp?ods_key=grantsgovguide). To obtain copies of the Application Guide and Application Forms Package, click on the Apply tab on the Grants.gov site, then click on the Apply Step 1: Download a Grant Application Package and Application Instructions link and enter the funding opportunity number, (the program solicitation number without the NSF prefix) and press the Download Package button. Paper copies of the Grants.gov Application Guide also may be obtained from the NSF Publications Clearinghouse, telephone (703) 292-8134 or by e-mail from nsfpubs@nsf.gov.
See PAPPG Chapter II.D.2 for guidance on the required sections of a full research proposal submitted to NSF. Please note that the proposal preparation instructions provided in this program solicitation may deviate from the PAPPG instructions.

Additional Information for all NQVL Proposals

Although more than one organization may participate in a QSTD proposal, a single organization must accept overall management responsibility for the project. The proposal must be submitted by one organization, with funding provided to any other organization through subawards. Separately submitted collaborative proposals are not permitted for QSTD proposals.

Letters of Support/Endorsement are not permitted.

Letters of Collaboration

Letters of collaboration are limited to stating the intent to collaborate. Endorsements or evaluations of the proposed project are not allowed. The Project Description should document the need for and nature of collaborations, such as intellectual contributions to the project, permission to access a site, an instrument, or a facility, offer of samples and materials for research, logistical support to the research and education program, or mentoring of U.S. students at a foreign site. Letters of collaboration should be included only when the involvement of the external collaborator is critical for the success of the proposed research. Letters of collaboration must follow the following format and be included in the Other Supplementary Documents section of the proposal:

"If the proposal submitted by Dr. [insert the full name of the Principal Investigator] entitled [insert the proposal title] is selected for funding by the NSF, it is our intent to collaborate and/or commit resources as detailed in the Project Description.

Specifically, our contributions to the project would include:

[followed by a succinct list]."

Departure from this format may result in the proposal being returned without review.

Letters of Membership

Letters of Membership in a scientific collaboration, identifying the individual to be a member of a formal collaboration operating under a set of collaboration bylaws, to be sent by the collaboration's spokesperson or equivalent also are allowed. They must follow this single-sentence format and be included in the Other Supplementary Documents section of the proposal:

"The [Name of PI's Organization] group is a member in good standing of the [Name of Collaboration], including Dr. [insert the full name of the Principal Investigator] as a member of that group."

Departure from this format may result in the proposal being returned without review.

Data Management and Sharing Plan

In addition to the PAPPG requirements regarding the management and sharing of data products resulting from NQVL activities, and in alignment with the National Science and Technology Council report on "Guidance for Implementing National Security Presidential Memorandum 33 (NSPM-33)" and the National Security Memorandum 10 (NSM-10), NQVL proposals should also include in the Data Management and Sharing Plan a description of how any proprietary information or intellectual property will be managed. This description may include a discussion of how data will be shared with project partners and affiliates, how access to the data will be managed, and how the sensitivity of various data sets will be assessed. Research security concerns are relevant for NQVL projects because quantum technologies have the potential to impact U.S. economic and national security interests.

Collaborators and Other Affiliations Information

PIs should carefully follow the instructions regarding preparation of the Collaborators and Other Affiliations (COA) form provided at https://www.nsf.gov/bfa/dias/policy/coa.jsp. A COA form in .xlsx format only must be submitted as a Single Copy Document for each individual identified as senior/key personnel of the QSTD team. For large collaborations or authorships, the form should only list those people with whom the senior/key personnel have collaborated in a direct and substantive way. Senior/key personnel with questions regarding whom they should list in their COA form should contact the cognizant NQVL Program Officer(s). Note in this context that listing a collaboration name or providing a collaboration URL is not sufficient.

Proposals that deviate from the required elements of this solicitation (or other items listed in the PAPPG) may be returned without review.

Additional Information for QSTD Proposals

PIs are reminded that the goal of the NQVL program is to accelerate progress towards demonstrations of practical quantum advantage, using a convergent, systems engineering, and co-design approach. The Program is committed to supporting use-inspired scientific research and technology development for the benefit of the national economy and to strengthen the Nation's strategic, scientific, and technological preeminence.

PIs are required to contact the NQVL Program Officer(s) at National Quantum Virtual Laboratory, telephone: 703-292-8235 or email: NQVL@nsf.gov as soon as possible, but not later than two weeks before submitting a proposal in response to this solicitation, in order to determine the level of readiness for submission to the appropriate QSTD phase as well as the appropriate structure of the QSTD proposal in terms of possible supplementary documents and/or page-limit extensions.

PIs should consult Chapter 5 of the Research Infrastructure Guide (RIG) for guidance on planning and oversight requirements relevant to QSTD projects.

QSTD proposals must clearly describe:

What: QSTD vision describing the specific Science and/or Technology area that is the focus of the translation to be supported under the NQVL program and who might be the potential users.
Why: Scientific and technology challenges that can be addressed effectively only by a QSTD project.
How: Plan of activities to address technical challenges.
Who: Team with the organizational, scientific, technical, and sociocultural skills, trusted and respected by the QISE community.
Readiness: Evidence that the QSTD project is feasible in the time and with the resources afforded by the NSF NQVL program.
Community: Plans for engaging the QISE community in the QSTD planning and execution, for fostering education and workforce development, and for promoting the full spectrum of diverse talent in the QISE community.
Partnerships: Dependencies. Synergies. Leverage other NQI-relevant investments by NSF or other U.S. Federal agencies. Public-private partnerships.
Management and Coordination: Roles and responsibilities of all senior/key personnel. Deliverables. Timeline. Milestones.
Outcomes.
Metrics of Success.
Additional Information for QSTD Design Proposals

At the Design phase, the proposal must contain the QSTD preliminary project design and include planning for the total anticipated QSTD project lifetime. Proposals must also include an appropriately scaled Project Execution Plan (PEP) describing how the project will be managed, the scope of work in a Work Breakdown Structure (WBS) format along with a WBS dictionary, the budget estimate and basis of estimate for each WBS element, and the risk or uncertainty in the budget estimate accompanied by the methodology for risk and budget contingency estimation. A resource-loaded schedule may also be required to support the proposed QSTD system integration funding profile. Projection of operating costs should be revisited in an updated plan for the operations component of the QSTD project.

Additional Information for QSTD Implementation Proposals

At the Implementation phase, the QSTD proposal demonstrates that the enabling research and technology development for the first-generation QSTD system integration project is completed, and that bid packages for major contracts or acquisitions have been completed. The QSTD system integration budget estimate for the first-generation QSTD is refined so that it is based substantially on externally provided information rather than internal engineering estimates (vendor quotes, budgetary estimates, etc.) Key staff members needed to manage project activities are recruited and ready to commence system integration. Commitments from external partners in the activity are confirmed. The largest and most complex projects are encouraged to use appropriately scaled Earned Value Management reporting during system integration and should prepare an Earned Value Management System during this phase in readiness for system integration.

B. Budgetary Information
Cost Sharing:

Inclusion of voluntary committed cost sharing is prohibited.

C. Due Dates
Full Proposal Target Date(s):

     April 01, 2025

NQVL:QSTD:Design

     April 07, 2026

NQVL:QSTD:Design

     April 07, 2026

NQVL:QSTD:Implementation

     April 06, 2027

NQVL:QSTD:Design

     April 06, 2027

NQVL:QSTD:Implementation

     April 04, 2028

NQVL:QSTD:Implementation

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

Design phase: The NSF proposal review at this phase will focus on project-related aspects such as budgets and project management, and will evaluate, as appropriate to this level:

the preliminary Project Execution Plan (PEP) describing how the project will be managed;
the scope of work in a Work Breakdown Structure (WBS) format along with a WBS dictionary;
the budget estimate and basis of estimate for each WBS element;
the risk or uncertainty in the budget estimate accompanied by the methodology for risk and budget contingency estimation; and
the preliminary Education and Workforce Development Plan (E&WDP).
The Program may seek additional reviews to evaluate the technical scope and costs at a level commensurate with preliminary design.

Implementation phase: The NSF proposal review at this phase will focus on reliability of cost estimates and technical readiness, as evidenced by the following:

the QSTD:Implementation proposal demonstrates that enabling research and technology development is completed;
any bid packages for major contracts or acquisitions have been completed;
the QSTD system integration budget estimate is refined so that it is based substantially on externally provided information rather than internal engineering estimates (vendor quotes, budgetary estimates, etc.);
key staff members needed to manage project activities are recruited and ready to commence system integration;
commitments from external partners in the activity are confirmed; and
the final Education and Workforce Development Plan (E&WDP) is satisfactory.
The Program may seek additional reviews to evaluate the technical scope and costs at a level commensurate with final design.

B. Review and Selection Process
Proposals submitted in response to this program solicitation will be reviewed by Ad hoc Review and/or Panel Review.

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

C. Reporting Requirements
For all multi-year grants (including both standard and continuing grants), the Principal Investigator must submit an annual project report to the cognizant Program Officer no later than 90 days prior to the end of the current budget period. (Some programs or awards require submission of more frequent project reports). No later than 120 days following expiration of a grant, the PI also is required to submit a final annual project report, and a project outcomes report for the general public.

Failure to provide the required annual or final annual project reports, or the project outcomes report, will delay NSF review and processing of any future funding increments as well as any pending proposals for all identified PIs and co-PIs on a given award. PIs should examine the formats of the required reports in advance to assure availability of required data.

PIs are required to use NSF's electronic project-reporting system, available through Research.gov, for preparation and submission of annual and final annual project reports. Such reports provide information on accomplishments, project participants (individual and organizational), publications, and other specific products and impacts of the project. Submission of the report via Research.gov constitutes certification by the PI that the contents of the report are accurate and complete. The project outcomes report also must be prepared and submitted using Research.gov. This report serves as a brief summary, prepared specifically for the public, of the nature and outcomes of the project. This report will be posted on the NSF website exactly as it is submitted by the PI.

More comprehensive information on NSF Reporting Requirements and other important information on the administration of NSF awards is contained in the NSF Proposal & Award Policies & Procedures Guide (PAPPG) Chapter VII, available electronically on the NSF Website at https://www.nsf.gov/publications/pub_summ.jsp?ods_key=pappg.

VIII. Agency Contacts
Please note that the program contact information is current at the time of publishing. See program website for any updates to the points of contact.

General inquiries regarding this program should be made to:

National Quantum Virtual Laboratory, telephone: (703) 292-8235, email: NQVL@nsf.gov
Bogdan Mihaila, MPS/PHY, telephone: (703) 292-8235, email: bmihaila@nsf.gov
Elizabeth Behrman, CISE/CCF, telephone: (703) 292-7049, email: ebehrman@nsf.gov
Almadena Y. Chtchelkanova, CISE/CCF, telephone: (703) 292-8910, email: achtchel@nsf.gov
Dominique M. Dagenais, ENG/ECCS, telephone: (703) 292-2980, email: ddagenai@nsf.gov
David Darwin, TIP/ITE, telephone: (703) 292-4728, email: ddarwin@nsf.gov
Pradeep P. Fulay, TIP/ITE, telephone: (703) 292-2445, email: pfulay@nsf.gov
Wu He, EDU/DRL, telephone: (703) 292-7593, email: wuhe@nsf.gov
Andrey Kanaev, CISE/OAC, telephone: (703) 292-2841, email: akanaev@nsf.gov
Matthew McCune, ENG/ECCS, telephone: (703) 292-2906, email: mamccune@nsf.gov
Engin Serpersu, BIO/MCB, telephone: (703) 292-7124, email: eserpers@nsf.gov
For questions related to the use of NSF systems contact:

NSF Help Desk: 1-800-381-1532
Research.gov Help Desk e-mail: rgov@nsf.gov
For questions relating to Grants.gov contact:

Grants.gov Contact Center: If the Authorized Organizational Representatives (AOR) has not received a confirmation message from Grants.gov within 48 hours of submission of application, please contact via telephone: 1-800-518-4726; e-mail: support@grants.gov.
For programmatic inquiries, please email the NQVL Program Director(s) at NQVL@nsf.gov. The partner Directorates are represented on the NQVL Management Team by the Program Directors listed under Agency Contacts.

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
        