
"""
simulate_testing.py

Simulate Manufacturing Testing.

Author:
Sumanth Vempalle + ChatGPT

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
    TestResult,
    QualityResult,
)

from generator.configs.paths import (
    SERIAL_NUMBERS_PATH,
    TEST_PROGRAMS_PATH,
    TEST_RESULTS_PATH,
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
# Load Data
# ============================================================

def load_serial_numbers() -> pd.DataFrame:

    df = pd.read_csv(
        SERIAL_NUMBERS_PATH,
        parse_dates=[
            "manufacturing_date",
        ],
    )

    logger.info(
        "Loaded %d serial numbers.",
        len(df),
    )

    return df


def load_test_programs() -> pd.DataFrame:

    df = pd.read_csv(
        TEST_PROGRAMS_PATH
    )

    logger.info(
        "Loaded %d test programs.",
        len(df),
    )

    return df


# ============================================================
# Simulation
# ============================================================

def simulate_testing(
    serial_numbers: pd.DataFrame,
    test_programs: pd.DataFrame,
) -> list[TestResult]:

    results: list[TestResult] = []

    counter = 1

    for _, serial in serial_numbers.iterrows():

        programs = test_programs[
            test_programs["product_code"]
            ==
            serial["product_code"]
        ]

        start_time = serial[
            "manufacturing_date"
        ]

        for _, program in programs.iterrows():

            target = float(
                program["target_value"]
            )

            minimum = float(
                program["minimum_value"]
            )

            maximum = float(
                program["maximum_value"]
            )

            measured = random.uniform(
                minimum,
                maximum,
            )

            passed = (
                minimum
                <=
                measured
                <=
                maximum
            )

            result = (
                QualityResult.PASS.value
                if passed
                else QualityResult.FAIL.value
            )

            duration = int(
                program["standard_duration_sec"]
            )

            end_time = (
                start_time +
                timedelta(
                    seconds=duration
                )
            )

            results.append(

                TestResult(

                    test_result_id=f"TEST-{counter:08d}",

                    serial_number=serial[
                        "serial_number"
                    ],

                    execution_id=serial[
                        "execution_id"
                    ],

                    product_code=serial[
                        "product_code"
                    ],

                    test_program_id=program[
                        "program_id"
                    ],

                    test_name=program[
                        "test_name"
                    ],

                    target_value=target,

                    measured_value=round(
                        measured,
                        2,
                    ),

                    unit=program["unit"],

                    result=result,

                    start_time=start_time,

                    end_time=end_time,

                )

            )

            counter += 1

            start_time = end_time

    logger.info(
        "Generated %d Test Results.",
        len(results),
    )

    return results


# ============================================================
# Validation
# ============================================================

def validate(
    results: list[TestResult],
) -> None:

    df = pd.DataFrame(
        [asdict(x) for x in results]
    )

    if df.empty:
        raise ValueError(
            "No test results generated."
        )

    if df[
        "test_result_id"
    ].duplicated().any():

        raise ValueError(
            "Duplicate Test IDs."
        )

    logger.info(
        "Testing validation successful."
    )


# ============================================================
# Export
# ============================================================

def export(
    results: list[TestResult],
) -> None:
    """
    Export Test Results to CSV.
    """

    df = pd.DataFrame(
        [asdict(result) for result in results]
    )

    TEST_RESULTS_PATH.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    df.to_csv(
        TEST_RESULTS_PATH,
        index=False,
    )

    logger.info(
        "Exported %d Test Results.",
        len(df),
    )


# ============================================================
# Summary
# ============================================================

def summary(
    results: list[TestResult],
) -> None:
    """
    Print simulation summary.
    """

    df = pd.DataFrame(
        [asdict(result) for result in results]
    )

    logger.info("========================================")
    logger.info(" Manufacturing Testing Summary")
    logger.info("========================================")
    logger.info(
        "Total Test Results : %d",
        len(df),
    )

    logger.info(
        "Serial Numbers     : %d",
        df["serial_number"].nunique(),
    )

    logger.info(
        "PASS               : %d",
        (df["result"] == "PASS").sum(),
    )

    logger.info(
        "FAIL               : %d",
        (df["result"] == "FAIL").sum(),
    )

    logger.info("========================================")


# ============================================================
# Main
# ============================================================

def main() -> None:
    """
    Simulate all manufacturing tests.
    """

    logger.info("========================================")
    logger.info("Starting Manufacturing Testing")
    logger.info("========================================")

    serial_numbers = load_serial_numbers()

    test_programs = load_test_programs()

    results = simulate_testing(
        serial_numbers,
        test_programs,
    )

    validate(
        results,
    )

    export(
        results,
    )

    summary(
        results,
    )

    logger.info(
        "Manufacturing Testing completed successfully."
    )


if __name__ == "__main__":
    main()
