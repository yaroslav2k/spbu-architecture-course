import io
from dataclasses import dataclass


@dataclass
class CommandStreams:
    input: io.TextIOWrapper
    output: io.TextIOWrapper
    error: io.TextIOWrapper
