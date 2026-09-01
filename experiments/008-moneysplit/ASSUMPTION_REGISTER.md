# Assumption Register — Initial

| ID | Importance | Assumption | Claim scope | Before test |
|---|---|---|---|---|
| A1 | Architectural | binary-float quota/remainder ranking is unsafe for exact cent allocation at large integer magnitudes | integer totals/weights beyond binary64 exact-integer range | E0 |
| A2 | Architectural | exact integer quotient/remainder arithmetic is sufficient to implement proportional allocation | nonnegative integer total and weights | E0 |
| A3 | Operational | after flooring exact quotas, undistributed cents are fewer than positive-weight recipients | valid nonnegative inputs with positive total weight | E0 |
| A4 | Operational | explicit original index can deterministically resolve equal remainders | equal exact remainder cases | E0 |
| A5 | Operational | zero total and zero-weight recipients have unambiguous invariant-preserving behavior; all-zero weights must be rejected | zero boundaries | E0 |
| A6 | Optimizing | Python integer arithmetic handles very large tested totals/weights without external numeric libraries | tested magnitudes through at least 10^50 | E0 |

Neighboring cases: one recipient, equal weights, unequal weights, tied remainders, zero total, mixed zero weights, all-zero weights, totals above 2^53.
