"""
json_writer.py

JSON writer utilities for the Smart Manufacturing Intelligence Platform (SMIP).

This module provides helper functions for writing manufacturing
events as JSON files for streaming ingestion.

Author:
Sumanth Vempalle + ChatGPT

Version:
2.0.0
"""

from __future__ import annotations

import json
import logging

from pathlib import Path

from streaming.configs.streaming_config import (
    STREAMING_EVENTS_PATH,
    JSON_INDENT,
    JSON_ENCODING,
)

from streaming.events.manufacturing_event import (
    ManufacturingEvent,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)-8s %(message)s",
)

logger = logging.getLogger(__name__)


# ============================================================
# JSON Writer
# ============================================================

class JSONWriter:
    """
    Writes Manufacturing Events as JSON files.

    Each event is written to an individual JSON file,
    allowing Databricks Auto Loader to detect new files
    as they arrive.
    """

    def __init__(
        self,
        output_directory: Path = STREAMING_EVENTS_PATH,
    ) -> None:

        self.output_directory = output_directory

        self.output_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

    # ============================================================
    # Public API
    # ============================================================

    def write_event(
        self,
        event: ManufacturingEvent,
    ) -> Path:
        """
        Write a Manufacturing Event to a JSON file.

        Parameters
        ----------
        event:
            ManufacturingEvent instance.

        Returns
        -------
        Path
            Path of the generated JSON file.
        """

        filename = (
            f"{event.event_timestamp:%Y%m%d_%H%M%S_%f}_"
            f"{event.event_id}.json"
        )

        file_path = self.output_directory / filename

        with open(
            file_path,
            "w",
            encoding=JSON_ENCODING,
        ) as file:

            json.dump(
                event.to_dict(),
                file,
                indent=JSON_INDENT,
                ensure_ascii=False,
            )

        logger.info(
            "Event written: %s",
            file_path.name,
        )

        return file_path

    # ============================================================
    # Batch Writer
    # ============================================================

    def write_events(
        self,
        events: list[ManufacturingEvent],
    ) -> list[Path]:
        """
        Write multiple Manufacturing Events.

        Returns
        -------
        list[Path]
            Generated file paths.
        """

        files: list[Path] = []

        for event in events:

            files.append(
                self.write_event(event)
            )

        logger.info(
            "Successfully wrote %d events.",
            len(files),
        )

        return files