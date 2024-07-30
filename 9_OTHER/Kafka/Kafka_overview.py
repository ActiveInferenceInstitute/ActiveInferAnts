"""
Apache Kafka Overview

Apache Kafka is a distributed streaming platform that enables building real-time data pipelines and streaming applications. It is designed for high-throughput, fault-tolerant, and scalable data streaming. Here's a comprehensive overview of the Apache Kafka framework:

1. Core Concepts:

   a. Topics:
      - Logical channels for publishing and subscribing to data streams.
      - Partitioned for parallelism and scalability.
      - Retain messages for a configurable period.

   b. Producers:
      - Applications that publish (write) data to Kafka topics.
      - Can choose which partition to send messages to.

   c. Consumers:
      - Applications that subscribe to (read) data from Kafka topics.
      - Can be part of consumer groups for load balancing.

   d. Brokers:
      - Servers that store and manage topics.
      - Form a Kafka cluster when multiple brokers are used.

   e. ZooKeeper:
      - Manages and coordinates the Kafka cluster.
      - Stores metadata about the cluster, topics, and partitions.

2. Architecture:

   a. Distributed System:
      - Horizontally scalable across multiple nodes.
      - Supports replication for fault tolerance.

   b. Partitions:
      - Topics are divided into partitions for parallel processing.
      - Each partition is an ordered, immutable sequence of records.

   c. Replication:
      - Partitions can be replicated across multiple brokers.
      - Ensures data durability and high availability.

   d. Leader-Follower Model:
      - One broker is the leader for a partition, handling all reads and writes.
      - Other brokers are followers, replicating data for fault tolerance.

3. Key Features:

   a. High Throughput:
      - Capable of handling millions of messages per second.
      - Optimized for batching and compression.

   b. Low Latency:
      - Can achieve end-to-end latencies as low as 2ms.

   c. Durability:
      - Data is persisted on disk and replicated within the cluster.

   d. Scalability:
      - Easily scale out by adding more brokers to the cluster.

   e. Fault Tolerance:
      - Replication ensures data availability even if brokers fail.

   f. Exactly-Once Semantics:
      - Guarantees that each message is processed once and only once.

4. Use Cases:

   a. Messaging System:
      - Decoupling of data streams between systems or applications.

   b. Activity Tracking:
      - Real-time monitoring and analytics of user activities.

   c. Metrics and Logging:
      - Centralized collection of operational data and logs.

   d. Stream Processing:
      - Real-time data transformation and analysis.

   e. Event Sourcing:
      - Storing and replaying events for application state.

   f. Commit Log:
      - Distributed systems can use Kafka as a commit log service.

5. Kafka Streams:

   a. Client Library:
      - For building stream processing applications.

   b. Stateful and Stateless Processing:
      - Supports both types of stream processing.

   c. Exactly-Once Processing:
      - Ensures accurate results in stream processing.

   d. One-Record-at-a-Time Processing:
      - Low latency processing model.

6. Kafka Connect:

   a. Data Integration Framework:
      - Standardized way to integrate Kafka with other systems.

   b. Source Connectors:
      - Import data from external systems into Kafka.

   c. Sink Connectors:
      - Export data from Kafka to external systems.

   d. Distributed and Scalable:
      - Can run on a single worker or scaled to a cluster.

7. Security Features:

   a. Authentication:
      - SSL/TLS, SASL, and Kerberos support.

   b. Authorization:
      - ACL-based security for topics and consumer groups.

   c. Encryption:
      - SSL/TLS for in-transit encryption.

8. Monitoring and Management:

   a. JMX Metrics:
      - Extensive metrics exposed via JMX.

   b. Kafka Manager:
      - Web-based tool for managing Kafka clusters.

   c. Confluent Control Center:
      - Advanced monitoring and management UI (commercial).

9. Ecosystem:

   a. Client Libraries:
      - Available for multiple programming languages.

   b. Schema Registry:
      - Manages schemas for data serialization.

   c. REST Proxy:
      - HTTP interface to Kafka cluster.

   d. KSQL:
      - SQL-like stream processing language for Kafka.

10. Important Kafka Methods and Topics:

    a. Producer Methods:
       - send(): Asynchronously send a record to a topic.
       - flush(): Wait for all asynchronous send requests to complete.
       - close(): Close the producer and wait for all requests to complete.
       - partitionsFor(): Get metadata about the partitions for a given topic.
       - metrics(): Get metrics about the producer.

    b. Consumer Methods:
       - subscribe(): Subscribe to a list of topics.
       - poll(): Fetch data for the subscribed topics.
       - commit(): Commit offsets returned on the last poll for all subscribed topics.
       - seek(): Seek to a specific offset for a partition.
       - close(): Close the consumer.
       - pause(): Suspend fetching from the requested partitions.
       - resume(): Resume fetching from the requested partitions.
       - assignment(): Get the set of partitions currently assigned to this consumer.
       - position(): Get the offset of the next record that will be fetched.
       - committed(): Get the last committed offset for the given partition.

    c. Admin Client Methods:
       - create_topics(): Create new topics.
       - delete_topics(): Delete existing topics.
       - list_topics(): List all available topics.
       - describe_configs(): Get the configuration of topics or brokers.
       - alter_configs(): Alter the configuration of topics or brokers.
       - create_partitions(): Create additional partitions for a topic.
       - describe_cluster(): Get information about the Kafka cluster.
       - list_consumer_groups(): List all consumer groups.
       - describe_consumer_groups(): Get detailed information about consumer groups.
       - list_acls(): List ACLs for a resource.
       - create_acls(): Create new ACLs.
       - delete_acls(): Delete ACLs.

    d. Kafka Streams Methods:
       - stream(): Create a KStream from a topic.
       - table(): Create a KTable from a topic.
       - to(): Write the records to a topic.
       - filter(): Filter records based on a predicate.
       - map(): Transform each record.
       - flatMap(): Transform each record into zero or more records.
       - join(): Join two streams or tables.
       - groupBy(): Group the records by a key.
       - count(): Count the number of records.
       - reduce(): Combine the values for a key.
       - aggregate(): Aggregate the values for a key.
       - through(): Materialize a stream to a topic and create a new stream.
       - branch(): Split a stream into multiple streams based on predicates.
       - merge(): Merge multiple streams into a single stream.
       - peek(): Perform a stateless operation on each record.
       - selectKey(): Assign a new key to each record.
       - transform(): Apply a stateful transformation to the stream.
       - process(): Process records with a custom processor.

    e. Important Kafka Topics:
       - __consumer_offsets: Internal topic for storing consumer group offsets.
       - __transaction_state: Internal topic for storing transaction metadata.
       - _schemas: Used by Schema Registry to store schema information.
       - connect-configs: Stores connector and task configurations for Kafka Connect.
       - connect-offsets: Stores connector offsets for Kafka Connect.
       - connect-status: Stores status updates of connectors and tasks for Kafka Connect.
       - _confluent-metrics: Used by Confluent Control Center for metrics collection.
       - _confluent-command: Used by Confluent Control Center for cluster management.
       - __confluent.support.metrics: Used for Confluent support and telemetry.
       - _confluent-controlcenter-<group>-alerts: Stores alerts for Confluent Control Center.
       - _confluent-controlcenter-<group>-command_topic: Used for Confluent Control Center commands.
       - _confluent-monitoring: Used for monitoring data in Confluent Platform.
       - _confluent-ksql-<ksql.service.id>_command_topic: KSQL command topic.
       - _confluent-ksql-<ksql.service.id>_ksql_processing_log: KSQL processing log topic.

11. Advanced Kafka Concepts:

    a. Transactions:
       - Allows for atomic writes across multiple partitions.
       - Ensures exactly-once semantics in stream processing.

    b. Idempotent Producer:
       - Prevents duplicate messages in case of network errors or broker failures.

    c. Compacted Topics:
       - Retain only the latest value for each key in a topic.

    d. Quotas and Throttling:
       - Limit the bandwidth or request rate for clients to prevent overload.

    e. Multi-tenancy:
       - Ability to run multiple independent Kafka clusters on the same hardware.

    f. Rack Awareness:
       - Distribute replicas across different racks or availability zones for improved fault tolerance.

    g. Mirror Maker:
       - Tool for mirroring data between Kafka clusters.

    h. Cruise Control:
       - Automated cluster balancing and healing tool.

    i. Tiered Storage:
       - Ability to offload older data to cheaper storage while maintaining accessibility.

    j. Exactly-Once Stream Processing:
       - Guarantees that each record is processed once and only once, even in the presence of failures.

    k. Incremental Cooperative Rebalancing:
       - Allows for smoother consumer group rebalances without stopping all consumers.

    l. Kafka Connect Transforms:
       - Simple message transformations that can be applied to data in Kafka Connect pipelines.

    m. Kafka Streams Interactive Queries:
       - Allows querying the state of a Kafka Streams application from outside the application.

    n. SASL/OAUTHBEARER Authentication:
       - Supports OAuth 2.0 for authentication in Kafka.

    o. Delegation Tokens:
       - Short-lived authentication tokens for Kafka clients.

    p. Kafka Improvement Proposals (KIPs):
       - Process for proposing, discussing, and implementing changes to Kafka.

Apache Kafka's robust architecture, high performance, and extensive ecosystem make it a popular choice for building real-time data pipelines and streaming applications across various industries and use cases.
"""

