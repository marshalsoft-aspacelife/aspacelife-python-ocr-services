import os
import json
import time
from quixstreams import Application

class QuixstreamsMessageSender:
    """Class for sending messages to a Kafka topic using Quixstreams."""

    def __init__(self, kafka_brokers=None, topic_name=None):
        """Initialize the Quixstreams message sender.

        Args:
            kafka_brokers (str, optional): Comma-separated list of Kafka broker addresses.
                                           Defaults to KAFKA_BROKERS_URL environment variable or 'localhost:9092'.
            topic_name (str, optional): The name of the Kafka topic to send messages to.
                                        Defaults to KAFKA_OUTPUT_TOPIC environment variable or 'my-output-topic'.
        """
        self.kafka_brokers = kafka_brokers or os.environ.get("KAFKA_BROKERS_URL", "localhost:9092")
        self.topic_name = topic_name or os.environ.get("KAFKA_OUTPUT_TOPIC", "my-output-topic")

        # Initialize Quixstreams Application without consumer_group_id here
        self.app = Application(broker_address=self.kafka_brokers)

        # Define the topic for producing messages
        self.output_topic = self.app.topic(self.topic_name, value_serializer='json')
        self.producer = None # Will be initialized when send_message is called or in __enter__
        print(f"QuixstreamsMessageSender initialized for topic: {self.topic_name} on brokers: {self.kafka_brokers}")

    def _get_producer(self):
        """Get or create the Quixstreams producer instance."""
        if self.producer is None:
            self.producer = self.app.get_producer()
        return self.producer

    def send_message(self, message):
        """Send a message to the configured Kafka topic.

        Args:
            message (dict): The message payload (will be serialized to JSON).
            key (str, optional): The message key. Defaults to None.
        """
        print(f"Produced message to {self.topic_name}: key=, value={json.dumps(message)}")
        try:
            producer_instance = self._get_producer()
            producer_instance.produce(topic=self.output_topic.name, key="key", value=message)
            print(f"Produced message to {self.topic_name}: key={"key"}, value={json.dumps(message)}")
        except Exception as e:
            print(f"Error sending message: QuixstreamsMessageSender {e}")
            raise

    def flush_and_close(self):
        """Flush any pending messages and close the producer connection."""
        if self.producer:
            try:
                self.producer.flush()
                self.producer = None # Reset producer after closing
                print("Quixstreams producer flushed and closed successfully.")
            except Exception as e:
                print(f"Error flushing or closing Quixstreams producer: {e}")

    def __enter__(self):
        """Context manager entry. Initializes the producer."""
        self._get_producer()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit. Ensures producer is flushed and closed."""
        self.flush_and_close()

