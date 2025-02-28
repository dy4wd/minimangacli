from pathlib import Path
from typing import Callable, Generator, Sequence

from . import config
from .exceptions import ImagesNotFound


Files = Generator[Path, None, None]
ImgLocations = Sequence[Path]


def get_all_paths_to_images(files: Files) -> ImgLocations:
    img_locations = []
    print("Image search...")
    for file in files:
        if file.suffix in config.IMAGES_SUFFIXES:
            img_locations.append(file)
    if len(img_locations) == 0:
        raise ImagesNotFound
    return img_locations
