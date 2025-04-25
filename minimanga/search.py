import sys

from pathlib import Path
from collections.abc import Iterator, Sequence

from minimanga.exceptions import TargetNotFound


Condition = Sequence[str]


def find_all(folder: Path, condition: Condition) -> list[Path]:
    try:
        targets = _to_find(folder.rglob('*'), condition)
    except TargetNotFound:
        sys.stderr.write('Nothing was found.\n')
        exit(1)
    return targets


def _to_find(files: Iterator[Path], condition: Condition) -> list[Path]:
    targets = []
    for file in files:
        if file.suffix.lower() in condition:
            targets.append(file)
    if len(targets) == 0:
        raise TargetNotFound
    return targets
