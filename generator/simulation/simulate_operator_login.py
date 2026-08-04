"""
simulate_operator_login.py

Simulate MES Operator Login Sessions.

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
    OperatorLogin,
)

from generator.configs.paths import (
    OPERATORS_PATH,
    MACHINES_PATH,
    PRODUCTION_EXECUTIONS_PATH,
    OPERATOR_LOGINS_PATH,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)-8s %(message)s",
)

logger = logging.getLogger(__name__)


# ============================================================
# Load Master & Transaction Data
# ============================================================

def load_operators() -> pd.DataFrame:
    """
    Load operator master data.
    """

    df = pd.read_csv(OPERATORS_PATH)

    logger.info(
        "Loaded %d operators.",
        len(df),
    )

    return df


def load_machines() -> pd.DataFrame:
    """
    Load machine master data.
    """

    df = pd.read_csv(MACHINES_PATH)

    logger.info(
        "Loaded %d machines.",
        len(df),
    )

    return df


def load_executions() -> pd.DataFrame:
    """
    Load production executions.
    """

    df = pd.read_csv(
        PRODUCTION_EXECUTIONS_PATH,
        parse_dates=[
            "execution_start",
            "execution_end",
        ],
    )

    logger.info(
        "Loaded %d production executions.",
        len(df),
    )

    return df

# ============================================================
# Simulate Operator Login Sessions
# ============================================================

def simulate_logins(
    operators: pd.DataFrame,
    machines: pd.DataFrame,
    executions: pd.DataFrame,
) -> list[OperatorLogin]:
    """
    Generate one operator login session
    for every production execution.
    """

    logins: list[OperatorLogin] = []

    counter = 1

    operator_ids = operators["operator_id"].tolist()

    machine_ids = machines["machine_id"].tolist()

    for _, execution in executions.iterrows():

        operator_id = random.choice(operator_ids)

        machine_id = random.choice(machine_ids)

        login_time = execution["execution_start"] - timedelta(
            minutes=random.randint(2, 10)
        )

        logout_time = execution["execution_end"] + timedelta(
            minutes=random.randint(1, 5)
        )

        login = OperatorLogin(

            login_id=f"LOGIN-{counter:08d}",

            operator_id=operator_id,

            machine_id=machine_id,

            execution_id=execution["execution_id"],

            work_order_id=execution["work_order_id"],

            shift=execution["planned_shift"],

            login_time=login_time,

            logout_time=logout_time,

            login_status="LOGIN_SUCCESS",

        )

        logins.append(login)

        counter += 1

    logger.info(
        "Generated %d Operator Login sessions.",
        len(logins),
    )

    return logins


# ============================================================
# Validation
# ============================================================

def validate(
    logins: list[OperatorLogin],
) -> None:
    """
    Validate generated operator login sessions.
    """

    df = pd.DataFrame(
        [asdict(x) for x in logins]
    )

    if df.empty:
        raise ValueError(
            "No operator login sessions generated."
        )

    if df["login_id"].duplicated().any():
        raise ValueError(
            "Duplicate Login IDs."
        )

    if (
        df["logout_time"]
        <=
        df["login_time"]
    ).any():
        raise ValueError(
            "Invalid login/logout timestamps."
        )

    logger.info(
        "Operator Login validation successful."
    )


# ============================================================
# Export
# ============================================================

def export(
    logins: list[OperatorLogin],
) -> None:
    """
    Export Operator Login sessions to CSV.
    """

    df = pd.DataFrame(
        [asdict(x) for x in logins]
    )

    OPERATOR_LOGINS_PATH.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    df.to_csv(
        OPERATOR_LOGINS_PATH,
        index=False,
    )

    logger.info(
        "Exported %d Operator Login sessions.",
        len(df),
    )


    # ============================================================
# Summary
# ============================================================

def summary(
    logins: list[OperatorLogin],
) -> None:
    """
    Print a summary of generated operator login sessions.
    """

    logger.info("========================================")
    logger.info(" Operator Login Summary")
    logger.info("========================================")
    logger.info("Login Sessions : %d", len(logins))
    logger.info(
        "Unique Operators : %d",
        len(
            {
                x.operator_id
                for x in logins
            }
        ),
    )
    logger.info(
        "Unique Machines  : %d",
        len(
            {
                x.machine_id
                for x in logins
            }
        ),
    )
    logger.info("========================================")


# ============================================================
# Main
# ============================================================

def main() -> None:
    """
    Simulate MES operator login sessions.
    """

    logger.info("========================================")
    logger.info("Starting Operator Login Simulation")
    logger.info("========================================")

    operators = load_operators()

    machines = load_machines()

    executions = load_executions()

    logins = simulate_logins(
        operators,
        machines,
        executions,
    )

    validate(
        logins,
    )

    export(
        logins,
    )

    summary(
        logins,
    )

    logger.info(
        "Operator Login simulation completed successfully."
    )


if __name__ == "__main__":
    main()