from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
import os, shutil, stat, zipfile

class ZipGuardError(Exception): pass
class UnsafeMember(ZipGuardError): pass
class DestinationConflict(ZipGuardError): pass

@dataclass(frozen=True)
class Member:
    info: zipfile.ZipInfo
    parts: tuple[str, ...]
    is_dir: bool

def _normalize(name: str) -> tuple[str, ...]:
    if not name or "\x00" in name:
        raise UnsafeMember("empty or NUL member name")
    if "\\" in name:
        raise UnsafeMember(f"backslash in member name: {name!r}")
    p = PurePosixPath(name)
    if p.is_absolute():
        raise UnsafeMember(f"absolute member path: {name!r}")
    parts=[]
    for part in p.parts:
        if part in ("", "."):
            continue
        if part == "..":
            raise UnsafeMember(f"parent traversal: {name!r}")
        parts.append(part)
    if not parts:
        raise UnsafeMember(f"empty normalized path: {name!r}")
    return tuple(parts)

def _classify(info: zipfile.ZipInfo) -> bool:
    mode = (info.external_attr >> 16) & 0xFFFF
    ftype = stat.S_IFMT(mode)
    by_name_dir = info.filename.endswith("/")
    if ftype:
        if stat.S_ISLNK(mode):
            raise UnsafeMember(f"symlink member: {info.filename!r}")
        if stat.S_ISDIR(mode):
            return True
        if not stat.S_ISREG(mode):
            raise UnsafeMember(f"non-regular member: {info.filename!r}")
        if by_name_dir:
            raise UnsafeMember(f"type disagreement for {info.filename!r}")
        return False
    return by_name_dir

def validate_archive(zf: zipfile.ZipFile) -> list[Member]:
    out=[]
    seen: dict[tuple[str,...], bool] = {}
    for info in zf.infolist():
        parts=_normalize(info.filename)
        is_dir=_classify(info)
        if parts in seen:
            raise DestinationConflict(f"duplicate destination: {'/'.join(parts)}")
        seen[parts]=is_dir
        out.append(Member(info, parts, is_dir))
    for parts, is_dir in seen.items():
        for i in range(1, len(parts)):
            prefix=parts[:i]
            if prefix in seen and not seen[prefix]:
                raise DestinationConflict(f"file/directory collision: {'/'.join(prefix)} blocks {'/'.join(parts)}")
    return out

_DIR_FLAGS = os.O_RDONLY | getattr(os, "O_DIRECTORY", 0) | getattr(os, "O_NOFOLLOW", 0)
_FILE_FLAGS = os.O_WRONLY | os.O_CREAT | os.O_EXCL | getattr(os, "O_NOFOLLOW", 0)

def _open_root(root: Path) -> int:
    root.mkdir(parents=True, exist_ok=True)
    try:
        return os.open(root, _DIR_FLAGS)
    except OSError as exc:
        raise DestinationConflict(f"unsafe extraction root: {root}") from exc

def _open_dir_chain(root_fd: int, parts: tuple[str,...]) -> int:
    fd=os.dup(root_fd)
    try:
        for part in parts:
            try:
                nxt=os.open(part, _DIR_FLAGS, dir_fd=fd)
            except FileNotFoundError:
                try:
                    os.mkdir(part, 0o755, dir_fd=fd)
                except FileExistsError:
                    pass
                try:
                    nxt=os.open(part, _DIR_FLAGS, dir_fd=fd)
                except OSError as exc:
                    raise DestinationConflict(f"unsafe directory component: {part!r}") from exc
            except OSError as exc:
                raise DestinationConflict(f"unsafe directory component: {part!r}") from exc
            os.close(fd)
            fd=nxt
        return fd
    except:
        os.close(fd)
        raise

def extract_zip(zip_path: str | os.PathLike[str], root: str | os.PathLike[str]) -> None:
    root=Path(root)
    with zipfile.ZipFile(zip_path, "r") as zf:
        members=validate_archive(zf)
        root_fd=_open_root(root)
        try:
            for m in members:
                if m.is_dir:
                    dfd=_open_dir_chain(root_fd, m.parts)
                    os.close(dfd)
                    continue
                parent_fd=_open_dir_chain(root_fd, m.parts[:-1])
                name=m.parts[-1]
                file_fd=None
                try:
                    try:
                        file_fd=os.open(name, _FILE_FLAGS, 0o600, dir_fd=parent_fd)
                    except FileExistsError as exc:
                        raise DestinationConflict(f"destination exists: {'/'.join(m.parts)}") from exc
                    except OSError as exc:
                        raise DestinationConflict(f"unsafe destination: {'/'.join(m.parts)}") from exc
                    try:
                        with zf.open(m.info, "r") as src, os.fdopen(file_fd, "wb", closefd=True) as dst:
                            file_fd=None
                            shutil.copyfileobj(src, dst, length=1024*1024)
                    except Exception:
                        try: os.unlink(name, dir_fd=parent_fd)
                        except OSError: pass
                        raise
                finally:
                    if file_fd is not None: os.close(file_fd)
                    os.close(parent_fd)
        finally:
            os.close(root_fd)
