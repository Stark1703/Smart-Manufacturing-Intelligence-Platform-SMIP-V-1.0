# 03 — Dashboard Walkthrough

## Introduction

The Factory Dashboard provides a consolidated view of manufacturing performance across the Smart Manufacturing Intelligence Platform (SMIP) V2.

It combines operational, quality, production, material, and packaging metrics into a single business interface, enabling stakeholders to monitor factory performance in real time.

This document provides a guided walkthrough of the dashboard, explaining the purpose of each section, the KPIs displayed, and how the information supports operational and strategic decision-making.

---

# Dashboard Overview

The Factory Dashboard is organized into five analytical sections.

```text
Factory Summary

↓

Machine Performance

↓

Quality Performance

↓

Production Performance

↓

Material Traceability

↓

Packaging Performance
```

Each section focuses on a specific manufacturing domain while contributing to an overall view of factory operations.

---

# Factory Summary

> **Insert Screenshot**

```
docs/08_images/dashboards/dashboard_home.png
```

### Business Purpose

The Factory Summary provides a high-level overview of manufacturing activity.

It enables users to understand the current operational status of the factory without navigating through detailed reports.

---

### Typical KPIs

- Total Operations
- Total Production
- Total Quality Inspections
- Total Material Scans
- Total Packaged Products

---

### Business Interpretation

Business users can quickly determine:

- Current production activity
- Overall manufacturing workload
- Factory throughput
- Operational health

This section acts as the dashboard landing page.

---

# Machine Performance

> **Insert Screenshot**

```
docs/08_images/dashboards/machine_kpis.png
```

### Business Purpose

The Machine Performance section evaluates equipment efficiency and operational performance.

---

### KPIs Displayed

- Operations Completed
- Average Cycle Time
- Average Target Force
- Average Actual Force
- Average Force Deviation

---

### Business Interpretation

Typical business questions answered include:

- Which machines perform the highest workload?
- Are machines operating within expected parameters?
- Is production becoming slower over time?
- Which machines require investigation?

---

# Quality Performance

> **Insert Screenshot**

```
docs/08_images/dashboards/quality_kpis.png
```

### Business Purpose

The Quality section monitors inspection activities and manufacturing quality.

---

### KPIs Displayed

- Total Quality Inspections
- Quality Pass Rate
- Average Target Value
- Average Measured Value
- Measurement Deviation

---

### Current Simulation

The current simulator produces only successful inspections.

Therefore:

```
Quality Pass Rate = 100%
```

---

### Future Dashboard

Future versions will visualize:

- Failed inspections
- Product defects
- Rework operations
- Quality trends

---

### Business Interpretation

Quality Engineers can determine:

- Overall product quality
- Inspection workload
- Measurement consistency
- Process stability

---

# Production Performance

> **Insert Screenshot**

```
docs/08_images/dashboards/production_kpis.png
```

### Business Purpose

This section measures manufacturing output.

---

### KPIs Displayed

- Production Quantity
- Production Executions
- Work Orders Processed
- Production by Product

---

### Business Interpretation

Plant Managers can monitor:

- Factory throughput
- Production demand
- Manufacturing activity
- Product mix

---

# Material Traceability

> **Insert Screenshot**

```
docs/08_images/dashboards/material_kpis.png
```

### Business Purpose

The Material Traceability section monitors production materials throughout the manufacturing process.

---

### KPIs Displayed

- Material Scans
- Suppliers Utilized
- Material Batches
- Scan Success

---

### Business Interpretation

This section enables users to answer questions such as:

- Which suppliers are supporting production?
- Which material batches were consumed?
- Is material traceability complete?

---

# Packaging Performance

> **Insert Screenshot**

```
docs/08_images/dashboards/packaging_kpis.png
```

### Business Purpose

The Packaging section monitors the preparation of finished products for shipment.

---

### KPIs Displayed

- Products Packaged
- Average Package Weight
- Shipment Readiness

---

### Current Simulation

The current simulator produces:

```
READY_FOR_SHIPMENT
```

Therefore:

```
Shipment Readiness = 100%
```

---

### Future Dashboard

Future releases may include:

- Packaging delays
- Shipment holds
- Packaging failures
- Logistics performance

---

### Business Interpretation

Operations teams can monitor:

- Packaging throughput
- Shipment readiness
- Finished goods inventory

---

# Dashboard Navigation

Users can navigate the dashboard by reviewing each section independently or by interpreting the dashboard as a complete operational overview.

```text
Factory Summary

↓

Machine KPIs

↓

Quality KPIs

↓

Production KPIs

↓

Material KPIs

↓

Packaging KPIs
```

This top-down organization mirrors the manufacturing lifecycle.

---

# Dashboard Refresh

The dashboard displays metrics generated from the Gold KPI tables.

```text
Manufacturing Events

↓

Lakeflow Pipeline

↓

Gold KPI Tables

↓

Databricks SQL Dashboard
```

As the pipeline processes new manufacturing events, KPI tables are refreshed, ensuring that dashboard information remains current.

---

# Current Dashboard Scope

The current dashboard demonstrates the complete analytical workflow using simulated manufacturing data.

The dashboard currently visualizes:

- Machine performance
- Production metrics
- Quality performance
- Material traceability
- Packaging activity
- Factory summary

These metrics validate the end-to-end functionality of the Lakehouse architecture.

---

# Future Dashboard Enhancements

Planned dashboard enhancements include:

- Time-series trend analysis
- Shift-level reporting
- Production line comparisons
- Machine utilization
- OEE dashboards
- Quality defect analysis
- Predictive maintenance indicators
- Drill-through reporting
- Interactive filtering

The modular architecture allows these features to be added without redesigning the existing platform.

---

# Summary

The Factory Dashboard represents the business interface of the Smart Manufacturing Intelligence Platform.

By combining manufacturing KPIs into a unified Databricks SQL Dashboard, the platform enables engineers, managers, and executives to monitor factory performance through trusted, interactive, and easy-to-understand visualizations.

The dashboard demonstrates how modern Lakehouse architectures can transform manufacturing events into actionable operational intelligence.

---

# Next Section

## 04 — Executive Metrics

The next document explains how business leaders interpret the dashboard KPIs, describing the operational significance of each metric and how they support manufacturing decision-making.