import networkx as nx
from typing import Dict, List, Tuple, Optional, Union
from enum import Enum, auto
import json
import time

class NostrEventKind(Enum):
    SET_METADATA = 0
    TEXT_NOTE = 1
    RECOMMEND_SERVER = 2
    CONTACT_LIST = 3
    ENCRYPTED_DIRECT_MESSAGE = 4
    DELETION = 5
    REPOST = 6
    REACTION = 7
    BADGE_AWARD = 8
    CHANNEL_CREATION = 40
    CHANNEL_METADATA = 41
    CHANNEL_MESSAGE = 42
    CHANNEL_HIDE_MESSAGE = 43
    CHANNEL_MUTE_USER = 44
    REPORTING = 1984
    ZAP_REQUEST = 9734
    ZAP_RECEIPT = 9735
    AUTHENTICATION = 22242
    LONG_FORM_CONTENT = 30023

class NostrEvent:
    def __init__(self, kind: NostrEventKind, content: str, tags: List[List[str]], pubkey: str):
        self.id = ""  # To be set after signing
        self.pubkey = pubkey
        self.created_at = int(time.time())
        self.kind = kind
        self.tags = tags
        self.content = content
        self.sig = ""  # To be set after signing

    def to_json(self) -> str:
        event_dict = {
            "id": self.id,
            "pubkey": self.pubkey,
            "created_at": self.created_at,
            "kind": self.kind.value,
            "tags": self.tags,
            "content": self.content,
            "sig": self.sig
        }
        return json.dumps(event_dict)

