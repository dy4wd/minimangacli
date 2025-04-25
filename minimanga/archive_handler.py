import sys

from enum import Enum
from pathlib import Path
from collections.abc import Sequence

from minimanga import search, archives, config
from minimanga.exceptions import UnknownArchiveType
from minimanga.image_handler import ImageHandler


class ArchiveType(str, Enum):
    ZIP = 'zip'
    RAR = 'rar'
    CBZ = 'cbz'
    CBR = 'cbr'


class ArchiveHandler:
    def __init__(self, source_folder: Path, result_folder: Path, format_:str, quality: int):
        self._source_folder = source_folder
        self._result_folder = result_folder
        self._format = format_
        self._quality = quality
        self._unpacking_folder = Path(
            self._source_folder.parent,
            f'{self._source_folder.name}{config.SUFFIX_UNPACK_FOLDER}',
        )

    def start(self):
        archives_ = self._get_all_archives()
        try:
            self._unpack(archives_)
        except UnknownArchiveType:
            sys.stderr.write('Unknown archive type.\n')
            exit(1)
        ImageHandler(
            self._unpacking_folder, self._result_folder, self._format, self._quality
        ).start()

    def _get_all_archives(self) -> list[Path]:
        sys.stdout.write('Archive search...\n')
        suffixes = '.zip .cbz .rar .cbr'.split()
        return search.find_all(self._source_folder, suffixes)

    def _unpack(self, archives_: Sequence[Path]):
        total_archives = len(archives_)
        for index, archive in enumerate(archives_):
            sys.stdout.write(
                f'Unpacking archive: {index+1} of {total_archives}\r'
            )
            path = Path(
                self._unpacking_folder, archive.parent.name, archive.stem
            )
            match archive.suffix[1:]:
                case ArchiveType.ZIP | ArchiveType.CBZ:
                    archives.extract_zip(archive, path=path)
                case ArchiveType.RAR | ArchiveType.CBR:
                    archives.extract_rar(archive, path=path)
                case _:
                    raise UnknownArchiveType
        sys.stdout.write('\n')
