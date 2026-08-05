# Databricks notebook source
"""
========================================================================
Smart Manufacturing Intelligence Platform (SMIP)

Silver Layer

Notebook : 03_fact_quality

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

banner("Silver Layer - Fact Quality")

# ============================================================================
# Read Bronze
# ============================================================================

tests = spark.table(
    f"{BRONZE_LAYER}.test_results"
)

materials = spark.table(
    f"{BRONZE_LAYER}.material_scans"
)

packages = spark.table(
    f"{BRONZE_LAYER}.packaging"
)

serials = spark.table(
    f"{BRONZE_LAYER}.serial_numbers"
)

validate_dataframe(tests)
validate_dataframe(materials)
validate_dataframe(packages)
validate_dataframe(serials)

# ============================================================================
# Read Dimensions
# ============================================================================

products = spark.table(
    f"{SILVER_LAYER}.dim_products"
)

info("Dimensions loaded.")

# ============================================================================
# Build Fact
# ============================================================================

df = (

    tests.alias("t")

    .join(

        serials.alias("sn"),

        col("t.serial_number") == col("sn.serial_number"),

        "left"

    )

    .join(

        materials.alias("ms"),

        col("t.serial_number") == col("ms.serial_number"),

        "left"

    )

    .join(

        packages.alias("pk"),

        col("t.serial_number") == col("pk.serial_number"),

        "left"

    )

    .join(

        products.alias("dp"),

        col("sn.product_code") == col("dp.product_code"),

        "left"

    )

)

# ============================================================================
# Transformations
# ============================================================================

df = (

    df

    .withColumn(

        "quality_key",

        monotonically_increasing_id()

    )

    .withColumn(

        "result",

        upper(trim(col("t.result")))

    )

    .withColumn(

        "scan_status",

        upper(trim(col("ms.scan_status")))

    )

    .withColumn(

        "packaging_status",

        upper(trim(col("pk.packaging_status")))

    )

)

# ============================================================================
# Select Columns
# ============================================================================

df = df.select(

    "quality_key",

    col("dp.product_key"),

    col("t.test_result_id"),

    col("t.serial_number"),

    col("t.execution_id"),

    col("t.product_code"),

    col("t.test_program_id"),

    col("t.test_name"),

    col("t.target_value"),

    col("t.measured_value"),

    col("t.unit"),

    col("result"),

    col("ms.material_number"),

    col("ms.batch_number"),

    col("ms.supplier"),

    col("scan_status"),

    col("pk.package_type"),

    col("pk.package_weight_kg"),

    col("packaging_status"),

    col("t.start_time"),

    col("t.end_time"),

    col("t.ingestion_timestamp"),

    col("t.load_date"),

    col("t.source_file")

)

# ============================================================================
# Remove Duplicates
# ============================================================================

df = df.dropDuplicates(

    ["test_result_id"]

)

# ============================================================================
# Write Silver
# ============================================================================

write_delta(

    df,

    f"{SILVER_LAYER}.fact_quality"

)

success("fact_quality created successfully.")

# ============================================================================
# Verification
# ============================================================================

display(df)

display(

    spark.sql(f"""

        SELECT

            COUNT(*) total_rows,

            COUNT(DISTINCT test_result_id) distinct_tests

        FROM {SILVER_LAYER}.fact_quality

    """)

)

display(

    spark.sql(f"""

        SELECT

            result,

            COUNT(*) total

        FROM {SILVER_LAYER}.fact_quality

        GROUP BY result

        ORDER BY total DESC

    """)

)

display(

    spark.sql(f"""

        SELECT

            supplier,

            COUNT(*) total_tests

        FROM {SILVER_LAYER}.fact_quality

        GROUP BY supplier

        ORDER BY total_tests DESC

    """)

)
