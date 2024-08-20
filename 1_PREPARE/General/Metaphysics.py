import itertools
from typing import List, Dict, Callable, Any, Tuple, Optional, Union
import json
import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict

class MetaphysicsSpecGenerator:
    """
    A sophisticated class to meta-specify all possible metaphysics and narratives based on categorization principles.
    Includes serialization, combination generation, advanced visualization, and analysis capabilities.
    """
    
    def __init__(self):
        self.metaphysics: Dict[str, Dict[str, Any]] = {}
        self.narratives: Dict[str, List[Tuple[str, Callable[[Dict[str, Any]], Dict[str, Any]]]]] = {}
        self.combinations: List[Dict[str, Any]] = []

    def add_metaphysical_concept(self, concept_name: str, properties: Dict[str, Any]) -> None:
        """
        Add a metaphysical concept with its associated properties.

        Args:
            concept_name (str): The name of the metaphysical concept.
            properties (Dict[str, Any]): A dictionary of properties associated with the concept.
        """
        self.metaphysics[concept_name] = properties

    def add_narrative(self, narrative_name: str, sequence: List[Tuple[str, Callable[[Dict[str, Any]], Dict[str, Any]]]]) -> None:
        """
        Add a narrative composed of a sequence of metaphysical transformations.

        Args:
            narrative_name (str): The name of the narrative.
            sequence (List[Tuple[str, Callable[[Dict[str, Any]], Dict[str, Any]]]]): A list of tuples, each containing a step name and a transformation function.
        """
        self.narratives[narrative_name] = sequence

    def generate_combinations(self) -> List[Dict[str, Any]]:
        """
        Generate all possible combinations of metaphysical concepts and narratives,
        returning a list of the resulting states.

        Returns:
            List[Dict[str, Any]]: A list of dictionaries, each representing a combination of concept, narrative, and result.
        """
        self.combinations = [
            {
                "concept": concept_name,
                "narrative": narrative_name,
                "result": self._apply_narrative_to_concept(concept_name, narrative_name, sequence)
            }
            for concept_name, properties in self.metaphysics.items()
            for narrative_name, sequence in self.narratives.items()
        ]
        return self.combinations

    def _apply_narrative_to_concept(self, concept_name: str, narrative_name: str, sequence: List[Tuple[str, Callable[[Dict[str, Any]], Dict[str, Any]]]]) -> Dict[str, Any]:
        """
        Apply a narrative sequence to a metaphysical concept, returning the final state.

        Args:
            concept_name (str): The name of the metaphysical concept.
            narrative_name (str): The name of the narrative.
            sequence (List[Tuple[str, Callable[[Dict[str, Any]], Dict[str, Any]]]]): The sequence of transformations to apply.

        Returns:
            Dict[str, Any]: The final state after applying the narrative.
        """
        current_state = self.metaphysics[concept_name].copy()
        transformation_history = []
        for step_name, transformation in sequence:
            previous_state = current_state.copy()
            current_state = transformation(current_state)
            transformation_history.append({
                "step_name": step_name,
                "before": previous_state,
                "after": current_state
            })
        return {
            "final_state": current_state,
            "transformation_history": transformation_history
        }

    def visualize_metaphysics(self, output_file: str = "metaphysics_visualization.png") -> None:
        """
        Visualize the metaphysical concepts and their narratives using networkx and matplotlib.

        Args:
            output_file (str): The filename to save the visualization. Defaults to "metaphysics_visualization.png".
        """
        G = nx.DiGraph()

        # Add nodes for concepts and narratives
        for concept in self.metaphysics:
            G.add_node(concept, node_type="concept")
        for narrative in self.narratives:
            G.add_node(narrative, node_type="narrative")

        # Add edges based on combinations
        for combo in self.combinations:
            G.add_edge(combo["concept"], combo["narrative"])
            G.add_edge(combo["narrative"], f"{combo['concept']}_{combo['narrative']}_result")

        # Set up node colors and shapes
        color_map = {'concept': 'skyblue', 'narrative': 'lightgreen', 'result': 'salmon'}
        node_colors = [color_map[G.nodes[node]['node_type']] if 'node_type' in G.nodes[node] else color_map['result'] for node in G]

        # Create the visualization
        plt.figure(figsize=(12, 8))
        pos = nx.spring_layout(G, k=0.9, iterations=50)
        nx.draw(G, pos, node_color=node_colors, with_labels=True, node_size=3000, alpha=0.8, font_size=8)
        
        # Add a legend
        legend_elements = [plt.Line2D([0], [0], marker='o', color='w', label=key.capitalize(), markerfacecolor=value, markersize=15) for key, value in color_map.items()]
        plt.legend(handles=legend_elements, loc='upper left')

        plt.title("Metaphysics and Narratives Visualization")
        plt.axis('off')
        plt.tight_layout()
        plt.savefig(output_file, format="png", dpi=300, bbox_inches="tight")
        plt.close()

    def save_to_file(self, filename: str) -> None:
        """
        Serialize the metaphysics and narratives to a JSON file.

        Args:
            filename (str): The name of the file to save the data to.
        """
        serializable_data = {
            "metaphysics": self.metaphysics,
            "narratives": {name: [(step, self._serialize_function(func)) for step, func in sequence] for name, sequence in self.narratives.items()},
            "combinations": self.combinations
        }
        with open(filename, 'w') as file:
            json.dump(serializable_data, file, indent=2)

    def load_from_file(self, filename: str) -> None:
        """
        Load metaphysics and narratives from a JSON file.

        Args:
            filename (str): The name of the file to load the data from.
        """
        with open(filename, 'r') as file:
            data = json.load(file)
            self.metaphysics = data.get("metaphysics", {})
            self.combinations = data.get("combinations", [])
            
            # Reconstruct narratives
            self.narratives = {name: [(step, self._deserialize_function(func_str)) for step, func_str in sequence] 
                               for name, sequence in data.get("narratives", {}).items()}

    def analyze_combinations(self) -> Dict[str, Any]:
        """
        Analyze the generated combinations to provide insights.

        Returns:
            Dict[str, Any]: A dictionary containing various analysis results.
        """
        analysis = {
            "total_combinations": len(self.combinations),
            "concepts_used": set(),
            "narratives_used": set(),
            "property_frequency": defaultdict(int),
            "transformation_frequency": defaultdict(int)
        }

        for combo in self.combinations:
            analysis["concepts_used"].add(combo["concept"])
            analysis["narratives_used"].add(combo["narrative"])
            
            for prop in combo["result"]["final_state"].get("properties", []):
                analysis["property_frequency"][prop] += 1
            
            for step in combo["result"]["transformation_history"]:
                analysis["transformation_frequency"][step["step_name"]] += 1

        analysis["concepts_used"] = list(analysis["concepts_used"])
        analysis["narratives_used"] = list(analysis["narratives_used"])
        analysis["most_common_property"] = max(analysis["property_frequency"], key=analysis["property_frequency"].get)
        analysis["most_common_transformation"] = max(analysis["transformation_frequency"], key=analysis["transformation_frequency"].get)

        return analysis

    @staticmethod
    def _serialize_function(func: Callable) -> str:
        """Serialize a function to a string representation."""
        return func.__name__

    @staticmethod
    def _deserialize_function(func_str: str) -> Callable:
        """Deserialize a function from its string representation."""
        # This is a simplified approach. In a real-world scenario, you might want to use a more robust method.
        return globals()[func_str]

