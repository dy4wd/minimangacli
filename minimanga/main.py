import sys

from . import cli, path_handler, image_parser
from .cli import get_arguments
from .exceptions import SpecifiedPathNotFolder, ImagesNotFound


def main():
    cli = get_arguments()

    try:
        path_handler.is_dir(cli.path)
    except SpecifiedPathNotFolder:
        sys.stderr.write("The specified path is not a folder.\n")
        sys.exit(1)

    try:
        img_locations = image_parser.get_all_paths_to_images(cli.path.rglob("*"))
    except ImagesNotFound:
        sys.stderr.write("Images not found.\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
