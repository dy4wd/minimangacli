import sys
import shutil

from pathlib import Path

from . import config


def clean():
    sys.stdout.write("\nDeleting folders after unpacking.")
    with open(config.TRASH_FILE) as file:
        trash = file.read().strip()

    for item in trash.split("\n"):
        shutil.rmtree(Path(item))
    Path(config.TRASH_FILE).unlink()
