from pathlib import Path

from .exceptions import SpecifiedPathNotFolder


def is_dir(path: Path):
    if not path.is_dir():
        raise SpecifiedPathNotFolder
