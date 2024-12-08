from confluent_kafka import consumer
import json

consumer = KafkaConsumer(
    'epharmacy_updates',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)

def consume_updates():
    for message in consumer:
        print(f"Received update: {message.value}")
