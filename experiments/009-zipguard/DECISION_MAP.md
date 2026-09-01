# Decision Map — ZipGuard

- Path authority: archive names are untrusted; extraction root is authoritative.
- Type authority: only regular files/directories may be materialized.
- Existing filesystem objects: never replace or traverse them.
- Duplicate destination names: reject archive before writes.
- Failure atomicity: validate whole archive before materialization; then create entries using no-overwrite primitives.
- Dependencies: stdlib only unless evidence requires more.