
"""
generate_tool_master.py

Generate Tool Master for the Smart Manufacturing Lakehouse.

Author:
Sumanth Vempalle

Version:
1.0.0
"""

from __future__ import annotations

import logging

import pandas as pd

from generator.configs.factory_digital_twin import (
    MachineType,
    MachineStatus,
    Tool,
    ToolType,
    to_dict,
)

from generator.configs.paths import (
    MACHINES_PATH,
    TOOLS_PATH,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)-8s %(message)s",
)

logger = logging.getLogger(__name__)


# =============================================================================
# Tool Templates
# =============================================================================

TOOL_CONFIGURATION = {

    MachineType.PRESS_FITTING: {
        "tool_prefix": "TL-PF",
        "tool_name": "Hydraulic Press Tool",
        "tool_type": ToolType.PRESS_TOOL,
        "calibration": 180,
    },

    MachineType.CIRCUIT_BREAKER_ASSEMBLY: {
        "tool_prefix": "TL-ASM",
        "tool_name": "Assembly Fixture",
        "tool_type": ToolType.ASSEMBLY_FIXTURE,
        "calibration": 365,
    },

    MachineType.DEAD_TANK_ASSEMBLY: {
        "tool_prefix": "TL-DTA",
        "tool_name": "Dead Tank Fixture",
        "tool_type": ToolType.ASSEMBLY_FIXTURE,
        "calibration": 365,
    },

    MachineType.GIS_ASSEMBLY: {
        "tool_prefix": "TL-GBA",
        "tool_name": "GIS Assembly Fixture",
        "tool_type": ToolType.ASSEMBLY_FIXTURE,
        "calibration": 365,
    },

    MachineType.VISUAL_INSPECTION: {
        "tool_prefix": "TL-VIS",
        "tool_name": "Inspection Gauge",
        "tool_type": ToolType.INSPECTION_GAUGE,
        "calibration": 90,
    },

    MachineType.MECHANICAL_TEST: {
        "tool_prefix": "TL-MOT",
        "tool_name": "Mechanical Test Fixture",
        "tool_type": ToolType.INSPECTION_GAUGE,
        "calibration": 180,
    },

    MachineType.HIGH_VOLTAGE_TEST: {
        "tool_prefix": "TL-HVT",
        "tool_name": "HV Test Probe",
        "tool_type": ToolType.INSPECTION_GAUGE,
        "calibration": 180,
    },

    MachineType.PRESSURE_TEST: {
        "tool_prefix": "TL-PLT",
        "tool_name": "Pressure Test Adapter",
        "tool_type": ToolType.INSPECTION_GAUGE,
        "calibration": 180,
    },

    MachineType.PACKAGING: {
        "tool_prefix": "TL-PKG",
        "tool_name": "Packaging Fixture",
        "tool_type": ToolType.ASSEMBLY_FIXTURE,
        "calibration": 365,
    },

}


# =============================================================================
# Load Machine Master
# =============================================================================

def load_machine_master() -> pd.DataFrame:

    df = pd.read_csv(MACHINES_PATH)

    logger.info("Loaded %d machines.", len(df))

    return df


# =============================================================================
# Generate Tool Master
# =============================================================================

def generate_tools(machine_df: pd.DataFrame) -> list[Tool]:

    tools = []

    counter = 1

    for _, machine in machine_df.iterrows():

        machine_type = MachineType(machine["machine_type"])

        config = TOOL_CONFIGURATION[machine_type]

        tool = Tool(

            tool_id=f"{config['tool_prefix']}-{counter:03d}",

            machine_id=machine["machine_id"],

            tool_name=config["tool_name"],

            tool_type=config["tool_type"],

            machine_type=machine_type,

            calibration_interval_days=config["calibration"],

            status=MachineStatus.ACTIVE,

        )

        tools.append(tool)

        counter += 1

    logger.info("Generated %d tools.", len(tools))

    return tools


# =============================================================================
# Validation
# =============================================================================

def validate_tools(tools: list[Tool]) -> None:

    ids = {tool.tool_id for tool in tools}

    if len(ids) != len(tools):
        raise ValueError("Duplicate Tool IDs detected.")

    logger.info("Tool validation successful.")


# =============================================================================
# Export
# =============================================================================

def export_tools(tools: list[Tool]) -> None:

    TOOLS_PATH.parent.mkdir(parents=True, exist_ok=True)

    df = pd.DataFrame(to_dict(tools))

    df.to_csv(TOOLS_PATH, index=False)

    logger.info("Exported Tool Master.")


# =============================================================================
# Main
# =============================================================================

def main():

    logger.info("Generating Tool Master...")

    machine_df = load_machine_master()

    tools = generate_tools(machine_df)

    validate_tools(tools)

    export_tools(tools)

    logger.info("Tool Master generation completed.")


if __name__ == "__main__":
    main()








