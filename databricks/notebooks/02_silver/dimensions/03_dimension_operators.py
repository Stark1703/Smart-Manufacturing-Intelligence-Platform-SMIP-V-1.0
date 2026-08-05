# Databricks notebook source
"""
========================================================================
SMIP

Silver Layer

Dimension Operators
========================================================================
"""

from pyspark.sql.functions import (
    col,
    trim,
    upper,
    concat_ws,
    monotonically_increasing_id
)

from framework.core.session import spark
from framework.core.configuration import BRONZE_LAYER, SILVER_LAYER
from framework.core.logger import banner, info, success

from framework.io.delta import write_delta
from framework.quality.validation import validate_dataframe

banner("Silver - Dimension Operators")

df = spark.table(f"{BRONZE_LAYER}.operators")

rows = validate_dataframe(df)

info(f"Rows Loaded : {rows}")

df = (

    df

    .dropDuplicates(["operator_id"])

    .withColumn("first_name", trim(col("first_name")))

    .withColumn("last_name", trim(col("last_name")))

    .withColumn("shift", upper(trim(col("shift"))))

    .withColumn(
        "operator_name",
        concat_ws(" ", col("first_name"), col("last_name"))
    )

    .withColumn(
        "operator_key",
        monotonically_increasing_id()
    )

)

df = df.select(

    "operator_key",

    "operator_id",

    "employee_number",

    "operator_name",

    "first_name",

    "last_name",

    "shift",

    "skill_level",

    "primary_machine_type",

    "years_of_experience",

    "mes_authorized",

    "active",

    "ingestion_timestamp",

    "load_date",

    "source_file"

)

write_delta(
    df,
    f"{SILVER_LAYER}.dim_operators"
)

success("dim_operators created successfully.")

display(df)
