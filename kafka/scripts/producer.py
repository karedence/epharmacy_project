from confluent_kafka import Producer
import json

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def send_update(update_data):
    producer.send('epharmacy_updates', update_data)
    producer.flush()  # Ensure the message is sent
