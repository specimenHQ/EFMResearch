from dataclasses import dataclass
import time
from typing import Callable, TypeVar

T = TypeVar('T')

@dataclass(frozen=True)
class RetryExhausted(Exception):
    reason: str
    attempts: int
    last_exception: BaseException

    def __str__(self) -> str:
        return f"retry exhausted: {self.reason} after {self.attempts} attempt(s): {self.last_exception}"


def run_with_retry(
    fn: Callable[[], T],
    *,
    retry_on: tuple[type[BaseException], ...],
    max_attempts: int,
    total_budget: float,
    backoff: float = 0.0,
    clock: Callable[[], float] = time.monotonic,
    sleep: Callable[[float], None] = time.sleep,
) -> T:
    if max_attempts < 1:
        raise ValueError('max_attempts must be >= 1')
    if total_budget < 0:
        raise ValueError('total_budget must be >= 0')
    if backoff < 0:
        raise ValueError('backoff must be >= 0')

    deadline = clock() + total_budget
    attempts = 0

    while True:
        attempts += 1
        try:
            return fn()
        except retry_on as exc:
            if attempts >= max_attempts:
                raise RetryExhausted('max_attempts', attempts, exc) from exc

            now = clock()
            if now >= deadline:
                raise RetryExhausted('deadline', attempts, exc) from exc

            delay = min(backoff, max(0.0, deadline - now))
            if delay:
                sleep(delay)

            if clock() >= deadline:
                raise RetryExhausted('deadline', attempts, exc) from exc
