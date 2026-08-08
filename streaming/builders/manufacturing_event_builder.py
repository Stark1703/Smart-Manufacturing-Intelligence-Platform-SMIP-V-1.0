"""
manufacturing_event_builder.py

Manufacturing Event Builder for the Smart Manufacturing Intelligence Platform (SMIP).

This module converts enriched manufacturing business records into
canonical ManufacturingEvent objects used throughout the SMIP v2.0
streaming platform.

Author:
Sumanth Vempalle 

Version:
2.0.0
"""

from __future__ import annotations

from datetime import datetime
from typing import Any

from streaming.events.event_types import EventType
from streaming.events.manufacturing_event import ManufacturingEvent


class ManufacturingEventBuilder:
    """
    Builder responsible for constructing ManufacturingEvent objects.

    Responsibilities
    ----------------
    - Build standardized manufacturing events
    - Populate common metadata
    - Validate mandatory fields
    - Create event payloads
    - Keep one consistent event schema across SMIP

    This class never reads CSV files or performs joins.
    Those responsibilities belong to the loaders and enrichers.
    """

    # ============================================================
    # Constructor
    # ============================================================

    def __init__(
        self,
        plant_code: str,
        event_version: str = "2.0",
    ) -> None:

        self.plant_code = plant_code
        self.event_version = event_version

    # ============================================================
    # Internal Validation
    # ============================================================

    @staticmethod
    def _validate_required_fields(
        data: dict[str, Any],
        required_fields: list[str],
    ) -> None:
        """
        Validate mandatory fields before creating an event.

        Raises
        ------
        ValueError
            If any required field is missing.
        """

        missing = [

            field

            for field in required_fields

            if data.get(field) in (None, "")

        ]

        if missing:

            raise ValueError(

                f"Missing required fields: {', '.join(missing)}"

            )

    # ============================================================
    # Build Manufacturing Context
    # ============================================================

    @staticmethod
    def _build_context(
        row: dict[str, Any],
        enriched: dict[str, Any],
    ) -> dict[str, Any]:
        """
        Build common manufacturing context shared by all events.
        """

        return {

            "hall_id":

                row.get("hall_id", ""),

            "line_id":

                row.get("line_id", ""),

            "machine_id":

                row.get("machine_id", ""),

            "execution_id":

                row.get("execution_id", ""),

            "work_order_id":

                row.get("work_order_id", ""),

            "serial_number":

                row.get("serial_number", ""),

            "operator_id":

                row.get("operator_id", ""),

            "product_code":

                row.get("product_code", ""),

        }

    # ============================================================
    # Internal Event Creator
    # ============================================================

    def _create_event(
        self,
        *,
        event_type: EventType,
        event_timestamp: datetime,
        row: dict[str, Any],
        enriched: dict[str, Any],
        payload: dict[str, Any],
    ) -> ManufacturingEvent:
        """
        Construct a ManufacturingEvent.

        All public builder methods eventually call this function.
        """

        context = self._build_context(

            row,

            enriched,

        )

        return ManufacturingEvent(

            event_timestamp=event_timestamp,

            event_type=event_type,

            event_version=self.event_version,

            plant_code=self.plant_code,

            hall_id=context["hall_id"],

            line_id=context["line_id"],

            machine_id=context["machine_id"],

            execution_id=context["execution_id"],

            work_order_id=context["work_order_id"],

            serial_number=context["serial_number"],

            operator_id=context["operator_id"],

            product_code=context["product_code"],

            payload=payload,

        )

    # ============================================================
    # Work Order Event
    # ============================================================

    def build_work_order_created(
        self,
        row: dict[str, Any],
        enriched: dict[str, Any],
    ) -> ManufacturingEvent:
        """
        Build WORK_ORDER_CREATED event.
        """

        self._validate_required_fields(

            row,

            [

                "work_order_id",

                "product_code",

                "planned_start",

            ],

        )

        payload = {

            "sap_order_number":

                row.get("sap_order_number"),

            "quantity":

                row.get("quantity"),

            "priority":

                row.get("priority"),

            "planned_shift":

                row.get("planned_shift"),

            "routing_version":

                row.get("routing_version"),

            "planner":

                row.get("planner"),

            "status":

                row.get("status"),

            # ----------------------------------------------------
            # Product Context
            # ----------------------------------------------------

            "product_name":

                enriched.get("product_name"),

            "family":

                enriched.get("family"),

            "rated_voltage_kv":

                enriched.get("rated_voltage_kv"),

        }

        return self._create_event(

            event_type=EventType.WORK_ORDER_CREATED,

            event_timestamp=row["planned_start"],

            row=row,

            enriched=enriched,

            payload=payload,

        )

        # ============================================================
    # Production Execution Started
    # ============================================================

    def build_execution_started(
        self,
        row: dict[str, Any],
        enriched: dict[str, Any],
    ) -> ManufacturingEvent:
        """
        Build EXECUTION_STARTED event.
        """

        self._validate_required_fields(

            row,

            [

                "execution_id",

                "execution_start",

            ],

        )

        payload = {

            "sap_order_number":
                row.get("sap_order_number"),

            "planned_shift":
                row.get("planned_shift"),

            "quantity":
                row.get("quantity"),

            "status":
                row.get("status"),

            "production_line":
                enriched.get("line_name"),

        }

        return self._create_event(

            event_type=EventType.EXECUTION_STARTED,

            event_timestamp=row["execution_start"],

            row=row,

            enriched=enriched,

            payload=payload,

        )

    # ============================================================
    # Serial Number Assigned
    # ============================================================

    def build_serial_number_assigned(
        self,
        row: dict[str, Any],
        enriched: dict[str, Any],
    ) -> ManufacturingEvent:
        """
        Build SERIAL_NUMBER_ASSIGNED event.
        """

        self._validate_required_fields(

            row,

            [

                "serial_number",

                "manufacturing_date",

            ],

        )

        payload = {

            "product_name":
                enriched.get("product_name"),

            "family":
                enriched.get("family"),

            "status":
                row.get("status"),

        }

        return self._create_event(

            event_type=EventType.SERIAL_NUMBER_ASSIGNED,

            event_timestamp=row["manufacturing_date"],

            row=row,

            enriched=enriched,

            payload=payload,

        )

    # ============================================================
    # Manufacturing Operation Completed
    # ============================================================

    def build_operation_completed(
        self,
        row: dict[str, Any],
        enriched: dict[str, Any],
    ) -> ManufacturingEvent:
        """
        Build OPERATION_COMPLETED event.

        This method is generic and supports every manufacturing
        operation performed in the factory.

        Examples
        --------
        - Press Fitting
        - GIS Assembly
        - Circuit Breaker Assembly
        - Visual Inspection
        - Mechanical Test
        - High Voltage Test
        - Pressure Test
        """

        self._validate_required_fields(

            row,

            [

                "press_operation_id",

                "operation_start",

                "machine_id",

            ],

        )

        payload = {

            # ----------------------------------------------------
            # Operation Information
            # ----------------------------------------------------

            "operation_number":
                row.get("operation_number"),

            "operation_name":
                enriched.get("operation_name"),

            "department":
                enriched.get("department"),

            # ----------------------------------------------------
            # Machine
            # ----------------------------------------------------

            "machine_name":
                enriched.get("machine_name"),

            "machine_type":
                enriched.get("machine_type"),

            "station_code":
                enriched.get("station_code"),

            "station_type":
                enriched.get("station_type"),

            "line_name":
                enriched.get("line_name"),

            "hall_name":
                enriched.get("hall_name"),

            # ----------------------------------------------------
            # Tool
            # ----------------------------------------------------

            "tool_name":
                enriched.get("tool_name"),

            "tool_type":
                enriched.get("tool_type"),

            # ----------------------------------------------------
            # Operator
            # ----------------------------------------------------

            "operator_name":
                enriched.get("operator_name"),

            "skill_level":
                enriched.get("skill_level"),

            # ----------------------------------------------------
            # Manufacturing Metrics
            # ----------------------------------------------------

            "target_force_kn":
                row.get("target_force_kn"),

            "actual_force_kn":
                row.get("actual_force_kn"),

            "force_deviation_kn":
                row.get("force_deviation_kn"),

            "displacement_mm":
                row.get("displacement_mm"),

            "cycle_time_sec":
                row.get("cycle_time_sec"),

            "quality_result":
                row.get("quality_result"),

        }

        return self._create_event(

            event_type=EventType.OPERATION_COMPLETED,

            event_timestamp=row["operation_start"],

            row=row,

            enriched=enriched,

            payload=payload,

        )


        # ============================================================
    # Quality Completed
    # ============================================================

    def build_quality_completed(
        self,
        row: dict[str, Any],
        enriched: dict[str, Any],
    ) -> ManufacturingEvent:
        """
        Build QUALITY_COMPLETED event.
        """

        self._validate_required_fields(

            row,

            [

                "test_result_id",

                "start_time",

                "result",

            ],

        )

        payload = {

            # ----------------------------------------------------
            # Test Information
            # ----------------------------------------------------

            "test_result_id":
                row.get("test_result_id"),

            "test_program_id":
                row.get("test_program_id"),

            "test_name":
                row.get("test_name"),

            # ----------------------------------------------------
            # Measurements
            # ----------------------------------------------------

            "target_value":
                row.get("target_value"),

            "measured_value":
                row.get("measured_value"),

            "unit":
                row.get("unit"),

            "result":
                row.get("result"),

            # ----------------------------------------------------
            # Product Context
            # ----------------------------------------------------

            "product_name":
                enriched.get("product_name"),

            "family":
                enriched.get("family"),

        }

        return self._create_event(

            event_type=EventType.QUALITY_COMPLETED,

            event_timestamp=row["start_time"],

            row=row,

            enriched=enriched,

            payload=payload,

        )

    # ============================================================
    # Material Scanned
    # ============================================================

    def build_material_scanned(
        self,
        row: dict[str, Any],
        enriched: dict[str, Any],
    ) -> ManufacturingEvent:
        """
        Build MATERIAL_SCANNED event.
        """

        self._validate_required_fields(

            row,

            [

                "scan_id",

                "scan_timestamp",

                "material_number",

            ],

        )

        payload = {

            "scan_id":
                row.get("scan_id"),

            "material_number":
                row.get("material_number"),

            "batch_number":
                row.get("batch_number"),

            "supplier":
                row.get("supplier"),

            "scan_status":
                row.get("scan_status"),

            "product_name":
                enriched.get("product_name"),

            "family":
                enriched.get("family"),

        }

        return self._create_event(

            event_type=EventType.MATERIAL_SCANNED,

            event_timestamp=row["scan_timestamp"],

            row=row,

            enriched=enriched,

            payload=payload,

        )

    # ============================================================
    # Packaging Completed
    # ============================================================

    def build_packaging_completed(
        self,
        row: dict[str, Any],
        enriched: dict[str, Any],
    ) -> ManufacturingEvent:
        """
        Build PACKAGING_COMPLETED event.
        """

        self._validate_required_fields(

            row,

            [

                "package_id",

                "packaging_start",

            ],

        )

        payload = {

            "package_id":
                row.get("package_id"),

            "package_type":
                row.get("package_type"),

            "package_weight_kg":
                row.get("package_weight_kg"),

            "package_length_mm":
                row.get("package_length_mm"),

            "package_width_mm":
                row.get("package_width_mm"),

            "package_height_mm":
                row.get("package_height_mm"),

            "packaging_status":
                row.get("packaging_status"),

            # ----------------------------------------------------
            # Product Context
            # ----------------------------------------------------

            "product_name":
                enriched.get("product_name"),

            "family":
                enriched.get("family"),

        }

        return self._create_event(

            event_type=EventType.PACKAGING_COMPLETED,

            event_timestamp=row["packaging_start"],

            row=row,

            enriched=enriched,

            payload=payload,

        )