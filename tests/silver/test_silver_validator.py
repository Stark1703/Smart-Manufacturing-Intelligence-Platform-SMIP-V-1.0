from streaming.bronze.bronze_reader import BronzeReader
from streaming.silver.silver_validator import SilverValidator

reader = BronzeReader()

validator = SilverValidator()

for bronze_event in reader.read():

    valid = validator.validate(bronze_event)

    print(bronze_event.event["event_id"])

    print("Valid :", valid)

    print("Errors:", validator.errors)

    print("-" * 80)