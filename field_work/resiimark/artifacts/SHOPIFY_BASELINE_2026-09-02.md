# Resiimark Shopify Baseline — 2026-09-02

Captured during live EFM field use on `2026-09-02` using the connected Shopify Admin API/ShopifyQL tools.

This artifact preserves the Shopify-side baseline used by the Resiimark continuity package. It does not contain supplier landed-cost, competitor-price, or fulfillment evidence; those must be captured separately rather than reconstructed from conversation memory.

## Store identity

Authenticated Shopify shop:

- Shop ID: `gid://shopify/Shop/83977994475`
- Name: `Resiimark`
- Underlying MyShopify domain: `6gnciw-zn.myshopify.com`
- Store URL / primary domain: `https://resiimark.myshopify.com`
- Currency: `USD`
- IANA timezone: `America/Denver`

The differing domain strings observed across Shopify tools resolve to the same authenticated shop: the Shopify GraphQL `shop` object returned both the underlying MyShopify domain and the current primary/store URL in one response.

## Catalog snapshot

A live product search returned 21 products total: 5 `ACTIVE` and 16 `ARCHIVED`.

### Active products

1. **Pure Titanium Keychain Pen** — $15.00
   - SKU `CJJT102670201AZ` — Natural Titanium
   - SKU `CJJT102670202BY` — Titanium Gray
2. **TC4 Titanium EDC Pry Tool** — $45.00
   - SKU `CJJT160517101AZ`
3. **Ultralight Titanium Camping Stove** — $25.00
   - SKU `CJLY125759301AZ`
4. **Titanium Quick-Release Keychain** — $30.00
   - SKU `CJYD244002801AZ`
5. **Pure Titanium Camping Mug** — $18.00
   - SKU `CJYD294925001AZ`

### Archived products

1. Titanium Tea Strainer — $60.00
2. Titanium Insulated Tea Bottle — $35.00
3. Titanium Insulated Office Cup — $89.00
4. Titanium EDC Starter Set — $79.00
5. Titanium Alloy Pocket Clip — $18.00
6. Titanium Alloy Fingertip Spinner — $25.00
7. Pure Titanium Water Bottle — 1L — $79.00
8. Pure Titanium Tasting Cups — $50.00 single / $65.00 pair
9. Pure Titanium Sealed Lighter — $45.00
10. Pure Titanium Polished Spoon — $15.00
11. Pure Titanium Outdoor Utility Clip — $29.00
12. Pure Titanium Ice Cubes — $19.00–$59.00 depending on quantity
13. Pure Titanium Frame Sunglasses — $59.00
14. Pure Titanium Folding Wood Stove — $80.00
15. Uncoated Pure Titanium Frying Pan — $600.00
16. Pure Titanium Outdoor Tea Set — $325.00

## 30-day Shopify analytics snapshot

ShopifyQL query window: `SINCE -30d UNTIL today`, captured `2026-09-02`.

Observed session funnel:

- Sessions: `183`
- Sessions with cart additions: `1`
- Sessions that reached checkout: `1`
- Sessions that completed checkout: `0`
- Reported conversion rate: `0.0`

A separate 30-day sales query grouped by product returned no rows.

## Claim boundary

This baseline establishes the authenticated shop identity, current catalog state, current Shopify retail prices/SKUs, and the reported Shopify analytics snapshot at capture time.

It does **not** establish why the store has no completed checkouts, whether the active products are economically viable, whether traffic was representative buyer traffic, whether supplier fulfillment is acceptable, or whether any product should be kept or removed.
