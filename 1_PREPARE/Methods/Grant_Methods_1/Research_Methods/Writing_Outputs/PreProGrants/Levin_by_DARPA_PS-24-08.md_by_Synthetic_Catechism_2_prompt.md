
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
        UNCLASSIFIED
UNCLASSIFIED
Program Solicitation
Rubble to Rockets (R2
)
DARPA STRATEGIC TECHNOLOGY OFFICE (STO)
DARPA-PS-24-08
March 14, 2024
UNCLASSIFIED
UNCLASSIFIED
PROGRAM SOLICITATION OVERVIEW INFORMATION
 Federal Agency Name – Defense Advanced Research Projects Agency (DARPA),
Strategic Technology Office (STO)
 Funding Opportunity Title – Rubble to Rockets (R2
)
 Announcement Type – Initial Announcement
 Funding Opportunity Number – DARPA-PS-24-08
 Dates
o Posting Date: March 14, 2024
o Industry Day: March 18, 2024
o Questions Due Date: March 29, 2024, by 5:00 PM, Eastern Time (ET)
o Abstracts Due Date and Time: April 05, 2024, by 5:00 PM (ET)
o Oral Presentations Due Date and Time: By Government request, estimated 4 weeks
after Abstract submission
 The Defense Advanced Research Projects Agency (DARPA) is soliciting innovative
approaches to address challenges in the following technical areas: contested logistics,
flexible manufacturing, deployable structures production, material informatics, and adaptive
design. Proposed research should investigate innovative approaches that enable
revolutionary advances in the aforementioned science, devices, and/or systems.
 Multiple awards are anticipated.
 Types of instruments that may be awarded – Other Transaction for Prototype agreements
 Agency Contact
The Solicitation Coordinator for this effort can be reached at:
DARPA-PS-24-08@darpa.mil
DARPA/STO
 ATTN: DARPA-PS-24-08
 675 North Randolph Street
 Arlington, VA 22203-2114
UNCLASSIFIED
UNCLASSIFIED
PROGRAM SOLICITATION
Defense Advanced Research Projects Agency (DARPA)
Rubble to Rockets (R2
)
1. PROGRAM INFORMATION
1.1. Background
The R2
 program seeks to enable the manufacture of critical structures using indigenously available
feedstock materials at the time and point of need (Figure 1), in a contested logistics environment,
and break current production paradigms. Current norms utilize structural systems that have an
optimized design based on an assumed, readily available, supply chain of “exquisite” material. In
this construct, any change in material input or operations outside a tightly controlled factory
requires costly re-design due to an inflexible production and design framework. Larger system level
effects of single components, much less whole scale material changes, are unable to be accounted
for without extensive analysis and testing. As such, flexibility is intentionally designed out, forcing
system convergence to point designs reliant on fixed inputs to produce fixed outputs.
Figure 1: R2
 looks to significantly increase the ability to produce critical items at point of need utilizing scavenged material. The
scope of the DARPA program includes updating the design and fabricating a sounding rocket from variable scavenged feedstocks,
with the potential to apply developed knowledge and technology in other capacities at the point of need.
Design flexibility could be revolutionized by building a framework which can account for system
level effects of materials and components. Existing, as well as future systems, would benefit from
an analytical framework for rapid component and/or system changes to incorporate the growing
number of new material developments and updated fabrication methods (e.g., additive
manufacturing), significantly reducing adoption risk.
R2
 seeks to upend the current limitations of forward production enabling the use of indigenously
available material for demanding structural applications while creating a solution that is both
flexible and deployable, while meeting other point of need manufacturing considerations. For
purposes of this solicitation, mobile and deployable are not synonymous. DARPA seeks to break
the need for monolithic facilities with large, immovable footprints; however, R2
 does not
necessarily seek a TEL-on-demand (Transport, Erect, Launch) type of capability. Solutions should
be deployable in a reasonable capacity, but are not required to be tactically mobile/agile on the
battlespace. Proposers should define the CONOPS (concept of operations) and SWaP (size, weight,
and power) their solution is applicable to and how that fits within existing and future Department
of Defense (DoD) capability gaps. Lower SWaP is desirable, however, proposers should balance
capability to achieve metrics with potential CONOPS.
While existing initiatives for forward structures production are advanced and innovative, they
operate under the assumption that pristine raw materials will be readily available with a fixed 
UNCLASSIFIED
UNCLASSIFIED
design with a fixed material, eliminating the flexibility required for forward and supply chain
impacted production. Material conversion, the process of substantially changing the geometric
and/or microstructural features (e.g., atomization, wire extrusion, sheet production, etc.) is typically
limited to large foundries in tightly controlled process configurations utilizing pristine materials.
Any structural use of material requires substantial qualification and analysis of both process and
material. Utilization of scavenged processed material is limited to non-structural applications due to
lack of confidence and inability to meet anticipated design requirements. Furthermore, the greater
the unknowns (e.g., unknown steel alloy or age condition) or less pristine (e.g., painted, rusted, mill
surface), the fewer applications for use exist. This drastically limits an ability to utilize scavenged
processed materials at point of need due to an inability to effectively convert and predict properties
to utilize for structural applications. Advances in material conversion and understanding of
contaminant effects may open entirely new spaces for highly available material with a lower risk
supply chain and improved energy footprint.
This Program Solicitation (PS) calls specifically for Abstracts to be submitted by April 05, 2024,
5:00PM ET. Abstracts will be reviewed by the Government; if selected, the proposer will be asked
to provide an Oral Presentation. Oral Presentations will be reviewed by the Government, and if
selected, may result in a Phase 1 award of an Other Transaction and eligibility to participate in
future Phases of the program.
This PS encourages solutions from all responsible sources capable of satisfying the Government’s
needs, including large and small businesses, nontraditional defense contractors as defined in 10
U.S.C. § 3014, and research institutions as defined in 15 U.S.C. § 638.
1.2. Program Description/Scope
Overall R2
 Program Scope
