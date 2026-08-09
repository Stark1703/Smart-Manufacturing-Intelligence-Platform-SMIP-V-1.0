"""
silver_reader.py

Reader for the Silver layer.

Reads validated and transformed manufacturing events stored
in JSONL format.

Author:
Sumanth Vempalle

Version:
2.0.0
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Iterator


class SilverReader:
    """
    Reads Silver Events from storage.
    """

    def __init__(self, path: str | Path):

        self.path = Path(path)

    # ============================================================
    # Read Events
    # ============================================================

    def read_events(self) -> Iterator[dict]:
        """
        Iterate through all Silver events.

        Yields
        ------
        dict
            One Silver Event.
        """

        if not self.path.exists():
            return

        with self.path.open(
            "r",
            encoding="utf-8",
        ) as file:

            for line in file:

                line = line.strip()

                if not line:
                    continue

                yield json.loads(line)

    # ============================================================
    # Read All
    # ============================================================

    def read_all(self) -> list[dict]:
        """
        Return all Silver Events.
        """

        return list(self.read_events())

    # ============================================================
    # Count
    # ============================================================

    def count(self) -> int:
        """
        Number of events stored.
        """

        return sum(1 for _ in self.read_events())