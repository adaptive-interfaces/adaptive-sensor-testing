"""
models.py: Shared domain models for synthetic PTAT sensor data.
"""

from dataclasses import dataclass
from typing import Literal

ScenarioKind = Literal[
    "clean",
    "drift",
    "spike",
    "dropout",
    "multi_sensor_divergence",
]


@dataclass(frozen=True)
class SensorReading:
    """A single PTAT-style sensor reading."""

    sample_index: int
    sensor_id: str
    temperature_celsius: float
    frequency_hz: float | None


@dataclass(frozen=True)
class GeneratorConfig:
    """Configuration for synthetic PTAT data generation."""

    batch_size: int = 1000
    num_sensors: int = 1
    sampling_rate_hz: int = 10
    base_temperature_celsius: float = 25.0
    temperature_step_celsius: float = 0.02
    nominal_frequency_at_25c_hz: float = 100000.0
    sensitivity_hz_per_kelvin: float = 512.0
    noise_stddev_hz: float = 8.0
    seed: int = 42


@dataclass(frozen=True)
class AnomalyFinding:
    """A single anomaly or suspicious finding."""

    sensor_id: str
    kind: str
    start_sample: int
    end_sample: int
    message: str
    severity: str


@dataclass(frozen=True)
class BatchResult:
    """Structured analysis result for a batch of readings."""

    total_readings: int
    sensors: tuple[str, ...]
    findings: tuple[AnomalyFinding, ...]

    @property
    def has_findings(self) -> bool:
        """Return True when any anomaly or suspicious pattern was found."""
        return len(self.findings) > 0
