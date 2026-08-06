
"""
generate_production_executions.py

Generate MES Production Executions from SAP Work Orders.

Author:
Sumanth Vempalle

Version:
1.0.0
"""

from __future__ import annotations

import logging
from dataclasses import asdict
from datetime import timedelta

import pandas as pd

from generator.configs.factory_digital_twin import (
    ExecutionStatus,
    ProductionExecution,
)

from generator.configs.paths import (
    WORK_ORDERS_PATH,
    PRODUCTION_EXECUTIONS_PATH,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)-8s %(message)s",
)

logger = logging.getLogger(__name__)


# ============================================================
# Load Work Orders
# ============================================================

def load_work_orders() -> pd.DataFrame:
    """
    Load generated SAP Work Orders.
    """

    df = pd.read_csv(
        WORK_ORDERS_PATH,
        parse_dates=[
            "planned_start",
            "planned_finish",
        ],
    )

    logger.info(
        "Loaded %d Work Orders.",
        len(df),
    )

    return df


# ============================================================
# Generate Production Executions
# ============================================================

def generate_executions(
    work_orders: pd.DataFrame,
) -> list[ProductionExecution]:
    """
    Generate one MES Production Execution
    for each SAP Work Order.
    """

    executions: list[ProductionExecution] = []

    for index, row in work_orders.iterrows():

        execution = ProductionExecution(

            execution_id=f"EXEC-{index+1:06d}",

            work_order_id=row["work_order_id"],

            sap_order_number=row["sap_order_number"],

            product_code=row["product_code"],

            quantity=int(row["quantity"]),

            plant_code="PLANT-001",

            production_line=row["production_line"],

            planned_shift=row["planned_shift"],

            execution_start=row["planned_start"],

            execution_end=row["planned_finish"],

            status=ExecutionStatus.PLANNED,
        )

        executions.append(execution)

    logger.info(
        "Generated %d Production Executions.",
        len(executions),
    )

    return executions

# ============================================================
# Validation
# ============================================================

def validate(
    executions: list[ProductionExecution],
) -> None:
    """
    Validate generated executions.
    """

    df = pd.DataFrame(
        [asdict(x) for x in executions]
    )

    if df.empty:
        raise ValueError(
            "No executions generated."
        )

    if df["execution_id"].duplicated().any():
        raise ValueError(
            "Duplicate Execution IDs."
        )

    if df["work_order_id"].duplicated().any():
        raise ValueError(
            "Duplicate Work Order IDs."
        )

    if (
        df["execution_end"]
        <=
        df["execution_start"]
    ).any():
        raise ValueError(
            "Invalid execution timestamps."
        )

    logger.info(
        "Production Execution validation successful."
    )


# ============================================================
# Export
# ============================================================

def export(
    executions: list[ProductionExecution],
) -> None:
    """
    Export Production Executions to CSV.
    """

    df = pd.DataFrame(
        [asdict(x) for x in executions]
    )

    PRODUCTION_EXECUTIONS_PATH.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    df.to_csv(
        PRODUCTION_EXECUTIONS_PATH,
        index=False,
    )

    logger.info(
        "Exported %d Production Executions.",
        len(df),
    )


# ============================================================
# Summary
# ============================================================

def summary(
    executions: list[ProductionExecution],
) -> None:
    """
    Print a summary of generated production executions.
    """

    logger.info("========================================")
    logger.info(" Production Execution Summary")
    logger.info("========================================")
    logger.info("Total Executions : %d", len(executions))
    logger.info("Status           : %s", ExecutionStatus.PLANNED.value)
    logger.info("Plant            : PLANT-001")
    logger.info("========================================")


# ============================================================
# Main
# ============================================================

def main() -> None:
    """
    Generate Production Executions from Work Orders.
    """

    logger.info("========================================")
    logger.info("Starting Production Execution Generation")
    logger.info("========================================")

    work_orders = load_work_orders()

    executions = generate_executions(
        work_orders
    )

    validate(
        executions
    )

    export(
        executions
    )

    summary(
        executions
    )

    logger.info("Production Execution generation completed.")


if __name__ == "__main__":
    main()
