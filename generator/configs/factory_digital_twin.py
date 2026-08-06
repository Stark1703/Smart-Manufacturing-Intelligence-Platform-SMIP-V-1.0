"""
factory_digital_twin.py

Digital Twin configuration for the Smart Manufacturing Lakehouse.

This file defines the structure of the manufacturing plant and all
master data used by the simulation engine.

Author:
Sumanth Vempalle

Version:
1.0
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Optional
from datetime import datetime

# =============================================================================
# ENUMS
# =============================================================================


class MachineStatus(Enum):
    ACTIVE = "Active"
    MAINTENANCE = "Maintenance"
    OUT_OF_SERVICE = "Out of Service"


class ShiftType(Enum):
    MORNING = "Morning"
    EVENING = "Evening"
    NIGHT = "Night"

    @property
    def release_time(self):
        from generator.configs.simulation_config import SHIFT_RELEASE_TIME
        return SHIFT_RELEASE_TIME[self.value]

    @property
    def start_time(self):
        from generator.configs.simulation_config import SHIFT_TIMES
        return SHIFT_TIMES[self.value]["start"]

    @property
    def end_time(self):
        from generator.configs.simulation_config import SHIFT_TIMES
        return SHIFT_TIMES[self.value]["end"]

class QualityResult(Enum):
    PASS = "PASS"
    FAIL = "FAIL"


class ProductFamily(Enum):
    GIS_BAY = "GIS Bay"
    CIRCUIT_BREAKER = "Circuit Breaker"
    DISCONNECTOR = "Disconnector"
    EARTHING_SWITCH = "Earthing Switch"
    CURRENT_TRANSFORMER = "Current Transformer"
    VOLTAGE_TRANSFORMER = "Voltage Transformer"


class MachineType(Enum):
    PRESS_FITTING = "Press Fitting Machine"
    CIRCUIT_BREAKER_ASSEMBLY = "Circuit Breaker Assembly"
    DEAD_TANK_ASSEMBLY = "Dead Tank Assembly"
    GIS_ASSEMBLY = "GIS Bay Assembly"
    VISUAL_INSPECTION = "Visual Inspection"
    MECHANICAL_TEST = "Mechanical Test Bench"
    HIGH_VOLTAGE_TEST = "High Voltage Test Bench"
    PRESSURE_TEST = "Pressure Leak Test Bench"
    PACKAGING = "Packaging Station"
  

class StationType(Enum):
    PRESS_FITTING = "Press Fitting"
    CIRCUIT_BREAKER_ASSEMBLY = "Circuit Breaker Assembly"
    DEAD_TANK_ASSEMBLY = "Dead Tank Assembly"
    GIS_ASSEMBLY = "GIS Bay Assembly"
    VISUAL_INSPECTION = "Visual Inspection"
    MECHANICAL_TEST = "Mechanical Test"
    HIGH_VOLTAGE_TEST = "HV Test"
    PRESSURE_TEST = "Pressure Test"
    PACKAGING = "Packaging"

class OperatorSkill(Enum):
    TRAINEE = "Trainee"
    JUNIOR = "Junior"
    SENIOR = "Senior"
    EXPERT = "Expert"

class ToolType(Enum):
    PRESS_TOOL = "Press Tool"
    ASSEMBLY_FIXTURE = "Assembly Fixture"
    TORQUE_TOOL = "Torque Tool"
    INSPECTION_GAUGE = "Inspection Gauge"



class TestType(Enum):
    MECHANICAL = "Mechanical"
    DIELECTRIC = "Dielectric"
    PRESSURE = "Pressure Leak"



class MaintenanceType(Enum):
    PREVENTIVE = "Preventive"
    CORRECTIVE = "Corrective"
    PREDICTIVE = "Predictive"



class PackagingType(Enum):
    EXPORT_CRATE = "Export Wooden Crate"
    DOMESTIC = "Domestic Shipment"
    CONTAINER = "Container Shipment"


class Department(Enum):
    PRESS_SHOP = "Press Shop"
    ASSEMBLY = "Assembly"
    QUALITY = "Quality"
    TESTING = "Testing"
    LOGISTICS = "Logistics"



class WorkOrderStatus(Enum):
    RELEASED = "Released"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"


class ExecutionStatus(Enum):
    PLANNED = "Planned"
    READY = "Ready"
    RUNNING = "Running"
    PAUSED = "Paused"
    COMPLETED = "Completed"
    FAILED = "Failed"
    CANCELLED = "Cancelled"

class SerialStatus(Enum):
    IN_PRODUCTION = "In Production"
    COMPLETED = "Completed"
    SCRAPPED = "Scrapped"
    REWORK = "Rework"

class Priority(Enum):
    LOW = "Low"
    NORMAL = "Normal"
    HIGH = "High"
    URGENT = "Urgent"


@dataclass(slots=True)
class Factory:

    factory_id: str

    name: str

    country: str

    city: str

    plant_code: str

    business_unit: str

    erp_system: str

    mes_system: str

    data_platform: str

    production_halls: int

    production_lines: int

    shifts: int


from datetime import datetime

@dataclass(slots=True)
class WorkOrder:

    work_order_id: str

    sap_order_number: str

    product_code: str

    quantity: int

    production_line: str

    priority: Priority

    planned_shift: ShiftType

    planned_start: datetime

    planned_finish: datetime

    routing_version: str

    planner: str

    status: WorkOrderStatus


@dataclass(slots=True)
class ProductionExecution:

    execution_id: str

    work_order_id: str

    sap_order_number: str

    product_code: str

    quantity: int

    plant_code: str

    production_line: str

    planned_shift: ShiftType

    execution_start: datetime

    execution_end: datetime

    status: ExecutionStatus

@dataclass(slots=True)
class SerialNumber:

    serial_number: str

    execution_id: str

    work_order_id: str

    sap_order_number: str

    product_code: str

    product_name: str

    production_line: str

    manufacturing_date: datetime

    status: SerialStatus


@dataclass(slots=True)
class PressOperation:

    press_operation_id: str

    serial_number: str

    execution_id: str

    work_order_id: str

    operation_number: int

    operation_name: str

    machine_id: str

    tool_id: str

    operator_id: str

    press_program_id: str

    operation_start: datetime

    operation_end: datetime

    target_force_kn: float

    actual_force_kn: float

    force_deviation_kn: float

    displacement_mm: float      # <-- ADD THIS

    cycle_time_sec: int

    quality_result: QualityResult


@dataclass(slots=True)
class ForceCurvePoint:

    point_id: str

    press_operation_id: str

    serial_number: str

    sample_number: int

    timestamp_ms: int

    displacement_mm: float

    force_kn: float


@dataclass(slots=True)
class TestResult:

    test_result_id: str

    serial_number: str

    execution_id: str

    product_code: str

    test_program_id: str

    test_name: str

    target_value: float

    measured_value: float

    unit: str

    result: QualityResult

    start_time: datetime

    end_time: datetime


@dataclass(slots=True)
class Packaging:

    package_id: str

    serial_number: str

    execution_id: str

    product_code: str

    package_type: str

    package_weight_kg: float

    package_length_mm: int

    package_width_mm: int

    package_height_mm: int

    packaging_start: datetime

    packaging_end: datetime

    packaging_status: str

@dataclass(slots=True)
class MaterialScan:

    scan_id: str

    serial_number: str

    execution_id: str

    product_code: str

    material_number: str

    batch_number: str

    supplier: str

    scan_timestamp: datetime

    scan_status: str

@dataclass(slots=True)
class ProductionHall:

    hall_id: str

    hall_name: str

    description: str



@dataclass(slots=True)
class ProductionLine:

    line_id: str

    hall_id: str

    line_name: str

    description: str

    status: MachineStatus


@dataclass(slots=True)
class Station:

    station_id: str

    line_id: str

    station_code: str

    station_type: StationType

    sequence: int



@dataclass(slots=True)
class Machine:

    machine_id: str

    line_id: str

    station_id: str

    station_sequence: int

    machine_name: str

    machine_type: MachineType

    manufacturer: str

    status: MachineStatus

    commissioned_year: int



@dataclass(slots=True)
class Operator:

    operator_id: str

    first_name: str

    last_name: str

    employee_number: str

    shift: ShiftType

    skill_level: OperatorSkill

    primary_machine_type: MachineType

    years_of_experience: int

    mes_authorized: bool

    active: bool = True

@dataclass(slots=True)
class OperatorLogin:

    login_id: str

    operator_id: str

    machine_id: str

    execution_id: str

    work_order_id: str

    shift: str

    login_time: datetime

    logout_time: datetime

    login_status: str

@dataclass(slots=True, frozen=True)
class Operation:

    operation_id: str

    operation_number: int

    operation_code: str

    operation_name: str

    department: Department

    station_type: StationType

    machine_type: MachineType

    requires_operator: bool

    requires_tool: bool

    quality_checkpoint: bool

    standard_cycle_time_sec: int

    predecessor_operation: int | None = None

    is_mandatory: bool = True



@dataclass(slots=True)
class Tool:

    tool_id: str

    machine_id: str

    tool_name: str

    tool_type: ToolType

    machine_type: MachineType

    calibration_interval_days: int

    last_calibration: Optional[str] = None

    next_calibration: Optional[str] = None

    status: MachineStatus = MachineStatus.ACTIVE


@dataclass(slots=True, frozen=True)
class Product:

    product_id: str
    product_code: str
    product_name: str
    family: ProductFamily

    rated_voltage_kv: float
    rated_current_a: int
    short_circuit_rating_ka: float

    target_force_kn: float
    force_tolerance_kn: float

    average_cycle_time_sec: int

    dielectric_test_voltage_kv: float
    pressure_test_bar: float



@dataclass(slots=True)
class PressProgram:

    program_id: str

    product_code: str

    operation_number: int

    operation_name: str

    machine_type: MachineType

    tool_type: ToolType

    target_force_kn: float

    force_tolerance_kn: float

    minimum_force_kn: float

    maximum_force_kn: float

    target_displacement_mm: float

    displacement_tolerance_mm: float

    maximum_cycle_time_sec: int

    active: bool = True



@dataclass(slots=True)
class TestProgram:

    program_id: str

    product_code: str

    operation_code: str

    test_type: TestType

    test_name: str

    target_value: float

    minimum_value: float

    maximum_value: float

    unit: str

    standard_duration_sec: int

    active: bool = True





@dataclass(slots=True)

class FactoryLayout:

    factory: Factory

    halls: list[ProductionHall]

    lines: list[ProductionLine]

    stations: list[Station]

    machines: list[Machine]

    tools: list[Tool]

    products: list[Product]

    press_programs: list[PressProgram]

    test_programs: list[TestProgram]



from dataclasses import asdict
from enum import Enum


def to_dict(objects: list) -> list[dict]:
    """
    Convert dataclass objects into dictionaries.
    Serialize Enum values before exporting to CSV.
    """

    rows = []

    for obj in objects:

        row = asdict(obj)

        for key, value in row.items():

            if isinstance(value, Enum):
                row[key] = value.value

        rows.append(row)

    return rows




