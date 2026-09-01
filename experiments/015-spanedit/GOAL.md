# Goal — SpanEdit

Apply a batch of edits to one Python Unicode string where every edit coordinate is defined against the original, unmodified source.

Each edit is `(start, end, replacement)` using zero-based half-open Python string indices `[start,end)`.

Requirements:
- replacements, deletions, and zero-length insertions are supported;
- edits are simultaneous with respect to original-source coordinates;
- declaration order must not change the result;
- indices are Python string code-point indices, not byte offsets or grapheme-cluster indices;
- negative, reversed, or out-of-bounds spans are rejected;
- overlapping nonempty spans are rejected;
- an insertion strictly inside a nonempty edited span is rejected;
- insertions at the start or end boundary of a nonempty span are allowed;
- multiple insertions at the same original position are rejected as ambiguous;
- adjacent nonempty spans are allowed;
- an empty edit batch returns the source unchanged.

Scope: finite in-memory Python strings and edit batches. No rich-text model, grapheme segmentation, collaborative editing, persistence, diff algorithm, or cybersecurity claim. Protocol v0.3 unchanged; goal frozen before tests.