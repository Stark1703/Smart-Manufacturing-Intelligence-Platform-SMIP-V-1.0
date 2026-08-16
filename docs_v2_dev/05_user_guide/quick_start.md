# Quick Start

## Overview

This guide demonstrates how to run the complete Smart Manufacturing Intelligence Platform from start to finish.

---

## Step 1

Clone the repository.

---

## Step 2

Install Python dependencies.

```bash
pip install -r requirements.txt
```

---

## Step 3

Generate Manufacturing Data

Run:

```
01_run_smip
```

This generates:

- Master Data
- Transactional Data

---

## Step 4

Execute Databricks Pipeline

Run the notebooks in sequence:

```
00_setup

01_bronze

02_silver

03_gold

04_sql
```

---

## Step 5

Create SQL Views

Execute

```
01_views.sql
```

---

## Step 6

Open Power BI

Connect to Databricks SQL Warehouse.

Import:

- vw_production_summary
- vw_quality_summary
- vw_oee_summary
- vw_traceability_summary
- vw_executive_summary

---

## Result

The complete analytics platform is now available.

---

## Related Documentation

- Installation
- Execution Order