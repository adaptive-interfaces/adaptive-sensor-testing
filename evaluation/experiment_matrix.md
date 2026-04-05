# Experiment Matrix

This matrix compares agent behavior under three levels
of specification completeness.

The task remains constant.
The scenario remains constant.
Only the specification stack changes.

## Condition A: Minimal

### Inputs

- basic task prompt only
- no skill file
- no domain prior
- no rubric guidance

### Expected Behavior

- writes or completes tests
- emphasizes pass/fail status
- weak anomaly reasoning
- likely misses gradual drift

### Typical Outcome

- low traceability
- low domain awareness
- weak or absent suspicion reporting

---

## Condition B: Partial

### Inputs

- task prompt
- partial skill definition
- partial domain context
- rubric available but not emphasized

### Expected Behavior

- generates reasonable tests
- may identify suspicious trend
- incomplete use of priors
- partial anomaly explanation

### Typical Outcome

- moderate traceability
- moderate domain awareness
- partial detection of drift

---

## Condition C: Complete

### Inputs

- task prompt
- full AST skill
- AO conventions
- domain prior (`ao-domain.toml`)
- rubric-guided evaluation

### Expected Behavior

- generates team-conforming tests
- evaluates behavior against priors
- identifies drift explicitly
- explains why passing tests are insufficient

### Typical Outcome

- high traceability
- strong domain awareness
- strong anomaly detection
- strong structured reporting

---

## Comparison Dimensions

Use the rubric to compare:

- Conformance (AO)
- Use of Priors
- Domain Correctness
- Anomaly Detection
- Reasoning Quality
- Output Quality

## Core Claim

Better outcomes come from stronger specification of:

- priors
- skills
- constraints
- evaluation expectations

not from prompt phrasing alone.