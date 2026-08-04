
"""
simulate_packaging.py

Simulate Packaging Operations.

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
    Packaging,
    QualityResult,
)

from generator.configs.paths import (
    TEST_RESULTS_PATH,
    PACKAGING_PATH,
)

from generator.configs.simulation_config import (
    RANDOM_SEED,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)-8s %(message)s",
)

logger = logging.getLogger(__name__)

random.seed(RANDOM_SEED)


# ============================================================
# Load Test Results
# ============================================================

def load_test_results() -> pd.DataFrame:

    df = pd.read_csv(
        TEST_RESULTS_PATH,
        parse_dates=[
            "start_time",
            "end_time",
        ],
    )

    logger.info(
        "Loaded %d Test Results.",
        len(df),
    )

    return df


# ============================================================
# Packaging Simulation
# ============================================================

def simulate_packaging(
    test_results: pd.DataFrame,
) -> list[Packaging]:

    packages: list[Packaging] = []

    counter = 1

    grouped = test_results.groupby(
        "serial_number"
    )

    for serial_number, group in grouped:

        execution_id = group.iloc[0][
            "execution_id"
        ]

        product_code = group.iloc[0][
            "product_code"
        ]

        package_start = group[
            "end_time"
        ].max()

        package_end = (
            package_start +
            timedelta(
                seconds=120
            )
        )

        all_pass = (
            group["result"] == QualityResult.PASS.value
        ).all()

        status = (
            "READY_FOR_SHIPMENT"
            if all_pass
            else "HOLD"
        )

        packages.append(

            Packaging(

                package_id=f"PKG-{counter:08d}",

                serial_number=serial_number,

                execution_id=execution_id,

                product_code=product_code,

                package_type="WOODEN_CRATE",

                package_weight_kg=round(
                    random.uniform(
                        220,
                        650,
                    ),
                    2,
                ),

                package_length_mm=random.randint(
                    1800,
                    3200,
                ),

                package_width_mm=random.randint(
                    1200,
                    1800,
                ),

                package_height_mm=random.randint(
                    1500,
                    2600,
                ),

                packaging_start=package_start,

                packaging_end=package_end,

                packaging_status=status,

            )

        )

        counter += 1

    logger.info(
        "Generated %d Packaging Records.",
        len(packages),
    )

    return packages


# ============================================================
# Validation
# ============================================================

def validate(
    packages: list[Packaging],
) -> None:

    df = pd.DataFrame(
        [asdict(x) for x in packages]
    )

    if df.empty:

        raise ValueError(
            "No packaging records generated."
        )

    if df[
        "package_id"
    ].duplicated().any():

        raise ValueError(
            "Duplicate Package IDs."
        )

    logger.info(
        "Packaging validation successful."
    )


# ============================================================
# Export
# ============================================================

def export(
    packages: list[Packaging],
) -> None:

    df = pd.DataFrame(
        [asdict(x) for x in packages]
    )

    PACKAGING_PATH.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    df.to_csv(
        PACKAGING_PATH,
        index=False,
    )

    logger.info(
        "Exported %d Packaging Records.",
        len(df),
    )


# ============================================================
# Summary
# ============================================================

def summary(
    packages: list[Packaging],
) -> None:

    df = pd.DataFrame(
        [asdict(x) for x in packages]
    )

    logger.info("========================================")
    logger.info(" Packaging Summary")
    logger.info("========================================")
    logger.info(
        "Packages Created : %d",
        len(df),
    )

    logger.info(
        "Ready For Shipment : %d",
        (
            df["packaging_status"]
            ==
            "READY_FOR_SHIPMENT"
        ).sum(),
    )

    logger.info(
        "On Hold : %d",
        (
            df["packaging_status"]
            ==
            "HOLD"
        ).sum(),
    )

    logger.info("========================================")


# ============================================================
# Main
# ============================================================

def main() -> None:

    logger.info("========================================")
    logger.info("Starting Packaging Simulation")
    logger.info("========================================")

    test_results = load_test_results()

    packages = simulate_packaging(
        test_results
    )

    validate(
        packages
    )

    export(
        packages
    )

    summary(
        packages
    )

    logger.info(
        "Packaging simulation completed successfully."
    )


if __name__ == "__main__":
    main()
