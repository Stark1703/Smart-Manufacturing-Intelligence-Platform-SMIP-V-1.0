# 05 — Troubleshooting

## Introduction

This document provides solutions to the most common issues encountered when deploying, executing, and operating the Smart Manufacturing Intelligence Platform (SMIP) V2.

The troubleshooting procedures described here cover the complete Lakehouse workflow, including repository deployment, Unity Catalog configuration, Lakeflow Declarative Pipelines, Delta tables, and the Databricks SQL Executive Dashboard.

Whenever possible, begin troubleshooting at the earliest stage of the pipeline, as downstream datasets depend on the successful completion of upstream processing.

---

# Troubleshooting Strategy

The recommended troubleshooting workflow is:

```text
Repository

↓

Environment

↓

Setup Notebook

↓

Lakeflow Pipeline

↓

Delta Tables

↓

Gold KPIs

↓

Executive Dashboard
```

Always resolve issues in this order.

---

# Common Issues

## 1. Repository Not Available

### Symptoms

- Project notebooks do not appear in Databricks Repos.
- Missing project folders.
- Git synchronization fails.

### Possible Causes

- Incorrect Git branch.
- Repository not cloned.
- Git authentication issue.

### Resolution

Verify that the correct repository has been cloned.

Repository:

```text
Smart-Manufacturing-Intelligence-Platform-SMIP-V-1.0
```

Branch:

```text
databricks-v2
```

Refresh the Databricks Repo after synchronization.

---

## 2. Setup Notebook Fails

### Symptoms

- Setup notebook terminates with errors.
- Catalog or schema cannot be created.

### Possible Causes

- Insufficient permissions.
- Unity Catalog unavailable.
- Existing objects with conflicting names.

### Resolution

Verify:

- Workspace permissions
- Unity Catalog access
- Existing catalog:

```text
smip_v2
```

Schema:

```text
manufacturing
```

Run the setup notebook again after correcting the issue.

---

## 3. Pipeline Will Not Start

### Symptoms

- Pipeline remains in Pending state.
- Execution never begins.
- Pipeline fails immediately.

### Possible Causes

- Missing setup configuration.
- Compute unavailable.
- Invalid notebook path.

### Resolution

Verify:

- Setup notebook completed successfully.
- Pipeline references the correct notebook folders.
- Compute resources are available.
- Lakeflow pipeline configuration is valid.

---

## 4. Bronze Tables Are Empty

### Symptoms

```text
bronze_raw_events

manufacturing_events
```

contain zero records.

### Possible Causes

- No JSON files available.
- Incorrect Volume path.
- File permissions.

### Resolution

Verify that manufacturing events exist in:

```text
/Volumes/smip_v2/manufacturing/raw_data/
```

Confirm that the generator has successfully produced JSON files before starting the pipeline.

---

## 5. Silver Tables Not Created

### Symptoms

Tables such as:

```text
parsed_events

operation_events

quality_events
```

are missing.

### Possible Causes

- Bronze ingestion failed.
- Invalid JSON structure.
- Pipeline validation failure.

### Resolution

Verify:

- Bronze tables contain data.
- JSON files are valid.
- Pipeline execution completed without errors.

Review Lakeflow execution logs for failed expectations.

---

## 6. Dimension Tables Missing

### Symptoms

Dimension tables are not generated.

Examples:

```text
machine_dimension

product_dimension

material_dimension
```

### Possible Causes

- Silver tables missing.
- Pipeline interrupted.
- Upstream validation failure.

### Resolution

Confirm that all Silver tables have been successfully created before the Dimension notebooks execute.

---

## 7. Fact Tables Missing

### Symptoms

Fact tables are unavailable.

Examples:

```text
fact_operations

fact_quality

fact_materials

fact_packaging

fact_production
```

### Possible Causes

- Dimension tables missing.
- Join failures.
- Pipeline interruption.

### Resolution

Verify that:

- Silver tables exist.
- Dimension tables exist.
- Pipeline completed successfully.

---

## 8. Gold KPI Tables Not Generated

### Symptoms

The following tables are missing:

```text
machine_kpis

quality_kpis

production_kpis

material_kpis

packaging_kpis

factory_dashboard
```

### Possible Causes

- Fact tables unavailable.
- Gold notebooks failed.
- Pipeline stopped before Gold layer.

### Resolution

Verify that all Fact tables contain records.

Restart the pipeline from the Gold stage if required.

---

## 9. SQL Dashboard Displays No Data

### Symptoms

The Executive Dashboard loads but visualizations are empty.

### Possible Causes

- Gold tables are empty.
- SQL Warehouse is stopped.
- Dashboard queries cannot access Unity Catalog.

### Resolution

Verify:

- SQL Warehouse is running.
- Gold KPI tables contain data.
- Dashboard queries reference:

```sql
smip_v2.manufacturing
```

Refresh the dashboard after the pipeline finishes.

---

## 10. SQL Query Returns No Results

### Symptoms

Queries execute successfully but return zero rows.

### Possible Causes

- Pipeline has not completed.
- Wrong schema selected.
- Empty Gold tables.

### Resolution

Verify the active catalog:

```sql
USE CATALOG smip_v2;
```

Verify the schema:

```sql
USE SCHEMA manufacturing;
```

Run:

```sql
SHOW TABLES;
```

Confirm that all expected datasets are present.

---

# Pipeline Validation Checklist

A successful execution should produce the following layers.

| Layer | Expected Result |
|--------|-----------------|
| Bronze | Manufacturing events ingested |
| Silver | Parsed manufacturing events |
| Dimensions | Business entities created |
| Facts | Analytical datasets available |
| Gold | KPI tables generated |
| SQL Dashboard | Visualizations populated |

If one layer fails, all downstream layers should be investigated.

---

# Useful Validation Queries

Verify Bronze:

```sql
SELECT COUNT(*)
FROM smip_v2.manufacturing.bronze_raw_events;
```

Verify Operations:

```sql
SELECT COUNT(*)
FROM smip_v2.manufacturing.fact_operations;
```

Verify Quality:

```sql
SELECT COUNT(*)
FROM smip_v2.manufacturing.fact_quality;
```

Verify Production:

```sql
SELECT COUNT(*)
FROM smip_v2.manufacturing.fact_production;
```

Verify Dashboard Dataset:

```sql
SELECT *
FROM smip_v2.manufacturing.factory_dashboard;
```

These queries provide a quick health check of the analytical pipeline.

---

# Best Practices

To ensure reliable operation:

- Execute the Setup notebook before deploying the pipeline.
- Verify Unity Catalog permissions.
- Store manufacturing events only in the configured Unity Catalog Volume.
- Validate Bronze tables before investigating downstream layers.
- Monitor Lakeflow execution after each deployment.
- Confirm Gold KPI tables before opening the Executive Dashboard.

Following these practices reduces deployment issues and simplifies troubleshooting.

---

# Summary

Most issues encountered within SMIP V2 originate from incomplete environment configuration, missing raw manufacturing events, or interruptions during pipeline execution.

By validating each processing layer sequentially—from Bronze ingestion through Gold KPI generation—users can quickly identify the source of a problem and restore the platform to a fully operational state.

The troubleshooting procedures described in this guide provide a structured approach for maintaining a reliable manufacturing analytics platform built on Databricks Lakehouse technologies.

---

# Chapter Complete

The **User Guide** has described the complete operational workflow of SMIP V2, including:

- Environment preparation
- Platform deployment
- Pipeline execution
- Dashboard usage
- Operational troubleshooting

Together, these documents enable users to successfully deploy, operate, and maintain the Smart Manufacturing Intelligence Platform within the Databricks ecosystem.