# Export to Power BI

## Overview

Power BI consumes manufacturing data directly from the Databricks SQL Warehouse through SQL Views.

This approach eliminates the need for manual CSV exports and ensures dashboards always use the latest Gold Layer data.

---

## Data Flow

```text
Gold Delta Tables
        │
        ▼
SQL Views
        │
        ▼
Databricks SQL Warehouse
        │
        ▼
Power BI
```

---

## Export Options

### Direct Connection (Recommended)

Power BI connects directly to Databricks SQL Views.

Advantages:

- Real-time reporting
- No manual exports
- Centralized governance

### CSV Export

SMIP also provides notebooks to export Gold datasets as CSV files for offline analysis.

---

## Benefits

- Simplified reporting
- Automatic data refresh
- Reduced maintenance
- Single source of truth

---

## Related Documentation

- SQL Views
- Power BI Overview