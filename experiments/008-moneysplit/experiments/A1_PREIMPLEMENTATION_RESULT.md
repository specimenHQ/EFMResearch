# A1 preimplementation result

A controlled search found a binary-float remainder-ranking failure at total `9007199255475472`, weights `[12,13,5,7]`.

Exact remainders over denominator 37: `[21,32,18,3]`; leftover cents: 2; exact award order begins recipients 1 then 0.

Binary-float fractional parts collapse to `[0.5,0.0,0.5,0.0]`, producing the wrong award order. A1 falsified naive float authority at E2.
