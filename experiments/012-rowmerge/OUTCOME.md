# Outcome — Experiment 012 RowMerge

RowMerge is a non-cyber EFM-native study in local CSV/data reconciliation.

## What changed before implementation

Four ordinary-looking implementation shortcuts were falsified before code was accepted:

1. numeric coercion can collapse distinct textual identifiers;
2. dictionary overwrite can silently destroy duplicate-ID rows;
3. blank IDs can collapse into one invented identity;
4. relying on source insertion order makes output nondeterministic.

The standard-library CSV parser passed the required quoting/newline fixtures, so no custom parser or third-party dependency was added.

The implementation therefore uses exact string identifiers, explicit duplicate ambiguity errors, a separate invalid-row channel, and deterministic sorting.

## Integration result

The first 11-test run produced 10 passes and one failure. Investigation showed the failure was an incorrect hand-written expected Unicode sort order in the evaluator. The judge was corrected and the application code was unchanged.

Final integration: 11/11 pass.

A post-green neighboring identity challenge confirmed that composed/decomposed Unicode strings and uppercase/lowercase strings remain distinct exact identifiers.

## Judge attack

The evaluator rejected 5/5 known-false designs:
- numeric ID coercion;
- duplicate last-write-wins overwrite;
- source-order authority;
- naive comma splitting;
- lowercase normalization as a near-miss false design.

The current implementation was accepted.

## Interpretation

This run is useful evidence for EFM's ability to constrain a small data-transformation design before implementation and for its insistence on testing the evaluator itself: the only integration failure was a false rejection produced by the test harness, not the application.

Evidence ceiling: E5 integration within the tested CSV-reconciliation scope. No E6, superiority, or cybersecurity claim is made.
