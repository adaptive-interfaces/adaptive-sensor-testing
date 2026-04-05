"""
test_processor.py: Tests for PTAT anomaly analysis.
"""

from sensor_sim.generator import generate_batch
from sensor_sim.models import GeneratorConfig, ProcessorConfig
from sensor_sim.processor import analyze_batch


def test_analyze_batch_detects_dropout() -> None:
    gen_config = GeneratorConfig(batch_size=400, num_sensors=1, seed=1)
    proc_config = ProcessorConfig()
    readings = generate_batch("dropout", gen_config)
    result = analyze_batch(readings, proc_config)

    kinds = {finding.kind for finding in result.findings}
    assert "dropout" in kinds


def test_analyze_batch_detects_spike() -> None:
    gen_config = GeneratorConfig(batch_size=800, num_sensors=1, seed=1)
    proc_config = ProcessorConfig()
    readings = generate_batch("spike", gen_config)
    result = analyze_batch(readings, proc_config)

    kinds = {finding.kind for finding in result.findings}

    max_ratio = 0.0
    max_delta = 0.0
    max_idx = -1

    for i in range(1, len(readings) - 1):
        c = readings[i].frequency_hz
        p = readings[i - 1].frequency_hz
        n = readings[i + 1].frequency_hz

        if c is None or p is None or n is None:
            continue

        local_mean = (p + n) / 2.0
        if local_mean == 0:
            continue

        delta = abs(c - local_mean)
        ratio = delta / abs(local_mean)

        if ratio > max_ratio:
            max_ratio = ratio
            max_delta = delta
            max_idx = i

    print(f"\nSPIKE DEBUG: max_ratio={max_ratio:.6f}, max_delta={max_delta:.2f} Hz at sample {max_idx}")
    assert "spike" in kinds


def test_analyze_batch_detects_drift_or_suspicious_trend() -> None:
    gen_config = GeneratorConfig(batch_size=800, num_sensors=1, seed=1)
    proc_config = ProcessorConfig()
    readings = generate_batch("drift", gen_config)
    result = analyze_batch(readings, proc_config)

    kinds = {finding.kind for finding in result.findings}
    assert "drift" in kinds or "suspicious_trend" in kinds


def test_analyze_batch_detects_multi_sensor_divergence() -> None:
    gen_config = GeneratorConfig(batch_size=800, num_sensors=3, seed=1)
    proc_config = ProcessorConfig()
    readings = generate_batch("multi_sensor_divergence", gen_config)
    result = analyze_batch(readings, proc_config)

    kinds = {finding.kind for finding in result.findings}
    assert "divergence" in kinds


def test_analyze_clean_batch_returns_known_sensors() -> None:
    gen_config = GeneratorConfig(batch_size=100, num_sensors=2, seed=1)
    proc_config = ProcessorConfig()
    readings = generate_batch("clean", gen_config)
    result = analyze_batch(readings, proc_config)

    assert result.total_readings == 200
    assert result.sensors == ("S01", "S02")
