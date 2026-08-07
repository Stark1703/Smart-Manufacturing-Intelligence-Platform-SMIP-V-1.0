# Execution Order

## Overview

The Smart Manufacturing Intelligence Platform follows a sequential execution model.

Each stage depends on the successful completion of the previous stage.

---

## Step 1

Generate Manufacturing Data

Notebook

```
05_generator/
01_run_smip
```

---

## Step 2

Bronze Layer

```
01_bronze/

01_ingest_master_data

02_ingest_transactional_data
```

---

## Step 3

Silver Layer

Execute

### Dimensions

- Products
- Machines
- Operators
- Tools
- Factory

### Facts

- Production
- Press Operations
- Quality
- Force Curves

---

## Step 4

Gold Layer

Run

- Production Summary
- Quality Summary
- OEE Summary
- Traceability Summary
- Executive Summary

---

## Step 5

SQL Views

Execute

```
04_sql/

01_views.sql
```

---

## Step 6

Power BI

Connect to Databricks SQL Warehouse.

Refresh the dashboards.

---

## Execution Flow

```
Generator

↓

Bronze

↓

Silver

↓

Gold

↓

SQL Views

↓

Power BI
```

---

## Related Documentation

- Quick Start