# Example usage
if __name__ == "__main__":
    generator = MetaphysicsSpecGenerator()
    
    # Adding metaphysical concepts
    generator.add_metaphysical_concept("Existence", {"properties": ["being", "consciousness", "reality"]})
    generator.add_metaphysical_concept("Time", {"properties": ["flow", "duration", "change"]})
    generator.add_metaphysical_concept("Space", {"properties": ["dimension", "extension", "locality"]})
    
    # Define transformation functions
    def expand(x: Dict[str, Any]) -> Dict[str, Any]:
        return {**x, "properties": x["properties"] + ["expansion"]}

    def contract(x: Dict[str, Any]) -> Dict[str, Any]:
        return {**x, "properties": [prop for prop in x["properties"] if prop != "expansion"]}

    def transcend(x: Dict[str, Any]) -> Dict[str, Any]:
        return {**x, "properties": x["properties"] + ["transcendence"]}

    def begin(x: Dict[str, Any]) -> Dict[str, Any]:
        return {**x, "properties": x["properties"] + ["origin"]}

    def develop(x: Dict[str, Any]) -> Dict[str, Any]:
        return {**x, "properties": x["properties"] + ["growth"]}

    def end(x: Dict[str, Any]) -> Dict[str, Any]:
        return {**x, "properties": [prop for prop in x["properties"] if prop not in ["origin", "growth"]]}

    # Adding narratives
    generator.add_narrative("Transformation", [
        ("Expand", expand),
        ("Contract", contract),
        ("Transcend", transcend)
    ])
    generator.add_narrative("Cyclical", [
        ("Begin", begin),
        ("Develop", develop),
        ("End", end)
    ])
    
    # Generate combinations
    results = generator.generate_combinations()
    print(f"Generated Combinations: {len(results)}")
    
    # Analyze combinations
    analysis = generator.analyze_combinations()
    print("Analysis Results:")
    print(json.dumps(analysis, indent=2))
    
    # Visualize metaphysics
    generator.visualize_metaphysics()
    
    # Save to file
    generator.save_to_file("metaphysics_spec.json")
    
    # Load from file (for demonstration)
    new_generator = MetaphysicsSpecGenerator()
    new_generator.load_from_file("metaphysics_spec.json")
    print(f"Loaded Metaphysics: {len(new_generator.metaphysics)}")
    print(f"Loaded Narratives: {len(new_generator.narratives)}")
