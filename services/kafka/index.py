# ============================================================================
# KafkaProducer Class
# ============================================================================
from kafka import KafkaProducer
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
            producer = KafkaProducer(
            # List of Kafka broker addresses
            bootstrap_servers=cls.KAFKA_BROKERS,
            
            # Function to serialize the message value to bytes (e.g., JSON)
            value_serializer=lambda v: json.dumps(v).encode('utf-8'),
            
            # Optional: Wait up to 1 second for metadata if brokers are down
            api_version=(0, 10, 1) 
            )
            print("Kafka Producer initialized successfully.")
            return producer
        except Exception as e:
            print(f"Error initializing Kafka Producer: {e}")
        return None
    
    @classmethod
    def broadcast(cls,message):
        """Sends a single message to the specified Kafka topic."""
        try:
            # Use .send() method to broadcast
            future = cls.producer.send(
                topic=cls.KAFKA_TOPIC, 
                value=message
                # Optional: Specify a key for partition assignment
                # key=str(message['id']).encode('utf-8') 
            )
            
            # Block until the message is sent (optional, but useful for confirmation)
            record_metadata = future.get(timeout=10)
            
            print(f"Message sent successfully!")
            print(f"  Topic: {record_metadata.topic}")
            print(f"  Partition: {record_metadata.partition}")
            print(f"  Offset: {record_metadata.offset}")

        except Exception as e:
            print(f"Error sending message: {e}")

# if __name__ == '__main__':
#     producer = create_producer()
    
#     if producer:
#         # Example data to broadcast
#         data = {
#             'timestamp': time.time(),
#             'event': 'user_logged_in',
#             'user_id': 1001,
#             'source': 'python_app'
#         }
        
#         print(f"\nAttempting to broadcast data: {data}")
#         broadcast_message(producer, data)

#         # Ensure all buffered messages are sent before closing
#         producer.flush()
#         producer.close()
#         print("\nProducer closed.")