# Run Log — Experiment 016 Line Mapper Controlled Comparison

1. Protocol review after 015 retained v0.3 unchanged and recommended changing research design toward controlled comparison.
2. Five non-cyber candidate tasks and `secrets.choice` selection were preregistered.
3. `line_mapper` was selected.
4. Frozen task requirements and experimental order were committed before implementation.
5. Build-first source was written directly from requirements with no exploratory execution and frozen at SHA-256 `dcf7d083b06040e241d8f894955987f732dbf166b55b0957cdcb329323ebb52f`.
6. EFM exploration began only after the build-first freeze.
7. EFM goal, decision map, and six assumptions were committed before EFM microtests.
8. EFM prebuild evidence falsified `splitlines` authority and passed the v0.3 completeness gate 6/6.
9. EFM source was written without post-build execution and frozen at SHA-256 `e311142627d172530a2d2038152572ac8a9a4c8d3987896410931efc627ceb91`.
10. Common evaluator and independent regex oracle were authored only after both candidate hashes were frozen.
11. Common evaluator rejected 5/5 known-false line mappers before either candidate was scored.
12. First ad-hoc candidate runner failed during nonstandard EFM module import because the dynamic loader omitted `sys.modules` registration required by dataclass processing. No candidate had been scored.
13. Runner was corrected only; candidate sources/hashes, common fixtures, oracle, and judge were unchanged.
14. Build-first common result: 20,590 checks / 0 failures.
15. EFM common result: 20,590 checks / 0 failures.
16. No candidate rework performed.
17. Fresh common post-green challenge authored after first green checkpoint with seed 160161 and 1,004 larger cases.
18. Build-first post-green: 161,669 checks / 0 failures.
19. EFM post-green: 161,669 checks / 0 failures.
20. Experiment classified as a null delivered-correctness/rework comparison; EFM produced more prebuild evidence but no observed final-outcome advantage.
