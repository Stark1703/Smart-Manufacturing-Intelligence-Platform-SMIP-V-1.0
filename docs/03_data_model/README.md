# 03 — Data Model

## Overview

The Smart Manufacturing Intelligence Platform (SMIP) V2 transforms raw manufacturing events into an analytical data model optimized for reporting, business intelligence, and operational analytics.

Rather than querying raw manufacturing events directly, the platform organizes information into a structured dimensional model that separates business entities from measurable manufacturing activities.

The resulting model provides a consistent foundation for analytical queries while improving performance, maintainability, and scalability.

This chapter describes the business model implemented throughout the Lakehouse and explains how manufacturing events are transformed into Dimensions, Facts, and Key Performance Indicators (KPIs).

---

# Purpose

The objective of the Data Model is to provide a business-oriented representation of manufacturing operations.

The analytical model enables engineers, production managers, and business analysts to answer questions such as:

- How efficiently are machines operating?
- What is the production output for each work order?
- How many quality inspections were completed?
- Which materials were consumed during production?
- What products have been packaged and are ready for shipment?
- How is overall factory performance evolving?

The model supports these analytical workloads while maintaining a clear separation between descriptive business entities and measurable manufacturing events.

---

# Data Modeling Strategy

SMIP V2 follows a **Dimensional Modeling** approach using a **Star Schema**.

The architecture separates data into three logical categories:

- **Dimensions** – descriptive business entities
- **Facts** – measurable manufacturing events
- **Gold KPI Tables** – business-ready aggregated metrics

This structure simplifies analytical queries and minimizes data redundancy.

---

# Data Model Overview

```text
Manufacturing Events
        │
        ▼
Parsed Manufacturing Events
        │
        ▼
Business Event Tables
        │
        ├──────────────┐
        ▼              ▼
Dimensions         Fact Tables
        │              │
        └──────┬───────┘
               ▼
         Gold KPI Tables
               │
               ▼
    Databricks SQL Dashboard
```

---

# Data Model Components

The analytical model consists of several interconnected layers.

| Component | Purpose |
|------------|----------|
| Manufacturing Event Model | Represents production events generated throughout the factory |
| Dimension Tables | Describe business entities such as machines, products, operators, and materials |
| Fact Tables | Capture measurable manufacturing activities |
| Star Schema | Organizes dimensions and facts for analytical processing |
| Business Keys | Maintain relationships between manufacturing processes |
| Gold KPI Tables | Provide executive-level manufacturing metrics |

---

# Data Flow

Manufacturing data progresses through several stages before becoming business intelligence.

```text
Raw Manufacturing Events

↓

Parsed Events

↓

Manufacturing Event Tables

↓

Dimension Tables

↓

Fact Tables

↓

Manufacturing KPIs

↓

Executive Dashboard
```

Each stage progressively increases business value while reducing data complexity.

---

# Data Model Documents

This chapter is organized into the following documents.

| Document | Description |
|----------|-------------|
| **01_manufacturing_process.md** | Describes the manufacturing workflow represented by the platform |
| **02_event_model.md** | Explains the manufacturing event structure and lifecycle |
| **03_star_schema.md** | Presents the dimensional Star Schema implemented in SMIP V2 |
| **04_dimensions.md** | Documents the Dimension tables and their business roles |
| **05_facts.md** | Describes the Fact tables and measurable manufacturing processes |
| **06_business_keys.md** | Explains the business identifiers and relationships across the platform |

---

# Design Principles

The analytical model was designed according to several principles.

## Business-Oriented

The model reflects real manufacturing processes rather than technical implementation details.

---

## Scalable

New manufacturing processes can be integrated by adding new event types, dimensions, or facts without redesigning the existing model.

---

## Reusable

Dimension and Fact tables are shared across multiple analytical workloads, dashboards, and future reporting requirements.

---

## Governed

All datasets are managed through Unity Catalog, ensuring consistent naming, metadata, and lineage throughout the platform.

---

## Analytics-Ready

The model is optimized for aggregation, filtering, and reporting rather than transactional processing.

This enables efficient KPI calculations and interactive dashboards.

---

# Expected Outcomes

After completing this chapter, readers will understand:

- The manufacturing process modeled by SMIP V2.
- The lifecycle of manufacturing events.
- The rationale behind the Star Schema.
- The purpose of each Dimension table.
- The purpose of each Fact table.
- How business keys relate manufacturing processes.
- How the analytical model supports manufacturing intelligence.

---

# Summary

The Data Model provides the analytical foundation of the Smart Manufacturing Intelligence Platform.

By combining manufacturing events, Dimension tables, Fact tables, and business keys into a structured Star Schema, the platform delivers reliable, scalable, and business-ready datasets for operational reporting and executive decision-making.

The following documents progressively explore each component of the analytical model, beginning with the manufacturing process itself.

---

# Next Section

## 01 — Manufacturing Process

The next document describes the manufacturing workflow represented within SMIP V2, introducing the sequence of business processes that generate the events used throughout the Lakehouse architecture.