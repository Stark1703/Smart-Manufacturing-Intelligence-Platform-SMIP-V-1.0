"""
event_types.py

Manufacturing Event Types for the Smart Manufacturing Intelligence Platform (SMIP).

This module defines all supported manufacturing events used by the
real-time streaming simulator.

Author:
Sumanth Vempalle + ChatGPT

Version:
2.0.0
"""

from __future__ import annotations

from enum import Enum


class EventType(Enum):
    """
    Supported manufacturing event types.
    """

    # ============================================================
    # ERP Events
    # ============================================================

    WORK_ORDER_CREATED = "WORK_ORDER_CREATED"

    # ============================================================
    # MES Events
    # ============================================================

    EXECUTION_STARTED = "EXECUTION_STARTED"

    EXECUTION_COMPLETED = "EXECUTION_COMPLETED"

    # ============================================================
    # Production Events
    # ============================================================

    PRESS_OPERATION = "PRESS_OPERATION"

    # ============================================================
    # Quality Events
    # ============================================================

    QUALITY_COMPLETED = "QUALITY_COMPLETED"

    # ============================================================
    # Traceability Events
    # ============================================================

    MATERIAL_SCANNED = "MATERIAL_SCANNED"

    SERIAL_NUMBER_ASSIGNED = "SERIAL_NUMBER_ASSIGNED"

    # ============================================================
    # Packaging Events
    # ============================================================

    PACKAGING_COMPLETED = "PACKAGING_COMPLETED"

    # ============================================================
    # Future Event Types (SMIP v2.x)
    # ============================================================

    MACHINE_STATUS_CHANGED = "MACHINE_STATUS_CHANGED"

    MAINTENANCE_STARTED = "MAINTENANCE_STARTED"

    MAINTENANCE_COMPLETED = "MAINTENANCE_COMPLETED"

    ENERGY_RECORDED = "ENERGY_RECORDED"

    SENSOR_READING = "SENSOR_READING"

    ALERT_CREATED = "ALERT_CREATED"

    PREDICTION_GENERATED = "PREDICTION_GENERATED"

    API_REQUEST = "API_REQUEST"

    @classmethod
    def values(cls) -> list[str]:
        """
        Return all event type values.
        """

        return [event.value for event in cls]