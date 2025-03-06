import sys

from . import cli, path_handler, file_sorter, image_converter
from .exceptions import SpecifiedPathNotFolder, ImagesNotFound


def main():
    cli_args = cli.get_arguments()

    try:
        path_handler.is_dir(cli_args.path)
    except SpecifiedPathNotFolder:
        sys.stderr.write("The specified path is not a folder.\n")
        sys.exit(1)

    try:
        images = file_sorter.find_images(cli_args.path.rglob("*"))
    except ImagesNotFound:
        sys.stderr.write("Images not found.\n")
        sys.exit(1)

    image_converter.run(
        target_folder=cli_args.path,
        images=images,
        quality=cli_args.quality,
    )


if __name__ == "__main__":
    main()
