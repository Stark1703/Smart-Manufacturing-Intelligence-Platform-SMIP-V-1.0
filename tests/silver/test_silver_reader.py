from streaming.silver.silver_reader import SilverReader

reader = SilverReader(
    "data/silver/manufacturing_events.jsonl"
)

print("Silver file:", reader.path)
print("Total events:", reader.count())
print()

for event in reader.read_events():

    print(event)