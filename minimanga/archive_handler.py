import sys
import shutil

from pathlib import Path
from collections.abc import Sequence

from minimanga import archives, config
from minimanga.handler import Handler, HandlerArgs
from minimanga.exceptions import UnknownArchiveType
from minimanga.image_handler import ImageHandler


class ArchiveHandler(Handler):
    __suffixes__ = ['.zip', '.cbz', '.rar', '.cbr']

    def __init__(self, *args):
        super().__init__(*args)
        self._unpacking_folder = Path(
            self._source_folder.parent,
            f'{self._source_folder.name}{config.SUFFIX_UNPACK_FOLDER}',
        )

    def start(self):
        archives_ = self._get_all_files()
        try:
            self._unpack(archives_)
        except UnknownArchiveType:
            sys.stderr.write('Unknown archive type.\n')
            exit(1)
        ImageHandler(
            HandlerArgs(
                source_folder=self._unpacking_folder,
                result_folder=self._result_folder,
                format_=self._format,
                quality=self._quality,
            )
        ).start()
        self._clear()

    def _unpack(self, archives_: Sequence[Path]):
        total_archives = len(archives_)
        for index, archive in enumerate(archives_):
            sys.stdout.write(
                f'Unpacking archive: {index+1} of {total_archives}\r'
            )
            path = Path(
                self._unpacking_folder, archive.parent.name, archive.stem
            )
            archives.unpack(archive, path)
        sys.stdout.write('\n')

    def _clear(self):
        shutil.rmtree(self._unpacking_folder)
