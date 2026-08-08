from streaming.bronze.bronze_reader import BronzeReader

reader = BronzeReader()

print("Bronze file:", reader.path)
print("Total events:", reader.count())

print()

for event in reader.read():
    print(event["manufacturing_event"]["event_id"])