import sys

from . import cli, path_handler, image_parser, image_formatter
from .exceptions import SpecifiedPathNotFolder, ImagesNotFound


def main():
    cli_args = cli.get_arguments()

    try:
        path_handler.is_dir(cli_args.path)
    except SpecifiedPathNotFolder:
        sys.stderr.write("The specified path is not a folder.\n")
        sys.exit(1)

    try:
        images = image_parser.get_all_paths_to_images(cli_args.path.rglob("*"))
    except ImagesNotFound:
        sys.stderr.write("Images not found.\n")
        sys.exit(1)

    folder_to_save = path_handler.generate_path_to_save(cli_args.path)

    image_formatter.format_images(
        image_formatter.ArgsFormatter(
            image_formatter.Folders(target=cli_args.path, to_save=folder_to_save),
            images=images,
            quality=cli_args.quality,
        )
    )


if __name__ == "__main__":
    main()
