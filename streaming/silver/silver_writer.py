"""
silver_writer.py

Silver Writer for the Smart Manufacturing Intelligence Platform (SMIP).

Responsible for persisting Silver Events using the Silver Storage layer.

Author:
Sumanth Vempalle

Version:
2.0.0
"""

from __future__ import annotations

import logging

from streaming.silver.silver_event import SilverEvent
from streaming.silver.silver_storage import SilverStorage

logger = logging.getLogger(__name__)


class SilverWriter:
    """
    Writes Silver Events to persistent storage.
    """

    def __init__(
        self,
        storage: SilverStorage | None = None,
    ) -> None:

        self.storage = storage or SilverStorage()

    # ============================================================
    # Write Event
    # ============================================================

    def write_event(
        self,
        event: SilverEvent,
    ) -> None:
        """
        Persist one Silver Event.
        """

        self.storage.write(event)

        logger.info(
            "Silver Event stored: %s",
            event.event["event_id"],
        )

    # ============================================================
    # Storage Path
    # ============================================================

    @property
    def path(self):

        return self.storage.path