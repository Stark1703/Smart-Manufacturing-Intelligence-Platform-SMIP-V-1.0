
"""
generate_operator_master.py

Generate Operator Master.

Author:
Sumanth Vempalle

Version:
1.0.0
"""

from __future__ import annotations

import logging
import random

import pandas as pd

from generator.configs.factory_digital_twin import (
    MachineType,
    Operator,
    OperatorSkill,
    ShiftType,
    to_dict,
)

from generator.configs.paths import OPERATORS_PATH

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)-8s %(message)s",
)

logger = logging.getLogger(__name__)


FIRST_NAMES = [
    "Adam",
    "Martin",
    "Peter",
    "Thomas",
    "Daniel",
    "Lucas",
    "Jan",
    "David",
    "Robert",
    "Michael",
    "Anna",
    "Maria",
    "Laura",
    "Eva",
    "Julia",
    "Petra",
]

LAST_NAMES = [
    "Novak",
    "Svoboda",
    "Horvat",
    "Kovac",
    "Schmidt",
    "Meyer",
    "Huber",
    "Novotny",
    "Kral",
    "Urban",
]


MACHINE_ASSIGNMENTS = [
    MachineType.PRESS_FITTING,
    MachineType.CIRCUIT_BREAKER_ASSEMBLY,
    MachineType.DEAD_TANK_ASSEMBLY,
    MachineType.GIS_ASSEMBLY,
    MachineType.MECHANICAL_TEST,
    MachineType.HIGH_VOLTAGE_TEST,
]

def generate_operators() -> list[Operator]:

    random.seed(42)

    operators = []

    operator_number = 1

    for shift in ShiftType:

        for _ in range(24):

            operators.append(

                Operator(

                    operator_id=f"OP-{operator_number:04d}",

                    first_name=random.choice(FIRST_NAMES),

                    last_name=random.choice(LAST_NAMES),

                    employee_number=f"EMP-{10000+operator_number}",

                    shift=shift,

                    skill_level=random.choice(list(OperatorSkill)),

                    primary_machine_type=random.choice(MACHINE_ASSIGNMENTS),

                    years_of_experience=random.randint(1,15),

                    mes_authorized=True,

                )

            )

            operator_number += 1

    logger.info("Generated %d operators.", len(operators))

    return operators


def validate_operators(operators: list[Operator]) -> None:

    ids = {o.operator_id for o in operators}

    if len(ids) != len(operators):
        raise ValueError("Duplicate Operator IDs.")

    logger.info("Operator validation successful.")



def export_operators(operators: list[Operator]) -> None:

    OPERATORS_PATH.parent.mkdir(parents=True, exist_ok=True)

    pd.DataFrame(to_dict(operators)).to_csv(
        OPERATORS_PATH,
        index=False,
    )

    logger.info("Operator Master exported.")


def main():

    logger.info("Generating Operator Master...")

    operators = generate_operators()

    validate_operators(operators)

    export_operators(operators)

    logger.info("Operator Master generation completed.")


if __name__ == "__main__":
    main()
