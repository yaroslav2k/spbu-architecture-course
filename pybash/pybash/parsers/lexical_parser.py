from ply import lex
from pybash.custom_exceptions import ParsingFailureException
from pybash.environment import Environment


class LexicalParser:
    tokens = ("ASSIGNMENT", "IDENTIFIER", "QUOTES_ENCLOSED_IDENTIFIER")

    t_ignore = " \t\n"

    def __init__(self):
        self._lexer = lex.lex(module=self)

    def get_parsing_backend(self):
        return self._lexer

    def parse(self, string: str):
        self._lexer.input(string)

        return list(self._lexer)

    # NOTE: This method could be implemented as class variable.
    # However, to make `ASSIGNMENT` token's priority higher than
    # `IDENTIFIER` token's priority, it's required to keep it as a
    # method.
    def t_ASSIGNMENT(self, t):
        r"\S+=\S+"

        return t

    def t_IDENTIFIER(self, t):
        r"[^ \t\n\r\f\v=\'\"]+"

        return t

    def t_QUOTES_ENCLOSED_IDENTIFIER(self, t):
        r"\'[^\t\n\r\f\v=]*\'|\"[^\t\n\r\f\v=]*\" "

        t.value = t.value[1:-1]

        return t

    def t_error(self, t):
        raise ParsingFailureException()
