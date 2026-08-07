# Master Data

## Overview

Master Data represents the relatively static information that defines the manufacturing environment. These datasets provide the foundation for all transactional manufacturing activities and ensure consistency throughout the Smart Manufacturing Intelligence Platform (SMIP).

The generated master data models the physical factory layout, manufacturing resources, products, tools, and production processes.

---

## Purpose

The Master Data layer is responsible for:

- Defining the manufacturing environment.
- Maintaining consistent reference data.
- Supporting transactional simulations.
- Enabling dimensional modeling in the Lakehouse.
- Providing lookup tables for analytics.

---

## Master Datasets

| Dataset | Description |
|----------|-------------|
| Factory | Manufacturing plant information |
| Production Halls | Factory production areas |
| Production Lines | Production lines within each hall |
| Stations | Manufacturing stations |
| Machines | Manufacturing equipment |
| Operators | Production operators |
| Products | High-voltage equipment products |
| Tools | Manufacturing tools |
| Operations | Manufacturing routing operations |
| Press Programs | Press fitting program parameters |
| Test Programs | Quality testing configurations |

---

## Relationships

```text
Factory
   │
Production Hall
   │
Production Line
   │
Station
   │
Machine
   │
Tool
```

Products are linked to:

- Operations
- Press Programs
- Test Programs

---

## Characteristics

- Low update frequency
- Reference data
- Shared across all manufacturing processes
- Used as dimensions in the Silver Layer

---

## Usage

Master Data is consumed by:

- Work Order Simulation
- Production Execution
- Press Operations
- Quality Testing
- Packaging
- Gold Layer Analytics

---

## Related Documentation

- Transactional Data
- Entity Relationships
- Factory Digital Twin