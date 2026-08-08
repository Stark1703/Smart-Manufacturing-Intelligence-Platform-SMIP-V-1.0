"""Base event model for manufacturing streaming events."""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict


@dataclass
class ManufacturingEvent:
    """Represents a manufacturing event emitted to the streaming pipeline."""

    event_type: str
    source: str
    payload: Dict[str, Any] = field(default_factory=dict)
    timestamp: datetime = field(default_factory=datetime.utcnow)

    def to_dict(self) -> Dict[str, Any]:
        """Convert the event to a serializable dictionary."""
        return {
            "event_type": self.event_type,
            "source": self.source,
            "payload": self.payload,
            "timestamp": self.timestamp.isoformat(),
        }
