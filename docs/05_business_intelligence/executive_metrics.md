# 04 — Executive Metrics

## Introduction

The Executive Dashboard represents the final analytical layer of the Smart Manufacturing Intelligence Platform (SMIP) V2.

Rather than presenting raw manufacturing events or engineering datasets, the dashboard provides business leaders with a concise overview of factory performance through a collection of carefully selected Key Performance Indicators (KPIs).

The objective is to enable rapid assessment of production performance, manufacturing quality, material traceability, and shipment readiness from a single interface.

---

# Executive Dashboard

> **Dashboard Overview**

![Executive Dashboard](../08_images/dashboards/dashboard_home.png)

The dashboard consolidates manufacturing KPIs into a unified operational view.

Instead of requiring users to navigate multiple reports, all critical manufacturing metrics are available from a single dashboard.

---

# Dashboard Objectives

The Executive Dashboard enables business users to answer questions such as:

- How many manufacturing operations have been completed?
- Is production meeting expected output?
- Are manufacturing processes operating efficiently?
- Is product quality meeting requirements?
- Are materials fully traceable?
- Are finished products ready for shipment?

---

# Dashboard Sections

The dashboard is organized into five business domains.

| Section | Business Focus |
|----------|----------------|
| Factory Summary | Overall manufacturing activity |
| Production | Manufacturing output |
| Machine Performance | Equipment efficiency |
| Quality | Inspection performance |
| Materials & Packaging | Supply chain and shipment readiness |

Each section provides a focused view while contributing to an overall understanding of factory performance.

---

# Factory Summary

The KPI cards displayed at the top of the dashboard provide an immediate overview of manufacturing activity.

Current metrics include:

| KPI | Current Value |
|------|--------------:|
| Operations Completed | **170,067** |
| Tests Completed | **127,526** |
| Products Started | **1,803** |
| Material Scanned | **42,562** |
| Packages Completed | **42,497** |
| Quality Pass Rate | **100%** |

These KPIs provide an instant snapshot of production performance.

---

# Production Analysis

The **Production by Product** visualization shows manufacturing activity across all product families.

Business users can quickly identify:

- Highest-volume products
- Production distribution
- Manufacturing demand
- Product mix

This visualization supports production planning and capacity management.

---

# Machine Performance

Machine performance is monitored through two visualizations:

- Operations by Machine
- Average Cycle Time

These metrics help manufacturing engineers evaluate equipment utilization and identify opportunities for process optimization.

Typical business questions include:

- Which machine performs the highest workload?
- Is equipment operating consistently?
- Are production cycles becoming longer?

---

# Quality Monitoring

The Quality section evaluates inspection performance.

Current KPIs include:

- Tests by Product
- Quality Pass Rate

The current simulation generates only successful inspections.

Therefore:

| KPI | Current Value |
|------|--------------:|
| Quality Pass Rate | **100%** |

The architecture supports future expansion to include failed inspections, rejected products, and rework scenarios.

---

# Material Traceability

Material traceability is monitored through supplier activity and scan performance.

Visualizations include:

- Material Scan Success
- Materials by Supplier

These metrics enable users to verify:

- Supplier participation
- Material consumption
- Traceability completeness

This information supports manufacturing compliance and supply chain visibility.

---

# Packaging Performance

Packaging metrics monitor products prepared for shipment.

Current visualizations include:

- Packages by Product

The current simulation produces only:

```
READY_FOR_SHIPMENT
```

As a result, all packaged products are considered shipment-ready.

Future versions of the simulator will introduce delayed shipments and packaging exceptions.

---

# Dashboard Filters

The dashboard supports interactive filtering.

Available filters include:

- Product Name
- Supplier
- Planned Shift

These filters allow users to analyze manufacturing performance from different operational perspectives without modifying SQL queries.

---

# Business Value

The Executive Dashboard enables different stakeholders to answer different business questions.

| Stakeholder | Typical Questions |
|--------------|------------------|
| Plant Manager | Is the factory meeting production targets? |
| Production Engineer | Which products dominate production? |
| Manufacturing Engineer | Are machines operating efficiently? |
| Quality Engineer | Is product quality stable? |
| Supply Chain Manager | Which suppliers support production? |
| Operations Manager | Are finished products ready for shipment? |

A single dashboard provides information relevant to multiple business functions.

---

# Current Dashboard Scope

The dashboard demonstrates the complete analytical workflow of SMIP V2 using simulated manufacturing data.

Current capabilities include:

- Factory overview
- Production analysis
- Machine monitoring
- Quality monitoring
- Material traceability
- Packaging performance

Although the current simulation models successful manufacturing scenarios, the dashboard architecture is designed to support more advanced operational metrics in future releases.

---

# Future Enhancements

The Executive Dashboard can be extended with additional manufacturing analytics, including:

- Overall Equipment Effectiveness (OEE)
- Machine downtime analysis
- Production trends over time
- Shift performance comparison
- Operator productivity
- Quality defect analysis
- Predictive maintenance indicators
- Real-time streaming dashboards
- Drill-through analysis

These enhancements can be implemented without changing the underlying Lakehouse architecture.

---

# Executive Summary

The Executive Dashboard transforms manufacturing data into actionable business intelligence.

By combining trusted Gold KPI tables with interactive Databricks SQL visualizations, SMIP V2 provides decision-makers with a comprehensive and easy-to-understand view of factory performance.

The dashboard demonstrates how a modern Lakehouse architecture can convert manufacturing events into operational insights that support continuous improvement, production monitoring, and strategic decision-making.

---

# Chapter Summary

The **Business Intelligence** chapter demonstrated how SMIP V2 delivers value beyond data engineering.

Starting from curated Gold KPI tables, the platform provides a unified Executive Dashboard that enables stakeholders to monitor production, evaluate quality, track materials, and assess packaging performance through a single analytical interface.

This completes the end-to-end journey of manufacturing data within SMIP V2—from raw event generation to executive decision support.