import sys
import shutil

from enum import Enum
from pathlib import Path
from collections.abc import Sequence
from zipfile import ZipFile

from rarfile import RarFile

from minimanga import config, search, images
from minimanga.exceptions import UnknownArchiveType
from minimanga.state import State


class Archives(str, Enum):
    ZIP = 'zip'
    RAR = 'rar'
    CBZ = 'cbz'
    CBR = 'cbr'


SUFFIXES = [f'.{arch.value}' for arch in Archives]


def reduce(state: State):
    source_folder = state.source
    state.source = result_folder = Path(
        state.source.parent,
        f'{state.source.name}{config.SUFFIX_UNPACK_FOLDER}',
    )
    archives = search.find_all(source_folder, SUFFIXES)

    try:
        _run(archives, result_folder)
    except UnknownArchiveType:
        sys.stderr.write('Unknown archive type.\n')
        exit(1)

    images.reduce(state)
    _clear(result_folder)


def _run(archives: Sequence[Path], folder: Path):
    total_archives = len(archives)
    for index, archive in enumerate(archives):
        sys.stdout.write(f'Unpacking archive: {index+1} of {total_archives}\r')
        path = Path(folder, archive.parent.name, archive.stem)
        _unpack(archive, path)
    sys.stdout.write('\n')


def _unpack(archive: Path, path: Path):
    match archive.suffix[1:]:
        case Archives.ZIP | Archives.CBZ:
            _extract_zip(archive, path=path)
        case Archives.RAR | Archives.CBR:
            _extract_rar(archive, path=path)
        case _:
            raise UnknownArchiveType


def _extract_zip(file: Path, path: Path):
    with ZipFile(file) as zfile:
        zfile.extractall(path=path)


def _extract_rar(file: Path, path: Path):
    with RarFile(file) as rfile:
        rfile.extractall(path=path)


def _clear(folder: Path):
    shutil.rmtree(folder)
