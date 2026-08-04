# 🏭 Factory Digital Twin

## Overview

The Smart Manufacturing Intelligence Platform (SMIP) models a complete **Factory Digital Twin** representing a modern high-voltage electrical equipment manufacturing facility.

The Digital Twin provides a structured digital representation of the physical factory, enabling manufacturing simulation, traceability, analytics, and future digital transformation initiatives.

---

# Objectives

The Factory Digital Twin is designed to:

- Represent the physical manufacturing environment.
- Model relationships between manufacturing assets.
- Support production planning and execution.
- Enable end-to-end product traceability.
- Generate realistic synthetic manufacturing datasets.
- Serve as the foundation for analytics and Digital Twin applications.

---

# Factory Hierarchy

The manufacturing facility is organized into the following hierarchy.

```text
Factory
│
├── Production Hall
│     │
│     ├── Production Line
│     │      │
│     │      ├── Station
│     │      │      │
│     │      │      ├── Machine
│     │      │      ├── Tool
│     │      │      └── Operator
│     │      │
│     │      └── Manufacturing Operations
│     │
│     └── Products
│
└── Production Planning
```

> Replace this diagram with `factory_digital_twin.svg` once created.

---

# Factory Structure

The simulated factory contains:

| Component | Quantity |
|-----------|---------:|
| Factory | 1 |
| Production Halls | 2 |
| Production Lines | 6 |
| Stations | 54 |
| Machines | 54 |
| Operators | 72 |
| Products | 12 |

---

# Production Hall

A Production Hall groups manufacturing lines performing similar operations.

Typical responsibilities include:

- Product assembly
- Testing
- Packaging
- Logistics

---

# Production Line

Each Production Hall contains multiple Production Lines.

A Production Line consists of an ordered sequence of Stations through which products flow during manufacturing.

Responsibilities:

- Product routing
- Operation sequencing
- Production scheduling

---

# Station

Stations represent individual manufacturing work areas.

Examples:

- Press Fitting
- GIS Bay Assembly
- Mechanical Testing
- Packaging

Each Station is associated with:

- One Machine
- One or more Operators
- Assigned Operations
- Manufacturing Tools

---

# Machine

Machines perform manufacturing operations.

Machine types include:

- Press Fitting Machine
- GIS Bay Assembly
- Mechanical Test Bench
- Packaging Station

Each machine has:

- Unique Machine ID
- Machine Type
- Production Line
- Station
- Operational Status

---

# Operator

Operators execute manufacturing activities.

Each operator is assigned to:

- Production Hall
- Production Line
- Shift
- Skill Level
- Machine

Operators are referenced throughout the simulation using login sessions and production execution records.

---

# Product

Products represent the manufactured high-voltage electrical equipment.

Each product includes:

- Product Code
- Product Name
- Target Force
- Force Tolerance
- Cycle Time
- Press Programs
- Test Programs

---

# Tool

Tools are assigned to machines and manufacturing operations.

Examples include:

- Press Tool
- Assembly Fixture
- Mechanical Fixture

Each tool is uniquely identified and linked to its machine.

---

# Manufacturing Operations

Operations define the routing required to manufacture each product.

Typical operations include:

1. Component Preparation
2. Press Fitting
3. Mechanical Assembly
4. Testing
5. Packaging

Each operation contains:

- Operation Number
- Operation Name
- Standard Cycle Time
- Required Machine Type

---

# Relationships

The Digital Twin maintains hierarchical relationships between all manufacturing entities.

```text
Factory
    │
    ▼
Production Hall
    │
    ▼
Production Line
    │
    ▼
Station
    │
    ▼
Machine
    │
    ├── Operator
    ├── Tool
    └── Manufacturing Operations
```

---

# Design Principles

The Factory Digital Twin follows these principles:

- Hierarchical organization
- Strongly typed entities using Python dataclasses
- Configuration-driven modeling
- Extensible architecture
- Complete traceability
- Separation of master and transactional data

---

# Future Enhancements

Planned improvements include:

- Machine maintenance schedules
- Energy consumption models
- Machine health monitoring
- Real-time IoT integration
- AGV (Automated Guided Vehicle) simulation
- Warehouse Digital Twin
- Inventory management
- Supplier integration

---

# Summary

The Factory Digital Twin serves as the core domain model of the Smart Manufacturing Intelligence Platform.

All manufacturing simulations, transactional datasets, analytics, and future Digital Twin capabilities are built upon this hierarchical representation of the factory.