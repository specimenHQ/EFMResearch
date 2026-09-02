# EFM Decisions

Append only. Consequential decisions cite evidence. Provisional decisions remain explicitly provisional until stronger evidence earns them.

## D-20260902-001
- Date: `2026-09-02`
- Status: `provisional`
- Decision: Treat longitudinal real-world use as a primary path for learning whether EFM is useful. Controlled experiments remain available when a consequential uncertainty benefits from isolation, but EFM itself will not be validated only through an expanding laboratory program.
- Evidence: `EV-20260902-001`, `EV-20260902-002`
- Alternatives: Continue primarily with lab-style comparative experiments; suspend methodology work until stronger formal validation exists.
- Reason: EFM is now operating inside real projects, and the practical continuity problem is observable now. Prior handoff tests already indicate that preserving durable evidence across AI contexts is feasible and valuable.
- Reopen if: Field use produces evidence that uncontrolled conditions make EFM decisions uninterpretable, or a controlled design is required to resolve a consequential dispute.
- Supersedes: `none`

## D-20260902-002
- Date: `2026-09-02`
- Status: `provisional`
- Decision: Use five durable files as the default continuity layer: `CURRENT_STATE.md`, `EVIDENCE_LEDGER.md`, `DECISIONS.md`, `OPEN_QUESTIONS.md`, and `HANDOFF.md`.
- Evidence: `EV-20260902-001`, `EV-20260902-002`
- Alternatives: One large handoff document; conversation-memory dependence; a larger database/schema; project-specific unstructured notes.
- Reason: The five-file split separates mutable present-state summaries from append-only provenance while staying small enough for routine use by humans and AI agents.
- Reopen if: Real projects show duplicated maintenance, missing provenance, poor reconstruction, or excessive token/attention cost.
- Supersedes: `none`
