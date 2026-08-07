# Medallion Architecture

## Overview

SMIP uses the Databricks Medallion Architecture to progressively improve data quality and prepare manufacturing data for analytics.

---

## Architecture

![Medallion Architecture](../images/architecture/medallion_architecture.png)

---

## Bronze Layer

Stores raw manufacturing datasets exactly as generated.

Characteristics:

- Raw data
- Append-only
- Minimal transformations

---

## Silver Layer

Cleans and enriches Bronze data.

Activities include:

- Validation
- Standardization
- Data Quality Checks
- Dimension Modeling
- Fact Table Creation

---

## Gold Layer

Produces business-ready datasets for reporting.

Examples include:

- Production Summary
- Quality Summary
- OEE Summary
- Traceability Summary
- Executive Summary

---

## Benefits

- Data Quality
- Scalability
- Reusability
- Simplified Reporting
- Improved Performance

---

## Related Documentation

- Bronze Layer
- Silver Layer
- Gold Layer