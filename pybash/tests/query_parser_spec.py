from pybash.command import Command
from pybash.query_parser import QueryParser

from mamba import description, context, it
from expects import expect, equal, be_a

from faker import Faker


with description("QueryParser") as self:
    with description("#call") as self:
        with it("returns an instance of `Command` class"):
            result = QueryParser().call(Faker().pystr())

            expect(result).to(be_a(Command))
