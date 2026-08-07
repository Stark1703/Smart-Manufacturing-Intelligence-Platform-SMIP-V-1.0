# Databricks Workflows

## Overview

SMIP uses Databricks Workflows to orchestrate the complete data engineering pipeline.

The workflow executes every notebook in the correct sequence, ensuring dependencies are respected and data flows consistently through the Lakehouse.

---

## Workflow Sequence

```text
01_run_smip
        │
        ▼
Bronze Layer
        │
        ▼
Silver Layer
        │
        ▼
Gold Layer
        │
        ▼
SQL Views
```

---

## Pipeline Stages

### Manufacturing Data Generation

Generates all master and transactional datasets.

### Bronze

Ingests raw CSV files into Delta tables.

### Silver

Creates validated dimensions and fact tables.

### Gold

Calculates manufacturing KPIs and analytical summaries.

### SQL

Creates business-facing SQL Views.

---

## Benefits

- Fully automated pipeline
- Reproducible execution
- Dependency management
- Simplified operations

---

## Related Documentation

- Databricks Lakehouse