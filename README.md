# 🏭 Smart Manufacturing Intelligence Platform (SMIP)


<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/9d40e088-41e0-4381-9f0d-2ab9630bf4fe" />



> **An end-to-end Manufacturing Intelligence Platform that simulates a modern high-voltage electrical equipment factory using Python, Databricks Lakehouse, Delta Lake, Unity Catalog, SQL, and Power BI.**

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Databricks](https://img.shields.io/badge/Databricks-Lakehouse-red)
![Delta Lake](https://img.shields.io/badge/Delta-Lake-orange)
![Unity Catalog](https://img.shields.io/badge/Unity-Catalog-purple)
![Power BI](https://img.shields.io/badge/Power-BI-F2C811?logo=powerbi&logoColor=black)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📖 Overview

The **Smart Manufacturing Intelligence Platform (SMIP)** is an end-to-end manufacturing analytics platform that simulates the complete production lifecycle of high-voltage electrical equipment.

The platform generates realistic manufacturing data, processes it through a **Databricks Lakehouse** using the **Medallion Architecture (Bronze → Silver → Gold)**, and delivers business-ready insights through interactive **Power BI dashboards**.

### Manufacturing Data Flow

```text
Manufacturing Simulation
        │
        ▼
Synthetic Manufacturing Data
        │
        ▼
Databricks Lakehouse
(Bronze → Silver → Gold)
        │
        ▼
SQL Business Views
        │
        ▼
Power BI Dashboards
```

---

## ✨ Key Features

### 🏭 Manufacturing Simulation

- Factory Digital Twin
- SAP Production Work Orders
- Production Executions
- Press Fitting Operations
- Force Curve Simulation
- Quality Testing
- Material Traceability
- Packaging Simulation

### ☁️ Data Engineering

- Databricks Lakehouse
- Medallion Architecture
- Delta Lake
- Unity Catalog
- Databricks Workflows
- SQL Business Views

### 📊 Business Intelligence

- Executive Dashboard
- Production Dashboard
- Quality Dashboard
- Press Fitting Operations Dashboard
- Product Traceability Dashboard

---

## 🏗 System Architecture

> Architecture diagram

```text
/images/architecture.png
```

*(Architecture diagram will be added here.)*

---

## 📊 Power BI Dashboards

SMIP includes five business-oriented dashboards.

| Dashboard | Purpose |
|-----------|---------|
| Executive Dashboard | Executive KPIs and manufacturing overview |
| Production Dashboard | Production monitoring and throughput |
| Quality Dashboard | Quality performance and pass/fail analysis |
| Press Fitting Dashboard | OEE, force analysis and cycle time monitoring |
| Traceability Dashboard | Complete product genealogy and manufacturing history |

Screenshots are available in the **powerbi/screenshots** directory.

---

## 🛠 Technology Stack

| Category | Technologies |
|----------|--------------|
| Programming | Python 3.13 |
| Data Processing | Pandas, NumPy |
| Data Platform | Databricks, Delta Lake, Unity Catalog |
| Analytics | SQL |
| Business Intelligence | Power BI |
| Version Control | Git, GitHub |

---

## 📂 Repository Structure

```text
Smart-Manufacturing-Intelligence-Platform-SMIP/
│
├── generator/
├── framework/
├── databricks/
├── powerbi/
├── sql/
├── docs/
├── data/
└── tests/
```

A detailed repository structure is available in:

```text
docs/architecture/project_structure.md
```

---

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/Stark1703/Smart-Manufacturing-Intelligence-Platform-SMIP-V-1.0.git

cd Smart-Manufacturing-Intelligence-Platform-SMIP-V-1.0
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Generate Manufacturing Data

Run the SMIP generator notebook:

```text
databricks/notebooks/05_generator/01_run_smip
```

### 4. Execute the Databricks Workflow

```text
SMIP Production Pipeline
```

The workflow automatically executes:

- Manufacturing Data Generation
- Bronze Layer
- Silver Layer
- Gold Layer

### 5. Open the Power BI Report

```text
powerbi/reports/SMIP_v1.0.pbix
```

---

## 📚 Documentation

Comprehensive documentation is available in the **docs** directory.

| Section | Description |
|----------|-------------|
| Architecture | System architecture and workflows |
| Data Model | Master and transactional datasets |
| Analytics | KPIs and dashboards |
| User Guide | Installation and execution |
| Development | Project roadmap and guidelines |

---

## 📈 Project Statistics

### Master Data

- 12 Products
- 2 Production Halls
- 6 Production Lines
- 54 Stations
- 54 Machines
- 72 Operators
- 54 Tools
- 48 Press Programs
- 36 Test Programs

### Transactional Data

- 640 Work Orders
- 640 Production Executions
- 1,803 Serial Numbers
- 7,212 Press Operations
- 3.6 Million Force Curve Points
- 5,409 Test Results
- 1,803 Packaging Records

---

## 🗺 Roadmap

### ✅ SMIP v1.0

- Manufacturing Data Simulator
- Factory Digital Twin
- Databricks Lakehouse
- Delta Lake
- Unity Catalog
- Databricks Workflows
- SQL Business Views
- Power BI Dashboards

### 🚀 SMIP v2.0

- Industrial IoT Streaming
- Real-Time Manufacturing Analytics
- Predictive Maintenance
- Machine Health Monitoring
- Digital Twin Enhancements

---

## 👨‍💻 Author

**Sumanth Vempalle**

Mechanical Engineer | Sustainable Industrial Engineering

**Specializations**

- Manufacturing Systems
- Industrial Digitalization
- Data Engineering
- Python
- SQL
- Databricks
- Power BI

---

## 📄 License

This project is licensed under the **MIT License**.

---

⭐ If you found this project interesting, consider giving it a **Star** on GitHub.
