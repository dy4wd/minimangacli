from enum import Enum
from pathlib import Path

from zipfile import ZipFile
from rarfile import RarFile

from minimanga.exceptions import UnknownArchiveType


class ArchiveType(str, Enum):
    ZIP = 'zip'
    RAR = 'rar'
    CBZ = 'cbz'
    CBR = 'cbr'


def unpack(archive: Path, path: Path):
    match archive.suffix[1:]:
        case ArchiveType.ZIP | ArchiveType.CBZ:
            _extract_zip(archive, path=path)
        case ArchiveType.RAR | ArchiveType.CBR:
            _extract_rar(archive, path=path)
        case _:
            raise UnknownArchiveType


def _extract_zip(file: Path, path: Path):
    with ZipFile(file) as zfile:
        zfile.extractall(path=path)


def _extract_rar(file: Path, path: Path):
    with RarFile(file) as rfile:
        rfile.extractall(path=path)
