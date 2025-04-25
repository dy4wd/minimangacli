import sys

from pathlib import Path

from PIL import Image as Img, ImageFile

from minimanga import search


MAX_SIZE_WEBP = 16383


class ImageHandler:
    def __init__(
        self,
        source_folder: Path,
        result_folder: Path,
        format_: str,
        quality: int,
    ):
        self._source_folder = source_folder
        self._result_folder = result_folder
        self._format = format_
        self._quality = quality

    def start(self):
        images = self._get_all_images()
        total_images = len(images)
        for index, image in enumerate(images):
            sys.stdout.write(
                f'\rProcessing image {index+1} out of {total_images}'
            )
            save_as = self._create_path_to_save_image(image)
            self._convert_image(image, save_as)

    def _get_all_images(self) -> list[Path]:
        sys.stdout.write('Image search...\n')
        suffixes = '.webp .jpeg .jpg .png .avif'.split()
        return search.find_all(self._source_folder, suffixes)

    def _create_path_to_save_image(self, image: Path) -> Path:
        tail = image.relative_to(self._source_folder)
        save_as = Path(*list(dict.fromkeys(tail.parts).keys())).with_suffix(
            f'.{self._format}'
        )
        return Path(self._result_folder, save_as)

    def _convert_image(self, image: Path, save_as: Path):
        with Img.open(image) as img:
            if self._format == 'webp' and max(img.size) > MAX_SIZE_WEBP:
                self._save_image(img, save_as.with_suffix('.jpeg'))
            else:
                self._save_image(img, save_as)

    def _save_image(self, imagefile: ImageFile.ImageFile, save_as: Path):
        save_as.parent.mkdir(parents=True, exist_ok=True)
        imagefile.save(
            save_as, format=self._format, quality=self._quality
        )
