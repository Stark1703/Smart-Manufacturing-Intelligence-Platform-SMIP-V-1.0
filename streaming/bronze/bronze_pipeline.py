"""
bronze_pipeline.py

Bronze Ingestion Pipeline for the Smart Manufacturing Intelligence Platform (SMIP).

Consumes manufacturing events from Kafka and persists them into
the Bronze layer.

Author:
Sumanth Vempalle

Version:
2.0.0
"""

from __future__ import annotations

import json
import logging

from streaming.bronze.bronze_event import BronzeEvent
from streaming.bronze.bronze_writer import BronzeWriter
from streaming.kafka.consumer import ManufacturingKafkaConsumer
from streaming.kafka.topics import MANUFACTURING_EVENTS_TOPIC

logger = logging.getLogger(__name__)


class BronzePipeline:
    """
    Bronze ingestion pipeline.

    Responsibilities
    ----------------
    - Consume Kafka messages
    - Deserialize Manufacturing Events
    - Create BronzeEvent objects
    - Persist Bronze Events
    """

    def __init__(self) -> None:

        self.consumer = ManufacturingKafkaConsumer()

        self.writer = BronzeWriter()

    # ============================================================
    # Initialize
    # ============================================================

    def initialize(self) -> None:

        self.consumer.subscribe(
            MANUFACTURING_EVENTS_TOPIC
        )

        logger.info(
            "Bronze Pipeline initialized."
        )

    # ============================================================
    # Run
    # ============================================================

    def run(self) -> None:

        self.initialize()

        logger.info(
            "Starting Bronze Ingestion..."
        )

        try:

            while True:

                msg = self.consumer.poll()

                if msg is None:
                    continue

                if msg.error():
                    logger.error(msg.error())
                    continue

                event = json.loads(
                    msg.value().decode("utf-8")
                )

                bronze_event = BronzeEvent.from_kafka_message(
                    topic=msg.topic(),
                    partition=msg.partition(),
                    offset=msg.offset(),
                    event=event,
                )

                self.writer.write(
                    bronze_event
                )

                logger.info(
                    "Bronze Event written (offset=%d)",
                    msg.offset(),
                )

        except KeyboardInterrupt:

            logger.info(
                "Stopping Bronze Pipeline..."
            )

        finally:

            self.consumer.close()