The R2
 program seeks to take assorted indigenous feedstock materials (starting with pristine
material feedstock), predict the material properties, then adaptively update a 200-350mm diameter
sounding rocket’s structural design with predictive changes in system level performance. To
accomplish this, R2
 aims to create a flexible and deployable manufacturing platform for the
adaptable production and characterization of various raw materials for use in structural fabrication.
R2
 intends to leverage material informatics and innovative processing and manufacturing
techniques in a rapid, iterative design challenge schedule culminating in a subscale pressure test
validation at the end of each primary phase. The objective of R2 is to work with continually more
diverse and unpredictable materials while simultaneously increasing the complexity and
performance of end state structures. It is envisioned that this technology may ultimately consist of
converting pulverized vehicular, structural, and other complex salvaged materials into
manufacturable feedstock.
Competitive proposals will include an integrated system to include novel material conversion
technology, in-line characterization of material properties, and the ability to rapidly iterate on the
development of components by understanding the system-level effects of material
variability/deviations and adapting the final design to meet program metrics. DARPA expects to
select a diverse set of performers across multiple common primary material streams to include
aluminum, steel, plastic, glass, and/or paper. Competitive proposals will also demonstrate a clear
understanding of available, developing, and/or novel material stream-dependent deployable
manufacturing concepts and how that integrates into their overall CONOPS for the R2
 system.
Figure 2 indicates the high-level approach to forward manufacturing envisioned by the R2
 program. 
UNCLASSIFIED
UNCLASSIFIED
As highlighted, R2
 will focus on the conversion, characterization, and adaptive designing aspects
of the creation cycle. DARPA is not interested in the development of new forward deployable
manufacturing cells for metallic or plastic additive manufacturing, but encourages leveraging
existing developments in this technology area to inform the R2
 specific CONOPS. More
conventional manufacturing, such as machining casting, forging, composite layup, and welding
(among many others), are within scope and proposers are encouraged to utilize readily available
and/or easily implemented manufacturing approaches where appropriate.
Figure 2: The focus of the R2
 program lies in its ability to convert, characterize, and use adaptive design to enable forward
manufacturing of structures in isolated logistics environments.
Convert to enable usable form factors with highest possible material property performance. R2
aims to overcome current limitations in processing diverse, complex, or contaminated indigenous
feedstock by developing tooling and processing approaches that can accommodate widely variable
inputs. Utilizing insights from current material conversion efforts (e.g., friction stir-extrusion of
wire from shredded aluminum) along with advances in tooling design (e.g., additive tooling) and
process control (e.g., closed loop feedback control), conversion systems will transform into material
processing units for readily-available scavenged feedstock. Successful proposers will develop
robust, innovative processing approaches to effectively utilize increasingly diverse (e.g., aluminum,
steel, plastic, glass, paper) and difficult (e.g., clean vs contaminated) scavenged feedstock streams
while maintaining high rate (>0.1 m3
/day) of functional feedstock production.
Proposers should define material streams in which they believe their processing capability is
effective. The description of a materials stream should be based on: material family, base materials,
purity, and material forms per the definitions that follow. Material streams that incorporate multiple
base materials within a given material family; multiple material families are preferred. The
combination of materials streams that a process can utilize is referred to as the “domain of
applicability.” Below may serve as a guide in aiding proposer defined domains of applicability, but
should not be considered exhaustive or prescriptive in all possible domains.
 Material Families: High-level material system being processed. Examples include:
o Metals
o Ceramics
o Plastics
UNCLASSIFIED
UNCLASSIFIED
o Composites
o Natural (e.g., wood/paper)
 Base Material: Lower-level identification of the primary constituents of the Material
Family. Examples by Material Family include:
o Metals: Primary element – e.g., iron (Fe) (ferrous), aluminum (Al), nickel (Ni),
titanium (Ti)
o Ceramics: Primary compound – e.g., aluminum oxide, yttrium-stabilized zirconia
(YSZ)
o Plastics: Polymer family – e.g., polyvinyl chloride (PVC), polycarbonate (PC),
polyether ether ketone (PEEK), polyphenylene sulfide (PPS)
o Composites: Resin & reinforcement combination – e.g., polyethylene (PE)/glass
fiber, epoxy/carbon fiber
o Natural: Primary compound – e.g., cellulose
 Purity: Percentage of the material stream, by mass, that is not associated with the base
material(s)
 Form: Material condition needed as input for processing. Examples include:
o Bulk material – e.g., components, thick sections
o Particulate – e.g., ground or chipped materials
o Wire
o Powder
 Material Stream: Single material family, with a mixture of base material(s), and form(s)
 Domain of Applicability: Combinations of independent or blended material streams
Highly diverse material streams are desired, as well as a path to handling blended material streams
containing multiple material families at varying concentrations to reduce the need for cleaning and
sorting material at point of need. Therefore, proposers should include quantitative, as well as
qualitative, descriptions of the differences between the materials streams handled within the
domain of applicability of the proposed process. Examples of quantitative difference metrics
between material streams might include density, melting point, and/or elastic modulus of the base
materials, as well as characteristic size (length scale) of the forms. Proposers should utilize a broad
and diverse domain of applicability that their processing capabilities can support with clear
technology paths. DARPA does not expect proposers to cover every material family, base material,
purity, or form of a material within their domain of applicability.
Within proposer defined domains of applicability, the Government team will provide materials for
periodic design trials as described in Section 1.4. Proposers should consider that rate is volumetric
to encourage a variety of material solutions regardless of density. Competitive proposals will
consider domains of applicability that would be available in a wide array of environments.
Characterize: establish error reduction to provide useable material property prediction for design.
R2
 will update and develop material informatics models to predict minimum material properties of
