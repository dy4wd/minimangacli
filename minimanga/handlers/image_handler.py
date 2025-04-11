import sys

from pathlib import Path

from PIL import Image as Img, ImageFile

from .. import search


class ImageHandler:
    __MAX_SIZE_WEBP = 16383
    __WEBP = "webp"
    __JPEG = "jpeg"
    __SUFFIXES = (__JPEG, __WEBP, "jpg", "png")

    def __init__(self, source_folder: Path, result_folder: Path, quality: int):
        self.__source_folder = source_folder
        self.__result_folder = result_folder
        self.__quality = quality

    def optimize(self):
        images = search.find_all(self.__source_folder, self.__SUFFIXES)
        total_images = len(images)
        for index, image in enumerate(images):
            sys.stdout.write(f"\rProcessing image {index+1} out of {total_images}")
            save_as = self.__create_path_to_save_image(image)
            self.__convert_image(image, save_as)

    def __create_path_to_save_image(self, image: Path) -> Path:
        tail = image.relative_to(self.__source_folder)
        tail = self.__remove_duplicates_in_path(tail)
        save_as = tail.with_suffix(f".{self.__WEBP}")
        return Path(self.__result_folder, save_as)

    def __remove_duplicates_in_path(self, tail: Path) -> Path:
        parts = tail.parts
        if parts[0] in parts[1:]:
            return Path(*parts[1:])
        return Path(*parts)

    def __convert_image(self, image: Path, save_as: Path):
        with Img.open(image) as img:
            if max(img.size) > self.__MAX_SIZE_WEBP:
                save_as = self.__change_suffix(save_as, self.__JPEG)
                self.__save_image(img, save_as)
            else:
                self.__save_image(img, save_as)

    def __change_suffix(self, image: Path, suffix: str) -> Path:
        return image.with_suffix(suffix)

    def __save_image(self, imagefile: ImageFile.ImageFile, save_as: Path):
        save_as.parent.mkdir(parents=True, exist_ok=True)
        imagefile.save(save_as, format=save_as.suffix[1:], quality=self.__quality)
