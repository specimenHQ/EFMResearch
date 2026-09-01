# Outcome — Experiment 016 Line Mapper Controlled Comparison

Status: **null delivered-correctness result**.

The build-first and EFM implementations were frozen before the common evaluator was authored. The common judge rejected 5/5 known-false line mappers before either frozen candidate was scored.

Both candidates then passed:
- 20,590/20,590 initial common checks;
- 161,669/161,669 fresh post-green checks;
- zero candidate failures;
- zero candidate rework.

EFM did produce meaningful preimplementation evidence: it falsified `str.splitlines()` as an authority for the frozen separator semantics and directly established empty/trailing-line, CRLF-boundary, and Unicode code-point behavior. But build-first had independently chosen the same broad explicit-scanner architecture and was equally correct under the common evaluation.

Therefore experiment 016 does not support a claim that EFM improved delivered correctness, reduced rework, or materially improved final architecture on this task. It supports a narrower claim: EFM can expose plausible dangerous alternatives before code, even when that evidence turns out to be redundant to a careful ordinary implementation.

This is the repository's second controlled comparison with a null correctness result. Alongside the clean native-build evidence, it argues for a narrower research program: stop treating more evidence as automatically valuable and test whether EFM changes consequential outcomes in settings where ordinary implementation is more likely to choose wrongly or where failures are more expensive.

A common runner/import defect was observed and corrected before candidate scoring; no candidate code or frozen hash changed.

No E4 independent-methodology, E6 operational, superiority, statistical-significance, or cybersecurity claim is made.