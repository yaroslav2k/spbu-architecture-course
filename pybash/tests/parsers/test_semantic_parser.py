import pytest

from pybash.parsers.lexical_parser import LexicalParser
from pybash.parsers.semantic_parser import SemanticParser
from pybash.custom_exceptions import ParsingFailureException
from pybash.environment import Environment


def test_parse_default():
    result = SemanticParser(LexicalParser.tokens).parse("foo bar 1 2 3")

    assert result == ["foo", "bar", "1", "2", "3"]


def test_parse_assignment():
    result = SemanticParser(LexicalParser.tokens).parse("foo=bar")

    assert result == ["assign", "foo", "bar"]


def test_error_not_debug():
    with pytest.raises(ParsingFailureException):
        SemanticParser(LexicalParser.tokens).parse("foo=bar foo=bar")


def test_error_debug(mocker):
    mocker.patch("builtins.print")
    Environment().set("PYBASH_DEBUG", "true")

    SemanticParser(LexicalParser.tokens).parse("foo=bar foo=bar")

    print.assert_called_once_with("Syntax error at 'foo=bar'")
