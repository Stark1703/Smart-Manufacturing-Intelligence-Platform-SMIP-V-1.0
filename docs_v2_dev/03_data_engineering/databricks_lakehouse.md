# Databricks Lakehouse

## Overview

The Smart Manufacturing Intelligence Platform (SMIP) uses the Databricks Lakehouse architecture to transform synthetic manufacturing data into business-ready analytical datasets.

The Lakehouse combines the scalability of a data lake with the reliability and performance of a data warehouse, enabling a single platform for data engineering, analytics, and business intelligence.

---

## Architecture

The platform is organized using the Medallion Architecture:

```text
Manufacturing Simulator
        │
        ▼
Unity Catalog Volume
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
        │
        ▼
Power BI
```

---

## Components

### Unity Catalog

Stores raw manufacturing datasets and manages access to Delta tables.

### Bronze Layer

Stores raw manufacturing data exactly as generated.

### Silver Layer

Cleans, validates, and models the data into dimensions and fact tables.

### Gold Layer

Produces business-ready datasets for reporting and dashboarding.

### SQL Layer

Creates curated SQL Views for external BI tools.

### Power BI

Consumes Gold SQL Views for executive and operational dashboards.

---

## Benefits

- Unified analytics platform
- ACID-compliant Delta tables
- Scalable ETL pipelines
- Simplified governance
- Business-ready reporting

---

## Related Documentation

- Bronze Layer
- Silver Layer
- Gold Layer
- Workflows