diverse material streams with high confidence according to the metrics in section 1.5. Proposers
may consider the use of online analysis (e.g., torque or power use) of the material conversion
process along with rapid testing (e.g., hardness) to achieve this goal, however, novel or processdependent approaches are encouraged. Proposers will be challenged to utilize material informatics 
UNCLASSIFIED
UNCLASSIFIED
“in reverse,” using a given new material and predicting property data as opposed to using material
data to predict a new material. Material property prediction should include feedstock production
and final manufacturing. Any anticipated heat treatment or post processing to improve material
properties should be included in the overall CONOPS. The primary objective is not to fully
characterize material properties, but to efficiently identify a lower bound design value for which
system level effects can be captured. Multiple common industry standard mechanical testing and
statistical approaches may be utilized to build and validate models. Balancing improved material
properties with error minimization is expected to present a broad solution space.
Adaptive Design: trained, low C-SWaP (Computational – Size, Weight, and Power) adaptive
design framework. R2
 will aim to efficiently update a base design to enable structural changes for
components with the newly predicted material properties that meets or exceeds the minimum range
metric as described in Section 1.5. Multiple evolving technologies of interest include change
propagation analysis, and machine learning/artificial intelligence (ML/AI)-assisted finite element
analysis (FEA). Alternative and/or integrated approaches are highly encouraged to meet the
program objectives.
The adaptive design framework will assume a fixed outer mold line (OML) and maximum flight
loads for the Government sounding rocket design, then challenge proposers to build a trained model
which can rapidly (<1 hour) update the design, confirm viability, and predict impacts on range
given the available materials. Designs should be manufacturable based on the complete system
CONOPS integrating target manufacturing approach. Production of demonstration components to
validate material properties and designs is required.
Competitive proposals will feature a low C-SWaP that allows for processing on a standard-issue
laptop or similar basic computer. Any model training or analysis for development can be completed
using alternate computational resources. Competitive proposals will also include the ability for endusers to understand and choose between trade-offs in range and payload. DARPA is not interested
in a framework that is only capable of producing singular point designs for a given material.
1.3. Acquisition Strategy
The R2
 program consists of a single Technical Area (TA). Abstracts for the overall effort (Phase 1
and Phase 2) are sought in response to this PS.
The Government’s aim is to lower the administrative burden to entry, reduce program risk, foster
competition, and have performing teams begin work faster. To facilitate this objective, the
Government will use the following acquisition process for R2
:
1. Abstracts: Through this solicitation, the Government requests proposers to submit Abstracts
(see Section 3.2) in response to this PS. The Government will review all submitted
Abstracts for technical comprehension and ability (see Section 3.3). Selected proposers will
be invited to provide an Oral Presentation (see Section 3.4) to the Government.
2. Oral Presentations: Upon the Government’s request, proposers will have the opportunity to
present their proposal to the DARPA program team. The Government will evaluate all Oral
Presentations (see Section 3.5) and anticipate that selected proposers will enter into contract
negotiations for an OT award with a 36-month period of performance.
3. Phase 1 (base) (18 months): Phase 1 will be individually negotiated using an OT mechanism
for award. This phase will focus on converting indigenous feedstock to useable material,
characterizing the material properties, and adaptively updating and understanding the
system level design, with traceability to contested logistics environments.
UNCLASSIFIED
UNCLASSIFIED
4. Phase 2 (option) (18 month): Phase 2 will be a priced option. This phase will focus on
finding the limits of material conversion for structural designs by incorporating multiple
domains of applicability and increasingly diverse scavenged feedstocks. It is anticipated that
not all Phase 1 (base) performers will become Phase 2 (option) performers.
5. Phase 2 Demonstration (currently not being solicited) (6 months): at the conclusion of
Phase 2 (option), DARPA anticipates a demonstration phase for a static fire test. Proposers
can assume a Government test facility will be available as Government furnished equipment
(GFE) for this test. Phase 2 (option) performers will be given instructions on submitting
proposals during Phase 2 (option) of the program. It is anticipated not all Phase 2 (option)
performers will become Phase 2 Demonstration performers.
The process and requirements for Abstract and Oral Presentation submissions are detailed in
Section 2.1 of this PS. The anticipated timeline and major milestone for the acquisition strategy
laid out above is illustrated in Figure 3 (figure is not to scale).
Figure 3:Anticipated Acquisition Strategy Timeline (not to scale)
1.4. Program Structure
As shown in Figure 4, R2
 will be executed over Phase 1 (Base), Phase 2 (Option), and Phase 2
