
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
        NSF 23-615: Division of Physics: Investigator-Initiated Research Projects (PHY)
Program Solicitation

**Document Information**
- **Posted:** August 11, 2023
- **Replaces:** NSF 21-593
- **Download the solicitation:** [PDF, 0.9mb](#)
- **View the program page:** [Link](#)

**NSF Logo**  
**National Science Foundation**  
**Directorate for Mathematical and Physical Sciences**  
**Division of Physics**

**Full Proposal Deadline(s) (due by 5 p.m. submitter's local time):**
- **November 20, 2023**
  - Third Monday in November, Annually Thereafter
- **Plasma Physics - Refer to Solicitation for Applicable Deadline**
  - November 22, 2023
  - Fourth Wednesday in November, Annually Thereafter
- **AMO - Theory and Experiment; Gravitational Physics - Theory and Experiment; LIGO Research Support; Integrative Activities in Physics - Refer to Solicitation for Applicable Deadline**
  - December 05, 2023
  - First Tuesday in December, Annually Thereafter
- **Elementary Particle Physics - Experiment; Particle Astrophysics - Experiment - Refer to Solicitation for Applicable Deadline**
  - December 12, 2023
  - Second Tuesday in December, Annually Thereafter
- **Nuclear Physics - Theory and Experiment; Elementary Particle Physics - Theory; Particle Astrophysics and Cosmology – Theory; Quantum Information Science; Physics of Living Systems - Refer to Solicitation for Applicable Deadline**

**Table Of Contents**
1. Summary of Program Requirements
2. Introduction
3. Program Description
4. Award Information
5. Eligibility Information
6. Proposal Preparation and Submission Instructions
   - Proposal Preparation Instructions
   - Budgetary Information
   - Due Dates
   - Research.gov/Grants.gov Requirements
7. NSF Proposal Processing and Review Procedures
   - Merit Review Principles and Criteria
   - Review and Selection Process
8. Award Administration Information
   - Notification of the Award
   - Award Conditions
   - Reporting Requirements
9. Agency Contacts
10. Other Information

**Important Information And Revision Notes**
This division-wide solicitation supersedes version NSF 21-593. This solicitation describes additional proposal submission requirements and review criteria beyond those in the NSF Proposal & Award Policies & Procedures Guide. These are specified in the sub-section labeled Additional Information in section (V.A) Proposal Preparation Instructions with further Additional Solicitation Specific Review Criteria specified in section (VI.A) Merit Review Principles and Criteria below. These additional requirements relate primarily to proposers who anticipate having multiple sources of support, proposals involving mid-scale research infrastructure and/or long-duration efforts, and proposals with letters of collaboration. Additional requirements have been included for proposals requiring Antarctic or Arctic logistics support.

This solicitation has annual deadlines that vary across programs. PIs are responsible for selecting the correct deadline from this solicitation for the program to which they are submitting their proposal; they should not rely upon aggregated deadlines posted on external websites. Note that programs are listed after their associated deadlines.

All proposals submitted to the Division of Physics that are not governed by another solicitation (such as CAREER, Major Research Instrumentation (MRI), and those listed below) should be submitted to this solicitation; otherwise they will be returned without review.

Research at Undergraduate Institutions (RUI) proposals should be submitted through a separate solicitation (NSF-14-579), following the documentation requirements therein. Such proposals must be submitted by the deadline listed in this division-wide solicitation that corresponds to the closest disciplinary match. RUI proposals should also follow the additional requirements specified in the sub-section labeled Additional Information in section (V.A) Proposal Preparation Instructions below.

The Physics at the Information Frontier (PIF) Program accepts proposals through separate solicitations. Prospective PIs are encouraged to contact the PIF Program Officer regarding proposal suitability and current funding opportunities. Additional information is provided on the PIF program web page.

Other solicitation and program numbers referenced herein are current at the time of the publication of this solicitation; if the referenced number is archived, refer to the successor publication whenever available.

Any proposal submitted in response to this solicitation should be submitted in accordance with the NSF Proposal & Award Policies & Procedures Guide (PAPPG) that is in effect for the relevant due date to which the proposal is being submitted. The NSF PAPPG is regularly revised and it is the responsibility of the proposer to ensure that the proposal meets the requirements specified in this solicitation and the applicable version of the PAPPG. Submitting a proposal prior to a specified deadline does not negate this requirement.

**Summary Of Program Requirements**

**General Information**
- **Program Title:** Division of Physics: Investigator-Initiated Research Projects (PHY)

**Synopsis of Program:**
The Division of Physics (PHY) supports physics research and the preparation of future scientists in the nation’s colleges and universities across a broad range of physics disciplines that span scales of space and time from the largest to the smallest and the oldest to the youngest. The Division is comprised of disciplinary programs covering experimental and theoretical research in the following major subfields of physics: Atomic, Molecular and Optical Physics; Elementary Particle Physics; Gravitational Physics; Integrative Activities in Physics; Nuclear Physics; Particle Astrophysics; Physics at the Information Frontier; Physics of Living Systems; Plasma Physics; and Quantum Information Science. Principal Investigators (PIs) are encouraged to consider including specific efforts to increase diversity of the physics community and broaden participation of under-represented groups in Science, Technology, Engineering, and Mathematics (STEM).

**Additional Information**
The Division of Physics strongly encourages single proposal submission for possible co-review rather than submission of multiple related proposals to several programs.

PIs considering submitting more than one proposal to this solicitation, or who already have an active PHY award, are encouraged to first consult with the relevant program officer(s) before preparing a new proposal. This does not apply to awards from or submissions to the MRI, REU, and/or center programs, or in cases of renewal proposals.

**Due Dates**

**Full Proposal Deadline(s) (due by 5 p.m. submitter’s local time):**

**Program(s) Deadline**
- **Plasma Physics**
  - Third Monday in November, e.g. November 20, 2023
- **AMO – Theory and Experiment**
- **Gravitational Physics – Theory and Experiment**
- **LIGO Research Support**
- **Integrative Activities in Physics**
  - Fourth Wednesday in November, e.g. November 22, 2023
- **Elementary Particle Physics – Experiment**
- **Particle Astrophysics – Experiment**
  - First Tuesday in December, e.g. December 05, 2023
- **Nuclear Physics – Theory and Experiment**
- **Elementary Particle Physics – Theory**
- **Particle Astrophysics and Cosmology – Theory**
- **Physics of Living Systems**
- **Quantum Information Science**
  - Second Tuesday in December, e.g. December 12, 2023

**Cognizant Program Officer(s):**
Please note that the following information is current at the time of publishing. See program website for any updates to the points of contact.

- **Krastan B. Blagoev**, Physics of Living Systems, telephone: (703) 292-4666, email: kblagoev@nsf.gov
- **Alex Cronin**, Quantum Information Science, telephone: (703) 292-5302, email: acronin@nsf.gov
- **Keith R. Dienes**, Elementary Particle Physics - Theory; Particle Astrophysics and Cosmology - Theory, telephone: (703) 292-5314, email: kdienes@nsf.gov
- **Robert Forrey**, Atomic, Molecular and Optical Physics - Theory; Quantum Information Science, telephone: (703) 292-5199, email: rforrey@nsf.gov
- **Angel E. Garcia**, Physics of Living Systems, telephone: (703) 292-8897, email: aegarcia@nsf.gov
- **John Gillaspy**, Atomic, Molecular and Optical Physics - Experiment, telephone: (703) 292-7173, email: jgillasp@nsf.gov
- **Nigel A. Sharp**, Acting Program Director, Particle Astrophysics/Cosmic Phenomena, telephone: (703) 292-4905 email: nsharp@nsf.gov
- **Kevin Jones**, Atomic, Molecular and Optical Physics - Experiment, telephone: (703) 292-7732, email: kejones@nsf.gov
- **Vyacheslav (Slava) Lukin**, Plasma Physics, telephone: (703) 292-7382, email: vlukin@nsf.gov
- **Pedro Marronetti**, Gravitational Physics - Theory and Experiment; LIGO Research Support, telephone: (703) 292-7372, email: pmarrone@nsf.gov
- **Kathleen McCloud**, Integrative Activities in Physics, telephone: (703) 292-8236, email: kmccloud@nsf.gov
- **Bogdan Mihaila**, Nuclear Physics - Theory, telephone: (703) 292-8235, email: bmihaila@nsf.gov
- **Allena K. Opper**, Nuclear Physics - Experiment, telephone: (703) 292-8958, email: aopper@nsf.gov
- **James T. Shank**, Elementary Particle Physics - Experiment, telephone: (703) 292-4516, email: jshank@nsf.gov
- **William Wester**, Particle Astrophysics - Experiment, telephone: (703) 292-4677, email: wwester@nsf.gov
- **Jeremiah D. Williams**, Plasma Physics, telephone: (703) 292-4687, email: jdwillia@nsf.gov

**Applicable Catalog of Federal Domestic Assistance (CFDA) Number(s):**
- 47.049 --- Mathematical and Physical Sciences

**Award Information**
- **Anticipated Type of Award:** Standard Grant or Continuing Grant or Cooperative Agreement
- **Estimated Number of Awards:** 300
- **Anticipated Funding Amount:** $120,000,000

Pending availability of funds, approximately $120M will be committed for the total budget of all new awards in each year. Estimated program budget, number of awards and average award size/duration are subject to the availability of funds.

**Eligibility Information**

**Who May Submit Proposals:**
Proposals may only be submitted by the following:
- **Institutions of Higher Education (IHEs):** Two- and four-year IHEs (including community colleges) accredited in, and having a campus located in the US, acting on behalf of their faculty members. Special Instructions for International Branch Campuses of US IHEs: If the proposal includes funding to be provided to an international branch campus of a US institution of higher education (including through use of subawards and consultant arrangements), the proposer must explain the benefit(s) to the project of performance at the international branch campus, and justify why the project activities cannot be performed at the US campus.
- **Non-profit, non-academic organizations:** Independent museums, observatories, research laboratories, professional societies and similar organizations located in the U.S. that are directly associated with educational or research activities.
- **For-profit organizations:** U.S.-based commercial organizations, including small businesses, with strong capabilities in scientific or engineering research or education and a passion for innovation.
- **State and Local Governments:** State educational offices or organizations and local school districts.
- **Tribal Governments:** The governing body of any Indian or Alaska Native tribe, band, nation, pueblo, village, or community that the Secretary of the Interior acknowledges to exist as an Indian tribe under the Federally Recognized Indian Tribe List Act of 1994 (25 U.S.C. 479a, et seq.)
- **Foreign organizations:** For cooperative projects involving U.S. and foreign organizations, support will only be provided for the U.S. portion.
- **Other Federal Agencies and Federally Funded Research and Development Centers (FFRDCs):** Contact the appropriate program before preparing a proposal for submission.

**Who May Serve as PI:**
There are no restrictions or limits.

**Limit on Number of Proposals per Organization:**
There are no restrictions or limits.

**Limit on Number of Proposals per PI or co-PI:**
None. However, the Division of Physics strongly encourages single proposal submission for possible co-review rather than submission of multiple related proposals to several programs.

PIs considering submitting more than one proposal to this solicitation, or who already have an active PHY award, are encouraged to first consult with the relevant program officer(s) before preparing a new proposal. This does not apply to awards from or submissions to the MRI, REU, and/or center programs, or in cases of renewal proposals.

**Proposal Preparation and Submission Instructions**

**A. Proposal Preparation Instructions**
- **Letters of Intent:** Not required
- **Preliminary Proposal Submission:** Not required
- **Full Proposals:**
  - **Full Proposals submitted via Research.gov:** NSF Proposal and Award Policies and Procedures Guide (PAPPG) guidelines apply. The complete text of the PAPPG is available electronically on the NSF website at: [NSF PAPPG](https://www.nsf.gov/publications/pub_summ.jsp?ods_key=pappg).
  - **Full Proposals submitted via Grants.gov:** NSF Grants.gov Application Guide: A Guide for the Preparation and Submission of NSF Applications via Grants.gov guidelines apply (Note: The NSF Grants.gov Application Guide is available on the Grants.gov website and on the NSF website at: [NSF Grants.gov Guide](https://www.nsf.gov/publications/pub_summ.jsp?ods_key=grantsgovguide)).

**B. Budgetary Information**
- **Cost Sharing Requirements:** Inclusion of voluntary committed cost sharing is prohibited.
- **Indirect Cost (F&A) Limitations:** Not Applicable
- **Other Budgetary Limitations:** Not Applicable

**C. Due Dates**
- **Full Proposal Deadline(s) (due by 5 p.m. submitter's local time):**
  - November 20, 2023
  - Third Monday in November, Annually Thereafter
  - **Plasma Physics - Refer to Solicitation for Applicable Deadline**
    - November 22, 2023
    - Fourth Wednesday in November, Annually Thereafter
  - **AMO - Theory and Experiment; Gravitational Physics - Theory and Experiment; LIGO Research Support; Integrative Activities in Physics - Refer to Solicitation for Applicable Deadline**
    - December 05, 2023
    - First Tuesday in December, Annually Thereafter
  - **Elementary Particle Physics - Experiment; Particle Astrophysics - Experiment - Refer to Solicitation for Applicable Deadline**
    - December 12, 2023
    - Second Tuesday in December, Annually Thereafter
  - **Nuclear Physics - Theory and Experiment; Elementary Particle Physics - Theory; Particle Astrophysics and Cosmology – Theory; Quantum Information Science; Physics of Living Systems - Refer to Solicitation for Applicable Deadline**

**Proposal Review Information Criteria**

**Merit Review Criteria:**
National Science Board approved criteria. Additional merit review criteria apply. Please see the full text of this solicitation for further information.

**Award Administration Information**

**Award Conditions:**
Additional award conditions apply. Please see the full text of this solicitation for further information.

**Reporting Requirements:**
Standard NSF reporting requirements apply.

**I. Introduction**
The Division of Physics (PHY) supports physics research and the preparation of future scientists in the nation’s colleges and universities across a broad range of physics disciplines that span scales of space and time from the largest to the smallest and the oldest to the youngest. The Division is comprised of disciplinary programs covering experimental and theoretical research in the following major subfields of physics: Atomic, Molecular and Optical Physics; Elementary Particle Physics; Gravitational Physics; Integrative Activities in Physics; Nuclear Physics; Particle Astrophysics; Physics at the Information Frontier; Physics of Living Systems; Plasma Physics; and Quantum Information Science.

**PHY Mission:**
To support fundamental research across the intellectual frontiers of physics, to support research that has broader impacts on other fields of science and on the health, economic strength, and defense of society, to enhance workforce preparation at all levels and share the excitement of science with the public through integration of research and education, and to steward the physics community so as to maintain the intellectual capital essential for future advances. Modes of support include single investigator awards, group awards, centers and institutes, some interdisciplinary in nature, and several national user facilities, as well as research equipment/instrumentation development grants and mid-scale research infrastructure awards.

**PHY Science:**
Physics research probes the properties of matter at its most fundamental level, the interactions between particles, and the organization of constituents and symmetry principles that lead to the rich structure and phenomena that we observe in the world around us. Physics seeks a deep understanding of processes that led to the formation of the cosmos, to the structure of matter at the very shortest distance scales where quantum effects dominate, and to the structure of atomic and molecular systems that shape and control the everyday world of chemistry and biological systems. Because of the breadth and scope of physics, it forms part of the core educational curriculum in most sciences and in engineering.

Physics research encompasses both theoretical and experimental studies, has very profound connections with fundamental mathematics, and underlies most of the other physical sciences. Collaboration with the other scientific disciplines is very important to the continued health and excitement of physics, some examples being in biological physics at the molecular and cellular levels, in quantum information science and at the physics-computer science/engineering interface, and in the large-scale structure and evolution of the universe. PHY will continue to emphasize the importance of interdisciplinary research.

Physics also supports the development of new tools and techniques needed to expand and refine our understanding of physical systems - from femtosecond lasers to probe and control atomic and molecular systems, to Artificial Intelligence numerical methods for the analysis of complex data sets, to LIGO (Laser Interferometer Gravitational-Wave Observatory), a new window to study the universe through the detection of gravitational waves. The extraordinary sensitivity required for some of the instrumentation demands new technology development and implementation of new mid-scale research infrastructure. PHY encourages research that pushes the envelope of technology as well as the reach of science and sees this also as an investment in developing the scientific leaders of the future.

Solving the cutting-edge problems pursued by the Physics community requires tapping the nation's human talent and resources in their entirety. The Division of Physics (PHY) recognizes that the development of a diverse Physics workforce is critical for continued progress in scientific discovery. Principal Investigators (PIs) are encouraged to consider including specific efforts to increase diversity of the physics community and broaden participation of under-represented groups in Science, Technology, Engineering, and Mathematics (STEM).

Proposals with scope covering topics within the purview of programs outside of the Division of Physics may be co-reviewed with the relevant Divisions as appropriate and at the discretion of the cognizant NSF Program Director.

**II. Program Description**
This solicitation covers three possible award types:
Nigel A. Sharp, Acting Program Director, Particle Astrophysics/Cosmic Phenomena, telephone: (703) 292-4905 email: nsharp@nsf.gov

Kevin Jones, Atomic, Molecular and Optical Physics - Experiment, telephone: (703) 292-7732, email: kejones@nsf.gov

Vyacheslav (Slava) Lukin, Plasma Physics, telephone: (703) 292-7382, email: vlukin@nsf.gov

Pedro Marronetti, Gravitational Physics - Theory and Experiment; LIGO Research Support, telephone: (703) 292-7372, email: pmarrone@nsf.gov

Kathleen McCloud, Integrative Activities in Physics, telephone: (703) 292-8236, email: kmccloud@nsf.gov

Bogdan Mihaila, Nuclear Physics - Theory, telephone: (703) 292-8235, email: bmihaila@nsf.gov

Allena K. Opper, Nuclear Physics - Experiment, telephone: (703) 292-8958, email: aopper@nsf.gov

James T. Shank, Elementary Particle Physics - Experiment, telephone: (703) 292-4516, email: jshank@nsf.gov

William Wester, Particle Astrophysics - Experiment, telephone: (703) 292-4677, email: wwester@nsf.gov

Jeremiah D. Williams, Plasma Physics, telephone: (703) 292-4687, email: jdwillia@nsf.gov

Applicable Catalog of Federal Domestic Assistance (CFDA) Number(s):

47.049 --- Mathematical and Physical Sciences
Award Information
Anticipated Type of Award: Standard Grant or Continuing Grant or Cooperative Agreement

Estimated Number of Awards: 300

Anticipated Funding Amount: $120,000,000

Pending availability of funds, approximately $120M will be committed for the total budget of all new awards in each year. Estimated program budget, number of awards and average award size/duration are subject to the availability of funds.

Eligibility Information
Who May Submit Proposals:

Proposals may only be submitted by the following:

Institutions of Higher Education (IHEs) - Two- and four-year IHEs (including community colleges) accredited in, and having a campus located in the US, acting on behalf of their faculty members. Special Instructions for International Branch Campuses of US IHEs: If the proposal includes funding to be provided to an international branch campus of a US institution of higher education (including through use of subawards and consultant arrangements), the proposer must explain the benefit(s) to the project of performance at the international branch campus, and justify why the project activities cannot be performed at the US campus.
Non-profit, non-academic organizations: Independent museums, observatories, research laboratories, professional societies and similar organizations located in the U.S. that are directly associated with educational or research activities.
For-profit organizations: U.S.-based commercial organizations, including small businesses, with strong capabilities in scientific or engineering research or education and a passion for innovation.
State and Local Governments: State educational offices or organizations and local school districts.
Tribal Governments: The governing body of any Indian or Alaska Native tribe, band, nation, pueblo, village, or community that the Secretary of the Interior acknowledges to exist as an Indian tribe under the Federally Recognized Indian Tribe List Act of 1994 (25 U.S.C. 479a, et seq.)
Foreign organizations: For cooperative projects involving U.S. and foreign organizations, support will only be provided for the U.S. portion.
Other Federal Agencies and Federally Funded Research and Development Centers (FFRDCs): Contact the appropriate program before preparing a proposal for submission.
Who May Serve as PI:

There are no restrictions or limits.

Limit on Number of Proposals per Organization:

There are no restrictions or limits.

Limit on Number of Proposals per PI or co-PI:

None. However, the Division of Physics strongly encourages single proposal submission for possible co-review rather than submission of multiple related proposals to several programs.

PIs considering submitting more than one proposal to this solicitation, or who already have an active PHY award, are encouraged to first consult with the relevant program officer(s) before preparing a new proposal. This does not apply to awards from or submissions to the MRI, REU, and/or center programs, or in cases of renewal proposals.

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

Full Proposal Deadline(s) (due by 5 p.m. submitter's local time):

     November 20, 2023

     Third Monday in November, Annually Thereafter

Plasma Physics - Refer to Solicitation for Applicable Deadline
     November 22, 2023

     Fourth Wednesday in November, Annually Thereafter

AMO - Theory and Experiment; Gravitational Physics - Theory and Experiment; LIGO Research Support; Integrative Activities in Physics - Refer to Solicitation for Applicable Deadline
     December 05, 2023

     First Tuesday in December, Annually Thereafter

Elementary Particle Physics - Experiment; Particle Astrophysics - Experiment - Refer to Solicitation for Applicable Deadline
     December 12, 2023

     Second Tuesday in December, Annually Thereafter

Nuclear Physics - Theory and Experiment; Elementary Particle Physics - Theory; Particle Astrophysics and Cosmology – Theory; Quantum Information Science; Physics of Living Systems - Refer to Solicitation for Applicable Deadline
Proposal Review Information Criteria
Merit Review Criteria:

National Science Board approved criteria. Additional merit review criteria apply. Please see the full text of this solicitation for further information.

Award Administration Information
Award Conditions:

Additional award conditions apply. Please see the full text of this solicitation for further information.

Reporting Requirements:

Standard NSF reporting requirements apply.

I. Introduction
The Division of Physics (PHY) supports physics research and the preparation of future scientists in the nation’s colleges and universities across a broad range of physics disciplines that span scales of space and time from the largest to the smallest and the oldest to the youngest. The Division is comprised of disciplinary programs covering experimental and theoretical research in the following major subfields of physics: Atomic, Molecular and Optical Physics; Elementary Particle Physics; Gravitational Physics; Integrative Activities in Physics; Nuclear Physics; Particle Astrophysics; Physics at the Information Frontier; Physics of Living Systems; Plasma Physics; and Quantum Information Science.

PHY Mission: To support fundamental research across the intellectual frontiers of physics, to support research that has broader impacts on other fields of science and on the health, economic strength, and defense of society, to enhance workforce preparation at all levels and share the excitement of science with the public through integration of research and education, and to steward the physics community so as to maintain the intellectual capital essential for future advances. Modes of support include single investigator awards, group awards, centers and institutes, some interdisciplinary in nature, and several national user facilities, as well as research equipment/instrumentation development grants and mid-scale research infrastructure awards.

PHY Science: Physics research probes the properties of matter at its most fundamental level, the interactions between particles, and the organization of constituents and symmetry principles that lead to the rich structure and phenomena that we observe in the world around us. Physics seeks a deep understanding of processes that led to the formation of the cosmos, to the structure of matter at the very shortest distance scales where quantum effects dominate, and to the structure of atomic and molecular systems that shape and control the everyday world of chemistry and biological systems. Because of the breadth and scope of physics, it forms part of the core educational curriculum in most sciences and in engineering.

Physics research encompasses both theoretical and experimental studies, has very profound connections with fundamental mathematics, and underlies most of the other physical sciences. Collaboration with the other scientific disciplines is very important to the continued health and excitement of physics, some examples being in biological physics at the molecular and cellular levels, in quantum information science and at the physics-computer science/engineering interface, and in the large-scale structure and evolution of the universe. PHY will continue to emphasize the importance of interdisciplinary research.

Physics also supports the development of new tools and techniques needed to expand and refine our understanding of physical systems - from femtosecond lasers to probe and control atomic and molecular systems, to Artificial Intelligence numerical methods for the analysis of complex data sets, to LIGO (Laser Interferometer Gravitational-Wave Observatory), a new window to study the universe through the detection of gravitational waves. The extraordinary sensitivity required for some of the instrumentation demands new technology development and implementation of new mid-scale research infrastructure. PHY encourages research that pushes the envelope of technology as well as the reach of science and sees this also as an investment in developing the scientific leaders of the future.

Solving the cutting-edge problems pursued by the Physics community requires tapping the nation's human talent and resources in their entirety. The Division of Physics (PHY) recognizes that the development of a diverse Physics workforce is critical for continued progress in scientific discovery. Principal Investigators (PIs) are encouraged to consider including specific efforts to increase diversity of the physics community and broaden participation of under-represented groups in Science, Technology, Engineering, and Mathematics (STEM).

Proposals with scope covering topics within the purview of programs outside of the Division of Physics may be co-reviewed with the relevant Divisions as appropriate and at the discretion of the cognizant NSF Program Director.

II. Program Description
This solicitation covers three possible award types:

individual investigator and group awards with standard time cycles;
mid-scale research infrastructure awards; and
awards that anticipate long-term support.
For standard individual investigator and group awards that follow the usual cycles for competitive renewal, proposals must follow the requirements of the NSF Proposal & Award Policies & Procedures Guide plus specific additional requirements included in this solicitation. See Additional Information under Proposal Preparation Instructions and Additional Solicitation Specific Review Criteria under Merit Review Principles and Criteria.

Proposals that involve significant investments either because they request mid-scale research infrastructure or because they involve activities that can span several renewal cycles are considered Large Investments by the Division and may involve additional instructions and additional review. See the relevant sections on Long-Duration Efforts and Mid-scale Research Infrastructure below.

________________

The Division of Physics invites research proposals in the following areas:

Atomic Molecular and Optical Physics - Experiment [Program Description]

Atomic Molecular and Optical Physics - Theory [Program Description]

Elementary Particle Physics - Experiment [Program Description]

Elementary Particle Physics - Theory [Program Description]

Gravitational Physics - Experiment [Program Description]
Gravitational Physics - Theory [Program Description]

LIGO Research Support [Program Description]

Integrative Activities in Physics [Program Description]

Nuclear Physics - Experiment [Program Description]

Nuclear Physics - Theory [Program Description]

Particle Astrophysics - Experiment [Program Description]

Particle Astrophysics and Cosmology - Theory [Program Description]

Physics of Living Systems [Program Description]

Plasma Physics [Program Description]

Quantum Information Science [Program Description]

The scope of each program is described on the program page. Proposals that are determined to be outside the scope of the program to which they were submitted may be returned without review. Proposers are encouraged to consult with Program Directors prior to submission deadlines.

________

The following sections apply to proposals associated with activities whose duration typically covers several award cycles (Long-Duration Efforts), and/or involve instrumentation acquisition or development (Mid-scale Research Infrastructure).

Large Investments

Any activity that requires a level of program support which is significant compared to the associated program budget is considered by the Division of Physics to be a large investment. Designation of an activity as a large investment, and therefore subject to the guidelines, is made by the Program Directors in consultation with the Division Director.

Some of these large investments entail the acquisition or development/implementation of research infrastructure. Large investments may also come in the form of long-duration efforts that require substantial funding over multiple award cycles while not necessarily requesting significant investments in a single award cycle. Activities that receive this designation typically aim to achieve a focused goal and may involve several individual or group awards. Large investments are not defined by a specific dollar amount, as these will vary by program. However, in all cases these projects require significant commitments from the individual programs, and therefore require special consideration. The largest of these investments may involve PHY mid-scale funding, which is allocated by the Division Director. Two modes are described below: A) Mid-scale Research Infrastructure and B) Long-duration activities.

The following language applies both to Mid-scale Research Infrastructure and Long-Duration activities.

Scientific Review
Proposals are first considered on the basis of their science goals. Because the investment will substantially impact the budget of any individual program and because the impact will likely extend for more than a single award cycle, the science goals must be of high priority within the program. Standard proposal review panels prioritize a proposal compared to other proposals received that year. To appropriately prioritize a proposal involving a potentially large investment, the review panel may be asked to additionally consider the programmatic balance of investments across the full program. In some cases, a special panel may be required to consider and prioritize the proposed investment.

Technical Review

The feasibility of the proposed activities must also be thoroughly reviewed. Given the scale and complexity of most large investments a separate panel may be required to assess implementation plans. For some proposals, including those with instrument development and/or fabrication, the review may consider technical readiness, risk mitigation, management plans, budgets and schedules. For long-duration efforts where the lifetime of the project is expected to exceed a single award period, the review may consider performance schedules, lifecycle planning, and, for renewal proposals, the record of success in achieving any previously set milestones. As needed, these reviews may involve site visits. In all cases, the technical review panel will be asked to consider and provide guidance to the Program Directors on the appropriate duration of the award and milestones needed to evaluate the project’s progress.

Award Oversight
Awards for Long-Duration efforts or for Mid-scale Research Infrastructure may be made through cooperative agreements that contain terms and conditions specific to the nature and risks associated with the project. These may involve site visits or mid-term reviews, and NSF approval of changes in management or schedule. Oversight will include monitoring progress towards any milestones established during the technical review. Depending on the nature of the project and the recommendations from the technical reviews, initial awards may be made for 3 to 5 years. The duration of support will be determined based on the scientific goals of the project with input from the technical review and taking into account the financial burden on the programs. Proposals for continued support may involve both scientific and technical review, as appropriate at the time of the request. Appropriate close-out should be planned in advance. For the largest investments a close-out phase may be described in the cooperative agreement.

New activities involving large investments will be governed by this solicitation. Currently funded projects that involve long-duration efforts will be subject to these same procedures if they apply for renewed support in order to determine whether the science continues to be of high priority within the programs and whether the implementation plans are sound.

Proponents of potential large investment activities are strongly encouraged to contact Program Directors before submitting proposals. Program Directors can advise potential PIs on the financial viability of the project and on the review process.
Mid-scale Research Infrastructure

Mid-scale research infrastructure represents some of the largest investments within the Division of Physics. All research infrastructure implementation with costs between $4 million and $30 million fall into this category. Proponents should contact the Program Directors for the relevant program(s) for details. Review of the proposal and subsequent oversight of mid-scale research infrastructure awards will scale with the size and complexity of the proposed project as described in the 2019 Major Facilities Guide (MFG), or subsequent revision in effect at time of proposal submission found at: https://www.nsf.gov/bfa/lfo/lfo_documents.jsp. The guidelines listed here follow standard practices for activities of this scope.

Requests for mid-scale research infrastructure support may involve a sequence of development phases and PHY Division-level reviews. For the most complex cases, these are designated by the following phases:

early conceptual phase;
pre-implementation phase;
implementation phase.
Less complex cases may skip development stages as determined by the cognizant PO.

All proposals are evaluated using the NSF merit review criteria concerning intellectual merit and broader impacts, as well as an assessment as to how well the proposed mid-scale research infrastructure will address the stated science goals. Consideration of all mid-scale research infrastructure requests begins by evaluating and prioritizing the science goals within the individual programs and determining the feasibility of the implementation plan. For each of the relevant phases listed above, the associated proposal will be reviewed before passing on to the next stage. At each stage of development, the Division of Physics may choose to provide support through the next phase or end its involvement. At successive development phases, the reviews will be increasingly detailed and will involve an increasing level of commitment from the Division. Project planning must take into account the total project lifecycle. The Division investment in mid-scale research infrastructure development is of finite duration, and at the completion of fabrication, the Division involvement ends; program funding may support project operations. As appropriate, these stages of development will be coordinated with funding partners in other agencies or organizations.

Although more than one organization may participate in a PHY mid-scale research infrastructure proposal, a single organization must accept overall management responsibility for the project. The proposal must be submitted by one organization, with funding provided to any other organization through subawards. The use of the separately submitted collaborative proposal method is not permitted for PHY mid-scale proposals. Awards for mid-scale research infrastructure will be in the form of cooperative agreements.

PIs should consult section 5 of the NSF Research Infrastructure Guide (found at: https://www.nsf.gov/bfa/lfo/lfo_documents.jsp) for guidance on planning and oversight of mid-scale research infrastructure projects.

For further information, see Additional Information for Mid-scale Research Infrastructure under Proposal Preparation Instructions.

Long-Duration Efforts

Long-duration efforts, while not necessarily requesting significant investments in a single award cycle, over time require substantial funding. Activities that receive this designation typically aim to achieve a focused goal (such as a single high-precision measurement) and may also include several individual or group awards. Proposals for these activities should indicate expected lifetimes as well as appropriate milestones. Reviews of these proposals may consider performance schedules, and, for renewal proposals, the record of success in achieving any previously set milestones. PIs who anticipate a long-duration effort should contact Program Directors for the relevant program(s).
Information Sharing with other Funding Agencies

As permitted under the Memorandums of Understanding (MOUs) between NSF and the Department of Energy National Nuclear Security Administration (DOE/NNSA), the DOE Office of Science (DOE SC), and the Air Force Research Laboratory (AFRL), NSF may share information from proposals for consideration of joint funding and may invite employees of these agencies to attend merit review panels as observers.

III. Award Information
Anticipated Type of Award: Continuing Grant or Cooperative Agreement or Standard Grant

Estimated Number of Awards: 300

Anticipated Funding Amount: $120,000,000

Pending availability of funds, approximately $120M will be committed for the total budget of all new awards in each year. Estimated program budget, number of awards and average award size/duration are subject to the availability of funds.

IV. Eligibility Information
Who May Submit Proposals:

Proposals may only be submitted by the following:

Institutions of Higher Education (IHEs) - Two- and four-year IHEs (including community colleges) accredited in, and having a campus located in the US, acting on behalf of their faculty members. Special Instructions for International Branch Campuses of US IHEs: If the proposal includes funding to be provided to an international branch campus of a US institution of higher education (including through use of subawards and consultant arrangements), the proposer must explain the benefit(s) to the project of performance at the international branch campus, and justify why the project activities cannot be performed at the US campus.
Non-profit, non-academic organizations: Independent museums, observatories, research laboratories, professional societies and similar organizations located in the U.S. that are directly associated with educational or research activities.
For-profit organizations: U.S.-based commercial organizations, including small businesses, with strong capabilities in scientific or engineering research or education and a passion for innovation.
State and Local Governments: State educational offices or organizations and local school districts.
Tribal Governments: The governing body of any Indian or Alaska Native tribe, band, nation, pueblo, village, or community that the Secretary of the Interior acknowledges to exist as an Indian tribe under the Federally Recognized Indian Tribe List Act of 1994 (25 U.S.C. 479a, et seq.)
Foreign organizations: For cooperative projects involving U.S. and foreign organizations, support will only be provided for the U.S. portion.
Other Federal Agencies and Federally Funded Research and Development Centers (FFRDCs): Contact the appropriate program before preparing a proposal for submission.
Who May Serve as PI:

There are no restrictions or limits.

Limit on Number of Proposals per Organization:

There are no restrictions or limits.

Limit on Number of Proposals per PI or co-PI:

None. However, the Division of Physics strongly encourages single proposal submission for possible co-review rather than submission of multiple related proposals to several programs.

PIs considering submitting more than one proposal to this solicitation, or who already have an active PHY award, are encouraged to first consult with the relevant program officer(s) before preparing a new proposal. This does not apply to awards from or submissions to the MRI, REU, and/or center programs, or in cases of renewal proposals.

Additional Eligibility Info:

Although more than one organization may participate in a PHY mid-scale research infrastructure proposal, a single organization must accept overall management responsibility for the project. The proposal must be submitted by one organization, with funding provided to any other organization through subawards. The use of the separately submitted collaborative proposal method is not permitted for PHY mid-scale proposals.

Accomplishment-Based Renewal proposals are not permitted.

V. Proposal Preparation And Submission Instructions
A. Proposal Preparation Instructions
Full Proposal Preparation Instructions: Proposers may opt to submit proposals in response to this Program Solicitation via Research.gov or Grants.gov.

Full Proposals submitted via Research.gov: Proposals submitted in response to this program solicitation should be prepared and submitted in accordance with the general guidelines contained in the NSF Proposal and Award Policies and Procedures Guide (PAPPG). The complete text of the PAPPG is available electronically on the NSF website at: https://www.nsf.gov/publications/pub_summ.jsp?ods_key=pappg. Paper copies of the PAPPG may be obtained from the NSF Publications Clearinghouse, telephone (703) 292-8134 or by e-mail from nsfpubs@nsf.gov. The Prepare New Proposal setup will prompt you for the program solicitation number.
Full proposals submitted via Grants.gov: Proposals submitted in response to this program solicitation via Grants.gov should be prepared and submitted in accordance with the NSF Grants.gov Application Guide: A Guide for the Preparation and Submission of NSF Applications via Grants.gov. The complete text of the NSF Grants.gov Application Guide is available on the Grants.gov website and on the NSF website at: (https://www.nsf.gov/publications/pub_summ.jsp?ods_key=grantsgovguide). To obtain copies of the Application Guide and Application Forms Package, click on the Apply tab on the Grants.gov site, then click on the Apply Step 1: Download a Grant Application Package and Application Instructions link and enter the funding opportunity number, (the program solicitation number without the NSF prefix) and press the Download Package button. Paper copies of the Grants.gov Application Guide also may be obtained from the NSF Publications Clearinghouse, telephone (703) 292-8134 or by e-mail from nsfpubs@nsf.gov.
In determining which method to utilize in the electronic preparation and submission of the proposal, please note the following:

Collaborative Proposals. All collaborative proposals submitted as separate submissions from multiple organizations must be submitted via Research.gov. PAPPG Chapter II.E.3 provides additional information on collaborative proposals.

See PAPPG Chapter II.D.2 for guidance on the required sections of a full research proposal submitted to NSF. Please note that the proposal preparation instructions provided in this program solicitation may deviate from the PAPPG instructions.

Additional Information for All Proposals

PIs should take care to follow the PAPPG instructions regarding preparation of the Current and Pending Support section of their proposal. For each entry in the Current and Pending Support section, a brief statement of the overall objectives of the project/proposal being proposed or in-kind contribution must be provided. The entry also should summarize potential overlap with any active or pending proposal or in-kind contribution and this proposal in terms of scope, budget, or person-months planned or committed to the project by the individual. The total award amount for the entire award period covered (including indirect costs) must be provided, as well as the number of person-months (or partial person-months) per year to be devoted to the project by the individual. The information contained in the budget section of the proposal is separate and distinct from the information entered in current and pending support, and each of these sections is used for a different purpose in NSF’s merit review process. The proposal review process will include an assessment of the proposers’ ability to carry out the proposed research in light of these commitments.

Letters of Support/Endorsement are not permitted.

Letters of Collaboration

Letters of collaboration limited to stating the intent to collaborate and not containing endorsements or evaluation of the proposed project are allowed. The Project Description should document the need for and nature of collaborations, such as intellectual contributions to the project, permission to access a site, an instrument, or a facility, offer of samples and materials for research, logistical support to the research and education program, or mentoring of U.S. students at a foreign site. Letters of collaboration should be included only when the involvement of the external collaborator is critical for the success of the proposed research. Letters of collaboration must follow the single-sentence format in a Supplementary Document:

“If the proposal submitted by Dr. [insert the full name of the Principal Investigator] entitled [insert the proposal title] is selected for funding by the NSF, it is my intent to collaborate and/or commit resources as detailed in the Project Description.”

Departure from this format may result in the proposal being returned without review.

Letters of Membership

Letters of Membership in a scientific collaboration, to be sent by the collaboration’s spokesperson or equivalent also are allowed. They must follow this single-sentence format in a Supplementary Document:

“The [Name of PI’s Institution] group is a member in good standing of the [Name of Collaboration], including you as a member of that group.”

Collaborators and Other Affiliations Forms

A Collaborators and Other Affiliations (COA) form must be submitted as a Single Copy Document for every senior personnel member. For large collaborations or authorships the form should only list those people with whom the senior personnel have collaborated in a direct and substantive way. Senior personnel with questions regarding whom they should list in their COA form should contact the cognizant program director. Note in this context that listing a collaboration name or providing a collaboration URL is not sufficient.

Research at Undergraduate Institutions

Research at Undergraduate Institutions (RUI) proposals should be submitted through a separate solicitation (NSF-14-579), following the documentation requirements therein. Such proposals must be submitted by the deadline listed in this division-wide solicitation that corresponds to the closest disciplinary match. RUI proposals should also follow the Additional Information requirements specified above.

Proposals which deviate from the required elements of this solicitation (or other items listed in the PAPPG) may be returned without review.

________

Additional Information for Proposals Requiring Antarctic or Arctic Logistics Support

PIs proposing instrumentation or infrastructure intended for use in the Antarctic are required to consult with the appropriate program officer in the Antarctic Sciences Section (ANT) of the NSF Office of Polar Programs (OPP) to discuss the timing and feasibility of their project; these program officers are identified in the current ANT solicitation for fieldwork proposals (see https://new.nsf.gov/funding/opportunities/antarctic-research-requiring-us-antarctic-program). Background on the overall Antarctic science support planning process may be found at https://www.usap.gov/proposalinformation/. For projects requiring logistical support in the Arctic region, please consult with the NSF Arctic Research Support and Logistics (RSL) Program to discuss any support requirements (see: https://www.nsf.gov/geo/opp/arctic/res_log_sup.jsp). Documentation in the form of email correspondence must be provided as a Single Copy Document. Failure to do so may result in a proposal being returned without review.

________

Additional Information for Mid-scale Research Infrastructure

This section applies to proposals for support of research infrastructure acquisition at costs between $4 million and $30 million. PIs should first contact the Program Director for their physics discipline to determine the appropriate development stage of the proposed project, as well as the appropriate structure of the proposal in terms of possible supplementary documents and/or page-limit extensions.

Mid-scale research infrastructure requests follow a plan of development phases or stages as described below. Some of these stages may be combined as appropriate, but PIs should be aware of these stages when planning proposals. Depending on the maturity of the project, a proposal requesting Mid-scale research infrastructure support has additional requirements as follows:

Early Conceptual Phase: At the early conceptual phase, the proposal must include the conceptual project design, scope contingency, and total project lifecycle planning including operations and close-out. This proposal must include a full statement of the science goals and sufficient technical detail to appropriately review the project. The associated disciplinary program will review the scientific merit on a competitive basis that includes the potential cost to the program of conducting the experiment that would be enabled by the instrumentation. The affordability of fabrication should be supported by parametric top-down budget estimates to provide a cost range.

Pre-Implementation Phase: At the pre-implementation phase, the proposal must contain the preliminary design and include the total project lifecycle planning. Proposals must also include an appropriately scaled Project Execution Plan (PEP) describing how the project will be managed, the scope in a Work Breakdown Structure (WBS) format along with a WBS dictionary, the budget estimate and basis of estimate for each WBS element, and the risk or uncertainty in the budget estimate accompanied by the methodology for risk and budget contingency estimation. A resource-loaded schedule is also required in order to support the proposed construction funding profile. Projection of operating costs should be revisited in an updated plan for the operations phase.

Implementation Phase: At this phase, the mid-scale research infrastructure proposal demonstrates that enabling R&D is completed, and that bid packages for major contracts or acquisitions have been completed. The fabrication budget estimate is refined so that it is based substantially on externally provided information rather than internal engineering estimates (vendor quotes, budgetary estimates, etc.) Key staff members needed to manage construction activities are recruited and ready to commence fabrication. Commitments from external partners in the activity are confirmed. The largest and most complex projects are encouraged to use appropriately scaled Earned Value Management reporting during construction, (see section 5 of the MFG) and should prepare an Earned Value Management System during this phase in readiness for fabrication.

Although more than one organization may participate in a PHY mid-scale proposal, a single organization must accept overall management responsibility for the project. The proposal must be submitted by one organization, with funding provided to any other organization through subawards. The use of the separately submitted collaborative proposal method is not permitted for PHY mid-scale infrastructure proposals.

PIs should consult section 5 of the NSF Research Infrastructure Guide (RIG) for additional guidance on planning and oversight of mid-scale research infrastructure projects.

B. Budgetary Information
Cost Sharing:

Inclusion of voluntary committed cost sharing is prohibited.

C. Due Dates
Full Proposal Deadline(s) (due by 5 p.m. submitter's local time):

     November 20, 2023

     Third Monday in November, Annually Thereafter

Plasma Physics - Refer to Solicitation for Applicable Deadline
     November 22, 2023

     Fourth Wednesday in November, Annually Thereafter

AMO - Theory and Experiment; Gravitational Physics - Theory and Experiment; LIGO Research Support; Integrative Activities in Physics - Refer to Solicitation for Applicable Deadline
     December 05, 2023

     First Tuesday in December, Annually Thereafter

Elementary Particle Physics - Experiment; Particle Astrophysics - Experiment - Refer to Solicitation for Applicable Deadline
     December 12, 2023

     Second Tuesday in December, Annually Thereafter

Nuclear Physics - Theory and Experiment; Elementary Particle Physics - Theory; Particle Astrophysics and Cosmology – Theory; Quantum Information Science; Physics of Living Systems - Refer to Solicitation for Applicable Deadline
D. Research.gov/Grants.gov Requirements
For Proposals Submitted Via Research.gov:

To prepare and submit a proposal via Research.gov, see detailed technical instructions available at: https://www.research.gov/research-portal/appmanager/base/desktop?_nfpb=true&_pageLabel=research_node_display&_nodePath=/researchGov/Service/Desktop/ProposalPreparationandSubmission.html. For Research.gov user support, call the Research.gov Help Desk at 1-800-381-1532 or e-mail rgov@nsf.gov. The Research.gov Help Desk answers general technical questions related to the use of the Research.gov system. Specific questions related to this program solicitation should be referred to the NSF program staff contact(s) listed in Section VIII of this funding opportunity.

For Proposals Submitted Via Grants.gov:

Before using Grants.gov for the first time, each organization must register to create an institutional profile. Once registered, the applicant's organization can then apply for any federal grant on the Grants.gov website. Comprehensive information about using Grants.gov is available on the Grants.gov Applicant Resources webpage: https://www.grants.gov/web/grants/applicants.html. In addition, the NSF Grants.gov Application Guide (see link in Section V.A) provides instructions regarding the technical preparation of proposals via Grants.gov. For Grants.gov user support, contact the Grants.gov Contact Center at 1-800-518-4726 or by email: support@grants.gov. The Grants.gov Contact Center answers general technical questions related to the use of Grants.gov. Specific questions related to this program solicitation should be referred to the NSF program staff contact(s) listed in Section VIII of this solicitation.

Submitting the Proposal: Once all documents have been completed, the Authorized Organizational Representative (AOR) must submit the application to Grants.gov and verify the desired funding opportunity and agency to which the application is submitted. The AOR must then sign and submit the application to Grants.gov. The completed application will be transferred to Research.gov for further processing.

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

Proposers are reminded that reviewers will also be asked to review the Data Management Plan and the Postdoctoral Researcher Mentoring Plan, as appropriate.

Additional Solicitation Specific Review Criteria

Additional Criterion for all Proposals

The proposal review process will include an assessment of the proposers’ ability to carry out the proposed research in light of the commitments indicated in the Current and Pending Support section.

Proposals that request support for large investments – either mid-scale research infrastructure or long-duration support – may include additional review, as described below.

Additional Criteria for Mid-scale Research Infrastructure

Early Conceptual Phase: The Division-level proposal review process will review the scientific merit on a competitive basis that includes the potential cost to the program of conducting the experiment that would be enabled by the instrumentation. The program may seek additional reviews to evaluate the technical scope and costs at a level commensurate with conceptual design.

Pre-Implementation Phase: The Division-level review at this phase will focus on project-related aspects such as budgets and project management, and will evaluate, as appropriate to this level, a Project Execution Plan (PEP) describing how the project will be managed, the scope in a Work Breakdown Structure (WBS) format along with a WBS dictionary, the budget estimate and basis of estimate for each WBS element, and the risk or uncertainty in the budget estimate accompanied by the methodology for risk and budget contingency estimation.

Implementation Phase: The Division-level review at this phase will focus on reliability of costs and technical readiness, as evidenced by the following; the mid-scale research infrastructure proposal demonstrates that enabling R&D is completed, and that bid packages for major contracts or acquisitions have been completed; the fabrication budget estimate is refined so that it is based substantially on externally provided information rather than internal engineering estimates (vendor quotes, budgetary estimates, etc.); key staff members needed to manage construction activities are recruited and ready to commence fabrication; and commitments from external partners in the activity are confirmed.

Additional Criteria for Long-Duration Efforts

For long-duration efforts, the review may consider performance schedules, life-cycle planning, and, for renewal proposals, the record of success in achieving any previously set milestones. As needed, these reviews may involve site visits.

As noted in section VII.B. under ‘Special Award Conditions,’ long-duration efforts may be comparatively reviewed in setting long-term scientific priorities, and as a result, funding may be phased out. Proposals seeking additional support after activities have been phased out will be reviewed as new long-duration efforts.

The review of proposals related to long-duration projects will include an assessment of the feasibility of the proposed efforts given the projected lifetime, including any phase-out timelines, of the associated long-duration project.

B. Review and Selection Process
Proposals submitted in response to this program solicitation will be reviewed by Ad hoc Review and/or Panel Review, or Site Visit Review.

Proposals may be reviewed through a combination of Ad hoc Reviews, Panel Reviews, or Site Visit Reviews

Reviewers will be asked to evaluate proposals using two National Science Board approved merit review criteria and, if applicable, additional program specific criteria. A summary rating and accompanying narrative will generally be completed and submitted by each reviewer and/or panel. The Program Officer assigned to manage the proposal's review will consider the advice of reviewers and will formulate a recommendation.

After scientific, technical and programmatic review and consideration of appropriate factors, the NSF Program Officer recommends to the cognizant Division Director whether the proposal should be declined or recommended for award. NSF strives to be able to tell applicants whether their proposals have been declined or recommended for funding within six months. Large or particularly complex proposals or proposals from new awardees may require additional review and processing time. The time interval begins on the deadline or target date, or receipt date, whichever is later. The interval ends when the Division Director acts upon the Program Officer's recommendation.

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

Consistent with the requirements of the Build America, Buy America Act (Pub. L. 117-58, Division G, Title IX, Subtitle A, November 15, 2021), no funding made available through this funding opportunity may be obligated for an award unless all iron, steel, manufactured products, and construction materials used in the project are produced in the United States. For additional information, visit NSF’s Build America, Buy America webpage.

Special Award Conditions:

NSF anticipates conducting comparative reviews of selected long-duration efforts on an as-needed basis. The intent of the review is primarily a strategic evaluation aimed at setting long-term scientific priorities. Such a review provides external advice about relative priorities within a given program. A review report for each long-duration effort will be made available to its principal investigators. One possible recommendation of the comparative review may be to phase out support for a long-duration effort and, where applicable, operation of associated instrumentation. For activities that have been phased out, any request for additional funding will be reviewed as a new long-duration effort. Since the affected activities may have different award dates, the review may also cover these activities at different stages of an award. A long-duration effort review report will also provide context for reviews of future proposals from individuals and groups who wish to use associated instrumentation.

C. Reporting Requirements
For all multi-year grants (including both standard and continuing grants), the Principal Investigator must submit an annual project report to the cognizant Program Officer no later than 90 days prior to the end of the current budget period. (Some programs or awards require submission of more frequent project reports). No later than 120 days following expiration of a grant, the PI also is required to submit a final project report, and a project outcomes report for the general public.

Failure to provide the required annual or final project reports, or the project outcomes report, will delay NSF review and processing of any future funding increments as well as any pending proposals for all identified PIs and co-PIs on a given award. PIs should examine the formats of the required reports in advance to assure availability of required data.

PIs are required to use NSF's electronic project-reporting system, available through Research.gov, for preparation and submission of annual and final project reports. Such reports provide information on accomplishments, project participants (individual and organizational), publications, and other specific products and impacts of the project. Submission of the report via Research.gov constitutes certification by the PI that the contents of the report are accurate and complete. The project outcomes report also must be prepared and submitted using Research.gov. This report serves as a brief summary, prepared specifically for the public, of the nature and outcomes of the project. This report will be posted on the NSF website exactly as it is submitted by the PI.

More comprehensive information on NSF Reporting Requirements and other important information on the administration of NSF awards is contained in the NSF Proposal & Award Policies & Procedures Guide (PAPPG) Chapter VII, available electronically on the NSF Website at https://www.nsf.gov/publications/pub_summ.jsp?ods_key=pappg.

VIII. Agency Contacts
Please note that the program contact information is current at the time of publishing. See program website for any updates to the points of contact.

General inquiries regarding this program should be made to:

Krastan B. Blagoev, Physics of Living Systems, telephone: (703) 292-4666, email: kblagoev@nsf.gov

Alex Cronin, Quantum Information Science, telephone: (703) 292-5302, email: acronin@nsf.gov

Keith R. Dienes, Elementary Particle Physics - Theory; Particle Astrophysics and Cosmology - Theory, telephone: (703) 292-5314, email: kdienes@nsf.gov

Robert Forrey, Atomic, Molecular and Optical Physics - Theory; Quantum Information Science, telephone: (703) 292-5199, email: rforrey@nsf.gov

Angel E. Garcia, Physics of Living Systems, telephone: (703) 292-8897, email: aegarcia@nsf.gov

John Gillaspy, Atomic, Molecular and Optical Physics - Experiment, telephone: (703) 292-7173, email: jgillasp@nsf.gov

Nigel A. Sharp, Acting Program Director, Particle Astrophysics/Cosmic Phenomena, telephone: (703) 292-4905, email: nsharp@nsf.gov

Kevin Jones, Atomic, Molecular and Optical Physics - Experiment, telephone: (703) 292-7732, email: kejones@nsf.gov

Vyacheslav (Slava) Lukin, Plasma Physics, telephone: (703) 292-7382, email: vlukin@nsf.gov

Pedro Marronetti, Gravitational Physics - Theory and Experiment; LIGO Research Support, telephone: (703) 292-7372, email: pmarrone@nsf.gov

Kathleen McCloud, Integrative Activities in Physics, telephone: (703) 292-8236, email: kmccloud@nsf.gov

Bogdan Mihaila, Nuclear Physics - Theory, telephone: (703) 292-8235, email: bmihaila@nsf.gov

Allena K. Opper, Nuclear Physics - Experiment, telephone: (703) 292-8958, email: aopper@nsf.gov

James T. Shank, Elementary Particle Physics - Experiment, telephone: (703) 292-4516, email: jshank@nsf.gov

William Wester, Particle Astrophysics - Experiment, telephone: (703) 292-4677, email: wwester@nsf.gov

Jeremiah D. Williams, Plasma Physics, telephone: (703) 292-4687, email: jdwillia@nsf.gov

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
The information requested on proposal forms and project reports is solicited under the authority of the National Science Foundation Act of 1950, as amended. The information on proposal forms will be used in connection with the selection of qualified proposals; and project reports submitted by awardees will be used for program evaluation and reporting within the Executive Branch and to Congress. The information requested may be disclosed to qualified reviewers and staff assistants as part of the proposal review process; to proposer institutions/grantees to provide or obtain data regarding the proposal review process, award decisions, or the administration of awards; to government contractors, experts, volunteers and researchers and educators as necessary to complete assigned work; to other government agencies or other entities needing information regarding applicants or nominees as part of a joint application review process, or in order to coordinate programs or policy; and to another Federal agency, court, or party in a court or Federal administrative proceeding if the government is a party. Information about Principal Investigators may be added to the Reviewer file and used to select potential candidates to serve as peer reviewers or advisory committee members. See System of Record Notices, NSF-50, "Principal Investigator/Proposal File and Associated Records," and NSF-51, "Reviewer/Proposal File and Associated Records.” Submission of the information is voluntary. Failure to provide full and complete information, however, may reduce the possibility of receiving an award.

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
        