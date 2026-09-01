# Common Runner v0 Failure — Experiment 016

The first attempt to execute the frozen candidates did not produce a candidate score and is not counted as an implementation failure.

## Failure

The initial ad-hoc dynamic loader created the EFM module with `importlib.util.module_from_spec` but did not register that module in `sys.modules` before executing it. Python's `dataclass` processing uses the defining module namespace during class construction, so the EFM module aborted during import with an `AttributeError` inside `dataclasses`.

The build-first module had been loaded, but neither candidate had yet been passed to the common evaluator when the runner aborted.

## Correction

The corrected runner executes each frozen candidate in a separate Python process using its candidate directory on `sys.path`, imports `line_mapper` normally, registers the common evaluation module before executing it, and then calls the same `evaluate(LineIndex)` function.

No candidate source, frozen hash, common evaluation fixture, oracle, or judge was changed.

After the runner correction:
- build-first: 20,590 checks / 0 failures;
- EFM: 20,590 checks / 0 failures.

Classification: common evaluation harness defect, preserved separately from candidate results.