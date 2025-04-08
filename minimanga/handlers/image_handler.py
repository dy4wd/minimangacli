import sys

from pathlib import Path

from PIL import Image as Img, ImageFile

from .. import config, search


class ImageHandler:
    def __init__(self, folder: Path, quality: int):
        self._folder = folder
        self._quality = quality
        self._suffixes = ("jpeg", "jpg", "png", "webp")
        self._images = search.find_all(self._folder, self._suffixes)
        self._dist = self._set_dist_folder()

    def optimize(self):
        for index, image in enumerate(self._images):
            sys.stdout.write(f"\rProcessing image {index+1} out of {len(self._images)}")
            save_as = self._create_path_to_save_image(image)
            self._convert_image(image, save_as)
        sys.stdout.write(f"\nDone.\n")

    def _set_dist_folder(self) -> Path:
        return self._folder.with_name(f"{self._folder.name}{config.SUFFIX_DIST_FOLDER}")

    def _create_path_to_save_image(self, image: Path) -> Path:
        tail = image.relative_to(self._folder)
        tail = self._remove_duplicates(tail)
        save_as = tail.with_suffix(config.DEFAULT_IMAGE_SUFFIX)
        return Path(self._dist, save_as)
    
    def _remove_duplicates(self, tail: Path) -> Path:
        parts = tail.parts
        if parts[0] in parts[1:]:
            return Path(*parts[1:])
        return Path(*parts)

    def _convert_image(self, image: Path, save_as: Path):
        with Img.open(image) as img:
            if max(img.size) > config.MAX_SIZE_WEBP:
                alt_save_as = self._change_suffix(save_as, config.ALT_IMAGE_SUFFIX)
                self._save_image(img, alt_save_as)
            else:
                self._save_image(img, save_as)

    def _change_suffix(self, image: Path, suffix: str) -> Path:
        return image.with_suffix(suffix)

    def _save_image(self, imagefile: ImageFile.ImageFile, save_as: Path):
        save_as.parent.mkdir(parents=True, exist_ok=True)
        imagefile.save(save_as, format=save_as.suffix[1:], quality=self._quality)
