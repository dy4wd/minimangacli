from pathlib import Path
from typing import Generator

from exceptions import SpecifiedPathNotFolder


Files = Generator[Path, None, None]

def check_path(path: Path) -> Path:
    """Checks whether the specified path is a folder."""
    if not path.is_dir():
        raise SpecifiedPathNotFolder
    return path.absolute()


def get_all_files(folder: Path) -> Files:
    """Collects all files in the specified folder."""
    return folder.glob("**/*")
