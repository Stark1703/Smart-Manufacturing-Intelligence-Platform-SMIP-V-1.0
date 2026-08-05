# Databricks notebook source
"""
========================================================================
Smart Manufacturing Intelligence Platform (SMIP)

Silver Layer

Dimension Factory

Author  : Sumanth Vempalle
Version : 1.2.0
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

banner("Silver Layer - Dimension Factory")

# ============================================================================
# Read Bronze Tables
# ============================================================================

halls = spark.table(f"{BRONZE_LAYER}.production_halls")

lines = spark.table(f"{BRONZE_LAYER}.production_lines")

stations = spark.table(f"{BRONZE_LAYER}.stations")

validate_dataframe(halls)
validate_dataframe(lines)
validate_dataframe(stations)

info("Bronze factory master data loaded successfully.")

# ============================================================================
# Build Factory Hierarchy
# ============================================================================

df = (

    halls.alias("h")

    .join(

        lines.alias("l"),

        col("h.hall_id") == col("l.hall_id"),

        "inner"

    )

    .join(

        stations.alias("s"),

        col("l.line_id") == col("s.line_id"),

        "inner"

    )

)

# ============================================================================
# Business Transformations
# ============================================================================

df = (

    df

    .withColumn(
        "hall_name",
        trim(col("h.hall_name"))
    )

    .withColumn(
        "line_name",
        trim(col("l.line_name"))
    )

    .withColumn(
        "station_code",
        trim(col("s.station_code"))
    )

    .withColumn(
        "station_type",
        upper(trim(col("s.station_type")))
    )

    .withColumn(
        "factory_key",
        monotonically_increasing_id()
    )

)

# ============================================================================
# Select Columns
# ============================================================================

df = df.select(

    "factory_key",

    col("h.hall_id").alias("hall_id"),

    "hall_name",

    col("l.line_id").alias("line_id"),

    "line_name",

    col("l.status").alias("line_status"),

    col("s.station_id").alias("station_id"),

    "station_code",

    "station_type",

    col("s.sequence").alias("station_sequence"),

    col("h.ingestion_timestamp").alias("ingestion_timestamp"),

    col("h.load_date").alias("load_date"),

    col("h.source_file").alias("source_file")

)

# ============================================================================
# Remove Duplicates
# ============================================================================

df = df.dropDuplicates(
    ["station_id"]
)

# ============================================================================
# Write Silver
# ============================================================================

write_delta(

    df,

    f"{SILVER_LAYER}.dim_factory"

)

success("dim_factory created successfully.")

# ============================================================================
# Verification
# ============================================================================

display(df)

display(

    spark.sql(

        f"""

        SELECT

            COUNT(*) AS total_rows

        FROM {SILVER_LAYER}.dim_factory

        """

    )

)

display(

    spark.sql(

        f"""

        SELECT *

        FROM {SILVER_LAYER}.dim_factory

        ORDER BY hall_id, line_id, station_sequence

        """

    )

)
