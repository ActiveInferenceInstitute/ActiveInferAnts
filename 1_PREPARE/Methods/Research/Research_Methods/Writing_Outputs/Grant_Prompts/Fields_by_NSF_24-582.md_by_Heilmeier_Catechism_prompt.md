
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
        NSF 24-582: NSF Small Business Innovation Research / Small Business Technology Transfer Fast-Track Pilot Programs (SBIR-STTR Fast-Track)
Program Solicitation
Document Information
Document History
Posted: June 17, 2024
Download the solicitation (PDF, 1mb)
View the program page
NSF Logo		
National Science Foundation
Directorate for Technology, Innovation and Partnerships
     Translational Impacts

Full Proposal Deadline(s) (due by 5 p.m. submitting organization’s local time):

     September 18, 2024

     November 06, 2024

     March 05, 2025

     July 02, 2025

     November 05, 2025

TABLE OF CONTENTS
Summary of Program Requirements

Introduction
Program Description
Award Information
Eligibility Information
Proposal Preparation and Submission Instructions
Proposal Preparation Instructions
Budgetary Information
Due Dates
Research.gov Requirements
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
The NSF SBIR/STTR Fast-Track programs (also known as America’s Seed Fund powered by NSF) provide non-dilutive, fixed amount cooperative agreements for the development of a broad range of technologies based on discoveries in science and engineering with the potential for societal and economic impacts.

This new pilot effort shares the same goals as the NSF SBIR/STTR Phase I and Phase II funding opportunities, but the NSF SBIR/STTR Fast-Track pilot programs have different eligibility requirements. Small businesses applying to the NSF SBIR/STTR Fast-Track pilot programs must have a lineage of NSF research funding, at least one Senior/Key Personnel to have undergone formal customer discovery training, and the entire team must already be in place (not yet to be determined) at the time of proposal submission. For further information see Eligibility Criteria.

The maximum total SBIR/STTR Fast-Track award amount is $1,555,000 (inclusive of direct and indirect costs, Technical and Business Assistance (TABA) funding, and the small business fee): $400,000 maximum for the Phase I component and $1,155,000 maximum for the Phase II component. The expected project duration will be between 24 months and 36 months. The duration of a Phase I component can be between 6 months and 12 months, to be specified by the company. The duration of a Phase II component can be between 18 months and 24 months, to be specified by the company.

NSF proposals are confidential and will only be shared with a select number of reviewers and NSF staff (as appropriate). All reviewers have agreed to maintain the confidentiality of the proposal content. Proposals to NSF do not constitute a public disclosure. If selected for an award, the company will be prompted to write a publicly available abstract that summarizes the intellectual merit and broader impact of the project.

The NSF SBIR/STTR Fast-Track pilot programs do not support clinical trials or proposals from companies whose commercialization pathway involves the production, distribution, or sale by the company of chemical components, natural or synthetic variations thereof, or other derivatives related to Schedule I controlled substances.

All proposals must be submitted through Research.gov.

NSF SBIR/STTR Fast-Track pilot proposals will not be accepted in Grants.gov. NSF Fast-Track SBIR and STTR pilot proposals are nearly identical but differ in the amount of work performed by the small business and a not-for-profit institution or a Federally funded research and development center (FFRDC) (as noted in the budget). For more details about the unique requirements of NSF STTR Fast-Track pilot awards, please refer to the Eligibility Information and Proposal Preparation and Submission Instructions sections of this solicitation.

NSF SBIR Fast-Track Pilot proposals submitted to this solicitation that meet all the requirements of an NSF STTR Fast-Track pilot proposal may, at NSF’s discretion, be converted to NSF STTR Fast-Track pilot proposal for award. Similarly, NSF STTR Fast-Track pilot proposals may be converted to NSF SBIR Fast-Track pilot awards at NSF’s discretion.

America’s Seed Fund powered by NSF is committed to assisting SBIR/STTR Phase II recipients to successfully commercialize their innovation research, grow their company and create jobs by attracting new investments and partnerships. To reinforce these commitments, the programs support a broad number of supplements and other opportunities. For more information, see: Supplemental Funding Overview, and the linked Dear Colleagues Letters.

For the purpose of this solicitation, the following definitions apply:
Funding Agreement: As used in this solicitation, the funding agreement is a Grant – a legal instrument of financial assistance between NSF and a recipient, consistent with 31 USC 6302-6305 and as noted in the NSF Proposal & Award Policies & Procedures Guide (PAPPG) Introduction, Section D ("Definitions & NSF-Recipient Relationships").
Small Business Concerns (SBCs): SBCs are independently owned and operated businesses that are not dominant in the field of operation. For this solicitation, firms qualifying as a small business concern are eligible to participate in the SBIR/STTR programs (see Section II. "Eligibility Information" of this solicitation for more details). Please note that the size limit of 500 employees includes affiliates. The firm must be in compliance with the SBA SBIR/STTR Policy Directive and the Code of Federal Regulations (13 CFR 121).
SBIR/STTR Data: As defined by the SBA SBIR/STTR Policy Directive, SBIR/STTR Data is all Data developed or generated in the performance of an SBIR or STTR award, including Technical Data and Computer Software developed or generated in the performance of an SBIR or STTR award. The term does not include information incidental to contract or grant administration, such as financial, administrative, cost or pricing or management information.
SBIR/STTR Data Rights: The Federal Government may, use, modify, reproduce, perform, display, release, or disclose SBIR/STTR Data that are Technical Data within the Government; however, the Government shall not use, release, or disclose the data for procurement, manufacturing, or commercial purposes; or release or disclose the SBIR/STTR Data outside the Government except as permitted by paragraph 10(B) of the SBIR/STTR Policy Directive's Data Rights Clause or by written permission of the recipient.
Research and Development (R&D): broadly defined in 2 CFR § 200.8, but specified for the NSF SBIR/STTR programs as follows:
the application of creative, original, and potentially transformative concepts to systematically study, create, adapt, or manipulate the structure and behavior of the natural or man-made worlds;
the use of the scientific method to propose well-reasoned, well-organized activities based on sound theory, computation, measurement, observation, experiment, or modeling;
the demonstration of a well-qualified individual, team, or organization ready to deploy novel methods of creating, acquiring, processing, manipulating, storing, or disseminating data or metadata; and/or
the novel integration of new theories, analysis, data, or methods regarding cognition, heuristics, and related phenomena, which can be supported by scientific rationale.
Non-Dilutive Funding: financing that does not involve equity, debt, or other elements of the business ownership structure.
Technical Risk: Technical risk assumes that the possibility of technical failure exists for an envisioned product, service, or solution to be successfully developed. This risk is present even to those suitably skilled in the art of the component, subsystem, method, technique, tool, or algorithm in question. If the new product, service, or solution is successfully realized and brought to the market, it would be difficult for a well-qualified, competing firm to reverse-engineer or otherwise neutralize the competitive advantage generated by leveraging fundamental science or engineering research techniques.
Technological Innovation indicates that the new product or service is differentiated from current products or services; that is, the new technology holds the potential to result in a product or service with a substantial and durable advantage over competing solutions on the market. It also generally provides a barrier to entry for competitors.
The proposal submission system, Research.gov, will stop accepting proposals at 5:00 pm submitting organization’s local time. If your submission is late, you will not be able to submit again until the next deadline. Proposers are strongly urged to submit well in advance of the deadline.

An Intellectual Property (IP) Rights agreement is required for STTR proposals and strongly recommended for SBIR proposals when there is a subaward to another institution. A fully signed agreement is not required for STTR proposals at the initial proposal submission but will be required before a recommendation for an award can be made.

A small business must receive an official invitation via the Project Pitch, a process to submit a full Fast-Track proposal. Details regarding this process as well as how to submit a Fast-Track Project Pitch can be found in Section III.A. of this document. Small businesses that meet the Fast-Track eligibility criteria can submit a Fast-Track Project Pitch at any time. Small businesses that have been invited to submit a full Fast-Track proposal can submit a proposal based on that Project Pitch at any time up to 4 months after the date of the invitation.

In addition to the standard NSF Merit Review Criteria, this solicitation provides additional clarification on how Intellectual Merit and Broader Impact might be applied to startups and small businesses. Additional solicitation-specific merit review criteria focused on Commercialization Potential is also applied.

Four documents: Biographical Sketch(es), Current and Pending (Other) Support forms, Collaborators and Other Affiliations (COA), and Synergistic Activities must be submitted for the PI, Co-PI (if STTR), and each Senior/Key Personnel specified in the proposal. Biographical Sketches and Current and Pending Support forms must be prepared using SciENcv: Science Experts Network Curriculum Vitae. Collaborators & Other Affiliations (COA) Information is prepared using the instructions and spreadsheet template.

Synergistic Activities. Each individual identified as a Senior/Key person must provide a document of up to one-page that includes a list of up to five distinct examples of synergistic activities that demonstrate the broader impact of the individual’s professional and scholarly activities that focus on the integration and transfer of knowledge as well as its creation.

In compliance with the CHIPS and Science Act of 2022, section 10636 (Person or entity of concern prohibition; 42 U.S.C. 19235): No person published on the list under section 1237(b) of the Strom Thurmond National Defense Authorization Act for Fiscal Year 1999 (Public Law 105-261; 50 U.S.C. 1701 note) or entity identified under section 1260h of the William M. (Mac) Thornberry National Defense Authorization Act for Fiscal Year 2021 (10 U.S.C. 113 note; Public Law 116-283) may receive or participate in any grant, award, program, support, or other activity under the Directorate for Technology, Innovation and Partnerships (TIP).

In accordance with Section 10632 of the CHIPS and Science Act of 2022 (42 U.S.C. § 19232), the Authorized Organizational Representative (AOR) must certify that all individuals identified as Senior/Key Personnel have been made aware of and have complied with their responsibility under that section to certify that the individual is not a party to a Malign Foreign Talent Recruitment Program.

In accordance with Section 223(a)(1) of the William M. (Mac) Thornberry National Defense Authorization Act for Fiscal Year 2021 (42 U.S.C. § 6605(a)(1)), each individual identified as Senior/Key Personnel is required to certify in SciENcv that the information provided in the Biographical Sketch and Current and Pending (Other) Support documents are accurate, current, and complete. Senior/Key Personnel are required to update their Current and Pending (Other) Support disclosures prior to award, and at any subsequent time the agency determines appropriate during the term of the award. See additional information on NSF Disclosure Requirements in the PAPPG, Chapter II.B. Each Senior/Key Person must also certify prior to proposal submission that they are not a party to a Malign Foreign Talent Recruitment Program and annually thereafter for the duration of the award.

Three (3) Letters of Support from potential product/service users or customers are required; Up to five (5) Letters of Support may be submitted.

Letters of Commitment that confirm the role of any subaward organization(s) in the project and explicitly state the subaward amount are also required.

Additional information on the due diligence process, used as part of the review and selection process, is included in Section VI. The due diligence process may include requests for clarification of the company structure, key personnel, conflicts of interest, foreign influence, cybersecurity practices, or other issues as determined by NSF. Participation in the due diligence process is not a guarantee that an award will be made.

SBIR/STTR Fast-Track proposals that have been declined by NSF are NOT eligible for reconsideration. A decision by NSF not to provide additional funding following either the Stage Gate 1 or Stage Gate 2 review will NOT be eligible for reconsideration or termination review as defined in Chapter XII.A.4 of the PAPPG.

This solicitation contains many instructions that deviate from the standard NSF PAPPG proposal preparation instructions. In the event of a conflict between the instructions in this solicitation and the PAPPG, use this solicitation’s instructions as a guide.

Any proposal submitted in response to this solicitation should be submitted in accordance with the NSF Proposal & Award Policies & Procedures Guide (PAPPG) that is in effect for the relevant due date to which the proposal is being submitted. The NSF PAPPG is regularly revised and it is the responsibility of the proposer to ensure that the proposal meets the requirements specified in this solicitation and the applicable version of the PAPPG. Submitting a proposal prior to a specified deadline does not negate this requirement.

Summary Of Program Requirements
General Information
Program Title:

NSF Small Business Innovation Research / Small Business Technology Transfer Fast-Track Pilot Programs (SBIR-STTR Fast-Track)
Synopsis of Program:

The NSF SBIR/STTR and SBIR/STTR Fast-Track pilot programs support moving scientific excellence and technological innovation from the lab to the market. By funding startups and small businesses, NSF helps build a strong national economy and stimulates the creation of novel products, services, and solutions in private, public, or government sectors with potential for broad impact; strengthens the role of small business in meeting federal research and development needs; increases the commercial application of federally supported research results; and develops and increases the US workforce, especially by fostering and encouraging participation by socially and economically disadvantaged and women-owned small businesses.

These NSF SBIR/STTR Fast-Track pilot programs provide fixed amount cooperative agreements for the development of a broad range of technologies based on discoveries in science and engineering with potential for societal and economic impacts. Unlike fundamental or basic research activities that focus on scientific and engineering discovery itself, the NSF SBIR/STTR Fast-Track pilot programs support the creation of opportunities to move use-inspired and translational discoveries out of the lab and into the market or other use at scale, through startups and small businesses. The NSF SBIR/STTR Fast-Track pilot programs do not solicit specific technologies or procure goods and services from startups and small businesses. Any invention conceived or reduced to practice with the assistance of SBIR/STTR funding is subject to the Bayh-Dole Act. For more information refer to SBIR/STTR Frequently Asked Questions #75.

NSF promotes inclusion by encouraging proposals from diverse populations and geographic locations.

