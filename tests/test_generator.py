"""
test_generator.py: Tests for synthetic PTAT batch generation.
"""

from sensor_sim.generator import generate_batch
from sensor_sim.models import GeneratorConfig


def test_generate_clean_batch_has_expected_size() -> None:
    config = GeneratorConfig(batch_size=50, num_sensors=1, seed=1)
    readings = generate_batch("clean", config)

    assert len(readings) == 50
    assert all(reading.frequency_hz is not None for reading in readings)


def test_generate_drift_batch_shifts_later_values_upward() -> None:
    config = GeneratorConfig(batch_size=700, num_sensors=1, seed=1)
    readings = generate_batch("drift", config)

    early = [r.frequency_hz for r in readings[50:150] if r.frequency_hz is not None]
    late = [r.frequency_hz for r in readings[550:650] if r.frequency_hz is not None]

    assert early
    assert late
    assert sum(late) / len(late) > sum(early) / len(early)


def test_generate_dropout_batch_contains_null_readings() -> None:
    config = GeneratorConfig(batch_size=400, num_sensors=1, seed=1)
    readings = generate_batch("dropout", config)

    null_count = sum(1 for reading in readings if reading.frequency_hz is None)
    assert null_count == 3


def test_multi_sensor_divergence_requires_multiple_sensors() -> None:
    config = GeneratorConfig(batch_size=100, num_sensors=1, seed=1)

    try:
        generate_batch("multi_sensor_divergence", config)
    except ValueError as exc:
        assert "num_sensors >= 2" in str(exc)
    else:
        raise AssertionError("Expected ValueError for single-sensor divergence scenario")
