# Preimplementation Results — ZipGuard

- A1 E2: traversal/absolute/backslash forms are directly detectable from member names; reject rather than sanitize.
- A2 E2: resolving a path through a pre-existing symlink parent escapes the root; symlink parents cannot be traversed.
- A3 E2: Unix symlink metadata is detectable via `external_attr >> 16` and `stat.S_ISLNK`.
- A4 E2: ZIP permits normalized duplicate/collision forms such as `a/b` vs `a/./b` and file `x` vs directory `x/`; validate all names/types before writes.
- A5 E2: exclusive file creation rejects an existing final file without changing its contents.
- A6 E2 design boundary: whole-archive structural validation can occur before materialization; runtime filesystem/I/O failures are outside the atomicity claim.
- A7 E2 newly admitted: validate-then-open by pathname is unsafe. A controlled parent-directory-to-symlink swap after successful containment validation caused `open(...,'xb')` to write outside the root.

Decision: implementation must use POSIX descriptor-relative traversal with `O_DIRECTORY|O_NOFOLLOW` for parents and `O_CREAT|O_EXCL|O_NOFOLLOW` for files. No third-party dependency is yet justified.