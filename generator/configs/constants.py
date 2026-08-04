
"""
constants.py

Global constants used throughout the Smart Manufacturing Lakehouse project.
"""

# ============================================================
# Factory Information
# ============================================================

FACTORY_NAME = "VoltGrid Manufacturing"

FACTORY_LOCATION = "Brno, Czech Republic"

NUMBER_OF_PRODUCTION_LANES = 6

SHIFTS = [
    "Morning",
    "Evening",
    "Night"
]

# ============================================================
# Product Families
# ============================================================

PRODUCT_FAMILIES = [
    "GIS-72",
    "GIS-145",
    "GIS-245",
    "GIS-420"
]

# ============================================================
# Machine Types
# ============================================================

MACHINE_TYPES = [
    "Press Fitting",
    "Assembly",
    "Mechanical Test",
    "Dielectric Test",
    "Pressure Test"
]

# ============================================================
# Operator Skill Levels
# ============================================================

SKILL_LEVELS = [
    "Junior",
    "Intermediate",
    "Senior"
]

# ============================================================
# Work Order Priorities
# ============================================================

WORK_ORDER_PRIORITIES = [
    "Low",
    "Medium",
    "High",
    "Critical"
]

# ============================================================
# Quality Results
# ============================================================

QUALITY_RESULTS = [
    "PASS",
    "FAIL"
]
