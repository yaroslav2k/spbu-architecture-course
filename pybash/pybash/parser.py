from typing import Optional
from dataclasses import dataclass

from pybash.parsers.lexical_parser import LexicalParser

from pybash.parsers.semantic_parser import SemanticParser

from pybash.command import Command


@dataclass
class ParsingResult:
    command: str
    arguments: list[str]


class Parser:
    """Class that provides parsing functionality."""

    def __init__(self):
        self._lexical_parser = LexicalParser()
        self._semantic_parser = SemanticParser(LexicalParser.tokens)

    def parse(self, string: str) -> Optional[tuple[str, list[str]]]:
        """
        Parses given string.

        Parameters
        ----------
        string: str
            string to parse

        Returns
        -------
        Optional[tuple[str, list[str]]]
            parsed result consists of command and its arguments
            or None if no tokens to parse were found
        """
        specification = self._semantic_parser.parser.parse(
            string, lexer=self._lexical_parser.get_parsing_backend()
        )

        if specification is None:
            return specification
        else:
            return ParsingResult(specification[0], specification[1:])
