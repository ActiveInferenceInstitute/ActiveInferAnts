import json
from typing import Dict, List, Tuple
from kafka import KafkaAdminClient, KafkaConsumer, KafkaProducer
from kafka.admin import NewTopic, ConfigResource, ConfigResourceType
from kafka.errors import TopicAlreadyExistsError
import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict

class KafkaPetriNet:
    def __init__(self, bootstrap_servers: List[str]):
        self.bootstrap_servers = bootstrap_servers
        self.admin_client = KafkaAdminClient(bootstrap_servers=bootstrap_servers)
        self.places: Dict[str, int] = {}  # Topic name: number of messages (tokens)
        self.transitions: Dict[str, Tuple[List[str], List[str]]] = {}  # Transition name: (input places, output places)
        self.graph = nx.DiGraph()  # For visualization and analysis

    def create_place(self, topic_name: str, num_partitions: int = 1, replication_factor: int = 1):
        """
        Create a new place (topic) in the Kafka Petri net.
        
        Args:
            topic_name (str): The name of the topic to create.
            num_partitions (int): The number of partitions for the topic.
            replication_factor (int): The replication factor for the topic.
        
        Raises:
            TopicAlreadyExistsError: If the topic already exists.
        """
        new_topic = NewTopic(name=topic_name, num_partitions=num_partitions, replication_factor=replication_factor)
        try:
            self.admin_client.create_topics([new_topic])
            self.places[topic_name] = 0
            self.graph.add_node(topic_name, node_type='place')
            print(f"Place (topic) '{topic_name}' created successfully")
        except TopicAlreadyExistsError:
            print(f"Place (topic) '{topic_name}' already exists")

    def create_transition(self, name: str, input_places: List[str], output_places: List[str]):
        """
        Create a new transition in the Kafka Petri net.
        
        Args:
            name (str): The name of the transition.
            input_places (List[str]): List of input place names.
            output_places (List[str]): List of output place names.
        
        Raises:
            ValueError: If any input or output place does not exist.
        """
        for place in input_places + output_places:
            if place not in self.places:
                raise ValueError(f"Place '{place}' does not exist")
        
        self.transitions[name] = (input_places, output_places)
        self.graph.add_node(name, node_type='transition')
        for input_place in input_places:
            self.graph.add_edge(input_place, name)
        for output_place in output_places:
            self.graph.add_edge(name, output_place)
        print(f"Transition '{name}' created successfully")

    def add_tokens(self, place: str, num_tokens: int):
        """
        Add tokens (messages) to a place (topic).
        
        Args:
            place (str): The name of the place to add tokens to.
            num_tokens (int): The number of tokens to add.
        
        Raises:
            ValueError: If the place does not exist.
        """
        if place not in self.places:
            raise ValueError(f"Place '{place}' does not exist")
        
        producer = KafkaProducer(
            bootstrap_servers=self.bootstrap_servers,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        for i in range(num_tokens):
            producer.send(place, value={"token": i})
        producer.flush()
        self.places[place] += num_tokens
        print(f"Added {num_tokens} tokens to place '{place}'")

    def remove_tokens(self, place: str, num_tokens: int):
        """
        Remove tokens (messages) from a place (topic).
        
        Args:
            place (str): The name of the place to remove tokens from.
            num_tokens (int): The number of tokens to remove.
        
        Raises:
            ValueError: If the place does not exist or if there are insufficient tokens.
        """
        if place not in self.places:
            raise ValueError(f"Place '{place}' does not exist")
        if self.places[place] < num_tokens:
            raise ValueError(f"Insufficient tokens in place '{place}'")
        
        consumer = KafkaConsumer(
            place,
            bootstrap_servers=self.bootstrap_servers,
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='petri_net_group',
            value_deserializer=lambda x: json.loads(x.decode('utf-8'))
        )
        messages = []
        for _ in range(num_tokens):
            try:
                message = next(consumer)
                messages.append(message)
            except StopIteration:
                break
        consumer.close()
        self.places[place] -= len(messages)
        print(f"Removed {len(messages)} tokens from place '{place}'")

    def fire_transition(self, transition_name: str):
        """
        Fire a transition in the Kafka Petri net.
        
        Args:
            transition_name (str): The name of the transition to fire.
        
        Raises:
            ValueError: If the transition does not exist or if there are insufficient tokens in input places.
        """
        if transition_name not in self.transitions:
            raise ValueError(f"Transition '{transition_name}' does not exist")

        input_places, output_places = self.transitions[transition_name]

        # Check if all input places have tokens
        for place in input_places:
            if self.places[place] == 0:
                raise ValueError(f"Cannot fire transition '{transition_name}': insufficient tokens in place '{place}'")

        # Remove tokens from input places
        for place in input_places:
            self.remove_tokens(place, 1)

        # Add tokens to output places
        for place in output_places:
            self.add_tokens(place, 1)

        print(f"Transition '{transition_name}' fired successfully")

    def get_marking(self) -> Dict[str, int]:
        """
        Get the current marking (distribution of tokens) of the Petri net.
        
        Returns:
            Dict[str, int]: A dictionary mapping place names to their token counts.
        """
        return self.places.copy()

    def visualize(self):
        """
        Visualize the Kafka Petri net using NetworkX and Matplotlib.
        """
        pos = nx.spring_layout(self.graph)
        plt.figure(figsize=(12, 8))
        
        # Draw places
        nx.draw_networkx_nodes(self.graph, pos, 
                               node_color='lightblue', 
                               nodelist=[n for n, d in self.graph.nodes(data=True) if d['node_type'] == 'place'])
        
        # Draw transitions
        nx.draw_networkx_nodes(self.graph, pos, 
                               node_color='lightgreen', 
                               nodelist=[n for n, d in self.graph.nodes(data=True) if d['node_type'] == 'transition'],
                               node_shape='s')
        
        # Draw edges
        nx.draw_networkx_edges(self.graph, pos)
        
        # Add labels
        labels = {n: f"{n}\n({self.places.get(n, '')})" for n in self.graph.nodes()}
        nx.draw_networkx_labels(self.graph, pos, labels)
        
        plt.title("Kafka Petri Net Visualization")
        plt.axis('off')
        plt.tight_layout()
        plt.show()

    def analyze(self):
        """
        Analyze the Kafka Petri net for properties like boundedness, liveness, etc.
        """
        print("Kafka Petri Net Analysis:")
        print("Number of places:", len(self.places))
        print("Number of transitions:", len(self.transitions))
        
        # Check for deadlocks
        deadlocks = [t for t, (inputs, _) in self.transitions.items() if all(self.places[p] == 0 for p in inputs)]
        if deadlocks:
            print("Potential deadlocks detected in transitions:", deadlocks)
        else:
            print("No immediate deadlocks detected")
        
        # Check for unbounded places
        unbounded = [p for p, tokens in self.places.items() if tokens > 1000]  # Arbitrary threshold
        if unbounded:
            print("Potentially unbounded places:", unbounded)
        else:
            print("All places appear to be bounded")
        
        # Analyze connectivity
        if nx.is_strongly_connected(self.graph):
            print("The Petri net is strongly connected")
        elif nx.is_weakly_connected(self.graph):
            print("The Petri net is weakly connected")
        else:
            print("The Petri net is not connected")
        
        # Identify source and sink places
        sources = [n for n, d in self.graph.in_degree() if d == 0 and self.graph.nodes[n]['node_type'] == 'place']
        sinks = [n for n, d in self.graph.out_degree() if d == 0 and self.graph.nodes[n]['node_type'] == 'place']
        print("Source places:", sources)
        print("Sink places:", sinks)

# Example usage
if __name__ == "__main__":
    kafka_petri_net = KafkaPetriNet(['localhost:9092'])

    # Create places (topics)
    kafka_petri_net.create_place("input_topic")
    kafka_petri_net.create_place("processing_topic")
    kafka_petri_net.create_place("output_topic")

    # Create transitions
    kafka_petri_net.create_transition("process_data", ["input_topic"], ["processing_topic"])
    kafka_petri_net.create_transition("finalize_data", ["processing_topic"], ["output_topic"])

    # Add initial tokens
    kafka_petri_net.add_tokens("input_topic", 5)

    # Visualize the initial state
    kafka_petri_net.visualize()

    # Fire transitions
    kafka_petri_net.fire_transition("process_data")
    kafka_petri_net.fire_transition("finalize_data")

    # Visualize the final state
    kafka_petri_net.visualize()

    # Analyze the Petri net
    kafka_petri_net.analyze()
