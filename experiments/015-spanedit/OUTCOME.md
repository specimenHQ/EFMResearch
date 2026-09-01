# Outcome — Experiment 015 SpanEdit

SpanEdit is the third clean Protocol-v0.3 EFM-native study and a non-cyber Unicode text-transformation run.

## What changed before implementation

Prebuild evidence materially constrained the design:

1. left-to-right mutation was falsified because an expanding earlier replacement shifted a later original-coordinate target;
2. right-to-left mutation matched an independently implemented forward-streaming reconstruction;
3. the conflict model was fixed to permit adjacent nonempty spans and boundary insertions while rejecting interior insertions and overlapping spans;
4. Python string code-point indices were explicitly separated from UTF-8 byte offsets and grapheme-cluster semantics;
5. same-position insertions were rejected after opposite declaration orders produced different outputs.

All six admitted consequential assumptions passed the v0.3 prebuild completeness gate before implementation.

## Integrated result

The evidence-earned implementation passed 14/14 integration tests on its first run. No application change was required.

The nontrivial four-edit expectation was independently derived with a forward streaming oracle before acceptance. The required post-green challenge then combined Unicode, replacement, deletion, and boundary insertions in a new six-edit fixture. All 720 declaration permutations matched the independent oracle result.

## Evaluator finding

The first adversarial judge was itself defective: a known-false editor raised on a known-good boundary-insertion fixture, and judge v0 allowed the exception to abort the run instead of treating the candidate as rejected. No E3 result was accepted from that judge.

The evaluator was corrected without changing application code. The corrected judge rejected 5/5 known-false editors and accepted SpanEdit.

## Interpretation

For the application, this is a non-defect EFM-native result: EFM changed architecture and semantics before code, and the first evidence-earned implementation survived integration and post-green testing without rework.

For the methodology, the run provides another concrete evaluator-integrity observation: testing the judge prevented a flawed evaluator from being silently treated as authoritative.

Evidence ceiling: E5 within the finite in-memory Python-string editing scope. No grapheme-cluster, collaborative editing, E6, superiority, or cybersecurity claim is made.