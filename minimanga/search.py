import sys

from pathlib import Path
from typing import Iterator, Sequence, Tuple

from minimanga.exceptions import TargetNotFound


Files = Iterator[Path]
Condition = Tuple[str, ...]
Targets = Sequence[Path]


def find_all(folder: Path, condition: Condition) -> Targets:
    try:
        targets = _to_find(folder.rglob('*'), condition)
    except TargetNotFound:
        sys.stderr.write('Nothing was found.\n')
        exit(1)
    return targets


def _to_find(files: Files, condition: Condition) -> Targets:
    targets = []
    for file in files:
        if file.suffix.lower() in condition:
            targets.append(file)
    if len(targets) == 0:
        raise TargetNotFound
    return targets
