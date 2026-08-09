"""
bronze_reader.py

Bronze Reader for the Smart Manufacturing Intelligence Platform (SMIP).

Responsible for reading Bronze Events from storage.

Current implementation:
    • JSON Lines (.jsonl)

Future implementations:
    • Delta Lake
    • Apache Parquet
    • Azure Data Lake
    • Amazon S3

Author:
Sumanth Vempalle

Version:
2.0.0
"""

from __future__ import annotations

import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Iterator

from streaming.bronze.bronze_event import BronzeEvent

logger = logging.getLogger(__name__)


class BronzeReader:
    """
    Reads Bronze Events from storage.
    """

    def __init__(
        self,
        path: str | Path = "data/bronze/manufacturing_events.jsonl",
    ) -> None:

        self.file_path = Path(path)

    # ============================================================
    # Read Events
    # ============================================================

    def read_events(self) -> Iterator[BronzeEvent]:
        """
        Iterate over Bronze Events.
        """

        if not self.file_path.exists():

            logger.warning(
                "Bronze storage does not exist: %s",
                self.file_path,
            )

            return

        with self.file_path.open(
            "r",
            encoding="utf-8",
        ) as file:

            for line in file:

                line = line.strip()

                if not line:
                    continue

                data = json.loads(line)

                yield BronzeEvent(

                    kafka_topic=data["kafka_topic"],

                    kafka_partition=data["kafka_partition"],

                    kafka_offset=data["kafka_offset"],

                    ingestion_timestamp=datetime.fromisoformat(
                        data["ingestion_timestamp"]
                    ),

                    event=data["event"],

                )

    # ============================================================
    # Backwards Compatibility
    # ============================================================

    def read(self) -> Iterator[BronzeEvent]:
        """
        Alias kept for backwards compatibility.
        """

        return self.read_events()

    # ============================================================
    # Read All
    # ============================================================

    def read_all(self) -> list[BronzeEvent]:
        """
        Return all Bronze Events.
        """

        return list(self.read_events())

    # ============================================================
    # Count
    # ============================================================

    def count(self) -> int:
        """
        Return number of Bronze Events.
        """

        return sum(1 for _ in self.read_events())

    # ============================================================
    # Storage Path
    # ============================================================

    @property
    def path(self) -> Path:
        """
        Bronze storage path.
        """

        return self.file_path