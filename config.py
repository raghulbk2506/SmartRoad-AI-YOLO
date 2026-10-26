"""Central configuration defaults for SmartRoad AI."""
from dataclasses import dataclass

@dataclass(frozen=True)
class DetectionConfig:
    confidence_threshold: float = 0.35
    vehicle_classes: tuple[str, ...] = ("car", "motorcycle", "bus", "truck")
    congestion_low_max: int = 5
    congestion_medium_max: int = 12
    parking_zone: tuple[int, int, int, int] | None = None

DEFAULT_CONFIG = DetectionConfig()
