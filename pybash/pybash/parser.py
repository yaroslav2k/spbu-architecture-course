from pybash.parsers.lexical_parser import LexicalParser
from pybash.parsers.semantic_parser import SemanticParser

from pybash.command import Command


class Parser:
    """Class that provides parsing functionality."""

    def __init__(self):
        self._lexical_parser = LexicalParser()
        self._semantic_parser = SemanticParser(LexicalParser.tokens)

    def parse(self, string: str) -> tuple[str, list[str]]:
        """
        Parses given string.

        Parameters
        ----------
        string: str
            string to parse

        Returns
        -------
        tuple[str, list[str]]
            parsed result consists of command and its arguments
        """
        specification = self._semantic_parser.parser.parse(
            string, lexer=self._lexical_parser.get_parsing_backend()
        )

        return specification[0], specification[1:]
