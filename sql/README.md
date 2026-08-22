# SQL

## Overview

The `sql` directory contains SQL scripts used throughout the Smart Manufacturing Intelligence Platform (SMIP V2).

These scripts support data definition, analytical queries, KPI generation, and business reporting.

---

## Directory Structure

```text
sql/

├── analytics/
├── ddl/
├── gold/
└── views/
```

---

## Folder Description

### `analytics/`

Contains SQL queries used for manufacturing analysis and KPI calculations.

Examples include:

- Production metrics
- Quality metrics
- Machine performance
- Material analytics

---

### `ddl/`

Contains Data Definition Language (DDL) scripts used to create database objects.

Examples include:

- CREATE TABLE
- CREATE VIEW
- ALTER TABLE

---

### `gold/`

Contains SQL scripts that generate Gold-layer KPI datasets used by the Executive Dashboard.

---

### `views/`

Contains reusable SQL views that simplify analytical queries and reporting.

---

## Role in the Platform

```text
Bronze Tables

↓

Silver Tables

↓

Dimensions

↓

Facts

↓

Gold KPIs

↓

SQL Views

↓

Executive Dashboard
```

---

## Summary

The SQL directory contains the analytical queries and database definitions that transform curated manufacturing datasets into business-ready insights.