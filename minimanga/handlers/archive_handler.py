import sys

from enum import Enum
from pathlib import Path

from zipfile import ZipFile
from rarfile import RarFile

from .. import search, config


class ArchiveType(str, Enum):
    ZIP = "zip"
    RAR = "rar"
    CBZ = "cbz"
    CBR = "cbr"


class ArchiveHandler:
    def __init__(self, folder: Path):
        self._folder = folder
        self._dist: Path | None = None
        self._suffixes = ("zip", "cbz", "rar", "cbr")
        self._archives = search.find_all(self._folder, self._suffixes)

    def unpack(self):
        for archive in self._archives:
            sys.stdout.write(f"Unpacking: {archive.name}\n")
            suffix = archive.suffix[1:]
            self._dist = self._set_dist_folder(archive)
            match suffix:
                case ArchiveType.ZIP | ArchiveType.CBZ:
                    self._extract_zip(archive)
                case ArchiveType.RAR | ArchiveType.CBR:
                    self._extract_rar(archive)
                case _:
                    sys.stderr.write(f"\"{suffix}\" is an unknown archive type.\n")
                    exit(1)

    def _set_dist_folder(self, archive: Path) -> Path:
        return Path(archive.parent, archive.stem)

    def _extract_zip(self, archive: Path):
        with ZipFile(archive) as zipfile_:
            zipfile_.extractall(path=self._dist)
            self._in_trash(str(self._dist))

    def _extract_rar(self, archive: Path):
        with RarFile(archive) as rarfile_:
            rarfile_.extractall(path=self._dist)
            self._in_trash(str(self._dist))

    def _in_trash(self, path: str):
        with open(config.TRASH_FILE, "a") as file:
            file.write(f"{path}\n")
