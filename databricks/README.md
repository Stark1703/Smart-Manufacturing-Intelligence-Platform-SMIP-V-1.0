# Databricks

## Overview

The `databricks` directory contains the notebooks that implement the Smart Manufacturing Intelligence Platform (SMIP V2) using the Databricks Data Intelligence Platform.

The notebooks are organized according to the Medallion Architecture and executed as part of the Lakeflow Declarative Pipeline.

---

## Notebook Structure

```text
databricks/

└── notebooks/

    ├── 00_setup
    ├── 01_bronze
    ├── 02_silver
    ├── 03_dimensions
    ├── 04_facts
    ├── 05_gold
    ├── 06_sql_dashboard
    └── 07_validation
```

---

## Notebook Description

### `00_setup`

Creates and configures the Databricks environment.

- Unity Catalog
- Schema
- Volumes
- Configuration

---

### `01_bronze`

Ingests raw manufacturing events into Bronze Delta tables.

---

### `02_silver`

Cleanses, validates, and standardizes manufacturing events.

---

### `03_dimensions`

Builds conformed Dimension tables used throughout the analytical model.

Examples include:

- Machine Dimension
- Product Dimension
- Material Dimension
- Operator Dimension

---

### `04_facts`

Creates analytical Fact tables.

Examples include:

- Fact Operations
- Fact Production
- Fact Quality
- Fact Materials
- Fact Packaging

---

### `05_gold`

Generates business-ready KPI datasets for reporting.

---

### `06_sql_dashboard`

Contains SQL queries used to build the Executive Dashboard.

---

### `07_validation`

Validates pipeline outputs and verifies data quality across all processing layers.

---

## Execution Order

```text
00_setup

↓

01_bronze

↓

02_silver

↓

03_dimensions

↓

04_facts

↓

05_gold

↓

06_sql_dashboard

↓

07_validation
```

---

## Summary

The notebooks in this directory implement the complete Lakehouse data pipeline, transforming raw manufacturing events into business-ready analytical datasets.