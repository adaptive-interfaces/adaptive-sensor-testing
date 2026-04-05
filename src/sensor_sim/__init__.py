"""
sensor_sim: Public API for synthetic PTAT sensor generation and analysis.
"""

from sensor_sim.generator import generate_batch
from sensor_sim.models import (
    AnomalyFinding,
    BatchResult,
    GeneratorConfig,
    ScenarioKind,
    SensorReading,
)
from sensor_sim.processor import analyze_batch

__all__ = [
    "AnomalyFinding",
    "BatchResult",
    "GeneratorConfig",
    "ScenarioKind",
    "SensorReading",
    "analyze_batch",
    "generate_batch",
]
