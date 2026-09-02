# EFM Continuity Standard

Version: `0.1`
Date: `2026-09-02`

## Purpose

EFM is increasingly expected to operate inside real work rather than only as isolated laboratory-style experiments. The continuity problem is therefore central: new evidence must survive changes of session, model, platform, collaborator, and time.

This standard defines the smallest durable project record needed for that continuity.

It does **not** replace EFM Protocol v0.3 or the Future-AI Handoff Standard. It is a lighter operational layer for ongoing field use.

## Core rule

> Store observations and decisions so that a future AI can continue from evidence rather than reconstructing intent from conversation history.

A project using this standard keeps five files:

1. `CURRENT_STATE.md`
2. `EVIDENCE_LEDGER.md`
3. `DECISIONS.md`
4. `OPEN_QUESTIONS.md`
5. `HANDOFF.md`

## Two storage classes

### Append-only records

`EVIDENCE_LEDGER.md` and `DECISIONS.md` are append-only.

Existing entries are never silently rewritten or deleted because later work changed the interpretation. If an entry is wrong, append a correction or superseding record that names the earlier ID.

This preserves provenance and negative/null results.

### Replaceable snapshots

`CURRENT_STATE.md` and `HANDOFF.md` may be rewritten as the project changes. They are summaries of the present, not historical authority.

`OPEN_QUESTIONS.md` may change status, but question entries are not deleted. Close them as `answered`, `deferred`, `abandoned`, or `superseded`.

## Stable IDs

Use stable IDs for durable records:

- evidence: `EV-YYYYMMDD-NNN`
- decisions: `D-YYYYMMDD-NNN`
- questions: `Q-YYYYMMDD-NNN`

IDs are never reused.

## Evidence record minimum

Every evidence entry records:

- ID and date;
- question or assumption;
- what happened;
- source/artifact location;
- evidence level if applicable;
- claim boundary: what the observation supports and does not support;
- consequence for the project.

A real-world event may count as evidence when the question is bounded and the observable outcome is preserved. A microtest does not have to be an artificial experiment.

## Decision record minimum

Every consequential decision records:

- ID and date;
- decision;
- evidence IDs supporting it;
- alternatives rejected, deferred, or still untested;
- reversal condition: what new evidence would justify reopening it.

A decision without evidence references is explicitly marked `provisional`.

## Open-question rule

`OPEN_QUESTIONS.md` contains uncertainties that could still change meaningful work.

Do not fill it with every unknown. Include a question when its answer could cause rework, invalidate a decision, materially change cost, or alter the result.

Each question states the next observable thing that would reduce the uncertainty.

## Snapshot rule

`CURRENT_STATE.md` answers only:

- What are we trying to achieve?
- What exists now?
- What is currently believed because of evidence?
- What is being tried now?
- What is the next action?

Do not turn it into a changelog.

## Handoff rule

`HANDOFF.md` is the compact reconstruction layer for a fresh AI. It should contain no unique evidence or decisions. It points to stable IDs and durable artifacts.

A fresh AI should be able to read `HANDOFF.md`, then follow IDs into the ledger/decision/question files without needing the original conversation.

## Anti-corruption rules

1. Never delete a negative, null, failed, or contradictory evidence entry.
2. Never silently edit an old evidence result to match a later interpretation.
3. Corrections append and reference the record they supersede.
4. Decisions cite evidence IDs rather than paraphrasing unsupported memory.
5. If evidence is missing, say `unknown` or `provisional`; do not infer a result into the record.
6. `HANDOFF.md` and `CURRENT_STATE.md` are caches, not authority.
7. Store raw artifacts beside or behind evidence references whenever practical.
8. Record protocol deviations and real-world confounders rather than cleaning them out of history.
9. Do not promote field observations beyond what they establish.
10. Prefer one durable fact recorded once and referenced by ID over duplicated prose in multiple files.

## Field-use loop

The normal operating loop is:

`uncertainty -> smallest credible action -> observable real-world result -> evidence record -> decision -> updated state -> next uncertainty`

A controlled microtest is one possible action inside this loop, not the definition of the loop.

## Fresh-context test

A continuity package is adequate if a fresh AI can answer, without the original conversation:

1. what the project is trying to achieve;
2. what is actually true now;
3. which observations changed the work;
4. why consequential decisions were made;
5. what remains unresolved;
6. what should happen next;
7. what new evidence would cause an important decision to be reopened.

If those answers require conversational memory, continuity has failed.