from kafka import KafkaProducer, KafkaConsumer, KafkaAdminClient
from kafka.admin import NewTopic, ConfigResource, ConfigResourceType
from kafka.errors import TopicAlreadyExistsError
import json

# Producer Example
def kafka_producer():
    producer = KafkaProducer(
        bootstrap_servers=['localhost:9092'],
        value_serializer=lambda v: json.dumps(v).encode('utf-8'),
        acks='all',  # Wait for all in-sync replicas to acknowledge the message
        retries=3,   # Retry sending the message up to 3 times
        linger_ms=10 # Wait up to 10ms to batch messages
    )
    
    for i in range(10):
        message = {'number': i}
        future = producer.send('test-topic', value=message)
        # Block until the message is sent (or fails)
        try:
            record_metadata = future.get(timeout=10)
            print(f"Produced: {message} to {record_metadata.topic}:{record_metadata.partition}:{record_metadata.offset}")
        except Exception as e:
            print(f"Error producing message: {e}")
    
    producer.flush()
    producer.close()

# Consumer Example
def kafka_consumer():
    consumer = KafkaConsumer(
        'test-topic',
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group',
        value_deserializer=lambda x: json.loads(x.decode('utf-8')),
        max_poll_records=100,  # Maximum number of records returned in a single call to poll()
        session_timeout_ms=30000,  # The timeout used to detect consumer failures
        heartbeat_interval_ms=3000  # The expected time between heartbeats to the consumer coordinator
    )
    
    try:
        for message in consumer:
            print(f"Consumed: {message.value} from {message.topic}:{message.partition}:{message.offset}")
            
            # Manually commit offsets if enable_auto_commit is False
            # consumer.commit()
    except KeyboardInterrupt:
        print("Stopping consumer...")
    finally:
        consumer.close()

