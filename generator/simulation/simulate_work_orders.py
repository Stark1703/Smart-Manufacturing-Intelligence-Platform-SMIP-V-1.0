
"""
simulate_work_orders.py

Simulate SAP Production Work Orders.

Author:
Sumanth Vempalle

Version:
1.0.0
"""

from __future__ import annotations

import logging

import pandas as pd

from dataclasses import asdict

from generator.engine.production_planner import ProductionPlanner

from generator.configs.paths import (
    PRODUCTS_PATH,
    WORK_ORDERS_PATH,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)-8s %(message)s",
)

logger = logging.getLogger(__name__)


def load_products() -> pd.DataFrame:

    """
    Load ERP Product Master.
    """

    df = pd.read_csv(PRODUCTS_PATH)

    logger.info(
        "Loaded %d products.",
        len(df),
    )

    return df

def validate(
    work_orders,
    products: pd.DataFrame,
) -> None:

    logger.info("Validating work orders...")

    df = pd.DataFrame(
        [asdict(order) for order in work_orders]
    )

    if df.empty:
        raise ValueError(
            "No work orders generated."
        )

    if df["work_order_id"].duplicated().any():
        raise ValueError(
            "Duplicate Work Order IDs."
        )

    if df["sap_order_number"].duplicated().any():
        raise ValueError(
            "Duplicate SAP Order Numbers."
        )

    valid_products = set(
        products["product_code"]
    )

    invalid = (
        ~df["product_code"].isin(valid_products)
    )

    if invalid.any():

        raise ValueError(
            "Invalid Product Codes detected."
        )

    if (df["quantity"] <= 0).any():

        raise ValueError(
            "Invalid quantity."
        )

    if (
        df["planned_finish"]
        <=
        df["planned_start"]
    ).any():

        raise ValueError(
            "Invalid timestamps."
        )

    logger.info(
        "Validation successful."
    )

def export(
    work_orders,
) -> None:

    df = pd.DataFrame(
        [asdict(order) for order in work_orders]
    )

    WORK_ORDERS_PATH.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    df.to_csv(
        WORK_ORDERS_PATH,
        index=False,
    )

    logger.info(
        "Exported %d work orders.",
        len(df),
    )

def main():

    logger.info(
        "=================================="
    )

    logger.info(
        "Starting Work Order Simulation"
    )

    logger.info(
        "=================================="
    )

    products = load_products()

    planner = ProductionPlanner(
        products
    )

    work_orders = planner.generate()

    validate(
        work_orders,
        products,
    )

    export(
        work_orders,
    )

    logger.info(
        "Simulation completed successfully."
    )


if __name__ == "__main__":
    main()





