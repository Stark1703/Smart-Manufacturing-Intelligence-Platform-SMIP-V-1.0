# 06 — User Guide

## Overview

This chapter provides practical guidance for deploying, configuring, and operating the Smart Manufacturing Intelligence Platform (SMIP) V2.

Unlike the previous chapters, which focus on architecture and implementation, the User Guide explains how to install the platform, execute the Lakeflow pipeline, access the analytical datasets, and interact with the Databricks SQL Dashboard.

The guide is intended for data engineers, analytics engineers, and technical users responsible for deploying or maintaining the platform.

---

# Purpose

The objectives of this guide are to:

- Prepare the required environment
- Deploy the SMIP V2 project
- Execute the Lakeflow pipeline
- Validate successful execution
- Access the SQL Dashboard
- Troubleshoot common issues

Following this guide enables users to reproduce the complete manufacturing analytics pipeline.

---

# User Workflow

```text
Clone Repository

↓

Configure Databricks

↓

Deploy Notebooks

↓

Run Setup

↓

Start Lakeflow Pipeline

↓

Validate Tables

↓

Open SQL Dashboard

↓

Analyze Manufacturing KPIs
```

---

# Prerequisites

Before using SMIP V2, users should have access to:

- Databricks Workspace
- Unity Catalog
- SQL Warehouse
- Lakeflow Declarative Pipelines
- Git repository
- Python 3.x
- Appropriate Databricks permissions

---

# Guide Structure

| Document | Description |
|----------|-------------|
| **01_environment_setup.md** | Configure the Databricks environment |
| **02_deployment.md** | Deploy SMIP V2 into the workspace |
| **03_running_the_pipeline.md** | Execute the complete Lakeflow pipeline |
| **04_dashboard_usage.md** | Use the Databricks SQL Dashboard |
| **05_troubleshooting.md** | Resolve common deployment and execution issues |

---

# Expected Outcomes

After completing this guide, users will be able to:

- Configure the Databricks environment
- Deploy SMIP V2
- Execute the complete pipeline
- Validate pipeline execution
- Explore manufacturing data
- Use the Executive Dashboard
- Troubleshoot common issues

---

# Summary

This chapter provides the operational knowledge required to install, execute, and use the Smart Manufacturing Intelligence Platform.

While previous chapters explain how the platform was designed and implemented, the User Guide focuses on day-to-day operation, enabling users to successfully deploy and maintain SMIP V2 within a Databricks environment.

---

# Next Section

## 01 — Environment Setup

The next document explains how to prepare the Databricks workspace, configure Unity Catalog, and verify that all required platform components are available before deploying SMIP V2.