# Admin Client Example
def kafka_admin():
    admin_client = KafkaAdminClient(
        bootstrap_servers=['localhost:9092'],
        client_id='my-admin-client'
    )

    # Create a new topic
    new_topic = NewTopic(name="new-topic", num_partitions=3, replication_factor=1)
    try:
        admin_client.create_topics([new_topic])
        print(f"Topic '{new_topic.name}' created successfully")
    except TopicAlreadyExistsError:
        print(f"Topic '{new_topic.name}' already exists")

    # List topics
    topics = admin_client.list_topics()
    print(f"Available topics: {topics}")

    # Describe topic configuration
    config_resource = ConfigResource(ConfigResourceType.TOPIC, "new-topic")
    configs = admin_client.describe_configs([config_resource])
    for resource, config_entries in configs.items():
        print(f"Configuration for {resource}:")
        for config_name, config_entry in config_entries.items():
            print(f"  {config_name}: {config_entry.value}")

    # Alter topic configuration
    new_config = {
        "retention.ms": "86400000"  # Set retention to 24 hours
    }
    config_resource.set_config(new_config)
    admin_client.alter_configs([config_resource])
    print(f"Updated configuration for topic 'new-topic'")

    # Create partitions
    topic_partitions = {
        "new-topic": NewPartitions(total_count=6)
    }
    admin_client.create_partitions(topic_partitions)
    print(f"Increased partitions for 'new-topic' to 6")

    # List consumer groups
    consumer_groups = admin_client.list_consumer_groups()
    print(f"Consumer groups: {consumer_groups}")

    # Describe consumer groups
    group_details = admin_client.describe_consumer_groups(["my-group"])
    for group, details in group_details.items():
        print(f"Details for consumer group '{group}':")
        print(f"  State: {details.state}")
        print(f"  Members: {len(details.members)}")

    # Delete a topic
    try:
        admin_client.delete_topics(["topic-to-delete"])
        print("Topic 'topic-to-delete' deleted successfully")
    except Exception as e:
        print(f"Error deleting topic: {e}")

    admin_client.close()

# Run producer, consumer, and admin examples
if __name__ == "__main__":
    print("Running Kafka Admin Client...")
    kafka_admin()

    print("\nRunning Kafka Producer...")
    kafka_producer()
    
    print("\nRunning Kafka Consumer...")
    kafka_consumer()
