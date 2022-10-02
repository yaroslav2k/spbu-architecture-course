import pytest

from pybash.substitution_processor import SubstitutionProcessor
from pybash.environment import Environment


Environment().set("var_a", "42")
Environment().set("var_b", "xyz")


def perform(value):
    return SubstitutionProcessor().substitute(value)


def test_single_substitution():
    value = "Hello $var_a,bye"
    expected_output = "Hello 42,bye"

    assert perform(value) == expected_output


def test_multiple_substitutions():
    value = "Hello $var_a bye $var_b$var_b"
    expected_output = "Hello 42 bye xyzxyz"

    assert perform(value) == expected_output


def test_absent_substitution():
    value = "Hello $user $"
    expected_output = "Hello  $"

    assert perform(value) == expected_output


def test_weak_quoting():
    value = "Hello '$var_a,gyt' bye $var_b$var_b"
    expected_output = "Hello '$var_a,gyt' bye xyzxyz"

    assert perform(value) == expected_output


def test_full_quoting():
    value = 'Hello "$var_a,gyt" bye $var_b$var_b'
    expected_output = 'Hello "42,gyt" bye xyzxyz'

    assert perform(value) == expected_output


def test_nested_quoting_full_outside():
    value = 'Hello "\'$var_a\'", "$"asd""'
    expected_output = 'Hello "\'42\'", "$"asd""'

    assert perform(value) == expected_output


def test_nested_quoting_weak_outside():
    value = "Hello 'bye $\"hi $var_b\"'"
    expected_output = "Hello 'bye $\"hi $var_b\"'"

    assert perform(value) == expected_output
