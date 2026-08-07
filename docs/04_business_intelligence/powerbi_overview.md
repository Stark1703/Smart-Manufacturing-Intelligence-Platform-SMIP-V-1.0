# Power BI Overview

## Overview

The Smart Manufacturing Intelligence Platform (SMIP) provides interactive Power BI dashboards that transform manufacturing data into actionable business insights.

The dashboards consume Gold Layer SQL Views from the Databricks Lakehouse, providing a centralized and consistent reporting experience.

---

## Objectives

The Power BI solution enables users to:

- Monitor manufacturing performance
- Analyze production throughput
- Track product quality
- Measure Overall Equipment Effectiveness (OEE)
- Perform end-to-end product traceability

---

## Dashboard Architecture

```text
Gold Layer
      │
SQL Views
      │
Databricks SQL Warehouse
      │
Power BI Desktop
      │
Interactive Dashboards
```

---

## Dashboards

SMIP includes five dashboards:

| Dashboard | Purpose |
|-----------|---------|
| Executive | Manufacturing KPIs |
| Production | Production performance |
| Quality | Product quality |
| Press Fitting | OEE and process monitoring |
| Traceability | Product genealogy |

---

## Data Source

All dashboards consume SQL Views directly from Databricks.

No manual CSV refresh is required.

---

## Benefits

- Single source of truth
- Interactive filtering
- Near real-time analytics
- Executive reporting
- Manufacturing insights

---

## Related Documentation

- Executive Dashboard
- Production Dashboard
- Quality Dashboard
- Press Fitting Dashboard
- Traceability Dashboard