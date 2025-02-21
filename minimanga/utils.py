from pathlib import Path
from typing import Generator, Sequence

import config
from exceptions import ImagesNotFound, SpecifiedPathNotFolder


Files = Generator[Path, None, None]
Images = Sequence[Path]


def path_handler(path: Path) -> Path:
    """Checks whether the specified path is a folder."""
    if not path.is_dir():
        raise SpecifiedPathNotFolder
    return path.absolute()


def get_all_files(folder: Path) -> Files:
    """Collects all files in the specified folder."""
    return folder.glob("**/*")


def sort_images(files: Files) -> Images:
    """Selects images from all found files."""
    print("Image search...")
    images = []
    for file in files:
        if file.suffix in config.IMAGES_SUFFIXES:
            images.append(file)
    if len(images) == 0:
        raise ImagesNotFound
    return images