class NostrPetriNet:
    def __init__(self):
        self.graph = nx.MultiDiGraph()
        self.places: Dict[str, int] = {}
        self.transitions: Dict[str, Dict[str, int]] = {}
        self.tokens: Dict[str, int] = {}

    def add_place(self, name: str, initial_tokens: int = 0, metadata: Optional[Dict] = None):
        """
        Add a place to the Nostr Petri net.
        
        Args:
            name (str): Unique identifier for the place.
            initial_tokens (int): Initial number of tokens in the place.
            metadata (Optional[Dict]): Additional information about the place.
        """
        self.graph.add_node(name, type='place', metadata=metadata or {})
        self.places[name] = initial_tokens
        self.tokens[name] = initial_tokens

    def add_transition(self, name: str, metadata: Optional[Dict] = None):
        """
        Add a transition to the Nostr Petri net.
        
        Args:
            name (str): Unique identifier for the transition.
            metadata (Optional[Dict]): Additional information about the transition.
        """
        self.graph.add_node(name, type='transition', metadata=metadata or {})
        self.transitions[name] = {}

    def add_arc(self, source: str, target: str, weight: int = 1, metadata: Optional[Dict] = None):
        """
        Add an arc between a place and a transition in the Nostr Petri net.
        
        Args:
            source (str): Name of the source node.
            target (str): Name of the target node.
            weight (int): Number of tokens consumed or produced by the arc.
            metadata (Optional[Dict]): Additional information about the arc.
        """
        self.graph.add_edge(source, target, weight=weight, metadata=metadata or {})
        if self.graph.nodes[source]['type'] == 'place':
            self.transitions[target][source] = weight
        else:
            self.transitions[source][target] = weight

    def is_enabled(self, transition: str) -> bool:
        """
        Check if a transition is enabled in the Nostr Petri net.
        
        Args:
            transition (str): Name of the transition to check.
        
        Returns:
            bool: True if the transition is enabled, False otherwise.
        """
        return all(self.tokens[place] >= weight for place, weight in self.transitions[transition].items())

    def fire_transition(self, transition: str):
        """
        Fire a transition in the Nostr Petri net if it's enabled.
        
        Args:
            transition (str): Name of the transition to fire.
        
        Raises:
            ValueError: If the transition is not enabled.
        """
        if not self.is_enabled(transition):
            raise ValueError(f"Transition {transition} is not enabled in the Nostr network.")
        
        for place, weight in self.transitions[transition].items():
            self.tokens[place] -= weight
        
        for successor in self.graph.successors(transition):
            if self.graph.nodes[successor]['type'] == 'place':
                weight = self.graph[transition][successor][0]['weight']
                self.tokens[successor] += weight

    def simulate_event_creation(self, pubkey: str, event: NostrEvent):
        """
        Simulate the creation of a Nostr event in the Petri net.
        
        Args:
            pubkey (str): Public key of the user creating the event.
            event (NostrEvent): The Nostr event being created.
        """
        event_id = f"event_{event.kind.name.lower()}_{int(time.time())}"
        self.add_place(f"{pubkey}_idle", initial_tokens=1, metadata={"pubkey": pubkey})
        self.add_place(f"{event_id}_created", metadata={"pubkey": pubkey, "event_type": event.kind.name})
        self.add_transition(f"{pubkey}_create_{event.kind.name}", metadata={"pubkey": pubkey, "action": "create_event", "event_type": event.kind.name})
        self.add_arc(f"{pubkey}_idle", f"{pubkey}_create_{event.kind.name}")
        self.add_arc(f"{pubkey}_create_{event.kind.name}", f"{event_id}_created")
        return event_id

    def simulate_relay_propagation(self, event_id: str, relays: List[str]):
        """
        Simulate the propagation of a Nostr event through multiple relays.
        
        Args:
            event_id (str): Unique identifier of the Nostr event.
            relays (List[str]): List of relay URLs to propagate the event to.
        """
        self.add_place(f"{event_id}_created", initial_tokens=1, metadata={"event_id": event_id})
        for relay in relays:
            self.add_place(f"{relay}_received_{event_id}", metadata={"relay": relay, "event_id": event_id})
            self.add_transition(f"propagate_{event_id}_to_{relay}", metadata={"action": "propagate", "event_id": event_id, "relay": relay})
            self.add_arc(f"{event_id}_created", f"propagate_{event_id}_to_{relay}")
            self.add_arc(f"propagate_{event_id}_to_{relay}", f"{relay}_received_{event_id}")

    def simulate_subscription(self, pubkey: str, relay: str, filters: List[Dict[str, Union[str, int, List[str]]]]):
        """
        Simulate a user subscribing to a Nostr relay with specific filters.
        
        Args:
            pubkey (str): Public key of the subscribing user.
            relay (str): URL of the relay being subscribed to.
            filters (List[Dict[str, Union[str, int, List[str]]]]): List of subscription filters.
        """
        subscription_id = f"sub_{pubkey}_{int(time.time())}"
        self.add_place(f"{pubkey}_not_subscribed_to_{relay}", initial_tokens=1, metadata={"pubkey": pubkey, "relay": relay})
        self.add_place(f"{pubkey}_subscribed_to_{relay}", metadata={"pubkey": pubkey, "relay": relay, "subscription_id": subscription_id, "filters": filters})
        self.add_transition(f"{pubkey}_subscribe_to_{relay}", metadata={"action": "subscribe", "pubkey": pubkey, "relay": relay, "filters": filters})
        self.add_arc(f"{pubkey}_not_subscribed_to_{relay}", f"{pubkey}_subscribe_to_{relay}")
        self.add_arc(f"{pubkey}_subscribe_to_{relay}", f"{pubkey}_subscribed_to_{relay}")

    def simulate_message_flow(self, sender: str, receiver: str, relay: str, event: NostrEvent):
        """
        Simulate the flow of a Nostr message from sender to receiver through a relay.
        
        Args:
            sender (str): Public key of the message sender.
            receiver (str): Public key of the message receiver.
            relay (str): URL of the relay facilitating the message transfer.
            event (NostrEvent): The Nostr event (message) being transferred.
        """
        event_id = f"event_{event.kind.name.lower()}_{int(time.time())}"
        self.add_place(f"{event_id}_created_by_{sender}", initial_tokens=1, metadata={"event_id": event_id, "sender": sender, "event": event.to_json()})
        self.add_place(f"{relay}_received_{event_id}", metadata={"relay": relay, "event_id": event_id})
        self.add_place(f"{receiver}_received_{event_id}", metadata={"receiver": receiver, "event_id": event_id})
        self.add_transition(f"send_{event_id}_to_{relay}", metadata={"action": "send", "event_id": event_id, "sender": sender, "relay": relay})
        self.add_transition(f"relay_{event_id}_to_{receiver}", metadata={"action": "relay", "event_id": event_id, "relay": relay, "receiver": receiver})
        self.add_arc(f"{event_id}_created_by_{sender}", f"send_{event_id}_to_{relay}")
        self.add_arc(f"send_{event_id}_to_{relay}", f"{relay}_received_{event_id}")
        self.add_arc(f"{relay}_received_{event_id}", f"relay_{event_id}_to_{receiver}")
        self.add_arc(f"relay_{event_id}_to_{receiver}", f"{receiver}_received_{event_id}")

    def simulate_nip05_verification(self, pubkey: str, nip05_identifier: str):
        """
        Simulate the NIP-05 verification process for a user.
        
        Args:
            pubkey (str): Public key of the user to be verified.
            nip05_identifier (str): NIP-05 identifier (user@domain.com) to be verified.
        """
        self.add_place(f"{pubkey}_unverified", initial_tokens=1, metadata={"pubkey": pubkey})
        self.add_place(f"{pubkey}_verified", metadata={"pubkey": pubkey, "nip05": nip05_identifier})
        self.add_transition(f"verify_{pubkey}_nip05", metadata={"action": "verify_nip05", "pubkey": pubkey, "nip05": nip05_identifier})
        self.add_arc(f"{pubkey}_unverified", f"verify_{pubkey}_nip05")
        self.add_arc(f"verify_{pubkey}_nip05", f"{pubkey}_verified")

    def simulate_nip26_delegation(self, delegator: str, delegatee: str, conditions: Dict[str, Union[int, List[int]]]):
        """
        Simulate the NIP-26 delegation process.
        
        Args:
            delegator (str): Public key of the delegator.
            delegatee (str): Public key of the delegatee.
            conditions (Dict[str, Union[int, List[int]]]): Delegation conditions (e.g., kinds, since, until).
        """
        delegation_id = f"delegation_{delegator}_{delegatee}_{int(time.time())}"
        self.add_place(f"{delegator}_no_delegation", initial_tokens=1, metadata={"pubkey": delegator})
        self.add_place(f"{delegation_id}_active", metadata={"delegator": delegator, "delegatee": delegatee, "conditions": conditions})
        self.add_transition(f"create_delegation_{delegation_id}", metadata={"action": "create_delegation", "delegator": delegator, "delegatee": delegatee, "conditions": conditions})
        self.add_arc(f"{delegator}_no_delegation", f"create_delegation_{delegation_id}")
        self.add_arc(f"create_delegation_{delegation_id}", f"{delegation_id}_active")

    def analyze_reachability(self) -> Dict[str, int]:
        """
        Analyze the reachability of the Nostr Petri net.
        
        Returns:
            Dict[str, int]: A dictionary mapping place names to their token counts.
        """
        return {place: self.tokens[place] for place in self.places}

    def find_deadlocks(self) -> List[str]:
        """
        Find potential deadlocks in the Nostr Petri net.
        
        Returns:
            List[str]: A list of transition names that are currently deadlocked.
        """
        return [transition for transition in self.transitions if not self.is_enabled(transition)]

    def visualize(self, filename: Optional[str] = None):
        """
        Visualize the Nostr Petri net using networkx and matplotlib.
        
        Args:
            filename (Optional[str]): If provided, save the visualization to this file instead of displaying it.
        """
        import matplotlib.pyplot as plt
        pos = nx.spring_layout(self.graph)
        plt.figure(figsize=(12, 8))
        nx.draw_networkx_nodes(self.graph, pos, node_color='lightblue', node_size=500)
        nx.draw_networkx_edges(self.graph, pos, edge_color='gray', arrows=True)
        nx.draw_networkx_labels(self.graph, pos)
        edge_labels = nx.get_edge_attributes(self.graph, 'weight')
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=edge_labels)
        plt.title("Nostr Petri Net Visualization")
        plt.axis('off')
        if filename:
            plt.savefig(filename)
        else:
            plt.show()

