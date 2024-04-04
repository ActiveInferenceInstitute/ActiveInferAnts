import itertools
from typing import List, Dict, Callable, Any, Tuple
import networkx as nx
import matplotlib.pyplot as plt

class CategoryTheoryAnalyzer:
    """
    A comprehensive script for advanced intelligence analysis using concepts from Category Theory.
    """
    
    def __init__(self):
        self.objects = {}
        self.morphisms = {}
        self.compositions = {}
        self.identity_morphisms = {}
        self.isomorphisms = {}
        self.epimorphisms = {}
        self.monomorphisms = {}
        self.initial_objects = []
        self.terminal_objects = []

    def add_object(self, obj_name: str, obj_data: Any) -> None:
        """
        Add an object to the category with associated data.
        """
        self.objects[obj_name] = obj_data
        self.identity_morphisms[obj_name] = lambda x: x

    def add_morphism(self, source: str, target: str, morphism: Callable) -> None:
        """
        Add a morphism between two objects.
        """
        if source not in self.objects or target not in self.objects:
            raise ValueError("Source or target object does not exist.")
        self.morphisms[(source, target)] = morphism

    def compose_morphisms(self, source: str, via: str, target: str) -> None:
        """
        Compose two morphisms to create a direct morphism from source to target.
        """
        if (source, via) not in self.morphisms or (via, target) not in self.morphisms:
            raise ValueError("Morphisms for composition do not exist.")
        self.compositions[(source, target)] = lambda x: self.morphisms[(via, target)](self.morphisms[(source, via)](x))

    def find_isomorphisms(self) -> None:
        """
        Find isomorphisms in the category.
        """
        for (source, target), morphism in self.morphisms.items():
            if (target, source) in self.morphisms:
                inverse_morphism = self.morphisms[(target, source)]
                if self._check_isomorphism(morphism, inverse_morphism):
                    self.isomorphisms[(source, target)] = morphism

    def _check_isomorphism(self, morphism: Callable, inverse_morphism: Callable) -> bool:
        """
        Check if two morphisms form an isomorphism.
        """
        # Check if the composition of morphism and inverse_morphism is the identity morphism
        for obj in self.objects:
            if morphism(inverse_morphism(self.objects[obj])) != self.objects[obj]:
                return False
            if inverse_morphism(morphism(self.objects[obj])) != self.objects[obj]:
                return False
        return True

    def find_epimorphisms(self) -> None:
        """
        Find epimorphisms in the category.
        """
        for (source, target), morphism in self.morphisms.items():
            if self._check_epimorphism(morphism):
                self.epimorphisms[(source, target)] = morphism

    def _check_epimorphism(self, morphism: Callable) -> bool:
        """
        Check if a morphism is an epimorphism.
        """
        # A morphism is an epimorphism if it is right-cancellable
        for (source1, target1), morphism1 in self.morphisms.items():
            for (source2, target2), morphism2 in self.morphisms.items():
                if target1 == target2:
                    if morphism1 != morphism2:
                        composed1 = self.compositions.get((source1, target), lambda x: x)
                        composed2 = self.compositions.get((source2, target), lambda x: x)
                        if composed1(morphism(self.objects[source])) == composed2(morphism(self.objects[source])):
                            return False
        return True

    def find_monomorphisms(self) -> None:
        """
        Find monomorphisms in the category.
        """
        for (source, target), morphism in self.morphisms.items():
            if self._check_monomorphism(morphism):
                self.monomorphisms[(source, target)] = morphism

    def _check_monomorphism(self, morphism: Callable) -> bool:
        """
        Check if a morphism is a monomorphism.
        """
        # A morphism is a monomorphism if it is left-cancellable
        for (source1, target1), morphism1 in self.morphisms.items():
            for (source2, target2), morphism2 in self.morphisms.items():
                if source1 == source2:
                    if morphism1 != morphism2:
                        composed1 = self.compositions.get((source1, target), lambda x: x)
                        composed2 = self.compositions.get((source2, target), lambda x: x)
                        if composed1(morphism1(self.objects[source1])) == composed2(morphism2(self.objects[source2])):
                            return False
        return True

    def find_initial_objects(self) -> None:
        """
        Find initial objects in the category.
        """
        for obj in self.objects:
            if self._check_initial_object(obj):
                self.initial_objects.append(obj)

    def _check_initial_object(self, obj: str) -> bool:
        """
        Check if an object is an initial object.
        """
        # An initial object has a unique morphism to every other object
        for target in self.objects:
            if target != obj:
                morphism_exists = False
                for (source, target_obj), morphism in self.morphisms.items():
                    if source == obj and target_obj == target:
                        morphism_exists = True
                        break
                if not morphism_exists:
                    return False
        return True

    def find_terminal_objects(self) -> None:
        """
        Find terminal objects in the category.
        """
        for obj in self.objects:
            if self._check_terminal_object(obj):
                self.terminal_objects.append(obj)

    def _check_terminal_object(self, obj: str) -> bool:
        """
        Check if an object is a terminal object.
        """
        # A terminal object has a unique morphism from every other object
        for source in self.objects:
            if source != obj:
                morphism_exists = False
                for (source_obj, target), morphism in self.morphisms.items():
                    if source_obj == source and target == obj:
                        morphism_exists = True
                        break
                if not morphism_exists:
                    return False
        return True

    def analyze_morphism_properties(self) -> None:
        """
        Analyze and print properties of morphisms such as injectivity, surjectivity, and bijectivity.
        """
        for (source, target), morphism in self.morphisms.items():
            is_injective = self._check_injectivity(morphism)
            is_surjective = self._check_surjectivity(morphism)
            is_bijective = is_injective and is_surjective
            print(f"Morphism from {source} to {target} is {'injective' if is_injective else 'not injective'}, {'surjective' if is_surjective else 'not surjective'}, {'bijective' if is_bijective else 'not bijective'}.")

    def _check_injectivity(self, morphism: Callable) -> bool:
        """
        Check if a morphism is injective.
        """
        # A morphism is injective if it maps distinct elements to distinct elements
        elements = set()
        for obj in self.objects.values():
            if morphism(obj) in elements:
                return False
            elements.add(morphism(obj))
        return True

    def _check_surjectivity(self, morphism: Callable) -> bool:
        """
        Check if a morphism is surjective.
        """
        # A morphism is surjective if every element in the codomain has a preimage
        codomain = set(self.objects.values())
        for obj in codomain:
            preimage_exists = False
            for source_obj in self.objects.values():
                if morphism(source_obj) == obj:
                    preimage_exists = True
                    break
            if not preimage_exists:
                return False
        return True

    def generate_product_objects(self) -> None:
        """
        Generate product objects from all pairs of objects.
        """
        for obj1, obj2 in itertools.combinations(self.objects.keys(), 2):
            product_obj = (self.objects[obj1], self.objects[obj2])
            product_name = f"{obj1}x{obj2}"
            self.objects[product_name] = product_obj
            self.identity_morphisms[product_name] = lambda x: x

            # Define projection morphisms
            proj1 = lambda x: x[0]
            proj2 = lambda x: x[1]
            self.add_morphism(product_name, obj1, proj1)
            self.add_morphism(product_name, obj2, proj2)

            # Define product morphism
            for (source, target1), morphism1 in self.morphisms.items():
                for (source, target2), morphism2 in self.morphisms.items():
                    if target1 == obj1 and target2 == obj2:
                        product_morphism = lambda x: (morphism1(x), morphism2(x))
                        self.add_morphism(source, product_name, product_morphism)

    def apply_functor(self, functor: Callable[[Any], Any]) -> None:
        """
        Apply a functor to transform objects and morphisms in the category.
        """
        transformed_objects = {obj: functor(data) for obj, data in self.objects.items()}
        transformed_morphisms = {(source, target): lambda x: functor(morphism(x)) for (source, target), morphism in self.morphisms.items()}
        self.objects = transformed_objects
        self.morphisms = transformed_morphisms

    def visualize_category(self) -> None:
        """
        Visualize the category with objects and morphisms.
        """
        G = nx.DiGraph()

        # Add objects as nodes
        for obj in self.objects:
            G.add_node(obj)

        # Add morphisms as edges
        for (source, target), morphism in self.morphisms.items():
            G.add_edge(source, target)

        # Draw the graph
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, font_weight='bold')
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