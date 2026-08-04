"""
generate_machine_layout.py

Generate the complete machine layout for the Smart Manufacturing Lakehouse.

Author:
Sumanth Vempalle

Version:
1.0.0
"""

from __future__ import annotations

import logging

from generator.configs.factory_digital_twin import (
    Machine,
    MachineStatus,
    MachineType,
    ProductionHall,
    ProductionLine,
    Station,
    StationType,
)

# =============================================================================
# Logging
# =============================================================================

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)-8s %(message)s",
)

logger = logging.getLogger(__name__)

# =============================================================================
# Factory Configuration
# =============================================================================

NUMBER_OF_HALLS = 2
LINES_PER_HALL = 3

HALL_NAMES = [
    "Production Hall A",
    "Production Hall B",
]

# =============================================================================
# Station Templates
# =============================================================================

STATION_TEMPLATES = [
    ("S10", 10, StationType.PRESS_FITTING),
    ("S20", 20, StationType.CIRCUIT_BREAKER_ASSEMBLY),
    ("S30", 30, StationType.DEAD_TANK_ASSEMBLY),
    ("S40", 40, StationType.GIS_ASSEMBLY),
    ("S50", 50, StationType.VISUAL_INSPECTION),
    ("S60", 60, StationType.MECHANICAL_TEST),
    ("S70", 70, StationType.HIGH_VOLTAGE_TEST),
    ("S80", 80, StationType.PRESSURE_TEST),
    ("S90", 90, StationType.PACKAGING),
]

# =============================================================================
# Machine Templates
# =============================================================================

MACHINE_TEMPLATES = [
    {
        "station": StationType.PRESS_FITTING,
        "prefix": "PF",
        "name": "Press Fitting Machine",
        "manufacturer": "Kistler",
        "machine_type": MachineType.PRESS_FITTING,
    },
    {
        "station": StationType.CIRCUIT_BREAKER_ASSEMBLY,
        "prefix": "ASM",
        "name": "Circuit Breaker Assembly Station",
        "manufacturer": "VoltGrid",
        "machine_type": MachineType.CIRCUIT_BREAKER_ASSEMBLY,
    },
    {
        "station": StationType.DEAD_TANK_ASSEMBLY,
        "prefix": "DTA",
        "name": "Dead Tank Assembly Station",
        "manufacturer": "VoltGrid",
        "machine_type": MachineType.DEAD_TANK_ASSEMBLY,
    },
    {
        "station": StationType.GIS_ASSEMBLY,
        "prefix": "GBA",
        "name": "GIS Bay Assembly Station",
        "manufacturer": "VoltGrid",
        "machine_type": MachineType.GIS_ASSEMBLY,
    },
    {
        "station": StationType.VISUAL_INSPECTION,
        "prefix": "VIS",
        "name": "Visual Inspection Station",
        "manufacturer": "Keyence",
        "machine_type": MachineType.VISUAL_INSPECTION,
    },
    {
        "station": StationType.MECHANICAL_TEST,
        "prefix": "MOT",
        "name": "Mechanical Test Bench",
        "manufacturer": "ABB",
        "machine_type": MachineType.MECHANICAL_TEST,
    },
    {
        "station": StationType.HIGH_VOLTAGE_TEST,
        "prefix": "HVT",
        "name": "High Voltage Test Bench",
        "manufacturer": "Haefely",
        "machine_type": MachineType.HIGH_VOLTAGE_TEST,
    },
    {
        "station": StationType.PRESSURE_TEST,
        "prefix": "PLT",
        "name": "Pressure Leak Test Bench",
        "manufacturer": "ATEQ",
        "machine_type": MachineType.PRESSURE_TEST,
    },
    {
        "station": StationType.PACKAGING,
        "prefix": "PKG",
        "name": "Packaging Station",
        "manufacturer": "VoltGrid",
        "machine_type": MachineType.PACKAGING,
    },
]

# =============================================================================
# Helper Functions
# =============================================================================

def line_id(line_number: int) -> str:
    """Return formatted production line ID."""
    return f"LINE-{line_number:02d}"


