# Goal — Prebugging 007: Invoice service worker

Target: `specimenHQ/invoice` `app/sw.js`, frozen baseline blob `16f9ee32372235dabc7093ad5104a40f3b4c8ee4`.

Without modifying the Invoice repository, test whether the service worker's install/activate/fetch behavior can create stale, missing, or incorrectly substituted app-shell responses under plausible lifecycle and offline conditions. Findings must be reproduced against the frozen baseline before being counted.
