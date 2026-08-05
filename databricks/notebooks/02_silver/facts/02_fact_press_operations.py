# Databricks notebook source
"""
========================================================================
Smart Manufacturing Intelligence Platform (SMIP)

Silver Layer

Notebook : 02_fact_press_operations

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

banner("Silver Layer - Fact Press Operations")

# ============================================================================
# Read Bronze Tables
# ============================================================================

press = spark.table(
    f"{BRONZE_LAYER}.press_operations"
)

serials = spark.table(
    f"{BRONZE_LAYER}.serial_numbers"
)

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

factory = spark.table(
    f"{SILVER_LAYER}.dim_factory"
)

info("Dimensions loaded successfully.")

# ============================================================================
# Build Fact Table
# ============================================================================

df = (

    press.alias("p")

    # ----------------------------------------------------------
    # Product Lookup
    # ----------------------------------------------------------

    .join(

        serials.alias("sn"),

        col("p.serial_number") == col("sn.serial_number"),

        "left"

    )

    .join(

        products.alias("dp"),

        col("sn.product_code") == col("dp.product_code"),

        "left"

    )

    # ----------------------------------------------------------
    # Machine
    # ----------------------------------------------------------

    .join(

        machines.alias("m"),

        col("p.machine_id") == col("m.machine_id"),

        "left"

    )

    # ----------------------------------------------------------
    # Operator
    # ----------------------------------------------------------

    .join(

        operators.alias("o"),

        col("p.operator_id") == col("o.operator_id"),

        "left"

    )

    # ----------------------------------------------------------
    # Tool
    # ----------------------------------------------------------

    .join(

        tools.alias("t"),

        col("p.tool_id") == col("t.tool_id"),

        "left"

    )

    # ----------------------------------------------------------
    # Factory
    # ----------------------------------------------------------

    .join(

        factory.alias("f"),

        col("m.station_id") == col("f.station_id"),

        "left"

    )

)

# ============================================================================
# Business Transformations
# ============================================================================

df = (

    df

    .withColumn(

        "quality_result",

        upper(trim(col("p.quality_result")))

    )

    .withColumn(

        "press_operation_key",

        monotonically_increasing_id()

    )

)

# ============================================================================
# Select Columns
# ============================================================================

df = df.select(

    "press_operation_key",

    col("p.press_operation_id"),

    col("p.serial_number"),

    col("p.execution_id"),

    col("p.work_order_id"),

    col("dp.product_key"),

    col("m.machine_key"),

    col("o.operator_key"),

    col("t.tool_key"),

    col("f.factory_key"),

    col("p.operation_number"),

    col("p.operation_name"),

    col("p.press_program_id"),

    col("p.operation_start"),

    col("p.operation_end"),

    col("p.target_force_kn"),

    col("p.actual_force_kn"),

    col("p.force_deviation_kn"),

    col("p.displacement_mm"),

    col("p.cycle_time_sec"),

    col("quality_result"),

    col("p.ingestion_timestamp"),

    col("p.load_date"),

    col("p.source_file")

)

# ============================================================================
# Remove Duplicates
# ============================================================================

df = df.dropDuplicates(

    ["press_operation_id"]

)

# ============================================================================
# Write Silver
# ============================================================================

write_delta(

    df,

    f"{SILVER_LAYER}.fact_press_operations"

)

success("fact_press_operations created successfully.")

# ============================================================================
# Verification
# ============================================================================

display(df)

display(

    spark.sql(f"""

    SELECT

        COUNT(*) total_rows,

        COUNT(DISTINCT press_operation_id) distinct_operations

    FROM {SILVER_LAYER}.fact_press_operations

    """)

)

display(

    spark.sql(f"""

    SELECT

        quality_result,

        COUNT(*) total

    FROM {SILVER_LAYER}.fact_press_operations

    GROUP BY quality_result

    ORDER BY total DESC

    """)

)

display(

    spark.sql(f"""

    SELECT

        machine_key,

        COUNT(*) operations

    FROM {SILVER_LAYER}.fact_press_operations

    GROUP BY machine_key

    ORDER BY operations DESC

    LIMIT 10

    """)

)