Demonstration (not currently being solicited). Performers will work with the Government team
throughout the program lifecycle to convey stakeholder interests, facilitate testing as required, and
connect performers with the operational community.
The anticipated events shown in Figure 4 are not a prescribed structure of milestone payments and
proposers should consider their technology development path and approach when setting proper
milestones. The design trial events are expected to occur at performer sites and may include
Government team observers. Each design trial will be preceded by a test readiness review (TRR)
conducted virtually. Design trials will consist of a provided fixed volume of material within the
performer’s domain of applicability and the performer will convert, predict material properties, and
update the design within the metric window. The pressure tests at the end of each primary phase
are expected to be conducted by the Government team at Government facilities using performer’s
manufactured vessels.
Technical Interchange Meetings (TIMs) and design review meetings are expected to be held at
performer sites with Government team participation. In addition, DARPA and the Government
team expect to interact virtually with the performer teams in bi-weekly program update meetings.
Program kick-off and close-out events are expected to be held at DARPA in Arlington, Virginia.
Performers should also expect to write and submit quarterly and final reports. The final program
deliverable at the end of Phase 2 (option) is a validated system design (material conversion and
material property analytics) and accompanying design code and instructions for implementation. 
UNCLASSIFIED
UNCLASSIFIED
Phase 1 (Base)
Phase 1 (base) is an 18-month effort to establish proof-of-concept work for a new manufacturing
paradigm. Phase 1 (base) is motivated by the assumption that pristine indigenous materials can be
scavenged at or near point of need from local stockpiles. The primary focuses of this phase are risk
reduction, technology proof of concept, and integrated system design to validate potential
CONOPS. Performers will be challenged with an iterative series of design trials wherein performers
will be given sorted scavenged feedstock materials that progressively increase in diversity,
complexity, and/or contamination to convert into sounding rockets that meet the metrics specified
in section 1.5. Performers will only progress into converting increasingly diverse and challenging
material streams upon demonstrating successful Phase 1 metrics close out as validated by the
Government team.
Phase 2 (Option)
Phase 2 (option) is an 18-month effort centered around expanding the limits of material conversion
and adaptive design for structures. Phase 2 (option) is motivated by the assumption that a greater
set of indigenous materials may be available in local stockpiles in a non-pristine condition.
Performers are to produce and demonstrate a pilot-scale system capable of achieving the set Phase
2 (option) metrics while continuing to improve their adaptive design model framework created in
Phase 1 (base) with new, more complex material trials.
Phase 2 Demonstration (not currently being solicited)
The Phase 2 Demonstration would take place after the conclusion of Phase 2 (option). It would
consist of a 6-month effort in which a single performer would conduct an integrated static fire test
of a 200-350mm sounding rocket made entirely of converted materials with solid rocket fuel.
Figure 4: R2
 program lifecycle and phasing.
1.5. Program Goals/Metrics
R2
 metrics are fundamentally concerned with the following (also shown in Figure 5) within the
context of a deployable system, as defined earlier:
 Conversion: can you process the scavenged feedstock given into a manufacturable
material?
 Characterize: do you understand the material properties of the material you created?
 Adaptive Design: can you produce a feasible design with tailored range and payload
fraction?
R2
 aims to demonstrate material conversion at a rate of 0.1 m3
/day from scavenged processed
feedstock, verified by iterative design trials and pressure testing of representative rocket motor
chambers to simulate peak load survivability. Performers will also be measured on their ability to 
UNCLASSIFIED
UNCLASSIFIED
predict with low error the yield strength and elastic modulus of given materials (standard materials
analysis), the ability to update designs for minimum and variable range (measured by Government
team analysis tool set to be developed on the program), and confirming manufacturing capabilities
with a representative burst pressure test. For range flexibility, DARPA is not seeking a single point
design solution within a performer’s material domains of applicability; DARPA is seeking an
adaptive design framework that can dynamically produce multiple solutions which vary in
performance above the minimum 35 km threshold range.
* From the government determined scavenged feedstock streams, performers must identify a domain of applicability in which
metrics can be retired. Government will define feedstocks based on their ability to be indigenously scavenged, pristine refers to a
highly curated and predictable starting state.
** 200-350mm diameter vessel produced from performer selected domain of applicability.
*** Demonstration of capability at subscale sufficient.
Figure 5: R2
 baseline metric chart
Material property prediction evaluation: Performers are expected to utilize internal or commercial
test capacity to validate predictions. Proposers should identify the statistical methodologies which
will demonstrate predictive capacity of the approach. The goal is to demonstrate high confidence
in minimum values, not to fully characterize material properties. This should be applicable across
multiple proposer-defined domains of applicability (e.g., material type, composition space,
contaminate threshold, etc.). Proposers should identify how these domains of applicability fit into
their proposed CONOPS and ability to execute operation of the R2
 system globally. Diversity of
materials will be taken into consideration when evaluating proposals and DARPA intends to ensure
a wide variety of material systems are represented among performers.
Adaptive design tool evaluation: Proposers should demonstrate an ability to rapidly update a
Government-provided sounding rocket design with a new material. Performers will periodically be
challenged with Government provided material streams within their defined domains of
applicability for which they will predict material properties and update the design in the time
dictated in the metrics table. Performers should have the ability to vary payload size to achieve
selected ranges while closing on a viable rocket design with an overall minimum range of 35 km. 
UNCLASSIFIED
UNCLASSIFIED
Performers may use typical ballistic calculations and publicly available data on potential propellent
performance to baseline range predictions. The adaptive design tool should be able to run on a
standard issue laptop or similar basic computer.
Burst pressure testing: Performers should anticipate producing pressure vessels as sub-components
of the standard sounding rocket design provided. These will be produced from Government
provided material streams within performer-defined domains of applicability. Performers will have
one week to design and begin production of the vessels and provide predictive performance to the
Government team. Burst pressure testing and posttest analysis will be provided by the Government.
Constraints: Performers should consider and justify how their system can be scaled in a deployable
configuration to > 0.1 m3
/day feedstock production.
Anticipated role of IV&V (Independent Verification and Validation): Periodic Design Trials will
be executed starting around months 6-9 of the program in which Government team members will
provide a curated subset of materials to performers to convert into feedstock and demonstrate a
design update based on material properties in < 1 week in Phase 1 (Base) and < 1 day in Phase 2
(Option). The IV&V team may monitor production at the performer site. The IV&V team is
anticipated to provide a tool for evaluation of anticipated range based on material and design
configurations from performers.
The primary risk of R2 is uncovering certain material and design combinations that will be unable
to produce viable structures. Performers will be challenged with increasingly variable and/or
diverse material streams to push the limits of usable materials. Ultimately, DARPA seeks to
understand the spectrum of material combinations from ideal to infeasible solutions.
During Phase 1 (base), performers should verify the analytical capabilities for both material
property prediction and adaptive design framework. Performers should demonstrate effective risk
mitigation and a path to system level capabilities which meet program objectives.
During Phase 2 (option), designs for a scaled pilot system should keep the following objectives in
mind: rocket is to be ground launched and non-human rated, with an objective range (>35 km);
contain a solid fuel system; and have a 200-350mm diameter. During Phase 2 (option), performance
will be validated in burst pressure testing in a 200-350mm vessel such as a sounding rocket.
2. PS AUTHORITY
This PS may result in the award of an Other Transaction (OT) for Prototype agreement, which can
include not only commercially-available technologies fueled by commercial or strategic
investment, but also concept demonstrations, pilots, and agile development activities that can
incrementally improve commercial technologies, existing Government-owned capabilities, and/or
concepts for broad defense and/or public application(s). The Government reserves the right to
award an OT for Prototypes under 10 U.S.C. § 4022, or make no award at all. In all cases, the
Government agreements officer shall have sole discretion to negotiate all agreement terms and
conditions with selected offerors. The OT agreement will not require cost sharing unless the offeror
is a traditional defense contractor who is not working with a non-traditional defense contractor
participating in the program to a significant extent.
2.1. PS Procedure
In response to this solicitation offerors are asked to submit a 3-page Abstract as described in Section
3.2. This process allows DARPA to ascertain (1) whether the proposers understand the key
challenges of the R2
 program, and (2) whether they are capable of executing a proposed concept. 
