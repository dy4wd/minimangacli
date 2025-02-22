from pathlib import Path
from typing import Callable, Generator, Sequence

import config
from exceptions import ImagesNotFound, SpecifiedPathNotFolder


Files = Generator[Path, None, None]
Images = Sequence[Path]


def path_handler(path: Path) -> Path:
    """Checks whether the specified path is a folder."""
    if not path.is_dir():
        raise SpecifiedPathNotFolder
    return path.absolute()


def get_images(folder: Path) -> Images:
    """Selects images from all found files."""
    files = _get_files(folder)
    images = []
    print("Image search...")
    for file in files:
        if file.suffix in config.IMAGES_SUFFIXES:
            images.append(file)
    if len(images) == 0:
        raise ImagesNotFound
    return images


_get_files: Callable[[Path], Files] = lambda folder: folder.rglob("*")


def create_folder_to_save(target: Path) -> Path:
    path_folder_to_save = target.with_name(
        f"{target.name}{config.SUFFIX_FOLDER_TO_SAVE}"
    )
    if not path_folder_to_save.exists():
        path_folder_to_save.mkdir()
    return path_folder_to_save
