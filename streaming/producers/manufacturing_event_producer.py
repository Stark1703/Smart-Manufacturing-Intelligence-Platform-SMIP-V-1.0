"""
production_event_producer.py

Production Event Producer for the Smart Manufacturing
Intelligence Platform (SMIP).

This module converts transactional manufacturing records into a
chronological stream of ManufacturingEvent objects.

Author:
Sumanth Vempalle 

Version:
2.0.0
"""

from __future__ import annotations

import logging

from collections.abc import Iterator

from streaming.builders.manufacturing_event_builder import (
    ManufacturingEventBuilder,
)

from streaming.enrichers.manufacturing_enricher import (
    ManufacturingEnricher,
)

from streaming.events.manufacturing_event import (
    ManufacturingEvent,
)

from streaming.loaders.transactional_loader import (
    TransactionalLoader,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)-8s %(message)s",
)

logger = logging.getLogger(__name__)


class ManufacturingEventProducer:
    """
    Produces chronological Manufacturing Events.

    Responsibilities
    ----------------

    • Read transactional datasets

    • Enrich transactions

    • Build Manufacturing Events

    • Sort by timestamp

    • Yield events one-by-one
    """

    # ============================================================
    # Constructor
    # ============================================================

    def __init__(

        self,

        loader: TransactionalLoader,

        enricher: ManufacturingEnricher,

        builder: ManufacturingEventBuilder,

    ) -> None:

        self.loader = loader

        self.enricher = enricher

        self.builder = builder

        self.events: list[ManufacturingEvent] = []

        self.index = 0

        self.total_processed = 0

        self.total_failed = 0

        logger.info(
            "Production Event Producer initialized."
        )

    # ============================================================
    # Iterator
    # ============================================================

    def __iter__(
        self,
    ) -> Iterator[ManufacturingEvent]:

        if not self.events:

            self._build_event_queue()

        self.index = 0

        return self

    def __next__(
        self,
    ) -> ManufacturingEvent:

        if self.index >= len(self.events):

            raise StopIteration

        event = self.events[self.index]

        self.index += 1

        return event

    # ============================================================
    # Event Queue
    # ============================================================

    def _build_event_queue(
        self,
    ) -> None:
        """
        Build one chronological event queue.
        """

        logger.info(
            "========================================"
        )

        logger.info(
            "Building Manufacturing Event Queue"
        )

        logger.info(
            "========================================"
        )

        self.events.clear()

        # --------------------------------------------------------
        # Manufacturing lifecycle
        # --------------------------------------------------------

        self.events.extend(

            self._collect_work_orders()

        )

        self.events.extend(

            self._collect_executions()

        )

        self.events.extend(

            self._collect_serial_numbers()

        )

        self.events.extend(

            self._collect_operations()

        )

        self.events.extend(

            self._collect_quality()

        )

        self.events.extend(

            self._collect_material()

        )

        self.events.extend(

            self._collect_packaging()

        )

        # --------------------------------------------------------
        # Chronological Order
        # --------------------------------------------------------

        self.events.sort(

            key=lambda event:

                event.event_timestamp

        )

        if not self.events:

            raise ValueError(
                "No manufacturing events were produced."
            )

        logger.info(

            "Manufacturing Event Queue built."

        )

        logger.info(

            "Events Produced    : %d",
            self.total_processed,
        )

        logger.info(

            "Failed Events      : %d",
            self.total_failed,
        )

        logger.info(

            "Queue Size         : %d",
            len(self.events),
        )


            # ============================================================
    # Work Orders
    # ============================================================

    def _collect_work_orders(
        self,
    ) -> list[ManufacturingEvent]:
        """
        Convert Work Orders into Manufacturing Events.
        """

        events: list[ManufacturingEvent] = []

        dataframe = self.loader.get_work_orders()

        for _, row in dataframe.iterrows():

            try:

                row = row.to_dict()

                enriched = self.enricher.enrich_work_order(
                    row
                )

                event = self.builder.build_work_order_created(
                    row,
                    enriched,
                )

                events.append(event)

                self.total_processed += 1

            except Exception:

                self.total_failed += 1

                logger.exception(
                    "Failed to build Work Order event."
                )

        logger.info(
            "Work Orders         : %d",
            len(events),
        )

        return events

    # ============================================================
    # Production Executions
    # ============================================================

    def _collect_executions(
        self,
    ) -> list[ManufacturingEvent]:
        """
        Convert Executions into Manufacturing Events.
        """

        events: list[ManufacturingEvent] = []

        dataframe = self.loader.get_executions()

        for _, row in dataframe.iterrows():

            try:

                row = row.to_dict()

                enriched = self.enricher.enrich_execution(
                    row
                )

                event = self.builder.build_execution_started(
                    row,
                    enriched,
                )

                events.append(event)

                self.total_processed += 1

            except Exception:

                self.total_failed += 1

                logger.exception(
                    "Failed to build Execution event."
                )

        logger.info(
            "Executions          : %d",
            len(events),
        )

        return events

    # ============================================================
    # Serial Numbers
    # ============================================================

    def _collect_serial_numbers(
        self,
    ) -> list[ManufacturingEvent]:
        """
        Convert Serial Numbers into Manufacturing Events.
        """

        events: list[ManufacturingEvent] = []

        dataframe = self.loader.get_serial_numbers()

        for _, row in dataframe.iterrows():

            try:

                row = row.to_dict()

                enriched = self.enricher.enrich_serial_number(
                    row
                )

                event = self.builder.build_serial_number_assigned(
                    row,
                    enriched,
                )

                events.append(event)

                self.total_processed += 1

            except Exception:

                self.total_failed += 1

                logger.exception(
                    "Failed to build Serial Number event."
                )

        logger.info(
            "Serial Numbers      : %d",
            len(events),
        )

        return events

    # ============================================================
    # Manufacturing Operations
    # ============================================================

    def _collect_operations(
        self,
    ) -> list[ManufacturingEvent]:
        """
        Convert Manufacturing Operations into Manufacturing Events.
        """

        events: list[ManufacturingEvent] = []

        dataframe = self.loader.get_press_operations()

        for _, row in dataframe.iterrows():

            try:

                row = row.to_dict()

                enriched = self.enricher.enrich_operation(
                    row
                )

                event = self.builder.build_operation_completed(
                    row,
                    enriched,
                )

                events.append(event)

                self.total_processed += 1

            except Exception:

                self.total_failed += 1

                logger.exception(
                    "Failed to build Operation event."
                )

        logger.info(
            "Operations          : %d",
            len(events),
        )

        return events

    # ============================================================
    # Quality Results
    # ============================================================

    def _collect_quality(
        self,
    ) -> list[ManufacturingEvent]:
        """
        Convert Quality Results into Manufacturing Events.
        """

        events: list[ManufacturingEvent] = []

        dataframe = self.loader.get_quality_results()

        for _, row in dataframe.iterrows():

            try:

                row = row.to_dict()

                enriched = self.enricher.enrich_quality(
                    row
                )

                event = self.builder.build_quality_completed(
                    row,
                    enriched,
                )

                events.append(event)

                self.total_processed += 1

            except Exception:

                self.total_failed += 1

                logger.exception(
                    "Failed to build Quality event."
                )

        logger.info(
            "Quality Results     : %d",
            len(events),
        )

        return events

    # ============================================================
    # Material Scans
    # ============================================================

    def _collect_material(
        self,
    ) -> list[ManufacturingEvent]:
        """
        Convert Material Scans into Manufacturing Events.
        """

        events: list[ManufacturingEvent] = []

        dataframe = self.loader.get_material_events()

        for _, row in dataframe.iterrows():

            try:

                row = row.to_dict()

                enriched = self.enricher.enrich_material(
                    row
                )

                event = self.builder.build_material_scanned(
                    row,
                    enriched,
                )

                events.append(event)

                self.total_processed += 1

            except Exception:

                self.total_failed += 1

                logger.exception(
                    "Failed to build Material event."
                )

        logger.info(
            "Material Scans      : %d",
            len(events),
        )

        return events

    # ============================================================
    # Packaging
    # ============================================================

    def _collect_packaging(
        self,
    ) -> list[ManufacturingEvent]:
        """
        Convert Packaging records into Manufacturing Events.
        """

        events: list[ManufacturingEvent] = []

        dataframe = self.loader.get_packaging_records()

        for _, row in dataframe.iterrows():

            try:

                row = row.to_dict()

                enriched = self.enricher.enrich_packaging(
                    row
                )

                event = self.builder.build_packaging_completed(
                    row,
                    enriched,
                )

                events.append(event)

                self.total_processed += 1

            except Exception:

                self.total_failed += 1

                logger.exception(
                    "Failed to build Packaging event."
                )

        logger.info(
            "Packaging           : %d",
            len(events),
        )

        return events

    # ============================================================
    # Summary
    # ============================================================

    def summary(
        self,
    ) -> None:
        """
        Print Producer Summary.
        """

        logger.info(
            "========================================"
        )

        logger.info(
            "Production Event Producer Summary"
        )

        logger.info(
            "========================================"
        )

        logger.info(
            "Events Produced    : %d",
            self.total_processed,
        )

        logger.info(
            "Failed Events      : %d",
            self.total_failed,
        )

        logger.info(
            "Queue Size         : %d",
            len(self.events),
        )

        logger.info(
            "========================================"
        )

