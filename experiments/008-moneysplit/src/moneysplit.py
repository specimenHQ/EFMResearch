def split_cents(total_cents: int, weights: list[int] | tuple[int, ...]) -> list[int]:
    if not isinstance(total_cents, int) or isinstance(total_cents, bool) or total_cents < 0:
        raise ValueError('total_cents must be a nonnegative integer')
    ws = list(weights)
    if not ws:
        raise ValueError('at least one weight is required')
    if any((not isinstance(w, int)) or isinstance(w, bool) or w < 0 for w in ws):
        raise ValueError('weights must be nonnegative integers')
    total_weight = sum(ws)
    if total_weight == 0:
        raise ValueError('at least one weight must be positive')

    base=[]; remainders=[]
    for w in ws:
        q, r = divmod(total_cents * w, total_weight)
        base.append(q); remainders.append(r)

    left = total_cents - sum(base)
    order = sorted(range(len(ws)), key=lambda i: (-remainders[i], i))
    for i in order[:left]:
        base[i] += 1
    return base
