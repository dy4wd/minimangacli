import sys

from pathlib import Path
from typing import Iterator, Sequence, Tuple

from .exceptions import TargetNotFound


Files = Iterator[Path]
Pattern = Tuple[str, ...]
Targets = Sequence[Path]


def find_all(files: Files, pattern: Pattern, msg: str) -> Targets:
    sys.stdout.write(f"{msg} search...\n")
    try:
        targets = _sort(files, pattern)
    except TargetNotFound:
        sys.stderr.write(f"{msg} not found.\n")
        exit(1)
    sys.stdout.write(f"{msg} search... Done.\n")
    return targets


def _sort(files: Files, pattern: Pattern) -> Targets:
    targets = []
    for file in files:
        if file.suffix[1:].lower() in pattern:
            targets.append(file)
    if len(targets) == 0:
        raise TargetNotFound
    return targets
