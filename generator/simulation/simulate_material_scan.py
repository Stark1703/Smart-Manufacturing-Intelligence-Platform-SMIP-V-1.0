"""
simulate_material_scan.py

Simulate Material Barcode / RFID Scan Events.

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
    MaterialScan,
)

from generator.configs.paths import (
    SERIAL_NUMBERS_PATH,
    MATERIAL_SCANS_PATH,
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
    """
    Load generated serial numbers.
    """

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
# Simulate Material Scan Events
# ============================================================

def simulate_material_scans(
    serial_numbers: pd.DataFrame,
) -> list[MaterialScan]:
    """
    Generate one material scan event
    for each manufactured serial number.
    """

    scans: list[MaterialScan] = []

    suppliers = [
        "ABB",
        "Siemens Energy",
        "Schneider Electric",
        "Hitachi Energy",
        "Mitsubishi Electric",
    ]

    counter = 1

    for _, serial in serial_numbers.iterrows():

        scan_time = (
            serial["manufacturing_date"]
            - timedelta(
                minutes=random.randint(5, 45)
            )
        )

        material_scan = MaterialScan(

            scan_id=f"SCAN-{counter:08d}",

            serial_number=serial[
                "serial_number"
            ],

            execution_id=serial[
                "execution_id"
            ],

            product_code=serial[
                "product_code"
            ],

            material_number=(
                f"MAT-{counter:08d}"
            ),

            batch_number=(
                f"BATCH-"
                f"{random.randint(10000,99999)}"
            ),

            supplier=random.choice(
                suppliers
            ),

            scan_timestamp=scan_time,

            scan_status="SUCCESS",

        )

        scans.append(
            material_scan
        )

        counter += 1

    logger.info(
        "Generated %d Material Scan records.",
        len(scans),
    )

    return scans

# ============================================================
# Validation
# ============================================================

def validate(
    scans: list[MaterialScan],
) -> None:
    """
    Validate generated material scan records.
    """

    df = pd.DataFrame(
        [asdict(x) for x in scans]
    )

    if df.empty:
        raise ValueError(
            "No Material Scan records generated."
        )

    if df["scan_id"].duplicated().any():
        raise ValueError(
            "Duplicate Scan IDs."
        )

    if df["serial_number"].duplicated().any():
        raise ValueError(
            "Duplicate Material Scan for Serial Number."
        )

    logger.info(
        "Material Scan validation successful."
    )


# ============================================================
# Export
# ============================================================

def export(
    scans: list[MaterialScan],
) -> None:
    """
    Export Material Scan records to CSV.
    """

    df = pd.DataFrame(
        [asdict(x) for x in scans]
    )

    MATERIAL_SCANS_PATH.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    df.to_csv(
        MATERIAL_SCANS_PATH,
        index=False,
    )

    logger.info(
        "Exported %d Material Scan records.",
        len(df),
    )


# ============================================================
# Summary
# ============================================================

def summary(
    scans: list[MaterialScan],
) -> None:
    """
    Print a summary of generated material scan records.
    """

    logger.info("========================================")
    logger.info(" Material Scan Summary")
    logger.info("========================================")
    logger.info("Material Scans : %d", len(scans))

    logger.info(
        "Unique Materials : %d",
        len(
            {
                x.material_number
                for x in scans
            }
        ),
    )

    logger.info(
        "Unique Suppliers : %d",
        len(
            {
                x.supplier
                for x in scans
            }
        ),
    )

    logger.info("========================================")


# ============================================================
# Main
# ============================================================

def main() -> None:
    """
    Simulate material barcode/RFID scan events.
    """

    logger.info("========================================")
    logger.info("Starting Material Scan Simulation")
    logger.info("========================================")

    serial_numbers = load_serial_numbers()

    scans = simulate_material_scans(
        serial_numbers,
    )

    validate(
        scans,
    )

    export(
        scans,
    )

    summary(
        scans,
    )

    logger.info(
        "Material Scan simulation completed successfully."
    )


if __name__ == "__main__":
    main()