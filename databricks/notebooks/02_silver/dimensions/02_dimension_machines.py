# Databricks notebook source
"""
========================================================================
Smart Manufacturing Intelligence Platform (SMIP)

Silver Layer

Dimension Machines
========================================================================
"""

# ============================================================================
# Imports
# ============================================================================

from pyspark.sql.functions import (
    col,
    trim,
    upper,
    monotonically_increasing_id
)

from framework.core.session import spark
from framework.core.configuration import BRONZE_LAYER, SILVER_LAYER
from framework.core.logger import banner, info, success

from framework.io.delta import write_delta
from framework.quality.validation import validate_dataframe

# ============================================================================
# Start
# ============================================================================

banner("Silver - Dimension Machines")

# ============================================================================
# Read Bronze
# ============================================================================

df = spark.table(f"{BRONZE_LAYER}.machines")

rows = validate_dataframe(df)

info(f"Rows Loaded : {rows}")

# ============================================================================
# Transformations
# ============================================================================

df = (

    df

    .dropDuplicates(["machine_id"])

    .withColumn("machine_name", trim(col("machine_name")))

    .withColumn("machine_type", trim(col("machine_type")))

    .withColumn("manufacturer", trim(col("manufacturer")))

    .withColumn("status", upper(trim(col("status"))))

    .withColumn("machine_key", monotonically_increasing_id())

)

# ============================================================================
# Column Order
# ============================================================================

df = df.select(

    "machine_key",

    "machine_id",

    "line_id",

    "station_id",

    "station_sequence",

    "machine_name",

    "machine_type",

    "manufacturer",

    "status",

    "commissioned_year",

    "ingestion_timestamp",

    "load_date",

    "source_file"

)

# ============================================================================
# Write Silver
# ============================================================================

write_delta(
    df,
    f"{SILVER_LAYER}.dim_machines"
)

success("dim_machines created successfully.")

display(df)
