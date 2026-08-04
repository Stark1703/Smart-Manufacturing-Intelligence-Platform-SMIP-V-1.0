# 📁 Project Structure

## Overview

The Smart Manufacturing Intelligence Platform (SMIP) is organized into modular components to separate configuration, business logic, simulation, analytics, and documentation.

```
Smart-Manufacturing-Intelligence-Platform-SMIP/
│
├── dashboard/
├── data/
├── datasets/
├── docs/
├── generator/
├── notebooks/
├── sql/
├── tests/
├── requirements.txt
└── README.md
```

---

# Repository Layout

## dashboard/

Contains dashboard assets, screenshots, and Power BI resources.

---

## data/

Stores all generated datasets.

```
data/
├── master_data/
└── transactional_data/
```

---

## datasets/

Reserved for Databricks Lakehouse storage.

```
datasets/
├── raw/
├── bronze/
├── silver/
└── gold/
```

---

## docs/

Project documentation.

- Architecture
- Data Model
- User Guide
- Analytics
- Development

---

## generator/

Core simulation engine.

```
generator/
├── configs/
├── engine/
├── master_data/
└── simulation/
```

### configs/

Configuration files and Digital Twin definitions.

### engine/

Production planning and scheduling logic.

### master_data/

Generates manufacturing master data.

### simulation/

Generates transactional manufacturing events.

---

## notebooks/

Databricks notebooks implementing Bronze, Silver, and Gold transformations.

---

## sql/

SQL scripts for analytics, views, and KPI calculations.

---

## tests/

Reserved for unit and integration tests.

---

# Design Principles

The repository follows:

- Modular architecture
- Clear separation of concerns
- Reusable simulation modules
- Strong typing with Python dataclasses
- Configuration-driven development
- Extensible folder structure