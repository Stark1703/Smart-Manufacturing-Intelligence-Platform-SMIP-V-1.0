from streaming.bronze.bronze_reader import BronzeReader

reader = BronzeReader()

print("Bronze file:", reader.path)
print("Total events:", reader.count())
print()

for bronze_event in reader.read():

    print("Kafka Topic      :", bronze_event.kafka_topic)
    print("Partition        :", bronze_event.kafka_partition)
    print("Offset           :", bronze_event.kafka_offset)
    print("Ingestion Time   :", bronze_event.ingestion_timestamp)

    print("Event ID         :", bronze_event.event["event_id"])
    print("Event Type       :", bronze_event.event["event_type"])

    print("-" * 80)