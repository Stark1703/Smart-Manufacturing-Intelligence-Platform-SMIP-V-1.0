
"""
generate_product_master.py

Generate ERP Product Master data for the Smart Manufacturing Lakehouse.

Author:
Sumanth Vempalle

Version:
1.0.0
"""

from __future__ import annotations

import logging

import pandas as pd

from generator.configs.factory_digital_twin import (
    Product,
    ProductFamily,
    to_dict,
)
from generator.configs.paths import PRODUCTS_PATH

# =============================================================================
# Logging
# =============================================================================

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)-8s %(message)s",
)

logger = logging.getLogger(__name__)

# =============================================================================
# Product Definitions
# =============================================================================

PRODUCT_MASTER = [

    Product(
        "PRD-0001",
        "GIS-072-2500",
        "GIS Bay 72.5 kV / 2500 A",
        ProductFamily.GIS_BAY,
        72.5,
        2500,
        31.5,
        145,
        5,
        35,
        140,
        8,
    ),

    Product(
        "PRD-0002",
        "GIS-072-3150",
        "GIS Bay 72.5 kV / 3150 A",
        ProductFamily.GIS_BAY,
        72.5,
        3150,
        31.5,
        150,
        5,
        36,
        140,
        8,
    ),

    Product(
        "PRD-0003",
        "GIS-145-3150",
        "GIS Bay 145 kV / 3150 A",
        ProductFamily.GIS_BAY,
        145,
        3150,
        40,
        155,
        5,
        40,
        275,
        8,
    ),

    Product(
        "PRD-0004",
        "GIS-145-4000",
        "GIS Bay 145 kV / 4000 A",
        ProductFamily.GIS_BAY,
        145,
        4000,
        40,
        160,
        5,
        42,
        275,
        8,
    ),

    Product(
        "PRD-0005",
        "GIS-170-4000",
        "GIS Bay 170 kV / 4000 A",
        ProductFamily.GIS_BAY,
        170,
        4000,
        40,
        162,
        5,
        43,
        325,
        8,
    ),

    Product(
        "PRD-0006",
        "GIS-245-3150",
        "GIS Bay 245 kV / 3150 A",
        ProductFamily.GIS_BAY,
        245,
        3150,
        50,
        168,
        5,
        46,
        460,
        9,
    ),

    Product(
        "PRD-0007",
        "GIS-245-4000",
        "GIS Bay 245 kV / 4000 A",
        ProductFamily.GIS_BAY,
        245,
        4000,
        50,
        170,
        5,
        47,
        460,
        9,
    ),

    Product(
        "PRD-0008",
        "GIS-300-4000",
        "GIS Bay 300 kV / 4000 A",
        ProductFamily.GIS_BAY,
        300,
        4000,
        50,
        175,
        5,
        50,
        510,
        9,
    ),

    Product(
        "PRD-0009",
        "GIS-420-4000",
        "GIS Bay 420 kV / 4000 A",
        ProductFamily.GIS_BAY,
        420,
        4000,
        63,
        180,
        5,
        55,
        680,
        10,
    ),

    Product(
        "PRD-0010",
        "GIS-420-5000",
        "GIS Bay 420 kV / 5000 A",
        ProductFamily.GIS_BAY,
        420,
        5000,
        63,
        185,
        5,
        58,
        680,
        10,
    ),

    Product(
        "PRD-0011",
        "GIS-550-5000",
        "GIS Bay 550 kV / 5000 A",
        ProductFamily.GIS_BAY,
        550,
        5000,
        63,
        195,
        5,
        62,
        950,
        10,
    ),

    Product(
        "PRD-0012",
        "GIS-800-5000",
        "GIS Bay 800 kV / 5000 A",
        ProductFamily.GIS_BAY,
        800,
        5000,
        63,
        205,
        5,
        70,
        1425,
        11,
    ),
]

# =============================================================================
# Validation
# =============================================================================

def validate_products(products: list[Product]) -> None:

    ids = {p.product_id for p in products}

    if len(ids) != len(products):
        raise ValueError("Duplicate Product IDs detected.")

    codes = {p.product_code for p in products}

    if len(codes) != len(products):
        raise ValueError("Duplicate Product Codes detected.")

    logger.info("Product validation successful.")

# =============================================================================
# Export
# =============================================================================

def export_products(products: list[Product]) -> None:

    PRODUCTS_PATH.parent.mkdir(parents=True, exist_ok=True)

    df = pd.DataFrame(to_dict(products))

    df.to_csv(PRODUCTS_PATH, index=False)

    logger.info("Exported %d products.", len(products))

# =============================================================================
# Main
# =============================================================================

def main():

    logger.info("Generating Product Master...")

    validate_products(PRODUCT_MASTER)

    export_products(PRODUCT_MASTER)

    logger.info("Product Master generation completed.")


if __name__ == "__main__":
    main()
