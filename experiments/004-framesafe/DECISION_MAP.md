# Decision Map — Before Code

| Area | Decision to earn | Consequence if wrong |
|---|---|---|
| Read semantics | Can one `recv(n)` be treated as n bytes? | Existential: truncated/corrupted messages |
| Framing | How are adjacent messages separated? | Architectural: coalesced TCP bytes merge messages |
| Disconnect | How is clean EOF distinguished from mid-frame EOF? | Operational: partial message accepted or hidden failure |
| Size bound | When is an oversized frame rejected? | Operational: excessive memory/read work |
| Byte order | How is frame length encoded across peers? | Architectural: incompatible length interpretation |
| Timeout | Does a per-read timeout bound total frame time? | Operational: slow trickle can defeat intended deadline |

No async framework, serialization format, database, or third-party networking package is justified by the goal.
