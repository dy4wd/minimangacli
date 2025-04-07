from enum import Enum
import sys

from pathlib import Path
from zipfile import ZipFile

from rarfile import RarFile

from .. import sorter
from ..exceptions import TargetNotFound


class ArchiveType(str, Enum):
    ZIP = "zip"
    RAR = "rar"
    CBZ = "cbz"
    CBR = "cbr"


class ArchiveHandler():
    def __init__(self, folder: Path):
        self._folder = folder
        self._suffixes = ("zip", "cbz", "rar", "cbr")
        self._archives = self._find_all()

    def _find_all(self) -> sorter.Targets:
        sys.stdout.write(f"Archive search...\n")
        try:
            archives = sorter.find_all(self._folder.rglob("*"), self._suffixes)
        except TargetNotFound:
            sys.stderr.write("Archives not found.\n")
            exit(1)
        sys.stdout.write(f"Done\n")
        return archives

    def unpack(self):
        for archive in self._archives:
            sys.stdout.write(f"Unpacking: {archive.name}...\n")
            match archive.suffix[1:]:
                case ArchiveType.ZIP | ArchiveType.CBZ:
                    self._extract_zip(archive)
                case ArchiveType.RAR | ArchiveType.CBR:
                    self._extract_rar(archive)
                case _:
                    break

    def _extract_zip(self, archive:Path):
        with ZipFile(archive) as zipfile_:
            dist = self._get_dist_folder(archive, zipfile_.namelist()[-1].strip("/"))
            zipfile_.extractall(path=dist)

    def _extract_rar(self, archive:Path):
        with RarFile(archive) as rarfile_:
            dist = self._get_dist_folder(archive, rarfile_.namelist()[-1].strip("/"))
            rarfile_.extractall(path=dist)

    def _get_dist_folder(self, archive:Path, inner_folder:str) -> Path:
        if archive.stem == inner_folder:
            return archive.parent
        return Path(archive.parent, archive.stem)
