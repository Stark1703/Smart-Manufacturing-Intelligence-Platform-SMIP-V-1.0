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
        input_directory: str = "data/bronze",
        filename: str = "manufacturing_events.jsonl",
    ) -> None:

        self.file_path = Path(input_directory) / filename

    # ============================================================
    # Read Events
    # ============================================================

    def read(self) -> Iterator[dict]:
        """
        Yield Bronze Events one at a time.
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

                if line.strip():

                    yield json.loads(line)

    # ============================================================
    # Count Events
    # ============================================================

    def count(self) -> int:
        """
        Return number of Bronze Events.
        """

        if not self.file_path.exists():

            return 0

        with self.file_path.open(
            "r",
            encoding="utf-8",
        ) as file:

            return sum(
                1
                for line in file
                if line.strip()
            )

    # ============================================================
    # Storage Path
    # ============================================================

    @property
    def path(self) -> Path:
        """
        Return Bronze storage path.
        """

        return self.file_path