The traditional NSF SBIR/STTR programs include two funding Phases – Phase I and Phase II. All proposers to the programs must first apply for Phase I funding – there is no direct-to-Phase II option. Under a traditional NSF SBIR/STTR Phase I award, a small business can receive non-dilutive funding for research and development (R&D) to demonstrate technical feasibility over 6 to 12 months and then, after completion of a Phase I project, companies may apply for Phase II funding to further develop the proposed technology.

There are significant benefits for SBIR/STTR Fast-Track recipients: the submission of only one proposal for Phase I and Phase II and a faster transition from Phase I to Phase II. While startups and small businesses face many challenges, NSF SBIR/STTR Fast-Track funding is intended to specifically focus on challenges associated with technological innovation; that is, on the creation of new products, services, and other scalable solutions based on fundamental science or engineering. A successful Fast-Track proposal must demonstrate how NSF funding will help the small business create a proof-of-concept or prototype by retiring technical risk.

NSF seeks unproven, leading-edge, technology innovations that demonstrate the following characteristics:

The innovations are underpinned and enabled by a new scientific discovery or meaningful engineering innovation.
The innovations still require intensive technical research and development to be fully embedded in a reliable product or service.
The innovations have not yet been reduced to practice by anyone and it is not guaranteed, at present, that doing so is technically possible.
The innovations provide a strong competitive advantage that are not easily replicable by competitors (even technically proficient ones).
Once reduced to practice, the innovations are expected to result in a product or service that would either be disruptive to existing markets or create new markets/new market segments.
The NSF SBIR/STTR Fast-Track pilot programs focus on stimulating technical innovation from diverse entrepreneurs and start-ups by translating new scientific and engineering concepts into products and services that can be scaled and commercialized into sustainable businesses with significant societal benefits. The programs provide non-dilutive funding for research and development (R&D) of use-inspired scientific and engineering activities at the earliest stages of the company and technology development. During the course of the award, the emphasis is expected to shift from de-risking those aspects preventing the innovation from reaching technical feasibility and driving the intended impact to a greater focus on commercially relevant development activities that will allow the company to differentiate itself and drive new value propositions to the market and society.

NSF encourages input and participation from the full spectrum of diverse talent that society has to offer which includes underrepresented and underserved communities.

These NSF programs are governed by 15 USC 638 and the National Science Foundation Act of 1950, as amended (42 USC §1861, et seq.).

Introduction to the Program

The NSF SBIR/STTR programs focus on stimulating technical innovation from diverse entrepreneurs and startups by translating new scientific and engineering discoveries emerging from the private sector, federal labs, and academia into products and services that can be scaled and commercialized into sustainable businesses with significant societal benefits.

These NSF SBIR/STTR Fast-Track pilot programs enable companies based on previous NSF awards (NSF award lineage) to submit a single proposal that, if awarded, can provide a faster pathway from Phase I to Phase II funding. Receipt of full funding under the Fast-Track pilot programs is contingent on the results of a company’s Phase II transition review.

The NSF SBIR/STTR Fast-Track pilot programs are part of the Directorate for Technology, Innovation and Partnerships (TIP), which was recently launched to accelerate innovation and enhance economic competitiveness by catalyzing partnerships and investments that strengthen the links between fundamental research and technology development, deployment, and use.

Cognizant Program Officer(s):

Please note that the following information is current at the time of publishing. See program website for any updates to the points of contact.

NSF SBIR/STTR Inbox, telephone: (703) 292-5111, email: sbir@nsf.gov

Applicable Catalog of Federal Domestic Assistance (CFDA) Number(s):

47.041 --- Engineering
47.049 --- Mathematical and Physical Sciences
47.050 --- Geosciences
47.070 --- Computer and Information Science and Engineering
47.074 --- Biological Sciences
47.075 --- Social Behavioral and Economic Sciences
47.076 --- STEM Education
47.079 --- Office of International Science and Engineering
47.083 --- Office of Integrative Activities (OIA)
47.084 --- NSF Technology, Innovation and Partnerships
Award Information
Anticipated Type of Award: Fixed Amount Cooperative Agreement

Estimated Number of Awards: 36

Approximately 20 awards for SBIR Fast-Track, pending the availability of funds.
Approximately 16 awards for STTR Fast-Track, pending the availability of funds.
Anticipated Funding Amount: $56,000,000

Approximately $31 M for SBIR Fast-Track
Approximately $25 M for STTR Fast-Track
Estimated program budget, number of awards and average award size/duration are subject to the availability of funds.

Eligibility Information
Who May Submit Proposals:

Proposals may only be submitted by the following:

Small businesses concerns must meet ALL of the following requirements:

Proposers that have submitted a SBIR/STTR Fast-Track Project Pitch and received an official invitation from a cognizant NSF SBIR/STTR Program Officer within the 4 months preceding the proposal submission date. To start this process, proposers must first create a log in and submit a Project Pitch document via the NSF SBIR/STTR Fast-Track Project Pitch online form. The cognizant NSF SBIR/STTR Program Officer will use the Project Pitch to determine whether the proposed project is a good fit for the Fast-Track program.
Companies qualifying as a small business concern are eligible to participate in the NSF SBIR/STTR Fast-Track pilot programs (see Guide to SBIR/STTR Program Eligibility for more information). Please note that the size limit of 500 employees includes affiliates. The firm must be in compliance with the SBIR/STTR Policy Directive and the Code of Federal Regulations. For STTR proposals, the proposing small business must also include a partner research institution in the project, see additional details below.
The SBIR/STTR Fast-Track pilot effort shares the same goals as the NSF SBIR/STTR Phase I and Phase II funding opportunities, but the Fast-Track pilot programs have different eligibility requirements. Small businesses applying to the NSF SBIR/STTR Fast-Track pilot programs must have 1) a lineage of NSF research funding, 2) at least one Senior/Key Personnel to have undergone formal customer discovery training, and 3) the entire team must already be in place (not yet to be determined) at the time of proposal submission. If the small business concern does not meet all three of these criteria, their proposal will be transferred to the NSF SBIR/STTR Phase I program for consideration.
Lineage Eligibility Requirement. The technical innovation in the Fast-Track proposal must be derived from a prior NSF research award that is either currently active or was active within the previous five years from the date of submission of the Fast-Track proposal. The Fast-Track Project Pitch and proposal must include the NSF award number and title of the research award that is relied upon to meet the lineage requirement. The Fast-Track proposal’s PI or at least one Senior/Key Personnel must have been supported under the lineage award. If the Fast-Track team member relied upon to meet the lineage requirement is named on the lineage award, no further documentation will be required. If not, the Fast-Track proposal must include a letter from the PI or a Co-PI of the lineage award confirming that either the PI or a named Senior/Key Personnel on the Fast-Track team was engaged in research undertaken under the lineage award. In addition to regular NSF research awards (e.g., CAREER, individual investigator awards, center/institute awards, etc.), Partnerships for Innovation (PFI) and NSF Graduate Research Fellowship Program (GRFP) awards do count as NSF lineage for SBIR/STTR Fast-Track eligibility. NSF Innovation Corps (I-Corps) and NSF SBIR/STTR awards do not count as NSF research lineage and do not convey SBIR/STTR Fast-Track eligibility.
Formal Customer Discovery Eligibility Requirement. Companies must have received formal customer discovery training, defined as follows, within the previous two years from the date of the Fast-Track proposal submission. At least one of the Senior/Key Personnel on the Fast-Track proposal must have undergone formal customer discovery training in relation to the proposed technology via a suitably qualified program, such as the NSF I-Corps program or a program at an incubator or accelerator, with a result that at the start of the Fast-Track project the proposing company has a clear understanding of the product-market fit and initial target customers for the proposed technology.
Complete Team Eligibility Requirement. Companies must have a complete Fast-Track team in place at the time of proposal submission – i.e., there must be no “to-be-determined” company personnel in budget lines A or B; all company personnel in budget lines A and B must have confirmed their availability for the proposed Fast-Track project per the proposed Phase I and Phase II component budgets; the proposing team must possess the required expertise to perform the proposed Fast-Track project; and the team members must dedicate sufficient time to the technical tasks that must be undertaken to achieve the objectives of the Fast-Track project.
In compliance with the CHIPS and Science Act of 2022, Section 10636 (Person or entity of concern prohibition; 42 U.S.C. 19235): No person published on the list under section 1237(b) of the Strom Thurmond National Defense Authorization Act for Fiscal Year 1999 (Public Law 105-261; 50 U.S.C. 1701 note) or entity identified under section 1260h of the William M. (Mac) Thornberry National Defense Authorization Act for Fiscal Year 2021 (10 U.S.C. 113 note; Public Law 116-283) may receive or participate in any grant, award, program, support, or other activity under the Directorate for Technology, Innovation, and Partnerships.
Individuals who are a current party to a Malign Foreign Talent Recruitment Program are not eligible to serve as a Senior/Key Person on an NSF proposal or on any NSF award made after May 20, 2024. See current PAPPG for additional information on required certifications associated with Malign Foreign Talent Organization. The Authorized Organizational Representative (AOR) must certify that all individuals identified as Senior/Key Personnel have been made aware of and have complied with their responsibility under that section to certify that the individual is not a party to a Malign Foreign Talent Recruitment Program.
The small business concern’s R&D must be performed within the United States. Startups and small businesses funded by NSF must be majority U.S.-owned companies.
The companies may not be majority-owned by one or more venture capital operating companies (VCOCs), hedge funds, or private equity firms. Proposals from joint ventures and partnerships are permitted, provided the proposing entity qualifies as a small business concern (see Guide to SBIR/STTR Program Eligibility for more information).
“Collaborative Proposal from Multiple Organizations” (a special proposal type in Research.gov) are not allowed.
Socially and economically disadvantaged small businesses and women-owned small businesses are also encouraged to apply.
Who May Serve as PI:

The primary employment of the Principal Investigator (PI) must be with the small business concern at the time of award and for the duration of the award, unless a new PI is approved by NSF. Primary employment is defined as at least 51 percent employed by the small business. NSF normally considers a full-time work week to be 40 hours and considers employment elsewhere of greater than 19.6 hours per week to be in conflict with this requirement. The PI must have a legal right to work for the proposing company in the United States, as evidenced by citizenship, permanent residency, or an appropriate visa. The PI does not need to be associated with an academic institution. There are no PI degree requirements (i.e., the PI is not required to hold a Ph.D. or any other degree). A PI must devote a minimum of three calendar months of effort per six months of performance to an NSF SBIR/STTR Fast-Track project.

Limit on Number of Proposals per Organization: 1

An organization must wait for a determination from NSF (e.g., award, decline, or returned without review) regarding a pending NSF SBIR/STTR Fast-Track pilot proposal before submitting a new Project Pitch in the next window.

An organization that has submitted a traditional SBIR/STTR Project Pitch, received an invitation to submit a traditional SBIR/STTR Phase I proposal, or has a traditional SBIR/STTR Phase I proposal under review may not submit a Fast-Track Project Pitch until either the traditional SBIR/STTR Project Pitch has been declined (i.e., not invited) or the outcome of the invited traditional SBIR/STTR proposal submission has been made available to the organization.

Proposals that have been Returned Without Review may be submitted using the same Project Pitch invitation (assuming that the proposal is received within 4 months of the original invitation).

Limit on Number of Proposals per PI or co-PI: 1

For NSF SBIR Fast-Track – 1 PI, co-PIs are not allowed.

For NSF STTR Fast-Track - 1 PI and 1 Co-PI are required (the PI must be an employee of the proposing small business and the Co-PI must be part of the STTR partner research institution). An individual may be listed as the PI for only one proposal submitted at a time to the NSF SBIR/STTR programs (including traditional and Fast-Track).

For NSF STTR Fast-Track proposals, a person may act as co-PI on an unlimited number of proposals.

Proposal Preparation and Submission Instructions
A. Proposal Preparation Instructions

Letters of Intent: Not required
Preliminary Proposal Submission: Not required
Full Proposal Preparation Instruction: This solicitation contains information that deviates from the standard NSF Proposal and Award Policies and Procedures Guide (PAPPG) proposal preparation guidelines. Please see the full text of this solicitation for further information.

B. Budgetary Information

Cost Sharing Requirements:

Inclusion of voluntary committed cost sharing is prohibited.

Indirect Cost (F&A) Limitations:

Not Applicable

Other Budgetary Limitations:

Other budgetary limitations apply. Please see the full text of this solicitation for further information.

C. Due Dates

Full Proposal Deadline(s) (due by 5 p.m. submitting organization’s local time):

     September 18, 2024

     November 06, 2024

     March 05, 2025

     July 02, 2025

     November 05, 2025

Proposal Review Information Criteria
Merit Review Criteria:

National Science Board approved criteria. Additional merit review criteria apply. Please see the full text of this solicitation for further information.

Award Administration Information
Award Conditions:

Additional award conditions apply. Please see the full text of this solicitation for further information.

Reporting Requirements:

Standard NSF reporting requirements apply.

I. Introduction
The NSF SBIR/STTR Fast-Track pilot programs focus on stimulating technical innovation from diverse entrepreneurs and startups by translating new scientific and engineering discoveries emerging from the private sector, federal labs, and academia into products and services that can be scaled and commercialized into sustainable businesses with significant societal benefits. The NSF SBIR/STTR Fast-Track pilot programs support moving scientific excellence and technological innovation from the lab to the market. By funding startups and small businesses, NSF helps build a strong national economy and stimulates the creation of novel products, services, and solutions in private, public, or government sectors with potential for broad impact; strengthens the role of small business in meeting federal research and development needs; increases the commercial application of federally supported research results; and develops and increases the US workforce, especially by fostering and encouraging participation by socially and economically disadvantaged and women-owned small businesses.

