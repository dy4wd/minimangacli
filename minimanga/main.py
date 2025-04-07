import sys

from . import cli
from .handlers.archive import ArchiveHandler
from .handlers.image import ImageHandler


def main():
    cli_args = cli.get_arguments()

    if not cli_args.path.is_dir():
        sys.stderr.write("The specified path is not a folder.\n")
        sys.exit(1)
    else:
        folder = cli_args.path

    if cli_args.is_extraction:
        ArchiveHandler(folder).unpack()
        ImageHandler(folder, cli_args.quality).optimize()
    else:
        ImageHandler(folder, cli_args.quality).optimize()


if __name__ == "__main__":
    main()
