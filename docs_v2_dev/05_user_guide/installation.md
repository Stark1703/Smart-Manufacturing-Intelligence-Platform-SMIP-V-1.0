# Installation

## Overview

This guide explains how to install and configure the Smart Manufacturing Intelligence Platform (SMIP).

SMIP consists of three major components:

- Python Manufacturing Simulator
- Databricks Lakehouse
- Power BI Dashboards

---

## Prerequisites

Before installing SMIP, ensure the following software is available:

| Software | Version |
|-----------|----------|
| Python | 3.13 or later |
| Git | Latest |
| Databricks Workspace | Free or Premium |
| Power BI Desktop | Latest |
| Visual Studio Code | Recommended |

---

## Clone Repository

```bash
git clone https://github.com/Stark1703/Smart-Manufacturing-Intelligence-Platform-SMIP-V-1.0.git

cd Smart-Manufacturing-Intelligence-Platform-SMIP-V-1.0
```

---

## Create Virtual Environment

```bash
python -m venv .venv
```

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Databricks Setup

Create a Databricks workspace.

Import the notebooks located in:

```
databricks/notebooks/
```

Create:

- Unity Catalog
- Volume
- SQL Warehouse

---

## Power BI Setup

Connect Power BI to the Databricks SQL Warehouse.

Import the Gold SQL Views.

---

## Installation Complete

The platform is now ready for execution.

---

## Related Documentation

- Quick Start
- Execution Order