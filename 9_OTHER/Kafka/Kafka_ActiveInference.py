import json
from typing import Dict, List, Tuple
from kafka import KafkaAdminClient, KafkaConsumer, KafkaProducer
from kafka.admin import NewTopic, ConfigResource, ConfigResourceType
from kafka.errors import TopicAlreadyExistsError
from kafka.structs import TopicPartition
import numpy as np
from scipy.special import softmax, kl_divergence
import logging
from dataclasses import dataclass
from collections import deque

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@dataclass
class KafkaSystemState:
    topic_count: int
    total_partitions: int
    total_messages: int
    consumer_group_count: int

class KafkaActiveInference:
    def __init__(self, bootstrap_servers: List[str], num_states: int, num_observations: int, num_actions: int):
        self.bootstrap_servers = bootstrap_servers
        self.admin_client = KafkaAdminClient(bootstrap_servers=bootstrap_servers)
        self.producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        self.consumer = KafkaConsumer(
            bootstrap_servers=bootstrap_servers,
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='active_inference_group',
            value_deserializer=lambda x: json.loads(x.decode('utf-8'))
        )
        
        # Active Inference model parameters
        self.num_states = num_states
        self.num_observations = num_observations
        self.num_actions = num_actions
        self.beliefs = np.ones((num_states,)) / num_states
        self.preferences = np.random.randn(num_observations)
        self.policies = np.eye(num_actions)
        self.transition_model = self._normalize(np.random.rand(num_states, num_states, num_actions))
        self.likelihood_model = self._normalize(np.random.rand(num_observations, num_states))
        self.learning_rate = 0.01
        
        # Free Energy Principle components
        self.prior_beliefs = np.ones((num_states,)) / num_states
        self.free_energy_history = deque(maxlen=100)
        self.kl_divergence_history = deque(maxlen=100)
        
        # Kafka system state
        self.kafka_state = KafkaSystemState(0, 0, 0, 0)

    @staticmethod
    def _normalize(matrix: np.ndarray) -> np.ndarray:
        return matrix / matrix.sum(axis=-1, keepdims=True)

    def create_topic(self, topic_name: str, num_partitions: int = 1, replication_factor: int = 1):
        new_topic = NewTopic(name=topic_name, num_partitions=num_partitions, replication_factor=replication_factor)
        try:
            self.admin_client.create_topics([new_topic])
            logger.info(f"Topic '{topic_name}' created successfully")
        except TopicAlreadyExistsError:
            logger.warning(f"Topic '{topic_name}' already exists")

    def produce_message(self, topic: str, message: Dict):
        self.producer.send(topic, value=message)
        self.producer.flush()
        logger.info(f"Produced message to topic '{topic}': {message}")

    def consume_messages(self, topic: str, timeout_ms: int = 1000) -> List[Dict]:
        self.consumer.subscribe([topic])
        messages = []
        for message in self.consumer.poll(timeout_ms=timeout_ms).values():
            for record in message:
                messages.append(record.value)
        return messages

    def free_energy(self, observations: np.ndarray) -> float:
        """
        Calculate the variational free energy.
        
        This function implements the core concept of the Free Energy Principle,
        quantifying the difference between the agent's internal model and the actual observations.
        """
        expected_log_likelihood = np.dot(observations, np.log(np.dot(self.likelihood_model, self.beliefs) + 1e-10))
        entropy = -np.sum(self.beliefs * np.log(self.beliefs + 1e-10))
        kl_div = kl_divergence(self.beliefs, self.prior_beliefs)
        
        fe = -expected_log_likelihood + kl_div - entropy
        self.free_energy_history.append(fe)
        self.kl_divergence_history.append(kl_div)
        
        return fe

    def update_beliefs(self, action: int, observation: int) -> None:
        """
        Update beliefs using Bayesian inference, a key component of active inference.
        """
        likelihood = self.likelihood_model[observation, :]
        prior = np.dot(self.transition_model[:, :, action].T, self.beliefs)
        posterior = likelihood * prior
        self.beliefs = posterior / np.sum(posterior)

    def expected_free_energy(self, policy: np.ndarray) -> float:
        """
        Calculate the expected free energy for a given policy.
        
        This function is crucial for action selection in active inference,
        as it quantifies the expected information gain and goal-directedness of actions.
        """
        G = 0
        beliefs = self.beliefs.copy()
        for action in policy:
            expected_beliefs = np.dot(self.transition_model[:, :, action].T, beliefs)
            expected_observations = np.dot(self.likelihood_model, expected_beliefs)
            
            # Information gain (epistemic value)
            information_gain = kl_divergence(expected_observations, np.dot(self.likelihood_model, self.prior_beliefs))
            
            # Expected value (pragmatic value)
            expected_value = np.dot(expected_observations, self.preferences)
            
            G += information_gain + expected_value
            beliefs = expected_beliefs
        return -G

    def select_action(self) -> int:
        """
        Select an action based on minimizing expected free energy.
        """
        action_values = np.array([self.expected_free_energy(policy) for policy in self.policies])
        action_probabilities = softmax(-action_values)
        return np.random.choice(self.num_actions, p=action_probabilities)

    def update_model(self, prev_action: int, prev_observation: int, curr_observation: int) -> None:
        """
        Update the generative model (transition and likelihood models) based on observations.
        
        This implements the learning aspect of active inference, allowing the agent to refine
        its internal model of the environment over time.
        """
        prediction_error = np.eye(self.num_observations)[curr_observation] - np.dot(self.likelihood_model, np.dot(self.transition_model[:, :, prev_action].T, self.beliefs))
        
        self.likelihood_model += self.learning_rate * np.outer(prediction_error, self.beliefs)
        self.transition_model[:, :, prev_action] += self.learning_rate * np.outer(self.beliefs, prediction_error).T
        
        self.likelihood_model = self._normalize(self.likelihood_model)
        self.transition_model = self._normalize(self.transition_model)

    def process_kafka_event(self, event: Dict) -> int:
        """
        Process a Kafka event using active inference principles.
        """
        observation = hash(json.dumps(event, sort_keys=True)) % self.num_observations
        
        action = self.select_action()
        self.update_beliefs(action, observation)
        
        fe = self.free_energy(np.eye(self.num_observations)[observation])
        
        logger.info(f"Processed event: {event}")
        logger.info(f"Selected Action: {action}, Free Energy: {fe}")
        logger.info(f"Updated Beliefs: {self.beliefs}")
        logger.info(f"KL Divergence: {self.kl_divergence_history[-1]}")
        
        return action

    def run_active_inference_loop(self, input_topic: str, output_topic: str, max_iterations: int = 100):
        """
        Run the main active inference loop for processing Kafka events.
        """
        for iteration in range(max_iterations):
            messages = self.consume_messages(input_topic)
            for message in messages:
                action = self.process_kafka_event(message)
                self.produce_message(output_topic, {"action": action, "original_message": message})
            
            # Update the model based on the latest action and observation
            if len(messages) > 0:
                prev_action = action
                prev_observation = hash(json.dumps(messages[-2], sort_keys=True)) % self.num_observations if len(messages) > 1 else 0
                curr_observation = hash(json.dumps(messages[-1], sort_keys=True)) % self.num_observations
                self.update_model(prev_action, prev_observation, curr_observation)
            
            # Periodically analyze the Kafka system
            if iteration % 10 == 0:
                self.analyze_kafka_system()

    def analyze_kafka_system(self):
        """
        Analyze the Kafka system state and update the internal representation.
        """
        topics = self.admin_client.list_topics()
        total_partitions = 0
        total_messages = 0

        for topic in topics:
            config = self.admin_client.describe_configs(
                [ConfigResource(ConfigResourceType.TOPIC, topic)]
            )
            logger.info(f"Topic '{topic}' configuration: {config}")

            consumer = KafkaConsumer(
                topic,
                bootstrap_servers=self.bootstrap_servers,
                auto_offset_reset='earliest'
            )
            partitions = consumer.partitions_for_topic(topic)
            if partitions:
                total_partitions += len(partitions)
                for partition in partitions:
                    tp = TopicPartition(topic, partition)
                    consumer.assign([tp])
                    consumer.seek_to_end(tp)
                    last_offset = consumer.position(tp)
                    consumer.seek_to_beginning(tp)
                    first_offset = consumer.position(tp)
                    total_messages += last_offset - first_offset
                    logger.info(f"Topic '{topic}', Partition {partition}: "
                                f"First Offset = {first_offset}, Last Offset = {last_offset}")
            consumer.close()

        consumer_groups = self.admin_client.list_consumer_groups()
        logger.info(f"Consumer Groups: {consumer_groups}")

        self.kafka_state = KafkaSystemState(
            topic_count=len(topics),
            total_partitions=total_partitions,
            total_messages=total_messages,
            consumer_group_count=len(consumer_groups)
        )

        logger.info(f"Updated Kafka System State: {self.kafka_state}")

    def run(self, input_topic: str, output_topic: str, max_iterations: int = 100):
        """
        Main function to run the Kafka Active Inference system.
        """
        self.create_topic(input_topic)
        self.create_topic(output_topic)
        self.analyze_kafka_system()
        self.run_active_inference_loop(input_topic, output_topic, max_iterations)
        
        # Final analysis
        logger.info("Final Free Energy Analysis:")
        logger.info(f"Average Free Energy: {np.mean(self.free_energy_history)}")
        logger.info(f"Average KL Divergence: {np.mean(self.kl_divergence_history)}")
        logger.info(f"Final Kafka System State: {self.kafka_state}")

# Example usage
if __name__ == "__main__":
    kafka_ai = KafkaActiveInference(['localhost:9092'], num_states=10, num_observations=20, num_actions=5)
    kafka_ai.run("input_topic", "output_topic", max_iterations=1000)
