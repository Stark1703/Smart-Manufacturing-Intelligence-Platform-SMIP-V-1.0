"""
bronze_event.py

Bronze Event model for SMIP.

Represents a raw manufacturing event as received from Kafka.

Author:
Sumanth Vempalle

Version:
2.0.0
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime


@dataclass(slots=True)
class BronzeEvent:

    kafka_topic: str

    kafka_partition: int

    kafka_offset: int

    ingestion_timestamp: datetime

    event: dict

    @classmethod
    def from_kafka_message(
        cls,
        *,
        topic: str,
        partition: int,
        offset: int,
        event: dict,
    ) -> "BronzeEvent":

        return cls(
            kafka_topic=topic,
            kafka_partition=partition,
            kafka_offset=offset,
            ingestion_timestamp=datetime.now(UTC),
            event=event,
        )

    def to_dict(self) -> dict:

        return {
            "kafka_topic": self.kafka_topic,
            "kafka_partition": self.kafka_partition,
            "kafka_offset": self.kafka_offset,
            "ingestion_timestamp": self.ingestion_timestamp.isoformat(),
            "event": self.event,
        }