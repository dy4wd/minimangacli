from enum import Enum
import sys

from pathlib import Path
from zipfile import ZipFile

from rarfile import RarFile

from . import sorter


class ArchiveType(str, Enum):
    ZIP = "zip"
    RAR = "rar"
    CBZ = "cbz"
    CBR = "cbr"


ARCHIVES_SUFFIXES = ("zip", "cbz", "rar", "cbr")


def unpack(folder: Path):
    archives = sorter.find_all(folder.rglob("*"), ARCHIVES_SUFFIXES, "Archives")

    for archive in archives:
        sys.stdout.write(f"Unpacking: {archive.name}...\n")
        match archive.suffix[1:]:
            case ArchiveType.ZIP | ArchiveType.CBZ:
                with ZipFile(archive) as zipfile_:
                    if archive.stem == zipfile_.namelist()[-1].strip("/"):
                        dist = archive.parent
                    else:
                        dist = Path(archive.parent, archive.stem)
                    zipfile_.extractall(path=dist)
            case ArchiveType.RAR | ArchiveType.CBR:
                with RarFile(archive) as rarfile_:
                    if archive.stem == rarfile_.namelist()[-1].strip("/"):
                        dist = archive.parent
                    else:
                        dist = Path(archive.parent, archive.stem)
                    rarfile_.extractall(path=dist)
            case _:
                break
