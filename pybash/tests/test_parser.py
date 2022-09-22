import pytest

from pybash.parser import Parser
from pybash.custom_exceptions import ParsingFailureException


def perform(value):
    return Parser().parse(value)


def test_regular_command_with_arguments():
    value = "cat abc.txt data.json"
    expected_output = ("cat", ["abc.txt", "data.json"])

    assert perform(value) == expected_output


def test_regular_command_without_arguments():
    value = "cat"
    expected_output = ("cat", [])

    assert perform(value) == expected_output


def test_command_staring_with_digit():
    value = "1cat"
    expected_output = ("1cat", [])

    assert perform(value) == expected_output


def test_relative_path():
    value = "./executable"
    expected_output = ("./executable", [])

    assert perform(value) == expected_output


def test_relative_path_with_arguments():
    value = "./executable foo bar"
    expected_output = ("./executable", ["foo", "bar"])

    assert perform(value) == expected_output


def test_regular_path_with_eclosed_in_single_quotes_argument():
    value = "./executable 'foo' bar"
    expected_output = ("./executable", ["foo", "bar"])

    assert perform(value) == expected_output


def test_regular_path_with_eclosed_in_double_quotes_argument():
    value = './executable foo "bar"'
    expected_output = ("./executable", ["foo", "bar"])

    assert perform(value) == expected_output


def test_regular_path_with_eclosed_in_single_and_double_quotes_argument():
    value = "./executable 'foo' \"bar\""
    expected_output = ("./executable", ["foo", "bar"])

    assert perform(value) == expected_output


def test_regular_path_with_empty_enclosed_in_quotes_argument():
    value = "executable ''"
    expected_output = ("executable", [""])


def test_regular_path_with_empty_enclosed_in_quotes_argument_and_regular_one():
    value = "executable '' abc"
    expected_output = ("executable", ["", "abc"])


def test_assignment():
    value = "a=b"
    expected_output = ("assign", ["a", "b"])

    assert perform(value) == expected_output


def test_invalid_input():
    value = "a=b foo=bar"

    with pytest.raises(ParsingFailureException):
        perform(value)