While startups and small businesses face many challenges, the NSF SBIR/STTR Fast-Track pilot programs are intended to specifically focus on challenges associated with technological innovation; that is, on the creation of new products, services, and other scalable solutions based on fundamental science or engineering. A successful Fast-Track proposal must demonstrate how NSF funding will help the small business create a proof-of-concept or prototype by retiring technical risk.

NSF seeks unproven, leading-edge, technology innovations that demonstrate the following characteristics:

The innovations are underpinned and enabled by a new scientific discovery or meaningful engineering innovation.
The innovations still require intensive technical research and development to be fully embedded in a reliable product or service.
The innovations have not yet been reduced to practice by anyone and it is not guaranteed, at present, that doing so is technically possible
The innovations provide a strong competitive advantage that are not easily replicable by competitors (even technically proficient ones).
Once reduced to practice, the innovations are expected to result in a product or service that would either be disruptive to existing markets or create new markets/new market segments.
The NSF SBIR/STTR Fast-Track pilot programs provide non-dilutive funding for the development of deep technologies, based on discoveries in fundamental science and engineering, that offer the potential for societal and economic impacts. The NSF SBIR/STTR Fast-Track pilot programs provide fixed amount cooperative agreements for the development of a broad range of technologies based on discoveries in science and engineering with potential for societal and economic impacts. Unlike fundamental or basic research activities that focus on scientific and engineering discovery itself, the NSF SBIR/STTR Fast-Track pilot programs support the creation of opportunities to move use-inspired and translational discoveries out of the lab and into the market or other use at scale, through startups and small businesses. The NSF SBIR/STTR pilot programs do not solicit specific technologies or procure goods and services from startups and small businesses. The funding provided is non-dilutive and NSF does not receive any stake or interest in the company or in the intellectual property resulting from the funded effort. NSF promotes inclusion by encouraging proposals from diverse populations and geographic locations.

II. Program Description
The aim of the NSF SBIR/STTR Fast-Track pilot programs is to enable eligible companies (see Section IV of this document) that have a complete R&D team (i.e., no “to-be-determined” team members) to submit a single proposal that, if awarded, can provide a faster pathway from Phase I to Phase II funding. A Fast-Track proposal will include a Phase I component and a Phase II component, each with a corresponding budget. Both Phase I and Phase II components of a Fast-Track proposal will be reviewed prior to the start of a Fast-Track project. On completion of the Phase I component, and contingent upon the results of a company’s Phase II transition review (see below for details), a Fast-Track awardee company will be able to transition directly to the Phase II component of the project. The primary benefits for Fast-Track awardee companies are (i) a pathway at the start of an awarded Fast-Track project to the full funding opportunities of the NSF SBIR/STTR Phase I and Phase II programs, and (ii) a faster transition from Phase I to Phase II than for traditional NSF SBIR/STTR Phase I awardees. Receipt of full funding under the Fast-Track programs is contingent upon the success of a company’s Phase II transition review.

The NSF SBIR/STTR Fast-Track pilot programs welcome proposals from almost all areas of technology. The program website presents a number of topic areas, but these are only meant to be suggestive of the types of topic areas that are anticipated. The programs are also open to proposals that focus on technical and market areas not explicitly noted in the aforementioned topics. Proposals that do not have an obvious fit in one of the specific topic areas can be submitted to “Other Topics”. NSF encourages eligible companies from all technology sectors and geographic areas to apply for funding. NSF does not test, verify, or otherwise use the technology developed under its SBIR/STTR Fast-Track awards.

The NSF SBIR/STTR Fast-Track pilot programs are expected to be highly competitive. Only a fraction of proposals submitted will be selected for an award. Thus, there may be many qualified businesses applying to the programs that do not receive funding.

NSF evaluates SBIR/STTR Fast-Track proposals under three distinct, but related merit review criteria: Intellectual Merit, Broader Impacts, and Commercialization Potential.

In addition to the standard NSF Merit Review Criteria (Section VI.A.), the following provides additional clarification of how Intellectual Merit and Broader Impact might be applied to startups and small businesses (Section II and IV.A.2).

The Intellectual Merit criterion encompasses the potential to advance knowledge and leverage fundamental science or engineering research techniques to overcome technical risk. This can be conveyed through the Research and Development (R&D) of the project.

NSF SBIR/STTR Fast-Track proposals are evaluated via the concepts of Technical Risk and Technological Innovation. Technical Risk assumes that the possibility of technical failure exists for an envisioned product, service, or solution to be successfully developed. This risk is present even to those suitably skilled in the art of the component, subsystem, method, technique, tool, or algorithm in question. Technological Innovation indicates that the new product or service is differentiated from current products or services; that is, the new technology holds the potential to result in a product or service with a substantial and durable advantage over competing solutions on the market. It also generally provides a barrier to entry for competitors. This means that if the new product, service, or solution is successfully realized and brought to the market, it should be difficult for a well-qualified, competing firm to reverse-engineer or otherwise neutralize the competitive advantage generated by leveraging fundamental science or engineering research techniques.

The Broader Impacts criterion encompasses the potential for the company to drive a benefit to society in terms of addressing major societal challenges. Considering the products developed under these programs will have a broad societal reach, will be widely distributed, and will therefore have impacts that are far reaching with people and communities. It is important to ensure adequate assessment of potential benefits and unintended consequences of the proposed technology.

The NSF SBIR/STTR Fast-Track pilot programs support the vision of the NSF, which is a nation that leads the world in science and engineering research and innovation to the benefit of all, without barriers to participation. Proposers may also consider the Broader Impacts Review Criterion at 42 U.S.C. §1862p-14 as related to the potential for broadest societal impact.

An additional, solicitation-specific merit review criteria focused on Commercialization Potential is also required. The Commercialization Potential of the proposed product or service is the potential for the resulting technology to disrupt the targeted market segment by way of a strong and durable value proposition for the customers or users.

The proposed product or service addresses an unmet, important, and scalable need for the target customer base.
The proposed small business is structured and staffed to focus on aggressive commercialization of the product/service.
The proposed small business can provide evidence of good product-market fit (as validated by direct and significant interaction with customers and related stakeholders).
More details and information regarding the NSF SBIR/STTR merit review criteria can be found in Section VI.A of this solicitation and the NSF SBIR/STTR website.

The review of an NSF SBIR/STTR Fast-Track proposal includes both the Phase I and Phase II components of the proposal. A team submitting an NSF SBIR/STTR Fast-Track proposal must have NSF-funded research lineage (see Section IV); customer discovery training in order to develop an understanding of the target market, product-market fit and initial target customers; and a complete team (no “to-be-determined” members).

The Phase I and Phase II components of an NSF SBIR/STTR Fast-Track proposal will be reviewed and evaluated separately. For cases in which reviewers and the cognizant Program Officer deem that the Phase I component is meritorious, but the Phase II component is not, the Program Officer may consider recommending the Fast-Track proposal for a traditional NSF SBIR/STTR Phase I award. The company would subsequently be eligible to apply for NSF SBIR/STTR Phase II funding via the traditional process (i.e., not via the Fast-Track process).

An NSF SBIR/STTR Fast-Track proposal must include specific, quantifiable performance targets for the Phase I component of the project. These Phase I targets may be renegotiated with the cognizant Program Officer during post-review diligence, so that at the start of the Fast-Track project there will be agreed performance targets in place for the Phase I component.

Phase II Transition Review: The Phase II transition review will consist of two stage gates:

Stage Gate 1: Progress Evaluation.

Approximately three (3) months prior to the end of the Phase I component, the NSF SBIR/STTR Fast-Track recipient will be required to participate in a reverse site visit during which they will present to NSF the results of the Phase I project to date. Detailed guidance regarding the reverse site visit will be provided to the recipient four to six weeks prior to the reverse site visit. NSF will evaluate progress made by the Fast-Track recipient company during the Phase I component, taking into account a number of factors including, but not limited to:

Phase I performance compared with the agreed performance targets;
commercial progress and commercial traction during Phase I;
team suitability for Phase II; and
additional resources – including company personnel, advisors, and funding that are accessible to the company for technical, regulatory, or commercial activities associated with the Phase II component.
Based on the results of NSF’s SBIR/STTR Fast-Track Stage Gate 1 review, if NSF determines, based on this progress evaluation, that a Fast-Track award recipient should have the opportunity to transition to the Phase II component, the company will advance to Stage Gate 2.

Alternatively, NSF may decide that an NSF SBIR/STTR Fast-Track award will not transition to the Phase II component. In such cases, the Fast-Track project will be limited to Phase I funding, and the award will conclude at the end of the Phase I component. NSF will communicate its decision and rationale back to the Fast-Track awardee. The company will not be eligible to apply for regular SBIR/STTR Phase II funding based on the Fast-Track award. NOTE: NSF’s decision not to provide SBIR/STTR Phase II funding following Stage Gate 1 is not subject to reconsideration or termination review as defined in Chapter XII.A.4 of the PAPPG.

Stage Gate 2: CAP Review

NSF SBIR/STTR Fast-Track award recipients who progress beyond the Stage Gate 1 will be required to prepare and submit administrative and supporting financial documentation for review by the NSF Cost Analysis and Pre-Award (CAP) Branch. See https://www.nsf.gov/bfa/dias/caar/sbirrev.jsp for detailed requirements. CAP reviews are conducted to evaluate a prospective recipient's ability to manage a federal award effectively and efficiently, as well as to establish the reasonableness of the dollar amount for the Phase II component of the award. Based on the results of the Stage Gate 2 review, NSF may decide that a Fast-Track award will not receive additional Phase II funding, and the award will conclude at the end of the Phase I component. NSF will communicate its decision and rationale back to the Fast-Track recipient. The company will not be allowed to apply for regular SBIR/STTR Phase II funding based on the Fast-Track award. NOTE: NSF’s decision not to provide SBIR/STTR Phase II funding following Stage Gate 2 is not subject to reconsideration or termination review as defined in Chapter XII.A.4 of the PAPPG.

Companies who pass both Stage Gates 1 and 2 will receive a funding increment for the Phase II component of the award, and they will be eligible to apply for the same Phase II supplemental funding opportunities as are available to a traditional NSF SBIR/STTR Phase II awardee.

III. Award Information
Anticipated Type of Award: Fixed Amount Cooperative Agreement

Estimated Number of Awards: 36

Approximately 20 awards for SBIR Fast-Track, pending the availability of funds.
Approximately 16 awards for STTR Fast-Track, pending the availability of funds.
Anticipated Funding Amount: $56,000,000

Approximately $31 M for SBIR Fast-Track
Approximately $25 M for STTR Fast-Track
Estimated program budget, number of awards and average award size/duration are subject to the availability of funds.

IV. Eligibility Information
Who May Submit Proposals:

Proposals may only be submitted by the following:

Small businesses concerns must meet ALL of the following requirements:

Proposers that have submitted a SBIR/STTR Fast-Track Project Pitch and received an official invitation from a cognizant NSF SBIR/STTR Program Officer within the 4 months preceding the proposal submission date. To start this process, proposers must first create a log in and submit a Project Pitch document via the NSF SBIR/STTR Fast-Track Project Pitch online form. The cognizant NSF SBIR/STTR Program Officer will use the Project Pitch to determine whether the proposed project is a good fit for the Fast-Track program.
Companies qualifying as a small business concern are eligible to participate in the NSF SBIR/STTR Fast-Track pilot programs (see Guide to SBIR/STTR Program Eligibility for more information). Please note that the size limit of 500 employees includes affiliates. The firm must be in compliance with the SBIR/STTR Policy Directive and the Code of Federal Regulations. For STTR proposals, the proposing small business must also include a partner research institution in the project, see additional details below.
The SBIR/STTR Fast-Track pilot effort shares the same goals as the NSF SBIR/STTR Phase I and Phase II funding opportunities, but the Fast-Track pilot programs have different eligibility requirements. Small businesses applying to the NSF SBIR/STTR Fast-Track pilot programs must have 1) a lineage of NSF research funding, 2) at least one Senior/Key Personnel to have undergone formal customer discovery training, and 3) the entire team must already be in place (not yet to be determined) at the time of proposal submission. If the small business concern does not meet all three of these criteria, their proposal will be transferred to the NSF SBIR/STTR Phase I program for consideration.
Lineage Eligibility Requirement. The technical innovation in the Fast-Track proposal must be derived from a prior NSF research award that is either currently active or was active within the previous five years from the date of submission of the Fast-Track proposal. The Fast-Track Project Pitch and proposal must include the NSF award number and title of the research award that is relied upon to meet the lineage requirement. The Fast-Track proposal’s PI or at least one Senior/Key Personnel must have been supported under the lineage award. If the Fast-Track team member relied upon to meet the lineage requirement is named on the lineage award, no further documentation will be required. If not, the Fast-Track proposal must include a letter from the PI or a Co-PI of the lineage award confirming that either the PI or a named Senior/Key Personnel on the Fast-Track team was engaged in research undertaken under the lineage award. In addition to regular NSF research awards (e.g., CAREER, individual investigator awards, center/institute awards, etc.), Partnerships for Innovation (PFI) and NSF Graduate Research Fellowship Program (GRFP) awards do count as NSF lineage for SBIR/STTR Fast-Track eligibility. NSF Innovation Corps (I-Corps) and NSF SBIR/STTR awards do not count as NSF research lineage and do not convey SBIR/STTR Fast-Track eligibility.
Formal Customer Discovery Eligibility Requirement. Companies must have received formal customer discovery training, defined as follows, within the previous two years from the date of the Fast-Track proposal submission. At least one of the Senior/Key Personnel on the Fast-Track proposal must have undergone formal customer discovery training in relation to the proposed technology via a suitably qualified program, such as the NSF I-Corps program or a program at an incubator or accelerator, with a result that at the start of the Fast-Track project the proposing company has a clear understanding of the product-market fit and initial target customers for the proposed technology.
Complete Team Eligibility Requirement. Companies must have a complete Fast-Track team in place at the time of proposal submission – i.e., there must be no “to-be-determined” company personnel in budget lines A or B; all company personnel in budget lines A and B must have confirmed their availability for the proposed Fast-Track project per the proposed Phase I and Phase II component budgets; the proposing team must possess the required expertise to perform the proposed Fast-Track project; and the team members must dedicate sufficient time to the technical tasks that must be undertaken to achieve the objectives of the Fast-Track project.
In compliance with the CHIPS and Science Act of 2022, Section 10636 (Person or entity of concern prohibition; 42 U.S.C. 19235): No person published on the list under section 1237(b) of the Strom Thurmond National Defense Authorization Act for Fiscal Year 1999 (Public Law 105-261; 50 U.S.C. 1701 note) or entity identified under section 1260h of the William M. (Mac) Thornberry National Defense Authorization Act for Fiscal Year 2021 (10 U.S.C. 113 note; Public Law 116-283) may receive or participate in any grant, award, program, support, or other activity under the Directorate for Technology, Innovation, and Partnerships.
Individuals who are a current party to a Malign Foreign Talent Recruitment Program are not eligible to serve as a Senior/Key Person on an NSF proposal or on any NSF award made after May 20, 2024. See current PAPPG for additional information on required certifications associated with Malign Foreign Talent Organization. The Authorized Organizational Representative (AOR) must certify that all individuals identified as Senior/Key Personnel have been made aware of and have complied with their responsibility under that section to certify that the individual is not a party to a Malign Foreign Talent Recruitment Program.
The small business concern’s R&D must be performed within the United States. Startups and small businesses funded by NSF must be majority U.S.-owned companies.
The companies may not be majority-owned by one or more venture capital operating companies (VCOCs), hedge funds, or private equity firms. Proposals from joint ventures and partnerships are permitted, provided the proposing entity qualifies as a small business concern (see Guide to SBIR/STTR Program Eligibility for more information).
“Collaborative Proposal from Multiple Organizations” (a special proposal type in Research.gov) are not allowed.
Socially and economically disadvantaged small businesses and women-owned small businesses are also encouraged to apply.
Who May Serve as PI:

