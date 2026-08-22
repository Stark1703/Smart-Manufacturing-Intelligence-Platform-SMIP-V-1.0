# 🏭 Smart Manufacturing Intelligence Platform (SMIP V2)

<p align="center">

<img src="assets/Hero Architecture.png" width="1000"/>

</p>

<p align="center">

<strong>An end-to-end Manufacturing Intelligence Platform built on the Databricks Lakehouse that demonstrates modern Data Engineering practices using synthetic manufacturing data.</strong>

</p>

<p align="center">

<img src="assets/Executive Dashboard.png" width="900"/>

</p>

---

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Databricks](https://img.shields.io/badge/Databricks-Lakehouse-red)
![Delta Lake](https://img.shields.io/badge/Delta-Lake-orange)
![Unity Catalog](https://img.shields.io/badge/Unity-Catalog-purple)
![Lakeflow](https://img.shields.io/badge/Lakeflow-Declarative%20Pipelines-red)
![SQL](https://img.shields.io/badge/SQL-Databricks-blue)
![License](https://img.shields.io/badge/License-MIT-green)

---
## 📑 Table of Contents

- [Overview](#-overview)
- [End-to-End Data Flow](#-end-to-end-data-flow)
- [Project Highlights](#-project-highlights)
- [Architecture](#-architecture)
- [Technology Stack](#-technology-stack)
- [Repository Structure](#-repository-structure)
- [Documentation](#-documentation)
- [Platform Statistics](#-platform-statistics)
- [Quick Start](#-quick-start)
- [Project Objectives](#-project-objectives)
- [Roadmap](#-roadmap)
- [Author](#-author)
- [License](#-license)

--- 

# 📖 Overview

The **Smart Manufacturing Intelligence Platform (SMIP V2)** is an end-to-end Data Engineering project that simulates a modern high-voltage electrical equipment factory using synthetic manufacturing events.

The platform demonstrates how raw manufacturing events can be ingested, validated, transformed, modeled, and analyzed within the **Databricks Data Intelligence Platform** using a modern **Lakehouse Architecture**.

Manufacturing events are processed through a complete **Medallion Architecture**, transformed into **Dimension and Fact tables**, aggregated into **Gold KPI datasets**, and finally visualized through an interactive **Databricks SQL Executive Dashboard**.

---

# 🚀 End-to-End Data Flow

```text
Manufacturing Event Generator

        │

        ▼

Raw JSON Manufacturing Events

        │

        ▼

Unity Catalog Volume

        │

        ▼

Lakeflow Declarative Pipeline

        │

        ▼

Bronze Layer

        │

        ▼

Silver Layer

        │

        ▼

Dimension Tables

        │

        ▼

Fact Tables

        │

        ▼

Gold KPI Tables

        │

        ▼

Databricks SQL Dashboard
```

---

# ✨ Project Highlights

## 🏭 Manufacturing Simulation

- Manufacturing Event Generator
- High-Voltage GIS Production Simulation
- Production Executions
- Manufacturing Operations
- Quality Inspections
- Material Traceability
- Packaging Simulation

---

## ⚙ Data Engineering

- Databricks Lakehouse
- Lakeflow Declarative Pipelines
- Delta Lake
- Unity Catalog
- Medallion Architecture
- Star Schema
- Data Quality Validation
- Incremental Processing

---

## 📊 Business Intelligence

- Executive Manufacturing Dashboard
- Production KPIs
- Machine Performance
- Quality Metrics
- Material Traceability
- Packaging Analytics

---

# 🏗 Architecture

<p align="center">

<img src="assets/Hero Architecture.png" width="900"/>

</p>

The platform follows a modern **Lakehouse Architecture** implemented using Databricks.

Core architectural components include:

- Manufacturing Event Generator
- Unity Catalog
- Delta Lake
- Lakeflow Declarative Pipelines
- Medallion Architecture
- Star Schema
- Gold KPI Layer
- Databricks SQL Dashboard

---

# 🛠 Technology Stack

| Layer | Technologies |
|----------|--------------|
| Programming | Python 3.13 |
| Data Platform | Databricks |
| Storage | Delta Lake |
| Governance | Unity Catalog |
| Processing | Apache Spark |
| Orchestration | Lakeflow Declarative Pipelines |
| Query Engine | Databricks SQL |
| Analytics | SQL |
| Version Control | Git & GitHub |

---

# 📂 Repository Structure

```text
Smart-Manufacturing-Intelligence-Platform-SMIP-V-1.0

│

├── data/
│   ├── bronze
│   ├── master_data
│   ├── silver
│   └── transactional_data
│
├── databricks/
│   └── notebooks/
│       ├── 00_setup
│       ├── 01_bronze
│       ├── 02_silver
│       ├── 03_dimensions
│       ├── 04_facts
│       ├── 05_gold
│       ├── 06_sql_dashboard
│       └── 07_validation
│
├── docs/
│
├── sql/
│
└── tests/
```

---

# 📚 Documentation

Complete project documentation is available in the **docs** directory.

| Documentation | Description |
|--------------|-------------|
| 📖 Overview | Project introduction and objectives |
| 🏗 Architecture | Lakehouse, Medallion and Pipeline Architecture |
| 📦 Data Model | Manufacturing events, Star Schema and business entities |
| ⚙ Data Engineering | Bronze, Silver, Dimension, Fact and Gold layers |
| 📊 Business Intelligence | Executive Dashboard and manufacturing KPIs |
| 👨‍💻 User Guide | Deployment, execution and troubleshooting |
| 🚀 Development | Project journey, architecture decisions and roadmap |

---

# 📈 Platform Statistics

### Manufacturing Dataset

| Metric | Value |
|---------|------:|
| Work Orders | 640 |
| Production Executions | 640 |
| Products Started | 1,803 |
| Manufacturing Operations | 170,067 |
| Quality Inspections | 127,526 |
| Material Scans | 42,562 |
| Packaging Events | 42,497 |

---

### Master Data

- 12 Products
- 7 Machines
- 73 Operators
- Multiple Suppliers
- Manufacturing Reference Data

---

# 🚀 Quick Start

## Clone Repository

```bash
git clone https://github.com/Stark1703/Smart-Manufacturing-Intelligence-Platform-SMIP-V-1.0.git

cd Smart-Manufacturing-Intelligence-Platform-SMIP-V-1.0
```

---

## Open Databricks

Import the notebooks into your Databricks Workspace.

Execute notebooks in the following order:

```text
00_setup

↓

01_bronze

↓

02_silver

↓

03_dimensions

↓

04_facts

↓

05_gold

↓

06_sql_dashboard

↓

07_validation
```

---

# 🎯 Project Objectives

This project demonstrates practical implementation of:

- Modern Data Engineering
- Lakehouse Architecture
- Delta Lake
- Medallion Architecture
- Data Modeling
- Manufacturing Analytics
- Databricks SQL
- Data Quality
- Business Intelligence

---

# 🛣 Roadmap

## ✅ Current (SMIP V2)

- Manufacturing Event Generator
- Databricks Lakehouse
- Delta Lake
- Unity Catalog
- Lakeflow Declarative Pipelines
- Star Schema
- Executive Dashboard

---

## 🚀 Future

- Real-Time Event Streaming
- IoT Integration
- Predictive Maintenance
- OEE Analytics
- Machine Learning
- Digital Twin Enhancements
- SAP Integration

---

# 👨‍💻 Author

## **Sumanth Vempalle**

**Mechanical and Sustainable Induistrial Engineer → Data Engineer**

### Areas of Interest

- Data Engineering
- Manufacturing Analytics
- Databricks
- Python
- SQL
- Lakehouse Architecture

---

# 📄 License

This project is licensed under the **MIT License**.

---

# ⭐ Support

If you found this project useful or interesting, consider giving it a **Star ⭐** on GitHub.