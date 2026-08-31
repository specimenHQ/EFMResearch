from dataclasses import dataclass
import os
import signal
import subprocess
from typing import Sequence

@dataclass(frozen=True)
class RunResult:
    argv: tuple[str, ...]
    returncode: int
    stdout: str
    stderr: str
    timed_out: bool

    @property
    def ok(self) -> bool:
        return (not self.timed_out) and self.returncode == 0

    @property
    def signaled(self) -> bool:
        return (not self.timed_out) and self.returncode < 0


def run_command(argv: Sequence[str], *, timeout: float) -> RunResult:
    argv = tuple(argv)
    if not argv:
        raise ValueError('argv must not be empty')
    if timeout < 0:
        raise ValueError('timeout must be nonnegative')
    p = subprocess.Popen(argv, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=False, start_new_session=True)
    timed_out = False
    try:
        stdout, stderr = p.communicate(timeout=timeout)
    except subprocess.TimeoutExpired:
        timed_out = True
        try:
            os.killpg(p.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
        stdout, stderr = p.communicate()
    return RunResult(argv, p.returncode, stdout, stderr, timed_out)
