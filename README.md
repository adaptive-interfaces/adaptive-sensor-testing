# adaptive-sensor-testing

[![CI Status](https://github.com/adaptive-interfaces/adaptive-sensor-testing/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/adaptive-interfaces/adaptive-sensor-testing/actions/workflows/ci.yml)
[![MIT](https://img.shields.io/badge/license-see%20LICENSE-yellow.svg)](./LICENSE)
[![Check Links](https://github.com/adaptive-interfaces/adaptive-sensor-testing/actions/workflows/links.yml/badge.svg?branch=main)](https://github.com/adaptive-interfaces/adaptive-sensor-testing/actions/workflows/links.yml)
[![Dependabot](https://img.shields.io/badge/Dependabot-enabled-brightgreen.svg)](https://github.com/adaptive-interfaces/adaptive-sensor-testing/security)

> Adaptive Sensor Testing (AST) UNDER CONSTRUCTION

Worked example: producing team-conforming test artifacts under domain-specific correctness constraints.

IMPORTANT: Better outcomes come less from better prompting alone
than from better specification of priors, skills, constraints, and evaluation.

## Separation of Concerns

This repository separates two concerns:

1. producing team-conforming artifacts (via ACS + AO + ATD)
2. determining domain correctness (via domain priors and evaluation scenarios)

## Priors

1. adaptive-conformance-specification # foundational (ACS)
2. adaptive-tool-discovery # domain skill (ATD)
3. adaptive-onboarding # conventions (AO)

- ACS: behavioral constraints (how the agent operates)
- AO: team conventions (how outputs must be structured)
- ATD: tool capabilities (what can be invoked)

Additional:

- Domain context: defines correctness (in this system)

## Scenarios

Each scenario evaluates whether the agent can detect anomalies
that are not captured by existing tests.

1. Basic: clean batch, generate missing tests
2. Drift detection: batch with injected calibration drift at sample 400, agent must find it
3. Multi-sensor: correlated array where one sensor diverges from peers

## Project Organization

```text
adaptive-sensor-testing/
  SKILL.md              # spec for generating tests and anomaly reports
  MANIFEST.toml
  DECISIONS.md
  LICENSE
  .agent/
    ao-config.toml
    ao-config-python.toml
    ao-domain.toml      # PTAT behavior, expected ranges, anomaly definitions
  evaluation/
    rubric.md
    scenarios/
      ptat-basic/       # single sensor, basic test generation
        prompt.md
        notes.md
        .agent/
      drift-detection/  # time-series anomaly across multiple readings
        prompt.md
        notes.md
        .agent/
      multi-sensor/     # correlated readings across sensor array
        prompt.md
        notes.md
        .agent/
    local/              # gitignored; proprietary test cases
  src/
    sensor_sim/
      __init__.py
      generator.py      # PTAT batch data generator
      processor.py      # anomaly detection, drift flagging
      models.py         # SensorReading, BatchResult types
  tests/
    test_generator.py   # partial agent fills gaps
    test_processor.py   # partial agent fills gaps
  data/
    sample_batch.csv    # pre-generated batch for scenarios
```

## Command Reference

The commands below are used in the workflow guide above.
They are provided here for convenience.

Follow the guide for the **full instructions**.

<details>
<summary>Show command reference</summary>

### In a machine terminal (open in your `Repos` folder)

After you get a copy of this repo in your own GitHub account,
open a machine terminal in your `Repos` folder:

```shell
# Replace username with YOUR GitHub username.
git clone https://github.com/username/cintel-06-continuous-intelligence

cd cintel-06-continuous-intelligence
code .
```

### In a VS Code terminal

```shell
uv self update
uv python pin 3.14
uv sync --extra dev --extra docs --upgrade

uvx pre-commit install
git add -A
uvx pre-commit run --all-files
# repeat if things change
git add -A
uvx pre-commit run --all-files

uv run python -m sensor_sim.data_maker

uv run ruff format .
uv run ruff check . --fix
uv run zensical build

npx markdownlint-cli2 "**/*.md" "#.venv" "#site" "#dist" "#node_modules"

git add -A
git commit -m "update"
git push -u origin main
```

</details>

## When Working with A Chat Agent

At the start of a session:

```text
Read https://raw.githubusercontent.com/adaptive-interfaces/adaptive-conformance-specification/main/SKILL.md
Apply the Adaptive Conformance Specification (ACS).
Follow its workflow and produce a full conformance record.
```

Then:

```text
Inspect the repository first.
Then generate tests that conform to local patterns.
Produce a full conformance record.
```

## License

MIT © 2026 [Adaptive Interfaces](https://github.com/adaptive-interfaces)
