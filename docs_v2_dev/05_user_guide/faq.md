# Frequently Asked Questions

## What is SMIP?

SMIP is a Smart Manufacturing Digital Twin and analytics platform built with Python, Databricks, SQL, and Power BI.

---

## Does SMIP require Databricks?

The manufacturing simulator can generate datasets independently.

Databricks is required for the Lakehouse architecture and business intelligence pipeline.

---

## Can I use Databricks Free Edition?

Yes.

The project has been developed and validated using Databricks Free Edition.

---

## Can Power BI connect directly to Databricks?

Yes.

Power BI connects directly to the Databricks SQL Warehouse using the Gold SQL Views.

---

## Does the project generate realistic manufacturing data?

Yes.

The simulator generates synthetic manufacturing datasets that model a realistic production environment, including work orders, production executions, quality tests, force curves, material traceability, and packaging records.

---

## Which dashboards are included?

- Executive Dashboard
- Production Dashboard
- Quality Dashboard
- Press Fitting Dashboard
- Traceability Dashboard

---

## How many datasets are generated?

SMIP generates:

- Master Data
- Transactional Data
- Silver Dimensions
- Silver Facts
- Gold Summary Tables
- SQL Views

---

## Is SMIP intended for production use?

No.

SMIP is an educational and portfolio project designed to demonstrate manufacturing simulation, data engineering, and business intelligence concepts.

---

## Related Documentation

- Installation
- Quick Start
- Execution Order