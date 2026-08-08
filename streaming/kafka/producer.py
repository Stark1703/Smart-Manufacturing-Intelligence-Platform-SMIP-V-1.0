"""
producer.py

Kafka Producer for the Smart Manufacturing Intelligence Platform (SMIP).

Responsible for publishing Manufacturing Events to Apache Kafka.

Author:
Sumanth Vempalle

Version:
2.0.0
"""

from __future__ import annotations

import json
import logging

from confluent_kafka import Producer

from streaming.events.manufacturing_event import ManufacturingEvent
from . import config


logger = logging.getLogger(__name__)


class ManufacturingKafkaProducer:

    def __init__(self) -> None:

        self.producer = Producer(
            {
                "bootstrap.servers": ",".join(config.BOOTSTRAP_SERVERS),
                "client.id": config.CLIENT_ID,
                "acks": config.ACKS,
            }
        )

    def _delivery_report(self, err, msg):
        """
        Kafka delivery callback.
        """

        if err is not None:
            logger.error("Delivery failed: %s", err)

        else:
            logger.info(
                "Delivered to %s [%d] offset %d",
                msg.topic(),
                msg.partition(),
                msg.offset(),
            )

    def _serialize(self, event: ManufacturingEvent) -> str:
        """
        Serialize ManufacturingEvent into JSON.
        """

        return json.dumps(
            event.to_dict(),
            default=str,
        )

    def send(
        self,
        topic: str,
        event: ManufacturingEvent,
    ) -> None:
        """
        Publish one ManufacturingEvent to Kafka.
        """

        self.producer.produce(
            topic=topic,
            key=event.event_id,
            value=json.dumps(
                 event.to_dict(),
                 default=str,
          ),
            callback=self._delivery_report,
        )

        self.producer.poll(0)

    def flush(self) -> None:
        """
        Wait until all queued messages are delivered.
        """

        self.producer.flush()