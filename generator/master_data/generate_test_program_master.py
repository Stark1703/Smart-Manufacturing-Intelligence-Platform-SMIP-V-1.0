
"""
generate_test_program_master.py

Generate Test Program Master.

Author:
Sumanth Vempalle

Version:
1.0.0
"""

from __future__ import annotations

import logging

import pandas as pd

from generator.configs.factory_digital_twin import (
    TestProgram,
    TestType,
    to_dict,
)

from generator.configs.paths import (
    PRODUCTS_PATH,
    TEST_PROGRAMS_PATH,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)-8s %(message)s",
)

logger = logging.getLogger(__name__)


def load_products() -> pd.DataFrame:

    df = pd.read_csv(PRODUCTS_PATH)

    logger.info("Loaded %d products.", len(df))

    return df

def generate_test_programs(
    product_df: pd.DataFrame,
) -> list[TestProgram]:

    programs = []

    counter = 1

    for _, product in product_df.iterrows():

        voltage = product["dielectric_test_voltage_kv"]

        pressure = product["pressure_test_bar"]

        # Mechanical Test
        programs.append(
            TestProgram(
                program_id=f"TP-{counter:04d}",
                product_code=product["product_code"],
                operation_code="OP90",
                test_type=TestType.MECHANICAL,
                test_name="Mechanical Endurance Test",
                target_value=100.0,
                minimum_value=98.0,
                maximum_value=102.0,
                unit="%",
                standard_duration_sec=300,
            )
        )
        counter += 1

        # High Voltage Test
        programs.append(
            TestProgram(
                program_id=f"TP-{counter:04d}",
                product_code=product["product_code"],
                operation_code="OP100",
                test_type=TestType.DIELECTRIC,
                test_name="High Voltage Dielectric Test",
                target_value=voltage,
                minimum_value=voltage * 0.98,
                maximum_value=voltage * 1.02,
                unit="kV",
                standard_duration_sec=420,
            )
        )
        counter += 1

        # Pressure Test
        programs.append(
            TestProgram(
                program_id=f"TP-{counter:04d}",
                product_code=product["product_code"],
                operation_code="OP110",
                test_type=TestType.PRESSURE,
                test_name="Pressure Leak Test",
                target_value=pressure,
                minimum_value=pressure - 0.2,
                maximum_value=pressure + 0.2,
                unit="bar",
                standard_duration_sec=360,
            )
        )
        counter += 1

    logger.info(
        "Generated %d test programs.",
        len(programs),
    )

    return programs

def validate_programs(
    programs: list[TestProgram],
) -> None:

    ids = {p.program_id for p in programs}

    if len(ids) != len(programs):
        raise ValueError("Duplicate Test Program IDs.")

    logger.info("Test Program validation successful.")


def export_programs(
    programs: list[TestProgram],
) -> None:

    TEST_PROGRAMS_PATH.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    pd.DataFrame(
        to_dict(programs)
    ).to_csv(
        TEST_PROGRAMS_PATH,
        index=False,
    )

    logger.info("Test Program Master exported.")

def main():

    logger.info("Generating Test Program Master...")

    products = load_products()

    programs = generate_test_programs(products)

    validate_programs(programs)

    export_programs(programs)

    logger.info(
        "Test Program generation completed."
    )


if __name__ == "__main__":
    main()
