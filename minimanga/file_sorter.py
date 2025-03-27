import sys

from pathlib import Path
from typing import Iterator, Sequence

from . import config
from .exceptions import ImagesNotFound


Files = Iterator[Path]
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
