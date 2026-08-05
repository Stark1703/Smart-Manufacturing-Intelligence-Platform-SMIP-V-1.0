# Databricks notebook source
"""
========================================================================
Smart Manufacturing Intelligence Platform (SMIP)

Silver Layer

Dimension Products

Author  : Sumanth Vempalle
Version : 1.2.0
========================================================================
"""

# ============================================================================
# Imports
# ============================================================================

from pyspark.sql.functions import *
from pyspark.sql.window import Window

from framework.core.session import spark
from framework.core.configuration import *
from framework.core.logger import *

from framework.io.delta import write_delta

from framework.quality.validation import validate_dataframe


# ============================================================================
# Start
# ============================================================================

banner("Silver Layer - Dimension Products")


# ============================================================================
# Read Bronze Table
# ============================================================================

df = spark.table(
    f"{BRONZE_LAYER}.products"
)

rows = validate_dataframe(df)

info(f"Rows Loaded : {rows}")


# ============================================================================
# Business Transformations
# ============================================================================

window = Window.orderBy("product_id")

df = (

    df

    .dropDuplicates(
        ["product_id"]
    )

    .withColumn(
        "product_name",
        trim(col("product_name"))
    )

    .withColumn(
        "family",
        trim(col("family"))
    )

    .withColumn(
        "product_key",
        row_number().over(window)
    )

)


# ============================================================================
# Reorder Columns
# ============================================================================

df = df.select(

    "product_key",

    "product_id",

    "product_code",

    "product_name",

    "family",

    "rated_voltage_kv",

    "rated_current_a",

    "short_circuit_rating_ka",

    "target_force_kn",

    "force_tolerance_kn",

    "average_cycle_time_sec",

    "dielectric_test_voltage_kv",

    "pressure_test_bar",

    "ingestion_timestamp",

    "load_date",

    "source_file"

)


# ============================================================================
# Write Silver Table
# ============================================================================

write_delta(

    df,

    f"{SILVER_LAYER}.dim_products"

)


success("dim_products created successfully.")


# ============================================================================
# Verification
# ============================================================================

display(df)

display(

    spark.sql(

        f"SELECT COUNT(*) FROM {SILVER_LAYER}.dim_products"

    )

)
