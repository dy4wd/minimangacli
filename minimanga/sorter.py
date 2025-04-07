import sys

from pathlib import Path
from typing import Iterator, Sequence, Tuple

from .exceptions import TargetNotFound


Files = Iterator[Path]
Pattern = Tuple[str, ...]
Targets = Sequence[Path]


def find_all(files: Files, pattern: Pattern) -> Targets:
    targets = []
    for file in files:
        if file.suffix[1:].lower() in pattern:
            targets.append(file)
    if len(targets) == 0:
        raise TargetNotFound
    return targets
