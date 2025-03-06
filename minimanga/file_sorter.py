import sys

from pathlib import Path
from typing import Generator, Sequence

from . import config
from .exceptions import ImagesNotFound


Files = Generator[Path, None, None]
Images = Sequence[Path]


def find_images(files: Files) -> Images:
    images = []
    sys.stdout.write("Image search...")
    for file in files:
        if file.suffix in config.IMAGES_SUFFIXES:
            images.append(file)
    if len(images) == 0:
        raise ImagesNotFound
    sys.stdout.write("\rImage search... Done.\n")
    return images
