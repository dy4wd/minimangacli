from pathlib import Path
from dataclasses import dataclass
from typing import Callable

from PIL import Image

from . import config
from .image_parser import ImgLocations


@dataclass(frozen=True, slots=True)
class Folders:
    target: Path
    to_save: Path


@dataclass(frozen=True, slots=True)
class ArgsFormatter:
    folders: Folders
    images: ImgLocations
    quality: int


def format_images(args: ArgsFormatter):
    args.folders.to_save.mkdir(exist_ok=True)
    for index, image in enumerate(args.images):
        img = Image.open(image)
        if max(img.size) > config.MAX_SIZE_WEBP:
            save_as = Path(
                args.folders.to_save,
                _change_suffix(
                    image.relative_to(args.folders.target), config.JPEG_SUFFIX
                ),
            )
        else:
            save_as = Path(
                args.folders.to_save,
                _change_suffix(
                    image.relative_to(args.folders.target), config.WEBP_SUFFIX
                ),
            )
        save_as.parent.mkdir(parents=True, exist_ok=True)
        img.save(save_as, quality=args.quality)
        img.close()
        print(index + 1, len(args.images))


_change_suffix: Callable[[Path, str], Path] = lambda image, suffix: image.with_suffix(
    suffix
)
