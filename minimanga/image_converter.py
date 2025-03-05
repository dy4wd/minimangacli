import sys

from pathlib import Path
from typing import Callable

from PIL import Image

from . import config
from .path_collector import ImgLocations


def convert(target_path: Path, path_to_save: Path, images: ImgLocations, quality: int):
    path_to_save.mkdir(exist_ok=True)
    for index, image in enumerate(images):
        sys.stdout.write(f"\rConvert image {index+1} of {len(images)}")
        img = Image.open(image)
        if max(img.size) > config.MAX_SIZE_WEBP:
            save_as = Path(
                path_to_save,
                _change_suffix(image.relative_to(target_path), config.JPEG_SUFFIX),
            )
        else:
            save_as = Path(
                path_to_save,
                _change_suffix(image.relative_to(target_path), config.WEBP_SUFFIX),
            )
        save_as.parent.mkdir(parents=True, exist_ok=True)
        img.save(save_as, quality=quality)
        img.close()
    sys.stdout.write(f"\nDone.\n")


_change_suffix: Callable[[Path, str], Path] = lambda image, suffix: image.with_suffix(
    suffix
)
