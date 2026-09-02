# Resiimark EFM Evidence Ledger

Append only. Corrections and later interpretations must be added as new records rather than rewriting prior evidence.

## EV-20260902-003
- Date: `2026-09-02`
- Question/assumption: Do the differing Shopify domain strings observed during this session refer to the same Resiimark shop, or could catalog and analytics data be coming from different stores?
- Observation: A Shopify Admin GraphQL query against the authenticated shop returned shop ID `gid://shopify/Shop/83977994475`, name `Resiimark`, underlying MyShopify domain `6gnciw-zn.myshopify.com`, and primary/store URL `https://resiimark.myshopify.com` in the same `shop` object.
- Source/artifact: `field_work/resiimark/artifacts/SHOPIFY_BASELINE_2026-09-02.md`
- Strength: `E2 — Controlled microtest` at the authenticated Shopify shop-identity boundary.
- Supports: The catalog search and ShopifyQL analytics that reported the underlying `6gnciw-zn.myshopify.com` domain can be attributed to the same authenticated Resiimark shop whose primary storefront domain is `resiimark.myshopify.com`.
- Does not establish: Product viability, sales performance quality, supplier economics, or fulfillment quality.
- Project consequence: Shopify-side observations from this session may be recorded as Resiimark evidence rather than quarantined as potentially cross-store data.
- Supersedes/corrects: `none`

## EV-20260902-004
- Date: `2026-09-02`
- Question/assumption: What is the current Shopify catalog state that Resiimark is actually exposing for further viability checks?
- Observation: A live Shopify product search returned 21 products: 5 `ACTIVE` and 16 `ARCHIVED`. The active products are Pure Titanium Keychain Pen ($15), TC4 Titanium EDC Pry Tool ($45), Ultralight Titanium Camping Stove ($25), Titanium Quick-Release Keychain ($30), and Pure Titanium Camping Mug ($18). Current active SKUs are preserved in the baseline artifact.
- Source/artifact: `field_work/resiimark/artifacts/SHOPIFY_BASELINE_2026-09-02.md`
- Strength: `E1 — Observation`
- Supports: The bounded catalog state and current Shopify retail-price/SKU baseline at capture time.
- Does not establish: That any active product is profitable, competitive, desirable, or correctly positioned; archived status also does not establish why a product was archived.
- Project consequence: Further product work should test the five active products rather than treating the full historical catalog as equally live.
- Supersedes/corrects: `none`

## EV-20260902-005
- Date: `2026-09-02`
- Question/assumption: What does Shopify currently report about recent Resiimark conversion activity?
- Observation: For the ShopifyQL window `SINCE -30d UNTIL today`, captured `2026-09-02`, Shopify reported 183 sessions, 1 session with a cart addition, 1 session reaching checkout, 0 sessions completing checkout, and 0.0 reported conversion rate. A separate 30-day product sales query returned no rows.
- Source/artifact: `field_work/resiimark/artifacts/SHOPIFY_BASELINE_2026-09-02.md`
- Strength: `E1 — Observation`
- Supports: Resiimark has no Shopify-reported completed checkout in this captured 30-day window and no product sales rows in the companion query.
- Does not establish: Why conversion is zero, whether traffic was representative customer traffic, whether product selection is the cause, or whether the store would convert under materially different traffic, price, fulfillment, or merchandising conditions.
- Project consequence: Do not use the absence of sales as a verdict on a specific product. Resolve product economics, market competition, fulfillment, and traffic-quality uncertainties at their own boundaries.
- Supersedes/corrects: `none`
