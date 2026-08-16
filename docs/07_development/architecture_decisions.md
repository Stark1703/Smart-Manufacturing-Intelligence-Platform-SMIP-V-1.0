# 02 — Architecture Decisions

## Introduction

Every software project involves architectural decisions that influence scalability, maintainability, performance, and future extensibility.

During the development of the Smart Manufacturing Intelligence Platform (SMIP) V2, several important design decisions were made to transform the project from a local streaming prototype into a modern Lakehouse-based analytics platform.

This document explains the rationale behind these decisions and the benefits they provide.

---

# Decision 1 — Simulate Manufacturing Data

## Challenge

Access to real manufacturing production data is often restricted due to confidentiality, intellectual property, and cybersecurity requirements.

## Decision

Develop a configurable manufacturing event generator capable of producing realistic production events.

## Benefits

- Independent development
- Repeatable testing
- Scalable datasets
- Reproducible experiments
- Safe demonstration environment

---

# Decision 2 — Event-Driven Architecture

## Challenge

Manufacturing systems continuously generate operational events.

## Decision

Model the manufacturing process as a sequence of events rather than static records.

Examples include:

- Work Order Created
- Execution Started
- Operation Completed
- Quality Inspection
- Material Scanned
- Packaging Completed

## Benefits

- Represents real factory behavior
- Supports streaming analytics
- Enables event traceability
- Easily extensible

---

# Decision 3 — Apache Kafka for Local Development

## Challenge

The platform required a mechanism to stream manufacturing events in real time during local development.

## Decision

Use Apache Kafka as the event streaming platform in the `v2.0-dev` branch.

## Benefits

- Real-time event streaming
- Industry-standard messaging platform
- Decoupled event producers and consumers
- Easy simulation of manufacturing activity

Kafka was retained for local development, while Databricks Auto Loader and Lakeflow were adopted for the cloud implementation.

---

# Decision 4 — Medallion Architecture

## Challenge

Raw manufacturing data should not be transformed directly into analytical reports.

## Decision

Adopt the Medallion Architecture.

```text
Bronze

↓

Silver

↓

Dimensions

↓

Facts

↓

Gold
```

## Benefits

- Layered processing
- Improved maintainability
- Better data quality
- Clear separation of responsibilities
- Simplified debugging

---

# Decision 5 — Databricks Lakehouse

## Challenge

The local Spark implementation required manual infrastructure management and limited governance.

## Decision

Migrate the analytical platform to Databricks.

## Benefits

- Managed infrastructure
- Delta Lake
- Unity Catalog
- Lakeflow Declarative Pipelines
- Databricks SQL
- Enterprise governance

---

# Decision 6 — Delta Lake

## Challenge

Analytical datasets require reliable storage with transactional guarantees.

## Decision

Store all analytical datasets as Delta tables.

## Benefits

- ACID transactions
- Schema enforcement
- Efficient queries
- Reliable incremental processing

---

# Decision 7 — Unity Catalog

## Challenge

Manufacturing datasets require centralized governance.

## Decision

Use Unity Catalog to manage:

- Catalog
- Schema
- Volumes
- Permissions
- Metadata

## Benefits

- Centralized governance
- Consistent naming
- Secure access
- Simplified administration

---

# Decision 8 — Lakeflow Declarative Pipelines

## Challenge

Managing notebook execution manually becomes increasingly complex as the pipeline grows.

## Decision

Use Lakeflow Declarative Pipelines.

Instead of defining notebook execution order manually, datasets declare their dependencies and Lakeflow automatically orchestrates execution.

## Benefits

- Automatic dependency resolution
- Incremental processing
- Simplified orchestration
- Reduced operational complexity

---

# Decision 9 — Star Schema

## Challenge

Operational event data is not optimized for business reporting.

## Decision

Create Dimension and Fact tables using a Star Schema.

Dimensions:

- Machine
- Operator
- Product
- Material

Facts:

- Operations
- Quality
- Production
- Materials
- Packaging

## Benefits

- Simplified reporting
- Better query performance
- Reduced redundancy
- Standard analytical model

---

# Decision 10 — Gold KPI Layer

## Challenge

Business dashboards should not calculate metrics directly from detailed Fact tables.

## Decision

Precompute manufacturing KPIs in the Gold layer.

Examples:

- Machine KPIs
- Production KPIs
- Quality KPIs
- Material KPIs
- Packaging KPIs

## Benefits

- Faster dashboards
- Consistent business metrics
- Simplified SQL
- Reusable analytical datasets

---

# Decision 11 — Single Executive Dashboard

## Challenge

Business users need a consolidated view of factory performance.

## Decision

Develop a single Executive Dashboard using Databricks SQL.

The dashboard combines:

- Factory Summary
- Machine Performance
- Production Analysis
- Quality Monitoring
- Material Traceability
- Packaging Performance

## Benefits

- Centralized reporting
- Simplified navigation
- Unified business view
- Executive-friendly interface

---

# Decision 12 — Comprehensive Documentation

## Challenge

Complex data engineering projects are difficult to maintain without proper documentation.

## Decision

Document every major component of the platform, including:

- Architecture
- Data Model
- Data Engineering
- Business Intelligence
- User Guide
- Development Process

## Benefits

- Easier onboarding
- Improved maintainability
- Better knowledge transfer
- Reproducible implementation

---

# Summary

The architectural decisions made during the development of SMIP V2 were guided by four primary objectives:

- Scalability
- Maintainability
- Reliability
- Business value

Each decision contributed to transforming the project from a local streaming prototype into a modern manufacturing analytics platform built on the Databricks Lakehouse architecture.

Together, these decisions establish a strong technical foundation for future enhancements such as predictive analytics, IoT integration, and machine learning while preserving the modular and extensible design of the platform.