# Databricks notebook source
"""
========================================================================
Smart Manufacturing Intelligence Platform (SMIP)

Silver Layer

Notebook : 04_fact_force_curve

Author  : Sumanth Vempalle
Version : 1.2.0
========================================================================
"""

# ============================================================================
# Imports
# ============================================================================

from pyspark.sql.functions import (
    col,
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

banner("Silver Layer - Fact Force Curve")

# ============================================================================
# Read Bronze
# ============================================================================

curve = spark.table(
    f"{BRONZE_LAYER}.force_curve_points"
)

press = spark.table(
    f"{BRONZE_LAYER}.press_operations"
)

serials = spark.table(
    f"{BRONZE_LAYER}.serial_numbers"
)

validate_dataframe(curve)
validate_dataframe(press)
validate_dataframe(serials)

# ============================================================================
# Read Silver Dimensions
# ============================================================================

products = spark.table(
    f"{SILVER_LAYER}.dim_products"
)

machines = spark.table(
    f"{SILVER_LAYER}.dim_machines"
)

operators = spark.table(
    f"{SILVER_LAYER}.dim_operators"
)

tools = spark.table(
    f"{SILVER_LAYER}.dim_tools"
)

info("Dimensions loaded successfully.")

# ============================================================================
# Build Fact
# ============================================================================

df = (

    curve.alias("fc")

    .join(

        press.alias("po"),

        col("fc.press_operation_id") == col("po.press_operation_id"),

        "left"

    )

    .join(

        serials.alias("sn"),

        col("fc.serial_number") == col("sn.serial_number"),

        "left"

    )

    .join(

        products.alias("dp"),

        col("sn.product_code") == col("dp.product_code"),

        "left"

    )

    .join(

        machines.alias("m"),

        col("po.machine_id") == col("m.machine_id"),

        "left"

    )

    .join(

        operators.alias("o"),

        col("po.operator_id") == col("o.operator_id"),

        "left"

    )

    .join(

        tools.alias("t"),

        col("po.tool_id") == col("t.tool_id"),

        "left"

    )

)

# ============================================================================
# Create Surrogate Key
# ============================================================================

df = df.withColumn(

    "force_curve_key",

    monotonically_increasing_id()

)

# ============================================================================
# Select Columns
# ============================================================================

df = df.select(

    "force_curve_key",

    col("dp.product_key"),

    col("m.machine_key"),

    col("o.operator_key"),

    col("t.tool_key"),

    col("fc.press_operation_id"),

    col("fc.point_id"),

    col("fc.serial_number"),

    col("fc.sample_number"),

    col("fc.timestamp_ms"),

    col("fc.displacement_mm"),

    col("fc.force_kn"),

    col("fc.ingestion_timestamp"),

    col("fc.load_date"),

    col("fc.source_file")

)

# ============================================================================
# Write Delta
# ============================================================================

write_delta(

    df,

    f"{SILVER_LAYER}.fact_force_curve"

)

success("fact_force_curve created successfully.")

# ============================================================================
# Verification
# ============================================================================

display(df.limit(20))

display(

    spark.sql(f"""

        SELECT

            COUNT(*) total_rows,

            COUNT(DISTINCT press_operation_id) distinct_operations

        FROM {SILVER_LAYER}.fact_force_curve

    """)

)

display(

    spark.sql(f"""

        SELECT

            press_operation_id,

            COUNT(*) samples

        FROM {SILVER_LAYER}.fact_force_curve

        GROUP BY press_operation_id

        ORDER BY samples DESC

        LIMIT 20

    """)

) 
