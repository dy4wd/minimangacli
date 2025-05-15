import argparse

from pathlib import Path
from dataclasses import dataclass

from minimanga import config


@dataclass(frozen=True, slots=True)
class CLIArguments:
    path: Path
    format: str
    quality: int
    is_extract: bool
    is_squeeze: bool


def get_arguments() -> CLIArguments:
    cli_args = _create_command_line_argument_parser()
    return CLIArguments(
        path=cli_args.path.absolute(),
        format=cli_args.format,
        quality=cli_args.quality,
        is_extract=cli_args.is_extract,
        is_squeeze=cli_args.is_squeeze
    )


def _create_command_line_argument_parser() -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog='MiniManga')
    _add_arguments_to_parser(parser)
    return parser.parse_args()


def _add_arguments_to_parser(parser: argparse.ArgumentParser):
    parser.add_argument('path', type=Path)
    parser.add_argument(
        '-f',
        '--format',
        type=str,
        choices=['webp', 'avif', 'jpeg'],
        default='webp',
    )
    parser.add_argument('-q', '--quality', type=int, default=config.QUALITY)
    parser.add_argument('-e', '--extract', dest='is_extract', action='store_true')
    parser.add_argument('-s', '--squeeze', dest='is_squeeze', action='store_true')
