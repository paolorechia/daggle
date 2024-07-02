import pathlib
from dataclasses import dataclass


@dataclass
class TableReference:
    name: str
    path: pathlib.Path
    format: str