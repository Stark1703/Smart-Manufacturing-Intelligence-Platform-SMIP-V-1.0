from streaming.bronze.bronze_reader import BronzeReader
from streaming.silver.silver_transformer import SilverTransformer
from streaming.silver.silver_writer import SilverWriter

reader = BronzeReader()
transformer = SilverTransformer()
writer = SilverWriter()

for bronze_event in reader.read():

    silver_event = transformer.transform(bronze_event)

    writer.write(silver_event)

print("Finished writing Silver Events.")
print("Output:", writer.path)