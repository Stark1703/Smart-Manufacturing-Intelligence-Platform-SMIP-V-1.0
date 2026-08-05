"""
SMIP Metadata
"""

from pyspark.sql import DataFrame

from pyspark.sql.functions import (
    current_date,
    current_timestamp,
    lit,
)


def add_audit_columns(
    df: DataFrame,
    source_file: str,
) -> DataFrame:

    return (

        df

        .withColumn(
            "ingestion_timestamp",
            current_timestamp(),
        )

        .withColumn(
            "load_date",
            current_date(),
        )

        .withColumn(
            "source_file",
            lit(source_file),
        )

    )