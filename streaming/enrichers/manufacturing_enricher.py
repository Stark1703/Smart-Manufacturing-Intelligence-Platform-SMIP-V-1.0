"""
manufacturing_enricher.py

Manufacturing Event Enricher for the Smart Manufacturing
Intelligence Platform (SMIP).

This module enriches transactional manufacturing records using
the Factory Digital Twin master data.

Author:
Sumanth Vempalle

Version:
2.0.0
"""

from __future__ import annotations

import logging
from typing import Any

from streaming.loaders.master_data_loader import (
    MasterDataLoader,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)-8s %(message)s",
)

logger = logging.getLogger(__name__)


class ManufacturingEnricher:
    """
    Enrich manufacturing transactions with Factory Digital Twin
    master data.

    Responsibilities
    ----------------

    - Resolve product information

    - Resolve machine information

    - Resolve operator information

    - Resolve tool information

    - Resolve operation information

    - Resolve station information

    - Resolve production line

    - Resolve production hall

    The enricher never modifies transactional data.

    It only enriches it with reference/master data.
    """

    # ============================================================
    # Constructor
    # ============================================================

    def __init__(
        self,
        master: MasterDataLoader,
    ) -> None:

        self.master = master

        logger.info(
            "Initializing Manufacturing Enricher..."
        )

        # --------------------------------------------------------
        # Product Lookup
        # --------------------------------------------------------

        self.products = (

            master.products

            .set_index(
                "product_code"
            )

            .to_dict(
                orient="index"
            )

        )

        # --------------------------------------------------------
        # Machine Lookup
        # --------------------------------------------------------

        self.machines = (

            master.machines

            .set_index(
                "machine_id"
            )

            .to_dict(
                orient="index"
            )

        )

        # --------------------------------------------------------
        # Operator Lookup
        # --------------------------------------------------------

        self.operators = (

            master.operators

            .set_index(
                "operator_id"
            )

            .to_dict(
                orient="index"
            )

        )

        # --------------------------------------------------------
        # Tool Lookup
        # --------------------------------------------------------

        self.tools = (

            master.tools

            .set_index(
                "tool_id"
            )

            .to_dict(
                orient="index"
            )

        )

        # --------------------------------------------------------
        # Operation Lookup
        # --------------------------------------------------------

        self.operations = (

            master.operations

            .set_index(
                "operation_number"
            )

            .to_dict(
                orient="index"
            )

        )

        # --------------------------------------------------------
        # Station Lookup
        # --------------------------------------------------------

        self.stations = (

            master.stations

            .set_index(
                "station_id"
            )

            .to_dict(
                orient="index"
            )

        )

        # --------------------------------------------------------
        # Production Line Lookup
        # --------------------------------------------------------

        self.lines = (

            master.production_lines

            .set_index(
                "line_id"
            )

            .to_dict(
                orient="index"
            )

        )

        # --------------------------------------------------------
        # Production Hall Lookup
        # --------------------------------------------------------

        self.halls = (

            master.production_halls

            .set_index(
                "hall_id"
            )

            .to_dict(
                orient="index"
            )

        )

        logger.info(
            "Manufacturing Enricher initialized successfully."
        )

        logger.info(
            "Products           : %d",
            len(self.products),
        )

        logger.info(
            "Machines           : %d",
            len(self.machines),
        )

        logger.info(
            "Operators          : %d",
            len(self.operators),
        )

        logger.info(
            "Tools              : %d",
            len(self.tools),
        )

        logger.info(
            "Operations         : %d",
            len(self.operations),
        )

        logger.info(
            "Stations           : %d",
            len(self.stations),
        )

        logger.info(
            "Production Lines   : %d",
            len(self.lines),
        )

        logger.info(
            "Production Halls   : %d",
            len(self.halls),
        )



            # ============================================================
    # Product Lookup
    # ============================================================

    def _get_product(
        self,
        product_code: str | None,
    ) -> dict:
        """
        Return Product master data.
        """

        if not product_code:
            return {}

        return self.products.get(
            product_code,
            {},
        )

    # ============================================================
    # Machine Lookup
    # ============================================================

    def _get_machine(
        self,
        machine_id: str | None,
    ) -> dict:
        """
        Return Machine master data.
        """

        if not machine_id:
            return {}

        return self.machines.get(
            machine_id,
            {},
        )

    # ============================================================
    # Operator Lookup
    # ============================================================

    def _get_operator(
        self,
        operator_id: str | None,
    ) -> dict:
        """
        Return Operator master data.
        """

        if not operator_id:
            return {}

        return self.operators.get(
            operator_id,
            {},
        )

    # ============================================================
    # Tool Lookup
    # ============================================================

    def _get_tool(
        self,
        tool_id: str | None,
    ) -> dict:
        """
        Return Tool master data.
        """

        if not tool_id:
            return {}

        return self.tools.get(
            tool_id,
            {},
        )

    # ============================================================
    # Operation Lookup
    # ============================================================

    def _get_operation(
        self,
        operation_number: int | None,
    ) -> dict:
        """
        Return Operation master data.
        """

        if operation_number is None:
            return {}

        return self.operations.get(
            operation_number,
            {},
        )

    # ============================================================
    # Station Lookup
    # ============================================================

    def _get_station(
        self,
        station_id: str | None,
    ) -> dict:
        """
        Return Station master data.
        """

        if not station_id:
            return {}

        return self.stations.get(
            station_id,
            {},
        )

    # ============================================================
    # Production Line Lookup
    # ============================================================

    def _get_line(
        self,
        line_id: str | None,
    ) -> dict:
        """
        Return Production Line master data.
        """

        if not line_id:
            return {}

        return self.lines.get(
            line_id,
            {},
        )

    # ============================================================
    # Production Hall Lookup
    # ============================================================

    def _get_hall(
        self,
        hall_id: str | None,
    ) -> dict:
        """
        Return Production Hall master data.
        """

        if not hall_id:
            return {}

        return self.halls.get(
            hall_id,
            {},
        )

    # ============================================================
    # Build Common Manufacturing Context
    # ============================================================

    def _build_common_context(
        self,
        row: dict[str, Any],
    ) -> dict:
        """
        Build the common manufacturing context shared by all
        streaming events.
        """

        product = self._get_product(
            row.get("product_code")
        )

        machine = self._get_machine(
            row.get("machine_id")
        )

        operator = self._get_operator(
            row.get("operator_id")
        )

        tool = self._get_tool(
            row.get("tool_id")
        )

        operation = self._get_operation(
            row.get("operation_number")
        )

        station = self._get_station(
            machine.get("station_id")
        )

        line = self._get_line(
            machine.get("line_id")
        )

        hall = self._get_hall(
            line.get("hall_id")
        )

        return {

            # ----------------------------------------------------
            # Product
            # ----------------------------------------------------

            "product_name":
                product.get("product_name"),

            "family":
                product.get("family"),

            "rated_voltage_kv":
                product.get("rated_voltage_kv"),

            "rated_current_a":
                product.get("rated_current_a"),

            # ----------------------------------------------------
            # Machine
            # ----------------------------------------------------

            "machine_name":
                machine.get("machine_name"),

            "machine_type":
                machine.get("machine_type"),

            "manufacturer":
                machine.get("manufacturer"),

            "machine_status":
                machine.get("status"),

            # ----------------------------------------------------
            # Station
            # ----------------------------------------------------

            "station_code":
                station.get("station_code"),

            "station_type":
                station.get("station_type"),

            "station_sequence":
                machine.get("station_sequence"),

            # ----------------------------------------------------
            # Production Line
            # ----------------------------------------------------

            "line_name":
                line.get("line_name"),

            # ----------------------------------------------------
            # Production Hall
            # ----------------------------------------------------

            "hall_name":
                hall.get("hall_name"),

            # ----------------------------------------------------
            # Operator
            # ----------------------------------------------------

            "operator_name":

                (
                    f"{operator.get('first_name', '')} "
                    f"{operator.get('last_name', '')}"
                ).strip(),

            "employee_number":
                operator.get("employee_number"),

            "skill_level":
                operator.get("skill_level"),

            # ----------------------------------------------------
            # Tool
            # ----------------------------------------------------

            "tool_name":
                tool.get("tool_name"),

            "tool_type":
                tool.get("tool_type"),

            # ----------------------------------------------------
            # Operation
            # ----------------------------------------------------

            "operation_name":
                operation.get("operation_name"),

            "department":
                operation.get("department"),
        }


        # ============================================================
    # Work Order Enrichment
    # ============================================================

    def enrich_work_order(
        self,
        row: dict[str, Any],
    ) -> dict:
        """
        Enrich a Work Order record with Digital Twin context.
        """

        context = self._build_common_context(row)

        context.update({

            "planner":
                row.get("planner"),

            "planned_shift":
                row.get("planned_shift"),

            "priority":
                row.get("priority"),

            "routing_version":
                row.get("routing_version"),

            "status":
                row.get("status"),

        })

        return context

    # ============================================================
    # Production Execution Enrichment
    # ============================================================

    def enrich_execution(
        self,
        row: dict[str, Any],
    ) -> dict:
        """
        Enrich a Production Execution record.
        """

        context = self._build_common_context(row)

        context.update({

            "execution_status":
                row.get("status"),

            "planned_shift":
                row.get("planned_shift"),

            "execution_start":
                row.get("execution_start"),

            "execution_end":
                row.get("execution_end"),

        })

        return context

    # ============================================================
    # Serial Number Enrichment
    # ============================================================

    def enrich_serial_number(
        self,
        row: dict[str, Any],
    ) -> dict:
        """
        Enrich a Serial Number record.
        """

        context = self._build_common_context(row)

        context.update({

            "serial_number":
                row.get("serial_number"),

            "manufacturing_date":
                row.get("manufacturing_date"),

        })

        return context

    # ============================================================
    # Manufacturing Operation Enrichment
    # ============================================================

    def enrich_operation(
        self,
        row: dict[str, Any],
    ) -> dict:
        """
        Enrich a manufacturing operation.

        This method is generic and supports all manufacturing
        operations including:

        - Press Fitting
        - GIS Assembly
        - Circuit Breaker Assembly
        - Mechanical Test
        - High Voltage Test
        - Pressure Test
        - Visual Inspection
        """

        context = self._build_common_context(row)

        context.update({

            # ----------------------------------------------------
            # Operation
            # ----------------------------------------------------

            "operation_id":
                (    
                    row.get("press_operation_id")
                    or row.get("press_operation_id")

                ),
                
            "operation_number":
                row.get("operation_number"),

            "operation_start":
                row.get("operation_start"),

            "operation_end":
                row.get("operation_end"),

            # ----------------------------------------------------
            # Process Parameters
            # ----------------------------------------------------

            "cycle_time_sec":
                row.get("cycle_time_sec"),

            "target_force_kn":
                row.get("target_force_kn"),

            "actual_force_kn":
                row.get("actual_force_kn"),

            "force_deviation_kn":
                row.get("force_deviation_kn"),

            "displacement_mm":
                row.get("displacement_mm"),

            # ----------------------------------------------------
            # Quality
            # ----------------------------------------------------

            "quality_result":
                row.get("quality_result"),

        })

        return context


        # ============================================================
    # Quality Enrichment
    # ============================================================

    def enrich_quality(
        self,
        row: dict[str, Any],
    ) -> dict:
        """
        Enrich a Quality Test record.
        """

        context = self._build_common_context(row)

        context.update({

            "test_result_id":
                row.get("test_result_id"),

            "test_program_id":
                row.get("test_program_id"),

            "test_name":
                row.get("test_name"),

            "target_value":
                row.get("target_value"),

            "measured_value":
                row.get("measured_value"),

            "unit":
                row.get("unit"),

            "result":
                row.get("result"),

            "test_start":
                row.get("start_time"),

            "test_end":
                row.get("end_time"),

        })

        return context

    # ============================================================
    # Material Scan Enrichment
    # ============================================================

    def enrich_material(
        self,
        row: dict[str, Any],
    ) -> dict:
        """
        Enrich a Material Scan record.
        """

        context = self._build_common_context(row)

        context.update({

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

            "scan_timestamp":
                row.get("scan_timestamp"),

        })

        return context

    # ============================================================
    # Packaging Enrichment
    # ============================================================

    def enrich_packaging(
        self,
        row: dict[str, Any],
    ) -> dict:
        """
        Enrich a Packaging record.
        """

        context = self._build_common_context(row)

        context.update({

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

            "packaging_start":
                row.get("packaging_start"),

            "packaging_end":
                row.get("packaging_end"),

        })

        return context

    # ============================================================
    # Summary
    # ============================================================

    def summary(self) -> None:
        """
        Display enrichment summary.
        """

        logger.info("========================================")
        logger.info("Manufacturing Enricher Summary")
        logger.info("========================================")

        logger.info(
            "Products            : %d",
            len(self.products),
        )

        logger.info(
            "Machines            : %d",
            len(self.machines),
        )

        logger.info(
            "Operators           : %d",
            len(self.operators),
        )

        logger.info(
            "Tools               : %d",
            len(self.tools),
        )

        logger.info(
            "Operations          : %d",
            len(self.operations),
        )

        logger.info(
            "Stations            : %d",
            len(self.stations),
        )

        logger.info(
            "Production Lines    : %d",
            len(self.lines),
        )

        logger.info(
            "Production Halls    : %d",
            len(self.halls),
        )

        logger.info("========================================")