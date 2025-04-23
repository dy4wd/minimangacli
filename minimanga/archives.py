from pathlib import Path

from zipfile import ZipFile
from rarfile import RarFile


def extract_zip(archive: Path, path: Path):
    with ZipFile(archive) as zfile:
        zfile.extractall(path=path)


def extract_rar(archive: Path, path: Path):
    with RarFile(archive) as rfile:
        rfile.extractall(path=path)
