"""
SMIP Validation
"""

from pyspark.sql import DataFrame


def validate_dataframe(
    df: DataFrame,
) -> int:

    rows = df.count()

    if rows == 0:

        raise ValueError(
            "Dataset is empty."
        )

    return rows