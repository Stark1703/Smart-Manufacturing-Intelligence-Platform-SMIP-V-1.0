"""
SMIP Data Ingestion
"""

from pyspark.sql import DataFrame

from framework.core.session import spark

from framework.core.configuration import CSV_OPTIONS


def read_csv(
    path: str,
) -> DataFrame:

    return (

        spark.read

        .options(
            **CSV_OPTIONS
        )

        .csv(path)

    )