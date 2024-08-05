class SyntheticPhilosophy:
    def __init__(self):
        self.metaphysics = {
            "ontology": "Process-based reality, emphasizing dynamic interactions and emergent properties",
            "mind_body_problem": "Non-reductive physicalism with enactivist and embodied cognition perspectives",
            "free_will": "Compatibilist view, recognizing agency as emerging from complex causal networks",
            "time": "B-theory of time with an emphasis on the subjective experience of temporal flow",
            "causality": "Circular and multi-scale causality, rejecting simple linear models"
        }
        self.metaphysics_keywords = [
            "substance", "essence", "existence", "being", "becoming", "reality", "actuality", "potentiality",
            "universals", "particulars", "identity", "change", "persistence", "mereology", "modality",
            "possible worlds", "necessity", "contingency", "determinism", "indeterminism", "emergence",
            "reductionism", "holism", "materialism", "idealism", "dualism", "monism", "pluralism"
        ]
        
        self.epistemology = {
            "nature_of_knowledge": "Embodied, situated, and culturally embedded",
            "justification": "Coherentist approach with pragmatic considerations",
            "limits_of_knowledge": "Acknowledges inherent limitations due to our embodied and situated nature",
            "sources_of_knowledge": "Sensory experience, reason, intuition, and intersubjective agreement",
            "scientific_method": "Emphasizing the theory-ladenness of observation"
        }
        self.epistemology_keywords = [
            "belief", "truth", "justification", "evidence", "skepticism", "foundationalism", "coherentism",
            "reliabilism", "internalism", "externalism", "a priori", "a posteriori", "empiricism", "rationalism",
            "phenomenology", "hermeneutics", "contextualism", "fallibilism", "verificationism", "falsificationism",
            "induction", "deduction", "abduction", "inference to the best explanation", "epistemic closure",
            "Gettier problems", "epistemic luck", "epistemic virtue", "social epistemology"
        ]
        
        self.ethics = {
            "moral_framework": "Care ethics integrated with virtue ethics and consequentialism",
            "value_theory": "Pluralistic, recognizing multiple sources of value including relational and contextual factors",
            "applied_ethics": "Emphasis on technology ethics, bioethics, and environmental ethics",
            "metaethics": "Moral realism with a recognition of the culturally situated nature of moral beliefs"
        }
        self.ethics_keywords = [
            "deontology", "utilitarianism", "virtue ethics", "care ethics", "contractarianism", "moral relativism",
            "moral absolutism", "moral particularism", "moral universalism", "moral realism", "moral anti-realism",
            "moral naturalism", "moral non-naturalism", "moral cognitivism", "moral non-cognitivism", "emotivism",
            "prescriptivism", "expressivism", "moral motivation", "moral responsibility", "moral luck",
            "moral dilemmas", "supererogation", "moral psychology", "moral development", "moral character"
        ]
        
        self.aesthetics = {
            "nature_of_beauty": "Emergent property arising from the interaction between perceiver and perceived",
            "art_theory": "Emphasizes the embodied and situated nature of artistic creation and appreciation",
            "aesthetic_experience": "Understood through the lens of perception and cognition"
        }
        self.aesthetics_keywords = [
            "beauty", "sublime", "taste", "aesthetic judgment", "aesthetic attitude", "aesthetic experience",
            "aesthetic properties", "aesthetic value", "art", "representation", "expression", "form",
            "content", "style", "genre", "creativity", "imagination", "interpretation", "criticism",
            "aesthetic education", "aesthetic perception", "aesthetic emotion", "aesthetic contemplation"
        ]
        
        self.political_philosophy = {
            "ideal_governance": "Deliberative democracy with a focus on fostering care and relational autonomy",
            "justice": "Capabilities approach integrated with care ethics",
            "rights": "Emphasis on positive rights and collective responsibilities",
            "power": "Analyzed through the lens of complex systems and network theory"
        }
        self.political_philosophy_keywords = [
            "sovereignty", "legitimacy", "authority", "liberty", "equality", "justice", "rights", "democracy",
            "republicanism", "liberalism", "conservatism", "socialism", "anarchism", "feminism", "multiculturalism",
            "cosmopolitanism", "nationalism", "civil society", "public sphere", "social contract", "rule of law",
            "separation of powers", "constitutionalism", "political obligation", "civil disobedience"
        ]
        
        self.philosophy_of_mind = {
            "nature_of_consciousness": "Emergent property of complex, self-organizing systems",
            "cognitive_architecture": "Hierarchical, embodied, and extended cognitive system",
            "personal_identity": "Narrative self-model continuously updated through experience",
            "other_minds": "Understood through social cognition and empathy"
        }
        self.philosophy_of_mind_keywords = [
            "qualia", "intentionality", "mental content", "mental causation", "functionalism", "behaviorism",
            "identity theory", "eliminative materialism", "property dualism", "panpsychism", "emergentism",
            "representationalism", "enactivism", "embodied cognition", "extended mind", "situated cognition",
            "free will", "agency", "self-awareness", "theory of mind", "mental states"
        ]
        
        self.philosophy_of_science = {
            "scientific_realism": "Critical realism acknowledging the mind-independent reality while recognizing the theory-ladenness of observation",
            "theory_change": "Emphasizing paradigm shifts and conceptual revolutions",
            "demarcation": "Fuzzy boundaries between science and non-science, emphasizing methodological naturalism",
            "reductionism": "Advocating for multi-scale explanations and emergent properties"
        }
        self.philosophy_of_science_keywords = [
            "scientific method", "hypothesis", "theory", "law", "explanation", "prediction", "observation",
            "experiment", "measurement", "causation", "correlation", "induction", "deduction", "abduction",
            "falsification", "verification", "paradigm", "research program", "scientific revolution",
            "underdetermination", "theory-ladenness", "scientific progress", "scientific realism",
            "instrumentalism", "constructive empiricism", "scientific models", "idealization"
        ]
        
        self.philosophy_of_technology = {
            "human_technology_relation": "Co-constitutive, emphasizing the embodied and extended nature of cognition",
            "ethics_of_AI": "Care ethics-based approach, focusing on relational autonomy and contextual sensitivity",
            "future_of_humanity": "Techno-social co-evolution guided by ethical considerations and care",
            "digital_ontology": "Information as a fundamental aspect of reality, but not reducible to it"
        }
        self.philosophy_of_technology_keywords = [
            "technological determinism", "social construction of technology", "technological mediation",
            "techno-human symbiosis", "posthumanism", "transhumanism", "artificial intelligence", "virtual reality",
            "cyberspace", "digital ethics", "information ethics", "computer ethics", "roboethics", "technoscience",
            "sociotechnical systems", "technological autonomy", "technological rationality", "digital ontology"
        ]
        
    def key_principles(self):
        return [
            "Reality is fundamentally process-based and dynamic",
            "Cognition is embodied, situated, and extended",
            "Care and relational autonomy are central to ethics and social philosophy",
            "Knowledge is culturally embedded and theory-laden",
            "Consciousness emerges from complex self-organizing systems",
            "Science and philosophy should embrace multi-scale explanations",
            "Technology co-evolves with human cognition and society",
            "Circular causality and complex systems thinking are essential for understanding phenomena",
            "Aesthetics and ethics are grounded in our embodied and situated nature"
        ]
        
    def quotes(self):
        return [
            "The mind is not a computer, but a dynamic, embodied process.",
            "Care is not just an ethical consideration, but a fundamental aspect of cognition and reality.",
            "We are not passive observers of reality, but active participants in its unfolding.",
            "Consciousness is the process by which a system becomes aware of its own existence and place in the world.",
            "Technology is not separate from us, but an extension of our cognitive processes.",
            "The boundaries between mind, body, and world are fluid and constantly negotiated.",
            "Science and philosophy must recognize the circular causality between our theories and our experiences.",
            "Aesthetics is not about passive appreciation, but active engagement with the world.",
            "Political systems should be understood as complex, adaptive networks of care and responsibility.",
            "The future of humanity lies in fostering positive human-AI relations guided by care ethics."
        ]
