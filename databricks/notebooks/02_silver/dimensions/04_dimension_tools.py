# Databricks notebook source
"""
========================================================================
SMIP

Silver Layer

Dimension Tools
========================================================================
"""

from pyspark.sql.functions import (
    col,
    trim,
    upper,
    to_date,
    monotonically_increasing_id
)

from framework.core.session import spark
from framework.core.configuration import BRONZE_LAYER, SILVER_LAYER
from framework.core.logger import banner, info, success

from framework.io.delta import write_delta
from framework.quality.validation import validate_dataframe

banner("Silver - Dimension Tools")

df = spark.table(f"{BRONZE_LAYER}.tools")

rows = validate_dataframe(df)

info(f"Rows Loaded : {rows}")

df = (

    df

    .dropDuplicates(["tool_id"])

    .withColumn("tool_name", trim(col("tool_name")))

    .withColumn("tool_type", trim(col("tool_type")))

    .withColumn("machine_type", trim(col("machine_type")))

    .withColumn("status", upper(trim(col("status"))))

    .withColumn(
        "last_calibration",
        to_date(col("last_calibration"))
    )

    .withColumn(
        "next_calibration",
        to_date(col("next_calibration"))
    )

    .withColumn(
        "tool_key",
        monotonically_increasing_id()
    )

)

df = df.select(

    "tool_key",

    "tool_id",

    "machine_id",

    "tool_name",

    "tool_type",

    "machine_type",

    "calibration_interval_days",

    "last_calibration",

    "next_calibration",

    "status",

    "ingestion_timestamp",

    "load_date",

    "source_file"

)

write_delta(
    df,
    f"{SILVER_LAYER}.dim_tools"
)

success("dim_tools created successfully.")

display(df)
