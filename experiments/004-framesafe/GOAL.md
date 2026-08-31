# FrameSafe — Durable Goal

Build a tiny local TCP framing tool whose critical invariant is:

> A byte message is delivered exactly once as one complete message, regardless of how TCP splits or coalesces reads; truncated or oversized frames are never accepted as complete.

Secondary requirements:
- standard library only unless evidence requires otherwise;
- binary-safe payloads, including empty payloads;
- bounded accepted frame size;
- explicit distinction between clean EOF before a frame and EOF inside a frame;
- small localhost client/server surface for integration testing.

The goal does not prescribe buffering strategy, thread model, or application framework.
