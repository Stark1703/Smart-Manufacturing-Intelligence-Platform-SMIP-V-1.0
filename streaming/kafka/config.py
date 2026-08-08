"""
config.py

Kafka configuration for the Smart Manufacturing Intelligence Platform (SMIP).

Author:
Sumanth Vempalle

Version:
2.0.0
"""

from __future__ import annotations

# ============================================================
# Kafka Broker
# ============================================================

BOOTSTRAP_SERVERS = [
    "localhost:9092",
]

# ============================================================
# Producer Configuration
# ============================================================

CLIENT_ID = "smip-streaming-producer"

ACKS = "all"

RETRIES = 5

REQUEST_TIMEOUT_MS = 30000

LINGER_MS = 5

BATCH_SIZE = 16384

MAX_IN_FLIGHT_REQUESTS = 5