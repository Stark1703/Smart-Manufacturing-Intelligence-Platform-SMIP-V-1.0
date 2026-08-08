"""
bronze_storage.py

Storage backend for the Bronze layer of the
Smart Manufacturing Intelligence Platform (SMIP).

Responsible for persisting Bronze Events.

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
from pathlib import Path

from streaming.bronze.bronze_event import BronzeEvent


logger = logging.getLogger(__name__)


class BronzeStorage:
    """
    Physical storage layer for Bronze events.
    """

    def __init__(
        self,
        output_directory: str = "data/bronze",
        filename: str = "manufacturing_events.jsonl",
    ) -> None:

        self.output_directory = Path(output_directory)

        self.output_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        self.file_path = self.output_directory / filename

    # ============================================================
    # Write Event
    # ============================================================

    def write(
        self,
        event: BronzeEvent,
    ) -> None:
        """
        Persist one Bronze Event.
        """

        with self.file_path.open(
            "a",
            encoding="utf-8",
        ) as file:

            json.dump(
                event.to_dict(),
                file,
                default=str,
            )

            file.write("\n")

    # ============================================================
    # Utilities
    # ============================================================

    @property
    def path(self) -> Path:
        """
        Return storage file path.
        """

        return self.file_path