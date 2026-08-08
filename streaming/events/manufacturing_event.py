"""
manufacturing_event.py

Manufacturing Event model for the Smart Manufacturing Intelligence Platform (SMIP).

This module defines the canonical event structure used by the
real-time streaming simulator.

Author:
Sumanth Vempalle + ChatGPT

Version:
2.0.0
"""

from __future__ import annotations

from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from enum import Enum
from typing import Any
from uuid import uuid4

from streaming.events.event_types import EventType


@dataclass(slots=True)
class ManufacturingEvent:
    """
    Canonical manufacturing event.

    Every manufacturing activity emitted by the streaming simulator
    uses this event structure.

    Event-specific attributes are stored in the payload dictionary.
    """

    # ============================================================
    # Event Metadata
    # ============================================================

    event_id: str = field(
        default_factory=lambda: f"EVT-{uuid4().hex[:12].upper()}"
    )

    event_timestamp: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    event_type: EventType = EventType.PRESS_OPERATION

    event_version: str = "2.0"

    # ============================================================
    # Manufacturing Context
    # ============================================================

    plant_code: str = "PLANT-001"

    hall_id: str = ""

    line_id: str = ""

    machine_id: str = ""

    execution_id: str = ""

    work_order_id: str = ""

    serial_number: str = ""

    operator_id: str = ""

    product_code: str = ""

    source_system: str = ""

    correlation_id: str = ""

    # ============================================================
    # Event Payload
    # ============================================================

    payload: dict[str, Any] = field(
        default_factory=dict
    )

    # ============================================================
    # Helper Methods
    # ============================================================

    def to_dict(self) -> dict[str, Any]:
        """
        Convert the event into a JSON-serializable dictionary.
        """

        data = asdict(self)

        data["event_timestamp"] = (
            self.event_timestamp.isoformat()
        )

        if isinstance(self.event_type, Enum):
            data["event_type"] = self.event_type.value

        return data

    def __str__(self) -> str:
        """
        Human-readable representation.
        """

        return (
            f"{self.event_type.value} | "
            f"{self.machine_id} | "
            f"{self.serial_number}"
        )