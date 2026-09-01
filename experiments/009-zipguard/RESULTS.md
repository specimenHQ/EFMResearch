# Results — Experiment 009 ZipGuard

Integration: 11/11 pass. Cases: normal nested/empty, parent traversal, absolute path, backslash traversal, ZIP symlink, normalized duplicate, file-directory collision, existing file preservation, pre-existing symlink parent, symlink root, explicit directory.

Post-green: PASS. Full extraction with an injected parent-directory-to-symlink swap after parent fd acquisition wrote to the already-open in-root directory, not the outside symlink target.

Judge: PASS 5/5 known-false implementations rejected: sanitize-parent, allow ZIP symlink, ignore duplicate destination, allow overwrite, follow parent symlink.
