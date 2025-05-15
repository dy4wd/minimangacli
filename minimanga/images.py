import sys

from pathlib import Path

from PIL import Image, ImageFile

from minimanga import search
from minimanga.state import State

MAX_SIZE_WEBP = 16383
SUFFIXES = ['.webp', '.jpeg', '.jpg', '.png', '.avif']


def reduce(state: State):
    images = search.find_all(state.source, SUFFIXES)
    total_images = len(images)
    for index, image in enumerate(images):
        sys.stdout.write(f'\rProcessing image {index+1} out of {total_images}')
        save_as = _generate_path_to_save(
            state.source, state.result, image, state.format
        )
        _convert(image, save_as, state.format, state.quality)


def _generate_path_to_save(
    source_folder: Path, result_folder: Path, image: Path, format: str
) -> Path:
    tail = image.relative_to(source_folder)
    tail = Path(*list(dict.fromkeys(tail.parts).keys())).with_suffix(
        f'.{format}'
    )
    return Path(result_folder, tail)


def _convert(image: Path, save_as: Path, format: str, quality: int):
    with Image.open(image) as img:
        if format == 'webp' and max(img.size) > MAX_SIZE_WEBP:
            _save(img, save_as.with_suffix('.jpeg'), format, quality)
        else:
            _save(img, save_as, format, quality)


def _save(
    imagefile: ImageFile.ImageFile, save_as: Path, format: str, quality: int
):
    save_as.parent.mkdir(parents=True, exist_ok=True)
    imagefile.save(save_as, format=format, quality=quality)
