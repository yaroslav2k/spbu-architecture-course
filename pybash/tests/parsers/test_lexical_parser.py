import pytest
from ply.lex import LexToken

from pybash.parsers.lexical_parser import LexicalParser
from pybash.custom_exceptions import ParsingFailureException


def perform(value):
    return LexicalParser().parse(value)


def test_default():
    result = perform("python -c 'print(1)'")

    assert len(result) == 3

    assert type(result[0]) == LexToken
    assert type(result[1]) == LexToken
    assert type(result[2]) == LexToken

    assert result[0].value == "python"
    assert result[1].value == "-c"
    assert result[2].value == "print(1)"

    assert result[0].type == "IDENTIFIER"
    assert result[1].type == "IDENTIFIER"
    assert result[2].type == "SINGLE_QUOTES_ENCLOSED_IDENTIFIER"


def test_assignment():
    result = perform("joy=division")

    assert len(result) == 1
    assert type(result[0]) == LexToken
    assert result[0].value == "joy=division"
    assert result[0].type == "ASSIGNMENT"


def test_basic_pipe():
    result = perform("foo bar | echo")

    expected_length = 4
    assert (len(result)) == expected_length

    for i in range(expected_length):
        assert type(result[i]) == LexToken

    expected_values = ["foo", "bar", "|", "echo"]
    for i in range(expected_length):
        assert result[i].value == expected_values[i]

    expected_types = ["IDENTIFIER", "IDENTIFIER", "PIPE", "IDENTIFIER"]
    for i in range(expected_length):
        assert result[i].type == expected_types[i]


def test_multiple_pipes():
    result = perform("cat | echo | eval | shutdown now")

    expected_length = 8
    assert (len(result)) == expected_length

    for i in range(expected_length):
        assert type(result[i]) == LexToken

    expected_values = ["cat", "|", "echo", "|", "eval", "|", "shutdown", "now"]
    for i in range(expected_length):
        assert result[i].value == expected_values[i]

    expected_types = [
        "IDENTIFIER",
        "PIPE",
        "IDENTIFIER",
        "PIPE",
        "IDENTIFIER",
        "PIPE",
        "IDENTIFIER",
        "IDENTIFIER",
    ]
    for i in range(expected_length):
        assert result[i].type == expected_types[i]


def test_error_not_debug():
    with pytest.raises(ParsingFailureException):
        perform("foo=")
