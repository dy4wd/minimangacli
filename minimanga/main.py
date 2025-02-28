import sys

from . import utils
from .cli import get_arguments
from .exceptions import SpecifiedPathNotFolder, ImagesNotFound


def main():
    cli = get_arguments()

    try:
        target_folder = utils.path_handler(cli.path)
    except SpecifiedPathNotFolder:
        sys.stderr.write("The specified path is not a folder.\n")
        sys.exit(1)

    try:
        images = utils.get_images(target_folder)
    except ImagesNotFound:
        sys.stderr.write("Images not found.\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
