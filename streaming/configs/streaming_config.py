"""
streaming_config.py

Streaming configuration for the Smart Manufacturing Intelligence Platform (SMIP).

This module contains all configuration parameters used by the
real-time manufacturing event simulator.

Author:
Sumanth Vempalle + ChatGPT

Version:
2.0.0
"""

from __future__ import annotations

from pathlib import Path

# ============================================================
# Streaming Directories
# ============================================================

# Root directory for streaming events
STREAMING_ROOT = Path("streaming_data")

# JSON event output directory
STREAMING_EVENTS_PATH = STREAMING_ROOT / "events"

# Checkpoint directory (used by Databricks Auto Loader)
CHECKPOINT_PATH = STREAMING_ROOT / "checkpoints"

# Archive directory for processed events
ARCHIVE_PATH = STREAMING_ROOT / "archive"

# ============================================================
# Simulation Configuration
# ============================================================

# Random seed for reproducibility
RANDOM_SEED = 42

# Number of events generated in each batch
EVENTS_PER_BATCH = 5

# Delay between batches (seconds)
EVENT_INTERVAL_SECONDS = 1

# Maximum number of events to generate
MAX_EVENTS = 1000

# ============================================================
# Event Configuration
# ============================================================

# Event ID prefix
EVENT_ID_PREFIX = "EVT"

# Manufacturing plant
PLANT_CODE = "PLANT-001"

# ============================================================
# Supported Event Types
# ============================================================

DEFAULT_EVENT_TYPES = [

    "WORK_ORDER_CREATED",

    "EXECUTION_STARTED",

    "PRESS_OPERATION",

    "QUALITY_COMPLETED",

    "MATERIAL_SCANNED",

    "PACKAGING_COMPLETED",

]

# ============================================================
# JSON Configuration
# ============================================================

JSON_INDENT = 4

JSON_ENCODING = "utf-8"

# ============================================================
# Auto Loader Configuration
# ============================================================

AUTO_LOADER_FORMAT = "json"

AUTO_LOADER_SCHEMA_EVOLUTION = True

AUTO_LOADER_INCLUDE_EXISTING_FILES = True

# ============================================================
# Logging
# ============================================================

LOG_LEVEL = "INFO"

# ============================================================
# Create Directories
# ============================================================

STREAMING_EVENTS_PATH.mkdir(
    parents=True,
    exist_ok=True,
)

CHECKPOINT_PATH.mkdir(
    parents=True,
    exist_ok=True,
)

ARCHIVE_PATH.mkdir(
    parents=True,
    exist_ok=True,
)