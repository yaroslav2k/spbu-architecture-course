from query_parser import QueryParser


class Executor:
    def __init__(self):
        pass

    def call(self, query):
        QueryParser().call(query).run()


Executor().call("cat 123") # Just for testing purposes.
