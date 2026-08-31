# Verification Run — Experiment 003 MergeSafe

## Initial prebuild microtests
```text
A1: PASS — Unequal JSON text parsed to equal objects, so raw text would create a false conflict.
A2: PASS — Equivalent objects canonicalized identically as '{"id":"r1","n":1,"name":"Ada"}'.
A3: PASS — Injected pre-replace failure left the previous output bytes unchanged.
A4: PASS — os.path.samefile identified a symlink alias as the same existing file.
A5: PASS — Reordered inputs and object keys produced byte-identical output (47 bytes).
A6: PASS — json, tempfile, os.replace, fsync, and samefile are available in the Python standard library.
```

## A7 strict JSON
```text
A7: FALSIFIED initial assumption — default json.loads accepted all 3 non-standard constants.
A7 correction microtest: PASS — parse_constant hook rejected all 3.
```

## A8/A9 corrective microtests
```text
A8: FALSIFIED v0 — parsed-equal numeric spellings produced different canonical strings and false conflict.
A8 correction: PASS — current project-canonical number rendering collapses 1 and 1.0 deterministically.
A9: FALSIFIED v0 — duplicate object member names silently used last-write-wins parsing.
A9 correction: PASS — current strict parser rejects duplicate object member names.
```

## Final integration suite
```text
test_blank_and_missing_id_are_rejected_before_output_change (test_mergesafe.MergeSafeIntegrationTests.test_blank_and_missing_id_are_rejected_before_output_change) ... ok
test_boolean_and_number_are_not_equivalent (test_mergesafe.MergeSafeIntegrationTests.test_boolean_and_number_are_not_equivalent) ... ok
test_conflicting_duplicate_preserves_previous_output (test_mergesafe.MergeSafeIntegrationTests.test_conflicting_duplicate_preserves_previous_output) ... ok
test_duplicate_object_members_are_rejected (test_mergesafe.MergeSafeIntegrationTests.test_duplicate_object_members_are_rejected) ... ok
test_equivalent_duplicates_collapse_and_output_is_canonical (test_mergesafe.MergeSafeIntegrationTests.test_equivalent_duplicates_collapse_and_output_is_canonical) ... ok
test_large_valid_number_does_not_overflow_to_nonfinite (test_mergesafe.MergeSafeIntegrationTests.test_large_valid_number_does_not_overflow_to_nonfinite) ... ok
test_malformed_input_reports_context_and_preserves_output (test_mergesafe.MergeSafeIntegrationTests.test_malformed_input_reports_context_and_preserves_output) ... ok
test_nonstandard_json_constants_are_rejected (test_mergesafe.MergeSafeIntegrationTests.test_nonstandard_json_constants_are_rejected) ... ok
test_numeric_equivalent_duplicates_collapse (test_mergesafe.MergeSafeIntegrationTests.test_numeric_equivalent_duplicates_collapse) ... ok
test_output_is_independent_of_input_order_and_key_order (test_mergesafe.MergeSafeIntegrationTests.test_output_is_independent_of_input_order_and_key_order) ... ok
test_replace_failure_preserves_previous_output_and_cleans_temp (test_mergesafe.MergeSafeIntegrationTests.test_replace_failure_preserves_previous_output_and_cleans_temp) ... ok
test_symlink_output_alias_is_rejected_without_source_change (test_mergesafe.MergeSafeIntegrationTests.test_symlink_output_alias_is_rejected_without_source_change) ... ok

----------------------------------------------------------------------
Ran 12 tests in 0.006s

OK
```

## Attack the judge
```text
baseline known-good: PASS
permissive non-standard constants: REJECTED
duplicate object members silently overwritten: REJECTED
numeric representation treated as identity: REJECTED
conflicting duplicate silently accepted: REJECTED
output/input alias check disabled: REJECTED
record output order depends on insertion order: REJECTED
staged replace bypassed: REJECTED
known-false mutants rejected: 7/7
```
