from streaming.kafka.consumer import ManufacturingKafkaConsumer
from streaming.kafka.topics import MANUFACTURING_EVENTS_TOPIC

consumer = ManufacturingKafkaConsumer()

consumer.subscribe(MANUFACTURING_EVENTS_TOPIC)

print("Waiting for messages...\n")

while True:

    msg = consumer.poll()

    if msg is None:
        continue

    if msg.error():
        print(msg.error())
        continue

    print("Topic :", msg.topic())
    print("Key   :", msg.key().decode())
    print("Value :", msg.value().decode())
    print("-" * 80)