import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from retrybudget import RetryExhausted, run_with_retry
class Retryable(Exception): pass
class FakeTime:
    def __init__(self): self.now=0.0; self.sleeps=[]
    def clock(self): return self.now
ft=FakeTime(); calls=[0]
def oversleep(d): ft.sleeps.append(d); ft.now += d + .2
def fn(): calls[0]+=1; raise Retryable('x')
try:
    run_with_retry(fn, retry_on=(Retryable,), max_attempts=2, total_budget=.5, backoff=.4, clock=ft.clock, sleep=oversleep)
    raise SystemExit('FAIL: late retry was allowed')
except RetryExhausted as exc:
    assert exc.reason == 'deadline'
    assert calls[0] == 1
print('PASS: oversleep/clock advance rechecked before retry; no late attempt started')
