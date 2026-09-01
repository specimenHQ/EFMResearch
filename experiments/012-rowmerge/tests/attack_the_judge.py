import csv
import io
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))
from rowmerge import reconcile_csv


def mutant_numeric(left, right):
    def load(text):
        rows=list(csv.DictReader(io.StringIO(text, newline='')))
        out={}
        for r in rows:
            raw=r['id']
            key=str(int(raw)) if raw.isdigit() else raw
            out[key]=r
        return out
    l=load(left); r=load(right)
    return sorted(l.keys() & r.keys())


def mutant_duplicate_overwrite(left, right):
    l={r['id']:r for r in csv.DictReader(io.StringIO(left)) if r['id']}
    r={r['id']:r for r in csv.DictReader(io.StringIO(right)) if r['id']}
    return sorted(l.keys() & r.keys())


def mutant_source_order(left, right):
    l=[r for r in csv.DictReader(io.StringIO(left))]
    rid={r['id'] for r in csv.DictReader(io.StringIO(right))}
    return [r['id'] for r in l if r['id'] in rid]


def mutant_naive_split(text):
    lines=text.splitlines()
    header=lines[0].split(',')
    return [dict(zip(header, line.split(','))) for line in lines[1:]]


def mutant_lowercase(left, right):
    def ids(text):
        return {r['id'].lower() for r in csv.DictReader(io.StringIO(text)) if r['id']}
    return sorted(ids(left) & ids(right))


cases=[]
cases.append(('numeric coercion', mutant_numeric('id,v\n001,L\n', 'id,v\n1,R\n') == []))
try:
    mutant_duplicate_overwrite('id,v\n001,a\n001,b\n', 'id,v\n001,x\n')
    duplicate_rejected = False
except Exception:
    duplicate_rejected = True
cases.append(('duplicate overwrite', duplicate_rejected))
a = mutant_source_order('id,v\nb,2\na,1\n', 'id,v\na,x\nb,y\n')
b = mutant_source_order('id,v\na,1\nb,2\n', 'id,v\na,x\nb,y\n')
cases.append(('source-order authority', a == b == ['a','b']))
parsed = mutant_naive_split('id,note\n001,"a,b"\n002,"line1\nline2"\n')
cases.append(('naive split parser', len(parsed) == 2 and parsed[0].get('note') == 'a,b' and parsed[1].get('note') == 'line1\nline2'))
cases.append(('lowercase normalization near miss', mutant_lowercase('id,v\nA,L\n', 'id,v\na,R\n') == []))

accepted = reconcile_csv('id,v\n001,L\nA,x\n', 'id,v\n001,R\na,y\n')
accepted_ok = [m.identifier for m in accepted.matched] == ['001'] and [r['id'] for r in accepted.left_only] == ['A'] and [r['id'] for r in accepted.right_only] == ['a']

failed=[]
for name, mutant_passed_judge in cases:
    rejected = not mutant_passed_judge
    print(('REJECTED' if rejected else 'ACCEPTED FALSE'), '-', name)
    if not rejected:
        failed.append(name)
print(('ACCEPTED' if accepted_ok else 'REJECTED GOOD'), '- current implementation')
if not accepted_ok:
    failed.append('current implementation')
if failed:
    raise SystemExit('judge failure: ' + ', '.join(failed))
print('PASS: judge rejected all 5 known-false designs and accepted the current implementation')
