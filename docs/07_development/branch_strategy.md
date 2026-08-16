# 03 — Branch Strategy

## Introduction

The Smart Manufacturing Intelligence Platform (SMIP) uses a structured Git branching strategy to separate stable releases, local development, and the Databricks implementation.

Rather than developing every feature directly on the main branch, the project evolved through dedicated branches, each with a specific engineering objective. This approach enabled experimentation, incremental development, and migration to a Lakehouse architecture while preserving a stable codebase.

---

# Branch Overview

The repository currently contains three primary branches.

```text
main

├── v2.0-dev

└── databricks-v2
```

Each branch represents a different stage in the evolution of the project.

---

# Main Branch

## Purpose

The `main` branch serves as the stable version of the project.

It contains:

- Stable source code
- Project documentation
- Reference implementation
- Production-ready commits

The `main` branch is updated only after new features have been validated.

---

# v2.0-dev Branch

## Purpose

The `v2.0-dev` branch was used for local development and experimentation.

Major developments included:

- Manufacturing Event Generator
- Apache Kafka integration
- Apache Spark Structured Streaming
- Local Medallion Architecture
- Event simulation
- Local KPI generation

Development was performed primarily in Visual Studio Code.

---

# databricks-v2 Branch

## Purpose

The `databricks-v2` branch contains the cloud-native implementation of SMIP.

Major components include:

- Unity Catalog
- Delta Lake
- Lakeflow Declarative Pipelines
- Bronze Layer
- Silver Layer
- Dimension Layer
- Fact Layer
- Gold KPI Layer
- Databricks SQL Dashboard

This branch represents the complete Lakehouse implementation.

---

# Development Workflow

The project evolved through the following workflow.

```text
main

↓

v2.0-dev

↓

Databricks Migration

↓

databricks-v2

↓

Testing

↓

Documentation

↓

Future Release
```

Each stage introduced new capabilities while preserving the stability of previous work.

---

# Benefits of the Branching Strategy

The adopted branching strategy provides several advantages.

- Stable production branch
- Independent feature development
- Safe experimentation
- Easier testing
- Simplified migration
- Clear project history

This workflow enabled the project to evolve from a local prototype into a production-oriented analytics platform without disrupting the existing implementation.

---

# Summary

The Git branching strategy reflects the evolution of SMIP from a local streaming application to a Databricks Lakehouse platform.

By separating stable releases from active development and cloud migration, the repository remains organized, maintainable, and ready for future enhancements.