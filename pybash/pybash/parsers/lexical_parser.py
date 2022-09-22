from ply import lex


class LexicalParser:
    tokens = ("ASSIGNMENT", "IDENTIFIER")

    t_ignore = " \t\n"

    def __init__(self):
        self.lexer = lex.lex(module=self)

    def parse(self, string):
        self.lexer.input(string)

        return list(self.lexer)

    # TODO: add comment.
    def t_ASSIGNMENT(self, t):
        r"\S+=\S+"

        return t

    def t_IDENTIFIER(self, t):
        r"[^ \t\n\r\f\v=]+"
        value = t.value

        if value[0] == '"' and value[-1] == '"' or value[0] == "'" and value[-1] == "'":
            value = value[1:-1]
        t.value = value

        return t

    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)