def hall_id(hall_number: int) -> str:
    """Return formatted production hall ID."""
    return f"HALL-{hall_number:02d}"


def machine_id(prefix: str, line_number: int, station_code: str) -> str:
    """Return formatted machine ID."""
    return f"{prefix}-L{line_number}-{station_code}"


def station_id(line_number: int, station_code: str) -> str:
    """Return formatted station ID."""
    return f"L{line_number}-{station_code}"


def get_machine_template(station_type: StationType) -> dict:
    """
    Return the machine template associated with a station type.
    """
    for template in MACHINE_TEMPLATES:
        if template["station"] == station_type:
            return template

    raise ValueError(f"No machine template defined for {station_type}")





# =============================================================================
# Production Hall Generator
# =============================================================================

def generate_production_halls() -> list[ProductionHall]:
    """
    Generate all production halls in the factory.
    """
    halls: list[ProductionHall] = []

    for hall_number in range(1, NUMBER_OF_HALLS + 1):

        halls.append(
            ProductionHall(
                hall_id=hall_id(hall_number),
                hall_name=HALL_NAMES[hall_number - 1],
                description=f"Main manufacturing hall {hall_number}",
            )
        )

    logger.info("Generated %d production halls", len(halls))

    return halls


# =============================================================================
# Production Line Generator
# =============================================================================

def generate_production_lines() -> list[ProductionLine]:
    """
    Generate all production lines.

    Hall 1
        LINE-01
        LINE-02
        LINE-03

    Hall 2
        LINE-04
        LINE-05
        LINE-06
    """

    lines: list[ProductionLine] = []

    line_number = 1

    for hall_number in range(1, NUMBER_OF_HALLS + 1):

        current_hall = hall_id(hall_number)

        for _ in range(LINES_PER_HALL):

            lines.append(
                ProductionLine(
                    line_id=line_id(line_number),
                    hall_id=current_hall,
                    line_name=f"Production Line {line_number}",
                    description=f"GIS Assembly Production Line {line_number}",
                    status=MachineStatus.ACTIVE,
                )
            )

            line_number += 1

    logger.info("Generated %d production lines", len(lines))

    return lines


# =============================================================================
# Station Generator
# =============================================================================

def generate_stations() -> list[Station]:
    """
    Generate all stations for every production line.

    Every line contains:

        S10 Press Fitting
        S20 Circuit Breaker Assembly
        S30 Dead Tank Assembly
        S40 GIS Assembly
        S50 Visual Inspection
        S60 Mechanical Test
        S70 High Voltage Test
        S80 Pressure Test
        S90 Packaging
    """

    stations: list[Station] = []

    total_lines = NUMBER_OF_HALLS * LINES_PER_HALL

    for line_number in range(1, total_lines + 1):

        for station_code, sequence, station_type in STATION_TEMPLATES:

            stations.append(
                Station(
                    station_id=station_id(
                        line_number=line_number,
                        station_code=station_code,
                    ),
                    line_id=line_id(line_number),
                    station_code=station_code,
                    station_type=station_type,
                    sequence=sequence,
                )
            )

    logger.info("Generated %d stations", len(stations))

    return stations



# =============================================================================
# Machine Generator
# =============================================================================

def generate_machines() -> list[Machine]:
    """
    Generate one machine for every station in every production line.

    Returns
    -------
    list[Machine]
    """

    machines: list[Machine] = []

    total_lines = NUMBER_OF_HALLS * LINES_PER_HALL

    for line_number in range(1, total_lines + 1):

        for station_code, sequence, station_type in STATION_TEMPLATES:

            template = get_machine_template(station_type)

            machines.append(
                Machine(
                    machine_id=machine_id(
                        prefix=template["prefix"],
                        line_number=line_number,
                        station_code=station_code,
                    ),
                    line_id=line_id(line_number),
                    station_id=station_id(
                        line_number=line_number,
                        station_code=station_code,
                    ),
                    station_sequence=sequence,
                    machine_name=template["name"],
                    machine_type=template["machine_type"],
                    manufacturer=template["manufacturer"],
                    status=MachineStatus.ACTIVE,
                    commissioned_year=2024,
                )
            )

    logger.info("Generated %d machines", len(machines))

    return machines


