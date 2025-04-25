import argparse

from pathlib import Path
from dataclasses import dataclass

from minimanga import config


@dataclass(frozen=True, slots=True)
class CLIArguments:
    path: Path
    format_: str
    quality: int
    is_archives: bool


def get_arguments() -> CLIArguments:
    cli_args = _create_command_line_argument_parser()
    return CLIArguments(
        path=cli_args.path.absolute(),
        format_=cli_args.format,
        quality=cli_args.quality,
        is_archives=cli_args.is_archives,
    )


def _create_command_line_argument_parser() -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog='MiniManga')
    _add_arguments_to_parser(parser)
    return parser.parse_args()


def _add_arguments_to_parser(parser: argparse.ArgumentParser):
    parser.add_argument('path', type=Path)
    parser.add_argument('-f', '--format', type=str, choices=['webp', 'avif', 'jpeg'], default='webp')
    parser.add_argument('-q', '--quality', type=int, default=config.QUALITY)
    parser.add_argument('-a', dest='is_archives', action='store_true')
