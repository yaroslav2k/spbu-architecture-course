from pybash.command import Command
from pybash.query_parser import QueryParser

from mamba import description, context, it
from expects import expect, equal, be_a

with description("QueryParser") as self:
    with description("#call") as self:
        with it("mocked test"):
            result = QueryParser().call("123")

            expect(result).to(be_a(Command))
