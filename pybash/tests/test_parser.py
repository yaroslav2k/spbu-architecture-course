from pybash.parser import Parser


def perform(value):
    return Parser().parse(value)


def test_regular_command_with_arguments():
    expected_input = "cat abc.txt data.json"
    expected_output = ("cat", ["abc.txt", "data.json"])

    assert perform(expected_input) == expected_output


def test_regular_command_without_arguments():
    expected_input = "cat"
    expected_output = ("cat", [])

    assert perform(expected_input) == expected_output


def test_command_staring_with_digit():
    expected_input = "1cat"
    expected_output = ("1cat", [])

    assert perform(expected_input) == expected_output


def test_relative_path():
    expected_input = "./executable"
    expected_output = ("./executable", [])

    assert perform(expected_input) == expected_output


def test_relative_path_with_arguments():
    expected_input = "./executable foo bar"
    expected_output = ("./executable", ["foo", "bar"])

    assert perform(expected_input) == expected_output


def test_regular_path_with_eclosed_in_single_quotes_argument():
    expected_input = "./executable 'foo' bar"
    expected_output = ("./executable", ["foo", "bar"])

    assert perform(expected_input) == expected_output


def test_regular_path_with_eclosed_in_double_quotes_argument():
    expected_input = './executable foo "bar"'
    expected_output = ("./executable", ["foo", "bar"])

    assert perform(expected_input) == expected_output


def test_regular_path_with_eclosed_in_single_and_double_quotes_argument():
    expected_input = "./executable 'foo' \"bar\""
    expected_output = ("./executable", ["foo", "bar"])

    assert perform(expected_input) == expected_output


def test_regular_path_with_empty_enclosed_in_quotes_argument():
    expected_input = "executable ''"
    expected_output = ("executable", [""])


def test_regular_path_with_empty_enclosed_in_quotes_argument_and_regular_one():
    expected_input = "executable '' abc"
    expected_output = ("executable", ["", "abc"])


def test_assignment():
    expected_input = "a=b"
    expected_output = ("assign", ["a", "b"])

    assert perform(expected_input) == expected_output
