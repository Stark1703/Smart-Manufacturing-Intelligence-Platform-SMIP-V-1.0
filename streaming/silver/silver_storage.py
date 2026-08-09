"""
silver_storage.py

Storage backend for the Silver layer of the
Smart Manufacturing Intelligence Platform (SMIP).

Responsible for persisting validated Silver Events.

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

from streaming.silver.silver_event import SilverEvent

logger = logging.getLogger(__name__)


class SilverStorage:
    """
    Physical storage layer for Silver Events.
    """

    def __init__(
        self,
        output_directory: str = "data/silver",
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
        event: SilverEvent,
    ) -> None:
        """
        Persist one Silver Event.
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
    # Storage Path
    # ============================================================

    @property
    def path(self) -> Path:
        """
        Return storage file path.
        """

        return self.file_path