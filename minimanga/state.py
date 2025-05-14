from pathlib import Path


class State:
    def __init__(
        self, from_: Path, to: Path, format: str, quality: int
    ) -> None:
        self.from_ = from_
        self.to = to
        self.format = format
        self.quality = quality

    def __repr__(self) -> str:
        return f'State(from={self.from_}, to={self.to}, format={self.format}, quality={self.quality})'
