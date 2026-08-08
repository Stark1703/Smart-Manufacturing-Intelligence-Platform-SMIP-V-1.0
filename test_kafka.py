from datetime import datetime, UTC

event_timestamp=datetime.now(UTC)

from streaming.events.event_types import EventType
from streaming.events.manufacturing_event import ManufacturingEvent
from streaming.kafka.producer import ManufacturingKafkaProducer
from streaming.kafka.topics import MANUFACTURING_EVENTS_TOPIC

producer = ManufacturingKafkaProducer()

event = ManufacturingEvent(
    event_id="TEST-001",
    event_type=EventType.OPERATION_COMPLETED,
    event_timestamp=datetime.utcnow(),
    payload={
        "machine_id": "MCH-001",
        "force": 21.7,
    },
)

producer.send(
    MANUFACTURING_EVENTS_TOPIC,
    event,
)

producer.flush()

print("Event sent successfully.")