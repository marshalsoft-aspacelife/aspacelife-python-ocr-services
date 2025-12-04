# ============================================================================
# KafkaProducer Class
# ============================================================================
from quixstreams import Application
import json
import time

# Configuration
# The name of the topic you want to broadcast to

class KafakMessageBrokerService:
    def __init__(self):
        """Initializes and returns a KafkaProducer instance."""
        KAFKA_BROKERS = ['localhost:9092']  # Replace with your Kafka broker addresses
        KAFKA_TOPIC = 'my_topic'        
        producer = self.create()

    @classmethod
    def create(cls):
        try:
            producer = Application(
                broker_address='localhost:9092',
                loglevel='DEBUG'
            )
            print("Kafka Producer initialized successfully.")
            return producer
        except Exception as e:
            print(f"Error initializing Kafka Producer: {e}")
        return None
    
    def broadcast(self, message):
        """Sends a single message to the specified Kafka topic."""
        try:
            # Use .send() method to broadcast
            self.producer.produce(
                topic="ocr_results", 
                key="d",
                value=json.dumps(message).encode('utf-8')
            )
            self.producer.flush()
            print(f"Message sent successfully!")

        except Exception as e:
            print(f"Error sending message: {e}")