The primary employment of the Principal Investigator (PI) must be with the small business concern at the time of award and for the duration of the award, unless a new PI is approved by NSF. Primary employment is defined as at least 51 percent employed by the small business. NSF normally considers a full-time work week to be 40 hours and considers employment elsewhere of greater than 19.6 hours per week to be in conflict with this requirement. The PI must have a legal right to work for the proposing company in the United States, as evidenced by citizenship, permanent residency, or an appropriate visa. The PI does not need to be associated with an academic institution. There are no PI degree requirements (i.e., the PI is not required to hold a Ph.D. or any other degree). A PI must devote a minimum of three calendar months of effort per six months of performance to an NSF SBIR/STTR Fast-Track project.

Limit on Number of Proposals per Organization: 1

An organization must wait for a determination from NSF (e.g., award, decline, or returned without review) regarding a pending NSF SBIR/STTR Fast-Track pilot proposal before submitting a new Project Pitch in the next window.

An organization that has submitted a traditional SBIR/STTR Project Pitch, received an invitation to submit a traditional SBIR/STTR Phase I proposal, or has a traditional SBIR/STTR Phase I proposal under review may not submit a Fast-Track Project Pitch until either the traditional SBIR/STTR Project Pitch has been declined (i.e., not invited) or the outcome of the invited traditional SBIR/STTR proposal submission has been made available to the organization.

Proposals that have been Returned Without Review may be submitted using the same Project Pitch invitation (assuming that the proposal is received within 4 months of the original invitation).

Limit on Number of Proposals per PI or co-PI: 1

For NSF SBIR Fast-Track – 1 PI, co-PIs are not allowed.

For NSF STTR Fast-Track - 1 PI and 1 Co-PI are required (the PI must be an employee of the proposing small business and the Co-PI must be part of the STTR partner research institution). An individual may be listed as the PI for only one proposal submitted at a time to the NSF SBIR/STTR programs (including traditional and Fast-Track).

For NSF STTR Fast-Track proposals, a person may act as co-PI on an unlimited number of proposals.

Additional Eligibility Info:

Required Project Pitch Invitation: Potential proposers must receive an invitation to submit a full NSF SBIR/STTR Fast-Track pilot proposal. Please see Project Pitch website for details.

STTR Research Institution. The SBIR/STTR Policy Directive requires that STTR proposals include an eligible research institution as a subawardee on the project budget. The STTR partner research institution is typically either a not-for-profit institution focused on scientific or educational goals (such as a college or university), or a Federally Funded Research and Development Center (FFRDC). For an NSF STTR Fast-Track proposal, a minimum of 40% of the research, as measured by the budget, must be performed by the small business concern, and a minimum of 30% must be performed by a single partner research institution, with the balance permitted to be allocated to either of these, or to other subawards or consultants.

Partnering. Proposing companies are encouraged to collaborate with experienced researchers at available facilities such as colleges, universities, national laboratories, and from other research sites. Funding for such collaborations may include research subawards or consulting agreements. The employment of faculty and students by the small business is allowed, however:

For an NSF SBIR Fast-Track proposal, a minimum of two-thirds of the research, as measured by the budget, must be performed by the small business during the Phase I component of the project, and a minimum of one-half of the research, as measured by the budget, must be performed by the small business during the Phase II component of the project. The balance of the budget may be outsourced to subawards or consultants or a combination thereof. The proportion requirements cited above must be met in both the Phase I and Phase II budgets independently.
For an NSF STTR Fast-Track proposal, the SBIR/STTR Policy Directive requires proposals to include an eligible research institution as a subawardee on the project budget. The institution is typically either a not-for-profit institution focused on scientific or educational goals (such as a college or university), or a Federally funded research and development center (FFRDC). A minimum of 40% of the research, as measured by the budget, must be performed by the small business. A minimum of 30% must be performed by a single partner research institution. The balance (remaining 30%) may be allocated to the small business, partner research institution, or to other subawards or consultants. The percentage requirements cited above must be met in both the Phase I and Phase II budgets independently.
For Both SBIR and STTR Fast-Track proposals, proposals should NOT be marked as a "Collaborative Proposal from Multiple Organizations" during submission.
Companies are allowed to switch between SBIR and STTR, and vice versa, as they transition from Phase I to Phase II.
Government-Wide Required Benchmarks (applies to previous SBIR/STTR recipients only):

Phase I to Phase II Transition Rate Benchmark. For Phase I proposers that have received more than 20 Phase I SBIR/STTR awards from any federal agency over the past five fiscal years, the minimum Phase I to Phase II Transition Rate over that period is 25%. Small businesses that fail to meet this transition requirement will be notified by the Small Business Administration and will not be eligible to submit a Phase I proposal for one (1) year.
Commercialization Benchmark (applies to previous SBIR/STTR recipients only). The commercialization benchmark required by the SBIR/STTR Reauthorization Act of 2011 only applies to proposers that have received more than 15 Phase II Federal SBIR/STTR awards over the past 10 fiscal years, excluding the last two years. These companies must have achieved the minimum required commercialization activity to be eligible to submit a Phase I proposal, as determined by the information entered in the company registry, see Completing the Company Registry Commercialization Report: Instructions and Definitions.
For more information, see Performance Benchmark Requirements.
V. Proposal Preparation And Submission Instructions
A. Proposal Preparation Instructions
Full Proposal Instructions: Proposals submitted in response to this program solicitation should be prepared and submitted in accordance with the guidelines specified in the NSF Proposal & Award Policies & Procedures Guide (PAPPG). The complete text of the PAPPG is available electronically on the NSF website at: https://www.nsf.gov/publications/pub_summ.jsp?ods_key=pappg. Paper copies of the PAPPG may be obtained from the NSF Publications Clearinghouse, telephone (703) 292-8134 or by e-mail from nsfpubs@nsf.gov.

See PAPPG Chapter II.D.2 for guidance on the required sections of a full research proposal submitted to NSF. Please note that the proposal preparation instructions provided in this program solicitation may deviate from the PAPPG instructions.

This solicitation contains MANY instructions that deviate from the standard NSF PAPPG proposal preparation instructions. This solicitation contains the information needed to prepare and submit a proposal and refers to specific sections of the PAPPG ONLY when necessary (and noted throughout the solicitation). In the event of conflict between the instructions in this solicitation and the PAPPG, use this solicitation's instructions as a guide.

The following project activities are not responsive to the solicitation:

Evolutionary development or incremental modification of established products or proven concepts;
Straightforward engineering or test and optimization efforts that are not hypothesis driven;
Evaluation or testing of existing products;
Basic scientific research or research not connected to any specific market opportunity or potential new product;
Business development, market research, and sales and marketing;
Clinical trials;
Research or commercialization pathways involving chemical components, natural or synthetic variations thereof, or other derivatives related to Schedule I controlled substances; or
Non-profit business concerns.
Non-responsive proposals may be returned without review.

An NSF SBIR/STTR Fast-Track pilot proposal that is Returned Without Review as being not responsive to the solicitation may be significantly revised and submitted for the next deadline if the proposal is still within the timeframe for eligible submission.

Required Project Pitch submission: To submit a full NSF SBIR/STTR Fast-Track proposal, potential proposers must first submit a Project Pitch and receive an invitation. The Project Pitch gives NSF the ability to review for appropriateness to the NSF STTR/STTR Fast-Track programs prior to the full proposal submission process, ensuring that proposers do not expend time or resources preparing full proposals that are not aligned with the program requirements. To start this process, proposers must first create a log-in and submit a Project Pitch via the NSF SBIR/STTR Fast-Track Project Pitch online form. NSF SBIR/STTR program staff will use the Project Pitch to determine whether the proposed project is a good fit for the program objectives.

All NSF SBIR/STTR Fast-Track Project Pitches MUST be submitted to “Fast-Track” using the drop-down on the site and MUST nominate the most appropriate technical topic area from the list,
Proposers may submit a Project Pitch at any time, regardless of the NSF SBIR/STTR Fast-Track pilot solicitation window.
Proposers must include their prior NSF award number (NSF lineage) in the Project Pitch.
When submitting an SBIR/STTR Fast-Track proposal in Research.gov, you must enter your invited SBIR/STTR Fast-Track Project Pitch Number in the SBIR/STTR Fast-Track Questionnaire. The Phase I award number must be validated before you can continue with the proposal preparation.
REQUIRED REGISTRATIONS: Small businesses applying for NSF SBIR/STTR Fast-Track funding must be registered in the following systems in order to submit a proposal to NSF. The registrations below can take several weeks or even months to process, so please start early.

You must register your company name, physical address, and all other identifying information identically in each of these systems. We recommend that you register your small business in the following order:

System for Award Management (SAM) Registration. You MUST register to do business with the U.S. government through SAM. When you register, you will have to share bank account information of the account where the NSF funds would be deposited. This registration process is free and must be renewed annually. An active SAM.gov registration and its associated SAM.gov Unique Entity Identifier (UEI) is needed to create a Research.gov account and submit a proposal to NSF. To submit proposals to NSF SBIR/STTR, you only need to request "financial assistance" authority and do NOT need "contract" authority (which can be a much longer process to obtain).
NSF will validate that each proposer’s UEI and SAM registration are valid and active prior to allowing submission of a proposal to NSF. If a registration is not active, an organization will not be able to submit a proposal. Additionally, if the SAM registration is not renewed annually and is not valid, NSF will block any award approval actions.
Any subawardees or subcontractors are also required to obtain a UEI and register in Research.gov. Entities can obtain a SAM UEI without full SAM registration. If you have a subrecipient that is not fully registered in SAM, but has been assigned a UEI number, please call the IT Help desk for further assistance.
Small Business Administration (SBA) Company Registration. A Small Business Concern Identification number (SBC ID) is required prior to submission of the proposal. SBA maintains and manages the Company Registry for SBIR/STTR proposers in order to track ownership and affiliation requirements. All SBCs must report ownership information prior to each SBIR/STTR proposal submission and update the SBC if any information changes prior to award. This registration process is free.
Research.gov. Research.gov is NSF’s online grant management system – how you submit your proposal. For more information, consult the "About Account Management" page. This registration process is free.
Beware of scammers charging fees for SAM and/or SBA registrations.

B. Tips on the Proposal Preparation and Submission

It is suggested that you create a single PDF document for each section of the proposal, aggregate those PDF documents into a single file joining the various sections, then upload this single PDF to Research.gov. This will avoid issues resulting from Research.gov conversion to PDF formats.

Submit a complete proposal:

Cover Sheet
SBIR (or STTR) Fast-Track Questionnaire
SBIR (or STTR) Fast-Track Certification Questions
Project Summary
Project Description
References Cited
Budget(s) (and Subaward Budget(s), if needed)
Budget Justification(s) (and Subaward Budget Justification(s), if needed)
Facilities, Equipment and Other Resources
Senior/Key Personnel Documents
Biographical Sketch
Current and Pending (Other) Support
Collaborations and Other Affiliations (Single Copy Document)
Synergistic Activities
Data Management and Sharing Plan
Mentoring Plan (Conditionally required)
Project Schedule
Letter(s) of Support (Required)
IP (Intellectual Property) Rights Agreement (Required for STTR proposals and strongly recommended for SBIR proposals when there is a subaward to another institution)
Other Personnel Biographical Information
Other Supplementary Documents
List of Suggested Reviewers (Single Copy Document)
List of Reviewers Not to Include (Single Copy Document)
Deviation Authorization (Single Copy Document)
Additional Single Copy Documents
DO NOT upload information beyond what is specifically required and permitted into the proposal (e.g., do not include marketing materials, research results, academic papers, patent applications, etc.).

