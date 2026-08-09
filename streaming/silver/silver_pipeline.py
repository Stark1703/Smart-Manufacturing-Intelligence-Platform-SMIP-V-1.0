"""
silver_pipeline.py

Silver Pipeline for the Smart Manufacturing Intelligence Platform (SMIP).

Reads Bronze events, validates them, transforms them,
and stores them in the Silver layer.

Author:
Sumanth Vempalle

Version:
2.0.0
"""

from __future__ import annotations



from streaming.bronze.bronze_reader import BronzeReader
from streaming.configs.data_paths import (
    BRONZE_EVENTS_PATH,
    SILVER_EVENTS_PATH,
)
from streaming.silver.silver_transformer import SilverTransformer
from streaming.silver.silver_validator import SilverValidator
from streaming.silver.silver_writer import SilverWriter

import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(message)s",
)

logger = logging.getLogger(__name__)

class SilverPipeline:
    """
    End-to-end Silver processing pipeline.
    """

    def __init__(self) -> None:

        self.reader = BronzeReader(
            BRONZE_EVENTS_PATH
        )

        self.validator = SilverValidator()

        self.transformer = SilverTransformer()

        self.writer = SilverWriter()

        self.total_events = 0
        self.valid_events = 0
        self.invalid_events = 0

    # ============================================================
    # Run
    # ============================================================

    def run(self) -> None:
        """
        Execute the Silver pipeline.
        """

        logger.info("=" * 60)
        logger.info("Starting Silver Pipeline")
        logger.info("=" * 60)

        for bronze_event in self.reader.read_events():

            self.total_events += 1

            try:

                if not self.validator.validate(bronze_event):

                    self.invalid_events += 1

                    logger.warning(
                        "Invalid Bronze Event skipped: %s",
                        self.validator.errors,
                    )

                    continue

                silver_event = self.transformer.transform(
                    bronze_event
                )

                self.writer.write_event(
                    silver_event
                )

                self.valid_events += 1

            except Exception as ex:

                self.invalid_events += 1

                logger.exception(
                    "Silver processing failed: %s",
                    ex,
                )

        self.summary()

    # ============================================================
    # Summary
    # ============================================================

    def summary(self) -> None:

        logger.info("=" * 60)
        logger.info("Silver Pipeline Summary")
        logger.info("=" * 60)

        logger.info(
            "Total Events   : %d",
            self.total_events,
        )

        logger.info(
            "Valid Events   : %d",
            self.valid_events,
        )

        logger.info(
            "Invalid Events : %d",
            self.invalid_events,
        )

        logger.info("=" * 60)