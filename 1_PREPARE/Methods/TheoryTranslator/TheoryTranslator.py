from typing import List, Dict, Optional
from dataclasses import dataclass

@dataclass
class ThreeMindsPerspective:
    """Represents a perspective with unconscious, conscious, and consciousness components."""
    perspective: str
    unconscious: str
    conscious: str
    consciousness: Optional[str]

class ThreeMindsAnalyzer:
    """Analyzes and compares different Three Minds perspectives."""

    def __init__(self):
        self.perspectives: List[ThreeMindsPerspective] = self._initialize_perspectives()

    def _initialize_perspectives(self) -> List[ThreeMindsPerspective]:
        """Initializes the list of ThreeMindsPerspective instances."""
        return [
            ThreeMindsPerspective("Ancient Greek Philosophy", "Appetite", "Spunk", "Reason"),
            ThreeMindsPerspective("Eastern Philosophy", "Yin", "Yang", "Balance/Harmony"),
            ThreeMindsPerspective("Religious (Saint Paul)", "Carnal", "Soulish", "Spiritual"),
            ThreeMindsPerspective("Spinoza", "Random Experience", "Reason", "Intuition"),
            ThreeMindsPerspective("Earl of Shaftesbury", "Beautiful", "Good", "True"),
            ThreeMindsPerspective("David Hume", "Impressions", "Ideas", "Synthesis"),
            ThreeMindsPerspective("Immanuel Kant (Critiques)", "Judgment", "Practical Reason", "Pure Reason"),
            ThreeMindsPerspective("Kant's Knowledge Categories", "Synthetic A Posteriori", "Analytic A Priori", "Synthetic A Priori"),
            ThreeMindsPerspective("Fichte's Dialectic", "Thesis", "Antithesis", "Synthesis"),
            ThreeMindsPerspective("Jane Austen", "Sensibility", "Sense", "Balance"),
            ThreeMindsPerspective("Charles Sanders Peirce", "Firstness", "Secondness", "Thirdness"),
            ThreeMindsPerspective("Sigmund Freud", "Id", "Ego", "Superego"),
            ThreeMindsPerspective("Georges Dumézil", "Economic", "Martial", "Sacral"),
            ThreeMindsPerspective("Star Trek Characters", "McCoy (Emotion)", "Spock (Logic)", "Kirk (Intuition)"),
            ThreeMindsPerspective("Split-Brain Theory", "Right Hemisphere", "Left Hemisphere", "Integration"),
            ThreeMindsPerspective("Dual Process Theory (Evans)", "Heuristic", "Analytic", "Meta-cognition"),
            ThreeMindsPerspective("Kahneman and Tversky", "System 1", "System 2", "Executive Function"),
            ThreeMindsPerspective("Artificial Intelligence", "Neural Network", "Symbolic", "Combined"),
            ThreeMindsPerspective("Grammar and Narration", "First Person", "Second Person", "Third Person"),
            ThreeMindsPerspective("McGilchrist's Brain Theory", "Right Hemisphere", "Left Hemisphere", "Integrated Consciousness"),
            ThreeMindsPerspective("Gender Stereotypes", "Emotional", "Rational", "Balanced"),
            ThreeMindsPerspective("Decision Theory", "Descriptive", "Normative", "Prescriptive"),
            ThreeMindsPerspective("Haidt's Metaphor", "Elephant (Intuition)", "Rider (Reasoning)", "Harmonious Control")
        ]

    def get_perspective(self, perspective_name: str) -> Optional[ThreeMindsPerspective]:
        """Retrieves a perspective by name, case-insensitive."""
        for perspective in self.perspectives:
            if perspective.perspective.lower() == perspective_name.lower():
                return perspective
        # Improved error message
        print(f"Perspective '{perspective_name}' not found.")
        return None

    def compare_perspectives(self, perspective1: str, perspective2: str) -> Dict[str, List[str]]:
        """Compares two perspectives and returns their components."""
        p1 = self.get_perspective(perspective1)
        p2 = self.get_perspective(perspective2)
        if not p1 or not p2:
            print("One or both perspectives not found for comparison.")
            return {}
        return {
            "Unconscious": [p1.unconscious, p2.unconscious],
            "Conscious": [p1.conscious, p2.conscious],
            "Consciousness": [p1.consciousness, p2.consciousness]
        }

    def analyze_common_themes(self) -> Dict[str, List[str]]:
        """Analyzes and aggregates common themes across all perspectives."""
        themes = {"Unconscious": [], "Conscious": [], "Consciousness": []}
        for perspective in self.perspectives:
            themes["Unconscious"].append(perspective.unconscious)
            themes["Conscious"].append(perspective.conscious)
            if perspective.consciousness:
                themes["Consciousness"].append(perspective.consciousness)
        return themes

# Example usage:
if __name__ == "__main__":
    analyzer = ThreeMindsAnalyzer()
    
    # Get a specific perspective
    freud_perspective = analyzer.get_perspective("Sigmund Freud")
    if freud_perspective:
        print(f"Freud's perspective: Unconscious={freud_perspective.unconscious}, "
              f"Conscious={freud_perspective.conscious}, Consciousness={freud_perspective.consciousness}")
    
    # Compare two perspectives
    comparison = analyzer.compare_perspectives("Ancient Greek Philosophy", "Sigmund Freud")
    if comparison:
        print("Comparison:", comparison)
    
    # Analyze common themes
    themes = analyzer.analyze_common_themes()
    print("Common themes:", themes)