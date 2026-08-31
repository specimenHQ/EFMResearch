# Integration Checkpoint — Experiment 004

Final suite: **11/11 passed**.

Integrated behaviors:
- fragmented header and payload;
- adjacent frames;
- empty and binary payloads;
- clean EOF versus partial header/payload EOF;
- exact-max and oversized frames;
- total deadline against slow trickle;
- multiple frames on one connection;
- real localhost TCP echo.

Protocol v0.2 post-green challenge:
- after the initial green suite, a real TCP stream was deliberately fragmented and coalesced across three messages;
- all three messages were echoed with exact boundaries and bytes;
- no implementation change was required.

Evidence level: **E5 integration**. No E6 claim.
