from pybash.parsers.lexical_parser import LexicalParser
from pybash.parsers.semantic_parser import SemanticParser

from pybash.command import Command


class Parser:
    def __init__(self):
        self.__lexical_parser = LexicalParser()
        self.__semantic_parser = SemanticParser(LexicalParser.tokens)

    def parse(self, string):
        specification = self.__semantic_parser.parser.parse(
            string, lexer=self.__lexical_parser.lexer
        )

        return specification[0], specification[1:]
