from ply import lex
from pybash.custom_exceptions import ParsingFailureException
from pybash.substitution_processor import SubstitutionProcessor


class LexicalParser:
    tokens = (
        "ASSIGNMENT",
        "IDENTIFIER",
        "SINGLE_QUOTES_ENCLOSED_IDENTIFIER",
        "DOUBLE_QUOTES_ENCLOSED_IDENTIFIER",
        "PIPE",
    )

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

        self._apply_callbacks(t)

        return t

    def t_IDENTIFIER(self, t):
        r"[^ \t\n\r\f\v=\'\"\|]+"

        self._apply_callbacks(t)

        return t

    def t_SINGLE_QUOTES_ENCLOSED_IDENTIFIER(self, t):
        r"""\'[^\t\n\r\f\v=\']*\'"""

        t.value = t.value[1:-1]
        self._apply_callbacks(t)

        return t

    def t_DOUBLE_QUOTES_ENCLOSED_IDENTIFIER(self, t):
        r"""\"[^\t\n\r\f\v=]*\" """

        t.value = t.value[1:-1]
        self._apply_callbacks(t)

        return t

    def t_PIPE(self, t):
        r"\|"

        self._apply_callbacks(t)

        return t

    def t_error(self, t):
        raise ParsingFailureException()

    def _apply_callbacks(self, t):
        self._on_parse_callback(t)

    def _on_parse_callback(self, t):
        if t.type == "IDENTIFIER" or t.type == "DOUBLE_QUOTES_ENCLOSED_IDENTIFIER":
            t.value = SubstitutionProcessor().substitute(t.value)
