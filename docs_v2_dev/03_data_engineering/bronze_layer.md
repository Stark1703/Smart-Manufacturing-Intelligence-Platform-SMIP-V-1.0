# Bronze Layer

## Purpose

The Bronze Layer is the landing zone for all generated manufacturing datasets.

It stores raw data without applying business logic or transformations, preserving the original source information for traceability and auditing.

---

## Input

Manufacturing simulator CSV files stored in Unity Catalog Volumes.

Datasets include:

- Products
- Machines
- Operators
- Work Orders
- Production Executions
- Serial Numbers
- Press Operations
- Force Curves
- Test Results
- Material Scans
- Packaging

---

## Processing

The Bronze notebooks:

- Read CSV files
- Infer schema
- Add ingestion timestamps
- Store data as Delta tables

---

## Output

Delta tables under the Bronze schema.

---

## Design Principles

- Append-only
- Immutable raw data
- Minimal transformations
- Full source fidelity

---

## Related Documentation

- Silver Layer
- Databricks Lakehouse