"""
bronze_writer.py

Bronze Layer Writer for the Smart Manufacturing Intelligence Platform (SMIP).

Responsible for persisting Bronze Events.

Author:
Sumanth Vempalle

Version:
2.0.0
"""

from __future__ import annotations

import json
import logging
from pathlib import Path

from streaming.bronze.bronze_event import BronzeEvent

logger = logging.getLogger(__name__)


class BronzeWriter:
    """
    Writes Bronze Events to the Bronze layer.

    Currently stores events as JSON Lines (.jsonl).

    Future versions will support:

    - Delta Lake
    - Apache Parquet
    - Azure Data Lake
    """

    def __init__(
        self,
        output_directory: str = "data/bronze",
        file_name: str = "manufacturing_events.jsonl",
    ) -> None:

        self.output_directory = Path(output_directory)

        self.output_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        self.output_file = (
            self.output_directory / file_name
        )

    # ============================================================
    # Write Event
    # ============================================================

    def write(
        self,
        bronze_event: BronzeEvent,
    ) -> None:
        """
        Append one Bronze Event to the Bronze layer.
        """

        with self.output_file.open(
            "a",
            encoding="utf-8",
        ) as file:

            json.dump(
                {
                    "kafka_topic":
                        bronze_event.kafka_topic,

                    "kafka_partition":
                        bronze_event.kafka_partition,

                    "kafka_offset":
                        bronze_event.kafka_offset,

                    "ingestion_timestamp":
                        bronze_event.ingestion_timestamp.isoformat(),

                    "event":
                        bronze_event.event,
                },
                file,
                default=str,
            )

            file.write("\n")

        logger.debug(
            "Bronze event written (offset=%d)",
            bronze_event.kafka_offset,
        )