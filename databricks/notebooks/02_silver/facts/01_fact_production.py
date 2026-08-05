# Databricks notebook source
"""
========================================================================
Smart Manufacturing Intelligence Platform (SMIP)

Silver Layer

Notebook : 01_fact_production

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

from framework.core.configuration import (
    BRONZE_LAYER,
    SILVER_LAYER
)

from framework.core.logger import (
    banner,
    info,
    success
)

from framework.io.delta import write_delta

from framework.quality.validation import validate_dataframe

# ============================================================================
# Start
# ============================================================================

banner("Silver Layer - Fact Production")

# ============================================================================
# Read Bronze Tables
# ============================================================================

work_orders = spark.table(
    f"{BRONZE_LAYER}.work_orders"
)

executions = spark.table(
    f"{BRONZE_LAYER}.production_executions"
)

serials = spark.table(
    f"{BRONZE_LAYER}.serial_numbers"
)

products = spark.table(
    f"{SILVER_LAYER}.dim_products"
)

validate_dataframe(work_orders)
validate_dataframe(executions)
validate_dataframe(serials)
validate_dataframe(products)

info("Bronze tables loaded.")

# ============================================================================
# Build Production Fact
# ============================================================================

df = (

    serials.alias("sn")

    .join(

        executions.alias("ex"),

        "execution_id",

        "left"

    )

    .join(

        work_orders.alias("wo"),

        "work_order_id",

        "left"

    )

    .join(

        products.alias("dp"),

        col("sn.product_code") == col("dp.product_code"),

        "left"

    )

)

# ============================================================================
# Business Transformations
# ============================================================================

df = (

    df

    .withColumn(

        "production_key",

        monotonically_increasing_id()

    )

)

# ============================================================================
# Select Columns
# ============================================================================

df = df.select(

    "production_key",

    col("dp.product_key"),

    col("sn.serial_number"),

    col("sn.product_code"),

    col("sn.product_name"),

    col("sn.execution_id"),

    col("sn.work_order_id"),

    col("sn.sap_order_number"),

    col("ex.quantity"),

    col("ex.plant_code"),

    col("ex.production_line"),

    col("ex.planned_shift"),

    col("sn.manufacturing_date"),

    col("ex.execution_start"),

    col("ex.execution_end"),

    col("sn.status").alias("serial_status"),

    col("sn.ingestion_timestamp"),

    col("sn.load_date"),

    col("sn.source_file")

)

# ============================================================================
# Remove Duplicates
# ============================================================================

df = df.dropDuplicates(
    ["serial_number"]
)

# ============================================================================
# Write Silver
# ============================================================================

write_delta(

    df,

    f"{SILVER_LAYER}.fact_production"

)

success("fact_production created successfully.")

# ============================================================================
# Verification
# ============================================================================

display(df)

display(

    spark.sql(

        f"""

        SELECT

            COUNT(*) AS total_rows

        FROM {SILVER_LAYER}.fact_production

        """

    )

)

display(

    spark.sql(

        f"""

        SELECT *

        FROM {SILVER_LAYER}.fact_production

        LIMIT 20

        """

    )

)
