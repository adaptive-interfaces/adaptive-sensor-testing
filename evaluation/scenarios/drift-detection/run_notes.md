# Run Notes: Drift Detection

## Purpose

This scenario is used to compare the effect of specification quality
on agent performance.

The underlying task remains fixed.
What changes is the completeness and quality of:

- priors
- skill definition
- prompt instructions
- evaluation constraints

## Scenario

A PTAT sensor batch contains sustained calibration drift
beginning near sample 400.

The scenario is designed so that:

- ordinary checks may still pass
- values may remain in range
- the anomaly is temporal and gradual
- weak agents may miss it

## Expected Comparison

### Minimal setup

Expected outcome:

- generate tests only
- rely on pass/fail outcomes
- miss sustained drift
- produce weak explanation

### Partial setup

Expected outcome:

- identify suspicious trend
- produce incomplete anomaly reasoning
- reference domain context only loosely
- detect issue but not classify it strongly

### Complete setup

Expected outcome:

- load and apply all priors
- detect drift explicitly
- distinguish passing tests from correctness
- produce structured, auditable explanation
- score strongly against rubric

## Notes from Runs

### Run template

- Date:
- Model / agent:
- Condition:
- Priors loaded:
- Skill completeness:
- Prompt completeness:
- Output artifacts:
- Score:
- Observed failure mode:
- Observed strength:

## Interpretation Guidance

Use this scenario to demonstrate:

- why tests alone are insufficient
- why domain priors matter
- why skill design affects outcomes
- how stronger specification improves behavior

## Caution

Keep the following fixed across comparisons:

- model
- batch data
- task
- expected artifacts

Only vary the specification stack.