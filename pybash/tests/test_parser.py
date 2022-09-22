import pytest

from pybash.parser import Parser, ParsingResult
from pybash.custom_exceptions import ParsingFailureException


def perform(value):
    return Parser().parse(value)


def test_regular_command_with_arguments():
    value = "cat abc.txt data.json"
    expected_output = ParsingResult("cat", ["abc.txt", "data.json"])

    assert perform(value) == expected_output


def test_regular_command_with_arguments_with_leading_spaces():
    value = "           cat abc.txt data.json"
    expected_output = ParsingResult("cat", ["abc.txt", "data.json"])

    assert perform(value) == expected_output


def test_regular_command_with_arguments_with_trailing_spaces():
    value = "cat abc.txt data.json  "
    expected_output = ParsingResult("cat", ["abc.txt", "data.json"])

    assert perform(value) == expected_output


def test_regular_command_with_arguments_with_spaces_between_arguments():
    value = "cat abc.txt    data.json"
    expected_output = ParsingResult("cat", ["abc.txt", "data.json"])

    assert perform(value) == expected_output


def test_regular_command_without_arguments():
    value = "cat"
    expected_output = ParsingResult("cat", [])

    assert perform(value) == expected_output


def test_regular_command_without_arguments_with_leading_spaces():
    value = "   cat"
    expected_output = ParsingResult("cat", [])

    assert perform(value) == expected_output


def test_regular_command_without_arguments_with_trailing_spaces():
    value = "cat      "
    expected_output = ParsingResult("cat", [])

    assert perform(value) == expected_output


def test_command_staring_with_digit():
    value = "1cat"
    expected_output = ParsingResult("1cat", [])

    assert perform(value) == expected_output


def test_relative_path():
    value = "./executable"
    expected_output = ParsingResult("./executable", [])

    assert perform(value) == expected_output


def test_relative_path_with_arguments():
    value = "./executable foo bar"
    expected_output = ParsingResult("./executable", ["foo", "bar"])

    assert perform(value) == expected_output


def test_regular_path_with_eclosed_in_single_quotes_argument():
    value = "./executable 'foo' bar"
    expected_output = ParsingResult("./executable", ["foo", "bar"])

    assert perform(value) == expected_output


def test_regular_path_with_eclosed_in_double_quotes_argument():
    value = './executable foo "bar"'
    expected_output = ParsingResult("./executable", ["foo", "bar"])

    assert perform(value) == expected_output


def test_regular_path_with_eclosed_in_single_and_double_quotes_argument():
    value = "./executable 'foo' \"bar\""
    expected_output = ParsingResult("./executable", ["foo", "bar"])

    assert perform(value) == expected_output


def test_regular_path_with_empty_enclosed_in_quotes_argument():
    value = "executable ''"
    expected_output = ParsingResult("executable", [""])


def test_regular_path_with_empty_enclosed_in_quotes_argument_and_regular_one():
    value = "executable '' abc"
    expected_output = ParsingResult("executable", ["", "abc"])


def test_assignment():
    value = "a=b"
    expected_output = ParsingResult("assign", ["a", "b"])

    assert perform(value) == expected_output


def test_invalid_input():
    value = "a=b foo=bar"

    with pytest.raises(ParsingFailureException):
        perform(value)


def test_empty_input():
    value = ""

    assert perform(value) is None


def test_blank_input():
    value = ""

    assert perform(value) is None


def test_whitespace_input():
    value = "  \t \n"

    assert perform(value) is None
