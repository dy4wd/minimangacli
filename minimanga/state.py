from pathlib import Path


class State:
    def __init__(
        self, source: Path, result: Path, format: str, quality: int
    ) -> None:
        self.source = source
        self.result = result
        self.format = format
        self.quality = quality

    def __repr__(self) -> str:
        return f'State(source={self.source}, result={self.result}, format={self.format}, quality={self.quality})'