DO NOT include samples, videotapes, slides, appendices, or other ancillary items within a proposal submission. Websites containing demonstrations and Uniform Resource Locators (URLs) (if applicable) must be cited in the References Cited section. Note: reviewers are not required to access any information outside the proposal document. Please refer to the NSF PAPPG (Chapter II.C) for more details on accepted proposal fonts and format.

C. Detailed Instructions on Proposal Preparation

Full Proposal Set-up: In Research.gov, complete the following steps:

Select "Prepare & Submit Proposals,” “Letters of Intent and Proposals”
Select “Prepare New” and from the pull down “Full Proposal.”
Funding Opportunity. Either filter by “SBIR” or “STTR” or “Fast-Track”, and select radio button for the NSF SBIR/STTR Fast-Track Pilot Programs.
Where to Apply. Select program: SBIR Fast-Track or STTR Fast-Track.
Proposal Type: Select SBIR or STTR.
Proposal Details: Answer questions:
Is your organization a sole proprietorship? Yes or No
Enter Proposal Title, then click on Prepare Proposal
You will now be on a new proposal page – Select Due Date (upper right corner)
Cover Sheet. The Cover Sheet requests general information about the proposal and proposing organization.

Other Federal Agencies (if applicable). If this proposal is being submitted to other Federal agencies, state or local governments, or non-governmental entities, enter a reasonable abbreviation, up to 10 characters, for each agency or entity. Only the first 5 agencies you enter will appear on the PDF version of the proposal, but all should be entered below. IT IS ILLEGAL TO ACCEPT DUPLICATE FUNDING FOR THE SAME WORK. IF A PROPOSER FAILS TO DISCLOSE EQUIVALENT OR OVERLAPPING PROPOSALS, THE PROPOSER COULD BE LIABLE FOR ADMINISTRATIVE, CIVIL, AND/OR CRIMINAL SANCTIONS.

Human Subjects (if applicable). According to 45 CFR 46, a human subject is "a living individual about whom an investigator (whether professional or student) conducting research:

Obtains information or biospecimens through intervention or interaction with the individual, and uses, studies, or analyzes the information or biospecimens; or
Obtains, uses, studies, analyzes, or generates identifiable private information or identifiable biospecimens.”
NIH provides a Decision Tool to assist investigators in determining whether their project involves non-exempt human subjects research, meetings the criteria for exempt human subjects research, or does not involve human subjects research.

Projects involving research with human subjects must ensure that subjects are protected from research risks in conformance with the relevant Federal policy known as the Common Rule (Federal Policy for the Protection of Human Subjects, 45 CFR 690). All projects involving human subjects must either (1) have approval from an Institutional Review Board (IRB) before issuance of an NSF award; or (2) must obtain a statement from the IRB indicating research exemption from IRB review; or 3) must obtain a just in time IRB designation and documentation. This documentation needs to be completed during due diligence discussions, in accordance with the applicable subsection, as established in section 101(b) of the Common Rule. If certification of exemption is provided after submission of the proposal and before the award is issued, the exemption number corresponding to one or more of the exemption categories also must be included in the documentation provided to NSF. The small business has three basic options with regard to human subjects review:

Establish your own IRB (see Office for Human Research Protections (OHRP) at the Department of Health and Human Services (HHS): https://www.hhs.gov/ohrp/irbs-and-assurances.html#registernew.
Use the review board of a (usually local) university or research institution, either via consultants to the project, a project subaward, or directly through its own contacts;
Use a commercial provider.
For projects lacking definite plans for the use of human subjects, their data, or their specimens, pursuant to 45 CFR § 690.118, NSF can accept a determination notice that establishes a limited time period under which the PI may conduct preliminary or conceptual work that does not involve human subjects. See more information and instructions regarding this documentation in the PAPPG.

Live Vertebrate Animals (if applicable). Any project proposing use of vertebrate animals for research or education shall comply with the Animal Welfare Act (7 USC 2131, et seq.) and the regulations promulgated thereunder by the Secretary of Agriculture (9 CFR 1 .1 -4.11) pertaining to the humane care, handling, and treatment of vertebrate animals held or used for research, teaching or other activities supported by Federal awards.

In accordance with these requirements, proposed projects involving use of any vertebrate animal for research or education must be approved by the submitting organization's Institutional Animal Care and Use Committee (IACUC) before an award can be made. For this approval to be accepted by NSF, the organization must have a current Public Health Service (PHS) Approved Assurance. See also PAPPG for additional information on the administration of awards that utilize vertebrate animals. This documentation must be completed before issuance of an NSF award.

SBIR (or STTR) Fast-Track Questionnaire. The SBIR/STTR Fast-Track Questionnaire MUST be filled in completely including Topic and Subtopic, Project Pitch Number, Authorized Company Officer Information, Proposing Small Business Information, SBIR/STTR Award History, Affiliated Companies, and Other Information (including NSF Funding Lineage).

Other Information.

Proprietary Information. To the extent permitted by law, the Government will not release properly identified and marked technical and commercially sensitive data.

If the proposal does not contain proprietary information, uncheck the box in the Phase I Questionnaire.

If the proposal does contain proprietary information identify the proprietary technical data by clearly marking the information and also providing a legend. NSF SBIR/STTR data, including proposals, are protected from disclosure by the participating agencies for not less than 20 years from the delivery of the last report or proposal associated with the given project. Typically, proprietary information is identified in the text either with an asterisk at the beginning and end of the proprietary paragraph, underlining the proprietary sections, or choosing a different font type. An entire proposal should not be marked proprietary.

For Statistical Purposes. Please check all of the appropriate boxes and fill in award numbers as needed.

SBIR (or STTR) Fast-Track Certification Questions. The Fast-Track Certification Questions MUST be filled in completely.

Project Summary. One (1) page MAXIMUM]. The Project Summary should be written in the third person, informative to other persons working in the same or related fields, and insofar as possible, understandable to a scientifically or technically literate lay reader. It should not be an abstract of the proposal. Do not include proprietary information in the summary.

The Project Summary is completed in Research.gov by entering information into the three text boxes in the Project Summary. To be valid, a heading must be on its own line with no other text on that line.

Overview: Describe the potential outcome(s) of the proposed activity in terms of a product, process, or service. Provide a list of key words or phrases that identify the areas of technical expertise to be invoked in reviewing the proposal and the areas of application that are the initial target of the technology. Provide the subtopic name.
Intellectual Merit: This section MUST begin with “This Small Business Innovation Research (or Small Business Technology Transfer) Fast-Track project...” Address the intellectual merits of the proposed activity. Briefly describe the technical hurdle(s) that will be addressed by the proposed R&D (which should be crucial to successful commercialization of the innovation), the goals of the proposed R&D, and a high-level summary of the plan to reach those goals.
Broader Impacts and Commercial Potential: Discuss the expected outcomes in terms of how the proposed project will bring the innovation closer to commercialization under a sustainable business model. In this box, also describe the potential commercial and market impacts that such a commercialization effort would have, if successful. Also discuss potential broader societal and economic impacts of the innovation (e.g., educational, environmental, scientific, societal, or other impacts on the nation and the world).
Project Description. Ten (10) pages MINIMUM and fifteen (15) pages MAXIMUM). The project description is the core of the proposal document, where the PI convinces the expert reviewers/panelists and NSF SBIR/STTR Fast-Track Program Officer that their proposed R&D project meets NSF’s criteria for Intellectual Merit, Broader Impacts, and Commercialization Potential. Note: The incorporation of URLs or websites within the Project Description is not acceptable and the proposal may not be accepted or will be Returned without Review.

The Project Description for a Fast-Track proposal is divided into the following sections:

Fast-Track Phase I R&D Plan – 4 pages MAXIMUM; duration between 6 months and 12 months (specified by the proposing small business).
Succinctly describe the proposed technical innovation, highlighting those aspects that are innovative and transformative relative to the current state of the art. Describe the innovation in sufficient technical detail for a knowledgeable reviewer to understand why it is innovative and how it can provide benefits in the target applications.
Describe the primary technical risks associated with developing the proposed innovation and the key technical objectives to be accomplished during Phase I, clearly explaining why these technical objectives are commercially relevant.
Provide an R&D plan to achieve the key Phase I technical objectives, along with a corresponding timeline. The R&D plan must leverage fundamental science or engineering research and techniques. Associated with this R&D plan, provide a set of clear, quantitative Phase I technical performance targets. Note that these performance targets, if met, must be sufficient to establish or strongly suggest technical viability of the proposed technology, although it is recognized that substantial further development work will likely be needed to generate a commercial product or service.
If the project involves subawards, explain why the subawardee(s) is(are) appropriate partners and describe the intended outcomes of the subawards.
Fast-Track Phase II R&D Plan – 5 pages MAXIMUM; duration between 18 months and 24 months (specified by the proposing small business)
Describe the technical performance metrics that you will need to achieve in order to develop (i) a minimum viable product or service, and (ii) a first-generation commercial-grade product or service. Describe the intended technical outcomes of the Phase II component of the project in terms of these two stages of development, clearly explaining how far you plan to progress towards a commercial solution during Phase II.
Describe the major non-commercial hurdles that will need to be overcome to achieve the above Phase II technical outcomes.
Provide a detailed R&D plan to transition the Phase I results into the intended Phase II technical outcomes described above, along with a corresponding timeline.
Clearly describe any security and privacy practices or standards, regulatory requirements, or other industry standards or practices that the proposed technology will need to comply with in order to be widely adopted and explain how you will ensure that the technology is compliant.
Discuss manufacturing/production, deployment/distribution, and technical scalability of the proposed solution.
If the project involves subawards, explain why the subawardee(s) is(are) appropriate partners and describe the intended outcomes of the or subawards.
Company and Team – 1 page MAXIMUM
Explain the motivation for the company in proposing this project.
Provide a concise description of the relevant qualifications, experience, and expertise of the company founders and the Senior/Key Personnel on the proposed project.
Describe your vision for the company and the company's expected impact over the next five years.
Describe any existing company operations and explain how the proposed effort would fit into these activities.
Provide the revenue and funding history of the company. Include and explicitly indicate any government funding (federal, state, or local) and private investment.
Describe the expertise and contributions to the project of any consultants that you proposed to engage during the project.
Describe how you expect to expand the team going into Phase II and present a rationale for the team changes relative to Phase I. In your response include a discussion of Phase II team members who will not be supported by NSF funds.
Commercialization Plan – 5 pages MAXIMUM. The Commercialization Plan is a critical section of the proposal. It is the primary opportunity to describe the strategy that the small business will employ to generate revenue from the proposed innovation research. The Commercialization Plan is the company's roadmap and should convey how the company will generate profits from its innovation. It should represent a compelling vision of a unique business opportunity.
Describe the target market (including the size and geography of the target market) and initial target customer(s), with examples where possible.
Describe results of ongoing customer discovery activities to date. Provide supporting data if possible.
Clearly describe the proposed product or service, and how it will be delivered to the target customers.
Clearly describe the value proposition.
Describe the proposed commercialization and monetization models. Provide a pricing model with supporting evidence.
Discuss commercial scalability of the proposed solution.
Describe the competition and explain how your company will build a sustainable competitive advantage.
Describe the company’s intellectual property strategy and provide a current status.
Present a financing plan to bring the company to profitability and explain how you will enact this plan.
Provide a 5-year pro-forma, with underlying assumptions and supporting evidence for the assumptions. Be sure to include a detailed breakdown of expected revenues, cost of goods sold, and company expenses.
Broader Impacts – 1 page MAXIMUM
Describe how the proposed product or service offers the potential for broader societal impacts as well as economic benefit (through commercialization under a sustainable business model). Examples of such outcomes may include (but are not limited to) those found in the American Innovation and Competitiveness Act (P.L. 114-329, Section 102) Broader Impacts Review Criterion.
The NSF SBIR/STTR Fast-Track pilot programs fund the development of new, high-risk technology innovations intended to generate positive societal outcomes. Discuss the envisioned broader impacts and the specific implementation plan, including: the relevant metrics and measurement plan; potential partners; potential risks and associated mitigation strategies; and additional anticipated needs for resources and the plan to secure them.
References Cited. Provide a comprehensive listing of relevant references, including websites or relevant URLs, patent numbers, and other relevant intellectual property citations. If there are no references, include a statement to that effect.

Budget(s) and Budget Justification(s). Proposers are required to submit budgets with their proposals, including specific dollar amounts by budget category. Proposers must submit a written justification explaining these amounts in detail. NSF SBIR/STTR Fast-Track Program Officers review these proposed budgets and rely on them in determining the final amount awarded for a given SBIR/STTR Fast-Track project. Enter budget figures for each project year into Research.gov. The system will automatically generate a cumulative budget for the entire project.

Detailed documentation of all budget line items is required and MUST be documented in detail on the Budget Justification. The budget should reflect the needs of the proposed R&D project. The maximum total budget shall not exceed $1,555,000: $400,000 for the Phase I component and $1,155,000 for the Phase II component.

IMPORTANT: The budget and budget justification for the Phase I component of the proposed SBIR/STTR Fast-Track project must be uploaded to the year 1 budget in Research.gov, while the Phase II component of the proposed Fast-Track project must be uploaded to the year 2 and year 3 budget in Research.gov.

The Budget Justification must be uploaded to the Research.gov Budget as a single PDF with two distinct sections – one section for the Phase I component of the Fast-Track project budget and one for the Phase II component. For each component, provide details for each non-zero line item of the budget, including a description and cost estimates. Identify each line item by its letter (e.g., A. Senior/Key Personnel). There is a five-page limit for the Budget Justification. Each Subaward Budget Justification, where required, also has a five-page limit. Additional information to help prepare your proposal budget is available here. The Budget Justification must also clearly state the expected duration of the corresponding Phase I or Phase II project component.

