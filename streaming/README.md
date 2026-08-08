# Sprint 01 – Streaming Foundation

**Version:** SMIP v2.0

**Sprint:** 01

**Status:** In Progress

---

# Overview

Sprint 01 marks the beginning of the Smart Manufacturing Intelligence Platform (SMIP) v2.0.

The objective of this sprint is to transform SMIP from a **batch-oriented manufacturing analytics platform** into an **event-driven streaming data platform**.

Rather than generating static CSV datasets that are processed periodically, manufacturing activities will be represented as individual events that continuously flow into the Databricks Lakehouse.

This sprint establishes the technical foundation required for future capabilities including Delta Live Tables, Predictive Maintenance, REST APIs, Docker deployment, and real-time analytics.

---

# Sprint Goal

Design and implement the first streaming ingestion pipeline capable of continuously processing manufacturing events.

The existing Medallion Architecture introduced in SMIP v1.0 will remain unchanged.

Only the ingestion mechanism will evolve.

---

# Current Architecture (SMIP v1.0)

```text
Manufacturing Simulator
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
Power BI
```

---

# Target Architecture (SMIP v2.0)

```text
Manufacturing Event Simulator
              │
              ▼
JSON Manufacturing Events
              │
              ▼
Unity Catalog Volume
              │
              ▼
Databricks Auto Loader
              │
              ▼
Streaming Bronze Delta Table
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
Power BI
```

---

# Objectives

The objectives of Sprint 01 are:

- Introduce event-driven manufacturing simulation.
- Create a reusable manufacturing event model.
- Generate JSON event files continuously.
- Configure Databricks Auto Loader.
- Build the first streaming Bronze table.
- Preserve compatibility with the existing Silver and Gold layers.

---

# Scope

## Included

- Manufacturing Event Model
- Streaming Simulator
- JSON Event Generation
- Auto Loader
- Streaming Bronze Layer
- Documentation

## Excluded

The following features are intentionally deferred to later sprints:

- Delta Live Tables
- Kafka
- Predictive Maintenance
- Machine Learning
- REST API
- Docker
- CI/CD

---

# Repository Changes

The following package will be introduced.

```text
streaming/
│
├── README.md
├── __init__.py
│
├── configs/
│   └── streaming_config.py
│
├── events/
│   ├── event_types.py
│   └── manufacturing_event.py
│
├── producers/
│   └── production_event_producer.py
│
├── simulator/
│   └── run_streaming_simulation.py
│
└── utils/
    └── json_writer.py
```

This package is independent from the existing batch generator and is dedicated to streaming functionality.

---

# Manufacturing Event Model

Every manufacturing activity will be represented as a single event.

Example:

```json
{
  "event_id": "EVT-00000001",
  "event_timestamp": "2026-08-08T10:15:24Z",
  "event_type": "PRESS_OPERATION",
  "plant_code": "PLANT-001",
  "hall_id": "HALL-01",
  "line_id": "LINE-02",
  "machine_id": "MACH-015",
  "execution_id": "EXEC-000145",
  "serial_number": "SN-000456",
  "operator_id": "OP-021",
  "product_code": "GIS-145KV",
  "force_kn": 213.4,
  "cycle_time_sec": 28,
  "quality_result": "PASS"
}
```

---

# Event Types

Sprint 01 introduces the following manufacturing events.

| Event | Description |
|---------|-------------|
| WORK_ORDER_CREATED | SAP Production Order Released |
| EXECUTION_STARTED | MES Execution Started |
| PRESS_OPERATION | Press Fitting Completed |
| QUALITY_COMPLETED | Quality Inspection Completed |
| MATERIAL_SCANNED | Material Traceability Event |
| PACKAGING_COMPLETED | Packaging Completed |

Future sprints may introduce additional event types.

---

# Event Storage

Instead of generating large CSV files, the streaming simulator will continuously generate small JSON files.

Example:

```text
streaming_events/

├── 20260808_101500_00001.json
├── 20260808_101501_00002.json
├── 20260808_101502_00003.json
├── 20260808_101503_00004.json
└── ...
```

This format is optimized for Databricks Auto Loader.

---

# Auto Loader

Databricks Auto Loader continuously monitors the event directory.

Whenever a new JSON file appears:

1. Detect the file.
2. Infer or apply the schema.
3. Append the event to the Bronze Delta table.
4. Record checkpoint information.
5. Wait for the next event.

---

# Streaming Bronze Layer

The Bronze Layer becomes a continuously updated Delta table.

Characteristics:

- Append-only
- Immutable events
- Schema evolution support
- Checkpointing
- Fault tolerance

---

# Expected Data Flow

```text
Manufacturing Event
        │
        ▼
JSON File
        │
        ▼
Unity Catalog Volume
        │
        ▼
Auto Loader
        │
        ▼
Streaming Bronze Delta
        │
        ▼
Silver
        │
        ▼
Gold
        │
        ▼
Power BI
```

---

# Deliverables

At the end of Sprint 01 the platform should include:

- Manufacturing Event dataclass
- Event Type definitions
- Streaming Configuration
- JSON Event Writer
- Event Producer
- Streaming Simulator
- Auto Loader Notebook
- Streaming Bronze Delta Table

---

# Success Criteria

Sprint 01 is considered complete when the following workflow executes successfully.

```text
Generate Manufacturing Event
            │
            ▼
Write JSON File
            │
            ▼
Auto Loader Detects File
            │
            ▼
Streaming Bronze Table Updated
```

---

# Future Sprints

Sprint 02 will introduce Delta Live Tables to replace notebook-based transformations with managed streaming pipelines.

Subsequent sprints will extend the platform with:

- Real-Time Dashboards
- Predictive Maintenance
- Machine Learning
- REST API
- Docker
- CI/CD

---

# Related Documentation

- Databricks Lakehouse
- Medallion Architecture
- Bronze Layer
- Sprint 02 – Delta Live Tables