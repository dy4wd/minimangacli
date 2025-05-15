import sys

from minimanga import cli, config, archives, images
from minimanga.state import State


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

    state = State(
        source=source_folder,
        result=result_folder,
        format=cli_args.format,
        quality=cli_args.quality,
    )

    if cli_args.is_archives:
        archives.reduce(state)
    else:
        images.reduce(state)

    sys.stdout.write('\nDone\n')
