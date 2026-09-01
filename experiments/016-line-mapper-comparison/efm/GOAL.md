# EFM Goal — Experiment 016 Line Mapper

Implement the preregistered `line_mapper` task without changing its frozen requirements.

The EFM arm must map logical line/column positions to Python Unicode string offsets and back using only `\n`, `\r\n`, and lone `\r` as line separators, preserve the required empty/trailing-line semantics, reject invalid coordinates and CRLF-interior offsets, and satisfy round-trip for every valid content position.

Protocol v0.3 applies unchanged. The build-first arm is already frozen and must not be modified during EFM investigation.