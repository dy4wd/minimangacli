import sys

from . import cli, archives_handler, images_handler


def main():
    cli_args = cli.get_arguments()

    if not cli_args.path.is_dir():
        sys.stderr.write("The specified path is not a folder.\n")
        sys.exit(1)
    else:
        folder = cli_args.path

    if cli_args.is_extraction:
        archives_handler.unpack(folder)
        images_handler.convert(folder, cli_args.quality)
    else:
        images_handler.convert(folder, cli_args.quality)


if __name__ == "__main__":
    main()
