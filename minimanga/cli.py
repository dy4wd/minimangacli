import argparse

from pathlib import Path
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class CLIArguments:
    path: Path
    quality: int
    is_extraction: bool

QUALITY = 75

def get_arguments() -> CLIArguments:
    cli_args = _create_command_line_argument_parser()
    return CLIArguments(
        path=cli_args.path.absolute(),
        quality=cli_args.quality,
        is_extraction=cli_args.is_extraction,
    )


def _create_command_line_argument_parser() -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog="MiniManga")
    _add_arguments_to_parser(parser)
    return parser.parse_args()


def _add_arguments_to_parser(parser: argparse.ArgumentParser):
    parser.add_argument("path", type=Path)
    parser.add_argument("-q", "--quality", type=int, default=QUALITY)
    parser.add_argument("-x", dest="is_extraction", action="store_true")
