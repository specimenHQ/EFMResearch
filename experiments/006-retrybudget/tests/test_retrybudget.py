import sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from retrybudget import RetryExhausted, run_with_retry

class Retryable(Exception): pass
class RetryableChild(Retryable): pass
class Fatal(Exception): pass

class FakeTime:
    def __init__(self): self.now = 0.0; self.sleeps=[]
    def clock(self): return self.now
    def sleep(self, d): self.sleeps.append(d); self.now += d

class Tests(unittest.TestCase):
    def test_success_first_attempt(self):
        self.assertEqual(run_with_retry(lambda: 7, retry_on=(Retryable,), max_attempts=3, total_budget=1), 7)
    def test_falsy_successes_are_success(self):
        for value in (None, False, 0, '', [], {}):
            calls=[0]
            def fn(v=value): calls[0]+=1; return v
            self.assertIs(run_with_retry(fn, retry_on=(Retryable,), max_attempts=3, total_budget=1), value)
            self.assertEqual(calls[0], 1)
    def test_retryable_subclass_retries(self):
        calls=[0]
        def fn():
            calls[0]+=1
            if calls[0] < 2: raise RetryableChild('x')
            return 'ok'
        self.assertEqual(run_with_retry(fn, retry_on=(Retryable,), max_attempts=3, total_budget=1), 'ok')
        self.assertEqual(calls[0], 2)
    def test_nonretryable_propagates_without_retry(self):
        calls=[0]
        def fn(): calls[0]+=1; raise Fatal('stop')
        with self.assertRaises(Fatal): run_with_retry(fn, retry_on=(Retryable,), max_attempts=3, total_budget=1)
        self.assertEqual(calls[0], 1)
    def test_max_attempts_exact(self):
        calls=[0]
        def fn(): calls[0]+=1; raise Retryable('x')
        with self.assertRaises(RetryExhausted) as cm: run_with_retry(fn, retry_on=(Retryable,), max_attempts=3, total_budget=100)
        self.assertEqual(calls[0], 3); self.assertEqual(cm.exception.reason, 'max_attempts')
    def test_budget_zero_allows_first_attempt_but_no_retry(self):
        calls=[0]; ft=FakeTime()
        def fn(): calls[0]+=1; raise Retryable('x')
        with self.assertRaises(RetryExhausted) as cm: run_with_retry(fn, retry_on=(Retryable,), max_attempts=3, total_budget=0, clock=ft.clock, sleep=ft.sleep)
        self.assertEqual(calls[0], 1); self.assertEqual(cm.exception.reason, 'deadline')
    def test_backoff_clipped_to_remaining_budget(self):
        ft=FakeTime(); calls=[0]
        def fn(): calls[0]+=1; ft.now += .7; raise Retryable('x')
        with self.assertRaises(RetryExhausted): run_with_retry(fn, retry_on=(Retryable,), max_attempts=3, total_budget=1.0, backoff=.5, clock=ft.clock, sleep=ft.sleep)
        self.assertEqual(len(ft.sleeps), 1); self.assertAlmostEqual(ft.sleeps[0], .3, places=12); self.assertEqual(calls[0], 1)
    def test_zero_backoff_can_retry_before_deadline(self):
        ft=FakeTime(); calls=[0]
        def fn():
            calls[0]+=1
            if calls[0] == 1: raise Retryable('x')
            return 'ok'
        self.assertEqual(run_with_retry(fn, retry_on=(Retryable,), max_attempts=2, total_budget=1, backoff=0, clock=ft.clock, sleep=ft.sleep), 'ok')
    def test_exact_deadline_does_not_start_retry(self):
        ft=FakeTime(); calls=[0]
        def fn(): calls[0]+=1; ft.now=1.0; raise Retryable('x')
        with self.assertRaises(RetryExhausted): run_with_retry(fn, retry_on=(Retryable,), max_attempts=2, total_budget=1.0, clock=ft.clock, sleep=ft.sleep)
        self.assertEqual(calls[0], 1)
    def test_invalid_policy_values_rejected(self):
        for kwargs in ({'max_attempts':0,'total_budget':1,'backoff':0}, {'max_attempts':1,'total_budget':-1,'backoff':0}, {'max_attempts':1,'total_budget':1,'backoff':-1}):
            with self.assertRaises(ValueError): run_with_retry(lambda: 1, retry_on=(Retryable,), **kwargs)

if __name__ == '__main__': unittest.main(verbosity=2)
