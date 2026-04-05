# Scenario: Drift Detection

Apply the Adaptive Sensor Testing (AST) skill to evaluate
sensor behavior and generate test artifacts.

Before acting, load and apply:

- ACS
- AO
- ATD (if tools are present)
- `.agent/ao-domain.toml`

## Situation

A batch of PTAT sensor readings has been collected.

A calibration drift has been injected beginning near sample 400.

Existing tests may still pass.

## Requirements

- Evaluate the data using domain priors
- Determine whether behavior is:
  - correct
  - anomalous
  - suspicious but not conclusively invalid
- Generate or complete tests as needed
- Do not assume that passing tests imply correctness
- Do not ignore gradual drift because values remain in range

## Output Requirements

Produce:

1. test artifacts (if needed)
2. anomaly assessment
3. structured explanation including:
   - what was evaluated
   - what passed
   - what is suspicious or anomalous
   - which priors support the conclusion

## Required Artifacts

After completing the evaluation:

1. Save generated tests to:
   `tests/test_processor.py` (or appropriate location)

2. Write a structured response to:
   `evaluation/scenarios/drift-detection/response.txt`

3. Score the output against `evaluation/rubric.md`
   and include the score table in `response.txt`

## Constraints

- Passing tests do not override domain expectations
- All conclusions must be grounded in priors
- No credit is given for test-only output without anomaly reasoning

## Expected Failure Mode

Weak executions:

- rely only on pass/fail tests
- generate tests without evaluating domain behavior
- miss gradual drift
- fail to explain why behavior is suspicious

Such executions are non-conformant.
