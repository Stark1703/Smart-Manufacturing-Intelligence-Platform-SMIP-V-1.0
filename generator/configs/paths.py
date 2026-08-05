"""
paths.py

Central file system paths for the Smart Manufacturing Lakehouse.
"""

from pathlib import Path

# ============================================================
# Root Directories
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_ROOT = PROJECT_ROOT / "data"

MASTER_DATA = DATA_ROOT / "master_data"

TRANSACTIONAL_DATA = DATA_ROOT / "transactional_data"

ANALYTICS_DATA = DATA_ROOT / "analytics"

# ============================================================
# Master Data
# ============================================================

PRODUCTS_PATH = MASTER_DATA / "products.csv"

HALLS_PATH = MASTER_DATA / "production_halls.csv"

LINES_PATH = MASTER_DATA / "production_lines.csv"

STATIONS_PATH = MASTER_DATA / "stations.csv"

MACHINES_PATH = MASTER_DATA / "machines.csv"

TOOLS_PATH = MASTER_DATA / "tools.csv"

OPERATORS_PATH = MASTER_DATA / "operators.csv"

OPERATIONS_PATH = MASTER_DATA / "operations.csv"

PRESS_PROGRAMS_PATH = MASTER_DATA / "press_programs.csv"

TEST_PROGRAMS_PATH = MASTER_DATA / "test_programs.csv"

# ============================================================
# Transactional Data
# ============================================================

WORK_ORDERS_PATH = TRANSACTIONAL_DATA / "work_orders.csv"

PRODUCTION_EXECUTIONS_PATH = TRANSACTIONAL_DATA / "production_executions.csv"

SERIAL_NUMBERS_PATH = TRANSACTIONAL_DATA / "serial_numbers.csv"

PRESS_OPERATIONS_PATH = TRANSACTIONAL_DATA / "press_operations.csv"

FORCE_CURVE_POINTS_PATH = TRANSACTIONAL_DATA / "force_curve_points.csv"

TEST_RESULTS_PATH = TRANSACTIONAL_DATA / "test_results.csv"

PACKAGING_PATH = TRANSACTIONAL_DATA / "packaging.csv"

OPERATOR_LOGINS_PATH = TRANSACTIONAL_DATA / "operator_logins.csv"

MATERIAL_SCANS_PATH = TRANSACTIONAL_DATA / "material_scans.csv"


# ============================================================
# Analytics
# ============================================================

ANALYTICS_PATH = ANALYTICS_DATA
