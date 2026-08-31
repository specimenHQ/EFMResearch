# SlotLock — Durable Goal

Build a tiny local reservation program whose critical invariant is:

> Two textual timestamps that identify the same real instant, or two concurrent
> attempts for that instant, must never create two active reservations.

Secondary requirements:
- persistence across restart;
- reserve, cancel, and list;
- preserve original user-entered timestamp for audit/display;
- reject timezone-less timestamps rather than silently guess;
- Python standard library only unless evidence proves that inadequate.

The goal deliberately does not prescribe SQLite, a framework, a server, or a UI.
