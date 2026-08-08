"""Simple entry point for running a streaming simulation."""

from streaming.events.event_types import PRODUCTION_COMPLETED, PRODUCTION_STARTED
from streaming.producers.production_event_producer import ProductionEventProducer
from streaming.utils.json_writer import write_json


def run_simulation(output_path: str = "streaming_output.json") -> None:
    """Generate a small set of sample manufacturing events."""
    producer = ProductionEventProducer()
    events = producer.produce_many(
        [
            (PRODUCTION_STARTED, {"line_id": "L01", "order_id": "O1001"}),
            (PRODUCTION_COMPLETED, {"line_id": "L01", "order_id": "O1001", "units": 120}),
        ]
    )

    write_json(output_path, {"events": [event.to_dict() for event in events]})


if __name__ == "__main__":
    run_simulation()
