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
