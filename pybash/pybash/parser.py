from pybash.parsers.lexical_parser import LexicalParser
from pybash.parsers.semantic_parser import SemanticParser

from pybash.command import Command


class Parser:
    def __init__(self):
        self._lexical_parser = LexicalParser()
        self._semantic_parser = SemanticParser(LexicalParser.tokens)

    def parse(self, string: str) -> tuple[str, list[str]]:
        specification = self._semantic_parser.parser.parse(
            string, lexer=self._lexical_parser.lexer
        )

        return specification[0], specification[1:]
