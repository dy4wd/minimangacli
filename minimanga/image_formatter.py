from pathlib import Path
from dataclasses import dataclass

from utils import Images


@dataclass(frozen=True, slots=True)
class DataForFormatter:
    images: Images
    to_save: Path
    image_quality: int


def format_images(data: DataForFormatter):
    pass
