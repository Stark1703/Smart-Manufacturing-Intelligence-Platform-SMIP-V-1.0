"""
streaming_pipeline.py

Streaming Pipeline for the Smart Manufacturing Intelligence Platform (SMIP).

This class orchestrates the complete streaming workflow.

Author:
Sumanth Vempalle + ChatGPT

Version:
2.0.0
"""

from __future__ import annotations

import logging
import time
from datetime import datetime

from streaming.builders.manufacturing_event_builder import ManufacturingEventBuilder
from streaming.configs.streaming_config import (
    PLANT_CODE,
    STREAM_DELAY_SECONDS,
)
from streaming.enrichers.manufacturing_enricher import ManufacturingEnricher
from streaming.loaders.master_data_loader import MasterDataLoader
from streaming.loaders.transactional_loader import TransactionalLoader
from streaming.producers.manufacturing_event_producer import (
    ManufacturingEventProducer,
)
from streaming.utils.json_writer import JSONEventWriter

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(message)s",
)

logger = logging.getLogger(__name__)


class StreamingPipeline:
    """
    End-to-end Manufacturing Streaming Pipeline.
    """

    def __init__(self) -> None:

        self.master_loader = None
        self.transactional_loader = None
        self.enricher = None
        self.builder = None
        self.producer = None
        self.writer = None

        self.events_processed = 0

        self.start_time = None
        self.end_time = None

    # ============================================================
    # Initialize
    # ============================================================

    def initialize(self) -> None:

        logger.info("=" * 60)
        logger.info("Initializing SMIP Streaming Pipeline")
        logger.info("=" * 60)

        # Master Data

        self.master_loader = MasterDataLoader()
        self.master_loader.summary()

        # Transactional Data

        self.transactional_loader = TransactionalLoader()
        self.transactional_loader.summary()

        # Enricher

        self.enricher = ManufacturingEnricher(
            self.master_loader
        )
        self.enricher.summary()

        # Builder

        self.builder = ManufacturingEventBuilder(
            plant_code=PLANT_CODE,
        )

        # Producer

        self.producer = ManufacturingEventProducer(
            loader=self.transactional_loader,
            enricher=self.enricher,
            builder=self.builder,
        )

        # Writer

        self.writer = JSONEventWriter()

        logger.info("Pipeline initialized successfully.")

    # ============================================================
    # Run
    # ============================================================

    def run(self) -> None:

        self.start_time = datetime.now()

        self.initialize()

        logger.info("=" * 60)
        logger.info("Starting Manufacturing Event Stream")
        logger.info("=" * 60)

        for event in self.producer:

            self.writer.write_event(event)

            self.events_processed += 1

            logger.info(
                "[%06d] %s",
                self.events_processed,
                event.event_type.name,
            )

            time.sleep(
                STREAM_DELAY_SECONDS
            )

        self.end_time = datetime.now()

        self.summary()

    # ============================================================
    # Summary
    # ============================================================

    def summary(self) -> None:

        duration = self.end_time - self.start_time

        logger.info("=" * 60)
        logger.info("SMIP Streaming Summary")
        logger.info("=" * 60)

        logger.info(
            "Pipeline Status   : SUCCESS"
        )

        logger.info(
            "Events Processed : %d",
            self.events_processed,
        )

        logger.info(
            "Duration         : %s",
            duration,
        )

        logger.info("=" * 60)