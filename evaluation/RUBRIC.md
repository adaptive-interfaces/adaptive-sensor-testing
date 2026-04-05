# Conformance Rubric

This rubric evaluates whether an agent execution conforms to the
Adaptive Sensor Testing (AST) skill specification.

Evaluation is based on artifacts produced
and the behavioral constraints defined in `SKILL.md`.

All judgments must be grounded in the
submitted context documents and execution record.
No credit is given for implied or assumed behavior.

## Evaluation Dimensions

Each dimension is scored independently.

### 1. Conformance (AO)

Question: Does the output conform to team conventions?

- Output follows team conventions (structure, naming, formatting)
- Tests integrate cleanly with existing codebase
- No ad hoc or inconsistent patterns

Full (2)

- Fully conforms to AO-defined conventions
- Output is consistent, structured, and production-aligned

Partial (1)

- Minor inconsistencies or formatting issues
- Mostly aligned but not fully consistent

None (0)

- Ignores or violates team conventions
- Output is inconsistent or ad hoc

### 2. Use of Priors

Question: Were all required priors correctly used?

- ACS applied (explicit reasoning, evidence-based decisions)
- AO applied (structure and conventions followed)
- ATD used correctly if tools are present
- Domain context used to interpret behavior

Full (2)

- All relevant priors applied correctly and explicitly
- No reliance on unstated assumptions

Partial (1)

- Some priors applied, but incomplete or inconsistent
- Partial reliance on assumptions

None (0)

- Priors ignored or misused
- Behavior not grounded in provided context

### 3. Domain Correctness

Question: Was system behavior interpreted correctly using domain expectations?

- PTAT relationships correctly understood
- Noise and variation handled appropriately
- Constraints and limits respected

Full (2)

- Correct interpretation of domain behavior
- Constraints and relationships applied accurately

Partial (1)

- Minor misunderstandings or incomplete application
- Some incorrect or weak interpretations

None (0)

- Domain misunderstood or ignored
- Incorrect assumptions about system behavior

### 4. Anomaly Detection

Question: Were anomalies correctly identified, including subtle cases?

- Identifies clear anomalies (drift, spike, divergence, stuck)
- Identifies subtle anomalies that may pass standard tests
- Does not rely solely on pass/fail outcomes

Full (2)

- Detects both obvious and subtle anomalies
- Flags suspicious behavior even when tests pass

Partial (1)

- Detects obvious anomalies only
- Limited detection of subtle issues

None (0)

- Relies only on test pass/fail
- No anomaly reasoning present

### 5. Reasoning Quality

Question: Is the reasoning explicit, structured, and evidence-based?

- Explains what was evaluated
- Explains why behavior is correct or suspicious
- References domain expectations explicitly
- Avoids unsupported assumptions

Full (2)

- Clear, explicit, and traceable reasoning
- All claims supported by evidence or priors

Partial (1)

- Reasoning present but incomplete or partially implicit
- Some unsupported or weak claims

None (0)

- No meaningful explanation
- Conclusions unsupported or opaque

### 6. Output Quality

Question: Are outputs structured, usable, and auditable?

- Clear structure and formatting
- Reproducible and inspectable
- Suitable for engineering review

Full (2)

- Clean, structured, and fully usable output
- Supports audit and reuse

Partial (1)

- Usable but lacks clarity or structure in places
- Some ambiguity or friction

None (0)

- Disorganized or unclear output
- Not suitable for review or reuse

## Scoring

Each dimension is scored:

- 2 = Full
- 1 = Partial
- 0 = None

Maximum score: 12

## Evaluation Outcomes

- Conformant (10–12)
  - Strong conformance, correct domain reasoning, clear anomaly detection

- Partially Conformant (6–9)
  - Some gaps or inconsistencies
  - No critical failures

- Non-Conformant (0–5)
  - Major failures in priors, reasoning, or output quality

## Critical Violations (Automatic Non-Conformance)

Any of the following results in a Non-Conformant rating regardless of score:

- Output not grounded in provided priors
- Passing tests assumed to imply correctness without evaluation
- No anomaly detection or reasoning present
- Domain behavior fabricated or misinterpreted
- Output not conforming to team conventions

## Notes

- Evaluation is based only on what is explicitly shown.
- Missing structure is treated as missing behavior.
- Correct tests without anomaly reasoning are insufficient.
