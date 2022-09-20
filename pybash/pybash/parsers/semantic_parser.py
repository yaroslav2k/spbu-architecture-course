from pybash.command import Command

import ply.yacc as yacc


class SemanticParser:
    start = "expression"

    def __init__(self, tokens):
        self.tokens = tokens
        self.parser = yacc.yacc(module=self)

    def parse(self, string):
        return self.parser.parse(string)

    def p_term(self, p):
        "term : TERM"
        p[0] = [p[1]]

    def p_assignment(self, p):
        "assignment : ASSIGNMENT"

        tokens = p[1].split("=")
        p[0] = ["assign", tokens[0], tokens[1]]

    def p_expression(self, p):
        # fmt: off
        """expression : expression term
                      | term
                      | assignment"""
        # fmt: on
        if len(p) == 3:
            p[0] = (p[1] or []) + p[2]
        else:
            p[0] = p[1]

    def p_error(self, p):
        print("Syntax error in input!")
