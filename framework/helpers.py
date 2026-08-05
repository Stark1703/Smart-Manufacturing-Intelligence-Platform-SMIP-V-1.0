"""
SMIP Helper Functions
"""

from pyspark.sql import DataFrame
from pyspark.sql.functions import col, trim, row_number
from pyspark.sql.window import Window


def trim_string_columns(df: DataFrame) -> DataFrame:
    """
    Trim whitespace from all string columns.
    """

    for field in df.schema.fields:

        if field.dataType.simpleString() == "string":

            df = df.withColumn(
                field.name,
                trim(col(field.name))
            )

    return df


def add_surrogate_key(
    df: DataFrame,
    business_key: str,
    surrogate_key: str,
) -> DataFrame:

    window = Window.orderBy(
        business_key
    )

    return df.withColumn(
        surrogate_key,
        row_number().over(window)
    )


def remove_duplicates(
    df: DataFrame,
    business_key: str,
) -> DataFrame:

    return df.dropDuplicates(
        [business_key]
    )