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


def test_copy(environment):
    environment.set("foo", "bar")
    copy = Environment.copy()

    assert copy != environment
    assert copy.get("foo") == "bar"


def test_items(environment):
    result = environment.items()

    assert type(result) == type(iter(dict().items()))
