"""
test_processor.py: Tests for PTAT anomaly analysis.
"""

from sensor_sim.generator import generate_batch
from sensor_sim.models import GeneratorConfig
from sensor_sim.processor import analyze_batch


def test_analyze_batch_detects_dropout() -> None:
    config = GeneratorConfig(batch_size=400, num_sensors=1, seed=1)
    readings = generate_batch("dropout", config)
    result = analyze_batch(readings)

    kinds = {finding.kind for finding in result.findings}
    assert "dropout" in kinds


def test_analyze_batch_detects_spike() -> None:
    config = GeneratorConfig(batch_size=800, num_sensors=1, seed=1)
    readings = generate_batch("spike", config)
    result = analyze_batch(readings)

    kinds = {finding.kind for finding in result.findings}
    assert "spike" in kinds


def test_analyze_batch_detects_drift_or_suspicious_trend() -> None:
    config = GeneratorConfig(batch_size=800, num_sensors=1, seed=1)
    readings = generate_batch("drift", config)
    result = analyze_batch(readings)

    kinds = {finding.kind for finding in result.findings}
    assert "drift" in kinds or "suspicious_trend" in kinds


def test_analyze_batch_detects_multi_sensor_divergence() -> None:
    config = GeneratorConfig(batch_size=800, num_sensors=3, seed=1)
    readings = generate_batch("multi_sensor_divergence", config)
    result = analyze_batch(readings)

    kinds = {finding.kind for finding in result.findings}
    assert "divergence" in kinds


def test_analyze_clean_batch_returns_known_sensors() -> None:
    config = GeneratorConfig(batch_size=100, num_sensors=2, seed=1)
    readings = generate_batch("clean", config)
    result = analyze_batch(readings)

    assert result.total_readings == 200
    assert result.sensors == ("S01", "S02")
