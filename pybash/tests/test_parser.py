import pytest

from pybash.parser import Parser, ParsingResult
from pybash.custom_exceptions import ParsingFailureException


def perform(value):
    return Parser().parse(value)


def test_parse():
    expectations = [
        ("cat abc.txt data.json", ParsingResult([["cat", ["abc.txt", "data.json"]]])),
        (
            "           cat abc.txt data.json",
            ParsingResult([["cat", ["abc.txt", "data.json"]]]),
        ),
        ("cat abc.txt data.json  ", ParsingResult([["cat", ["abc.txt", "data.json"]]])),
        (
            "cat abc.txt    data.json",
            ParsingResult([["cat", ["abc.txt", "data.json"]]]),
        ),
        ("cat", ParsingResult([["cat", []]])),
        ("   cat", ParsingResult([["cat", []]])),
        ("cat      ", ParsingResult([["cat", []]])),
        ("1cat", ParsingResult([["1cat", []]])),
        ("./executable", ParsingResult([["./executable", []]])),
        ("./executable foo bar", ParsingResult([["./executable", ["foo", "bar"]]])),
        ('./executable foo "bar"', ParsingResult([["./executable", ["foo", "bar"]]])),
        (
            "./executable 'foo' \"bar\"",
            ParsingResult([["./executable", ["foo", "bar"]]]),
        ),
        ("executable ''", ParsingResult([["executable", [""]]])),
        ("executable '' abc", ParsingResult([["executable", ["", "abc"]]])),
        (
            "python -c 'import os; print(os.environ.get('PATH'))'",
            ParsingResult(
                [["python", ["-c", "import os; print(os.environ.get('PATH'))"]]]
            ),
        ),
        ("a=b", ParsingResult([["__internal_assign", ["a", "b"]]])),
        ("executable '' abc", ParsingResult([["executable", ["", "abc"]]])),
        ("", None),
        ("       ", None),
        ("    \t   \n", None),
        # pipes
        ("foo | bar", ParsingResult([["foo", []], ["bar", []]])),
        ("foo | bar a123 -c", ParsingResult([["foo", []], ["bar", ["a123", "-c"]]])),
        ("foo foo foo | bar", ParsingResult([["foo", ["foo", "foo"]], ["bar", []]])),
        (
            "foo | bar | alpha | gamma",
            ParsingResult([["foo", []], ["bar", []], ["alpha", []], ["gamma", []]]),
        ),
        # FIXME!
        # (
        #     "python -c 'print(1)' | python -c 'print(1)'",
        #     ParsingResult(
        #         [["python", ["-c", "print(1)"]], ["python", ["-c", "print(1)"]]]
        #     ),
        # ),
    ]

    for expectation_entry in expectations:
        result = perform(expectation_entry[0])

        assert perform(expectation_entry[0]) == expectation_entry[1]


def test_errors():
    test_data = ["a=b foo=bar", "foo |", "| foo", "foo | |"]

    for test_entry in test_data:
        with pytest.raises(ParsingFailureException):
            perform(test_entry)
