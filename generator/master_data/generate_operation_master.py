
"""
generate_operation_master.py

Generate Operation Master for the Smart Manufacturing Lakehouse.

Author:
Sumanth Vempalle

Version:
1.0.0
"""

from __future__ import annotations

import logging

import pandas as pd

from generator.configs.factory_digital_twin import (
    Department,
    MachineType,
    Operation,
    StationType,
    to_dict,
)

from generator.configs.paths import OPERATIONS_PATH

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)-8s %(message)s",
)

logger = logging.getLogger(__name__)


OPERATIONS = [

    Operation(
        operation_id="OP-001",
        operation_number=10,
        operation_code="OP10",
        operation_name="Contact Press Fit",
        department=Department.PRESS_SHOP,
        station_type=StationType.PRESS_FITTING,
        machine_type=MachineType.PRESS_FITTING,
        requires_operator=True,
        requires_tool=True,
        quality_checkpoint=True,
        standard_cycle_time_sec=15,
    ),

    Operation(
        operation_id="OP-002",
        operation_number=20,
        operation_code="OP20",
        operation_name="Mechanism Press Fit",
        department=Department.PRESS_SHOP,
        station_type=StationType.PRESS_FITTING,
        machine_type=MachineType.PRESS_FITTING,
        requires_operator=True,
        requires_tool=True,
        quality_checkpoint=True,
        standard_cycle_time_sec=20,
    ),

    Operation(
        operation_id="OP-003",
        operation_number=30,
        operation_code="OP30",
        operation_name="Insulator Press Fit",
        department=Department.PRESS_SHOP,
        station_type=StationType.PRESS_FITTING,
        machine_type=MachineType.PRESS_FITTING,
        requires_operator=True,
        requires_tool=True,
        quality_checkpoint=True,
        standard_cycle_time_sec=30,
    ),

    Operation(
        operation_id="OP-004",
        operation_number=40,
        operation_code="OP40",
        operation_name="Final Housing Press Fit",
        department=Department.PRESS_SHOP,
        station_type=StationType.PRESS_FITTING,
        machine_type=MachineType.PRESS_FITTING,
        requires_operator=True,
        requires_tool=True,
        quality_checkpoint=True,
        standard_cycle_time_sec=40,
    ),

    Operation(
        operation_id="OP-005",
        operation_number=50,
        operation_code="OP50",
        operation_name="Circuit Breaker Assembly",
        department=Department.ASSEMBLY,
        station_type=StationType.CIRCUIT_BREAKER_ASSEMBLY,
        machine_type=MachineType.CIRCUIT_BREAKER_ASSEMBLY,
        requires_operator=True,
        requires_tool=False,
        quality_checkpoint=False,
        standard_cycle_time_sec=120,
    ),

    Operation(
        operation_id="OP-006",
        operation_number=60,
        operation_code="OP60",
        operation_name="Dead Tank Assembly",
        department=Department.ASSEMBLY,
        station_type=StationType.DEAD_TANK_ASSEMBLY,
        machine_type=MachineType.DEAD_TANK_ASSEMBLY,
        requires_operator=True,
        requires_tool=False,
        quality_checkpoint=False,
        standard_cycle_time_sec=180,
    ),

    Operation(
        operation_id="OP-007",
        operation_number=70,
        operation_code="OP70",
        operation_name="GIS Bay Assembly",
        department=Department.ASSEMBLY,
        station_type=StationType.GIS_ASSEMBLY,
        machine_type=MachineType.GIS_ASSEMBLY,
        requires_operator=True,
        requires_tool=False,
        quality_checkpoint=True,
        standard_cycle_time_sec=240,
    ),

    Operation(
        operation_id="OP-008",
        operation_number=80,
        operation_code="OP80",
        operation_name="Visual Inspection",
        department=Department.QUALITY,
        station_type=StationType.VISUAL_INSPECTION,
        machine_type=MachineType.VISUAL_INSPECTION,
        requires_operator=True,
        requires_tool=False,
        quality_checkpoint=True,
        standard_cycle_time_sec=45,
    ),

    Operation(
        operation_id="OP-009",
        operation_number=90,
        operation_code="OP90",
        operation_name="Mechanical Test",
        department=Department.TESTING,
        station_type=StationType.MECHANICAL_TEST,
        machine_type=MachineType.MECHANICAL_TEST,
        requires_operator=True,
        requires_tool=False,
        quality_checkpoint=True,
        standard_cycle_time_sec=300,
    ),

    Operation(
        operation_id="OP-010",
        operation_number=100,
        operation_code="OP100",
        operation_name="High Voltage Test",
        department=Department.TESTING,
        station_type=StationType.HIGH_VOLTAGE_TEST,
        machine_type=MachineType.HIGH_VOLTAGE_TEST,
        requires_operator=True,
        requires_tool=False,
        quality_checkpoint=True,
        standard_cycle_time_sec=420,
    ),

    Operation(
        operation_id="OP-011",
        operation_number=110,
        operation_code="OP110",
        operation_name="Pressure Leak Test",
        department=Department.TESTING,
        station_type=StationType.PRESSURE_TEST,
        machine_type=MachineType.PRESSURE_TEST,
        requires_operator=True,
        requires_tool=False,
        quality_checkpoint=True,
        standard_cycle_time_sec=360,
    ),

    Operation(
        operation_id="OP-012",
        operation_number=120,
        operation_code="OP120",
        operation_name="Packaging",
        department=Department.LOGISTICS,
        station_type=StationType.PACKAGING,
        machine_type=MachineType.PACKAGING,
        requires_operator=True,
        requires_tool=False,
        quality_checkpoint=False,
        standard_cycle_time_sec=180,
    ),
]


def validate_operations(operations: list[Operation]) -> None:

    ids = {op.operation_id for op in operations}

    if len(ids) != len(operations):
        raise ValueError("Duplicate operation IDs.")

    codes = {op.operation_code for op in operations}

    if len(codes) != len(operations):
        raise ValueError("Duplicate operation codes.")

    logger.info("Operation validation successful.")


def export_operations(operations: list[Operation]) -> None:

    OPERATIONS_PATH.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    pd.DataFrame(
        to_dict(operations)
    ).to_csv(
        OPERATIONS_PATH,
        index=False,
    )

    logger.info("Operation Master exported.")


def main():

    logger.info("Generating Operation Master...")

    validate_operations(OPERATIONS)

    export_operations(OPERATIONS)

    logger.info("Operation Master generation completed.")


if __name__ == "__main__":
    main()
