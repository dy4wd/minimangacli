import shutil

from pathlib import Path

from . import config


def clean():
    with open(config.TRASH_FILE) as file:
        trash = file.read().strip()

    for item in trash.split("\n"):
        shutil.rmtree(Path(item))
    Path(config.TRASH_FILE).unlink()


if __name__ == "__main__":
    clean()
