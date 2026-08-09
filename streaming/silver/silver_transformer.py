"""
silver_transformer.py

Silver Transformer for the Smart Manufacturing Intelligence Platform (SMIP).

Transforms validated Bronze Events into standardized Silver Events.

Author:
Sumanth Vempalle

Version:
2.0.0
"""

from __future__ import annotations

from copy import deepcopy

from streaming.bronze.bronze_event import BronzeEvent
from streaming.silver.silver_event import SilverEvent


class SilverTransformer:
    """
    Transforms Bronze Events into Silver Events.
    """

    # ============================================================
    # Transform
    # ============================================================

    def transform(
        self,
        bronze_event: BronzeEvent,
    ) -> SilverEvent:
        """
        Transform one Bronze Event into a Silver Event.
        """

        event = deepcopy(bronze_event.event)

        self._normalize_strings(event)

        self._normalize_empty_values(event)

        return SilverEvent.from_bronze_event(
            bronze_event=BronzeEvent(
                kafka_topic=bronze_event.kafka_topic,
                kafka_partition=bronze_event.kafka_partition,
                kafka_offset=bronze_event.kafka_offset,
                ingestion_timestamp=bronze_event.ingestion_timestamp,
                event=event,
            )
        )

    # ============================================================
    # Normalize Strings
    # ============================================================

    def _normalize_strings(
        self,
        obj,
    ) -> None:
        """
        Strip leading/trailing whitespace from all strings.
        """

        if isinstance(obj, dict):

            for key, value in obj.items():

                if isinstance(value, str):

                    obj[key] = value.strip()

                elif isinstance(value, (dict, list)):

                    self._normalize_strings(value)

        elif isinstance(obj, list):

            for item in obj:

                self._normalize_strings(item)

    # ============================================================
    # Normalize Empty Values
    # ============================================================

    def _normalize_empty_values(
        self,
        obj,
    ) -> None:
        """
        Convert empty strings to None recursively.
        """

        if isinstance(obj, dict):

            for key, value in obj.items():

                if value == "":

                    obj[key] = None

                elif isinstance(value, (dict, list)):

                    self._normalize_empty_values(value)

        elif isinstance(obj, list):

            for item in obj:

                self._normalize_empty_values(item)