You can add Subaward Organization(s) to your proposal (required for STTR submissions and allowed for SBIR submissions), and make changes to personnel information by navigating to the Budget “Manage Personnel and Subaward Organizations” tab.

All activities on an NSF SBIR/STTR Fast-Track pilot project, including services that are provided by consultants, must be carried out in the United States ("United States" means the 50 states, the territories and possessions of the U.S. Federal Government, the Commonwealth of Puerto Rico, the District of Columbia, the Republic of the Marshall Islands, the Federated States of Micronesia, and the Republic of Palau).Based on a rare and unique circumstance, agencies may approve a particular portion of the R/R&D work to be performed or obtained in a country outside of the United States, for example, if a supply or material or other item or project requirement is not available in the United States. The Funding Agreement officer must approve each such specific condition in writing.

Guidelines for the budget and budget justification follows.

Line A – Senior/Key Personnel. List the PI, co-PI (if STTR), and Senior/Key Personnel by name, their time commitments (in calendar months), and the dollar amount requested. Only salaries and wages for employees of the proposing organization should be included on Line A. Research effort is to be estimated in “Months” (1 Month = 173 hours). Months do not include paid time off and represents actual effort that will be dedicated to the project. The PI must be budgeted for a minimum of three calendar months of effort per six months of performance to the proposed NSF SBIR/STTR Fast-Track project.

In the Budget Justification provide the name; title; a brief description of responsibilities for the PI, co-PI (if STTR), and each of the Senior/Key Personnel as well as the annual, monthly, or hourly salary rate; time commitment; and a calculation of the total requested salary.

You can add additional senior/key personnel to your proposal (e.g., for STTR submissions), and make changes to personnel information by navigating to the Budget “Manage Personnel and Subaward Organizations” tab.

The best source for determining an appropriate salary request is the Bureau of Labor Statistics (BLS). In the Budget Justification provide the title; annual, monthly, or hourly salary rate; time commitment; a calculation of the total requested salary; and a description of responsibilities for the PI, co-PI (if STTR), and each of the Senior/Key Personnel.

You can add additional senior/key personnel to your proposal (e.g., for STTR submissions), and make changes to personnel information by navigating to the "Manage Personnel and Subaward Organizations" page.

Line B - Other Personnel. List the number of people, months, and funding for additional personnel: Other Professionals (Technicians, Programmers, etc.), Administrative/Clerical, and/or Other. These personnel must be employed at the proposing company. The budget justification should state individual employee names and titles (to the extent known), expected role in the project, effort in months and annual salary for each person.

Postdoctoral scholars and students (undergraduate and graduate) are generally listed on a subaward budget to a research institution. If they are employees of the company, they may be listed in Line A. Senior/Key Personnel (Line A), or Line B. Other Professionals or Other, as appropriate.

Secretarial/clerical effort is generally included as part of indirect costs. Salaries for secretarial/clerical should be budgeted as a direct cost only if this type of cost is consistently treated as a direct cost in like circumstances for all other project and cost objectives.
Line C - Fringe Benefits. It is recommended that proposers allot funds for fringe benefits here ONLY if the proposer's usual (established) accounting practices provide that fringe benefits be treated as direct costs. If Fringe Benefits are included on Line C, describe what is included in fringe benefits and the calculations that were used to arrive at the amount requested.

Otherwise, fringe benefits should be included in Line I. Indirect Costs.

Line D - Equipment. Equipment is defined as non-expendable, tangible personal property, having a useful life of more than one year and an acquisition cost of $5,000 or more per unit. However, organizations may elect to establish their capitalization threshold as less than $5,000. Equipment should be budgeted consistently with the proposing organization's capitalization policy. Requests should not be made for general purpose or routine equipment that a business conducting research in the field should be expected to have available. The budget justification must explain the need for any equipment and include the item identification/description, vendor identification, quantity, price, and extended amount. The budget justification should also include, as a separate document if needed, pricing documentation (e.g., quotes, invoices, links to online price lists, past purchase orders, etc.) for each budgeted piece of equipment.

Note that the purchase of Equipment may NOT be included in the budget of the Phase I component of a Fast-Track proposal (Year 1), but MAY be included in the budget of the Phase II component of a Fast-Track proposal (Years 2 and 3).

Line E - Travel. NSF requires that the PI budget travel (for the first year of the project only) to attend the NSF SBIR/STTR Awardee Workshop. A good estimate for the Awardee Workshop is $2,000 per person and is limited to $4,000 per year. Other than the Awardee Workshop and funds for Technical And Business Assistance (TABA, see below), all budgeted travel must be directly related to the execution of the research effort. Only domestic travel will be considered.

The Budget Justification must include the purpose for domestic travel and, for each budgeted trip: the destination, purpose of travel, number of days, and the estimated costs for airfare, cab fare, car rental, per diem rates, hotel, and other incidentals. No supporting detail is required for attendance at the Awardee Workshop at $2,000 (or less) per person. If the workshop is organized as virtual only, proposers can (if awarded) reallocate these funds towards other project activities, pending the approval of the cognizant SBIR/STTR Program Officer.

Travel for purposes other than the project R&D effort (e.g., marketing, customer engagements) is not permitted in the NSF SBIR/STTR Fast-Track budget.

Foreign travel expenses are NOT permitted.

Line F - Participant Support Costs. Participant support costs are NOT permitted on an NSF SBIR/STTR Fast-Track budget.

Line G. Other Direct Costs.

Materials and Supplies. Materials and supplies are defined as tangible personal property, other than equipment, costing less than $5,000, or other lower threshold consistent with the policy established by the proposing organization. The Budget Justification should indicate the specifics of the materials and supplies required, including an itemized listing with item/description, vendor, unit cost, quantity, price, and extended amount. Items with a total cost exceeding $5,000 may require pricing documentation (e.g., quote, link to online price list, prior purchase order or invoice) after the proposal is reviewed, as part of the NSF SBIR/STTR Fast-Track Program Officer's due diligence efforts. Please see Section VI. for details.

Publication Costs/Documentation/Distrib. Publication, documentation and distribution costs are not allowed.

Consultant Services. Consultant services include specialized work that will be performed by professionals that are not employees of the proposing small business. All consultant activities must be carried out in the United States (see above).

No person who is an equity holder, employee, or officer of the proposing small business may be paid as a consultant unless an exception is recommended by the cognizant SBIR/STTR Fast-Track Program Officer and approved by the Division Director of Translational Impacts (TI).

The proposal must include a signed agreement (Letter of Commitment) from each consultant confirming the services to be provided (role in the project), primary organizational affiliation, number of days committed to the research effort, availability to provide services, and consulting daily rate. The agreement must clearly state the number of days on the project, the consulting daily rate (8 hours/day) and the total dollar amount of the consulting agreement. Include a copy of the signed Letter of Commitment in the "Other Supplementary Documents" section. Multiple letters should be combined as a single PDF before uploading.

The consulting daily rate represents the total labor compensation for an 8-hour period and may not exceed $1,000 per day. Any miscellaneous costs, such as supplies, that are not included as part of the daily rate must be identified and justified. Consultant travel should be shown under the domestic travel category, Line E, but counts as an outsourcing expense for the purpose of determining whether the small business concern meets the minimum level of effort for an NSF SBIR/STTR proposal. Any information above and beyond the above will be considered not responsive and may be removed from your proposal.

Biographical sketches for each consultant may be requested by the cognizant NSF SBIR/STTR Fast-Track Program Officer after the proposal is reviewed, as part of their due diligence efforts. Please see Section VI. for details.

Computer Services. This line can include funds for fee-for-service computing activities or resources (such as supercomputer time, cloud services, etc.). Any extended line item should be accompanied by pricing documentation (e.g., quote, link to online price list, prior purchase order, or invoice) in the budget justification. Requested services with a total cost exceeding $5,000 may require pricing documentation (e.g., quote, link to online price list, prior purchase order or invoice) after the proposal is reviewed, as part of the NSF SBIR/STTR Fast-Track Program Officer's due diligence efforts.

Subaward(s). Subawards may be utilized when a significant portion of the work is performed by another organization and when the work to be done is not widely commercially available. Work performed by a university or research laboratory is one example of a common subaward.

Subawards require a separate subaward budget and subaward budget justification, in the same format as the main budget. To enter a subaward budget in Research.gov, go to the Budget module tab and add Subaward Organization(s) by opening the “Manage Personnel and Subaward Organizations” tab. Each subawardee will have its own budget pages for each year of the project.

A subawardee research institution partner is mandatory for STTR Fast-Track proposals. Explicitly list who the research partner will be and provide a brief description of the work they will perform. A minimum of 40% of the research, as measured by the budget, must be performed by the small business concern and a minimum of 30% of the research, as measured by the budget, must be performed by a single subawardee research institution, with the balance permitted to be allocated to either of these, or to other subawards or consultants. Subawardees are not permitted to request profit (Line K) as part of their budgets.

The proposing organization's budget justification must discuss the tasks to be performed and how these are related to the overall project. Also discuss any organizational relationships (e.g., common ownership or related parties) between the proposing organization and the subawardee, and the type of subaward contemplated (e.g., fixed price or cost reimbursement).

Subawardees (the institution, not the individual PI or researcher) should also provide a Letter of Commitment that confirms the role of each subaward organization in the project and explicitly states the subaward amount(s). Provide this letter(s) as part of the Other Supplementary Documents.

For NSF SBIR Fast-Track proposals, subaward funds do not count as funds spent by the small business, and the total amount requested for subawards (when added to consultant funds and any other subawards) cannot exceed 1/3 of the total Phase I budget component and cannot exceed 1/2 of the total Phase II budget component.

No significant part of the research or substantive effort under an NSF award may be contracted or otherwise transferred to another organization without prior NSF authorization. The intent to enter into such arrangements should be disclosed in the proposal.

No person who is an equity holder, employee, or officer of the proposing small business may be paid under a subaward unless an exception is recommended by the NSF SBIR/STTR Program Director and approved by the TI Division Director.

Any subrecipients named in the proposal are also required to obtain a SAM UEI and register in Research.gov. Subrecipients named in the proposal, however, do not need to be registered in SAM. Entities can obtain a SAM UEI without full SAM registration. If you have a subrecipient that is not fully registered in SAM, but has been assigned a UEI number, please call the IT Help desk for further assistance.

It is the responsibility of the proposing organization to confirm that submitted subaward budgets have been approved by an Authorized Organizational Representative at the subawardee organization.

An IP (Intellectual Property) Rights Agreement is required for STTR proposals and strongly recommended for SBIR proposals when there is a subaward to another institution. A fully signed agreement is not required for STTR proposals at the initial proposal submission but will be required before a recommendation for an award can be made. Provide this Agreement, as a PDF, as part of the Optional Documents.

Other. This line includes the purchase of routine analytical or other services, or fabricated components from commercial sources. The budget justification must explain the need for the services, provide a description of the services, and give a detailed cost itemization. Any single "other" item with a total cost of $5,000 must be further itemized into smaller costs or supported by pricing documentation (e.g., quote, link to online pricing list, past purchase order) in the budget justification. This detail will be requested as part of the NSF SBIR/STTR Fast-Track Program Officer's due diligence efforts.

SBIR/STTR Fast-Track Technical and Business Assistance (TABA): Proposers are encouraged to include up to $6,500 in the Phase I component budget and up to $50,000 in the Phase II component budget to assist in technology commercialization efforts (as outlined in the current SBIR/STTR Policy Directive and the John S. McCain National Defense Authorization Act for Fiscal Year 2019). Specifically, this funding is for securing the services of one or more third-party service providers that will assist with one or more of the following commercialization activities:

Phase II Commercialization Plan research and preparation
Phase II Broader Impact plan research and preparation
Making better technical decisions on SBIR/STTR Fast-Track projects;
Solving technical problems that arise during SBIR/STTR projects;
Minimizing technical risks associated with SBIR/STTR projects; and
Commercializing the SBIR/STTR product or process, including securing intellectual property protections
If a proposer is not able to identify what commercial assistance may be required at the time of proposal submission, the proposing small business may block up to the maximum allowable amount for TABA activities (as detailed above) on Line G. Other with the understanding that prior to expending funds for these purposes, the recipient will be required to obtain written approval from the cognizant NSF SBIR/STTR Fast-Track Program Officer.

In addition to the above, for the Phase I component of a Fast-Track project only, NSF permits the inclusion of additional funds on the G budget line, as follows. The funds noted below may ONLY be spent on the commercial or business purposes explicitly permitted below. The proposer may budget up to $10,000 as a direct charge on line G.6 of a Phase I component budget for the following specific purposes related to financials and accounting:

Hiring a certified public accountant (CPA) to prepare audited, compiled, or reviewed financial statements;
Hiring a CPA to perform an initial financial viability assessment based on standard financial ratios so the recipient organization would have time to improve their financial position prior to the CAP assessment for the transition to the Phase II component of the Fast-Track project;
Hiring a CPA to review the adequacy of the recipient's project cost accounting system; and/or purchasing a project cost accounting system.
If the proposer elects to budget funds for one of the above purposes, the Budget Justification should include a brief description of the desired use of funds. The use of funds must be approved by the cognizant NSF SBIR/STTR Fast-Track Program Officer prior to award.

