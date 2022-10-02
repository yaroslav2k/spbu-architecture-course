import pytest

from pybash.parsers.lexical_parser import LexicalParser
from pybash.parsers.semantic_parser import SemanticParser
from pybash.custom_exceptions import ParsingFailureException
from pybash.environment import Environment


def perform(value):
    return SemanticParser(LexicalParser.tokens).parse(value)


def test_parse():
    expectations = [
        ("foo bar 1 2 3", [["foo", "bar", "1", "2", "3"]]),
        ("foo=bar", [["__internal_assign", "foo", "bar"]]),
    ]

    for expectation_entry in expectations:
        result = perform(expectation_entry[0])

        assert perform(expectation_entry[0]) == expectation_entry[1]


def test_error_not_debug():
    with pytest.raises(ParsingFailureException):
        SemanticParser(LexicalParser.tokens).parse("foo=bar foo=bar")


def test_error_debug(mocker):
    mocker.patch("builtins.print")
    Environment().set("PYBASH_DEBUG", "true")

    SemanticParser(LexicalParser.tokens).parse("foo=bar foo=bar")

    print.assert_called_once_with("Syntax error at 'foo=bar'")
