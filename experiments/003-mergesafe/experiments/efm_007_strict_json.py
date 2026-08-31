import json

def reject_constant(token: str):
    raise ValueError(f"non-standard JSON constant: {token}")

bad = ['{"id":"x","v":NaN}', '{"id":"x","v":Infinity}', '{"id":"x","v":-Infinity}']
accepted_default = []
rejected_strict = []
for text in bad:
    try:
        json.loads(text)
        accepted_default.append(text)
    except ValueError:
        pass
    try:
        json.loads(text, parse_constant=reject_constant)
    except ValueError:
        rejected_strict.append(text)

assert len(accepted_default) == 3
assert len(rejected_strict) == 3
print('A7: FALSIFIED initial assumption — default json.loads accepted all 3 non-standard constants.')
print('A7 correction microtest: PASS — parse_constant hook rejected all 3.')
