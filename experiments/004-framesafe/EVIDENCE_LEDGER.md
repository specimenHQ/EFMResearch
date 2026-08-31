# Evidence Ledger — Experiment 004 FrameSafe

| ID | Result | Evidence | Decision effect |
|---|---|---|---|
| A1 | confirmed | E2 | use exact-read loop; never assume one `recv` fills request |
| A2 | confirmed with neighbors | E2 | 4-byte length prefix retained; empty and adjacent frames included |
| A3 | confirmed | E2/E5 | clean EOF only before header; partial header/payload is truncation |
| A4 | confirmed | E2/E5 | reject declared oversize immediately after header |
| A5 | confirmed | E2/E5 | retain `struct !I` network-order uint32 framing |
| A6 | confirmed | E2/E5 | implement total frame deadline rather than relying on per-read socket timeout |
| J1 | judge hardened | E3 | 7/7 known-false readers rejected, including near-miss partial EOF and off-by-one max |
| I1 | integration | E5 | 11/11 integration tests pass; post-green second-frame stall preserves first frame and times out second |

No E6 operational claim.
