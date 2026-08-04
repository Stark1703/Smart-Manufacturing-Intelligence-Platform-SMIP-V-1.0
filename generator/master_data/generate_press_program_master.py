"""
generate_press_program_master.py

Generate Press Program Master.

Author:
Sumanth Vempalle

Version:
1.0.0
"""

from __future__ import annotations

import logging

import pandas as pd

from generator.configs.factory_digital_twin import (
    MachineType,
    PressProgram,
    ToolType,
    to_dict,
)

from generator.configs.paths import (
    PRODUCTS_PATH,
    PRESS_PROGRAMS_PATH,
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


def generate_press_programs(
    product_df: pd.DataFrame,
) -> list[PressProgram]:
    """
    Generate Press Program Master.

    Assumption:
    Every product has 4 press-fit operations.
    """

    programs: list[PressProgram] = []

    counter = 1

    for _, product in product_df.iterrows():

        target_force = float(product["target_force_kn"])
        tolerance = float(product["force_tolerance_kn"])
        displacement = 25.0
        cycle_time = int(product["average_cycle_time_sec"])

        for operation_number in range(1, 5):

            program = PressProgram(

                program_id=f"PP-{counter:04d}",

                product_code=product["product_code"],

                operation_number=operation_number,

                operation_name=f"PRESS_FIT_{operation_number}",

                machine_type=MachineType.PRESS_FITTING,

                tool_type=ToolType.PRESS_TOOL,

                target_force_kn=target_force,

                force_tolerance_kn=tolerance,

                minimum_force_kn=target_force - tolerance,

                maximum_force_kn=target_force + tolerance,

                target_displacement_mm=round(displacement, 2),

                displacement_tolerance_mm=1.5,

                maximum_cycle_time_sec=cycle_time,

                active=True,
            )

            programs.append(program)

            counter += 1

    logger.info(
        "Generated %d press programs.",
        len(programs),
    )

    return programs


def validate_programs(
    programs: list[PressProgram],
) -> None:

    ids = {p.program_id for p in programs}

    if len(ids) != len(programs):
        raise ValueError("Duplicate Program IDs.")

    logger.info(
        "Press Program validation successful."
    )


def export_programs(
    programs: list[PressProgram],
) -> None:

    PRESS_PROGRAMS_PATH.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    pd.DataFrame(
        to_dict(programs)
    ).to_csv(
        PRESS_PROGRAMS_PATH,
        index=False,
    )

    logger.info(
        "Press Programs exported."
    )


def main():

    logger.info(
        "Generating Press Program Master..."
    )

    product_df = load_products()

    programs = generate_press_programs(
        product_df
    )

    validate_programs(programs)

    export_programs(programs)

    logger.info(
        "Press Program Master generation completed."
    )


if __name__ == "__main__":
    main()