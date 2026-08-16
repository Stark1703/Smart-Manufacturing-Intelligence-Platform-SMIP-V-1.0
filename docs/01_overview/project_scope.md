# Project Scope

## Introduction

Clearly defining the project scope establishes the boundaries of the Smart Manufacturing Intelligence Platform (SMIP) V2.

The scope describes what is included in the current implementation, what assumptions were made during development, and which areas remain outside the objectives of this version.

---

# Project Scope

SMIP V2 focuses on the design and implementation of a modern manufacturing analytics platform using the Databricks Lakehouse Platform.

The project demonstrates the complete transformation of manufacturing events into business-ready analytical datasets through a layered architecture.

The implementation emphasizes Data Engineering, dimensional modeling, and business intelligence rather than manufacturing automation or machine control.

---

# Included in Scope

The current implementation includes the following major components.

## Manufacturing Event Processing

The platform processes manufacturing events representing key stages of a production lifecycle, including:

- Work Order Creation
- Manufacturing Execution
- Machine Operations
- Quality Inspection
- Material Traceability
- Packaging

---

## Lakehouse Architecture

The project implements a complete Medallion Architecture consisting of:

- Bronze Layer
- Silver Layer
- Dimension Tables
- Fact Tables
- Gold KPI Tables

Each layer has clearly defined responsibilities within the data pipeline.

---

## Data Modeling

The analytical model includes:

- Star Schema
- Dimension Tables
- Fact Tables
- Business Keys
- Manufacturing Relationships

The model is optimized for analytical workloads and reporting.

---

## Business Intelligence

The project includes:

- Manufacturing KPI calculations
- Databricks SQL queries
- Executive manufacturing dashboard
- Operational reporting

---

## Documentation

Comprehensive technical documentation accompanies the implementation, describing:

- Architecture
- Data model
- Engineering decisions
- Pipeline implementation
- Dashboard design

---

# Out of Scope

The following areas are intentionally excluded from this version of the project.

## Production Systems

The platform does not connect directly to live manufacturing systems such as:

- Manufacturing Execution Systems (MES)
- Enterprise Resource Planning (ERP)
- Industrial PLCs
- SCADA platforms

Manufacturing events are generated through simulation to demonstrate the architecture.

---

## Real-Time Factory Operations

Although the architecture supports streaming concepts, the project is intended as a demonstration platform rather than a production deployment.

Operational concerns such as high availability, disaster recovery, and enterprise security are beyond the scope of this implementation.

---

## Advanced Analytics

The project focuses on descriptive manufacturing analytics.

Advanced topics such as:

- Predictive Maintenance
- Machine Learning
- Demand Forecasting
- Optimization Algorithms

are identified as potential future enhancements.

---

# Assumptions

Several assumptions were made during development.

- Manufacturing events follow a consistent schema.
- Business identifiers are unique.
- Production data represents a single manufacturing facility.
- Event relationships remain consistent throughout the production lifecycle.
- The platform is optimized for demonstration and educational purposes.

---

# Project Deliverables

The completed project delivers:

- Databricks Lakehouse implementation
- Medallion Architecture
- Manufacturing Star Schema
- Dimension Tables
- Fact Tables
- Gold KPI tables
- SQL dashboard
- Technical documentation
- GitHub repository

---

# Future Enhancements

Potential future developments include:

- Real-time Kafka ingestion
- IoT sensor integration
- Predictive analytics
- Multi-plant manufacturing support
- Equipment performance analytics
- Advanced manufacturing dashboards
- CI/CD deployment pipelines

---

# Summary

The scope of SMIP V2 focuses on demonstrating a complete manufacturing analytics platform built with modern Data Engineering technologies.

The implementation provides a strong foundation that can be extended to support additional manufacturing systems, advanced analytics, and enterprise-scale deployments.

---

# Next Section

**02 — Architecture**

The next chapter introduces the overall system architecture and explains how the Databricks Lakehouse Platform transforms manufacturing events into analytics-ready business information.