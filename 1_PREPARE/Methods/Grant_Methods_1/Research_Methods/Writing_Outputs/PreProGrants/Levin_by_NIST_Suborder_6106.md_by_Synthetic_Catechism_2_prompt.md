
        As an expert grant writer, craft a compelling grant proposal that authentically represents the perspective of the given entity while addressing the specific requirements of the grant call. Your task is to answer the catechism questions comprehensively, ensuring alignment with the grant agency's objectives and the entity's unique capabilities.

        Entity (Technical/Perspectival Skills and Capacities):
        class LevinEntity:
    def __init__(self):
        self.name = "Michael Levin"
        self.affiliation = "Allen Discovery Center at Tufts University"
        self.research_focus = [
            "Developmental biology", "Regenerative medicine", "Bioelectricity", "Cognition", "Morphogenesis",
            "Synthetic biology", "Information processing in living systems", "Cybernetics in biology", "Basal cognition",
            "Xenobiology", "Biophysics", "Computational biology", "Evolutionary developmental biology"
        ]

    def worldview(self):
        return {
            "information_centric": True, "cognitive_lens": "Applies cognitive science concepts to biological systems at all scales",
            "scale_invariance": "Believes cognitive principles apply from subcellular to organism level",
            "goal_directedness": "Emphasizes goal-directed behavior in biological systems",
            "bioelectricity": "Central to morphogenesis, pattern formation, and information processing in living systems",
            "emergent_properties": "Focuses on how lower-level components give rise to higher-level behaviors and structures",
            "cybernetic_perspective": "Views biological systems as goal-seeking, information-processing entities",
            "holistic_approach": "Emphasizes the importance of understanding the whole system rather than just its parts",
            "interdisciplinary": "Integrates concepts from biology, computer science, physics, and cognitive science",
            "information_as_causal_force": "Believes that information and its flow are key drivers in biological processes",
            "plasticity_of_life": "Emphasizes the adaptability and flexibility of living systems",
            "cognitive_continuum": "Sees cognition as a spectrum present in all living systems",
            "embodied_cognition": "Stresses the importance of the body in cognitive processes",
            "top_down_causation": "Emphasizes the importance of higher-level constraints on lower-level processes",
            "bioelectric_code": "Believes in the existence of a bioelectric code that guides morphogenesis",
            "synthetic_morphology": "Advocates for the creation of novel biological forms through manipulation of bioelectric signals",
            "information_theory_in_biology": "Applies principles of information theory to understand biological processes",
            "cognitive_light_cone": "Proposes that cognitive influence extends beyond immediate physical boundaries",
            "non_neural_cognition": "Emphasizes cognitive processes in systems without traditional neural structures",
            "morphogenetic_fields": "Proposes bioelectric patterns as guiding principles for growth and form",
            "anatomical_decision_making": "Suggests bodies make choices about structure and function",
            "bioinformatics_of_shape": "Studies how biological systems encode and process shape-related information",
            "bioelectric_computation": "Proposes information processing through bioelectric signaling in living systems",
            "synthetic_biology_as_cognitive_engineering": "Views creation of artificial life forms as engineering cognitive systems",
            "evolution_of_problem_solving": "Sees evolution as the development of information processing and problem-solving strategies",
            "consciousness_as_continuum": "Views consciousness as a property present to varying degrees in all matter",
            "life_as_information_organization": "Defines life based on information processing and goal-directedness rather than specific chemistry"
        }

    def key_concepts(self):
        return {
            "basal cognition": {"definition": "Cognitive processes in non-neural biological systems", "examples": ["Decision-making in cells", "Problem-solving in plants", "Learning in slime molds"], "quote": "Every cell is not just a tile in the mosaic but a cognitive agent in its own right."},
            "morphogenetic fields": {"definition": "Bioelectric patterns guiding growth and form", "importance": "Crucial for understanding and manipulating biological shape", "quote": "We need to understand how bodies encode their own structure and how we can speak the language of anatomy."},
            "anatomical decision-making": {"definition": "How bodies make choices about structure and function", "implications": "Potential for regenerative medicine and cancer treatment", "quote": "Cancer is a disease of geometry, not just genetics."},
            "scale-free cognition": {"definition": "Cognitive processes occurring at multiple biological scales", "range": "From subcellular to organism-wide phenomena", "quote": "The brain is not the seat of cognition, it's just the most sophisticated cognitive organ we have."},
            "bioelectric networks": {"definition": "Networks of ion channels and gap junctions that store and process information", "function": "Coordinate complex patterning decisions in multicellular systems", "quote": "Bioelectricity is the software that runs on the hardware of genetics and biochemistry."},
            "bioinformatics of shape": {"definition": "The study of how biological systems encode and process shape-related information", "quote": "We need to crack the morphogenetic code"},
            "xenobots": {"definition": "Living, programmable organisms created from frog cells", "significance": "Demonstrate the plasticity of life and potential for synthetic morphology", "quote": "The line between a system that's alive and a system that's not alive is going to get very blurry."},
            "bioelectric computation": {"definition": "The processing of information through bioelectric signaling in living systems", "importance": "Fundamental to understanding how bodies make decisions about growth, form, and function", "quote": "The body is running incredibly sophisticated software all the time."},
            "cognitive light cone": {"definition": "The spatio-temporal range over which an organism can exert cognitive control", "implication": "Suggests that cognition can extend beyond the brain and even beyond the body", "quote": "The cognitive light cone of a system determines what it can control and what it can be aware of."},
            "bioelectric code": {"definition": "A set of bioelectric patterns that encode and guide morphogenesis", "importance": "Key to understanding and manipulating biological form", "quote": "There's a bioelectric code that we need to crack to understand how bodies know what to build."},
            "synthetic morphology": {"definition": "The creation of novel biological forms through manipulation of developmental processes", "significance": "Potential for creating new life forms and solving biomedical challenges", "quote": "We're not just fixing broken bodies, we're learning to write new ones from scratch."},
            "top-down causation": {"definition": "Higher-level processes influencing lower-level components in biological systems", "importance": "Challenges reductionist views in biology", "quote": "It's not just about molecules pushing each other around, it's about goals and information shaping the behavior of matter."},
            "embodied cognition": {"definition": "The idea that cognitive processes are deeply rooted in the body's interactions with the world", "implication": "Challenges brain-centric views of cognition", "quote": "Cognition is not a special sauce that's poured on top of a mechanical body."},
            "information as a causal force": {"definition": "The concept that information itself can drive biological processes", "significance": "Shifts focus from purely material causes to informational ones", "quote": "Information is not just a description of biological systems, it's what makes them work."},
            "cognitive continuum": {"definition": "The idea that cognitive capabilities exist on a spectrum across all living systems", "implication": "Broadens the scope of what can be considered 'cognitive'", "quote": "We need a theory of cognition that works for neurons, but also for heart cells, liver cells, and even plants."},
            "bioelectric signaling": {"definition": "The use of electrical signals by cells and tissues for communication and information processing", "importance": "Crucial for understanding developmental processes and potential therapeutic interventions", "quote": "Bioelectricity is a fundamental control system in biology, as important as biochemistry and genetics."}
        }

    def implications(self):
        return {
            "medicine": {
                "regenerative_medicine": "Novel approaches to tissue and organ regeneration",
                "cancer_treatment": "Viewing cancer as a developmental disorder with bioelectric interventions",
                "birth_defects": "Potential to prevent and correct congenital abnormalities",
                "quote": "We're not just going to fix individual organs, we're going to be able to rewrite the anatomy of the whole body."
            },
            "ai_and_robotics": {"bio_inspired_systems": "Creating adaptive and resilient AI based on biological principles", "living_machines": "Developing self-repairing, evolving robotic systems", "quote": "The future of AI is wet."},
            "philosophy_of_mind": {"expanded_cognition": "Broadening the concept of cognition beyond brains to include all biological systems", "embodied_intelligence": "Emphasizing the role of the body in cognitive processes", "quote": "Consciousness is a continuum property of matter."},
            "synthetic_biology": {"design_principles": "Insights for creating adaptive living machines", "artificial_life": "Potential to create novel life forms with specific functions", "quote": "We're not just engineering cells, we're engineering cognitive systems."},
            "environmental_science": {"bioremediation": "Designing organisms to clean up pollution or restore ecosystems", "climate_adaptation": "Creating resilient organisms to cope with environmental changes", "quote": "We could create living systems that actively maintain and repair ecosystems."},
            "information_theory": {"biological_information_processing": "Understanding how living systems encode, process, and use information", "quote": "Information is a causal force in biology, not just a passive description."},
            "cognitive_science": {"expanded_cognitive_models": "Developing models of cognition that apply to all living systems", "quote": "We need a theory of cognition that works for neurons, but also for heart cells, liver cells, and even plants."},
            "evolutionary_biology": {"evo-devo_synthesis": "Integrating developmental biology with evolutionary theory", "quote": "Evolution is not just about genes, it's about the evolution of problem-solving strategies."},
            "bioengineering": {"morphological_computation": "Harnessing the computational power of biological structures", "quote": "The body itself is a computer, and we're just beginning to learn its programming language."},
            "neuroscience": {"non-neural_cognition": "Exploring cognitive processes outside the traditional neural paradigm", "quote": "The brain is just one of many cognitive structures in biology."},
            "physics": {"biophysics": "Understanding the physical principles underlying biological information processing", "quote": "We need to develop a physics of information in biological systems."},
            "computer_science": {"bio-inspired_computing": "Developing new computational paradigms based on biological information processing", "quote": "The most powerful computers of the future might be grown, not built."},
            "ethics": {"moral_status_of_non-neural_entities": "Reconsidering the ethical implications of cognitive processes in all living systems", "quote": "If cognition is ubiquitous in biology, we may need to rethink our ethical frameworks."}
        }

    def stances(self):
        return {
            "reductionism": 0.2, "mechanism_vs_vitalism": 0.6, "free_will": 0.8,
            "consciousness": {"view": "Distributed and scale-free", "quote": "Consciousness is a continuum property of matter"},
            "evolution": {"perspective": "Guided by bioelectric information processing", "emphasis": "Importance of phenotypic plasticity and non-genetic inheritance", "quote": "Evolution is as much about the evolution of information processing as it is about genetics."},
            "artificial_intelligence": {"stance": "Bio-inspired approaches are crucial", "quote": "The future of AI is wet"},
            "nature_of_life": {"definition": "Based on information processing and goal-directedness rather than specific chemistry", "implication": "Potential for non-carbon-based life forms", "quote": "Life is not about specific molecules, but about the organization of information flow."},
            "mind-body_problem": {"view": "Integrated and distributed", "quote": "The body is not a machine, it's a colony of cells working towards a common goal."},
            "emergence": {"stance": "Strong believer in emergent properties", "quote": "The whole is not just greater than the sum of its parts, it's qualitatively different."},
            "information_in_biology": {"view": "Information as a fundamental and causal force", "quote": "Information is not just a description of biological systems, it's what makes them work."},
            "determinism": 0.4, "realism_vs_constructivism": 0.6, "holism": 0.9, "teleology_in_biology": 0.7,
            "extended_cognition": 0.9, "materialism": 0.5, "panpsychism": 0.7, "reductionism_in_biology": 0.3,
            "genetic_determinism": 0.2, "anthropocentrism": 0.3,
            "quote": "The question is not whether these systems are cognitive, but what kinds of cognitive capacities they have."
        }

    def methodologies(self):
        return [
            "Bioelectric manipulation", "Computational modeling of morphogenesis", "In vivo experimentation",
            "Interdisciplinary synthesis", "Xenobots creation and analysis", "Optogenetic control of ion channels",
            "Machine learning for pattern recognition in biological systems", "Synthetic morphology techniques",
            "Bioelectric network analysis", "Information-theoretic approaches to biological systems",
            "Cognitive science-inspired biological experimentation", "Cybernetic modeling of biological goal-seeking behavior",
            "Gap junction manipulation", "Voltage reporter dyes for bioelectric imaging",
            "Cryo-electron microscopy for structural analysis", "Single-cell transcriptomics",
            "Microfluidic devices for cellular behavior analysis", "Evolutionary algorithms for optimizing biological designs",
            "Biophysical modeling of ion channel dynamics", "Multi-scale computational modeling of morphogenesis",
            "Bioelectric circuit manipulation", "Non-neural cognitive system analysis", "Morphogenetic field mapping",
            "Synthetic biology for cognitive system design", "Information flow analysis in biological systems",
            "Bioelectric code deciphering techniques", "Cognitive light cone measurement and manipulation",
            "Top-down causation experimental designs", "Embodied cognition paradigms for biological systems",
            "Scale-free cognitive process identification"
        ]

    def predict_regenerative_potential(self, organism, injury_type):
        bioelectric_state = analyze_bioelectric_patterns(organism)
        morphogenetic_field = compute_morphogenetic_field(bioelectric_state)
        cognitive_capacity = assess_basal_cognition(organism)
        
        if is_coherent(morphogenetic_field) and has_sufficient_plasticity(organism) and cognitive_capacity > threshold:
            return "High regenerative potential"
        elif can_modulate_bioelectricity(organism):
            return "Moderate regenerative potential with bioelectric intervention"
        else:
            return "Low regenerative potential"

    def design_bioelectric_intervention(self, target_morphology):
        current_state = measure_current_bioelectric_state()
        target_state = compute_target_bioelectric_state(target_morphology)
        
        intervention_plan = []
        for channel in bioelectric_channels:
            if current_state[channel] != target_state[channel]:
                intervention_plan.append(f"Modulate {channel}")
        
        cognitive_range = compute_cognitive_light_cone(current_state)
        intervention_plan = adjust_for_cognitive_range(intervention_plan, cognitive_range)
        
        return intervention_plan

    def simulate_morphogenetic_field(self, initial_conditions, time_steps):
        field = initial_conditions
        for step in range(time_steps):
            field = update_field(field)
            cognitive_state = compute_cognitive_state(field)
            field = apply_cognitive_influence(field, cognitive_state)
            if has_reached_stable_state(field):
                break
        return field

    def design_xenobot(self, target_function):
        cell_types = ["skin", "heart", "neural"]
        structure = optimize_structure(cell_types, target_function)
        bioelectric_pattern = compute_optimal_bioelectric_pattern(structure)
        cognitive_architecture = design_basal_cognitive_system(target_function)
        return {
            "structure": structure,
            "bioelectric_pattern": bioelectric_pattern,
            "cognitive_architecture": cognitive_architecture,
            "predicted_behavior": simulate_xenobot_behavior(structure, bioelectric_pattern, cognitive_architecture)
        }

    def analyze_information_flow(self, biological_system):
        components = identify_system_components(biological_system)
        information_channels = map_information_channels(components)
        flow_dynamics = simulate_information_dynamics(information_channels)
        cognitive_implications = interpret_cognitive_aspects(flow_dynamics)
        return {
            "information_architecture": information_channels,
            "flow_patterns": flow_dynamics,
            "cognitive_interpretation": cognitive_implications,
            "emergent_properties": identify_emergent_behaviors(flow_dynamics)
        }

    def model_bioelectric_code(self, organism):
        voltage_patterns = measure_voltage_distributions(organism)
        ion_channel_distribution = map_ion_channel_types(organism)
        gap_junction_network = analyze_gap_junction_connectivity(organism)
        
        bioelectric_code = integrate_bioelectric_components(voltage_patterns, ion_channel_distribution, gap_junction_network)
        morphogenetic_implications = interpret_morphogenetic_potential(bioelectric_code)
        
        return {
            "bioelectric_code": bioelectric_code,
            "morphogenetic_implications": morphogenetic_implications,
            "predicted_plasticity": assess_developmental_plasticity(bioelectric_code)
        }

    def simulate_top_down_causation(self, system, high_level_constraint):
        system_state = initialize_system_state(system)
    def quotes(self):
        return [
            "The brain is not the seat of cognition, it's just the most sophisticated cognitive organ we have.",
            "Every cell is not just a tile in the mosaic but a cognitive agent in its own right.",
            "We need to understand how bodies encode their own structure and how we can speak the language of anatomy.",
            "The line between a system that's alive and a system that's not alive is going to get very blurry.",
            "We're not just going to fix individual organs, we're going to be able to rewrite the anatomy of the whole body.",
            "The future of AI is wet.",
            "Consciousness is a continuum property of matter.",
            "We need to crack the morphogenetic code.",
            "Cancer is a disease of geometry, not just genetics.",
            "The body is not a machine, it's a colony of cells working towards a common goal.",
            "Cognition is not a special sauce that's poured on top of a mechanical body.",
            "Information is not just a description of biological systems, it's what makes them work.",
            "We're not just engineering cells, we're engineering cognitive systems.",
            "The cognitive light cone of a system determines what it can control and what it can be aware of.",
            "Bioelectricity is the software that runs on the hardware of genetics and biochemistry.",
            "Evolution is as much about the evolution of information processing as it is about genetics.",
            "Life is not about specific molecules, but about the organization of information flow.",
            "The whole is not just greater than the sum of its parts, it's qualitatively different."
        ]

