from pybash.command import Command
from pybash.custom_exceptions import ParsingFailureException
from pybash.environment import Environment

import ply.yacc as yacc


class SemanticParser:
    start = "expression"

    def __init__(self, tokens):
        self.tokens = tokens
        self.parser = yacc.yacc(module=self)

    def parse(self, string):
        return self.parser.parse(string)

    def p_empty(self, p):
        "empty :"
        pass

    def p_identifier(self, p):
        # fmt: off
        """identifier : IDENTIFIER
                      | SINGLE_QUOTES_ENCLOSED_IDENTIFIER
                      | DOUBLE_QUOTES_ENCLOSED_IDENTIFIER"""
        # fmt: on
        p[0] = [p[1]]

    def p_assignment(self, p):
        "assignment : ASSIGNMENT"

        tokens = p[1].split("=")
        p[0] = ["assign", tokens[0], tokens[1]]

    def p_expression(self, p):
        # fmt: off
        """expression : empty
                      | identifier
                      | expression identifier
                      | assignment"""
        # fmt: on
        if len(p) == 3:
            p[0] = (p[1] or []) + p[2]
        else:
            p[0] = p[1]

    def p_error(self, p):
        if Environment().get("PYBASH_DEBUG") == "true":
            print(f"Syntax error at {p.value!r}")
        else:
            raise ParsingFailureException()
