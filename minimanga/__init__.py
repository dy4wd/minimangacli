import sys

from minimanga import cli, config
from minimanga.handler import HandlerArgs
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

    handler_args = HandlerArgs(
        source_folder=source_folder,
        result_folder=result_folder,
        format_=cli_args.format_,
        quality=cli_args.quality,
    )

    if cli_args.is_archives:
        ArchiveHandler(handler_args).start()
    else:
        ImageHandler(handler_args).start()

    sys.stdout.write('\nDone\n')
