import itertools
from typing import List, Dict, Callable, Any, Tuple, Optional
import json

class MetaphysicsSpecGenerator:
    """
    A class to meta-specify all possible metaphysics and narratives based on categorization principles.
    Enhanced to include serialization and improved combination generation.
    """
    
    def __init__(self):
        self.metaphysics = {}
        self.narratives = {}

    def add_metaphysical_concept(self, concept_name: str, properties: Dict[str, Any]) -> None:
        """
        Add a metaphysical concept with its associated properties.
        """
        self.metaphysics[concept_name] = properties

    def add_narrative(self, narrative_name: str, sequence: List[Tuple[str, Callable[[Any], Any]]]) -> None:
        """
        Add a narrative composed of a sequence of metaphysical transformations.
        """
        self.narratives[narrative_name] = sequence

    def generate_combinations(self) -> List[Dict[str, Any]]:
        """
        Generate all possible combinations of metaphysical concepts and narratives,
        returning a list of the resulting states.
        """
        results = []
        for concept_name, properties in self.metaphysics.items():
            for narrative_name, sequence in self.narratives.items():
                result = self._apply_narrative_to_concept(concept_name, narrative_name, sequence)
                results.append({"concept": concept_name, "narrative": narrative_name, "result": result})
        return results

    def _apply_narrative_to_concept(self, concept_name: str, narrative_name: str, sequence: List[Tuple[str, Callable[[Any], Any]]]) -> Dict[str, Any]:
        """
        Apply a narrative sequence to a metaphysical concept, returning the final state.
        """
        current_state = self.metaphysics[concept_name].copy()  # Ensure original state is not modified
        for step_name, transformation in sequence:
            current_state = transformation(current_state)
        return current_state

    def visualize_metaphysics(self) -> None:
        """
        Visualize the metaphysical concepts and their narratives.
        Placeholder for visualization logic, potentially using graph libraries like networkx or matplotlib.
        """
        pass

    def save_to_file(self, filename: str) -> None:
        """
        Serialize the metaphysics and narratives to a JSON file.
        """
        with open(filename, 'w') as file:
            json.dump({"metaphysics": self.metaphysics, "narratives": str(self.narratives)}, file)

    def load_from_file(self, filename: str) -> None:
        """
        Load metaphysics and narratives from a JSON file.
        Note: Custom narrative functions cannot be directly serialized/deserialized,
        so this method primarily serves to reload metaphysical concepts.
        """
        with open(filename, 'r') as file:
            data = json.load(file)
            self.metaphysics = data.get("metaphysics", {})
            # Narratives require special handling due to containing callables

# Example usage
if __name__ == "__main__":
    generator = MetaphysicsSpecGenerator()
    generator.add_metaphysical_concept("Existence", {"properties": ["being", "consciousness", "reality"]})
    generator.add_narrative("Transformation", [("Expand", lambda x: {**x, "properties": x["properties"] + ["expansion"]}), ("Contract", lambda x: {**x, "properties": [prop for prop in x["properties"] if prop != "expansion"]})])
    results = generator.generate_combinations()
    print(results)
    generator.visualize_metaphysics()
    generator.save_to_file("metaphysics_spec.json")