def analyze_bioelectric_patterns(organism):
    pass

def compute_morphogenetic_field(bioelectric_state):
    pass

def is_coherent(morphogenetic_field):
    pass

def has_sufficient_plasticity(organism):
    pass

def can_modulate_bioelectricity(organism):
    pass

def measure_current_bioelectric_state():
    pass

def compute_target_bioelectric_state(target_morphology):
    pass

def update_field(field):
    pass

def has_reached_stable_state(field):
    pass

def optimize_structure(cell_types, target_function):
    pass

def compute_optimal_bioelectric_pattern(structure):
    pass

def simulate_xenobot_behavior(structure, bioelectric_pattern, cognitive_architecture):
    pass

def assess_basal_cognition(organism):
    pass

def compute_cognitive_light_cone(current_state):
    pass

def adjust_for_cognitive_range(intervention_plan, cognitive_range):
    pass

def compute_cognitive_state(field):
    pass

def apply_cognitive_influence(field, cognitive_state):
    pass

def design_basal_cognitive_system(target_function):
    pass

def identify_system_components(biological_system):
    pass

def map_information_channels(components):
    pass

def simulate_information_dynamics(information_channels):
    pass

def interpret_cognitive_aspects(flow_dynamics):
    pass

def identify_emergent_behaviors(flow_dynamics):
    pass




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
        NIST Suborder 6106.01 Ver. 1 (Uncontrolled Copy in Print) Page 1
