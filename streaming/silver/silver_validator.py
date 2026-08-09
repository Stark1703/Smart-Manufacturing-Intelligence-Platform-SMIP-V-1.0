"""
silver_validator.py

Silver Validator for the Smart Manufacturing Intelligence Platform (SMIP).

Responsible for validating Bronze Events before they enter
the Silver layer.

Author:
Sumanth Vempalle

Version:
2.0.0
"""

from __future__ import annotations

import logging

from streaming.bronze.bronze_event import BronzeEvent

logger = logging.getLogger(__name__)


class SilverValidator:
    """
    Validates Bronze Events.
    """

    REQUIRED_EVENT_FIELDS = {

        "event_id",

        "event_timestamp",

        "event_type",

        "event_version",

        "plant_code",

        "payload",

    }

    def __init__(self) -> None:

        self.errors: list[str] = []

    # ============================================================
    # Validate
    # ============================================================

    def validate(
        self,
        bronze_event: BronzeEvent,
    ) -> bool:
        """
        Validate one Bronze Event.
        """

        self.errors.clear()

        event = bronze_event.event

        self._validate_required_fields(event)

        self._validate_payload(event)

        self._validate_types(event)

        self._validate_event_version(event)

        return len(self.errors) == 0

    # ============================================================
    # Required Fields
    # ============================================================

    def _validate_required_fields(
        self,
        event: dict,
    ) -> None:

        for field in self.REQUIRED_EVENT_FIELDS:

            if field not in event:

                self.errors.append(
                    f"Missing required field: {field}"
                )

    # ============================================================
    # Payload
    # ============================================================

    def _validate_payload(
        self,
        event: dict,
    ) -> None:

        payload = event.get("payload")

        if payload is None:

            self.errors.append(
                "Payload is missing."
            )

            return

        if not isinstance(payload, dict):

            self.errors.append(
                "Payload must be a dictionary."
            )

    # ============================================================
    # Basic Types
    # ============================================================

    def _validate_types(
        self,
        event: dict,
    ) -> None:

        if not isinstance(
            event.get("event_id"),
            str,
        ):

            self.errors.append(
                "event_id must be a string."
            )

        if not isinstance(
            event.get("event_type"),
            str,
        ):

            self.errors.append(
                "event_type must be a string."
            )

    # ============================================================
    # Event Version
    # ============================================================

    def _validate_event_version(
        self,
        event: dict,
    ) -> None:

        version = event.get("event_version")

        if version != "2.0":

            self.errors.append(
                f"Unsupported event version: {version}"
            )