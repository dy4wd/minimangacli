import sys

from pathlib import Path

from PIL import Image as Img, ImageFile

from . import config, sorter, path_handler

IMAGES_SUFFIXES = ("jpeg", "jpg", "png", "webp")


def convert(folder: Path, quality: int):
    images = sorter.find_all(folder.rglob("*"), IMAGES_SUFFIXES, "Images")

    for index, image in enumerate(images):
        sys.stdout.write(f"\rConvert image {index+1} of {len(images)}")
        dist_folder = path_handler.create_path_to_dist_folder(folder)
        save_as = path_handler.create_path_to_save_image(folder, dist_folder, image)
        _convert_image(image, quality, save_as)
    sys.stdout.write(f"\nDone.\n")


def _convert_image(image: Path, quality: int, save_as: Path):
    with Img.open(image) as img:
        if max(img.size) > config.MAX_SIZE_WEBP:
            alt_save_as = path_handler.change_suffix(save_as, config.ALT_IMAGE_SUFFIX)
            _save_image(img, quality, alt_save_as)
        else:
            _save_image(img, quality, save_as)


def _save_image(imagefile: ImageFile.ImageFile, quality: int, save_as: Path):
    save_as.parent.mkdir(parents=True, exist_ok=True)
    imagefile.save(save_as, format=save_as.suffix[1:], quality=quality)
