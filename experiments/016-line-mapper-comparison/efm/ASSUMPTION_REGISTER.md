# EFM Assumption Register — Experiment 016 Line Mapper

Protocol: v0.3

| ID | Class | Assumption | Claim scope | Falsifier / decision effect |
|---|---|---|---|---|
| A1 | Architectural | `str.splitlines(keepends=True)` can serve as the segmentation authority for the frozen separator set | strings containing required and non-required Unicode line-break characters | it splits on characters outside `\n`, `\r`, `\r\n`; reject convenience API as authority |
| A2 | Architectural | an explicit scanner limited to `\r`, `\n`, and `\r\n` can produce exact `(content_start, content_end, separator_end)` spans | finite Python strings | scanner disagrees with separately derived exact-separator oracle; change segmentation design |
| A3 | Operational | empty text and text ending in a required separator need explicit final-empty-line handling | `""`, `"a\n"`, `"a\r"`, `"a\r\n"` | ordinary segmentation already produces required final empty line automatically; special handling unnecessary |
| A4 | Operational | for CRLF, the boundary between `\r` and `\n` is the only integer offset inside the separator and must be rejected, while both outer boundaries are valid content positions | one CRLF-separated two-line fixture | mapping cannot distinguish these three boundaries consistently; revise offset semantics |
| A5 | Operational | Python `str` offsets remain code-point offsets on multibyte Unicode text and can round-trip independently of UTF-8 byte length | emoji and combining-mark fixtures | code-point and encoded-byte positions behave equivalently in tested boundary cases; unit concern weakens |
| A6 | Operational | round-trip over every valid content position plus a separately implemented exact-separator regex oracle can independently validate the mapping structure | mixed newline fixtures including non-required Unicode separators | independent oracle or round-trip invariant cannot detect plausible segmentation/mapping errors; evaluator strategy changes |

Prebuild completeness requirement: A1–A6 must each be tested, durably deferred, or removed from active scope before EFM implementation begins.

Required neighboring fixtures before implementation: empty text, no separator, each required separator, mixed required separators, trailing separator, consecutive separators, CRLF interior offset, emoji, combining mark, and at least two Unicode line-break characters that are not in the frozen separator set.