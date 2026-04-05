# Evaluation Notes: Drift Detection

## What to look for

### Drift identification

- Agent identifies sustained deviation beginning near sample 400
- Agent recognizes drift even if values remain within absolute bounds
- Drift is treated as a temporal pattern, not a single-point anomaly

### Test vs domain distinction

- Agent does not equate passing tests with correctness
- Agent explicitly evaluates behavior against domain priors
- Agent flags suspicious behavior even when tests pass

### Use of priors

- Domain model (PTAT relationship) is used in reasoning
- Constraints and thresholds are applied correctly
- Suspicious patterns are referenced explicitly

### Reasoning quality

- Explanation is explicit and structured
- All conclusions are traceable to priors
- No hidden assumptions

### Output quality

- Tests (if generated) follow AO conventions
- Response is structured and auditable
- Output is suitable for engineering review

---

## Common failure modes

- Agent produces tests only, without anomaly analysis
- Agent reports success because tests pass
- Drift treated as acceptable because values are in range
- No reference to domain priors
- Conclusions not supported by evidence

---

## Notes from scenario runs

(To be populated after runs)

Record:

- strengths of execution
- failure patterns
- scoring outcomes
