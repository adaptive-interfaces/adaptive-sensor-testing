---
name: adaptive-sensor-testing
description: >
  Generate and evaluate test artifacts for sensor data systems,
  identifying anomalies beyond standard test results.
---

# Adaptive Sensor Testing (AST) Skill

This skill generates and evaluates test artifacts for sensor data systems
using domain priors and team conventions.

It operates under the Adaptive Conformance Specification (ACS).
Apply ACS discovery and conformance discipline before executing
domain-specific actions below.

## 1.0 Scope

### 1.1 What this skill does

- Generates test artifacts consistent with team conventions
- Evaluates sensor data using domain priors
- Identifies anomalies, including cases where tests pass but behavior is suspicious
- Produces structured, auditable explanations of findings

### 1.2 What this skill does not do

- Assume passing tests imply correctness
- Invent domain rules not present in priors
- Ignore suspicious patterns that fall within thresholds
- Produce output without explicit reasoning

## 2.0 Purpose

Generate and evaluate test artifacts for sensor data systems in a way that is:

- consistent with team conventions
- aligned with domain expectations
- capable of identifying anomalies not captured by existing tests

The goal is not only to produce passing tests,
but to detect when passing results are suspicious.

## 3.0 Required Priors

The agent MUST load and apply:

- ACS (adaptive-conformance-specification)
  - governs decision discipline and evidence requirements

- AO (adaptive-onboarding)
  - defines code structure, naming, and documentation conventions

- ATD (adaptive-tool-discovery), if tools are present
  - defines how to invoke available tools correctly

- Domain context (`ao-domain.toml`)
  - defines expected system behavior, constraints, and anomaly conditions

## 4.0 Prior Precedence

When conflicts occur:

Domain context (`ao-domain.toml`) >
AO conventions >
ACS behavioral constraints >
existing tests

Passing tests do not override domain expectations.

## 5.0 Required Inputs

- Existing code in `src/`
- Existing tests in `tests/`
- Sample or scenario data in `data/` or scenario folders
- Scenario prompt (if running under evaluation)

## 6.0 Expected Outputs

The agent must produce:

1. Test artifacts
   - new or completed tests
   - consistent with team conventions (AO)

2. Anomaly findings
   - explicit identification of suspicious patterns
   - including cases where tests pass but behavior is questionable

3. Structured explanation
   - what was evaluated
   - what passed
   - what is suspicious and why
   - what assumptions and priors were used

## 7.0 Workflow

### 7.1 Discover

- Load all required priors
- Inspect code, tests, and data sources
- Identify available signals and constraints

### 7.2 Interpret

- Determine expected behavior from domain model
- Compare observed behavior to expected relationships
- Evaluate whether deviations fall within constraints

### 7.3 Execute

- Generate or complete tests
- Identify anomalies
- Produce structured outputs

### 7.4 Validate

- Ensure all conclusions are grounded in priors
- Ensure no assumptions are implicit
- Ensure suspicious conditions are explicitly reported

## 8.0 Decision Rules

The agent MUST:

- Use domain priors to interpret data behavior
- Not assume that passing tests imply correctness
- Prefer explicit reasoning over implicit assumptions
- Align all outputs with AO-defined conventions
- Report anomalies when domain expectations are violated,
  even if all tests pass

The agent MUST NOT:

- invent domain rules not present in priors
- silently ignore inconsistencies
- rely solely on pass/fail outcomes
- produce unstructured or non-auditable output

No credit is given for passing tests without explicit evaluation
against domain expectations.

## 9.0 Failure / Stop Conditions

The agent must stop and report if:

- required priors are missing or incomplete
- domain expectations are unclear or contradictory
- data cannot be interpreted within defined constraints
- observed behavior cannot be reconciled with domain expectations

The agent must explicitly state what is missing and why execution cannot proceed.

## 10.0 Evaluation Targets

Outputs will be evaluated on:

- conformance to team conventions (AO)
- correct use of priors (ACS, ATD, AO, domain)
- ability to detect non-obvious anomalies
- clarity and auditability of reasoning
