"""
======================================================================
Smart Manufacturing Intelligence Platform (SMIP)

Framework Configuration

Author  : Sumanth Vempalle
Version : 1.2.0
======================================================================
"""

# ======================================================================
# Unity Catalog
# ======================================================================

CATALOG = "smip"

# ======================================================================
# Schemas
# ======================================================================

BRONZE_SCHEMA = "bronze"

SILVER_SCHEMA = "silver"

GOLD_SCHEMA = "gold"

REFERENCE_SCHEMA = "reference"

# ======================================================================
# Volume
# ======================================================================

VOLUME = "source_data"

# ======================================================================
# Source Directories
# ======================================================================

MASTER_DATA_FOLDER = "master_data"

TRANSACTIONAL_DATA_FOLDER = "transactional_data"

REFERENCE_DATA_FOLDER = "reference_data"

ARCHIVE_FOLDER = "archive"

# ======================================================================
# Volume Paths
# ======================================================================

MASTER_DATA_PATH = (
    f"/Volumes/{CATALOG}/{BRONZE_SCHEMA}/{VOLUME}/{MASTER_DATA_FOLDER}"
)

TRANSACTIONAL_DATA_PATH = (
    f"/Volumes/{CATALOG}/{BRONZE_SCHEMA}/{VOLUME}/{TRANSACTIONAL_DATA_FOLDER}"
)

REFERENCE_DATA_PATH = (
    f"/Volumes/{CATALOG}/{BRONZE_SCHEMA}/{VOLUME}/{REFERENCE_DATA_FOLDER}"
)

ARCHIVE_PATH = (
    f"/Volumes/{CATALOG}/{BRONZE_SCHEMA}/{VOLUME}/{ARCHIVE_FOLDER}"
)

# ======================================================================
# Delta Layer Names
# ======================================================================

BRONZE_LAYER = f"{CATALOG}.{BRONZE_SCHEMA}"

SILVER_LAYER = f"{CATALOG}.{SILVER_SCHEMA}"

GOLD_LAYER = f"{CATALOG}.{GOLD_SCHEMA}"

REFERENCE_LAYER = f"{CATALOG}.{REFERENCE_SCHEMA}"

# ======================================================================
# Master Data Registry
# ======================================================================

MASTER_DATASETS = {

    "products": "products.csv",

    "machines": "machines.csv",

    "operators": "operators.csv",

    "operations": "operations.csv",

    "press_programs": "press_programs.csv",

    "production_halls": "production_halls.csv",

    "production_lines": "production_lines.csv",

    "stations": "stations.csv",

    "test_programs": "test_programs.csv",

    "tools": "tools.csv",

}

# ======================================================================
# Transactional Data Registry
# ======================================================================

TRANSACTIONAL_DATASETS = {

    "work_orders": "work_orders.csv",

    "production_executions": "production_executions.csv",

    "serial_numbers": "serial_numbers.csv",

    "press_operations": "press_operations.csv",

    "force_curve_points": "force_curve_points.csv",

    "test_results": "test_results.csv",

    "packaging": "packaging.csv",

    "material_scans": "material_scans.csv",

    "operator_logins": "operator_logins.csv",

}

# ======================================================================
# CSV Read Options
# ======================================================================

CSV_OPTIONS = {

    "header": "true",

    "inferSchema": "true",

    "escape": "\"",

    "multiLine": "false",

}

# ======================================================================
# Delta Write Options
# ======================================================================

DELTA_OPTIONS = {

    "mode": "overwrite",

    "overwriteSchema": "true",

}

# ======================================================================
# Audit Columns
# ======================================================================

AUDIT_COLUMNS = [

    "ingestion_timestamp",

    "load_date",

    "source_file",

]

# ======================================================================
# Data Quality Thresholds
# ======================================================================

ALLOW_EMPTY_DATASET = False

ALLOW_DUPLICATES = False