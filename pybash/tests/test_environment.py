import pytest

from pybash.environment import Environment


@pytest.fixture
def environment():
    return Environment()


def test_get_previosly_set_value(environment):
    environment.set("foo", "bar")

    assert environment.get("foo") == "bar"


def test_get_not_set_value(environment):
    environment.set("foo", "bar")

    assert environment.get("bar") == ""


def test_get_variables(environment):
    environment.set("foo", "bar")
    variables = environment.get_variables()

    assert type(variables) == dict
    assert variables.get("foo") == "bar"
