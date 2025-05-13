from dataclasses import dataclass
from pathlib import Path

from minimanga import search


@dataclass(slots=True, frozen=True)
class HandlerArgs:
    source_folder: Path
    result_folder: Path
    format_: str
    quality: int


class Handler:
    __suffixes__ = []

    def __init__(self, args: HandlerArgs) -> None:
        self._source_folder = args.source_folder
        self._result_folder = args.result_folder
        self._format = args.format_
        self._quality = args.quality

    def _get_all_files(self) -> list[Path]:
        return search.find_all(self._source_folder, self.__suffixes__)
