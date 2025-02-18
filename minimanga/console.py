import argparse

from pathlib import Path
from dataclasses import dataclass

import config


@dataclass(frozen=True, slots=True)
class CLIArguments:
    path: Path
    quality: int


def get_command_line_arguments() -> CLIArguments:
    cli_args = _create_command_line_argument_parser()
    return CLIArguments(path=cli_args.path, quality=cli_args.quality)


def _create_command_line_argument_parser() -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog="MiniManga")
    _add_arguments_to_parser(parser)
    return parser.parse_args()


def _add_arguments_to_parser(parser: argparse.ArgumentParser):
    parser.add_argument("path", type=Path)
    parser.add_argument("-q", "--quality", type=int, default=config.QUALITY)
