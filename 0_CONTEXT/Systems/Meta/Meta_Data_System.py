import time
import sys
from typing import Any, Dict, Optional

class Logger:
    def __init__(self, filename: str):
        self.terminal = sys.stdout
        self.log = open(filename, "w")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)
        self.log.flush()

    def flush(self):
        self.terminal.flush()
        self.log.flush()

sys.stdout = Logger("log.txt")

class MetaDataLayer:
    def __init__(self, prefix: str):
        self.prefix = prefix
        self.data: Dict[str, Any] = {}
        self.meta: Dict[float, Dict[str, Any]] = {}

    def add_data(self, key: str, value: Any) -> None:
        prefixed_key = f"{self.prefix}{key}"
        self.data[prefixed_key] = value
        print(f"[{self.prefix}] Added data: {prefixed_key} = {value}")

    def add_meta(self, operation: str, details: Dict[str, Any]) -> None:
        timestamp = time.time()
        self.meta[timestamp] = {'operation': operation, 'details': details}
        print(f"[{self.prefix}] Added meta: {operation} - {details}")

    def query(self, key: Optional[str] = None, meta_filter: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        result = {}
        if key:
            prefixed_key = f"{self.prefix}{key}"
            result['data'] = self.data.get(prefixed_key)
        if meta_filter:
            result['meta'] = {t: m for t, m in self.meta.items() if all(m.get(k) == v for k, v in meta_filter.items())}
        print(f"[{self.prefix}] Query result: {result}")
        return result

class MetaDataSystem:
    def __init__(self):
        self.A_primary = MetaDataLayer("A_")
        self.B_metadata = MetaDataLayer("B_")
        self.C_meta_metadata = MetaDataLayer("C_")
        self.D_meta_meta_metadata = MetaDataLayer("D_")
        self.E_meta_meta_meta_metadata = MetaDataLayer("E_")

    def add_data(self, key: str, value: Any) -> None:
        self.A_primary.add_data(key, value)
        self.B_metadata.add_meta('add_data', {'key': key, 'value': value})
        self.C_meta_metadata.add_meta('add_meta', {'layer': 'B_metadata', 'operation': 'add_data', 'key': key})
        self.D_meta_meta_metadata.add_meta('add_meta', {'layer': 'C_meta_metadata', 'operation': 'add_meta', 'key': key})
        self.E_meta_meta_meta_metadata.add_meta('add_meta', {'layer': 'D_meta_meta_metadata', 'operation': 'add_meta', 'key': key})

    def nest(self, key: str, subsystem: 'MetaDataSystem') -> None:
        self.A_primary.add_data(key, subsystem)
        self.B_metadata.add_meta('nest', {'key': key, 'subsystem': id(subsystem)})
        self.C_meta_metadata.add_meta('add_meta', {'layer': 'B_metadata', 'operation': 'nest', 'key': key})
        self.D_meta_meta_metadata.add_meta('add_meta', {'layer': 'C_meta_metadata', 'operation': 'add_meta', 'key': key})
        self.E_meta_meta_meta_metadata.add_meta('add_meta', {'layer': 'D_meta_meta_metadata', 'operation': 'add_meta', 'key': key})

    def query(self, layer: str, key: Optional[str] = None, meta_filter: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        layers = {
            'A_primary': self.A_primary,
            'B_metadata': self.B_metadata,
            'C_meta_metadata': self.C_meta_metadata,
            'D_meta_meta_metadata': self.D_meta_meta_metadata,
            'E_meta_meta_meta_metadata': self.E_meta_meta_meta_metadata
        }
        if layer in layers:
            return layers[layer].query(key, meta_filter)
        else:
            raise ValueError("Invalid layer. Choose from: " + ", ".join(layers.keys()))

# Usage example
print("Creating main system...")
system = MetaDataSystem()

print("\nAdding user data...")
system.add_data('user', {'name': 'Alice', 'age': 30})

print("\nCreating subsystem...")
subsystem = MetaDataSystem()

print("\nAdding preference to subsystem...")
subsystem.add_data('preference', 'dark mode')

print("\nNesting subsystem...")
system.nest('user_prefs', subsystem)

print("\nQuerying examples:")
for layer in ['A_primary', 'B_metadata', 'C_meta_metadata', 'D_meta_meta_metadata', 'E_meta_meta_meta_metadata']:
    print(f"\n{layer} layer query:")
    if layer == 'A_primary':
        print(system.query(layer, 'user'))
    else:
        print(system.query(layer, meta_filter={'operation': 'add_data'}))

print("\nLogging complete. Check log.txt for the full output.")
