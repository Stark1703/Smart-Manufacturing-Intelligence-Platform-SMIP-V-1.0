"""
simulation_config.py

Central simulation configuration for the Smart Manufacturing Lakehouse.

This module contains all configurable parameters used by the simulation
engine. Changing values here changes the behaviour of the entire factory.

Author:
Sumanth Vempalle

Version:
1.0.0
"""

from __future__ import annotations

from datetime import date, time

# =============================================================================
# Factory Calendar
# =============================================================================

SIMULATION_NAME = "Smart Manufacturing Lakehouse"

SIMULATION_VERSION = "1.0"

START_DATE = date(2026, 1, 5)

SIMULATION_DAYS = 30

WORKING_DAYS = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
]

# =============================================================================
# Production Planning
# =============================================================================

MIN_WORK_ORDERS_PER_DAY = 18

MAX_WORK_ORDERS_PER_DAY = 24

MIN_QUANTITY_PER_ORDER = 1

MAX_QUANTITY_PER_ORDER = 5

PLANNER_NAME = "Production Planner"

ROUTING_VERSION = "RV-001"

# =============================================================================
# Production Shifts
# =============================================================================

SHIFT_TIMES = {

    "Morning": {
        "start": time(7, 0),
        "end": time(15, 0),
    },

    "Evening": {
        "start": time(15, 0),
        "end": time(23, 0),
    },

    "Night": {
        "start": time(23, 0),
        "end": time(7, 0),
    },

}

SHIFT_RELEASE_TIME = {

    "Morning": time(6, 45),

    "Evening": time(14, 45),

    "Night": time(22, 45),

}

# =============================================================================
# Production Lines
# =============================================================================

PRODUCTION_LINES = [

    "LINE-01",
    "LINE-02",
    "LINE-03",
    "LINE-04",
    "LINE-05",
    "LINE-06",

]

# =============================================================================
# Product Planning Weights
# =============================================================================

PRODUCT_SELECTION_WEIGHTS = {

    "GIS-072-2500": 15,
    "GIS-072-3150": 15,

    "GIS-145-3150": 15,
    "GIS-145-4000": 10,

    "GIS-170-4000": 8,

    "GIS-245-3150": 10,
    "GIS-245-4000": 8,

    "GIS-300-4000": 6,

    "GIS-420-4000": 5,
    "GIS-420-5000": 4,

    "GIS-550-5000": 3,

    "GIS-800-5000": 1,

}

# =============================================================================
# Work Order Priorities
# =============================================================================

WORK_ORDER_PRIORITIES = {

    "LOW": 10,

    "NORMAL": 65,

    "HIGH": 20,

    "URGENT": 5,

}

# =============================================================================
# Manufacturing Assumptions
# =============================================================================

PRESS_OPERATIONS_PER_PRODUCT = 4

TEST_OPERATIONS_PER_PRODUCT = 3

PACKAGING_OPERATIONS_PER_PRODUCT = 1

# =============================================================================
# Quality Simulation
# =============================================================================

FIRST_PASS_YIELD = 0.985

PRESS_OPERATION_PASS_RATE = 0.990

MECHANICAL_TEST_PASS_RATE = 0.995

HIGH_VOLTAGE_TEST_PASS_RATE = 0.992

PRESSURE_TEST_PASS_RATE = 0.997

# =============================================================================
# Random Seed
# =============================================================================

RANDOM_SEED = 42

# =============================================================================
# Data Generation
# =============================================================================

EXPORT_CSV = True

EXPORT_PARQUET = False

LOG_LEVEL = "INFO"
