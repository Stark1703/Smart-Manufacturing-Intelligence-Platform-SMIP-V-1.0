# Troubleshooting

## Overview

This guide lists common issues encountered while running SMIP and their recommended solutions.

---

## Python Dependencies

### Problem

```
ModuleNotFoundError
```

### Solution

Install all dependencies:

```bash
pip install -r requirements.txt
```

---

## Databricks

### Problem

Notebook cannot locate CSV files.

### Solution

Verify that:

- Unity Catalog Volume exists.
- CSV files have been uploaded.
- Configuration paths are correct.

---

## SQL Warehouse

### Problem

Power BI cannot connect.

### Solution

Verify:

- SQL Warehouse is running.
- Server Hostname is correct.
- HTTP Path is correct.
- Personal Access Token is valid.

---

## Power BI

### Problem

Relationships cannot be created.

### Solution

Ensure the Gold SQL Views have been refreshed and verify the key columns used for relationships.

---

## Generator

### Problem

Simulation fails.

### Solution

Execute the generator notebooks in the documented order and verify the master datasets are present before generating transactional data.

---

## Related Documentation

- FAQ
- Installation