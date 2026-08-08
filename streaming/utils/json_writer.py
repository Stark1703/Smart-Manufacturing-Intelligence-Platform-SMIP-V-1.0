"""Utility helpers for writing JSON payloads."""

import json
from pathlib import Path
from typing import Any, Dict


def write_json(path: str, data: Dict[str, Any]) -> None:
    """Write a JSON payload to disk."""
    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as handle:
        json.dump(data, handle, indent=2, default=str)
