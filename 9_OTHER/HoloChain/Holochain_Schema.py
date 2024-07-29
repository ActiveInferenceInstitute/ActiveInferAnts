from typing import List, Dict, Any, Optional
from dataclasses import dataclass
from enum import Enum

# Basic Holochain Types
AgentPubKey = str
EntryHash = str
ActionHash = str
Timestamp = int

# Enum for Entry Types
class EntryType(Enum):
    AGENT = "Agent"
    APP = "App"
    CAPABILITY_GRANT = "CapabilityGrant"
    CAPABILITY_CLAIM = "CapabilityClaim"

# Base Entry
@dataclass
class Entry:
    entry_type: EntryType
    content: Any

# Action Types
class ActionType(Enum):
    CREATE = "Create"
    UPDATE = "Update"
    DELETE = "Delete"

# Action
@dataclass
class Action:
    type: ActionType
    author: AgentPubKey
    timestamp: Timestamp
    entry_hash: Optional[EntryHash] = None
    prev_action: Optional[ActionHash] = None

# Link
@dataclass
class Link:
    base: EntryHash
    target: EntryHash
    tag: str

# Capability Grant
@dataclass
class CapabilityGrant:
    grantor: AgentPubKey
    grantee: Optional[AgentPubKey]
    functions: List[str]
    properties: Dict[str, Any]

# Capability Claim
@dataclass
class CapabilityClaim:
    grantor: AgentPubKey
    secret: str

# DNA
@dataclass
class DNA:
    name: str
    properties: Dict[str, Any]
    zomes: List['Zome']

# Zome
@dataclass
class Zome:
    name: str
    entry_types: List[EntryType]
    functions: List['ZomeFunction']

# Zome Function
@dataclass
class ZomeFunction:
    name: str
    inputs: List[Any]
    outputs: Any

# Cell
@dataclass
class Cell:
    dna: DNA
    agent_pub_key: AgentPubKey

# Conductor
@dataclass
class Conductor:
    cells: List[Cell]
    interfaces: List['Interface']

# Interface
@dataclass
class Interface:
    name: str
    driver: str
    config: Dict[str, Any]

# Validation Package
@dataclass
class ValidationPackage:
    entry: Entry
    action: Action
    validation_data: Any

# Validation Result
@dataclass
class ValidationResult:
    valid: bool
    message: Optional[str] = None

# Query
@dataclass
class Query:
    entry_type: Optional[EntryType] = None
    action_type: Optional[ActionType] = None
    include_entries: bool = True
    time_range: Optional[Dict[str, Timestamp]] = None
    pagination: Optional[Dict[str, int]] = None

# Path
@dataclass
class Path:
    segments: List[str]

# Signal
@dataclass
class Signal:
    name: str
    payload: Any

# Membrane Proof
@dataclass
class MembraneProof:
    payload: Any
    signature: str

# Network Seed
@dataclass
class NetworkSeed:
    network_name: str
    properties: Dict[str, Any]

# These schemas represent the core patterns and data structures in Holochain.
# They can be extended or modified based on specific application requirements.
