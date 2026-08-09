"""
silver_event.py

Silver Event model for the Smart Manufacturing Intelligence Platform (SMIP).

Represents a validated and standardized manufacturing event.

Author:
Sumanth Vempalle

Version:
2.0.0
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime


@dataclass(slots=True)
class SilverEvent:
    """
    Standardized event stored in the Silver layer.
    """

    event: dict

    bronze_ingestion_timestamp: datetime

    silver_processing_timestamp: datetime

    def to_dict(self) -> dict:

        return {

            "bronze_ingestion_timestamp":
                self.bronze_ingestion_timestamp.isoformat(),

            "silver_processing_timestamp":
                self.silver_processing_timestamp.isoformat(),

            "event":
                self.event,

        }

    @classmethod
    def from_bronze_event(
        cls,
        bronze_event,
    ) -> "SilverEvent":

        return cls(

            event=bronze_event.event,

            bronze_ingestion_timestamp=
                bronze_event.ingestion_timestamp,

            silver_processing_timestamp=
                datetime.now(UTC),

        )