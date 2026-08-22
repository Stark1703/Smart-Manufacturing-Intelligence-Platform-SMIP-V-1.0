# Tests

## Overview

The `tests` directory contains validation scripts used to verify the correctness of the Smart Manufacturing Intelligence Platform (SMIP V2).

The tests ensure that manufacturing data is processed accurately across every layer of the Lakehouse architecture.

---

## Directory Structure

```text
tests/

├── bronze/
├── gold/
├── integration/
└── silver/
```

---

## Folder Description

### `bronze/`

Validates raw data ingestion.

Typical checks include:

- File ingestion
- Schema validation
- Record counts
- Null value detection

---

### `silver/`

Verifies data cleansing and standardization.

Typical checks include:

- Data quality rules
- Business validations
- Event transformations

---

### `gold/`

Validates KPI calculations and business metrics.

Typical checks include:

- Aggregations
- KPI accuracy
- Dashboard datasets

---

### `integration/`

Performs end-to-end validation across the complete data pipeline.

Examples include:

- Pipeline execution
- Layer dependencies
- Dataset consistency
- End-to-end workflow validation

---

## Validation Strategy

```text
Raw Events

↓

Bronze Validation

↓

Silver Validation

↓

Dimension & Fact Validation

↓

Gold KPI Validation

↓

Dashboard Validation
```

---

## Summary

The testing framework helps ensure that each stage of the manufacturing analytics pipeline produces reliable, accurate, and consistent datasets for downstream reporting and analysis.