Line I - Indirect Costs. Indirect costs are defined as costs that are necessary and appropriate for the operation of the business, but which are not specifically allocated to the NSF SBIR/STTR Fast-Track project. Common indirect cost expenses include legal and accounting expenses, employee health insurance, fringe benefits, rent, and utilities. If the proposing small business has a Federally negotiated rate, please specify the base and rate and include a copy of the negotiated indirect cost rate agreement. If the proposing business has a history of at least two years of stable operation that reflect the costs expected to occur during the execution of the SBIR/STTR award, please base the indirect rate estimate on this historical data (and provide an explanation if the rate is expected to deviate significantly from the rate used in recent years). Instructions for Indirect Cost Rate (IDC) Proposal Submission Procedures can be found here.

Recipients without experience and knowledge of Federal indirect cost rate negotiation and Federal Acquisition Regulation (FAR) Part 31 Cost Principles may want to consider engaging professional services in preparing an IDC proposal.

If the proposing small business has no negotiated rate with a federal agency, and no previous experience with Federal indirect cost rate negotiation, you may claim (without submitting justification) a total amount of indirect costs (inclusive of fringe benefits) either up to 50% of total budgeted salary and wages on the project or equal to 10% de minimis on MODIFIED total direct costs on the project. Modified Total Direct Cost (MTDC): MTDC means all direct salaries and wages, applicable fringe benefits, materials and supplies, services, travel, and up to the first $25,000 of each subaward (regardless of the period of performance of the subawards under the award). MTDC excludes equipment, capital expenditures, charges for patient care, rental costs, tuition remission, scholarships and fellowships, participant support costs and the portion of each subaward in excess of $25,000. Other items may only be excluded when necessary to avoid a serious inequity in the distribution of indirect costs, and with the approval of the cognizant agency for indirect costs.

Note: NSF does not fund Independent Research and Development (IR&D) as part of an indirect cost rate under its awards. See the FAR 31.205-18(a) for more information.

Line K - Fee. The small business fee is intended to be consistent with normal profit margins provided to profit-making firms for R&D work. Up to seven percent (7%) of the total indirect and direct project costs may be requested as a Small Business Fee for the Phase I budget component. Up to ten percent (10%) of the total indirect and direct project costs may be requested as a fee for the Phase II budget component. The fee applies solely to the small business concern receiving the award and not to any other participant in the project. The fee is not a direct or indirect "cost" item and may be used by the small business concern for any purpose, including additional effort under the NSF SBIR/STTR Fast-Track award (and including items on the "Prohibited Expenditures" list below).

Prohibited Expenditures including, but not limited to, Equipment (during the Phase I component), Foreign Travel (during the Phase I and Phase II components), Participant Support Cots, and Publication Costs are not allowable expenditures as either direct or indirect costs. However, these expenses may be purchased from the small business fee funds (Line K).

Budget Revisions. Budget revisions may be requested by the cognizant SBIR/STTR Program Officer. Revised budgets must contain a revised and complete Budget Justification as described above. Revised budgets with budget impact statements that only address revisions are not acceptable for budget processing, see Budget Revision Instructions.

Note: Should the proposal be considered for funding, the NSF SBIR/STTR Program Officer will refer the proposer to the Cost Analysis and Pre-Award Review (CAP) Division’s SBIR/STTR Administrative/Financial Reviews website. Proposing small businesses in this category will be given 10 calendar days to provide CAP the underlying supporting documentation for their budget. The organization should review and understand the CAP documentation requirements as it prepares its budget. Once NSF requests the underlying supporting documentation for the CAP review, proposers will not be given an opportunity to re-budget unsupported costs. Funding will be provided for only the dollar amount that is reasonable and adequately supported. The awarded budget will reflect the supported dollar amount for the proposed effort. Organizations that accept awards at less than the proposed dollar amount may not reduce the effort to be provided; however, organizations may choose to decline award offers.

Facilities, Equipment and Other Resources. Specify the availability and location of significant equipment, instrumentation, computers, and physical facilities necessary to complete the portion of the research that is to be carried out by the proposing firm in the Phase I or Phase II component of a Fast-Track project. Note that purchase of equipment is NOT permitted in the Phase I component of a Fast-Track proposal. If the equipment, instrumentation, computers, and facilities for this research are not the property (owned or leased) of the proposing firm, include a statement signed by the owner or lessor which affirms the availability of these facilities for use in the proposed research, reasonable lease or rental costs for their use, and any other associated costs. Upload images of the scanned statements into this section.

Many research projects require access to computational, data, analysis, and/or visualization resources to complete the work proposed. For projects that require such resources at scales beyond what may be available locally, researchers in all disciplines can apply for allocations for computer or data resources from over two dozen high-performance computational systems via the Advanced Cyberinfrastructure Coordination Ecosystem: Services & Support (ACCESS) program. See cognizant Program Officer or PAPPG for additional details. If a proposer wants to arrange the use of unique or one-of-a-kind Government facilities, a waiver must be obtained from the Small Business Administration to approve such use.

If no equipment, facilities, or other resources are required for this project, a statement to that effect should be uploaded here.

Senior/Key Personnel Documents. For the Principal Investigator (PI), Co-PI, and for each person listed in the “Senior/Key Personnel” section, the four required documents are listed below.

Biographical Sketch(es). All proposals are required to include Biographical Sketches for each PI, co-PI (if STTR), and Senior/Key Personnel (individuals with critical expertise who will be working on the project and are employed at the proposing company or at a subaward organization). Proposers must prepare biographical sketch files using SciENcv (Science Experts Network Curriculum Vitae), which will produce a compliant PDF. Senior/Key Personnel must prepare, save, certify, and submit these documents as part of their proposal via Research.gov.

Full requirements for these documents can be found in the current NSF Proposal and Award Policies and Procedures Guide. Frequently Asked Questions on using SciENcv can be found here.

Current and Pending (Other) Support. This information will provide reviewers with visibility into the potential availability of company personnel during the period of performance if awarded. All PIs, Co-PIs (if STTR), and Senior/Key Personnel must prepare Current and Pending (Other) Support files using SciENcv. Detailed information about the required content is available in the current PAPPG.

For the PI, co-PI (if STTR), and each of the Senior/Key Personnel listed on Line A or B of the budget, please provide the following information, regardless of whether the person will receive salary from the activity:

Name of sponsoring organization.
Total award amount (if already awarded) or expected award amount (if pending) for the entire award period covered (including indirect costs).
Title and performance period of the proposal or award.
Annual person-months (calendar months) devoted to the project by the PI or Senior/Key Personnel.
Please report:

All current and pending support for ongoing projects and proposals (from any source, including in kind support or equity investment), including continuing grant and contract funding.
All current and pending support for ongoing projects and proposals (from any source, including in kind support or equity investment), including continuing grant and contract funding.
Proposals submitted to other agencies. Concurrent submission of a proposal to other organizations will not influence the review of the proposal submitted to NSF.
Upcoming submissions.
The current Phase I proposal is considered "pending" and therefore MUST appear in the Current and Pending Support form for each PI and Senior/Key Personnel.
Collaborators and Other Affiliations (COA) Information (Single Copy Document). This document must be provided for the PI, Co-PI (if STTR) and each Senior/Key Person. This document will not be viewable by reviewers but will be used by NSF to manage the selection of reviewers. Download the required Collaborators and Other Affiliations template and follow the instructions. Detailed information about the required content is available in the current PAPPG. Frequently Asked Questions on COA can be found here.

Synergistic Activities. Each individual identified as a senior/key person must provide a PDF document of up to one-page that includes a list of up to five distinct examples that demonstrates the broader impact of the individual’s professional and scholarly activities that focus on the integration and transfer of knowledge as well as its creation. Examples of synergistic activities may include but are not limited to the training of junior scientists and engineers in innovation and entrepreneurship; the development of new and novel products, tools, and/or services based on deep technologies; broadening participation of groups underrepresented in STEM; service to the scientific and engineering communities outside the individual’s company; and/or participation in the national and/or international commercial market.

Data Management and Sharing Plan. The Data Management and Sharing Plan should include the statement, "All data generated in this NSF SBIR/STTR Fast-Track project is considered proprietary." This single sentence is sufficient to fulfill the Data Management and Sharing Plan requirement, but proposers may add more detail about how the resulting data will be managed, if they desire. The PDF cannot exceed 2 pages.

Mentoring Plan (Conditionally Required). If a proposal requests funding to support postdoctoral scholars or graduate students at a research institution (through a subaward), a Mentoring Plan MUST be uploaded to the system. The mentoring plan must describe the mentoring that will be provided to all postdoctoral scholars or graduate students supported by the project, regardless of whether they reside at the submitting organization or at any subrecipient organization. Describe only the mentoring activities that will be provided to all postdoctoral scholars or graduate students supported by the project. The PDF cannot exceed 1 page.

Individual Development Plans (IDP) for Postdoctoral Scholars and Graduate Students. For each NSF award that provides substantial support to postdoctoral scholars and graduate students, each individual must have an Individual Development Plan, which is updated annually. The IDP maps the educational goals, career exploration, and professional development of the individual. NSF defines “substantial support” as an individual that has received one person month or more during the annual reporting period under the NSF award. Certification that a postdoctoral scholar(s) and/or graduate student(s) has and IDP must be included in the annual and final reports.

Project Schedule. The required Project Schedule must show the estimated duration and timing of major project tasks that are required to implement the research plan. This document should clearly estimate the initiation and completion of tasks in relation to other tasks within the timeline of the award.

NSF recommends downloading the Project Schedule template and uploading a completed version of this form into Research.gov. This schedule should also provide projected levels of effort for each key person during each reporting period of the project. Key personnel to be listed generally include any senior/key personnel listed on Line A of the main project budget, any persons listed on Line A of any subaward budgets, or any budgeted consultants. The schedule should also include estimates of total level of effort (for all project personnel) and total expenditures for each six-month project period.

Optional. NOTE: Various subsections are REQUIRED depending on the type of proposal (SBIR or STTR), whether the company has a commercialization history, whether this proposal is a resubmission, etc. Please read section requirements carefully.

Letter(s) of Support (REQUIRED). Three (3) Letters of Support from potential product/service users or customers are required; Up to five (5) Letters of Support may be included. All Letters of Support should be uploaded in Research.gov in one PDF.

Letters of Support should address market validation for the proposed innovation, market opportunity, or small business/team, and add significant credibility to the proposed effort. These Letters should ideally demonstrate that the company has developed partnerships and/or a meaningful dialog with relevant stakeholders (e.g., potential customers, strategic partners, or investors) for the proposed innovation and that a real business opportunity may exist. The Letters of Support must contain affiliation and contact information for the signatory stakeholder.

Letters of commitment and supporting documents from consultants and subawards (or any personnel identified in the Budget Justification) are NOT considered letters of support.

IP (Intellectual Property) Rights Agreement (Required for STTR and strongly recommended for SBIR proposals when there is a subaward to another institution). A fully signed Allocation of Intellectual Property Rights is not required at the initial proposal submission but will be required before a recommendation for an award can be made. For proposal submission, place a draft of the Allocation of Intellectual Property Rights or a letter that includes the name of the partner research institution stating that an agreement will be provided upon Program Officer notification of a potential award recommendation.

The SBIR/STTR Policy Directive indicates: “The model (IP) agreement will direct the parties to, at a minimum:

State specifically the degree of responsibility, and ownership of any product, process, or other invention or Innovation resulting from the cooperative research. The degree of responsibility shall include responsibility for expenses and liability, and the degree of ownership shall also include the specific rights to revenues and profits.
State which party may obtain United States or foreign patents or otherwise protect any inventions resulting from the cooperative research.
State which party has the right to any continuation of research, including non-STTR follow-on awards.”
Other Personnel Biographical Information (Strongly Recommended). This section can be used to provide additional biographical information about project participants who are not listed as Senior/Key Personnel for the small business or for a subawardee as well as for writers of Letters of Support. Biographical sketches should be prepared using SciENcv and uploaded as a single PDF.

Other Supplementary Documents. The required other supplementary documents of an NSF SBIR/STTR Phase II proposal are limited to the following (if applicable).

Company Commercialization History (required if the proposer has received any prior SBIR or STTR Phase II awards). This section is required for any proposer who has ever received a Phase II SBIR or STTR award (from any Federal agency). All items MUST be addressed in the format given in the NSF Commercialization History Template. Changes to the NSF template, additional narratives and/or commercialization history documents from other agencies are not permitted.
Letters of Commitment from Subawardees and Consultants (Required, but may be provided in post-award diligence). Please refer to Budget and Budget Justification for details.
List of Suggested Reviewers (Single Copy Document). This section can be used to suggest the names of reviewers who might be appropriate to assess the technical and commercial merits of the proposal. Reviewers who have significant personal or professional relationships with the proposing small business or its personnel should generally not be included.

List of Reviewers Not to Include (Single Copy Document).This section can be used by the proposer to suggest names (or even specific affiliations) of reviewers/panelists not to be involved in the review of their proposal.

Deviation Authorization (Single Copy Document).This section should generally not be used unless NSF staff have specifically instructed the proposer to do so.

Additional Single Copy Documents. This section should be blank.

B. Budgetary Information
Cost Sharing:

Inclusion of voluntary committed cost sharing is prohibited.

Other Budgetary Limitations:

Other budgetary limitations apply. Please see the full text of this solicitation for further information.

C. Due Dates
Full Proposal Deadline(s) (due by 5 p.m. submitting organization’s local time):

     September 18, 2024

     November 06, 2024

     March 05, 2025

     July 02, 2025

     November 05, 2025

Proposers are required to prepare and submit all proposals for this solicitation via Research.gov. Detailed instructions regarding the technical aspects or proposal preparation and submission via Research.gov are available at: https://www.research.gov/research-portal/appmanager/base/desktop?_nfpb=true&_pageLabel=research_node_display&_nodePath=/researchGov/Service/Desktop/ProposalPreparationandSubmission.html. For Research.gov user support, call the Research.gov Help Desk at 1-800-673-6188 or e-mail rgov@nsf.gov. The Research.gov Help Desk answers general technical questions related to the use of the Research.gov system. Specific questions related to this program solicitation should be referred to the NSF program staff contact(s) listed in Section VIII of this funding opportunity.

