"""
production_planner.py

Production Planning Engine for the Smart Manufacturing Lakehouse.

This module generates realistic SAP work orders based on the
Product Master and simulation configuration.

Author:
Sumanth Vempalle + ChatGPT

Version:
1.0.0
"""

from __future__ import annotations

import random

from datetime import datetime
from datetime import timedelta

import pandas as pd

from generator.configs.factory_digital_twin import (
    Priority,
    ShiftType,
    WorkOrder,
    WorkOrderStatus,
)

from generator.configs.simulation_config import (
    START_DATE,
    SIMULATION_DAYS,
    MIN_WORK_ORDERS_PER_DAY,
    MAX_WORK_ORDERS_PER_DAY,
    PRODUCT_SELECTION_WEIGHTS,
    PRODUCTION_LINES,
    ROUTING_VERSION,
    PLANNER_NAME,
    RANDOM_SEED,
)


class ProductionPlanner:
    """
    Production Planning Engine.

    Responsibilities
    ----------------
    - Generate daily production plans
    - Select products using weighted probabilities
    - Generate SAP Work Orders
    - Assign production lines
    - Assign priorities
    - Calculate planned start and finish timestamps
    """

    def __init__(self, products: pd.DataFrame):

        self.products = products

        self.random = random.Random(RANDOM_SEED)

        self.current_date = START_DATE

        self.work_order_counter = 1

        self.sap_counter = 5_000_000_000

        self.line_counter = 0

    # ============================================================
    # Public API
    # ============================================================

    def generate(self) -> list[WorkOrder]:
        """
        Generate all work orders for the configured
        simulation period.
        """

        work_orders: list[WorkOrder] = []

        for _ in range(SIMULATION_DAYS):

            work_orders.extend(
                self._generate_day()
            )

            self.current_date += timedelta(days=1)

        return work_orders

    # ============================================================
    # Daily Planning
    # ============================================================

    def _generate_day(self) -> list[WorkOrder]:
        """
        Generate one production day.
        """

        daily_orders: list[WorkOrder] = []

        order_count = self.random.randint(
            MIN_WORK_ORDERS_PER_DAY,
            MAX_WORK_ORDERS_PER_DAY,
        )

        release_time = datetime.combine(
            self.current_date,
            ShiftType.MORNING.release_time,
        )

        for index in range(order_count):

            planned_start = (
                release_time +
                timedelta(minutes=index * 20)
            )

            daily_orders.append(
                self._create_work_order(
                    planned_start
                )
            )

        return daily_orders

    # ============================================================
    # Work Order Creation
    # ============================================================

    def _create_work_order(
        self,
        planned_start: datetime,
    ) -> WorkOrder:
        """
        Create one WorkOrder object.
        """

        product = self._select_product()

        quantity = self._select_quantity(
            product
        )

        cycle_time = int(
            product["average_cycle_time_sec"]
        )

        planned_finish = (
            planned_start +
            timedelta(
                minutes=max(
                    quantity * cycle_time / 60,
                    30,
                )
            )
        )

        return WorkOrder(

            work_order_id=self._next_work_order_id(),

            sap_order_number=self._next_sap_order(),

            product_code=product["product_code"],

            quantity=quantity,

            production_line=self._next_line(),

            priority=self._select_priority(),

            planned_shift=ShiftType.MORNING,

            planned_start=planned_start,

            planned_finish=planned_finish,

            routing_version=ROUTING_VERSION,

            planner=PLANNER_NAME,

            status=WorkOrderStatus.RELEASED,

        )

    # ============================================================
    # Product Selection
    # ============================================================

    def _select_product(self) -> pd.Series:
        """
        Select a product using weighted probabilities.
        """

        product_codes = list(PRODUCT_SELECTION_WEIGHTS.keys())
        weights = list(PRODUCT_SELECTION_WEIGHTS.values())

        selected_code = self.random.choices(
            population=product_codes,
            weights=weights,
            k=1,
        )[0]

        product = self.products.loc[
            self.products["product_code"] == selected_code
        ]

        return product.iloc[0]

    # ============================================================
    # Quantity Selection
    # ============================================================

    def _select_quantity(
        self,
        product: pd.Series,
    ) -> int:
        """
        Determine production quantity based on
        rated voltage.
        """

        voltage = float(product["rated_voltage_kv"])

        if voltage <= 72.5:
            return self.random.randint(3, 5)

        if voltage <= 145:
            return self.random.randint(2, 4)

        if voltage <= 170:
            return self.random.randint(2, 3)

        if voltage <= 245:
            return self.random.randint(1, 3)

        if voltage <= 420:
            return self.random.randint(1, 2)

        return 1

    # ============================================================
    # Priority Selection
    # ============================================================

    def _select_priority(self) -> Priority:
        """
        Select work order priority.
        """

        priorities = [
            Priority.LOW,
            Priority.NORMAL,
            Priority.HIGH,
            Priority.URGENT,
        ]

        weights = [10, 65, 20, 5]

        return self.random.choices(
            population=priorities,
            weights=weights,
            k=1,
        )[0]

    # ============================================================
    # Production Line Allocation
    # ============================================================

    def _next_line(self) -> str:
        """
        Allocate work orders using round-robin scheduling.
        """

        line = PRODUCTION_LINES[self.line_counter]

        self.line_counter += 1

        if self.line_counter >= len(PRODUCTION_LINES):
            self.line_counter = 0

        return line

    # ============================================================
    # Work Order ID Generation
    # ============================================================

    def _next_work_order_id(self) -> str:
        """
        Generate unique Work Order ID.
        """

        work_order = (
            f"WO-"
            f"{self.current_date:%Y%m%d}-"
            f"{self.work_order_counter:06d}"
        )

        self.work_order_counter += 1

        return work_order

    # ============================================================
    # SAP Order Number Generation
    # ============================================================

    def _next_sap_order(self) -> str:
        """
        Generate SAP Production Order number.
        """

        self.sap_counter += 1

        return str(self.sap_counter)

    # ============================================================
    # Summary
    # ============================================================

    def summary(
        self,
        work_orders: list[WorkOrder],
    ) -> None:
        """
        Print a summary of generated work orders.
        """

        print("\n========================================")
        print(" Production Planning Summary")
        print("========================================")
        print(f"Simulation Days : {SIMULATION_DAYS}")
        print(f"Work Orders     : {len(work_orders)}")
        print(f"Products         : {self.products['product_code'].nunique()}")
        print(f"Production Lines : {len(PRODUCTION_LINES)}")
        print("========================================")
