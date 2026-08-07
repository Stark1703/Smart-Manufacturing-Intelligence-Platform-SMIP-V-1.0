# System Architecture

## Overview

SMIP follows a modular architecture that separates manufacturing simulation, data engineering, analytics, and visualization into independent layers.

This separation improves scalability, maintainability, and extensibility.

---

## High-Level Architecture

![System Architecture](../images/architecture/hero_architecture.png)

---

## Architecture Layers

### Manufacturing Simulation

Responsible for generating realistic manufacturing master and transactional data.

---

### Databricks Lakehouse

Stores and processes manufacturing data using Delta Lake and the Medallion Architecture.

---

### SQL Business Layer

Provides curated SQL Views for reporting and dashboard development.

---

### Business Intelligence

Power BI consumes Gold Layer SQL Views to provide interactive dashboards for business users.

---

## Design Principles

SMIP follows the following principles:

- Modular Design
- Separation of Concerns
- Scalable Data Processing
- Reusable Components
- Layered Architecture
- Business-Oriented Data Modeling

---

## Technologies

- Python
- Databricks
- Delta Lake
- Unity Catalog
- SQL
- Power BI

---

## Related Documentation

- Manufacturing Workflow
- Medallion Architecture