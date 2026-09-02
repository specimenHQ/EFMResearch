# Resiimark EFM Handoff

Updated: `2026-09-02`

This is a reconstruction map, not the authoritative evidence store.

## Goal
Prebug the existing Resiimark Shopify store using EFM field use: test consequential product/supplier assumptions before more catalog, marketing, or cosmetic work compounds them.

## Where things stand
Resiimark already existed before this field package, so it is explicitly **not** being retroactively labeled EFM-native.

The Shopify identity boundary was checked after different domain strings appeared in connected-tool outputs. They resolve to the same authenticated shop — `EV-20260902-003`.

Current bounded assortment: 21 Shopify products total, 5 active and 16 archived — `EV-20260902-004`. The five active products are:

- Pure Titanium Keychain Pen — $15
- TC4 Titanium EDC Pry Tool — $45
- Ultralight Titanium Camping Stove — $25
- Titanium Quick-Release Keychain — $30
- Pure Titanium Camping Mug — $18

A 30-day Shopify snapshot reported 183 sessions, 1 cart addition, 1 checkout reached, and 0 completed checkouts — `EV-20260902-005`. Do not infer cause from this observation.

## Decision currently in force
- `D-20260902-003` — treat Resiimark as a field-use/prebugging case; pause catalog expansion and cosmetic optimization as decision drivers while consequential product economics, competition, and fulfillment uncertainties are checked.

## Open questions
- `Q-20260902-002` — do supplier product + shipping economics support current retail prices?
- `Q-20260902-003` — do readily available competitors invalidate any active offer?
- `Q-20260902-004` — does supplier fulfillment time contradict premium positioning?

## Next action
Choose one of the five active SKUs and capture current supplier product cost, shipping cost, and delivery estimate to a declared representative US destination from the actual supplier source. Preserve the source/date, then compare that same product against current customer-facing alternatives.

## Do not assume
- Prior CJ/EPROLO screenshots are exact durable evidence until their relevant values are recaptured or otherwise preserved with provenance.
- Zero completed checkouts proves a specific product is bad.
- Titanium material alone creates a premium offer.
- An attractive supplier source price remains attractive after shipping.
- The five active products should all survive the field check.

## Read order
1. `CURRENT_STATE.md`
2. `OPEN_QUESTIONS.md`
3. `EVIDENCE_LEDGER.md`
4. `DECISIONS.md`
5. `artifacts/SHOPIFY_BASELINE_2026-09-02.md`
