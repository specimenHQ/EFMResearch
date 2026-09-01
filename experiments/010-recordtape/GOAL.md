# Goal — RecordTape

Append byte records to one local file and recover all and only previously complete records after a process-level torn final write. A fully written record whose bytes are corrupted must be reported as corruption, not silently treated as a recoverable torn tail. Prior valid records must remain intact.

Scope: single writer, local regular file, process-level partial/torn write simulation. No claim about concurrent writers, storage-device lies, or power-loss durability. Protocol v0.2 unchanged; goal frozen before tests.