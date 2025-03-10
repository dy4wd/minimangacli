import sys

from . import cli, path_handler, path_collector, image_converter
from .exceptions import SpecifiedPathNotFolder, ImagesNotFound


def main():
    cli_args = cli.get_arguments()

    try:
        path_handler.is_dir(cli_args.path)
    except SpecifiedPathNotFolder:
        sys.stderr.write("The specified path is not a folder.\n")
        sys.exit(1)

    try:
        images = path_collector.get_all_paths_to_images(cli_args.path.rglob("*"))
    except ImagesNotFound:
        sys.stderr.write("Images not found.\n")
        sys.exit(1)

    folder_to_save = path_handler.generate_path_to_save(cli_args.path)

    image_converter.convert(
        target_path=cli_args.path,
        path_to_save=folder_to_save,
        images=images,
        quality=cli_args.quality,
    )


if __name__ == "__main__":
    main()
