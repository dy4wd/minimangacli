from pathlib import Path
from dataclasses import dataclass
from typing import Callable

from . import config
from .utils import Images


@dataclass(frozen=True, slots=True)
class DataForFormatter:
    target_images: Images
    manga_name: str
    image_quality: int


def format_images(data: DataForFormatter):
    pass


def _generate_path_to_save(manga_name: str, image: Path) -> Path:
    image = _change_suffix(image)
    root_dir, tail = str(image).split(manga_name)
    new_manga_name = f"{manga_name}{config.SUFFIX_FOLDER_TO_SAVE}"
    path_to_save = Path(root_dir, new_manga_name, tail[1:])
    return path_to_save


_change_suffix: Callable[[Path], Path] = lambda image: image.with_suffix(
    config.WEBP_SUFFIX
)