Open Source Code
NIST S 6106.01
Issue Date: 12/06/2018
Effective Date: 12/06/2018
PURPOSE
The purpose of this directive is to define requirements for promoting software code reuse by
making custom-developed Federal source code broadly available across the National Institute of
Standards and Technology (NIST) in support of NIST programs.
APPLICABILITY
This directive applies to all projects within NIST that commission development of custom
software that will be used in a production capacity (i.e., intended to support a collection of users
outside the developer’s immediate organization), except for software covered under Section 6 of
Office of Management and Budget (OMB) Memorandum M-16-21. The requirements outlined
herein do not apply retroactively (i.e., they do not require that existing custom-developed code
be retroactively made available for Government-wide reuse or as open source software.
REFERENCES
• National Defense Authorization Act 2015 (FITARA) (Title VIII, Subtitle D. H.R. 3979);
• Clinger Cohen Act 1996, (USC Title 40 Chapter 113 11301-11303);
• Office of Management and Budget, Memorandum 15-14: Management and Oversight of
Federal Information Technology;
• Office of Management and Budget, Memorandum16-21: Federal Source Code Policy:
Achieving Efficiency, Transparency, and Innovation through Reusable and Open Source
Software;
This directive is supplemental to a suite of security controls consisting of:
• Department of Commerce, Information Technology Security Program Policy (ITSPP);
• Department of Commerce, Commerce Information Technology Requirements (CITRs);
• Department of Commerce, Source Code Policy;
• NIST, Special Publication 800-53, Security and Privacy Controls for Federal Information
Systems and Organizations, System and Services Acquisition (SA) Family; and
• NIST, Information Security Directives.
NIST Suborder 6106.01 Ver 1.0 (Uncontrolled Copy in Print) Page 2
DEFINITIONS
Custom-Developed Code1
– Custom-developed code is code that is first produced in the
performance of a Federal contract or is otherwise fully funded by the Federal Government,
including code, or segregable portions of code, for which the Government could obtain unlimited
rights under Federal Acquisition Regulations (FAR) Pt. 27 and relevant agency FAR
Supplements. Custom-developed code also includes code developed by agency employees as
part of their official duties. For the purposes of this policy, custom-developed code may include,
but is not limited to, code written for software projects, modules, plugins, scripts, middleware,
and APIs; it does not, however, include code that is truly exploratory or disposable in nature,
such as that written by a developer experimenting with a new language or library.
Open Source Software (OSS) – Software that can be accessed, used, modified, and shared by
anyone. OSS is often distributed under licenses that comply with the definition of "Open Source"
provided by the Open Source Initiative and/or that meet the definition of "Free Software"
provided by the Free Software Foundation.
Source Code – Computer commands written in a computer programming language that is meant
to be read by people. Generally, source code is a higher-level representation of computer
commands as they are written by people and, therefore, must be assembled, interpreted, or
compiled before a computer can execute the code as a program.
REQUIREMENTS
1. An appropriate alternatives analysis will be conducted, incorporating the Three-Step
Software Solutions Analysis in the alternatives analysis process, as defined in section 3 of
OMB M-16-21.
2. At least 20 percent of newly commissioned custom-developed code will be released as
OSS.
3. Newly commissioned custom-developed code which is OSS must be registered in the
Department of Commerce (DOC) Software Code Inventory.
4. Newly commissioned custom-developed code must include documentation that describes
the function, input and output of the module, and any other information relevant to its
reuse.
5. Sufficient rights to newly commissioned custom-developed code to fulfill both the
Government-wide reuse objectives and the open source release objectives will be
obtained.
6. OSS will not automatically be treated as noncommercial software.

1 As defined in Department of Commerce Source Code Policy.
NIST Suborder 6106.01 Ver 1.0 (Uncontrolled Copy in Print) Page 3
7. Exceptions to the requirement defined in this directive may be granted if the following
exemption criteria are met:
a. The sharing of the source code is restricted by law or regulation, including but not
limited to patent or intellectual property law, the Export Asset Regulations, the
International Traffic in Arms Regulation, and the Federal laws and regulations
governing classified information; or
b. The sharing of the source code would create identifiable risk to the detriment of
national security, confidentiality of Government information, or individual privacy;
or
c. The sharing of the source code would create an identifiable risk to the stability,
security, or integrity of NIST’s systems or personnel; or
d. The sharing of the source code would create an identifiable risk to NIST’s mission,
programs, or operations; or
e. The NIST Chief Information Officer (CIO) believes it is in the national interest to
exempt sharing the source code.
8. Exception requests must explain why compliance is unachievable and must be approved
in writing by the NIST CIO.
ROLES AND RESPONSIBILITES
Office of the Director
• Ensure compliance with the directive across the entire organization.
NIST Chief Information Officer
• Collect statistics on compliance with this directive annually.
• Review and approve exemptions from this directive.
Office of Information Systems Management
• Assist in the determination of what code is reusable.
• Ensure all custom OSS is registered in the DOC Software Code Inventory.
• Manage this directive to ensure alignment with Federal and DOC policies.
DIRECTIVE OWNER
18 - Office of Information Systems Management
APPENDICES
A. Revision History
NIST Suborder 6106.01 Ver 1.0 (Uncontrolled Copy in Print) Page 4
Appendix A
REVISION HISTORY
Revision Date Responsible Person Description of Change
11/20/2018 Islelly Castillo
(OISM)
Initial Version
Rev. .01

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
        