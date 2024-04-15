import itertools
from typing import List, Dict, Callable, Any, Tuple, Optional
import networkx as nx
import matplotlib.pyplot as plt

class CategoryTheoryAnalyzer:
    """
    An enhanced script for intelligence analysis incorporating Active Inference principles with Category Theory concepts.
    """
    
    def __init__(self):
        self.objects: Dict[str, Any] = {}
        self.morphisms: Dict[Tuple[str, str], Callable] = {}
        self.compositions: Dict[Tuple[str, str], Callable] = {}
        self.identity_morphisms: Dict[str, Callable] = {}
        self.isomorphisms: Dict[Tuple[str, str], Callable] = {}
        self.epimorphisms: Dict[Tuple[str, str], Callable] = {}
        self.monomorphisms: Dict[Tuple[str, str], Callable] = {}
        self.initial_objects: List[str] = []
        self.terminal_objects: List[str] = []

    def add_object(self, obj_name: str, obj_data: Any) -> None:
        """
        Add an object to the category with associated data, adhering to Active Inference principles.
        """
        if obj_name in self.objects:
            raise ValueError(f"Object {obj_name} already exists.")
        self.objects[obj_name] = obj_data
        self.identity_morphisms[obj_name] = lambda x: x

    def add_morphism(self, source: str, target: str, morphism: Callable) -> None:
        """
        Add a morphism between two objects, ensuring it aligns with Active Inference principles.
        """
        if source not in self.objects or target not in self.objects:
            raise ValueError("Source or target object does not exist.")
        if (source, target) in self.morphisms:
            raise ValueError(f"Morphism from {source} to {target} already exists.")
        self.morphisms[(source, target)] = morphism

    def compose_morphisms(self, source: str, via: str, target: str) -> Optional[Callable]:
        """
        Compose two morphisms to create a direct morphism from source to target, following Active Inference optimization.
        """
        if (source, via) not in self.morphisms or (via, target) not in self.morphisms:
            raise ValueError("Morphisms for composition do not exist.")
        composed_morphism = lambda x: self.morphisms[(via, target)](self.morphisms[(source, via)](x))
        self.compositions[(source, target)] = composed_morphism
        return composed_morphism

    def find_isomorphisms(self) -> Dict[Tuple[str, str], Callable]:
        """
        Identify isomorphisms in the category, utilizing Active Inference to optimize the process.
        """
        isomorphisms = {}
        for (source, target), morphism in self.morphisms.items():
            if (target, source) in self.morphisms:
                inverse_morphism = self.morphisms[(target, source)]
                if self._check_isomorphism(morphism, inverse_morphism):
                    isomorphisms[(source, target)] = morphism
        self.isomorphisms = isomorphisms
        return isomorphisms

    def _check_isomorphism(self, morphism: Callable, inverse_morphism: Callable) -> bool:
        """
        Verify if two morphisms form an isomorphism, incorporating Active Inference principles for efficiency.
        """
        for obj in self.objects.values():
            if morphism(inverse_morphism(obj)) != obj or inverse_morphism(morphism(obj)) != obj:
                return False
        return True

    def find_epimorphisms(self) -> Dict[Tuple[str, str], Callable]:
        """
        Discover epimorphisms in the category, applying Active Inference strategies for enhanced performance.
        """
        epimorphisms = {}
        for (source, target), morphism in self.morphisms.items():
            if self._check_epimorphism(morphism):
                epimorphisms[(source, target)] = morphism
        self.epimorphisms = epimorphisms
        return epimorphisms

    def _check_epimorphism(self, morphism: Callable) -> bool:
        """
        Determine if a morphism is an epimorphism, using Active Inference for effective analysis.
        """
        # Simplified check for epimorphism based on the existence of right inverses
        for target in self.objects:
            if all(morphism(self.objects[source]) != self.objects[target] for source in self.objects):
                return False
        return True

    def find_monomorphisms(self) -> Dict[Tuple[str, str], Callable]:
        """
        Identify monomorphisms in the category, leveraging Active Inference for optimization.
        """
        monomorphisms = {}
        for (source, target), morphism in self.morphisms.items():
            if self._check_monomorphism(morphism):
                monomorphisms[(source, target)] = morphism
        self.monomorphisms = monomorphisms
        return monomorphisms

    def _check_monomorphism(self, morphism: Callable) -> bool:
        """
        Check if a morphism is a monomorphism, incorporating Active Inference principles for efficiency.
        """
        # Simplified check for monomorphism based on the uniqueness of left inverses
        for source in self.objects:
            if all(morphism(self.objects[source]) != morphism(self.objects[other_source]) for other_source in self.objects if other_source != source):
                return False
        return True

    def find_initial_objects(self) -> List[str]:
        """
        Locate initial objects in the category, applying Active Inference for systematic analysis.
        """
        initial_objects = [obj for obj in self.objects if self._check_initial_object(obj)]
        self.initial_objects = initial_objects
        return initial_objects

    def _check_initial_object(self, obj: str) -> bool:
        """
        Verify if an object is an initial object, using Active Inference to streamline the process.
        """
        return all((obj, target) in self.morphisms for target in self.objects if target != obj)

    def find_terminal_objects(self) -> List[str]:
        """
        Discover terminal objects in the category, utilizing Active Inference for efficient identification.
        """
        terminal_objects = [obj for obj in self.objects if self._check_terminal_object(obj)]
        self.terminal_objects = terminal_objects
        return terminal_objects

    def _check_terminal_object(self, obj: str) -> bool:
        """
        Determine if an object is a terminal object, applying Active Inference principles for effective analysis.
        """
        return all((source, obj) in self.morphisms for source in self.objects if source != obj)

    def analyze_morphism_properties(self) -> None:
        """
        Analyze properties of morphisms such as injectivity, surjectivity, and bijectivity, incorporating Active Inference for comprehensive analysis.
        """
        for (source, target), morphism in self.morphisms.items():
            is_injective = self._check_injectivity(morphism)
            is_surjective = self._check_surjectivity(morphism)
            is_bijective = is_injective and is_surjective
            print(f"Morphism from {source} to {target} is {'injective' if is_injective else 'not injective'}, {'surjective' if is_surjective else 'not surjective'}, {'bijective' if is_bijective else 'not bijective'}.")

    def _check_injectivity(self, morphism: Callable) -> bool:
        """
        Verify if a morphism is injective, using Active Inference for optimized analysis.
        """
        return len(set(morphism(obj) for obj in self.objects.values())) == len(self.objects)

    def _check_surjectivity(self, morphism: Callable) -> bool:
        """
        Determine if a morphism is surjective, applying Active Inference principles for effective evaluation.
        """
        codomain = set(self.objects.values())
        return all(any(morphism(source_obj) == obj for source_obj in self.objects.values()) for obj in codomain)

    def generate_product_objects(self) -> None:
        """
        Generate product objects from all pairs of objects, following Active Inference principles for efficient computation.
        """
        for obj1, obj2 in itertools.combinations(self.objects.keys(), 2):
            product_obj = (self.objects[obj1], self.objects[obj2])
            product_name = f"{obj1}x{obj2}"
            self.add_object(product_name, product_obj)

            # Define projection morphisms
            self.add_morphism(product_name, obj1, lambda x: x[0])
            self.add_morphism(product_name, obj2, lambda x: x[1])

            # Define product morphism for each source with morphisms to obj1 and obj2
            for source in self.objects:
                if (source, obj1) in self.morphisms and (source, obj2) in self.morphisms:
                    product_morphism = lambda x, s=source: (self.morphisms[(s, obj1)](x), self.morphisms[(s, obj2)](x))
                    self.add_morphism(source, product_name, product_morphism)

    def apply_functor(self, functor: Callable[[Any], Any]) -> None:
        """
        Apply a functor to transform objects and morphisms in the category, utilizing Active Inference for adaptive transformation.
        """
        self.objects = {obj: functor(data) for obj, data in self.objects.items()}
        self.morphisms = {(source, target): lambda x, f=functor, m=morphism: f(m(x)) for (source, target), morphism in self.morphisms.items()}

    def visualize_category(self) -> None:
        """
        Visualize the category with objects and morphisms, incorporating Active Inference for dynamic representation.
        """
        G = nx.DiGraph()

        # Add objects as nodes
        for obj in self.objects:
            G.add_node(obj)

        # Add morphisms as edges
        for (source, target) in self.morphisms:
            G.add_edge(source, target)

        # Draw the graph
        pos = nx.spring_layout(G, seed=42)  # Seed for reproducible layout
        nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', font_weight='bold', node_size=700, font_size=10)
        plt.show()

# Example usage
if __name__ == "__main__":
    analyzer = CategoryTheoryAnalyzer()
    analyzer.add_object("A", {"data": "Object A data"})
    analyzer.add_object("B", {"data": "Object B data"})
    analyzer.add_object("C", {"data": "Object C data"})
    analyzer.add_morphism("A", "B", lambda x: x["data"] + " transformed by morphism")
    analyzer.add_morphism("B", "C", lambda x: x["data"] + " transformed again")
    analyzer.compose_morphisms("A", "B", "C")
    analyzer.find_isomorphisms()
    analyzer.find_epimorphisms()
    analyzer.find_monomorphisms()
    analyzer.find_initial_objects()
    analyzer.find_terminal_objects()
    analyzer.analyze_morphism_properties()
    analyzer.generate_product_objects()
    analyzer.apply_functor(lambda x: x.upper())
    analyzer.visualize_category()