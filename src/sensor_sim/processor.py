"""
processor.py: PTAT sensor anomaly analysis utilities.

This module provides simple, inspectable anomaly detection for
synthetic PTAT sensor data. It is intentionally explicit rather
than optimized so that generated reasoning remains auditable.
"""

from __future__ import annotations

from statistics import mean, pstdev
from typing import Iterable

from sensor_sim.models import AnomalyFinding, BatchResult, SensorReading


def _group_by_sensor(
    readings: Iterable[SensorReading],
) -> dict[str, list[SensorReading]]:
    """Group readings by sensor identifier."""
    grouped: dict[str, list[SensorReading]] = {}
    for reading in readings:
        grouped.setdefault(reading.sensor_id, []).append(reading)
    for sensor_id in grouped:
        grouped[sensor_id].sort(key=lambda item: item.sample_index)
    return grouped


def _non_null_frequencies(readings: Iterable[SensorReading]) -> list[float]:
    """Return frequency values excluding null readings."""
    return [
        reading.frequency_hz
        for reading in readings
        if reading.frequency_hz is not None
    ]


def detect_dropouts(readings: list[SensorReading]) -> list[AnomalyFinding]:
    """Detect null or zero-valued readings."""
    findings: list[AnomalyFinding] = []

    for reading in readings:
        if reading.frequency_hz is None or reading.frequency_hz == 0.0:
            findings.append(
                AnomalyFinding(
                    sensor_id=reading.sensor_id,
                    kind="dropout",
                    start_sample=reading.sample_index,
                    end_sample=reading.sample_index,
                    message="Sensor reported null or zero frequency.",
                    severity="high",
                )
            )

    return findings


def detect_spikes(
    readings: list[SensorReading],
    sigma_threshold: float = 5.0,
) -> list[AnomalyFinding]:
    """Detect abrupt single-sample spikes."""
    values = _non_null_frequencies(readings)
    if len(values) < 3:
        return []

    center = mean(values)
    spread = pstdev(values)
    if spread == 0.0:
        return []

    findings: list[AnomalyFinding] = []

    for reading in readings:
        if reading.frequency_hz is None:
            continue
        z_score = abs(reading.frequency_hz - center) / spread
        if z_score > sigma_threshold:
            findings.append(
                AnomalyFinding(
                    sensor_id=reading.sensor_id,
                    kind="spike",
                    start_sample=reading.sample_index,
                    end_sample=reading.sample_index,
                    message=(
                        f"Single-sample deviation exceeds {sigma_threshold} sigma "
                        f"(z={z_score:.2f})."
                    ),
                    severity="high",
                )
            )

    return findings


def detect_drift(
    readings: list[SensorReading],
    baseline_window: int = 100,
    comparison_window: int = 100,
    drift_offset_percent: float = 2.0,
) -> list[AnomalyFinding]:
    """Detect sustained deviation from an early baseline."""
    values = _non_null_frequencies(readings)
    if len(values) < baseline_window + comparison_window:
        return []

    baseline = mean(values[:baseline_window])
    threshold = baseline * (drift_offset_percent / 100.0)

    findings: list[AnomalyFinding] = []

    for start_index in range(
        baseline_window,
        len(values) - comparison_window + 1,
    ):
        window = values[start_index : start_index + comparison_window]
        window_mean = mean(window)
        offset = window_mean - baseline

        if abs(offset) > threshold:
            findings.append(
                AnomalyFinding(
                    sensor_id=readings[0].sensor_id,
                    kind="drift",
                    start_sample=start_index,
                    end_sample=start_index + comparison_window - 1,
                    message=(
                        "Sustained deviation from calibrated baseline exceeds "
                        f"{drift_offset_percent:.1f}% "
                        f"(offset={offset:.2f} Hz)."
                    ),
                    severity="medium",
                )
            )
            break

    return findings


def detect_suspicious_trend(
    readings: list[SensorReading],
    early_window: int = 100,
    late_window: int = 100,
) -> list[AnomalyFinding]:
    """Detect monotonic directional change that may remain in range."""
    values = _non_null_frequencies(readings)
    if len(values) < early_window + late_window:
        return []

    early_mean = mean(values[:early_window])
    late_mean = mean(values[-late_window:])

    if late_mean <= early_mean:
        return []

    difference = late_mean - early_mean
    if difference <= 0.0:
        return []

    return [
        AnomalyFinding(
            sensor_id=readings[0].sensor_id,
            kind="suspicious_trend",
            start_sample=len(values) - late_window,
            end_sample=len(values) - 1,
            message=(
                "Late-window mean exceeds early-window mean, indicating "
                "possible monotonic drift within range."
            ),
            severity="low",
        )
    ]


def detect_multi_sensor_divergence(
    readings: list[SensorReading],
    deviation_percent: float = 2.0,
) -> list[AnomalyFinding]:
    """Detect a sensor diverging from correlated peers."""
    grouped = _group_by_sensor(readings)
    if len(grouped) < 2:
        return []

    sensor_means: dict[str, float] = {}
    for sensor_id, sensor_readings in grouped.items():
        values = _non_null_frequencies(sensor_readings)
        if not values:
            continue
        sensor_means[sensor_id] = mean(values)

    if len(sensor_means) < 2:
        return []

    global_mean = mean(sensor_means.values())
    findings: list[AnomalyFinding] = []

    for sensor_id, sensor_mean in sensor_means.items():
        percent_difference = abs(sensor_mean - global_mean) / global_mean * 100.0
        if percent_difference > deviation_percent:
            sensor_readings = grouped[sensor_id]
            findings.append(
                AnomalyFinding(
                    sensor_id=sensor_id,
                    kind="divergence",
                    start_sample=sensor_readings[0].sample_index,
                    end_sample=sensor_readings[-1].sample_index,
                    message=(
                        "Sensor mean deviates from peer group by more than "
                        f"{deviation_percent:.1f}%."
                    ),
                    severity="medium",
                )
            )

    return findings


def analyze_batch(readings: list[SensorReading]) -> BatchResult:
    """Run all supported anomaly checks over a batch."""
    grouped = _group_by_sensor(readings)
    findings: list[AnomalyFinding] = []

    for _sensor_id, sensor_readings in grouped.items():
        findings.extend(detect_dropouts(sensor_readings))
        findings.extend(detect_spikes(sensor_readings))
        findings.extend(detect_drift(sensor_readings))
        findings.extend(detect_suspicious_trend(sensor_readings))

    findings.extend(detect_multi_sensor_divergence(readings))

    return BatchResult(
        total_readings=len(readings),
        sensors=tuple(sorted(grouped.keys())),
        findings=tuple(findings),
    )