D. Research.gov Requirements
Proposers are required to prepare and submit all proposals for this program solicitation through use of the NSF Research.gov system. Detailed instructions regarding the technical aspects of proposal preparation and submission via Research.gov are available at: https://www.research.gov/research-web/content/aboutpsm. For Research.gov user support, call the Research.gov Help Desk at 1-800-381-1532 or e-mail rgov@nsf.gov. The Research.gov Help Desk answers general technical questions related to the use of the Research.gov system. Specific questions related to this program solicitation should be referred to the NSF program staff contact(s) listed in Section VIII of this funding opportunity.

Submission of Electronically Signed Cover Sheets. The Authorized Organizational Representative (AOR) must electronically sign the proposal Cover Sheet to submit the required proposal certifications (see PAPPG Chapter II.C.1.d for a listing of the certifications). The AOR must provide the required electronic certifications at the time of proposal submission. Further instructions regarding this process are available on the Research.gov Website at: https://www.research.gov/research-web/content/aboutpsm.

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

The NSF SBIR/STTR Fast-Track programs have additional criteria that reflect the emphasis on commercialization and complement the standard NSF review criteria listed above. The following elements will be considered in the review of the Commercialization Potential.

Is there a significant market opportunity that could be addressed by the proposed product, process, or service?
Does the company possess a significant and durable competitive advantage, based on scientific or technological innovation, that would be difficult for competitors to neutralize or replicate?
Is there a compelling potential business model?
Does the proposing company/team have the essential elements, including expertise, structure, and experience, that would suggest the potential for strong commercial outcomes?
Will NSF support serve as a catalyst to improve substantially the technical and commercial impact of the underlying commercial endeavor?
NSF SBIR/STTR Fast-Track Award Considerations

An NSF SBIR/STTR Fast-Track proposal includes Phase I and Phase II components. Each component includes an R&D plan and a budget. In addition, the proposal will include a section on the company and team and a section on the Commercialization Plan. Hence, the core of a Fast-Track proposal comprises the following elements:

Phase I R&D Plan
Phase I Budget and Budget Justification
Phase II R&D Plan
Phase II Budget and Budget Justification
The Company and Team
Commercialization Plan
The review of an NSF SBIR/STTR Fast-Track proposal will include a review of both the Phase I and Phase II components of the proposal. A team submitting an NSF SBIR/STTR Fast-Track proposal must have NSF-funded research lineage; an understanding of the target market, product-market fit and initial target customers; and a complete team.

An NSF SBIR/STTR Fast-Track proposal must include specific, quantifiable performance targets for the Phase I component of the project. These Phase I targets may be renegotiated with the cognizant Program Officer during post-review diligence, so that at the start of the Fast-Track project, there will be agreed performance targets in place for the Phase I component.

Due Diligence. Once the panel and/or ad hoc review of an individual NSF SBIR or STTR Fast-Track proposal has concluded and the proposal is considered potentially meritorious, a follow-on due diligence process may be conducted in which the Principal Investigator will be asked to provide additional information and/or to answer questions specific to their proposal in order to inform the final decision. This due diligence process will address weaknesses and questions raised during the external merit review as well as by the cognizant SBIR/STTR Fast-Track Program Officer. The due diligence process may include requests for clarification of the company structure, key personnel, conflicts of interest, foreign influence, cybersecurity practices, or other issues as determined by NSF. Participation in the diligence process is not a guarantee of an award.

Financial Viability. If the small business' proposal is to be further considered for funding after it is competitively reviewed, the cognizant NSF SBIR/STTR Fast-Track Program Officer will refer the proposer to the Cost Analysis and Pre-Award Review (CAP) Administrative/Financial Reviews Site. These reviews are conducted to evaluate a prospective recipient's ability to manage a Federal award responsibly, effectively, and efficiently.

After programmatic approval has been obtained, the proposals recommended for funding will be forwarded to the Division of Grants and Agreements for review of business, financial, and policy implications. After an administrative review has occurred, Grants and Agreements Officers perform the processing and issuance of an award or other agreement. Proposers are cautioned that only a Grants and Agreements Officer may make commitments, obligations, or awards on behalf of NSF or authorize the expenditure of funds. No commitment on the part of NSF should be inferred from technical or budgetary discussions with an NSF Program Officer. A Principal Investigator or organization that makes financial or personnel commitments in the absence of a grant or cooperative agreement signed by the NSF Grants and Agreements Officer does so at their own risk.

The Phase I and Phase II components of a NSF SBIR/STTR Fast-Track proposal will be reviewed and evaluated separately. NSF SBIR/STTR Fast-Track proposals submitted to this solicitation for which the Phase I component is considered meritorious but the Phase II component is not considered meritorious may, based on budgetary considerations and at NSF's discretion, be considered for award as regular NSF SBIR/STTR Phase I projects, in which case (if awarded) the company would subsequently apply for NSF SBIR/STTR Phase II funding via the regular process (i.e., not via the Fast-Track process).

NSF requires each NSF SBIR/STTR Fast-Track recipient company to attend and participate in the NSF SBIR/STTR Phase I Awardees Conference.

Once an award or declination decision has been made, Principal Investigators are provided feedback about their proposals. In all cases, reviews are treated as confidential documents. Verbatim copies of reviews, excluding the names of the reviewers or any reviewer-identifying information, and the panel summary (if a panel summary was prepared) will be available to the proposer via research.gov.

NSF SBIR Phase II proposals submitted to this solicitation which are considered meritorious, and which meet all the requirements of the NSF STTR Phase II program may, based on budgetary considerations and at NSF's discretion, be converted for award as an NSF STTR Phase II project. NSF may also, at its discretion, convert NSF STTR Phase II proposals to NSF SBIR Phase II proposals.

Supplemental Funding. America’s Seed Fund powered by NSF is committed to assisting SBIR/STTR Phase II recipients to successfully commercialize their innovation research, grow their company and create jobs by attracting new investments and partnerships. To reinforce these commitments, the programs support a broad number of supplements and other opportunities. For more information, see: Supplemental Funding Overview, and the linked Dear Colleagues Letters.

Debriefing on Unsuccessful Proposals. As outlined in Chapter IV of the PAPPG, a proposer may request additional information from the cognizant Program Officer or Division Director. Proposers may contact the cognizant Program Officer to set up a date/time for a debrief call.

Resubmission. Declined NSF SBIR/STTR Fast-Track proposals are NOT eligible for resubmission. A proposer of a previously declined proposal must submit a new Project Pitch and, if invited, submit a new proposal after substantial revision, addressing the reviewers’, panel’s (if appropriate), and Program Officer’s concerns.

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

As expressed in Executive Order 14005, Ensuring the Future is Made in All of America by All of America’s Workers (86 FR 7475), it is the policy of the executive branch to use terms and conditions of Federal financial assistance awards to maximize, consistent with law, the use of goods, products, and materials produced in, and services offered in, the United States.

Consistent with the requirements of the Build America, Buy America Act (Pub. L. 117-58, Division G, Title IX, Subtitle A, November 15, 2021), no funding made available through this funding opportunity may be obligated for infrastructure projects under an award unless all iron, steel, manufactured products, and construction materials used in the project are produced in the United States. For additional information, visit NSF’s Build America, Buy America webpage.

Special Award Conditions:

NSF SBIR/STTR Fast-Track awards are subject to the availability of funds. NSF has no obligation to make any specific number of Fast-Track awards based on a solicitation and may elect to make several or no awards under any specific technical topic or subtopic.

The NSF SBIR/STTR Fast-Track fixed amount cooperative agreements will not exceed $1,555,000 per award and normally will be made for a 24-month period of performance.

NSF requires each NSF SBIR/STTR Fast-Track recipient company to attend and participate in the NSF SBIR/STTR Awardees’ Conference.

Terms and Conditions for awards made under this SBIR/STTR Phase II solicitation were posted in May 2024 and are available on the Award Conditions page, under SBIR/STTR Terms and Conditions. The linked page includes "SBIR/STTR Phase II Cooperative Agreement Financial & Administrative Terms and Conditions (SBIR/STTR-II-CA-FATC)" AND "SBIR/STTR Phase II General Terms & Conditions."

The award notice specifies a pre-determined, fixed amount of NSF support for the project described in the referenced proposal. This amount is based upon the budget approved by NSF for the referenced proposal, as amended.

Phase II Transition:

Phase II component funding will be released to the Fast-Track recipient contingent on successfully passing both Stage Gates 1 and 2 of the Phase II Transition Review.

Companies that do not pass either Stage Gate 1 or 2 will be limited to Phase I funding, and the award will conclude at the end of the Phase I component. The final $25,000 will be made available to the company upon submission and NSF approval of the Phase I final project report and upon submission of a Project Outcomes report.

A decision by NSF not to provide additional funding following either the Stage Gate 1 or Stage Gate 2 review will NOT be eligible for reconsideration or termination review as defined in Chapter XII.A.4 of the PAPPG.

Payment Schedule:

Companies that pass both Stage Gates 1 and 2 will receive access to the final $25,000 of Phase I component funding and a funding increment for the Phase II component of the award. Phase II component payments will generally be managed in accordance with the following schedule:

25% Advance Payment.
25% upon acceptance by an NSF SBIR Fast-Track Program Officer of first interim report.
25% upon acceptance by an NSF SBIR Fast-Track Program Officer of second interim report.
The remainder of funds, less $25,000, upon acceptance by an NSF SBIR Fast-Track Program Officer of third interim report.
Final $25,000 upon acceptance by an NSF SBIR Fast-Track Program Officer of a satisfactory final annual project report and upon submission of a Project Outcomes report.
A deviation from the standard payment schedule can be requested if the standard schedule poses significant difficulties for the recipient or would negatively affect the execution of the project. If the standard payment schedule as described above is not appropriate, please request alternative amounts for each payment, and provide a brief justification for the departure from the standard schedule.

Payment of the award amount is subject to compliance with the award terms and conditions and NSF's acceptance of the reports submitted by the recipient. On the basis of its review of these reports and/or other pertinent information, NSF reserves the right to modify the payment schedule or suspend or terminate the award, if NSF determines that such actions are appropriate. If estimated total expenditures are significantly less than the award amount, the recipient shall contact NSF to renegotiate the scope of this award. Similarly, if the recipient expects that the full scope of work will be completed at a total cost significantly lower than the award amount, it is the obligation of the recipient to promptly notify NSF.

C. Reporting Requirements
For all multi-year grants (including both standard and continuing grants), the Principal Investigator must submit an annual project report to the cognizant Program Officer no later than 90 days prior to the end of the current budget period. (Some programs or awards require submission of more frequent project reports). No later than 120 days following expiration of a grant, the PI also is required to submit a final annual project report, and a project outcomes report for the general public.

Failure to provide the required annual or final annual project reports, or the project outcomes report, will delay NSF review and processing of any future funding increments as well as any pending proposals for all identified PIs and co-PIs on a given award. PIs should examine the formats of the required reports in advance to assure availability of required data.

PIs are required to use NSF's electronic project-reporting system, available through Research.gov, for preparation and submission of annual and final annual project reports. Such reports provide information on accomplishments, project participants (individual and organizational), publications, and other specific products and impacts of the project. Submission of the report via Research.gov constitutes certification by the PI that the contents of the report are accurate and complete. The project outcomes report also must be prepared and submitted using Research.gov. This report serves as a brief summary, prepared specifically for the public, of the nature and outcomes of the project. This report will be posted on the NSF website exactly as it is submitted by the PI.

More comprehensive information on NSF Reporting Requirements and other important information on the administration of NSF awards is contained in the NSF Proposal & Award Policies & Procedures Guide (PAPPG) Chapter VII, available electronically on the NSF Website at https://www.nsf.gov/publications/pub_summ.jsp?ods_key=pappg.

VIII. Agency Contacts
Please note that the program contact information is current at the time of publishing. See program website for any updates to the points of contact.

General inquiries regarding this program should be made to:

NSF SBIR/STTR Inbox, telephone: (703) 292-5111, email: sbir@nsf.gov

For questions related to the use of NSF systems contact:

NSF Help Desk: 1-800-381-1532
Research.gov Help Desk e-mail: rgov@nsf.gov
NSF SBIR/STTR Inbox, telephone: (703) 292-5111, email: sbir@nsf.gov

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
The information requested on proposal forms and project reports is solicited under the authority of the National Science Foundation Act of 1950, as amended. The information on proposal forms will be used in connection with the selection of qualified proposals; and project reports submitted by proposers will be used for program evaluation and reporting within the Executive Branch and to Congress. The information requested may be disclosed to qualified reviewers and staff assistants as part of the proposal review process; to proposer institutions/grantees to provide or obtain data regarding the proposal review process, award decisions, or the administration of awards; to government contractors, experts, volunteers and researchers and educators as necessary to complete assigned work; to other government agencies or other entities needing information regarding proposers or nominees as part of a joint application review process, or in order to coordinate programs or policy; and to another Federal agency, court, or party in a court or Federal administrative proceeding if the government is a party. Information about Principal Investigators may be added to the Reviewer file and used to select potential candidates to serve as peer reviewers or advisory committee members. See System of Record Notices, NSF-50, "Principal Investigator/Proposal File and Associated Records," and NSF-51, "Reviewer/Proposal File and Associated Records.” Submission of the information is voluntary. Failure to provide full and complete information, however, may reduce the possibility of receiving an award.

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
        