"""
bronze_writer.py

Bronze Writer for the Smart Manufacturing Intelligence Platform (SMIP).

Responsible for converting Manufacturing Events into Bronze Events
and delegating persistence to the Bronze Storage layer.

Author:
Sumanth Vempalle

Version:
2.0.0
"""

from __future__ import annotations

import logging
from datetime import datetime, UTC

from streaming.events.manufacturing_event import ManufacturingEvent

from .bronze_event import BronzeEvent
from .bronze_storage import BronzeStorage

logger = logging.getLogger(__name__)


class BronzeWriter:
    """
    Converts Manufacturing Events into Bronze Events and stores them.
    """

    def __init__(self) -> None:

        self.storage = BronzeStorage()

    # ============================================================
    # Write Event
    # ============================================================

    def write(
        self,
        event: ManufacturingEvent,
    ) -> BronzeEvent:
        """
        Convert a ManufacturingEvent into a BronzeEvent and persist it.
        """

        bronze_event = BronzeEvent(

            ingestion_timestamp=datetime.now(UTC),

            source="kafka",

            manufacturing_event=event,

        )

        self.storage.write(bronze_event)

        logger.info(
            "Bronze Event stored: %s",
            bronze_event.manufacturing_event.event_id,
        )

        return bronze_event