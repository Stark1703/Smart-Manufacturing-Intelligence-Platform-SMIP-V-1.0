"""
simulate_press_operations.py

Generate MES Press Operation records
for every manufactured serial number.

Author:
Sumanth Vempalle

Version:
1.0.0
"""

from __future__ import annotations

import logging
import random
from dataclasses import asdict
from datetime import timedelta

import pandas as pd

from generator.configs.factory_digital_twin import (
    PressOperation,
    QualityResult,
)

from generator.configs.paths import (
    SERIAL_NUMBERS_PATH,
    PRESS_PROGRAMS_PATH,
    MACHINES_PATH,
    TOOLS_PATH,
    OPERATORS_PATH,
    PRESS_OPERATIONS_PATH,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)-8s %(message)s",
)

logger = logging.getLogger(__name__)


# ============================================================
# Load Serial Numbers
# ============================================================

def load_serial_numbers() -> pd.DataFrame:

    df = pd.read_csv(
        SERIAL_NUMBERS_PATH,
        parse_dates=[
            "manufacturing_date",
        ],
    )

    logger.info(
        "Loaded %d Serial Numbers.",
        len(df),
    )

    return df


# ============================================================
# Load Press Programs
# ============================================================

def load_press_programs() -> pd.DataFrame:

    df = pd.read_csv(
        PRESS_PROGRAMS_PATH,
    )

    logger.info(
        "Loaded %d Press Programs.",
        len(df),
    )

    return df


# ============================================================
# Load Machines
# ============================================================

def load_machines() -> pd.DataFrame:

    df = pd.read_csv(
        MACHINES_PATH,
    )

    df = df[
        df["machine_type"] == "Press Fitting Machine"
    ]

    logger.info(
        "Loaded %d Press Machines.",
        len(df),
    )

    return df


# ============================================================
# Load Tools
# ============================================================

def load_tools() -> pd.DataFrame:

    df = pd.read_csv(
        TOOLS_PATH,
    )

    logger.info(
        "Loaded %d Tools.",
        len(df),
    )

    return df


# ============================================================
# Load Operators
# ============================================================

def load_operators() -> pd.DataFrame:

    df = pd.read_csv(
        OPERATORS_PATH,
    )

    logger.info(
        "Loaded %d Operators.",
        len(df),
    )

    return df


# ============================================================
# Helper Functions
# ============================================================

def random_force(
    target_force: float,
    tolerance: float,
) -> float:
    """
    Generate realistic press force.
    """

    return round(
        random.uniform(
            target_force - tolerance * 0.70,
            target_force + tolerance * 0.70,
        ),
        2,
    )


def determine_quality(
    actual: float,
    target: float,
    tolerance: float,
) -> QualityResult:

    if abs(actual - target) <= tolerance:
        return QualityResult.PASS

    return QualityResult.FAIL


# ============================================================
# Generate Press Operations
# ============================================================