UNCLASSIFIED
UNCLASSIFIED
Specific evaluation criteria used to make the assessment can be found in Section 3.3. If DARPA
finds that both of these conditions are met, it may request the offeror participate in an Oral
Presentation to DARPA, as described in Section 3.4, where the proposed technical solution will be
evaluated. Specific evaluation criteria used to make the assessment can be found in Section 3.5.
After the Oral Presentations, DARPA will make a determination as to which offerors may be
awarded an OT for Prototypes agreement for Phase 1 (base) and Phase 2 (option) of the program;
instructions to submit a full proposal for Phase 2 Demonstration will be provided during the
execution of Phase 2 (option). The Government will not pay offerors responding to this PS for the
costs associated with Abstract submissions or Oral Presentations.
Abstracts (result if successful: invitation to participate in Oral Presentations)
Abstracts shall be submitted as specified in Section 3 of this PS. The Government will evaluate
abstracts against the criteria stated in this PS.
It is important to note that offerors must submit an Abstract in response to this solicitation to be
considered for participation in the R2
 program. Offerors will not be invited to provide an Oral
Presentation, or be included in any further progression of the program, without participating in the
Abstract phase of the solicitation.
Oral Presentations (result if successful: Phase 1 (Base) award (18-month period of performance),
with Phase 2 (Option) (18-month period of performance)
Offerors responding to this PS may be invited to further explain their proposed approach and
solution via an Oral Presentation. Oral Presentations will take place approximately four weeks after
notification from the Government that an Oral Presentation is requested. Additional instructions (to
include content due date and presentation date/time) will be provided within the official invitation
to participate in Oral Presentations.
Awards (for Phase 1 (Base) and Phase 2 (Option))
DARPA will review Oral Presentations to determine which proposed solutions sufficiently meet
the evaluation criteria stated in Section 3.5. Upon favorable review, and subject to the availability
of funds, the Government may award an OT for Prototypes under 10 U.S.C. § 4022.
3. GUIDELINES FOR ABSTRACTS, ORAL PRESENTATIONS, AND
PROPOSALS
3.1. General Guidelines
a. Do not include elaborate brochures or marketing materials; only include information
relevant to the submission requirements or evaluation criteria.
b. Use of a diagram(s) or figure(s) to depict the essence of the proposed solution is
permitted.
c. All Abstracts, Oral Presentations, and Proposals are expected to be unclassified.
Classified material pertaining to relevant experience may be submitted on a case-bycase basis. Requests for the ability to submit classified material should be submitted to
DARPA-PS-24-08@darpa.mil prior to the submission deadline for adjudication.
d. Offerors are responsible for clearly identifying proprietary information. Submissions
containing proprietary information must have the cover page and each page containing
such information clearly marked with a label such as “Proprietary” or “Company 
UNCLASSIFIED
UNCLASSIFIED
Proprietary.” NOTE: “Confidential” is a classification marking used to control the
dissemination of U.S. Government National Security Information as dictated in
Executive Order 13526 and should not be used to identify proprietary business
information.
e. Questions can be sent to DARPA-PS-24-08@darpa.mil by March 29, 2024, 5:00 PM
(ET).
f. Send Abstracts to DARPA-PS-24-08@darpa.mil by April 05, 2024, 5:00 PM (ET).
Files containing Controlled Unclassified Information (CUI) must be encrypted when
sending over the Internet. If e-mail encryption is infeasible, contact DARPA-PS-24-
08@darpa.mil within 48 hours before the deadline to arrange another method of
delivery, such as DoD SAFE.
g. Submissions sent through other mediums, channels, or after the prescribed PS deadline
will not be considered, reviewed, nor evaluated.
h. Offerors providing Abstracts that are not invited to an Oral Presentation will be
notified in writing as soon as practicable.
3.2. Abstract Content
a. Abstracts should not exceed three (3) single-sided 8.5” by 11” written pages using 12-
point Times New Roman font with 1” margins all around.
b. Abstracts must include the following:
1. Title page: Offeror Name, Title, Date, Point of Contact Name, E-Mail Address,
Phone, Address, and Commercial and Government Entity (CAGE) Code (if
available). The Title Page does not count against page limits; the title page may not
contain any non-administrative data.
 The offeror shall include a statement that no people on the offeror’s team work
for DARPA as Scientific Engineering Technical Assistance (SETA), Advisory
and Assistance Services (A&AS) or similar support services, as DARPA has a
policy prohibiting such people from working as a technical performer. Include
this statement on the title page; it will NOT count as part of the three (3) written
pages limit.
2. Technical Understanding: Provide a summary of the technical goals of R2
. This
summary shall be stated in the offeror’s own words without any “copy and paste” of
this solicitation. The goal is for the offeror to demonstrate clear understanding of
R2
’s purpose and goals. The summary shall be no more than 1 page and is included
in the three (3) written pages limit.
 Cost Rough Order of Magnitude (ROM): Provide a ROM for the total cost of
Phase 1 (base) and Phase 2 (option) (not Phase 2 Demonstration) of the proposed
solution with minimal, high-level instantiations of said cost. This cost can be
given as a range. The ROM will not count against the page limit but should not
be more than ¼-½ page. 
UNCLASSIFIED
UNCLASSIFIED
3. Technical Challenges: Identify specific technical challenges faced in R2
. The
offeror should include what they think the primary risks are to successful
development of the R2 program. This section shall be no more than 1.5 pages and is
included in the three (3) written pages limit.
4. Technical Ability: Detail the offeror’s team and organization and explain the ability
to be successful at achieving the goals, if selected, for R2
. The offeror may include
past experience, organizational capabilities, team members’ qualifications, or
anything else that demonstrates competence in designing and executing the R2
. This
section shall be no more than 1 page and is included in the three (3) written pages
limit.
3.3. Abstracts – Process and Basis of Evaluation
Abstract evaluation criteria are listed in order of importance. Individual Abstracts will be evaluated
against the evaluation criteria described below:
a. Technical Comprehension: The proposed technical understanding is accurate, and key
technical challenges and risks are identified.
b. Technical Ability: The offerors demonstrate an ability, if selected, to achieve the goals of
the R2 program.
Abstracts will be evaluated by DARPA using the evaluation criteria listed above. DARPA will use
the evaluation criteria to assess similarities, differences, strengths, and weaknesses of the competing
abstracts and, ultimately, use that assessment to determine the selection of those proposers offered
the opportunity to proceed to Oral Presentations. The Government will endeavor to complete the
evaluation of Abstracts within 10 business days of the closing of the submittal period. As stated
above, offerors are required to submit an Abstract for evaluation by DARPA to minimize effort and
reduce the potential expense of preparing an unsuccessful proposal. DARPA will respond to the 3-
page Abstract with a statement as to whether DARPA is interested in seeing a 1 hour (approximately
40 minutes presentation, 20 minutes question and answer period) Oral Presentation. If DARPA is
not interested in an Oral Presentation, it will state this in an email to the offeror. Specific feedback
and informal feedback sessions will not be permitted for Abstracts. Upon review of Abstracts, the
Government may elect to invite all, some, or none of the offerors to Oral Presentations. Only
Abstract offerors invited by DARPA to participate in Oral Presentations are eligible to provide
one.
3.4. Oral Presentations Content
If DARPA expresses interest in an Oral Presentation, the offeror will be asked to provide a
presentation to provide further details on its proposed solution. Specific instructions (including
content submission guidelines) will be provided in the invitation to participate. If selected, offerors
can expect to be asked to provide the following information (offeror can address them in any order
they choose):
a. Company introduction/overview: Provide information regarding company and key
personnel dedicated to the program and how their past performance and qualifications
will contribute to the technical approach. Identify and explain efforts of similar scope
and complexity.
b. Technical Approach: Provide a technical approach to accomplish the objectives and 
UNCLASSIFIED
UNCLASSIFIED
scope laid out in this solicitation. This should include at least the following elements:
1. Description of the offeror’s overall proposed solution, to include CONOPS, anticipated
capability, and summary of innovative claims.
2. Detailed description of innovative claims and how they will achieve R2
 objectives and
metrics. These should at least include:
• Material conversion strategy of managing variable material steams with
targeted feedstock output.
• Manner in which the proposer intends to develop a high confidence
understanding of the converted feedstock.
• Adaptive design methodology that is low C-SWaP, flexible, with accurate
system performance prediction.
3. Technical Risks and Mitigation Strategy.
4. Program development timeline ensuring to highlight technical and programmatic
milestones.
c. Price breakdown for Phase 1 (base) and Phase 2 (option). Budget overview should be
contained in one slide that will count against the limit. The price breakdown for Phase
1 (base) and Phase 2 (option) should be loaded across major milestone events that
define the level of effort across the program during execution. Additionally, the budget
shall identify any risks present in the proposal that may manifest in increased cost to
the program. Proposers are asked to submit an instantiated, high level cost ROM for
the Phase 2 Demonstration. The full details of the price breakdown shall be included
as a separate cost volume (Volume II) to be submitted with Oral Presentations.
d. Teaming/subcontractors: Identify any teammates or subcontractors expected to
comprise the team. Identify their roles, any key personnel, and how their past
performance and qualifications will contribute to the technical approach. Include
required or unique capabilities that enable technical approach.
e. Data Rights: Identify the proposed patent or data rights to be given to the Government
under this agreement for the components of the proposed solution. For intellectual
property (IP) developed prior to the start of the agreement that will be utilized during
program activities, clearly identify that IP and the anticipated level of IP rights that
will be given to the Government. Identify any items that would not give the
Government full and unlimited rights including, but not limited to: anticipated license
restrictions, patents, etc.
In addition to the above required areas, the Government may request the offeror provide additional
information or detail with respect to its Abstract. Offerors should expect to have approximately 40
minutes for presentation and approximately 20 minutes to address any questions from the
Government panel. Oral presentations are subject to the following constraints:
 No more than 20 slides in PDF or PowerPoint format
 No smaller than 10-point font; this includes text in figures
 Video demonstrations are allowed
 Detailed budget information should be submitted as a separate cost spreadsheet and
does not count towards the slide/page count for Oral Presentations. The cost 
UNCLASSIFIED
UNCLASSIFIED
spreadsheet shall include all proposed material purchases with supporting
documentation such as recent purchase orders, commercial catalogs, etc.
 Additional required artifacts not included in page/slide count:
o Any redlines to the model OT Agreement
 Non-Traditional Defense Contractor (NTDC) Attestations (to include
both qualifying information, and participation details)
 See Draft OT Article XIX
 All proposed cost share should be reflected in the milestones of the OT
o Value analysis responses (questions below)
o Completed OT representations and certifications, available at the following
link: https://www.darpa.mil/work-with-us/reps-certs
o Loaded integrated master schedule to include staffing plan showing proposed
labor hours broken down by task
 All presented material is to be submitted to DARPA-PS-24-08@darpa.mil at least 48 hours
before the start of the Oral Presentation. Files containing Controlled Unclassified
Information (CUI) must be encrypted when sending over the Internet. If the file size is too
large for email, send an email to the address above for further instructions.
R2
 Value Assessment Questions for Proposers
1. Please provide your understanding of current technology in this space, and how it has
informed or influenced your proposed technical solution.
2. How does your proposed solution deliver increased capability beyond what is possible
today?
3. How would your proposed solution, if successful, enable federal entities to do that they
cannot already?
a. How much time and money could the DoD / Federal Government save when
compared to the current state of technology?
b. What future value does this technology offer to the DoD / Federal Government?
c. What commercial best practices or processes do you plan to instantiate to deliver
value to the Government?
4. How would your proposed solution, if successful, enable the commercial markets to do that
they cannot already?
a. What future value does this technology offer to the commercial sector?
b. Is your solution disruptive to the market, or does it provide incremental
improvements to current practices?
5. Detail the technical risks in your proposal to be solved under the DARPA program. How
does DARPA engaging in this program accelerate the timeline for value, schedule, technical
debt, and transition to commercial or DoD marketplaces?
3.5. Oral Presentations – Process and Basis of Evaluation
Oral presentation evaluation criteria are listed in order of importance. Individual presentations will
be evaluated against the evaluation criteria described below:
a. Technical Approach: The proposed technical approach is reasonable, feasible, and
innovative. The approach demonstrates an innovative yet feasible approach to address the
identified technical risks and challenges and meet program metrics.
UNCLASSIFIED
UNCLASSIFIED
b. Relevant Qualifications: Personnel and/or company experience and qualifications are
accurate, relevant, and demonstrate the ability of the offeror to meet the technical goals of
the program.
c. Budget: The proposed solution is reasonable, realistic, and affordable.
d. Schedule: The proposed solution will be executed on a reasonable and realistic timeline.
e. Data Rights: Extent to which data assertions allow the Government to realize the
objectives of the R2 program.
The Government intends to give proposers the option to attend Oral Presentations in-person or
virtually. Note, in either case the Government reserves the right to record presentations. The
Government will evaluate information provided in the content submission (documentation), the
Oral Presentation, and Q&A (question and answer) session as basis for evaluation. Oral
Presentations will be evaluated by the R2 Program Manager with support from a panel composed
of Government subject matter experts (SMEs).
After completing evaluation of Oral Presentations, DARPA will: 1) make an 18-month award for
Phase 1 (base) and 18-month Phase 2 (option) of the program; 2) inform the offeror that its proposed
concept/technology/solution is not of continued interest to the Government and they are no longer
considered for participation in the program. If DARPA does not intend to issue an award for the
Phase 1 effort to an offeror, DARPA may provide brief feedback to the offeror regarding the
rationale for the decision.
4. AWARDS
4.1. General Guidelines
Upon favorable review of the proposal and subject to the availability of funds, the Government may
choose to award an OT for Prototypes agreement for Phase 1 (base) and Phase 2 (option).
The Agreements Officer reserves the right to negotiate directly with the offeror on the terms and
conditions prior to execution of the resulting OT agreement, including payment terms, and will
execute the agreement on behalf of the Government. A copy of the draft OT agreement is attached
to this PS for review. In order to speed up negotiations, offerors selected for Oral Presentations will
be required to either attest to compliance of all OT agreement articles or note those they take
exception to. Be advised, only a Government Agreements Officer has the authority to enter into, or
modify, a binding agreement on behalf of the United States Government.
In order to receive an award:
a. Offerors must have a Unique Identity ID number and must register in the System for
Award Management (SAM). Offerors are advised to commence SAM registration upon
notification of entry to the competition.
b. Offerors must also register in the prescribed Government invoicing system (Wide Area
Work Flow: https://wawf.eb.mil/xhtml/unauth/registration/notice.xhtml). DARPA
Contracts Management Office (CMO) personnel will provide assistance to those offerors
from whom a proposal is requested.
c. Offerors must be determined to be responsible by the Agreements Officer and must not
be suspended or debarred from award by the Federal Government nor be prohibited by
Presidential Executive Order and/or law from receiving an award.
UNCLASSIFIED
UNCLASSIFIED
d. Being asked to submit a proposal does not guarantee that an offeror will receive an
award. The Government reserves the right not to make an award.
4.2. Controlled Unclassified Information (CUI) and Controlled Technical Information
(CTI) on Non-DoD Information Systems
Further information on Controlled Unclassified Information identification, marking, protecting
and control, to include processing on Non-DoD Information Systems, is incorporated herein and
can be found at www.darpa.mil/work-with-us/additional-baa. A program-specific CUI Guide has
been established to help offerors determine CUI thresholds for information relevant to, and
technologies developed under the program. As CTI is anticipated for this program, foreign proposers
are encouraged to understand U.S. export law and have a plan in place to obtain export licenses when
necessary. Possible methods include teaming with a U.S. prime and/or having a U.S.
subsidiary/parent company. The CUI Guide for R2
 is provided as an Appendix.
4.3. Representations and Certifications
All offerors are required to submit DARPA-specific representations and certifications for Prototype
OT awards in order to be eligible to receive an OT award. See http://www.darpa.mil/work-withus/reps-certs for further information on required representations and certifications for Prototype OT
awards.
4.4. Competition Sensitive Information
DARPA policy is to treat all submissions as competition sensitive, and to disclose their contents only
for the purpose of evaluation. Restrictive notices notwithstanding, during the evaluation process,
submissions may be handled by support contractors for administrative purposes and/or to assist with
technical evaluation. All DARPA support contractors performing this role are expressly prohibited
from performing DARPA sponsored technical research and are bound by appropriate nondisclosure
agreements. Input on technical aspects of the proposals may be solicited by DARPA from nonGovernment consultants/experts who are strictly bound by the appropriate non-disclosure
requirements.
4.5. Phase 1 & Phase 2 Intellectual Property / Data Rights
The Government will require Government purpose rights, as defined in Section 5 of this PS, to IP
developed under the program until an agreement is reached during negotiations for Phase 1 of R2
.
4.6. Procurement Integrity Act (PIA)
All awards under this PS shall be treated as Federal Agency procurements for purposes of 41 U.S.C.
Chapter 21. Accordingly, the PS competitive solicitation process and awards made thereof must
adhere to the ethical standards required by the PIA.
5. PS DEFINITIONS
“Data” refers to recorded information, regardless of form or method of recording, which includes
but is not limited to, technical data, software, mask works and trade secrets. The term does not
include financial, administrative, cost, pricing or management information and does not include
inventions.
“Government Purpose” means any activity in which the United States Government is a party,
including cooperative agreements with international or multi-national defense organizations, or
sales or transfers by the United States Government to foreign governments or international 
UNCLASSIFIED
UNCLASSIFIED
organizations. Government purposes do not include the rights to use, modify, reproduce, release,
perform, display, or disclose technical data for commercial purposes or authorize others to do so.
“Government Purpose Rights” means the rights to use, duplicate, or disclose Data, in whole or in
part and in any manner, for Government Purposes only, and to have or permit others to do so for
Government Purposes only.
“Limited Rights” means the rights to use, modify, reproduce, release, perform, display, or disclose
Data, in whole or in part, within the Government, to include Government support contractors.
“Nontraditional Defense Contractor” is defined in 10 U.S.C. § 3014 as an entity that is not
currently performing and has not performed, for at least the one-year period preceding the
solicitation of sources by the DoD for the procurement or transaction, any contract or subcontract
for the DoD that is subject to full coverage under the cost accounting standards prescribed pursuant
to 41 U.S.C. § 1502 and the regulations implementing such section. This includes all small business
concerns under the criteria and size standards in 15 U.S.C. § 632 and 13 C.F.R. Part 121.
"Other Transaction” refers to the type of OT that may be awarded as a result of this PS. This type
of OT is authorized by 10 U.S.C. § 4022 for prototype projects directly relevant to enhancing the
mission effectiveness of military personnel and the supporting platforms, systems, components, or
materials proposed to be acquired or developed by the DoD, or for the improvement of platforms,
systems, components, or materials in use by the armed forces.
“Prototype Project” is described in the DoD Other Transactions Guide (Version 1, Nov. 2018)
issued by the Office of the Under Secretary of Defense for Acquisition and Sustainment:
https://www.dau.edu/cop/ot/documents/dod-other-transactions-guide
“Restricted Rights” applies only to noncommercial computer software and means the
Government’s right to use, modify, reproduce, perform, display, release disclose or transfer
computer software are restricted, except that the Government may use a computer program on a
limited number of computers and make the minimum number of copies of the computer software
required for safekeeping (archive), backup, or modification purposes. The Government will not
transfer the software outside of the Government or for any purpose other than the R2
 program,
except that the Government may allow the use of the noncommercial computer software outside of
the Government under a limited set of circumstances, including use by a covered Government
support contractor in performance of its covered Government support contract (management and
administrative support), and after the contractor or subcontractor asserting the restriction is notified
in writing as far in advance as practicable that a release or disclosure to particular contractors or
subcontractor is planned to be made.
“Small Business Concerns” is defined in the Small Business Act (15 U.S.C. § 632).
6. ACRONYMS
A&AS: Advisor and Assistance Services
Al: Aluminum
CAGE Code: Commercial and Government Entity Code
CMO: Contracts Management Office
CONOPS: Concept of Operations
CUI: Controlled Unclassified Information
C-SWaP: Computational – Size, Weight, and Power
UNCLASSIFIED
UNCLASSIFIED
DARPA: Defense Advanced Research Projects Agency
DoD: Department of Defense
ET: Eastern Time
Fe: Iron
FEA: Finite Element Analysis
GFE: Government Furnished Equipment
IP: Intellectual Property
IV&V: Independent Verification and Validation
km: Kilometer
m3
: cubic meters
ML/AI: Machine Learning/Artificial Intelligence
mm: Millimeter
Ni: Nickel
OML: Outer Mold Line
OT: Other Transaction
OTH: Over the Horizon
PC: Polycarbonate
PE: Polyethylene
PEEK: Polyether Ether Ketone
PIA: Program Integrity Act
PPS: Polyphenylene Sulfide
PS: Program Solicitation
PVC: Polyvinyl Chloride
Q&A: Question and Answer
R2
: Rubble to Rockets
ROM: Rough Order of Magnitude
SAM: System for Award Management
SETA: Scientific Engineering and Technical Assistant
SME: Subject Matter Expert
STO: Strategic Technology Office
SWaP: Size, Weight, and Power
TA: Technical Area
TEL: Transport, Erect, Launch
Ti: Titanium
TIM: Technical Interchange Meeting
TRR: Test Readiness Review
YSZ: Yttrium-Stabilized Zirconia

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
        