# =============================================================================
# Validation
# =============================================================================

def validate_machine_layout(machines: list[Machine]) -> None:
    """
    Validate generated machine layout.
    """

    machine_ids = {machine.machine_id for machine in machines}

    if len(machine_ids) != len(machines):
        raise ValueError("Duplicate machine IDs detected.")

    expected_machine_count = (
        NUMBER_OF_HALLS
        * LINES_PER_HALL
        * len(STATION_TEMPLATES)
    )

    if len(machines) != expected_machine_count:
        raise ValueError(
            f"Expected {expected_machine_count} machines "
            f"but generated {len(machines)}."
        )

    logger.info("Machine layout validation successful.")


# =============================================================================
# Factory Layout Builder
# =============================================================================

def build_factory_layout() -> FactoryLayout:
    """
    Build the complete factory layout.

    Returns
    -------
    FactoryLayout
    """

    logger.info("Building factory layout...")

    factory = Factory(
        factory_id="FG-001",
        name="VoltGrid Manufacturing",
        country="Czech Republic",
        city="Brno",
        plant_code="CZ-BR-01",
        business_unit="Grid Solutions",
        erp_system="SAP S/4HANA",
        mes_system="VoltMES",
        data_platform="Azure Databricks",
        production_halls=NUMBER_OF_HALLS,
        production_lines=NUMBER_OF_HALLS * LINES_PER_HALL,
        shifts=3,
    )

    halls = generate_production_halls()

    lines = generate_production_lines()

    stations = generate_stations()

    machines = generate_machines()

    validate_machine_layout(machines)

    layout = FactoryLayout(
        factory=factory,
        halls=halls,
        lines=lines,
        stations=stations,
        machines=machines,
        tools=[],
        products=[],
        press_programs=[],
        test_programs=[],
    )

    logger.info("Factory layout successfully created.")

    return layout


# =============================================================================
# CSV Export
# =============================================================================

import pandas as pd

from generator.configs.factory_digital_twin import to_dict
from paths import (
    HALLS_PATH,
    LINES_PATH,
    MACHINES_PATH,
    STATIONS_PATH,
)


def export_factory_layout(layout: FactoryLayout) -> None:
    """
    Export the complete factory layout to CSV files.
    """

    HALLS_PATH.parent.mkdir(parents=True, exist_ok=True)

    pd.DataFrame(to_dict(layout.halls)).to_csv(
        HALLS_PATH,
        index=False,
    )

    pd.DataFrame(to_dict(layout.lines)).to_csv(
        LINES_PATH,
        index=False,
    )

    pd.DataFrame(to_dict(layout.stations)).to_csv(
        STATIONS_PATH,
        index=False,
    )

    pd.DataFrame(to_dict(layout.machines)).to_csv(
        MACHINES_PATH,
        index=False,
    )

    logger.info("Factory layout exported successfully.")


# =============================================================================
# Summary
# =============================================================================

def print_summary(layout: FactoryLayout) -> None:
    """
    Print a summary of the generated factory.
    """

    logger.info("===========================================")
    logger.info("FACTORY DIGITAL TWIN")
    logger.info("===========================================")

    logger.info("Factory           : %s", layout.factory.name)

    logger.info("Production Halls  : %d", len(layout.halls))

    logger.info("Production Lines  : %d", len(layout.lines))

    logger.info("Stations          : %d", len(layout.stations))

    logger.info("Machines          : %d", len(layout.machines))

    logger.info("===========================================")



# =============================================================================
# Main
# =============================================================================

def main() -> None:

    logger.info("Starting Machine Layout Generation...")

    layout = build_factory_layout()

    export_factory_layout(layout)

    print_summary(layout)

    logger.info("Machine Layout Generation Completed.")


if __name__ == "__main__":
    main()








































