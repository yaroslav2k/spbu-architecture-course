import sys
import pytest

from pybash.commands import CommandStreams, AssignCommand
from pybash.environment import Environment


@pytest.fixture
def command_streams():
    return CommandStreams(sys.stdin, sys.stdout, sys.stderr)


def test_mutates_environment(command_streams):
    arguments = ["foo", "bar"]
    AssignCommand().run(arguments, command_streams)

    assert Environment().get(arguments[0]) == arguments[1]
