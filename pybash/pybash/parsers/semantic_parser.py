from pybash.custom_exceptions import ParsingFailureException
from pybash.environment import Environment
from pybash.commands.assign_command import AssignCommand


import ply.yacc as yacc


class SemanticParser:
    precedence = (("left", "PIPE"), ("left", "IDENTIFIER"))

    def __init__(self, tokens):
        self.tokens = tokens
        self.parser = yacc.yacc(module=self, debug=True)

    def parse(self, string):
        return self.parser.parse(string)

    def p_pipeline(self, p):
        # fmt: off
        """pipeline : expression
                    | pipeline pipe expression"""
        # fmt: on

        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = p[1] + [p[3]]

    def p_expression(self, p):
        # fmt: off
        """expression : identifier
                      | expression identifier
                      | assignment"""
        # fmt: on
        if len(p) == 3:
            p[0] = (p[1] or []) + p[2]
        else:
            p[0] = p[1]

    def p_assignment(self, p):
        """assignment : ASSIGNMENT"""

        tokens = p[1].split("=")
        p[0] = [AssignCommand._INTERNAL_IDENTIFIER, tokens[0], tokens[1]]

    def p_identifier(self, p):
        # fmt: off
        """identifier : IDENTIFIER
                      | SINGLE_QUOTES_ENCLOSED_IDENTIFIER
                      | DOUBLE_QUOTES_ENCLOSED_IDENTIFIER"""
        # fmt: on
        p[0] = [p[1]]

    def p_pipe(self, p):
        """pipe : PIPE"""

        pass

    def p_error(self, p):
        if Environment().get("PYBASH_DEBUG") == "true":
            print(f"Syntax error at {p.value!r}")
        else:
            raise ParsingFailureException()
