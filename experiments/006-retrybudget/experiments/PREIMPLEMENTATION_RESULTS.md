# Preimplementation results

- A1 PASS E2: `time.monotonic()` advanced across controlled sleep; elapsed-time authority retained.
- A2 PASS E2: retryable subclass matched configured exception tuple while unrelated exception did not.
- A3 PASS E2: `None`, `False`, `0`, empty string/list/dict are all valid falsy return values; truthiness cannot be retry authority.
- A4 FALSIFIED naive design E2: at t=0.7 with deadline=1.0, fixed 0.5 backoff reaches 1.2; backoff must be clipped and deadline rechecked.
- A5 PASS E2: injected clock/sleep advanced deterministic fake time exactly.
- A6 PASS E2: synchronous callable exceeded a 0.01 scheduling budget while already running; hard cancellation is outside this build's earned scope.
