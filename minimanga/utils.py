from pathlib import Path

from exceptions import SpecifiedPathNotFolder


def check_path(path: Path) -> Path:
    """Checks whether the specified path is a folder."""
    if not path.is_dir():
        raise SpecifiedPathNotFolder
    return path.absolute()
