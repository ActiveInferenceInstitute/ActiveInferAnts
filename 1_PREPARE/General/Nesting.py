import json
from typing import Dict, Any, Union

class CategoryTheorySystem:
    """
    A class to represent and manipulate systems based on Category Theory concepts,
    allowing for the arbitrary nesting of systems. It supports adding objects, morphisms,
    nested systems, along with serialization, deserialization, and querying of the system state.
    """
    
    def __init__(self):
        self.system_components = {
            "objects": {},
            "morphisms": {},
            "systems": {}
        }
    
    def add_component(self, component_type: str, name: str, *args, **kwargs) -> None:
        """
        General method to add objects, morphisms, or systems.
        """
        component_methods = {
            "object": self._add_object,
            "morphism": self._add_morphism,
            "system": self._add_system
        }
        try:
            component_methods[component_type](name, *args, **kwargs)
        except KeyError:
            raise ValueError(f"Unknown component type: {component_type}")
    
    def _add_object(self, name: str, **kwargs) -> None:
        self.system_components["objects"][name] = kwargs
    
    def _add_morphism(self, name: str, source: str, target: str, **kwargs) -> None:
        self.system_components["morphisms"][name] = {
            "source": source, "target": target, **kwargs
        }
    
    def _add_system(self, name: str, objects: Dict[str, Any], morphisms: Dict[str, Any]) -> None:
        self.system_components["systems"][name] = {
            "objects": objects, "morphisms": morphisms
        }
    
    def serialize_system(self, filename: str) -> None:
        """
        Serialize the system to a JSON file.
        """
        with open(filename, 'w') as file:
            json.dump(self.system_components, file, indent=4)
    
    def load_system(self, filename: str) -> None:
        """
        Load a system from a JSON file.
        """
        with open(filename, 'r') as file:
            self.system_components = json.load(file)
    
    def query_component(self, component_type: str, name: str) -> Union[Dict[str, Any], None]:
        """
        Query a specific component by type and name.
        """
        return self.system_components.get(component_type, {}).get(name, None)

    def list_components(self, component_type: str) -> list:
        """
        List all components of a specific type.
        """
        return list(self.system_components.get(component_type, {}).keys())

# Example usage
if __name__ == "__main__":
    ct_system = CategoryTheorySystem()
    ct_system.add_component("object", "ObjectA", property1="value1")
    ct_system.add_component("object", "ObjectB", property2="value2")
    ct_system.add_component("morphism", "Morphism1", "ObjectA", "ObjectB", propertyM="valueM")
    ct_system.add_component("system", "NestedSystem1", {"ObjectA": {"property1": "value1"}}, {"Morphism1": {"source": "ObjectA", "target": "ObjectB", "propertyM": "valueM"}})
    ct_system.serialize_system("category_theory_system.json")
