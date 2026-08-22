# Data

## Overview

The `data` directory contains the sample datasets used by the Smart Manufacturing Intelligence Platform (SMIP V2).

The datasets represent the input to the manufacturing analytics pipeline and are organized according to their role within the Lakehouse architecture.

---

## Directory Structure

```text
data/

├── bronze/
├── master_data/
├── silver/
└── transactional_data/
```

---

## Folder Description

### `bronze/`

Contains raw manufacturing events in their original format before any transformations are applied.

Examples include:

- JSON event files
- Raw ingestion data
- Source extracts

---

### `master_data/`

Contains reference datasets shared across the platform.

Examples include:

- Products
- Machines
- Operators
- Suppliers
- Materials

These datasets provide the business context required during data enrichment.

---

### `silver/`

Contains cleansed and standardized datasets generated during intermediate processing.

Typical transformations include:

- Data validation
- Schema normalization
- Event parsing
- Business rule application

---

### `transactional_data/`

Contains simulated manufacturing transactions produced by the Manufacturing Event Generator.

Examples include:

- Work Orders
- Production Executions
- Manufacturing Operations
- Quality Inspections
- Material Scans
- Packaging Events

---

## Role in the Pipeline

```text
Manufacturing Event Generator

↓

Transactional Data

↓

Bronze Layer

↓

Silver Layer

↓

Dimensions

↓

Facts

↓

Gold KPIs
```

---

## Summary

The `data` directory provides the sample datasets used to demonstrate the end-to-end manufacturing analytics workflow implemented in SMIP V2.