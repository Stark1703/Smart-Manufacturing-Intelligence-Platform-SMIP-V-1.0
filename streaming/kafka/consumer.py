"""
consumer.py

Kafka Consumer for the Smart Manufacturing Intelligence Platform (SMIP).

Consumes Manufacturing Events from Kafka.

Author:
Sumanth Vempalle

Version:
2.0.0
"""

from __future__ import annotations

import json
import logging

from confluent_kafka import Consumer

from . import config

logger = logging.getLogger(__name__)


class ManufacturingKafkaConsumer:

    def __init__(self) -> None:

        self.consumer = Consumer(
            {
                "bootstrap.servers": ",".join(config.BOOTSTRAP_SERVERS),
                "group.id": "smip-consumer-group",
                "auto.offset.reset": "earliest",
            }
        )

    def subscribe(self, topic: str) -> None:
        """
        Subscribe to a Kafka topic.
        """

        self.consumer.subscribe([topic])

        logger.info("Subscribed to %s", topic)

    def poll(self):

        return self.consumer.poll(timeout=1.0)

    def close(self):

        self.consumer.close()