# Example usage:
# nostr_net = NostrPetriNet()
# alice_pubkey = "alice_pubkey"
# bob_pubkey = "bob_pubkey"
# relay_url = "wss://relay.example.com"

# Create and propagate a text note
# text_note = NostrEvent(NostrEventKind.TEXT_NOTE, "Hello, Nostr!", [], alice_pubkey)
# event_id = nostr_net.simulate_event_creation(alice_pubkey, text_note)
# nostr_net.simulate_relay_propagation(event_id, [relay_url])

# Simulate subscription
# filters = [{"kinds": [1, 4], "authors": [alice_pubkey, bob_pubkey]}]
# nostr_net.simulate_subscription(bob_pubkey, relay_url, filters)

# Simulate encrypted direct message
# dm_content = "encrypted_message_content"
# dm = NostrEvent(NostrEventKind.ENCRYPTED_DIRECT_MESSAGE, dm_content, [["p", bob_pubkey]], alice_pubkey)
# nostr_net.simulate_message_flow(alice_pubkey, bob_pubkey, relay_url, dm)

# Simulate NIP-05 verification
# nostr_net.simulate_nip05_verification(alice_pubkey, "alice@example.com")

# Simulate NIP-26 delegation
# delegation_conditions = {"kinds": [1, 4], "until": int(time.time()) + 86400}  # 24-hour delegation
# nostr_net.simulate_event_creation("alice_pubkey", NostrEventType.TEXT_NOTE)
# nostr_net.simulate_relay_propagation("text_note_1", ["wss://relay1.com", "wss://relay2.com"])
# nostr_net.simulate_subscription("bob_pubkey", "wss://relay1.com")
# nostr_net.simulate_message_flow("alice_pubkey", "bob_pubkey", "wss://relay1.com", "encrypted_dm_1")
# nostr_net.visualize("nostr_petri_net.png")
# reachability = nostr_net.analyze_reachability()
# deadlocks = nostr_net.find_deadlocks()
