import sys
import shutil

from enum import Enum
from pathlib import Path

from zipfile import ZipFile
from rarfile import RarFile

from .. import search


class ArchiveType(str, Enum):
    ZIP = "zip"
    RAR = "rar"
    CBZ = "cbz"
    CBR = "cbr"


class ArchiveHandler:
    def __init__(self, folder: Path):
        self._folder = folder
        self._suffixes = ("zip", "cbz", "rar", "cbr")
        self._trash = []

    def unpack(self):
        archives = search.find_all(self._folder, self._suffixes)
        for archive in archives:
            sys.stdout.write(f"Unpacking: {archive.name}\n")
            suffix = archive.suffix[1:]
            dist = self._set_dist_folder(archive)
            match suffix:
                case ArchiveType.ZIP | ArchiveType.CBZ:
                    self._extract_zip(archive, dist)
                case ArchiveType.RAR | ArchiveType.CBR:
                    self._extract_rar(archive, dist)
                case _:
                    sys.stderr.write(f'"{suffix}" is an unknown archive type.\n')
                    exit(1)
        self._clean()

    def _set_dist_folder(self, archive: Path) -> Path:
        return Path(archive.parent, archive.stem)

    def _extract_zip(self, archive: Path, dist: Path):
        with ZipFile(archive) as zipfile_:
            zipfile_.extractall(path=dist)
            self._trash.append(dist)

    def _extract_rar(self, archive: Path, dist: Path):
        with RarFile(archive) as rarfile_:
            rarfile_.extractall(path=dist)
            self._trash.append(dist)

    def _clean(self):
        sys.stdout.write("\nDeleting folders after unpacking.")
        for item in self._trash:
            shutil.rmtree(item)
