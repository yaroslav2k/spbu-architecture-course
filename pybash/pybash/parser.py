from typing import Optional
from dataclasses import dataclass

from pybash.parsers.lexical_parser import LexicalParser
from pybash.parsers.semantic_parser import SemanticParser


@dataclass
class ParsingResult:
    commands: list[tuple[str, list[str]]]


class Parser:
    """
    Thin facade around PLY (python-lex-yacc), which is a dependency-free
    python implementation of GNU Flex and GNU YACC parsers.
    Current implementation uses LALR(1) parsing algorithm.
    """

    def __init__(self):
        self._lexical_parser = LexicalParser()
        self._semantic_parser = SemanticParser(LexicalParser.tokens)

    def parse(self, string: str) -> Optional[ParsingResult]:
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
        if not len(string.strip()):
            return None

        specification = self._semantic_parser.parser.parse(
            string, lexer=self._lexical_parser.get_parsing_backend()
        )

        if not specification:
            return None
        else:
            return ParsingResult(
                list(map(lambda item: [item[0], item[1:]], specification))
            )