def generate_press_operations(
    serial_numbers: pd.DataFrame,
    press_programs: pd.DataFrame,
    machines: pd.DataFrame,
    tools: pd.DataFrame,
    operators: pd.DataFrame,
) -> list[PressOperation]:
    """
    Generate one press operation record for every
    press-fit operation of every manufactured serial number.
    """

    operations: list[PressOperation] = []

    operation_counter = 1

    press_program_lookup = (
        press_programs
        .sort_values(
            ["product_code", "operation_number"]
        )
        .groupby("product_code")
    )

    machine_ids = machines["machine_id"].tolist()
    tool_ids = tools["tool_id"].tolist()
    operator_ids = operators["operator_id"].tolist()

    for _, serial in serial_numbers.iterrows():

        product_code = serial["product_code"]

        if product_code not in press_program_lookup.groups:
            continue

        product_programs = press_program_lookup.get_group(
            product_code
        )

        operation_start = pd.to_datetime(
            serial["manufacturing_date"]
        )

        for _, program in product_programs.iterrows():

            cycle_time = int(
                program["maximum_cycle_time_sec"]
            )

            operation_end = (
                operation_start
                + timedelta(seconds=cycle_time)
            )

            target_force = float(
                program["target_force_kn"]
            )

            tolerance = float(
                program["force_tolerance_kn"]
            )

            actual_force = random_force(
                target_force,
                tolerance,
            )

            deviation = round(
                actual_force - target_force,
                2,
            )

            quality = determine_quality(
                actual_force,
                target_force,
                tolerance,
            )

            operation = PressOperation(

                press_operation_id=(
                    f"POP-{operation_counter:08d}"
                ),

                serial_number=serial["serial_number"],

                execution_id=serial["execution_id"],

                work_order_id=serial["work_order_id"],

                operation_number=int(
                    program["operation_number"]
                ),

                operation_name=program[
                    "operation_name"
                ],

                machine_id=random.choice(
                    machine_ids
                ),

                tool_id=random.choice(
                    tool_ids
                ),

                operator_id=random.choice(
                    operator_ids
                ),

                press_program_id=program[
                    "program_id"
                ],

                operation_start=operation_start,

                operation_end=operation_end,

                target_force_kn=target_force,

                actual_force_kn=actual_force,

                force_deviation_kn=deviation,

                displacement_mm=float( program["target_displacement_mm"]),

                cycle_time_sec=cycle_time,

                quality_result=quality,
            )

            operations.append(operation)

            operation_counter += 1

            operation_start = (
                operation_end
                + timedelta(
                    seconds=random.randint(10, 40)
                )
            )

    logger.info(
        "Generated %d Press Operations.",
        len(operations),
    )

    return operations


# ============================================================
# Validation
# ============================================================

def validate(
    operations: list[PressOperation],
) -> None:
    """
    Validate generated press operations.
    """

    df = pd.DataFrame(
        [asdict(x) for x in operations]
    )

    if df.empty:
        raise ValueError(
            "No press operations generated."
        )

    if df["press_operation_id"].duplicated().any():
        raise ValueError(
            "Duplicate Press Operation IDs."
        )

    if df["serial_number"].isnull().any():
        raise ValueError(
            "Missing Serial Numbers."
        )

    logger.info(
        "Press Operation validation successful."
    )


# ============================================================
# Export
# ============================================================

def export(
    operations: list[PressOperation],
) -> None:
    """
    Export press operations to CSV.
    """

    PRESS_OPERATIONS_PATH.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    df = pd.DataFrame(
        [asdict(x) for x in operations]
    )

    df.to_csv(
        PRESS_OPERATIONS_PATH,
        index=False,
    )

    logger.info(
        "Exported %d Press Operations.",
        len(df),
    )


# ============================================================
# Summary
# ============================================================

def summary(
    operations: list[PressOperation],
) -> None:
    """
    Print generation summary.
    """

    logger.info("========================================")
    logger.info(" Press Operation Summary")
    logger.info("========================================")
    logger.info(
        "Total Press Operations : %d",
        len(operations),
    )

    passed = sum(
        1
        for op in operations
        if op.quality_result == QualityResult.PASS
    )

    failed = len(operations) - passed

    logger.info("PASS : %d", passed)
    logger.info("FAIL : %d", failed)
    logger.info("========================================")


    # ============================================================
# Main
# ============================================================

def main() -> None:
    """
    Generate simulated press operations.
    """

    logger.info("========================================")
    logger.info("Starting Press Operation Simulation")
    logger.info("========================================")

    serial_numbers = load_serial_numbers()

    press_programs = load_press_programs()

    machines = load_machines()

    tools = load_tools()

    operators = load_operators()

    operations = generate_press_operations(
        serial_numbers=serial_numbers,
        press_programs=press_programs,
        machines=machines,
        tools=tools,
        operators=operators,
    )

    validate(
        operations
    )

    export(
        operations
    )

    summary(
        operations
    )

    logger.info("Press Operation simulation completed successfully.")


# ============================================================
# Entry Point
# ============================================================

if __name__ == "__main__":
    main()