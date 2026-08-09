from streaming.bronze.bronze_reader import BronzeReader
from streaming.silver.silver_transformer import SilverTransformer

reader = BronzeReader()
transformer = SilverTransformer()

for bronze_event in reader.read():

    silver_event = transformer.transform(bronze_event)

    print("Event ID :", silver_event.event["event_id"])
    print("Machine  :", silver_event.event["machine_id"])
    print("Payload  :", silver_event.event["payload"])
    print("-" * 80)