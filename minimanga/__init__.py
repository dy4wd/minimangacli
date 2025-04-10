import sys

from . import cli
from .handlers.archive_handler import ArchiveHandler
from .handlers.image_handler import ImageHandler


SUFFIX_RESULT_FOLDER = "_mini"

def main():
    cli_args = cli.get_arguments()

    if not cli_args.path.is_dir():
        sys.stderr.write("The specified path is not a folder.\n")
        sys.exit(1)
    else:
        source_folder = cli_args.path

    result_folder = source_folder.with_name(f"{source_folder.name}{SUFFIX_RESULT_FOLDER}")

    if cli_args.is_extraction:
        archives = ArchiveHandler(source_folder)
        archives.unpack()
        ImageHandler(source_folder, result_folder, cli_args.quality).optimize()
        archives.clean()
    else:
        ImageHandler(source_folder, result_folder, cli_args.quality).optimize()

    sys.stdout.write("\nDone\n")
