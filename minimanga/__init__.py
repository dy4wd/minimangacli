import sys

from minimanga import cli, config
from minimanga.archive_handler import ArchiveHandler
from minimanga.image_handler import ImageHandler


def main():
    cli_args = cli.get_arguments()

    if not cli_args.path.is_dir():
        sys.stderr.write('The specified path is not a folder.\n')
        sys.exit(1)
    else:
        source_folder = cli_args.path

    result_folder = source_folder.with_name(
        f'{source_folder.name}{config.SUFFIX_RESULT_FOLDER}'
    )

    if cli_args.is_archives:
        ArchiveHandler(source_folder, result_folder, cli_args.format_, cli_args.quality).start()
    else:
        ImageHandler(source_folder, result_folder, cli_args.format_, cli_args.quality).start()

    sys.stdout.write('\nDone\n')
