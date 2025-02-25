
        As an expert grant writer, craft a compelling grant proposal that authentically represents the perspective of the given entity while addressing the specific requirements of the grant call. Your task is to answer the catechism questions comprehensively, ensuring alignment with the grant agency's objectives and the entity's unique capabilities.

        Entity (Technical/Perspectival Skills and Capacities):
        class FieldsWorldView:
    def __init__(self):
        self.name = "Chris Fields"
        self.description = ("A physicist and interdisciplinary researcher focusing on the foundations of cognition, "
                            "consciousness, and reality from an information-theoretic perspective")
        self.key_concepts = {
            "information_realism": "Information is the most fundamental aspect of reality, more fundamental than matter or energy.",
            "observer_dependence": "Reality is fundamentally shaped by observation and cannot be separated from the observer.",
            "active_inference": "A framework explaining how systems interact with and model their environment through prediction and error minimization.",
            "free_energy_principle": "A unifying principle explaining the behavior of self-organizing systems through the minimization of free energy.",
            "semantic_information": "Information is inherently meaningful and relational, forming the basis of reality.",
            "quantum_cognition": "Applying quantum mechanical principles to understanding cognition and consciousness.",
            "embodied_cognition": "Cognitive processes are deeply rooted in the body's interactions with the world.",
            "predictive_processing": "Perception and cognition are fundamentally predictive processes, constantly refining models of the world.",
            "measurement_problem": "The issue in quantum mechanics regarding the nature of measurement and observation, potentially linked to consciousness.",
            "context_dependence": "Context determines meaning and reality; information has no meaning without context.",
            "cognitive_illusions": "Phenomena that reveal fundamental truths about perception and reality, rather than mere errors of cognition.",
            "thermodynamics_of_cognition": "The study of energetic costs and constraints of information processing in cognitive systems.",
            "category_theory": "A mathematical framework for describing structures and relationships, potentially more fundamental than set theory for describing reality.",
            "quantum_darwinism": "A theory explaining the emergence of classical reality from quantum substrates through a process analogous to natural selection."
        }
        
    def worldview(self) -> Dict[str, Any]:
        return {
            "information_theory": {
                "importance": 10,
                "description": "The fundamental basis for understanding reality, perception, and cognition",
                "quote": "Information is more fundamental than matter or energy; it's the currency of reality."
            },
            "active_inference": {
                "importance": 10,
                "description": "A framework explaining how systems interact with and model their environment",
                "quote": "Active inference isn't just a theory of brain function; it's a theory of life itself."
            },
            "quantum_mechanics": {
                "importance": 9,
                "description": "A theory providing insights into the nature of reality, information, and potentially consciousness",
                "quote": "Quantum mechanics isn't just about particles; it's about how reality itself is structured."
            },
            "free_energy_principle": {
                "importance": 10,
                "description": "A unifying principle explaining the behavior of self-organizing systems",
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
                "description": "Reality is fundamentally shaped by observation",
                "quote": "The world is not 'out there' waiting to be observed; it is constructed by observation."
            },
            "information_realism": {
                "importance": 10,
                "description": "Information is the most fundamental aspect of reality",
                "quote": "The universe is not just described by information; it is information."
            },
            "semantic_information": {
                "importance": 9,
                "description": "Information is inherently meaningful and relational",
                "quote": "Reality is not made of stuff, but of semantics - meaningful relationships between bits of information."
            },
            "quantum_darwinism": {
                "importance": 8,
                "description": "A theory explaining the emergence of classical reality from quantum substrates",
                "quote": "Quantum Darwinism shows how the classical world emerges from the quantum realm through information selection."
            },
            "embodied_cognition": {
                "importance": 9,
                "description": "Cognitive processes are deeply rooted in the body's interactions with the world",
                "quote": "Cognition isn't just in the head; it involves the entire body and its environment."
            },
            "consciousness": {
                "importance": 10,
                "description": "A fundamental aspect of reality, potentially intrinsic to information processing",
                "quote": "Consciousness is not something the brain does; it's something the brain participates in."
            },
            "measurement_problem": {
                "importance": 9,
                "description": "The issue in quantum mechanics regarding the nature of measurement and observation",
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
                "quote": "The costs of information processing shape the very nature of cognition and reality."
            },
            "category_theory": {
                "importance": 7,
                "description": "A mathematical framework for describing structures and relationships",
                "quote": "Category theory provides a language for describing the deep structure of reality that transcends the limitations of set theory."
            },
            "predictive_processing": {
                "importance": 9,
                "description": "Perception and cognition are fundamentally predictive processes",
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
            belief: True for belief in [
                "reality_is_observer_dependent", "information_is_fundamental", "consciousness_is_fundamental",
                "cognition_extends_beyond_brain", "quantum_effects_relevant_to_cognition", "free_will_is_illusion",
                "self_is_constructed", "perception_is_active_inference", "reality_is_unified_information_space",
                "measurement_creates_reality", "time_is_emergent", "space_is_emergent", "holographic_principle_applies_to_cognition",
                "hard_problem_of_consciousness_is_solvable", "observer_and_observed_are_inseparable", "reality_is_fundamentally_semantic",
                "quantum_decoherence_explains_classical_reality", "cognition_is_quantum_computational", "information_has_physical_consequences",
                "consciousness_is_intrinsic_to_information_processing", "context_is_fundamental_to_information", "cognitive_illusions_reveal_fundamental_truths",
                "quantum_darwinism_explains_classical_emergence", "thermodynamics_constrains_cognition", "category_theory_describes_deep_structure_of_reality",
                "active_inference_applies_to_all_self_organizing_systems", "free_energy_principle_is_universal", "reality_is_fundamentally_relational",
                "information_processing_has_intrinsic_cost", "observer_observed_distinction_is_artificial"
            ]
        }
    
    def methodologies(self) -> List[str]:
        return [
            "Information theory", "Quantum mechanics", "Active inference", "Free energy principle", "Bayesian inference",
            "Category theory", "Cognitive neuroscience", "Philosophy of mind", "Computational modeling", "Interdisciplinary synthesis",
            "Quantum information theory", "Holographic models", "Graph theory", "Formal semantics", "Thermodynamics of computation",
            "Quantum cognition models", "Information-theoretic approaches to consciousness", "Predictive processing frameworks",
            "Quantum decoherence analysis", "Semantic network analysis", "Quantum Darwinism modeling", "Contextual analysis",
            "Cognitive illusion studies", "Information-theoretic cost analysis", "Holographic cognitive integration modeling",
            "Category-theoretic modeling of cognition", "Observer-dependent reality simulations", "Semantic information processing models",
            "Embodied cognition experiments", "Quantum measurement theory"
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
            "Quantum Darwinism shows how the classical world emerges from the quantum realm through information selection.",
            "The costs of information processing shape the very nature of cognition and reality.",
            "The hard problem of consciousness and the measurement problem in quantum mechanics are deeply connected. Solving one may solve the other.",
            "The brain doesn't create consciousness; it constrains it.",
            "Reality is not a collection of things, but a network of relationships.",
            "The distinction between epistemology and ontology breaks down at the quantum level.",
            "Information is physical, and physics is informational.",
            "The universe computes its own evolution."
        ]

    def key_papers(self) -> List[Dict[str, str]]:
        return [
            {"title": "If Physics Is an Information Science, What Is an Observer?", "description": "Explores the idea of observers as information-processing systems and its implications for physics and cognition."},
            {"title": "Conscious observation and the measurement problem in quantum mechanics", "description": "Discusses the role of consciousness in quantum measurement and its implications for our understanding of reality."},
            {"title": "Some consequences of the thermodynamic cost of system identification", "description": "Examines the energetic costs of perception and cognition from an information-theoretic perspective."},
            {"title": "A holographic model of cognitive integration and quantum cognition", "description": "Proposes a model of cognition based on the holographic principle and quantum information theory."},
            {"title": "Decoherence and the theory of the subject", "description": "Explores the relationship between quantum decoherence and the emergence of classical reality and subjectivity."},
            {"title": "On the reality of cognitive illusions", "description": "Examines the nature of cognitive illusions from an information-theoretic perspective, challenging traditional notions of perception and reality."},
            {"title": "Quantum Darwinism as a darwinian process", "description": "Analyzes the concept of quantum Darwinism and its implications for the emergence of classical reality from quantum substrates."},
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




        Catechism (Comprehensive Project Description):
        ## Comprehensive Project Catechism

**1. Project Essence and Vision**
- What core problem or opportunity does your project address?
- Can you succinctly articulate your project's purpose without jargon?
- What inspired or initiated this project?
- How does this initiative align with your organization's mission, values, and strategy?
- What are the primary objectives and key results (OKRs) for this project?
- How does this project advance knowledge or practice in its field?

**2. Current Landscape Analysis**
- What is the current state of the art in this field?
- Who are the key players, competitors, and thought leaders?
- What are the limitations or gaps in existing solutions?
- Are there any regulatory, legal, or ethical considerations impacting this project?
- What recent technological advancements or societal shifts make this project relevant now?
- How does your project fit into or challenge current paradigms?

**3. Innovation and Methodological Approach**
- What is novel or groundbreaking about your approach?
- How does your solution differ from and improve upon existing alternatives?
- What specific technologies, methodologies, or theoretical frameworks will you use?
- Have you conducted preliminary experiments or pilot studies? What were the results?
- How scalable and adaptable is your proposed solution?
- What interdisciplinary approaches or collaborations does your project leverage?

**4. Impact and Significance Assessment**
- Who are the primary beneficiaries or target audiences?
- What quantifiable impact do you expect in the short, medium, and long term?
- How does this project contribute to long-term goals or grand challenges in the field?
- Are there any potential unintended consequences, both positive and negative?
- How will you measure, evaluate, and communicate the project's success and impact?
- What is the potential for this project to create paradigm shifts or breakthrough innovations?

**5. Comprehensive Risk Assessment**
- What are the top risks that could derail the project?
- Are there any ethical concerns or potential controversies?
- What technical challenges or obstacles do you anticipate?
- How might market conditions, geopolitical factors, or other external variables affect the project?
- What contingency plans and risk mitigation strategies do you have?
- How will you address potential resistance or skepticism from stakeholders or the public?

**6. Resource Requirements and Allocation**
- What is the estimated total budget, and how is it justified?
- How is the budget allocated across major categories (e.g., personnel, equipment, operations)?
- What human resources are required, including specific expertise and potential new hires?
- What equipment, infrastructure, or technological investments are necessary?
- Are there any critical dependencies on external resources, partnerships, or collaborations?
- How will you ensure efficient use of resources and prevent scope creep?

**7. Timeline, Milestones, and Project Management**
- What is the projected timeline from initiation to completion, including major phases?
- What are the key milestones, deliverables, and decision points?
- How have you accounted for potential delays, setbacks, or necessary iterations?
- What is the critical path for the project, and how will you manage dependencies?
- How will you track, report, and communicate progress to stakeholders?
- What project management methodologies or tools will you use to ensure efficient execution?

**8. Evaluation Framework and Success Criteria**
- What specific metrics and key performance indicators (KPIs) will you use to measure success?
- How will you conduct ongoing evaluations and mid-project assessments?
- What constitutes a minimum viable product (MVP) or initial success threshold?
- How will you gather, analyze, and incorporate user feedback and stakeholder input?
- What are your criteria for deciding to pivot, scale, or terminate the project if necessary?
- How will you ensure objectivity and rigor in your evaluation process?

**9. Team Composition and Expertise**
- Who are the key team members, and what are their roles and responsibilities?
- What unique expertise, skills, or experience does each team member bring?
- Are there any skill gaps or areas where additional expertise is needed?
- How will you foster collaboration, communication, and knowledge sharing within the team?
- What external advisors, mentors, or subject matter experts will you consult?
- How will you promote diversity, equity, and inclusion within your team and project execution?

**10. Market Analysis and Commercialization Strategy**
- Who is your target market, user base, or beneficiary group?
- What is the potential market size and growth trajectory for your solution?
- How will you price, monetize, or sustain your product/service?
- What is your go-to-market strategy, including marketing and distribution plans?
- How will you protect your intellectual property and maintain a competitive advantage?
- What partnerships or alliances might be beneficial for market penetration or scaling?

**11. Sustainability and Scalability Planning**
- How will the project sustain itself beyond the initial funding or implementation phase?
- What is the long-term vision for the project, product, or service?
- How will you scale the solution if it proves successful?
- What potential spin-off projects, applications, or research directions do you foresee?
- How will you ensure the project's environmental sustainability and social responsibility?
- What strategies will you employ to maintain relevance and adapt to changing conditions over time?

**12. Stakeholder Engagement and Communication**
- Who are the key stakeholders, both internal and external?
- How will you engage, communicate with, and manage expectations of diverse stakeholders?
- What potential resistance or opposition might you face, and how will you address it constructively?
- How will you deliver regular updates and maintain transparency throughout the project lifecycle?
- What partnerships or collaborations are crucial for success, and how will you nurture them?
- How will you leverage stakeholder expertise and feedback to improve the project?

**13. Learning, Adaptation, and Knowledge Management**
- How will you capture, document, and share lessons learned throughout the project?
- What mechanisms do you have for rapid iteration, adaptation, and continuous improvement?
- How will you encourage innovation, creative problem-solving, and calculated risk-taking within the team?
- What benchmarking or best practices will you adopt from other industries or fields?
- How will you contribute to the broader knowledge base in your field?
- What systems will you implement for effective knowledge management and organizational learning?

**14. Ethical Considerations and Responsible Innovation**
- What ethical frameworks or guidelines will you adhere to?
- How will you address potential ethical dilemmas or conflicts?
- What measures will you take to ensure data privacy, security, and responsible use of information?
- How will you consider and mitigate potential negative societal impacts of your innovation?
- What strategies will you employ to ensure fairness, transparency, and accountability?
- How will you engage with relevant ethical review boards or oversight committees?

**15. Future Outlook and Strategic Positioning**
- How does this project position your organization or field for future developments?
- What emerging trends or technologies might impact the long-term relevance of your project?
- How will you stay ahead of the curve and anticipate future challenges or opportunities?
- What is your vision for the next generation of research or innovation building on this project?
- How will you leverage the outcomes of this project to secure future funding or support?
- What is the potential for this project to create lasting change or transformation in its domain?

**16. Grant Team and Internal Coordination**
- Who are the key members of the grant team, and what are their specific roles and responsibilities?
- What criteria will you use to include team members in the grant project?
- How will you ensure that the team has the necessary expertise and skills to achieve the project's objectives?
- What internal deadlines are associated with important milestones, and how will you manage them?
- How will you foster effective communication and collaboration within the grant team?
- What strategies will you use to ensure accountability and track progress against internal deadlines?
- How will you handle potential conflicts or challenges within the team?
- What mechanisms will you put in place to ensure continuous improvement and adaptation throughout the project lifecycle?
- How will you ensure that the grant team adheres to the project's ethical guidelines and standards?



        Grant Call (Agency Requirements):
        Naval Information Warfare Systems Center, Pacific (NIWC Pacific)  
53560 Hull Street  
San Diego, CA 92152-5001  

In collaboration with the  
Intelligence Advanced Research Projects Activity  
Broad Agency Announcement (BAA)  
Biointelligence and Biosecurity for the Intelligence Community (B24IC) Seedling Research Topic  
N66001-22-S-4704 Amendment 01  
Release Date: 7 July 2022  

## Table of Contents
1. Overview Information ................................................................................................................................ 3  
2. Award Information ..................................................................................................................................... 7  
3. Eligibility Information ................................................................................................................................ 8  
4. Application and Submission Information ................................................................................................. 9  
5. Evaluation of White Papers/Proposals .................................................................................................... 17  
6. Award Administration Information ....................................................................................................... 20  
7. APPENDIX A - BAA Attachments ......................................................................................................... 28  

## 1. Overview Information
This notice constitutes a Broad Agency Announcement (BAA) and sets forth research of interest in the area described in detail below. The solicitation process will follow Federal Acquisition Regulation (FAR) Part 35, Research and Development Contracting, as supplemented with additional information included in this notice. Awards based on responses to this BAA will be considered the result of full and open competition.

- **Federal Agency Name**: Naval Information Warfare Center, Pacific (NIWC Pacific) on behalf of the Office of the Director of National Intelligence/Intelligence Advanced Research Projects Activity (IARPA)
- **Funding**: RDT&E (2 year)
- **Funding Opportunity Title**: Biointelligence and Biosecurity for the Intelligence Community Seedling Research Topics
- **Announcement Type**: Initial Announcement
- **Funding Opportunity Number**: N66001-22-S-4704
- **Catalog of Federal Domestic Assistance (CFDA) Number**: Not applicable
- **Dates**:
  - White papers (abstracts) Due Date: 5:00PM ET, 25 July, 2022 (Offerors are required to submit white papers before submitting a proposal. White papers may be submitted any time between release of the BAA until 5:00PM ET, 19 July, 2022.
  - Proposal Due Date: 5:00PM ET, 13 September, 2022. (A BAA amendment will be issued to announce subsequent rounds of selections, if any)
- **Anticipated individual awards**: Multiple awards are anticipated; the Government reserves the right to select for award all, some, one, or none of the proposals received in response to this announcement.
- **Types of instruments that may be awarded**: Procurement contracts[^1]
- **Amendments**: Any amendments to this BAA will be posted via NAVWAR e-Commerce Central at [https://e-commerce.sscno.nmci.navy.mil](https://e-commerce.sscno.nmci.navy.mil) (Note that this does not include a "www" prefix).
- **Agency Contact**:
  - IARPA Program Email: [dni-iarpa-B24IC-BAASubmission-2022@iarpa.gov](mailto:dni-iarpa-B24IC-BAASubmission-2022@iarpa.gov)
  - Eric Pomroy (Primary)  
    Contract Specialist  
    Email: [Eric.R.Pomroy.civ@us.navy.mil](mailto:Eric.R.Pomroy.civ@us.navy.mil)
  - Stephen Enokida (Alternate)  
    Contracting Officer  
    Email: [Stephen.I.Enokida.civ@us.navy.mil](mailto:Stephen.I.Enokida.civ@us.navy.mil)
- **Program Manager (PM)**: Michael Patterson, Ph.D.
- **Program Website**: [https://www.iarpa.gov/index.php/research-programs](https://www.iarpa.gov/index.php/research-programs)

### BAA Summary
IARPA seeks to develop and incorporate novel technologies and knowledge, leveraging the wider synthetic biology and biotechnology fields, to meet biosecurity threats of the 21st century. This includes developing new methods to collect, detect, analyze, and prevent traditional biothreats, while also addressing the latest opportunities and vulnerabilities associated with the advancing fields of biotechnology and synthetic biology.

The Intelligence Advanced Research Projects Activity (IARPA) invests in high-risk/high-payoff research programs that have the potential to provide our nation with an overwhelming intelligence advantage. IARPA seeks to develop new capabilities, matching the wider synthetic biology and biotechnology fields, ensuring the Intelligence Community’s (IC’s) capability to meet the biointelligence and biosecurity threats of the 21st century. This includes developing new ways to collect, detect, analyze, and prevent traditional biothreats while also addressing the promise and perils associated with the growing fields of biotechnology and synthetic biology. To address these challenges, the IC seeks to advance research across multiple sub-disciplines of biology.

In recent decades, the rise of synthetic biology has corresponded with critical advances in biology research. From polymerase chain reaction (PCR) in the 1980s to next generation sequencing (NGS) in the late 90s to numerous mechanisms for genetic engineering enabling a variety of engineered organisms in the past decade, the branches of synthetic biology and enabling biotechnologies have advanced at a prodigious rate. The IC, and IARPA specifically, has pursued numerous research programs to advance security interests, but the needs of the IC require rapid advancement of numerous research topics to meet and leverage the advances the many biological disciplines have brought into reality in the past decades. These needs align with developing new methods for countering traditional biothreats of concern while also looking towards the future where bio-focused capabilities may enable or support IC relevant capabilities.

In particular, IARPA seeks novel research ideas from multidisciplinary teams pursuing advanced research topics capable of supporting the below interests:

- **Biointelligence**: Instruments, knowledge, and/or methods enhancing the IC’s capability to counter inappropriate use of biological sciences or leverage advancements derived from the biological sciences capable of advancing the IC’s ability to collect, analyze, characterize, secure, and utilize information related to threats to our nation.
- **Biosecurity**: Methods for ensuring the security of instruments, knowledge, environments, or capabilities aligned with biological research or advancements which have the potential to cause harm or detrimentally impact other organisms, materials, or infrastructure.

These technologies align well with needs of the intelligence and national security communities and are, therefore, under the purview of IARPA’s research mission. Successful technology solutions will require creative, multidisciplinary methods, paradigm changing thinking, and transformative approaches. Preference will be given to research with the ability to revolutionize capabilities and instruments or demonstrate that revolutionary change is possible in the coming decade. Critical interests align with technologies to improve targeting, collections, analysis, characterization, and mission specific capabilities. Multidisciplinary or convergent approaches derived from other technical fields and disciplines are welcome and encouraged.

This BAA solicits short-term, limited scope research in topic areas that are not addressed by emerging or ongoing IARPA programs or other published IARPA solicitations. It is primarily, but not solely, intended for early-stage research that may lead to larger, focused programs through a separate BAA in the future.

Seedlings are structured as a Phase A base with a Phase B option. Phase A represents an initial proof of concept of the proposed approach. Phase B, if exercised, will build upon the proof-of-concept research in Phase A to deliver a demonstration. Phase A shall be of a duration of 9 months to demonstrate prototype proof-of-concept, with preliminary reports due at month 4 and month 8. The reports shall be used in evaluation of projects for continuation to Phase B. Phase B shall be no longer than 15 months in duration. Shorter duration projects, if appropriate for the subject matter, may be considered. See Figure 1 for a proposed project timeline.

**Figure 1: Proposed Phase A + B timeline with key activities.**

Proposals must explicitly address relevance of the technical approach to the future potential of biointelligence and biosecurity in the United States. Proposals shall demonstrate that the proposed effort has the potential to make revolutionary, rather than incremental, improvements to current capabilities. Research that primarily results in evolutionary improvement to the existing state of practice is specifically excluded.

Proposals must include offeror-defined objectives, as well as milestones and performance metrics as task-driven intermediate steps towards the objectives.

### 1.1 Description of Topics and Areas of Interest

#### A. Biointelligence
- Methods and approaches for enabling attribution and/or origination of biological material, including organisms, that are not based purely upon individual databases, plasmid-focused analytics, isotopic ratios, or bioinformatics data.
- Platform-based, highly sensitive, target agnostic or multiplexable plug-and-play target-specific instrumentation for detection of biomolecules from complex samples or environments.
- Approaches for building biological systems capable of autonomous and consistent/repeatable responses and reporting outputs following non-Boolean logic based upon external stimuli to include advances in biocomputing, bioelectronics, and biological/biomolecule neural networks.
- Advanced approaches for loss-less, shelf-stable collection, separation, and/or sterilization of diverse biomolecules from complex environments (soil, water, and/or air).
- Approaches for integrating structured and unstructured, multi-modal data types, beyond bioinformatically derived, to identify poorly or under reported health incidents or changes in health status.

#### B. Biosecurity
- Methods for assuring digital and physical security associated with infrastructure, instrumentation, databases, and data associated with synthetic biology, biological samples, and biotechnologies from direct, indirect, remote, and stand-off analysis or intrusion.
- Methods for detecting and/or characterizing biological targets of interest to include venoms, toxins, community/environmental metabolomics, antibody paratopes (linear and conformational), non-canonical/synthetic biomolecules, and properties/effects of encapsulation.
- Methods and instruments for near and remote, >1 meter, passive detection or evaluation of health-status or health anomalies.
- Methods for reducing storage requirements, enabling improved security and analysis of large or mixed ‘omics datatypes, and improving transfer of pre-processed ‘omics data at scale from the point of generation.
- Methods for integrating and analyzing multi-modal data or materials, informing towards improved understanding and prediction, in near real-time, of research activities, timelines, objectives.

The following topics are out of scope for this seedling effort: research focused purely on improving biosafety in the laboratory or the field; research focused on systems integration of existing approaches or instruments; research focused entirely on improving size, weight, or power requirements associated with existing instrumentation; research focused entirely on COVID-19 or SARS-CoV-2; research focused on developing or improving medical countermeasures or therapeutics; research focused on topics at a technology readiness level of 4 or above; and/or research which are resubmissions of work already awarded by the National Science Foundation, National Institutes of Health, Department of Defense, Intelligence Community, or other federal agencies.

### 1.2 Proposal Information and Structure
The Government anticipates that proposals submitted in response to this BAA will be UNCLASSIFIED.

Proposals must address two independent and sequential project phases: Phase A - Initial Proof of Concept (base) and Phase B - Demonstration (option). The periods of performance for these phases shall not exceed 9 months for Phase A and 15 months for Phase B. Combined Phase A and Phase B shall not exceed 24 months. Specific technical objectives to be achieved within the topic areas listed above, task descriptions, intellectual property rights, milestone schedule, and deliverables shall be addressed in the proposal. Detailed proposal preparation instructions are provided in Section 4. The total award value for the combined Phase A base and Phase B option shall be less than $4,000,000.

## 2. Award Information

### 2.1 General Award Information
The BAA shall result in awards for both Phases of the seedling. Exercise of the Phase B option shall depend upon performance during Phase A - base as well as program goals, the availability of funding, and IARPA priorities. Exercising of the Phase B option is at the sole discretion of the Government. Multiple awards are anticipated. The amount of resources made available under this BAA shall depend on the quality of the proposals received and the availability of funds.

The Government reserves the right to select for negotiation all, some, one, or none of the proposals received in response to this solicitation and to make awards without discussions with Offerors. The Government also reserves the right to conduct discussions if determined to be necessary. Evaluation and award of proposals will follow FAR Part 35 processes as described herein.

Proposals selected for negotiation may result in a procurement contract. Awards under this BAA shall be made to Offerors on the basis of the Evaluation Factors listed herein, as well as successful completion of negotiations.

This announcement constitutes the full solicitation package. This solicitation will be conducted in two steps:

**STEP ONE** – Submission of white papers. This submission is required to continue to step two.

**STEP TWO** – A reasonable number of Offerors apparently qualified to respond to the intent of this BAA who submit whitepapers in step one will be approved and notified to submit a technical and cost proposal. Offerors not approved to submit a proposal from step one or that do not submit a whitepaper will not have their proposals reviewed by the government. All proposals must be submitted by the due date listed in Section 1 of this BAA.

See Section 4.0 of this announcement for further details regarding the proposal requirements.

Upon evaluation, the Government will contact Offerors whose proposals are selected for negotiations and may request additional information required for award. The Government may establish a deadline for the close of fact-finding and negotiations that allows a reasonable time for the award of a contract. Offerors that are not responsive to Government deadlines established and communicated with the request may be removed from award consideration. Offerors may also be removed from award consideration should the parties fail to reach agreement within a reasonable time on contract terms, conditions, and cost/price.

### 2.2 Multiple Submissions to the BAA
Organizations may participate as a prime or subcontractor in more than one submission to the BAA. However, if multiple submissions to the BAA which include a common team member are selected, such common team members shall not receive duplicative funding (i.e., no one entity can be paid twice to perform the same task).

## 3. Eligibility Information

### 3.1 Eligible Applicants
All responsible sources capable of satisfying the Government's needs may submit a proposal. Historically Black Colleges and Universities, Small Businesses, Small Disadvantaged Businesses and Minority Institutions are encouraged to submit proposals and team with others to submit proposals; however, no portion of this announcement shall be set aside for these organizations’ participation due to the impracticality of reserving discrete or severable areas for exclusive competition among these entities. Other Government Agencies, Federally Funded Research and Development Centers, University Affiliated Research Centers, Government-Owned, Contractor-Operated facilities, Government Military Academies, and any other similar type of organization that has a special relationship with the Government, that gives them access to privileged and/or proprietary information or access to Government equipment or real property, are not eligible to submit proposals under this BAA or participate as team members under proposals submitted by eligible entities. An entity of which only a portion has been designated as a UARC may be eligible to submit a proposal or participate as a team member subject to an organizational conflict of interest review.

#### 3.1.1 U.S. Academic Institutions
According to Executive Order 12333, as amended, paragraph 2.7, “Elements of the Intelligence Community are authorized to enter into contracts or arrangements for the provision of goods or services with private companies or institutions in the United States and need not reveal the sponsorship of such contracts or arrangements for authorized intelligence purposes. Contracts or arrangements with academic institutions may be undertaken only with the consent of appropriate officials of the institution.”

Offerors shall submit a completed and signed Academic Institution Acknowledgment Letter for each U.S. academic institution that is a part of their team, whether the academic institution is serving in the role of a prime, or a subcontractor or a consultant at any tier of their team with their proposal. Each Letter must be signed by a senior official from the institution (e.g., President, Chancellor, Provost, or other appropriately designated official). A template of the Academic Institution Acknowledgment Letter is enclosed in Appendix A of this BAA. Note: It is highly recommended that this letter(s) be submitted with the Offeror’s proposal. In any case, IARPA shall not enter into negotiations with an Offeror whose team includes a U.S. academic institution until all required Academic Institution Acknowledgment Letters are received.

#### 3.1.2 Foreign Entities
Foreign entities and/or individuals may participate only as a prime if they are registered with SAM.gov and have a United States bank account or as part of a U.S. based team. The prime contractor must be a U.S. company in the case the entities or individuals do not have an account or are not registered with SAM.gov. All foreign participation must comply with any necessary Non-Disclosure Agreements, Security Regulations, Export Control Laws and other governing statutes applicable under the circumstances. Offerors are expected to ensure that the efforts of foreign participants do not either directly or indirectly compromise the laws of the United States, nor its security interests. As such, all Offerors should carefully consider the roles and responsibilities of foreign participants as they pursue teaming arrangements.

### 3.2 Organizational Conflicts of Interest
According to FAR 2.101 “Organizational Conflict of Interest” (OCI) means that because of other activities or relationships with other persons, a person is unable or potentially unable to render impartial assistance or advice to the Government, or the person’s objectivity in performing the contract work is or might be otherwise impaired, or a person has an unfair competitive advantage.

In accordance with FAR 9.5, Offerors are required to identify and disclose all facts relevant to potential OCIs involving the Offeror’s organization and any proposed team member (subawardee, consultant). Under this Section, the Offeror is responsible for providing this disclosure with each proposal submitted pursuant to the BAA. The disclosure must include the Offeror’s, and as applicable, proposed team member’s OCI mitigation plan. The OCI mitigation plan must include a description of the actions the Offeror has taken, or intends to take, to prevent the existence of conflicting roles that might bias the Offeror’s judgment and to prevent the Offeror from having an unfair competitive advantage. The OCI mitigation plan will specifically discuss the disclosed OCI in the context of each of the OCI limitations outlined in FAR 9.505-1 through FAR 9.505-4.

Naval Information Warfare Systems Center, Pacific (NIWC Pacific)  
53560 Hull Street  
San Diego, CA 92152-5001  
In collaboration with the  
Intelligence Advanced Research Projects Activity  
Broad Agency Announcement (BAA)  
Biointelligence and Biosecurity for the Intelligence Community (B24IC) Seedling Research Topic  
N66001-22-S-4704 Amendment 01  
Release Date: 7 July 2022  

Naval Information Warfare Systems Center, Pacific (NIWC Pacific)
53560 Hull Street
San Diego, CA 92152-5001
In collaboration with the
Intelligence Advanced Research Projects Activity
Broad Agency Announcement (BAA)
Biointelligence and Biosecurity for the Intelligence Community (B24IC) Seedling Research Topic
N66001-22-S-4704 Amendment 01
Release Date: 7 July 2022
Table of Contents
1 Overview Information ................................................................................................................................ 3
2 Award Information..................................................................................................................................... 7
3 Eligibility Information................................................................................................................................ 8
4 Application and Submission Information................................................................................................. 9
5 Evaluation of White Papers/Proposals.................................................................................................... 17
6 Award Administration Information ....................................................................................................... 20
7 APPENDIX A - BAA Attachments ......................................................................................................... 28
3
1 Overview Information
This notice constitutes a Broad Agency Announcement (BAA) and sets forth research of interest in
the area described in detail below. The solicitation process will follow Federal Acquisition Regulation
(FAR) Part 35, Research and Development Contracting, as supplemented with additional information
included in this notice. Awards based on responses to this BAA will be considered the result of full
and open competition.
• Federal Agency Name: Naval Information Warfare Center, Pacific (NIWC Pacific) on
behalf of the Office of the Director of National Intelligence/Intelligence Advanced Research
Projects Activity (IARPA)
• Funding: RDT&E (2 year)
• Funding Opportunity Title: Biointelligence and Biosecurity for the Intelligence
Community Seedling Research Topics
• Announcement Type: Initial Announcement
• Funding Opportunity Number: N66001-22-S-4704
• Catalog of Federal Domestic Assistance (CFDA) Number: Not applicable
• Dates:
o White papers (abstracts) Due Date: 5:00PM ET, 25 July, 2022 (Offerors are
required to submit white papers before submitting a proposal. White papers may be
submitted any time between release of the BAA until 5:00PM ET, 19 July, 2022.
o Proposal Due Date: 5:00PM ET, 13 September, 2022. (A BAA amendment will be
issued to announce subsequent rounds of selections, if any)
• Anticipated individual awards: Multiple awards are anticipated; the Government reserves
the right to select for award all, some, one, or none of the proposals received in response to
this announcement.
• Types of instruments that may be awarded: Procurement contracts1
• Amendments: Any amendments to this BAA will be posted via NAVWAR e-Commerce
Central at https://e-commerce.sscno.nmci.navy.mil (Note that this does not include a "www"
prefix).
• Agency Contact:
IARPA Program Email: dni-iarpa-B24IC-BAASubmission-2022@iarpa.gov
Eric Pomroy (Primary)
Contract Specialist
Email: Eric.R.Pomroy.civ@us.navy.mil
Stephen Enokida (Alternate)
Contracting Officer
Email: Stephen.I.Enokida.civ@us.navy.mil
• Program Manager (PM):

1 Procurement Contract: This is a standard government contract that follows the processes, format and terms and conditions as
outlined in the Federal Acquisition Regulations (FAR) and supplementing Agency specific regulations.
4
Michael Patterson, Ph.D.
• Program Website:
https://www.iarpa.gov/index.php/research-programs
BAA Summary – IARPA seeks to develop and incorporate novel technologies and knowledge,
leveraging the wider synthetic biology and biotechnology fields, to meet biosecurity threats of the
21st century. This includes developing new methods to collect, detect, analyze, and prevent
traditional biothreats, while also addressing the latest opportunities and vulnerabilities associated
with the advancing fields of biotechnology and synthetic biology.
The Intelligence Advanced Research Projects Activity (IARPA) invests in high-risk/high-payoff
research programs that have the potential to provide our nation with an overwhelming intelligence
advantage. IARPA seeks to develop new capabilities, matching the wider synthetic biology and
biotechnology fields, ensuring the Intelligence Community’s (IC’s) capability to meet the
biointelligence and biosecurity threats of the 21st century. This includes developing new ways to
collect, detect, analyze, and prevent traditional biothreats while also addressing the promise and
perils associated with the growing fields of biotechnology and synthetic biology. To address these
challenges, the IC seeks to advance research across multiple sub-disciplines of biology.
In recent decades, the rise of synthetic biology has corresponded with critical advances in biology
research. From polymerase chain reaction (PCR) in the 1980s to next generation sequencing (NGS)
in the late 90s to numerous mechanisms for genetic engineering enabling a variety of engineered
organisms in the past decade, the branches of synthetic biology and enabling biotechnologies have
advanced at a prodigious rate. The IC, and IARPA specifically, has pursued numerous research
programs to advance security interests, but the needs of the IC require rapid advancement of
numerous research topics to meet and leverage the advances the many biological disciplines have
brought into reality in the past decades. These needs align with developing new methods for
countering traditional biothreats of concern while also looking towards the future where bio-focused
capabilities may enable or support IC relevant capabilities.
In particular, IARPA seeks novel research ideas from multidisciplinary teams pursuing advanced
research topics capable of supporting the below interests:
• Biointelligence –Instruments, knowledge, and/or methods enhancing the IC’s capability to
counter inappropriate use of biological sciences or leverage advancements derived from the
biological sciences capable of advancing the IC’s ability to collect, analyze, characterize, secure,
and utilize information related to threats to our nation; and
• Biosecurity - Methods for ensuring the security of instruments, knowledge, environments, or
capabilities aligned with biological research or advancements which have the potential to cause
harm or detrimentally impact other organisms, materials, or infrastructure.
These technologies align well with needs of the intelligence and national security communities and
are, therefore, under the purview of IARPA’s research mission. Successful technology solutions will
require creative, multidisciplinary methods, paradigm changing thinking, and transformative
approaches. Preference will be given to research with the ability to revolutionize capabilities and
instruments or demonstrate that revolutionary change is possible in the coming decade. Critical
interests align with technologies to improve targeting, collections, analysis, characterization, and
mission specific capabilities. Multidisciplinary or convergent approaches derived from other
technical fields and disciplines are welcome and encouraged. 
5
This BAA solicits short-term, limited scope research in topic areas that are not addressed by
emerging or ongoing IARPA programs or other published IARPA solicitations. It is primarily, but
not solely, intended for early-stage research that may lead to larger, focused programs through a
separate BAA in the future.
Seedlings are structured as a Phase A base with a Phase B option. Phase A represents an initial proof
of concept of the proposed approach. Phase B, if exercised, will build upon the proof-of-concept
research in Phase A to deliver a demonstration. Phase A shall be of a duration of 9 monthsto
demonstrate prototype proof-of-concept, with preliminary reports due at month 4 and month 8.The
reports shall be used in evaluation of projects for continuation to Phase B. Phase B shall be no longer
than 15 months in duration. Shorter duration projects, if appropriate for the subject matter, may be
considered. See Figure 1 for a proposed project timeline.
Figure 1: Proposed Phase A + B timeline with key activities.
Proposals must explicitly address relevance of the technical approach to the future potential of
biointelligence and biosecurity in the United States. Proposals shall demonstrate that the
proposed effort has the potential to make revolutionary, rather than incremental, improvements
to current capabilities. Research that primarily results in evolutionary improvement to the
existing state of practice is specifically excluded.
Proposals must include offeror-defined objectives, as well as milestones and performance
metrics as task-driven intermediate steps towards the objectives.
1.1 Description of Topics and Areas of Interest
A. Biointelligence
• Methods and approaches for enabling attribution and/or origination of biological material,
including organisms, that are not based purely upon individual databases, plasmid-focused
analytics, isotopic ratios, or bioinformatics data;
• Platform-based, highly sensitive, target agnostic or multiplexable plug-and-play targetspecific instrumentation for detection of biomolecules from complex samples or
environments;
• Approaches for building biological systems capable of autonomous and consistent/repeatable
responses and reporting outputs following non-Boolean logic based upon external stimuli to 
6
include advances in biocomputing, bioelectronics, and biological/biomolecule neural
networks;
• Advanced approaches for loss-less, shelf-stable collection, separation, and/or sterilization of
diverse biomolecules from complex environments (soil, water, and/or air);
• Approaches for integrating structured and unstructured, multi-modal data types, beyond
bioinformatically derived, to identify poorly or under reported health incidents or changes
in health status.
B. Biosecurity
• Methods for assuring digital and physical security associated with infrastructure,
instrumentation, databases, and data associated with synthetic biology, biological samples,
and biotechnologies from direct, indirect, remote, and stand-off analysis or intrusion;
• Methods for detecting and/or characterizing biological targets of interest to include venoms,
toxins, community/environmental metabolomics, antibody paratopes (linear and
conformational), non-canonical/synthetic biomolecules, and properties/effects of
encapsulation;
• Methods and instruments for near and remote, >1 meter, passive detection or evaluation of
health-status or health anomalies;
• Methods for reducing storage requirements, enabling improved security and analysis of large
or mixed ‘omics datatypes, and improving transfer of pre-processed ‘omics data at scale
from the point of generation;
• Methods for integrating and analyzing multi-modal data or materials, informing towards
improved understanding and prediction, in near real-time, of research activities, timelines,
objectives.
The following topics are out of scope for this seedling effort: research focused purely on improving
biosafety in the laboratory or the field; research focused on systems integration of existing
approaches or instruments; research focused entirely on improving size, weight, or power
requirements associated with existing instrumentation; research focused entirely on COVID-19 or
SARS-CoV-2; research focused on developing or improving medical countermeasures or
therapeutics; research focused on topics at a technology readiness level of 4 or above; and/or
research which are resubmissions of work already awarded by the National Science Foundation,
National Institutes of Health, Department of Defense, Intelligence Community, or other federal
agencies.
1.2 Proposal Information and Structure
The Government anticipates that proposals submitted in response to this BAA will be
UNCLASSIFIED.
Proposals must address two independent and sequential project phases: PhaseA - Initial Proof of
Concept (base) and Phase B - Demonstration (option). The periods of performance for these phases
shall not exceed 9 months for Phase A and 15 months for Phase B. Combined Phase A and Phase B
shall not exceed 24 months. Specific technical objectives to be achieved within the topic areas listed
above, task descriptions, intellectual property rights, milestone schedule, and deliverables shall be
addressed in the proposal. Detailed proposal preparation instructions are provided in Section 4. The 
7
total award value for the combined Phase A base and Phase B option shall be less than $4,000,000.
2 Award Information
2.1 General Award Information
The BAA shall result in awards for both Phases of the seedling. Exercise of the Phase B option shall
depend upon performance during Phase A - base as well as program goals, the availability of funding,
and IARPA priorities. Exercising of the Phase B option is at the sole discretion of the Government.
Multiple awards are anticipated. The amount of resources made available under this BAA shall
depend on the quality of the proposals received and the availability of funds.
The Government reserves the right to select for negotiation all, some, one, or none of the proposals
received in response to this solicitation and to make awards without discussions with Offerors. The
Government also reserves the right to conduct discussions if determined to be necessary. Evaluation
and award of proposals will follow FAR Part 35 processes as described herein.
Proposals selected for negotiation may result in a procurement contract.
Awards under this BAA shall be made to Offerors on the basis of the Evaluation Factors listed
herein, as well as successful completion of negotiations.
This announcement constitutes the full solicitation package. This solicitation will be conducted in
two steps:
STEP ONE – Submission of white papers. This submission is required to continue to step two.
STEP TWO – A reasonable number of Offerors apparently qualified to respond to the intent of this
BAA who submit whitepapers in step one will be approved and notified to submit a technical and
cost proposal. Offerors not approved to submit a proposal from step one or that do not submit a
whitepaper will not have their proposals reviewed by the government. All proposals must be
submitted by the due date listed in Section 1 of this BAA.
See Section 4.0 of this announcement for further details regarding the proposal requirements.
Upon evaluation, the Government will contact Offerors whose proposals are selected for
negotiations and may request additional information required for award. The Government may
establish a deadline for the close of fact-finding and negotiations that allows a reasonable time for
the award of a contract. Offerors that are not responsive to Government deadlines established and
communicated with the request may be removed from award consideration. Offerors may also be
removed from award consideration should the parties fail to reach agreement within a reasonable
time on contract terms, conditions, and cost/price.
2.2 Multiple Submissions to the BAA
Organizations may participate as a prime or subcontractor in more than one submission to the BAA.
However, if multiple submissions to the BAA which include a common team member are selected,
such common team members shall not receive duplicative funding (i.e., no one entity canbe paid 
8
twice to perform the same task).
3 Eligibility Information
3.1 Eligible Applicants
All responsible sources capable of satisfying the Government's needs may submit a proposal.
Historically Black Colleges and Universities, Small Businesses, Small Disadvantaged Businesses
and Minority Institutions are encouraged to submit proposals and team with others to submit
proposals; however, no portion of this announcement shall be set aside for these organizations’
participation due to the impracticality of reserving discrete or severable areas for exclusive
competition among these entities. Other Government Agencies, Federally Funded Research and
Development Centers, University Affiliated Research Centers, Government-Owned, ContractorOperated facilities, Government Military Academies, and any other similar type of organization that
has a special relationship with the Government, that gives them access to privileged and/or
proprietary information or access to Government equipment or real property, are not eligible to
submit proposals under this BAA or participate as team members under proposals submitted by
eligible entities. An entity of which only a portion has been designated as a UARC may be eligibleto
submit a proposal or participate as a team member subject to an organizational conflict of interest
review.
3.1.1 U.S. Academic Institutions
According to Executive Order 12333, as amended, paragraph 2.7, “Elements of the Intelligence
Community are authorized to enter into contracts or arrangements for the provision of goods or
services with private companies or institutions in the United States and need not reveal the
sponsorship of such contracts or arrangements for authorized intelligence purposes. Contracts or
arrangements with academic institutions may be undertaken only with the consent of appropriate
officials of the institution.”
Offerors shall submit a completed and signed Academic Institution Acknowledgment Letter for
each U.S. academic institution that is a part of their team, whether the academic institution is serving
in the role of a prime, or a subcontractor or a consultant at any tier of their team with their proposal.
Each Letter must be signed by a senior official from the institution (e.g., President, Chancellor,
Provost, or other appropriately designated official). A template of the Academic Institution
Acknowledgment Letter is enclosed in Appendix A of this BAA. Note: It is highly recommended
that this letter(s) be submitted with the Offeror’s proposal. In any case, IARPA shall not enter into
negotiations with an Offeror whose team includes a U.S. academic institution until all required
Academic Institution Acknowledgment Letters are received.
3.1.2 Foreign Entities
Foreign entities and/or individuals may participate only as a prime if they are registered with
SAM.gov and have a United States bank account or as part of a U.S. based team. The prime
contractor must be a U.S. company in the case the entities or individuals do not have an account or
are not registered with SAM.gov. All foreign participation must comply with any necessary NonDisclosure Agreements, Security Regulations, Export Control Laws and other governing statutes
applicable under the circumstances. Offerors are expected to ensure that the efforts of foreign
participants do not either directly or indirectly compromise the laws of the United States, nor its
security interests. As such, all Offerors should carefully consider the roles and responsibilities of
foreign participants as they pursue teaming arrangements.
3.2 Organizational Conflicts of Interest
9
According to FAR 2.101 “Organizational Conflict of Interest” (OCI) means that because of other
activities or relationships with other persons, a person is unable or potentially unable to render
impartial assistance or advice to the Government, or the person’s objectivity in performing the
contract work is or might be otherwise impaired, or a person has an unfair competitive advantage.
In accordance with FAR 9.5, Offerors are required to identify and disclose all facts relevant to
potential OCIs involving the Offeror’s organization and any proposed team member (subawardee,
consultant). Under this Section, the Offeror is responsible for providing this disclosure with each
proposal submitted pursuant to the BAA. The disclosure must include the Offeror’s, and as
applicable, proposed team member’s OCI mitigation plan. The OCI mitigation plan must includea
description of the actions the Offeror has taken, or intends to take, to prevent the existence of
conflicting roles that might bias the Offeror’s judgment and to prevent the Offeror from having an
unfair competitive advantage. The OCI mitigation plan will specifically discuss the disclosed OCIin
the context of each of the OCI limitations outlined in FAR 9.505-1 through FAR 9.505-4.
IARPA generally prohibits Contractors from concurrently providing Scientific Engineering
Technical Assistance (SETA), Advisory and Assistance Services (A&AS), or similar support
services and being a technical Contractor. Therefore, as part of the FAR 9.5 disclosure requirement
above, address whether an Offeror or an Offeror’s team member (e.g. sub-awardee, consultant) is
providing SETA, A&AS, or similar support (e.g., T&E services) to IARPA under: (a) a current
award or subaward; or (b) a past award or subaward.
• If SETA, A&AS, or similar support is or was being provided to IARPA, the proposal
must include: The name of the IARPA program or office receiving the support;
• The prime contract number; and
• Identification of proposed team member (sub-awardee, consultant) providing the
support.
As part of their proposal, Offerors shall include either (a) a copy of their OCI notification including
mitigation plan or (b) a written certification that neither they nor their subcontractor teammates have
any potential conflicts of interest, real or perceived. A sample certification is provided in Appendix
A.
The Government will evaluate OCIs and potential OCIs to determine whether they can be avoided,
neutralized or mitigated and/or whether it is in the Government’s interest to grant a waiver. The
Government will make OCI determinations, as applicable, for proposals that are otherwise
selectable under the BAA Evaluation Factors.
The Government may require Offerors to provide additional information to assist the Government in
evaluating OCIs and OCI mitigation plans.
If the Government determines that an Offeror failed to fully disclose an OCI; or failed to provide
the affirmation of IARPA support as described above; or failed to reasonably provide additional
information requested by Government to assist in evaluating the Offeror’s OCI and proposed OCI
mitigation plan, the Government may reject the proposal and withdraw it from consideration for
award.
4 Application and Submission Information
STEP ONE – White Paper Submission: Interested Offerors are required to submit white papers
prior to proposal submissions. White papers will be accepted until 5:00 PM ET, 25 July, 2022.
The Government anticipates that Offerors will receive a response to their white paper within 30 days 
10
of submission stating whether the Government approves the offeror to step two of this BAA,
submission of a proposal. The purpose of the white paper is to ensure proposals are submitted from
a reasonable number of apparently qualified sources with technical approaches/solutions of interest
to the Government.
STEP TWO – Proposal submission: Upon review of the white papers from step one, the
Government anticipates approving a reasonable number of apparently qualified offerors, whose
research ideas are of interest to the Government, to submit full proposals (Volume I, Technical and
Management Proposal, Volume 2 Cost/Price Proposal). In order to receive consideration for award,
Offerors must have received approval for submission in step one from the Government associated
with their white paper and compliant proposals should be received by the proposal due date in Section
1 of the BAA. Proposals received after this date will be considered late and may not be reviewed. If
there are any subsequent rounds of selection, the BAA will be amended to notify Offerors and to
provide the proposal due date forthe next round of selections. Selection for award remains
contingent on the technical and fundingavailability evaluation factors. Offerors not approved to
submit a proposal from step one or that do not submit a whitepaper will not have their proposals
reviewed by the government.
The Government intends to use Booz Allen Hamilton, Serco, Patriot Solutions Group, Airlin
Technologies, Bluemont Technology and Research, Navstar, Crimson Phoenix, Northwood Global
Solutions, and Onts & Quants, Inc., along with SMEs from other Government laboratories, federally
funded research and development centers (FFRDCs), and University-affiliated research centers
(UARCs) or to provide expert advice, regarding portions of the white papers and proposals submitted
to the Government and to provide logistical support in carrying out the evaluation process. All
Government and Contractor personnel shall have signed and be subject to the terms and conditions
of non-disclosure agreements. By submission of its white paper and/or proposal, an Offeror agrees
that its white paper and/or proposal information may be disclosed to employees of these
organizations for the limited purposes stated above. Offerors who object to this arrangement shall
provide clear notice of their objection as part of their submittal as indicated in the white
paper/proposal preparation instructions. If Offerors do not include a notice of objection to this
arrangement, the Government shall assume consent to the use of contractor support personnel in
assisting the review of submittal(s) under this BAA. Only Government personnel will make
evaluation and award determinations under this BAA.
All administrative correspondence and questions regarding this solicitation shall be directed by
email to dni-iarpa-B24IC-BAASubmission-2022@iarpa.gov. White paper and proposals shall be
submitted in accordance with the procedures stated in the BAA.
4.1 White paper Preparation Instructions
The white papers shall not exceed 3-pages summarizing Offeror qualifications and the Offeror’s
intended technical approach/solution to the BAA Topics and Areas of Interest, see Section 1.1.
White papers must concisely answer all the following questions:
Qualifications:
1. Summarize your organization’s qualifications to perform research and development in
the specific field of science and technology.
2. Provide a short description of present and past performance of similar work.
Heilmeier questions (Address in relation to the technical approach/solution for your intended
proposal): 
11
1. What are you trying to do?
2. How isit done at present? Who does it? What are the limitations of present approaches?
3. What is new about your approach? Why do you think that you can be successful at this
time?
4. If you succeed, what difference will it make?
5. How will you evaluate progress during and at the conclusion of the effort? (i.e., what are
your proposed milestones and metrics?)
The white paper shall not describe management nor detailed cost/price information. All white papers
shall be written in English. Additionally, text should be black and paper size 8-1/2 by 11- inch, white
in color with 1” margins from paper edge to text or graphic on all sides. Submissions should also use
Times New Roman font with font size not smaller than 12-point. Additionally, the font size for
figures, tables and charts should not be smaller than 10-point. All contents shall be clearly legible
with the unaided eye or the white paper may not be considered. White papers shall be submitted in
a PDF format.
The Government anticipates white papers submitted under this BAA will be UNCLASSIFIED.
All white papers shall be in the format given below. The Government reserves the right to reject a
white paper without review if the information requested below is not adequately addressed.
4.1.1 White paper structure
- Cover Sheet - Offerors will be prompted by IARPA’s electronic proposal submittal system,
IDEAS (see BAA Section 4.3), to complete a white paper cover sheet. It will also prompt Offerorsto
insert a cost/price. In this case, please include the proposal limit stated in BAA paragraph 1.2,
$3,999,999, as a placeholder as cost/price will not be assessed as part of the white paper review.
Offeror’s will also be prompted to indicate whether they have any objections to non-Government
personnel reviewing their white paper (see BAA Section 4). This system generated cover sheet is
not included in the white paper page count. Note: In addition to the system generated cover sheets,
proposals require additional cover sheets for the Technical/Management and Cost Volumes, which
are included in BAA Appendix A. These additional cover sheets are not required for the white paper.
- Qualifications
- Heilmeier questions
White paper not to exceed 3 pages.
4.2 Proposal Preparation Instructions
All proposals shall be in the format given below:
Proposals shall consist of Volume 1 - Technical and Management Proposal and Volume 2 –
Cost/Price Proposal. All proposals shall be written in English. Additionally, text should be black
and paper size 8-1/2 by 11-inch, white in color with 1” margins from paper edge to text or graphic on
all sides. Submissions should also use Times New Roman font with font size not smaller than12
point. Additionally, the font size for figures, tables and charts should not be smaller than 10 point.
All contents shall be clearly legible with the unaided eye or the proposal may not be considered.
Proposals shall be submitted in PDF version.
The Government anticipates proposals submitted under this BAA will be UNCLASSIFIED.
12
Proposals shall be valid for 120 days unless the Offeror proposes a shorter validity period.
The Government reserves the right to reject a proposal without review if the information requested
below is not adequately addressed.
Each proposal submitted in response to this BAA shall consist of the following:
4.2.1 Volume 1 – Technical & Management Proposal
- Cover Sheet (not included in page count)
- Transmittal Letter (limited to 1 page, not included in page count)
- Technical Proposal to include the Statement of Work (not to exceed 15 pages)
- Attachments (not included in page count)
1 – Academic Institution Acknowledgment Letter, if required
2 – Intellectual Property Rights 3 – OCI Notification or Certification
4 – Bibliography
The Cover Sheet template is included in Appendix A. Complete all sections and include as the
proposal cover. The Cover Sheet is not included in the page count.
The Transmittal Letter shall include the following (not to exceed one page):
Introduction of Offeror and team (subcontractors and consultants), the BAA number, Offeror’s
Program name, the proposal validity period, the type of contract vehicle being requested (Cost/CostPlus-Fixed-Fee/FFP/Cost-Sharing procurement contract) with a short rationale, any non-negotiable
conditions on which the offer is based (such as contract type, Intellectual Property(IP ) restrictions,
etc.), any restrictions from review (e.g., Government Eyes Only or restricted from certain entities,
see paragraph 4.0) and the Offeror’s points of contact information including: name, email and
phone number for both technical and administrative issues.
The Proposal shall include the mandatory elements specified in sections A. through C. below.
A. Technical Proposal Overview
• A technical overview of the proposed research and plan. Effectively and succinctly convey
the main objective, key innovations, expected impact, and other unique aspects of the
proposed research project. The overview must include a paragraph on the relevance of the
proposed research to the Intelligence Community mission, as well as a realistic timeframe
for implementation of results. This shall include a description of the key technical
challenges, a concise review of the technologies proposed to overcome these challenges and
achieve the project’s goal, and a clear statement of the novelty and uniqueness of the
proposed work are required. This section shall address in detail the following questions:
What is the proposed work attempting to accomplish or do? How is it done today, and what
are the limitations? Who or what will be affected and what will be the impact if the work is
successful?
• Summary of the products, transferable technology and deliverables associated with the
proposed research results. Describe measurable deliverables that show progress toward
achieving proposed milestones and goals. (All proprietary claims to the results, prototypes,
IP, or systems supporting and/or necessary for the use of the research, results, and/or
demonstration shall be detailed in proposal Attachment 2, Should no proprietary claims be
identified in Attachment 2, the Government shall receive Unlimited Rights, as defined in
13
FAR 52.227-14, to all technology and deliverables resulting from or delivered under this
BAA.)
• Schedule and milestones for the proposed research. Summarize, in table form the schedule
and milestones for the proposed research. Do not include proprietary information with the
milestone chart. (The milestone chart may become part of the resultant contract.)
• Related research. Include a brief summary of other research in this area, comparing the
significance and plausibility of the proposed innovations against competitive approaches to
achieve proposed objectives.
• Project contributors. Include a clearly defined organizational chart of all anticipated project
participants and affiliations (e.g. subcontractor, consultant), organized under functional roles
for the effort, along with the associated task number responsibilities for each. Provide a
summary of expertise of the proposed team, including any sub-awardees/consultants and key
personnel who will be executing the work. Identify a principal investigator (PI) for the project.
• Facilities. Describe the facilities and resources that will be used for the proposed effort,
including computational and experimental resources.
• Resource Share. Include the type of support, if any, the Offeror might request from the
Government, such as facilities, equipment, materials, or any such resources the Offeror is
willing to provide at no additional cost to the Government to support the research effort.
(Cost-sharing is not required from Offerors and is not an evaluation criterion but is
encouraged where there is a reasonable probability of a potential commercial application
related to the proposed research and development effort). The names of other federal, state
or local agencies or other parties receiving the proposal and/or funding the proposed effort. If
none, so state. Concurrent submission of the proposal to other organizations will not
prejudice its review but may impact IARPA’s decision to fund the effort.
• Quad Chat. A single slide capturing the seedling concept, impact, expected outcomes and an
overarching figure (refer to Appendix A.5).
B. Statement of Work (SOW)
This section shall provide a detailed, clearly defined plan for the technical tasks/subtasks to be
performed, by phase, their durations and the dependencies among them. For each task/subtask,
provide:
• A general description of the objective;
• A detailed description of the approach to be taken, developed in an orderly progression
and in enough detail to establish the feasibility of accomplishing the goals of the task;
• Identification of the primary organization responsible for task execution (prime, subcontractor, team member, etc.) by name;
• Quantifiable metrics, and reasoning for including, which the performers and
Government can use to evaluate research progress throughout the project;
• The exit criteria for each task/activity (i.e., a product, event or milestone that defines
its completion); and
• Identification of all deliverables (e.g. reports, software) to be provided to the
Government. 
14
Note: Do not include any proprietary information in the SOW (The SOW will be
incorporated into the resultant contract).
C. Technical Proposal Attachments (Not included in page count):
• Attachment 1: Academic Institution Acknowledgment Letter (see BAA Section 3.1.1. and
sample letter in Appendix A).
• Attachment 2: Intellectual Property and Data Rights Assertion (estimated not to exceed 2
pages, see template in Appendix A).
• Attachment 3: OCI notification including mitigation plan or Certification stating no OCI
(see BAA Section 3.2 and sample certification letter in Appendix A.)
• Attachment 4: Bibliography. A brief bibliography of relevant technical papers and research
notes (published and unpublished) which document the technical ideas on which the proposal
is based.
4.2.2 Volume 2: Cost/Price Proposal (No page Limit)
IARPA anticipates awarding Cost type procurement contracts. However, Offerors may request other
than a Cost type procurement contract (e.g. FFP, cost-share).
Regardless of the type of contract, the Offeror’s cost/price proposal shall contain sufficient
supporting information to establish the Offeror’s understanding of the project, the perception of
project risks, the ability to organize and perform the work and to support the realism and
reasonableness of the proposed cost/price, to the extent appropriate.
Offerors shall provide the detailed cost supporting information addressed below and in the Volume 2
Cost Element Spreadsheet, Appendix A. Offerors may submit alternative cost/price supporting
information or information in a different format; however, this will be subject to a CO determination
of acceptability. If alternative information and formatting are not found acceptable, the CO will
request the Offeror provide appropriate cost supporting information during negotiations. Examples
where alternative cost/price supporting information and formatting may be found acceptable are
when submitted by non-traditional contractors such as commercial entities that do not typically
accept FAR-based contracts, small businesses, start-up companies or foreign companies.
The Cost/Price Volume shall include the following:
A. Cost Element Breakdown and Total Cost Summary
Offerors shall submit an Excel document, in the format provided in Appendix A. It shall include
intact formulas and shall not be hard numbered. The base and option period cost data should roll up
into a total cost summary. The Excel files may be write-protected but shall not be password
protected.
• Completed cost element breakdown for the base period, option period and the total project
summary in the format provided in Appendix A.
• Total costs broken down by major task.
B. Narrative Supporting Information
In addition to the above, supporting cost and pricing information shall be provided in sufficient
detail to substantiate the Offeror’s cost estimates. Include a description of the basis of estimate
(BOE) in a narrative for each cost element and provide supporting documentation, as applicable: 
15
Direct Labor –Describe the basis of the proposed labor categories and rates and provide a copy of
the most recent Forward Pricing Rate Agreement (FPRA) with the Government. If Offerors do not
have a current FPRA with the Government, provide payroll records or contingency hire letters with
salary data to support each proposed labor category, including those for key individuals, and the
most recent Forward Pricing Rate Proposal Submission, if applicable. Offeror should also address
whether any portion of their labor rates is attributable to uncompensated overtime.
Labor Escalation Factor – State the proposed escalation rate and the basis for that rate (e.g., based
upon Global Insight indices, Cost Index or historical data). If the escalation rate is based upon
historical data, provide data to demonstrate the labor escalation trend. Provide a sample calculation
demonstrating application of the factor to direct labor.
Subcontracts (to include consultants and Inter-organizational Transfers (IOTs) – The Offeror is
responsible for compiling and providing full subcontractor proposals with the Cost Volume.
Subcontractor cost element sheets shall be completed for the base period, option period and the total
summary using the same format required for the prime contractor (See Appendix A). Consultant
letter(s) of commitment shall also be attached.
Information shall be presented in Excel with intact formulas using the format provided in Appendix
A. The Offeror shall also provide justification for why the subcontractor was selected and its
determination that the cost/price is fair and reasonable (Reference FAR Part 44 and FAR clause
52.244-2). If subcontractors have concerns about proprietary cost information, subcontractors can
submit their detailed cost proposal information directly to the CO during negotiations.
Materials and Equipment – Provide copies of quotes, bill of materials, historical data or any other
information including Offeror’s analysis to support proposed costs.
Travel - The proposed travel supporting detail shall include destination and purpose of the trip,
number of trips, number of travelers and days per trip and price per traveler in sufficient detail to
verify the BOE. Limited travel is anticipated. Offerors may require travel to meet with team
members. Offerors will not be required to travel to meet with IARPA. Proposed travel costs shall
comply with the limitations set forth in FAR Part 31.
Conference travel will not be authorized under this contract.
Other Direct Costs (ODCs) – ODCs shall be listed separately and supported by quotes, historical
data or any other information including the Offeror’s analysis.
Indirect Costs – The Offeror shall show indirect cost calculations, identify the proposed indirect rate
by fiscal year and period (base, option) and provide information on indirect cost pools and allocation
bases for each year and program period involved. If a Government agency recently audited the
Offeror’s indirect rates, the Offeror shall identify the agency that conducted the audit,when the rates
were approved and the period for which they are effective. Include a copy of this rate agreement.
Absent current Government rate recommendations, it is incumbent on the Offerorto provide some
other means of demonstrating indirect rate realism (e.g., 3 years of historical actual costs with
applicable pools and bases). If proposed rates vary significantly from historical experience, the
Offeror shall explain of the variance.
Cost sharing – Describe the source, nature and amount of cost-sharing, if any. (Acceptable formsof
cost share include (but may not be limited to): Cash contributions (application of discretionary
resources) from prime Offeror and/or subcontractor(s); unreimbursed labor; materials and
equipment; use of materials or equipment for program duration (lease value equivalent); and IP with
established market value. Non- acceptable forms of cost share include (but may not be limitedto):
foregone fee; foregone G&A and COM if using independent research and development (IR&D) as 
16
cost share; valuation of IP with no established market value; facilities or other assets accounted for
in overhead rates applied to labor; and capital assets without clear and direct contribution to the
program.)
Other Pricing Assumptions – Identify all pricing assumptions, that should be incorporated into the
resulting award instrument (e.g., use of Government Furnished Property/Facilities/Information,
access to Government Subject Matter Experts, etc.).
Facilities Capital Cost of Money (FCCM) – If proposing FCCM, the Offeror shall show FCCM cost
calculations, identify the proposed FCCM factors by contractor fiscal year and program yearand
provide a copy of the Forward Price Rate Agreement (FPRA), Forward Price Rate System (FPRS)
or Forward Pricing Rate Recommendation (FPRR), if available.
Profit/Fee - Identify the proposed profit or fee percentage and the proposed profit/fee base. Provide
justification for your proposed profit or fee.
Systems - For the systems listed below, provide a brief description of the cognizant federal agency
and audit results. If the system has been determined inadequate, provide a short narrative describing
the steps your organization has taken to address the inadequacies and the current status.If a formal
audit has been performed by a Government Agency, please provide a complete copy of the audit
report or adequacy determination letter. If the system has never received a formal Government
review and approval include a statement to that effect. Address whether your organization has
contracts that are Cost Accounting Standards (CAS) covered and if so, whether they are subject to
full or modified CAS coverage.
• Accounting system (if proposing a cost reimbursement contract)
4.3 White Paper and Proposal Submission Information
White papers and proposals shall be submitted electronically through the IARPA Distribution and
Evaluation System (IDEAS). Offerors interested in providing a submission in response to this BAA
shall first register by electronic means in accordance with the instructions provided on the following
web site: https://iarpa-ideas.gov. Offerors are strongly encouraged to register a few days prior to the
due date. Offerors who do not register in advance do so at their own risk, and IARPA shall not
extend the due date to accommodate such Offerors. Failure to register as stated shall prevent the
Offeror’s submittal of documents.
After registration has been approved, Offerors should upload a white paper or proposal, in ‘pdf’
format, or as otherwise directed (Excel, PowerPoint, etc.). Offerors are responsible for ensuring
compliant and timely submissions. Time management to upload and submit is wholly the
responsibility of the Offeror. The submittal due date and time for white papers is 5:00pm ET 25
July, 2022. The submittal due date and time for proposals is 5:00pm ET, 13 September, 2022.
Upon completing the white paper or proposal submission, the Offeror shall receive an automated
confirmation email from IDEAS. The Government strongly suggests that the Offeror document the
submission of their white paper or proposal package by printing the electronic receipt (time and date
stamped) that appears on the final screen following compliant submission of a white paper or
proposal to the IDEAS website.
Should an Offeror be unable to complete the electronic submittal, the Offeror shall employ the
following procedure. The Offeror shall send an e-mail dni-iarpa-B24IC-BAASubmission2022@iarpa.gov, prior to the due date and time specified in the BAA and indicate that an attempt
was made to submit electronically and that the submittal was unsuccessful. This e-mail shall include
contact information for the Offeror. Upon receipt of such notification, the Government will provide
17
additional guidance regarding submission. White papers or proposals submitted by any means other
than IDEAS shall not be considered unless the Offeror notified the Government of its unsuccessful
attempted electronic submittal and complied with the Government’s subsequent guidance regarding
submission.
It is at the Government’s sole discretion whether to call for a second round of proposals. Selection
of any subsequent rounds remains contingent on the technical and funding availability evaluation
factors.
Submissions received after the due date and time are deemed to be late and may not be reviewed.
Failure to comply with the submission procedures may result in the submittal not being evaluated.
Although classified proposals are not anticipated for this program, if an Offeror chooses to submita
classified white paper or proposal, the Offeror must first contact the Government via dni-iarpaB24IC-BAASubmission-2022@iarpa.gov and request consideration. The Government reserves the
right not to accept classified proposals or supporting information. In no case shall classified
information be uploaded into IDEAS.
Regarding proprietary markings, Offerors are responsible for clearly identifying proprietary
information. Submissions containing proprietary information must have the cover page and each
page containing such information clearly marked with a label such as “Proprietary.” NOTE:
“Confidential” is a classification marking used to control the dissemination of U.S. Government
National Security Information and should not be used to identify proprietary business information.
See BAA Section 6.2.1 for additional information on Proprietary Data.
5 Evaluation of White Papers/Proposals
White papers:
White papers will be reviewed by Government Technical expert(s) to determine a reasonable
number of Offerors apparently qualified to meet the intent of the BAA. This determination will be
based on the Offeror presenting technical qualifications specific to the field of science and
technology needed for the technical approach/solution presented, and the Government’s interest in
the Offeror’s intended technical approach/solution. Program balance across Topics and Areas of
Interest and program budget constraints may also be considerations in determining a reasonable
number of Offerors permitted to submit Proposals.
The Government will conduct rolling reviews of white papers. Submittal time may impact when an
Offeror receives the Government’s notice of whether their proposal is approved, however all efforts
will be made to provide a response within two weeks days of submission.
Based on the above determination, Offerors will either be approved to submit a proposal or not
approved to submit a proposal. Proposals will be reviewed as set forth in this BAA. Offerors not
approved to submit a proposal from step one or that do not submit a whitepaper will not have their
proposals reviewed by the government.
Offerors are cautioned that failure to follow submittal instructions may negatively impact their
proposal evaluation or may result in rejection of the proposal for non-compliance.
Proposals:
Proposals will be evaluated in line with FAR Part 35 and as described below.
The factors used to evaluate and select proposals for negotiation for this BAA are described in the
following paragraphs. Because there is no common SOW, each proposal shall be evaluated on its
18
own merits and its relevance to the BAA goals rather than against other proposals submitted in
response to this BAA.
The proposals shall be evaluated on the basis of technical evaluation and funding availability factors.
The technical evaluation and funding availability factors are of equal importance. Withinthe
technical evaluation factor, the specific technical criteria are in descending order of importance, as
follows: Overall Scientific and Technical Merit and Potential Contribution and Relevance to the
IARPA Mission. Within the funding availability factor, the sub criteria are of equal importance.
Specifics about the evaluation criteria are provided below.
Awards will be made on the basis of the technical evaluation and funding availability factors, and
subject to successful negotiations with the Government. Award shall not be made to Offeror(s)
whose proposal(s) are determined not to be selectable.
Offerors are cautioned that failure to follow submittal instructions may negatively impact their
proposal evaluation or may result in rejection of the proposal for non-compliance.
5.1 Technical Evaluation Factor (sub criteria are in descending order of importance)
Proposals will be evaluated using the following technical criteria, listed in descending order of
importance, to determine whether proposals submitted are consistent with the intent of this BAA
and of interest to the Government:
A. Overall Scientific and Technical Merit
Evaluators will assess the extent to which:
- The proposed technical approach is novel, innovative, feasible, achievable, and complete.
- The proposed technical team has the expertise and experience to accomplish the proposed
tasks.
- Task descriptions and associated technical elements provided are complete and in a logical
sequence with all proposed deliverables clearly defined such that a final outcome that
achieves the goal can be expected as a result of award.
- The proposal identifies major technical risks and planned mitigation efforts are clearly
defined and feasible.
B. Potential Contribution and Relevance to the IARPA Mission
Evaluators will also assess the potential contributions of the proposed effort to bolster the national
security technology base, and support IARPA’s mission to make pivotal early technology
investments that create or prevent technological surprise. Additionally, evaluators will assess the
extent to which the proposed intellectual property restrictions (if any) will impact the Government’s
ability to utilize and transition the technology to partners.
5.2 Funding Availability Factor (sub criteria are of equal importance)
A. Budget Constraints
The Government will seek to maximize the likelihood of meeting the BAA objectives within budget
constraints. This may involve awarding one or more contracts. Note: If the Offeror has submitted
the proposal to other federal, state or local agencies or other parties that may fund the proposed
effort, this may impact the Government’s decision to fund the effort.
19
B. Program Balance
The Government will take into account IARPA’s overall mission and the BAA objectives to ensure a
balanced approach to achieving program goals. This may include, but is not limited to, broadening
the variety of technical approaches and developing capabilities aligned with IC priorities.
5.3 Review and Selection Process
It is the policy of the Government to ensure impartial, equitable and comprehensive proposal
evaluations. The Government anticipates more than one award. Given the Government’s limited
resources anddesire to issue awards rapidly for this requirement, proposals may be evaluated and
awarded on a rolling basis. Topic and Area of Interest mayalso be factors in determining the order
in which proposals are evaluated in order to ensure program balance. Additionally, the Government
may discontinue evaluating proposals when available funding is exhausted. If new funds become
available, prior to proposal expiration, the Government may restart proposal evaluations and issue
additional awards.
Selection for negotiation will be conducted through a peer or scientific review process. A qualified
Government Reviewer(s) will assess each proposal’s strengths, weaknesses, and risks2
 against the
technical criteria. If necessary, non-Government technical experts with specialized expertise may
advise the Reviewer(s). However, only Government personnel will make recommendations and
selection determinations under this BAA. When the Government has completed its proposal review,
the Reviewer(s) will provide its findings and technical recommendations to the IARPA Scientific
Review Official (SRO).
The SRO will make the final decision as to selectability for negotiations based on the technical
recommendation and all stated factors (technical evaluation factor and funding availability factor).
At this point, Offerors will be notified in writing as to whether they have been determined selectable
or not selectable. For the purposes of this proposal evaluation process, these terms are defined as
follows:
Selectable: A selectable proposal is a proposal that has been evaluated by the Government against
the evaluation factors listed in the BAA, and determined to be technically competent, aligned to
IARPA’s overall mission and the BAA objectives, and funding is available. The technicalstrengthsof
the proposal outweigh any technical weaknesses and risks. Additionally, there are no technical
weaknesses that would require other than minor negotiation. The proposal can now move to the
negotiation and award process.
Non-Selectable: A proposal is considered non-selectable when the proposal has been evaluated by
the Government against the evaluation factors listed in the BAA and determined to be technically
weak, not aligned with IARPA’s overall mission and the BAA objectives, or funding is not
available.
Contract award is contingent on CO determination of a fair and reasonable cost/price and contract
agreement on terms and conditions.
5.4 Negotiation and Award

2 Strength- An aspect of an Offeror’s proposal that has appreciable merit or appreciably exceeds specified performance or capability requirements
in a way that will be advantageous to the Government during contract performance.
Weakness – A flaw in the proposal that increases the risk of unsuccessful contract performance.
Risk - The potential for unsuccessful contract performance. The consideration of risk assesses the degree to which an Offeror’s proposed
approach to achieving the technical factor or subfactor may involve risk of disruption of schedule, increased cost or degradation of performance,
the need for increased Government oversight, or the likelihood of unsuccessful contract performance. 
20
After selection and before award, the CO will contact Offerors whose proposals were determined
selectable to engage in negotiations. The CO will review the cost/price proposal using the proposal
analysis techniques described in FAR 15.404-1, as appropriate, to determine a fair and reasonable
cost/price. The CO’s evaluation will include review of proposed anticipated costs/prices of the
Offeror and proposed subcontractors, to ensure the Offeror has fully analyzed the budget
requirements, provided sufficient supporting information, has adequate systems for managing the
contract (i.e., accounting, purchasing as applicable), and that data is traceable and reconcilable. The
CO’s evaluation will also determine whether the prospective contractor understands the project and
its risks and has the ability to organize and perform the work and that, the Offeror meets the
responsibility standards of FAR 9.104. Additional information and supporting data may be
requested.
Procurement contracts, as determined by the contracting officer, shall be awarded to those Offerors
whose proposals are deemed most advantageous to the Government, all stated evaluation factors
considered, and pending the successful conclusion of negotiations.
5.5 Proposal Retention
Proposals shall not be returned upon completion of the source selection process. The original of
each proposal received shall be retained at IARPA and all other non-required copies shall be
destroyed. A certification of destruction may be requested, provided that the formal request is sentto
IARPA via e-mail to dni-iarpa-B24IC-BAASubmission-2022@iarpa.gov within 5 days after
notification of proposal results.
6 Award Administration Information
6.1 Communications and Award Notices
All questions or discussions regarding this solicitation must be directed to the Contracting Specialist
and/or Officer. All communication throughout this process must be handled formally and through
the proper channels, which means all parties must ensure a Government Contract Specialist or
Contracting Officer is present and/or engaged during any and all communication exchanges. Any
informal communications or outside communication will delay and may also jeopardize a potential
award.
As soon as practicable after the evaluation of a proposal is complete, the Offeror will be notified
that: (1) its proposal has been selected for negotiations, or (2) its proposal has not been selected for
negotiations.
6.1.2 Types of Awards
Procurement contracts will be made under this announcement. There are no limits on award
amounts.
6.1.3 Obligating of the Government
Prospective Offerors are advised that only Contracting Officers are legally authorized to commit the
Government. Only Contracting Officers may obligate the Government to an agreement involving
the expenditure of Government funds. Any resultant procurement contract award would include all
clauses required by the FAR and appropriate supplements.
6.1.4 Security Guidance
Security classification guidance via a DD Form 254, “DoD Contract Security Classification
Specification,” will not be provided at this time since the Government is soliciting ideas only. After 
21
reviewing the incoming proposals, if a determination is made that the award instrument may result
in access to classified information a DD Form 254 will be issued and attached as part of the award.
Depending on the work to be performed, the Offeror may require a SECRET facility clearance and
safeguarding capability; therefore, personnel identified for assignment to a classified effort must be
cleared for access to SECRET information at the time of award. In addition, the Offeror may be
required to have, or have access to, a certified and Government-approved facility to support work
under this BAA.
6.1.5 Proposal Handling
The Government has contracted for various business and staff support services, some of which
require contractors to obtain access to proprietary information submitted by Offerors. Any objection
to access must be in writing to the Contracting Officer and shall include a detailed statement of the
basis for the objection.
6.1.6 Offer Markings
All proposals containing proprietary data should have the cover page and each page containing
proprietary data clearly marked as containing proprietary data. If only portions of the page contain
proprietary information, those portions should be clearly marked. It is the Proposer’s responsibility
to clearly define to the Government what is considered proprietary data. No proposals containing
classified information should be submitted under this announcement.
6.2 Other Administrative Information
6.2.1 Intellectual Property
General. The Government may request additional information from the Offeror, as may be
necessary, to evaluate the Offeror’s IP rights assertions. If Offerors do not identify any restrictions
with respect to the proposed deliverables, the Government shall assume in its review of the proposal
that the Government will receive Unlimited Rights in accordance with FAR 52.227-11. Further,
failure to provide complete information may result in a determination that the proposal is not
compliant with the solicitation, and the Government reserves the right to reject a proposal if the
Offeror does not appropriately address all required IP rights issues.
IP Ownership. The Government’s rights will be in accordance with the resulting contract which will
include but may not be limited to FAR 52.227-11, 52.227-14, 52.227-16 and IA52.227-702.
Regardless of the scope of the Government’s rights, Offerors receiving contracts under this BAA
may freely use IP generated under the contract for their own commercial purposes unless restricted
by U.S. export control laws or security classification. Therefore, technical data and computer
software developed under any contract resulting from this solicitation will remain the property of
the Contractor,subject to IARPA’srights asset forth in the contract. For inventions first conceivedor
actually reduced to practice under this effort, Contractor shall grant the Government a nonexclusive,
nontransferable, irrevocable, paid-up license to practice, or have practiced for or on its behalf, such
invention throughout the world; Contractor may elect to retain title as described inthe award
instrument.
Indemnification. Offerors/Contractors expecting to use, but not to deliver, data or patentable
inventions, including commercial open-source tools in implementing their approach shall be
required to indemnify the Government against legal liability arising from such use.
Technical Data--Withholding of Payment. If technical data specified to be delivered under a contract
awarded under this solicitation are not delivered within the time specified by the contract or are
deficient upon delivery (including having restrictive markings not specifically authorized by the
22
contract), the CO is permitted, until such data are accepted by the Government, to withholdpayment
to the contractor of ten percent (10%) of the total contract price or amount unless a lesserwithholding
is specified in the contract. Payments may not be withheld, nor any other action takenpursuant to this
paragraph when the contractor's failure to make timely delivery or to deliver suchdata without
deficiencies arises out of causes beyond its control and without fault or negligence ofthe contractor.
The withholding of any amount or subsequent payment to the contractor shall notbe construed as a
waiver of any rights accruing to the Government under the contract.
6.2.2 Public Release
It is the policy of the Department of Defense that the publication of products of fundamental research
will remain unrestricted to the maximum extent possible. Research to be performed as a result of
this BAA may be Fundamental. The Government does not anticipate applying publication
restrictions of any kind but reserves the right to require prior review before publication in appropriate
or required circumstances.
Offerors should note that pre-publication approval of certain information may be required if it is
determined that its release may result in the disclosure of sensitive intelligence information.
A courtesy soft copy of any work submitted for publication shall be provided to the IARPA PM and
the Contracting Officer Representative (COR) a minimum of 5 business days prior to release in any
forum.
6.2.3 Export Control
Offerors are warned that compliance with International Traffic in Arms Regulations (ITAR) may be
required and will be included in all procurement contracts. The ITAR, issued by the Dept. of State,
controls the export of defense-related articles and services, including technical data, ensuring
compliance with the Arms Export Control Act (22 U.S.C. 2751 et seq.) If a Proposer has questions
regarding how to comply with the ITAR, they are directed to look at DFARS 252.225-7048(c).
Offerors are also warned that compliance with the Export Administration Regulations (EAR) may
be required and will be included in all procurement contracts. The EAR, issued by the Dept. of
Commerce, controls the export of dual-use times, (items that have both commercial and military or
proliferation applications) and purely commercial items. These items include commodities,
software, and technology. Refer to the Commerce Control List, which is part of the EAR, to identify
items subject to EAR, at http://www.gpoaccess.gov/cfr/index.html and
http://www.access.gpo.gov/bis/ear/ear_data.html.
The following clause, DFARS 252.225-7048 - Export-Controlled Items, will be included in awards
as deemed appropriate:
(a) Definition. “Export-controlled items,” as used in this clause, means items subject to the Export
Administration Regulations (EAR) (15 CFR Parts 730-774) or the International Traffic in Arms
Regulations (ITAR) (22 CFR Parts 120-130). The term includes:
(1) “Defense items,” defined in the Arms Export Control Act, 22 U.S.C. 2778(j)(4)(A), as defense
articles, defense services, and related technical data, and further defined in the ITAR, 22 CFR Part
120.
(2) “Items,” defined in the EAR as “commodities”, “software”, and “technology,” terms that are also
defined in the EAR, 15 CFR 772.1.
23
(b) The Contractor shall comply with all applicable laws and regulations regarding export-controlled
items, including, but not limited to, the requirement for contractors to register with the Department
of State in accordance with the ITAR. The Contractor shall consult with the Department of State
regarding any questions relating to compliance with the ITAR and shall consult with the Department
of Commerce regarding any questions relating to compliance with the EAR.
(c) The Contractor's responsibility to comply with all applicable laws and regulations regarding
export-controlled items exists independent of, and is not established or limited by, the information
provided by this clause.
(d) Nothing in the terms of this contract adds, changes, supersedes, or waives any of the requirements
of applicable Federal laws, Executive orders, and regulations, including but not limited to—
(1) The Export Administration Act of 1979, as amended (50 U.S.C. App. 2401, et seq.);
(2) The Arms Export Control Act (22 U.S.C. 2751, et seq.);
(3) The International Emergency Economic Powers Act (50 U.S.C. 1701, et seq.);
(4) The Export Administration Regulations (15 CFR Parts 730-774);
(5) The International Traffic in Arms Regulations (22 CFR Parts 120-130); and
(6) Executive Order 13222, as extended.
(e) The Contractor shall include the substance of this clause, including this paragraph (e), in all
subcontracts.
6.2.4 Subcontracting
It is the policy of the Government to enable small business and small disadvantaged business
concerns to be considered fairly as sub-contractors to contractors performing work or rendering
services as prime contractors or sub-contractors under Government contracts and to assure that
prime contractors and sub-contractors carry out this policy. Each Offeror that is selected for
negotiation for award and is expected to be awarded a contract which exceeds the simplified
acquisition threshold may be asked to submit a sub-contracting plan before award in accordance
with FAR 19.702(a) (1). The plan format is outlined in FAR 19.704.
Offerors shall declare teaming relationships in their Technical and Cost proposals and shall specify
the type of teaming arrangement in place, including any exclusive teaming arrangements. IARPA
neither promotes nor discourages the establishment of exclusive teaming agreements within
Proposer teams. Individuals or organizations associated with multiple teams shall take care not to
over-commit those resources being applied.
6.2.5 Reporting
Fiscal and management responsibility are important to the Government. Although the number and
types of reports shall be specified in the award document, all Offerors shall, at a minimum, provide
the CO, Contracting Officer’s Technical Representative (COTR) and PM with monthly technical
status reports, monthly financial status reports and final reports. The reports shall be prepared and
submitted in accordance with the procedures contained in the award document and mutually agreed
upon before award. Technical reports shall describe technical highlights and accomplishments,
priorities and plans, issues and concerns, evaluation results, and future plans. Financial reports
shall present an on-going financial profile of the project, including total project funding, funds
invoiced, funds received, funds expended during the preceding month, and planned expenditures
over the remaining period (financial report format may be modified for FFP contracts). Additional 
24
reports and briefing material may also be required, as appropriate, to document progress in
accomplishing program metrics.
Reports shall be delivered to the CO, COTR and the PM.
6.2.6 System for Award Management (SAM)
In accordance with FAR 52.204-7 and DFARS 252.204-7004, an Offeror must be actively registered
in the System for Award Management. Selected Offerors not already registered in SAM will be
required to register prior to any award under this BAA. FAR 52.204-7 System for Award
Management and FAR 52.204-13 System for Award Management Maintenance are incorporated
into this BAA, and FAR 52.204-13 will be incorporated in all awards. Information on SAM
registration is available at https://www.sam.gov/portal/public/SAM/.
6.2.7 Representations and Certifications
In accordance with FAR 4.1201, prospective Proposers shall complete electronic annual
representations and certifications at https://www.sam.gov/portal/public/SAM/.
6.2.8 Lawful Use and Privacy Protection Measures
All data gathered by the Offeror shall be obtained in accordance with U.S. laws and in compliance
with the End User License Agreement, Copyright Laws, Terms of Service, and laws and policies
regarding privacy protection of U.S. Persons. Before using such data, the Offeror shall provide proof
that the data was acquired in accordance with U.S. laws and regulations.
6.2.9 Invoicing, Receipt, Acceptance, and Property Transfer (iRAPT) (formerly Wide Area
Work Flow (WAWF))
Unless using another approved electronic invoicing system, Performers will be required to submit
invoices for payment directly via the Internet/WAWF at https://wawf.eb.mil. Registration to
iRAPT/WAWF will be required prior to any award under this BAA.
6.2.10 NAVWAR e-Commerce Central
Proposal submissions for contracts will only be accepted via NAVWAR e-Commerce Central at
https://e-commerce.sscno.nmci.navy.mil. (Note that this does not include a "www" prefix) by
selecting NIWC Pacific then Open BAAs from the left-hand menu and selecting the Solicitation
number.
6.2.11 Certificate of Current Cost and Pricing Data
Upon completion of negotiations and agreement on contract cost, a Certificate of Current Cost or
Pricing Data may be required in accordance with FAR 15.406-2. In addition, any Offeror who is
required to submit and certify cost or pricing data shall certify on behalf of subcontractors.
6.2.12 Employment Eligibility Verification (E-verify)
As per FAR 22.1802, recipients of FAR-based procurement contracts must enroll as Federal
Contractors in E-verify and use E-verify to verify employment eligibility of all employees assigned
to the award. All resultant contracts from this solicitation will include FAR 52.222-54,
“Employment Eligibility Verification.”
6.2.13 Public Access to Results
The Government is committed to making the results of this research available and maximally
useful to thepublic, industry, government, and the scientific community, in accordance with the
policy set forth in the White House Office of Science and Technology Policy’s memorandum 
25
“Increasing Accessto the Results of Federally Funded Scientific Research,” dated February 22,
2013, consistent withall other applicable law and policy; agency mission; resource constraints;
and U.S. national, homeland, and economic security.
(https://obamawhitehouse.archives.gov/sites/default/files/microsites/ostp/ostp_public_access_me
mo_2013.pdf)
Upon acceptance for publication of any manuscript or paper reporting results of work under a
contract awarded pursuant to this BAA, the author’s final peer-reviewed manuscript(s) or
conference paper(s) must be submitted to the IARPA-designated repository for public access, in
accordance with the instructions on IARPA’s website at http://www.iarpa.gov. The Government
will make the Publication available to the public through the repository at no charge, following a
one-year embargo to preserve the rights of the publisher. The author must inform the publisher of
rights that will be retained by the author and IARPA by including in the publishing/transfer of
copyright agreement a provision substantially as follows:
“Journal acknowledges that Author retains the right to provide a copy of the final peer-reviewed
manuscript (“Work”) to the Federal agency funding the research on which the Work is based upon
acceptance for Journal publication, for public archiving as soon as possible but no later than 12
months after publication by Journal. Journal further acknowledges that the Federal Government,
having funded the research upon which the Work is based, has certain irrevocable and nonexclusive contractual rights in the Work, which are not affected or altered in any way by this
Agreement.”
Additionally, awardee must deposit the data underlying the results and findings in the publicationin
a suitable public repository, in accordance with the project’s Data Management Plan. If the metadata
describing the underlying or supporting research data is not included in the Publication,the awardee
must provide the metadata to the IARPA-designated public access repository, in accordance with
the instructions on IARPA’s website at http://www.iarpa.gov.
The Government will accept a final published article in lieu of a final peer-reviewed manuscript,
provided the author has the right to provide the article and authorize IARPA to release the article
publicly.
Data produced under the program, reports to the Government, and program-related publications
should beconsistent with the Transparency and Openness Promotion Guidelines of the Center for
Open Science, including preregistration of studies and analysis plans. (https://cos.io/ourservices/top- guidelines/). To the extent possible, all reports to IARPA and all program-related
publications should be consistent with statistical best practices described in (Psychological Science
(2014) http://pss.sagepub.com/content/25/1/3). For example, wherever appropriate, effect sizes and
confidence intervals (or the Bayesian equivalents) should be reported, and the data and methodology
must be presented so that it is easily used for meta-analysis and independent re- analysis of the data.
All Offerors must describe plans to ensure that the above requirements are satisfied.
6.2.14 Electronic and Information Technology
All electronic and information technology acquired through the BAA must satisfy the accessibility
requirements of Section 508 of the Rehabilitation Act (29 U.S.C. § 794d) and FAR Subpart 39.2.
Each Proposer who submits a proposal involving the creation or inclusion of electronic and
information technology must ensure that Federal employees with disabilities will have access to and
use of information that is comparable to the access and use by Federal employees who are not
individuals with disabilities. Additionally, each Proposer must ensure that members of the public
with disabilities seeking information or services from NIWC Pacific will have access to and use of
information and data that is comparable to the access and use of information and data by members 
26
of the public who are not individuals with disabilities.
6.3 FAR / DFARS Provisions & Clauses
6.3.1 Provisions
For purposes of illustration and not limitation, the following provisions may be applicable to NIWC Pacific contracts:
FAR Clause No. Title
52.204-8 Annual Representations and Certifications
52.204-16 Commercial and Government Entity Code Reporting
52.204-22 Alternative Line Item Proposal
52.204-24 Representation Regarding Certain Telecommunications and Video Surveillance Services or Equipment
52.209-7 Information Regarding Responsibility Matters
52.209-13 Violation of Arms Control Treaties or Agreements—Certification
52.215-16 Facilities Capital Cost of Money
52.215-22 Limitations on Pass-Through Charges—Identification of Subcontract Effort
52.216-1 Type of Contract
52.216-27 Single or Multiple Awards
52.217-4 Evaluation of Options Exercised at Time of Contract Award
52.217-5 Evaluation of Options
52.229-11 Tax on Certain Foreign Procurements—Notice and Representation.
52.230-1 Cost Accounting Standards Notices and Certification
52.230-7 Proposal Disclosure—Cost Accounting Practice Changes
52.233-2 Service of Protest
52.252-1 Solicitation Provisions Incorporated by Reference
52.252-5 Authorized Deviations in Provisions
DFARS Clause No. Title
252.203-7005 Representation Relating to Compensation of Former DoD Officials
252.204-7007 Alternate A, Annual Representations and Certifications
252.204-7008 Compliance with Safeguarding Covered Defense Information Controls
252.204-7016 Covered Defense Telecommunications Equipment or Services--Representation
252.204-7017 Prohibition on the Acquisition of Covered Defense Telecommunications Equipment or Services--
Representation
252.204-7019 Notice of NIST SP 800-171 DoD Assessment Requirements.
252.215-7003 Requirement for Submission of Data Other Than Certified Cost or Pricing Data—Canadian Commercial
Corporation
252.215-7007 Notice of Intent to Resolicit
252.215-7009 Proposal Adequacy Checklist
252.215-7010 Requirements for Certified Cost or Pricing Data and Data Other Than Certified Cost or Pricing Data--Basic
252.215-7011 Requirements for Submission of Proposals to the Administrative Contracting Officer and Contract Auditor
252.215-7012 Requirements for Submission of Proposals via Electronic Media
252.215-7013 Supplies and Services Provided by Nontraditional Defense Contractors
252.225-7003 Report of Intended Performance Outside the United States and Canada—Submission with Offer
252.225-7032 Waiver of United Kingdom Levies—Evaluation of Offers
252.225-7973 Prohibition on the Procurement of Foreign-Made Unmanned Aircraft Systems—Representation.
(DEVIATION 2020-O0015)
252.225-7974 Representation Regarding Persons that have Business Operations with the Maduro
Regime (DEVIATION 2020-O0005)
252.227-7017 Identification and Assertion of Use, Release, or Disclosure Restrictions
252.227-7028 Technical Data or Computer Software Previously Delivered to the Government
252.239-7098 Prohibition on Contracting to Maintain or Establish a Computer Network Unless Such Network is Designed
to Block Access to Certain Websites--Prepresention
252.247-7022 Representation of Extent of Transportation by Sea
27
6.3.2 Clauses
FAR and DFARS clauses apply to any contract awarded under this BAA. Specific clauses depend
on a variety of factors (e.g., contract type, contract value, business size, etc.) and will be negotiated
at award.
6.3.2.1 Combating Trafficking in Persons
Appropriate language from FAR Clause 52.222-50 will be incorporated in all awards.
6.3.2.2 Ensuring Adequate COVID-19 Safety Protocols for Federal Contractors
DFARS Clause 252.223-7999 Ensuring Adequate COVID-19 Safety Protocols for Federal
Contractors (DEVIATION 2021-O0009) will be incorporated in all awards.
6.3.2.3 Certification Regarding Trafficking in Persons Compliance Plan
Prior to award of a contract, for any portion of the contract that is for supplies, other than
commercially available off-the-shelf items, to be acquired outside the United States, or services to
be performed outside the United States, and which has an estimated value that exceeds $500,000,
the contractor shall submit the certificate as specified in paragraph (c) of 52.222-56, Certification
Regarding Trafficking in Persons Compliance Plan.
6.3.2.4 Updates of Information regarding Responsibility Matters
FAR clause 52.209-9, “Updates of Publicly Available Information Regarding Responsibility
Matters”, will be included in all contracts that exceed $600,000 where the contractor has current
active Federal contracts and grants with total value greater than $10,000,000.
28
7 APPENDIX A - BAA Attachments
o 1 - VOLUME I: TECHNCIAL AND MANAGEMENT PROPOSAL COVERSHEET
o 2 - ACADEMIC INSTITUTION ACKNOWLEDGMENT LETTER SAMPLE
o 3 - INTELLECTUAL PROPERTY AND DATA RIGHTS ASSERTIONS FORM
o 4 - OCI CERTIFICATION LETTER SAMPLE
o 5 - QUAD CHART SUMMARY
o 6 - VOLUME 2: COST PROPOSAL COVER SHEET
o 7 - VOLUME 2: COST ELEMENT BREAKDOWN SPREADSHEET
29
A.1 Cover Sheet for Volume 1: Technical and Management Proposal
(1) BAA Number N66001-22-S-4704
(2) Topic and Area of Interest –(Reference BAA Section 1.1)
(3) Lead Organization Submitting Proposal
(4) Type of Business, Selected Among the Following Categories: “Large
Business”, “Small Disadvantaged Business”, “Other Small Business”,
“HBCU”, “MI”, “Other Educational”, or “Other Nonprofit”
(5) Offeror’s Reference Number (if any)
(6) Other Team Members (if applicable) and Type of Business for Each
(7) Proposal Title
(8) Technical Point of Contact to Include: Title, First Name, Last Name,
Street Address, City, State, Zip Code, Telephone, Fax (if available),
Electronic Mail (if available)
(9) Administrative Point of Contact to Include: Title, First Name, Last
Name, Street Address, City, State, Zip Code, Telephone, Fax (if available),
Electronic Mail (if available)
(10) Volume 1 no more than the specified page limit Yes/No
(11) Restrictions on Intellectual property rights details provided inAppendix
A format?
Yes/No
(12) Research Data Management Plan included? Not Applicable Yes/No
(13) OCI Notification Yes/No
(13a) If No, is written OCI certification included (see Appendix A)? Yes/No
(14) Are one or more U.S. Academic Institutions part of your team? Yes/No
(14a) If Yes, are you including an Academic Institution Acknowledgment
Statement with your proposal for each U.S. Academic Institution that is part
of your team (see Appendix A)?
Yes/No
(15) Total Funds Requested from IARPA and the Amount of Cost Share (if
any)
$
(16) Date of Proposal Submission
30
Appendix A.2 Academic Institution Acknowledgment Letter
-- Please Place on Official Letterhead --
<Insert date>
To: Contracting Officer
 NIWC Pacific
Office of the Director of National Intelligence Washington,
D.C. 20511
Subject: Academic Institution Acknowledgment Letter Reference: Executive Order 12333, As Amended,
Para 2.7
This letter is to acknowledge that the undersigned is the responsible official of <insert name of the
academic institution>, authorized to approve the contractual relationship in support of the Office of the
Director of National Intelligence’s Intelligence Advanced Research Projects Activity and this academic
institution.
The undersigned further acknowledges that he/she is aware of the Intelligence Advanced Research
Projects Activity’s proposed contractual relationship with <insert name of institution> through N66001-22-
S-4704 and is hereby approved by the undersigned official, serving as the president, vice-president,
chancellor, vice-chancellor, or provost of the institution.
<Name> Date
<Position>
31
Appendix A.3 Intellectual Property and Data Rights Assertion
[Please provide here your good faith representation of ownership or possession of appropriate
licensing rights to all IP that shall be utilized under the Program.]
Patents
PATENTS
Patent number(or
application
number)
Patent name Inventor name(s) Patent owner(s)or
assignee
Incorporation into
deliverable
(LIST) (LIST) (LIST) (LIST) (Yes/No; applicable
deliverable)
(1) Intended use of the patented invention(s) listed above in the conduct of the proposedresearch.
(2) Description of license rights to make, use, offer to sell, or sell, if applicable, that arebeing
offered to the Government in patented inventions listed above.
(3) How the offered rights will permit the Government to reach its program goals (including
transition) with the rights offered.
(4) Cost to the Government to acquire additional or alternative rights, if applicable.
(5) Alternatives, if any, that would permit IARPA to achieve program goals.
Data (Including Technical Data and Computer Software)
NONCOMMERCIAL ITEMS
Technical Data,
Computer Software To
be Furnished With
Restrictions
Basis for Assertion Asserted Rights
Category
Name of Person Asserting
Restrictions
(LIST) (LIST) (LIST) (LIST)
32
COMMERCIAL ITEMS
Technical Data,
Computer Software To be
Furnished With
Restrictions
Basis for Assertion Asserted Rights
Category
Name of Person
Asserting Restrictions
(LIST) (LIST) (LIST) (LIST)
(1) Intended use of the data, including, technical data and computer software, listed above inthe
conduct of the proposed research.
(2) Description of Asserted Rights Categories, specifying restrictions on Government’s ability
to use, modify, reproduce, release, perform, display, or disclose technical data, computer
software, and deliverables incorporating technical data and computer softwarelisted above.
(3) How the offered rights will permit the Government to reach its program goals (including
transition) with the rights offered.
(4) Cost to the Government to acquire additional or alternative rights, if applicable.
(5) Alternatives, if any, that would permit IARPA to achieve program goals.
33
Appendix A.4 Organizational Conflicts of Interest Certification Letter
(Month DD, YYYY)
Office of the Director of National Intelligence
Intelligence Advanced Research Projects Activity (IARPA) Biointelligence and Biosecurity for the
Intelligence Community BAA
ATTN: NIWC Pacific, Contracting Officer
Subject: OCI Certification
Reference: <Insert Program Name>, N66001-22-S-4704, (Insert assigned proposal ID#, if received)Dear ,
In accordance with Broad Agency Announcement N66001-22-S-4704, Organizational Conflicts of Interest
(OCI), and on behalf of (Offeror name) I certify that neither (Offeror name) nor any of our subcontractor
teammates has as a potential conflict of interest, real or perceived, as it pertains to the Biointelligence and
Biosecurity for the Intelligence Community BAA. Please note the following subcontractors and their
proposed roles:
[Please list all proposed contractors by name with a brief description of their proposed involvement.]
If you have any questions, or need any additional information, please contact (Insert name of contact) at
(Insert phone number) or (Insert e-mail address).
Sincerely,
(Insert organization name) (Shall be signed by an official that has the authority to bind the organization)
(Insert signature)
(Insert name of signatory) (Insert title of signatory)
31
Appendix A.5 Quad Chart Summary of the Proposal
32
Appendix A.6 Cover Sheet for Volume 2 Cost/Price Proposal
(1) BAA Number N66001-22-S-4704
(2) Topic and Area of Interest:
(See BAA Section 1.1)
(3) Lead organization submitting proposal
(4) Type of Business, Selected Among the Following Categories: “Large
Business”, “Small Disadvantaged Business”, “Other Small Business”,
“HBCU”, “MI”, “Other Educational”, or “Other Nonprofit”
(5) Offeror’s Reference Number (if any)
(6) Other Team Members (if applicable) and Type of Business for Each
(7) Proposal Title
(8) Technical Point of Contact to Include: Title, First Name, Last Name,
Street Address, City, State, Zip Code, Telephone, Fax (if available),
Electronic Mail (if available)
(9) Administrative Point of Contact to Include: Title, First Name, Last
Name, Street Address, City, State, Zip Code, Telephone, Fax (ifavailable),
Electronic Mail (if available)
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
(19) Proposal Validity Period
(20) Cost Summaries Provided
(21) Size of Business in accordance with NAICS Code 541712
33
Appendix A.7 Contractor/Subcontractor Cost Element Sheet for Volume 2 Cost Proposal
Prime Contractor/Subcontractor Cost Element Sheet for Volume 2 Cost Proposal
Complete a Summary Cost Element Sheet and separate sheets for the Base Period and each Option Period
COST ELEMENT BASE RATE AMT
DIRECT LABOR (List each labor category
separately. Identify Key Personnel by
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
SUBCONTRACTORIOT
& CONSULTANT
NAME
SOW TASKS
PERFORMED*
TYPE OF
AWARD
SUB- CONTRACTOR, IOT &
CONSULTANT
QUOTED PRICE
COST PROPOSED BY
PRIME FOR
SUBCONTRACTOR,IOT
& CONSULTANT
DIFFERENCE
(Column D -
Column E) IF
APPLICABLE
TOTALS
*Identify Statement of Work, Milestone or Work Breakdown Structure paragraph, or provide a narrative
explanation as an addendum to this Table that describes the effort to be performed.
34
Software and IP Costs
Item Cost Date of Expiration
(List)
NOTE: Educational institutions and non-profit organizations as defined in FAR 31.3 and 31.7, respectively, at the
prime and subcontractor level may deviate from the cost template in Appendix B when estimating the direct labor
portion of the proposal to allow for OMB guided accounting methods(2 CFR 220) that are used by their institutions.
The methodology shall be clear and provide sufficientdetail to substantiate proposed labor costs. For example, each
labor category shall be listed separately;identify Key Personnel and provide hours/rates or salaries and percentage of
time allocated to the project.

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
        