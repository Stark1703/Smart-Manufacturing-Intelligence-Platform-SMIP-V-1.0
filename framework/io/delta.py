"""
SMIP Delta Operations
"""

from pyspark.sql import DataFrame

from framework.core.configuration import DELTA_OPTIONS

from framework.core.session import spark

from pyspark.sql import DataFrame


def read_delta(
    table_name: str,
) -> DataFrame:

    return spark.table(
        table_name
    )

def write_delta(
    df: DataFrame,
    table_name: str,
) -> None:

    (

        df.write

        .format("delta")

        .mode(
            DELTA_OPTIONS["mode"]
        )

        .option(
            "overwriteSchema",
            DELTA_OPTIONS[
                "overwriteSchema"
            ],
        )

        .saveAsTable(
            table_name
        )

    )