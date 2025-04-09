import sys

from . import cli
from .handlers.archive_handler import ArchiveHandler
from .handlers.image_handler import ImageHandler


def main():
    cli_args = cli.get_arguments()

    if not cli_args.path.is_dir():
        sys.stderr.write("The specified path is not a folder.\n")
        sys.exit(1)
    else:
        folder = cli_args.path

    if cli_args.is_extraction:
        archives = ArchiveHandler(folder)
        archives.unpack()
        ImageHandler(folder, cli_args.quality).optimize()
        archives.clean()
    else:
        ImageHandler(folder, cli_args.quality).optimize()
    sys.stdout.write("\nDone\n")


if __name__ == "__main__":
    main()
