
"""
generate_serial_numbers.py

Generate Serial Numbers from Production Executions.

Author:
Sumanth Vempalle 

Version:
1.0.0
"""

from __future__ import annotations

import logging
from dataclasses import asdict

import pandas as pd

from generator.configs.factory_digital_twin import (
    SerialNumber,
)

from generator.configs.paths import (
    PRODUCTS_PATH,
    PRODUCTION_EXECUTIONS_PATH,
    SERIAL_NUMBERS_PATH,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)-8s %(message)s",
)

logger = logging.getLogger(__name__)


# ============================================================
# Load Data
# ============================================================

def load_products() -> pd.DataFrame:
    """
    Load Product Master.
    """

    products = pd.read_csv(PRODUCTS_PATH)

    logger.info(
        "Loaded %d products.",
        len(products),
    )

    return products


def load_executions() -> pd.DataFrame:
    """
    Load Production Executions.
    """

    executions = pd.read_csv(
        PRODUCTION_EXECUTIONS_PATH,
        parse_dates=[
            "execution_start",
            "execution_end",
        ],
    )

    logger.info(
        "Loaded %d executions.",
        len(executions),
    )

    return executions


# ============================================================
# Generate Serial Numbers
# ============================================================

def generate_serial_numbers(
    executions: pd.DataFrame,
    products: pd.DataFrame,
) -> list[SerialNumber]:
    """
    Generate one serial number for each
    manufactured unit.
    """

    serial_numbers: list[SerialNumber] = []

    serial_counter = 1

    product_lookup = (
        products
        .set_index("product_code")
        .to_dict("index")
    )

    for _, execution in executions.iterrows():

        work_order = execution["work_order_id"]

        product_code = execution["product_code"]

        quantity = int(
            execution["quantity"]
        )

        product = product_lookup[
            product_code
        ]

        for unit in range(quantity):

            serial_numbers.append(

                SerialNumber(

                    serial_number=(
                        f"SN-"
                        f"{serial_counter:08d}"
                    ),

                    execution_id=execution[
                        "execution_id"
                    ],

                    work_order_id=work_order,

                    sap_order_number=execution[
                        "sap_order_number"
                    ],

                    product_code=product_code,

                    product_name=product[
                        "product_name"
                    ],

                    production_line=execution[
                        "production_line"
                    ],

                    manufacturing_date=execution[
                        "execution_start"
                    ],

                    status="IN_PRODUCTION",

                )

            )

            serial_counter += 1

    logger.info(
        "Generated %d Serial Numbers.",
        len(serial_numbers),
    )

    return serial_numbers


# ============================================================
# Validation
# ============================================================

def validate(
    serial_numbers: list[SerialNumber],
) -> None:
    """
    Validate generated serial numbers.
    """

    df = pd.DataFrame(
        [asdict(sn) for sn in serial_numbers]
    )

    if df.empty:
        raise ValueError(
            "No serial numbers generated."
        )

    if df["serial_number"].duplicated().any():
        raise ValueError(
            "Duplicate Serial Numbers."
        )

    if df.isnull().any().any():
        raise ValueError(
            "Null values detected."
        )

    logger.info(
        "Serial Number validation successful."
    )

# ============================================================
# Export
# ============================================================

def export(
    serial_numbers: list[SerialNumber],
) -> None:
    """
    Export Serial Numbers to CSV.
    """

    df = pd.DataFrame(
        [asdict(sn) for sn in serial_numbers]
    )

    SERIAL_NUMBERS_PATH.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    df.to_csv(
        SERIAL_NUMBERS_PATH,
        index=False,
    )

    logger.info(
        "Exported %d Serial Numbers.",
        len(df),
    )


# ============================================================
# Summary
# ============================================================

def summary(
    serial_numbers: list[SerialNumber],
) -> None:
    """
    Print generation summary.
    """

    logger.info("========================================")
    logger.info(" Serial Number Generation Summary")
    logger.info("========================================")
    logger.info(
        "Total Serial Numbers : %d",
        len(serial_numbers),
    )

    if serial_numbers:

        logger.info(
            "First Serial Number : %s",
            serial_numbers[0].serial_number,
        )

        logger.info(
            "Last Serial Number  : %s",
            serial_numbers[-1].serial_number,
        )

    logger.info("========================================")


# ============================================================
# Main
# ============================================================

def main() -> None:
    """
    Generate Serial Numbers from Production Executions.
    """

    logger.info("========================================")
    logger.info("Starting Serial Number Generation")
    logger.info("========================================")

    products = load_products()

    executions = load_executions()

    serial_numbers = generate_serial_numbers(
        executions,
        products,
    )

    validate(
        serial_numbers,
    )

    export(
        serial_numbers,
    )

    summary(
        serial_numbers,
    )

    logger.info(
        "Serial Number generation completed successfully."
    )


if __name__ == "__main__":
    main()


