from pathlib import Path
from typing import Callable

from . import config


def create_path_to_dist_folder(target_folder: Path) -> Path:
    return target_folder.with_name(f"{target_folder.name}{config.SUFFIX_DIST_FOLDER}")


def create_path_to_save_image(target_folder: Path, dist: Path, image: Path) -> Path:
    tail = image.relative_to(target_folder)
    save_as = tail.with_suffix(config.DEFAULT_IMAGE_SUFFIX)
    return Path(dist, save_as)


change_suffix: Callable[[Path, str], Path] = lambda image, suffix: image.with_suffix(
    suffix
)
