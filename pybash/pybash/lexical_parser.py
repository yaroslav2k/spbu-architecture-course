from ply import lex


class LexicalParser:
    tokens = ("TERM", "ASSIGNMENT")
    # tokens = ("TERM", )

    t_ignore = " \t\n"
    t_TERM = r"[a-zA-Z]+[0-9]*"
    t_ASSIGNMENT = r"[a-zA-Z]+[0-9]*=[a-zA-Z]+[0-9]*"

    def __init__(self):
        self.lexer = lex.lex(module=self)

    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)
