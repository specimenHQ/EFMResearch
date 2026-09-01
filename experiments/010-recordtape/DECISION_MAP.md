# Decision Map — RecordTape

- Framing must identify record boundaries without trusting file EOF as success.
- Integrity evidence must cover both declared length and payload.
- Incomplete final record may be discarded; complete-record corruption must stop recovery.
- Recovery may truncate only to the last independently verified record boundary.
- Record length is bounded before allocation/read.
- No third-party dependency unless stdlib cannot support the tested boundary.