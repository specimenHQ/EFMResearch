# Goal — ZipGuard

Extract an untrusted ZIP archive into a chosen destination while ensuring no archive entry can write outside that destination, replace a pre-existing filesystem object, or create/follow a symbolic link. Valid regular files and directories should extract without third-party dependencies.

Protocol: v0.2, applied unchanged. Goal frozen before microtests.