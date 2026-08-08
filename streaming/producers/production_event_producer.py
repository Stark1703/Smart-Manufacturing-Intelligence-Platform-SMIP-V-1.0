"""Producer utilities for manufacturing events."""

from typing import List

from streaming.events.manufacturing_event import ManufacturingEvent


class ProductionEventProducer:
    """Simple producer that emits manufacturing events."""

    def __init__(self, source: str = "simulator"):
        self.source = source

    def produce(self, event_type: str, payload: dict) -> ManufacturingEvent:
        """Create a manufacturing event instance."""
        return ManufacturingEvent(event_type=event_type, source=self.source, payload=payload)

    def produce_many(self, events: List[tuple]) -> List[ManufacturingEvent]:
        """Create multiple events from a list of tuples."""
        return [self.produce(event_type, payload) for event_type, payload in events]
