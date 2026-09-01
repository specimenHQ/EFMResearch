# Assumption Register — ZipGuard

| ID | Class | Assumption | Claim scope |
|---|---|---|---|
| A1 | Existential | ZIP member names can encode traversal or absolute-path attempts that must be rejected before extraction | POSIX-style ZIP names including `..`, leading `/`, and backslashes |
| A2 | Architectural | lexical normalization plus resolved-root containment is sufficient only if extraction never follows pre-existing symlinks | Linux/POSIX destination tree |
| A3 | Operational | ZIP symlink entries are detectable from Unix mode bits in `external_attr` and can be rejected | archives carrying Unix file type metadata |
| A4 | Operational | duplicate normalized destinations can exist and must be rejected before writes | case-sensitive POSIX destination |
| A5 | Operational | Python file creation with exclusive mode can prevent replacement of an existing final path | regular-file targets |
| A6 | Operational | validating all members before writes prevents archive-structure failures from causing partial extraction | validation-detectable failures |

Neighbor cases required before broader claims: `a/../b`, `../b`, `/b`, `a\\..\\b`, duplicate names, file-vs-directory collision, pre-existing symlink parent, symlink ZIP entry, and existing final file.