# Databricks Setup

## Overview

This guide explains how to configure Databricks for the Smart Manufacturing Intelligence Platform (SMIP).

The platform uses Databricks to ingest manufacturing data, process it through the Medallion Architecture, expose analytical SQL Views, and serve Power BI dashboards.

---

# Prerequisites

Before starting, ensure you have:

- A Databricks Workspace
- Unity Catalog enabled
- A SQL Warehouse
- Python simulator executed successfully
- Power BI Desktop (optional)

---

# Repository Structure

Import the notebooks located in:

```
databricks/notebooks/
```

The notebooks are organized as:

```
00_setup
01_bronze
02_silver
03_gold
04_sql
05_generator
06_exports
```

---

# Step 1 – Create a Catalog

Create a Unity Catalog named:

```
smip
```

---

# Step 2 – Create Schemas

Create the following schemas:

```
bronze

silver

gold
```

---

# Step 3 – Create a Volume

Inside the catalog create a volume.

Example:

```
Catalog

└── smip

      └── raw_data
```

This volume stores all generated CSV files.

---

# Step 4 – Upload Manufacturing Data

Run

```
01_run_smip
```

This generates:

- Master Data
- Transactional Data

Upload the generated CSV files into the Unity Catalog Volume.

---

# Step 5 – Configure Environment

Execute

```
00_setup/

01_environment_setup
```

This notebook configures:

- Catalog
- Schemas
- Spark Session
- Paths

---

# Step 6 – Execute Bronze Layer

Run:

```
01_ingest_master_data

02_ingest_transactional_data
```

Output:

Raw Delta Tables.

---

# Step 7 – Execute Silver Layer

Run all Dimension notebooks:

- Products
- Machines
- Operators
- Tools
- Factory

Run all Fact notebooks:

- Production
- Press Operations
- Quality
- Force Curves

Output:

Validated Dimension and Fact Tables.

---

# Step 8 – Execute Gold Layer

Run:

- Production Summary
- Quality Summary
- OEE Summary
- Traceability Summary
- Executive Summary

Output:

Business-ready KPI tables.

---

# Step 9 – Create SQL Views

Execute:

```
04_sql/

01_views.sql
```

Views created:

- vw_production_summary
- vw_quality_summary
- vw_oee_summary
- vw_traceability_summary
- vw_executive_summary

---

# Step 10 – Start SQL Warehouse

Open:

```
Compute

↓

SQL Warehouse
```

Start the warehouse.

---

# Step 11 – Connect Power BI

Open Power BI Desktop.

Choose:

```
Get Data

↓

Azure

↓

Azure Databricks
```

Enter:

- Server Hostname
- HTTP Path
- Personal Access Token

---

# Step 12 – Import SQL Views

Import:

- vw_production_summary
- vw_quality_summary
- vw_oee_summary
- vw_traceability_summary
- vw_executive_summary

---

# Step 13 – Refresh Dashboards

After the Lakehouse pipeline completes:

```
Refresh
```

Power BI automatically loads the latest Gold Layer data.

No CSV exports are required.

---

# Complete Data Flow

```
Python Generator
        │
        ▼
CSV Files
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
SQL Warehouse
        │
        ▼
Power BI
```

---

# Troubleshooting

### Bronze tables empty

Verify CSV files were uploaded correctly.

---

### Silver notebooks fail

Verify Bronze notebooks completed successfully.

---

### Gold tables empty

Ensure Silver Fact tables exist.

---

### SQL Views missing

Execute:

```
01_views.sql
```

again.

---

### Power BI connection fails

Verify:

- SQL Warehouse is running
- Server Hostname
- HTTP Path
- Personal Access Token

---

## Related Documentation

- Installation
- Execution Order
- Databricks Lakehouse
- Power BI Overview