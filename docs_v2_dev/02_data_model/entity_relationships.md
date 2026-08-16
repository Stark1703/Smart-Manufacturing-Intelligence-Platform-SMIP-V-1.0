# Entity Relationships

## Overview

SMIP follows a relational manufacturing data model that links products, work orders, production executions, manufacturing operations, quality inspections, and packaging records.

---

## High-Level Relationship Diagram

```text
Product
   │
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

## Relationship Summary

| Parent | Child |
|----------|-------|
| Product | Work Order |
| Work Order | Production Execution |
| Production Execution | Serial Number |
| Serial Number | Press Operation |
| Press Operation | Force Curve |
| Serial Number | Test Result |
| Serial Number | Packaging |

---

## Benefits

- Complete genealogy
- Manufacturing traceability
- KPI generation
- Data consistency

---

## Related Documentation

- Data Lineage
- Manufacturing Workflow