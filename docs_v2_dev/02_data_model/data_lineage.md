# Data Lineage

## Overview

Data Lineage describes how manufacturing data flows through the Smart Manufacturing Intelligence Platform from generation to business reporting.

---

## Data Flow

```text
Manufacturing Simulator
        │
        ▼
CSV Generation
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

## Bronze Layer

Raw manufacturing datasets are ingested without modification.

---

## Silver Layer

Data is cleaned, validated, standardized, and transformed into dimension and fact tables.

---

## Gold Layer

Business-ready datasets are created for analytics and reporting.

---

## Benefits

- Data traceability
- Data quality
- Simplified debugging
- Improved governance

---

## Related Documentation

- Bronze Layer
- Silver Layer
- Gold Layer