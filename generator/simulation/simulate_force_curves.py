
"""
simulate_force_curves.py

Generate Press Force Curves.

One Press Operation
        ↓
500 Sensor Samples

Author:
Sumanth Vempalle + ChatGPT
Version: 1.0.0
"""

from __future__ import annotations

import logging
import random
from dataclasses import asdict

import pandas as pd

from generator.configs.factory_digital_twin import (
    ForceCurvePoint,
)

from generator.configs.paths import (
    PRESS_OPERATIONS_PATH,
    FORCE_CURVE_POINTS_PATH,
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

SAMPLES_PER_CURVE = 500


# ============================================================
# Load Press Operations
# ============================================================

def load_press_operations() -> pd.DataFrame:

    df = pd.read_csv(PRESS_OPERATIONS_PATH)

    logger.info(
        "Loaded %d press operations.",
        len(df),
    )

    return df


# ============================================================
# Generate Force Curves
# ============================================================

def generate_force_curves(
    press_operations: pd.DataFrame,
) -> list[ForceCurvePoint]:

    points: list[ForceCurvePoint] = []

    point_counter = 1

    for _, operation in press_operations.iterrows():

        target_force = float(
            operation["target_force_kn"]
        )

        displacement_max = float(
            operation["displacement_mm"]
        )

        for sample in range(SAMPLES_PER_CURVE):

            progress = sample / (SAMPLES_PER_CURVE - 1)

            displacement = (
                displacement_max * progress
            )

            if progress <= 0.8:

                force = (
                    target_force *
                    (progress / 0.8)
                )

            else:

                force = (
                    target_force -
                    (
                        (progress - 0.8)
                        * target_force
                        * 0.10
                    )
                )

            noise = random.gauss(0, target_force * 0.005)

            force += noise

            points.append(

                ForceCurvePoint(

                    point_id=f"POINT-{point_counter:010d}",

                    press_operation_id=operation[
                        "press_operation_id"
                    ],

                    serial_number=operation[
                        "serial_number"
                    ],

                    sample_number=sample + 1,

                    timestamp_ms=sample * 10,

                    displacement_mm=round(
                        displacement,
                        3,
                    ),

                    force_kn=round(
                        force,
                        3,
                    ),

                )

            )

            point_counter += 1

    logger.info(
        "Generated %d force curve points.",
        len(points),
    )

    return points


# ============================================================
# Validation
# ============================================================

def validate(
    points: list[ForceCurvePoint],
) -> None:

    df = pd.DataFrame(
        [asdict(p) for p in points]
    )

    if df.empty:

        raise ValueError(
            "No force curve points generated."
        )

    if df["point_id"].duplicated().any():

        raise ValueError(
            "Duplicate point IDs."
        )

    logger.info(
        "Force curve validation successful."
    )


# ============================================================
# Export
# ============================================================

def export(
    points: list[ForceCurvePoint],
) -> None:
    """
    Export force curve points to CSV.
    """

    df = pd.DataFrame(
        [asdict(point) for point in points]
    )

    FORCE_CURVE_POINTS_PATH.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    df.to_csv(
        FORCE_CURVE_POINTS_PATH,
        index=False,
    )

    logger.info(
        "Exported %d force curve points.",
        len(df),
    )


# ============================================================
# Summary
# ============================================================

def summary(
    points: list[ForceCurvePoint],
) -> None:
    """
    Print simulation summary.
    """

    df = pd.DataFrame(
        [asdict(point) for point in points]
    )

    logger.info("========================================")
    logger.info(" Force Curve Simulation Summary")
    logger.info("========================================")
    logger.info(
        "Total Curve Points : %d",
        len(df),
    )

    logger.info(
        "Press Operations   : %d",
        df["press_operation_id"].nunique(),
    )

    logger.info(
        "Serial Numbers     : %d",
        df["serial_number"].nunique(),
    )

    logger.info(
        "Samples / Curve    : %d",
        SAMPLES_PER_CURVE,
    )

    logger.info("========================================")


# ============================================================
# Main
# ============================================================

def main() -> None:
    """
    Generate force curves for every press operation.
    """

    logger.info("========================================")
    logger.info("Starting Force Curve Simulation")
    logger.info("========================================")

    press_operations = load_press_operations()

    points = generate_force_curves(
        press_operations
    )

    validate(
        points
    )

    export(
        points
    )

    summary(
        points
    )

    logger.info(
        "Force Curve simulation completed successfully."
    )


if __name__ == "__main__":
    main()
