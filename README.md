# 🏭 Smart Manufacturing Intelligence Platform (SMIP)

> **A complete end-to-end Smart Manufacturing Digital Twin and Manufacturing Execution System (MES) simulation platform built with Python.**

![Python](https://img.shields.io/badge/Python-3.13-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active%20Development-orange.svg)
![Platform](https://img.shields.io/badge/Platform-Databricks-red.svg)

---


# 📑 Table of Contents

- [Overview](#overview)
- [project Highlights](#-project-highlights)
- [Architecture](#architecture)
- [Key Features](#key-features)
  - [Factory Digital Twin](#factory-digital-twin)
  - [Manufacturing Simulation](#manufacturing-simulation)
  - [Analytics](#analytics)
- [Repository Structure](#repository-structure)
- [Generated Datasets](#generated-datasets)
  - [Master Data](#master-data)
  - [Transactional Data](#transactional-data)
- [Quick Start](#quick-start)
- [Documentation](#documentation)
- [Roadmap](#roadmap)
  - [Completed](#completed)
  - [In Progress](#in-progress)
  - [Planned](#planned)
- [Technologies](#technologies)
- [Screenshots](#screenshots)
- [Project Statistics](#project-statistics)
- [Future Work](#future-work)
- [Author](#author)
- [License](#license)


## Overview

The **Smart Manufacturing Intelligence Platform (SMIP)** is a modular simulation platform that models the operation of a modern manufacturing facility producing high-voltage electrical equipment.

The project generates realistic synthetic manufacturing data covering the complete production lifecycle, from ERP work orders through manufacturing execution, quality inspection, packaging, and product traceability.

The generated datasets are intended for:

- 🏭 Manufacturing Analytics
- 🤖 Factory Digital Twin
- 📡 Industrial IoT (IIoT)
- 📊 Power BI Dashboards
- ☁️ Databricks Lakehouse
- 🧠 Machine Learning
- 📈 Manufacturing KPI Analysis
- 🔍 End-to-End Product Traceability

---

## 🌟 Project Highlights

- 🏭 End-to-end Smart Manufacturing Digital Twin
- ⚙️ 10+ master data generators
- 📦 9 transactional manufacturing simulations
- 📈 3.6 million synthetic IoT force curve data points
- 🔗 Complete product genealogy and traceability
- ☁️ Designed for Databricks Lakehouse architecture
- 📊 Analytics-ready datasets for SQL and Power BI
- 🐍 Built with modern Python and a modular architecture

---

## Architecture

> **System Architecture Diagram**

```
docs/images/architecture/system_architecture.svg
```

*(Replace this placeholder with the exported SVG once the diagram is created.)*

---

## Key Features

### Factory Digital Twin

- Factory hierarchy
- Production halls
- Production lines
- Stations
- Machines
- Operators
- Products
- Tools

### Manufacturing Simulation

- SAP Work Orders
- Production Executions
- Operator Login
- Material Scans
- Serial Numbers
- Press Operations
- Force Curve Simulation
- Quality Testing
- Packaging

### Analytics

- Manufacturing KPIs
- SQL Analytics
- Databricks Lakehouse
- Power BI
- Product Traceability

---

## Repository Structure

```text
Smart-Manufacturing-Intelligence-Platform-SMIP/
│
├── generator/
├── data/
├── datasets/
├── notebooks/
├── sql/
├── docs/
├── dashboard/
└── tests/
```

See the complete structure in:

**📄 `docs/development/project_structure.md`**

---

## Generated Datasets

### Master Data

- Production Halls
- Production Lines
- Stations
- Machines
- Operators
- Products
- Tools
- Operations
- Press Programs
- Test Programs

### Transactional Data

- Work Orders
- Production Executions
- Operator Login Sessions
- Material Scans
- Serial Numbers
- Press Operations
- Force Curve Points
- Test Results
- Packaging Records

---

## Quick Start

Clone the repository:

```bash
git clone https://github.com/<your-username>/Smart-Manufacturing-Intelligence-Platform-SMIP.git

cd Smart-Manufacturing-Intelligence-Platform-SMIP
```

Create a virtual environment:

```bash
python -m venv .venv
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Generate the complete manufacturing dataset:

```bash
python -m generator.master_data.generate_machine_layout

python -m generator.master_data.generate_product_master

python -m generator.master_data.generate_tool_master

...

python -m generator.simulation.simulate_packaging
```

Detailed instructions are available in:

**📄 `docs/user_guide/execution_order.md`**

---

## Documentation

Complete technical documentation is available in the `docs` directory.

| Section | Description |
|----------|-------------|
| Architecture | System design and workflows |
| Data Model | Master and transactional datasets |
| User Guide | Installation and execution |
| Analytics | KPIs, SQL, dashboards |
| Development | Repository structure and roadmap |

👉 **See:** `docs/README.md`

---

## Roadmap

### Completed

- Factory Digital Twin
- Master Data Generation
- Manufacturing Simulation
- Production Planning
- Force Curve Simulation
- Manufacturing Testing
- Packaging Simulation

### In Progress

- Databricks Bronze Layer
- Silver Transformations
- Gold KPI Tables
- SQL Analytics

### Planned

- Delta Lake Integration
- Real-Time Streaming
- Power BI Dashboards
- Predictive Maintenance
- Machine Learning Models
- Docker Support
- CI/CD

---

## Technologies

- Python 3.13
- Pandas
- NumPy
- SQL
- Databricks (planned)
- Power BI (planned)

---



# 📸 Screenshots

The following screenshots will be added as the project evolves.

| Screenshot | Description |
|------------|-------------|
| Factory Digital Twin | Factory hierarchy |
| Manufacturing Workflow | Production process |
| Databricks Lakehouse | Bronze → Silver → Gold |
| Power BI Dashboard | Manufacturing KPIs |
| Force Curve | IoT press-fit visualization |

> Screenshots and architecture diagrams are available in `docs/images/`.

---

# 📈 Project Statistics

### Generated Master Data

| Dataset | Records |
|----------|---------:|
| Production Halls | 2 |
| Production Lines | 6 |
| Stations | 54 |
| Machines | 54 |
| Operators | 72 |
| Products | 12 |
| Tools | 54 |
| Press Programs | 48 |
| Test Programs | 36 |

---

### Generated Transactional Data

| Dataset | Records |
|----------|---------:|
| Work Orders | 640 |
| Production Executions | 640 |
| Operator Login Sessions | 640 |
| Material Scans | 1,803 |
| Serial Numbers | 1,803 |
| Press Operations | 7,212 |
| Force Curve Points | **3,606,000** |
| Test Results | 5,409 |
| Packaging Records | 1,803 |

---


# 🚀 Future Work

The Smart Manufacturing Intelligence Platform will continue to evolve with additional capabilities.

### Data Platform

- Delta Lake integration
- Databricks Unity Catalog
- Incremental ETL pipelines
- Streaming data ingestion

### Manufacturing

- Predictive Maintenance
- Machine Downtime Simulation
- Energy Consumption Simulation
- Production Scheduling Optimization

### Analytics

- Power BI Executive Dashboard
- Manufacturing KPI Dashboard
- Quality Dashboard
- Traceability Dashboard

### Engineering

- REST API
- Docker Support
- GitHub Actions CI/CD
- Automated Testing
- Performance Benchmarking

---


## Author

**Sumanth Vempalle**

Mechanical Engineer | Sustainable Industrial Engineering

Specializations:

- Manufacturing Systems
- Industrial Digitalization
- Data Engineering
- Python
- SQL
- Power BI
- Databricks

---

## License

This project is licensed under the **MIT License**.

---

⭐ If you found this project useful, consider giving it a star on GitHub.