import sys
import shutil

from enum import Enum
from typing import List
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
    __SUFFIXES = ("zip", "cbz", "rar", "cbr")

    def __init__(self, folder: Path):
        self.__folder = folder
        self.__trash: List[Path] = []

    def unpack(self):
        archives = search.find_all(self.__folder, self.__SUFFIXES)
        for archive in archives:
            sys.stdout.write(f"Unpacking: {archive.name}\n")
            suffix = archive.suffix[1:]
            dist = self.__set_dist_folder(archive)
            match suffix:
                case ArchiveType.ZIP | ArchiveType.CBZ:
                    self.__extract_zip(archive, dist)
                case ArchiveType.RAR | ArchiveType.CBR:
                    self.__extract_rar(archive, dist)
                case _:
                    sys.stderr.write(f'"{suffix}" is an unknown archive type.\n')
                    exit(1)

    def __set_dist_folder(self, archive: Path) -> Path:
        return Path(archive.parent, archive.stem)

    def __extract_zip(self, archive: Path, dist: Path):
        with ZipFile(archive) as zipfile_:
            zipfile_.extractall(path=dist)
            self.__trash.append(dist)

    def __extract_rar(self, archive: Path, dist: Path):
        with RarFile(archive) as rarfile_:
            rarfile_.extractall(path=dist)
            self.__trash.append(dist)

    def clean(self):
        sys.stdout.write("\nDeleting folders after unpacking.")
        for item in self.__trash:
            shutil.rmtree(item)
