# Transactional Data

## Overview

Transactional Data captures the events generated during the manufacturing process.

Unlike Master Data, these datasets are continuously generated and represent production activities occurring on the factory floor.

---

## Purpose

Transactional datasets enable:

- Production monitoring
- Manufacturing traceability
- KPI calculation
- Quality analysis
- OEE reporting
- Business intelligence

---

## Transactional Datasets

| Dataset | Description |
|----------|-------------|
| Work Orders | ERP production orders |
| Production Executions | MES execution records |
| Serial Numbers | Product genealogy |
| Press Operations | Manufacturing operations |
| Force Curves | IoT press measurements |
| Test Results | Quality inspection |
| Material Scans | Material traceability |
| Operator Login | Operator activity |
| Packaging | Final packaging records |

---

## Manufacturing Flow

```text
Work Order
      │
Production Execution
      │
Serial Number
      │
Press Operation
      │
Force Curve
      │
Quality Test
      │
Packaging
```

---

## Characteristics

- High data volume
- Time-series events
- Manufacturing history
- End-to-end traceability

---

## Related Documentation

- Master Data
- Data Lineage
- Manufacturing Workflow