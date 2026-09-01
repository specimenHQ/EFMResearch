from __future__ import annotations
import queue
import threading
from collections.abc import Callable
from typing import Generic, TypeVar

T=TypeVar("T")
_STOP=object()

class QueueGate(Generic[T]):
    def __init__(self, handler: Callable[[T], None], *, capacity: int, workers: int = 1):
        if not isinstance(capacity,int) or isinstance(capacity,bool) or capacity < 1:
            raise ValueError("capacity must be >= 1")
        if not isinstance(workers,int) or isinstance(workers,bool) or workers < 1:
            raise ValueError("workers must be >= 1")
        self._handler=handler
        self._q: queue.Queue[object]=queue.Queue(maxsize=capacity)
        self._state_lock=threading.Lock()
        self._error_lock=threading.Lock()
        self._closed=False
        self._done=threading.Event()
        self._errors: list[tuple[object,Exception]]=[]
        self._threads=[threading.Thread(target=self._worker,daemon=True,name=f"QueueGate-{i}") for i in range(workers)]
        for t in self._threads: t.start()

    @property
    def closed(self) -> bool:
        with self._state_lock:
            return self._closed

    @property
    def errors(self) -> tuple[tuple[object,Exception],...]:
        with self._error_lock:
            return tuple(self._errors)

    def submit(self, item: T) -> bool:
        with self._state_lock:
            if self._closed:
                return False
            try:
                self._q.put_nowait(item)
            except queue.Full:
                return False
            return True

    def _worker(self) -> None:
        while True:
            item=self._q.get()
            try:
                if item is _STOP:
                    return
                try:
                    self._handler(item)
                except Exception as exc:
                    with self._error_lock:
                        self._errors.append((item,exc))
            finally:
                self._q.task_done()

    def close(self) -> None:
        owner=False
        with self._state_lock:
            if not self._closed:
                self._closed=True
                owner=True
        if not owner:
            self._done.wait()
            return
        self._q.join()
        for _ in self._threads:
            self._q.put(_STOP)
        self._q.join()
        for t in self._threads:
            t.join()
        self._done.set()
