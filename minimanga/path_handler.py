from pathlib import Path

from . import config
from .exceptions import SpecifiedPathNotFolder


def is_dir(path: Path):
    if not path.is_dir():
        raise SpecifiedPathNotFolder


def generate_path_to_save(target_folder: Path) -> Path:
    return target_folder.with_name(f"{target_folder.name}{config.SUFFIX_FOLDER_TO_SAVE}")
