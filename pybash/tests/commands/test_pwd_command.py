import sys
import pytest
from unittest.mock import call

from pybash.commands import CommandStreams, PwdCommand
from pybash.environment import Environment


@pytest.fixture
def command_streams():
    return CommandStreams(sys.stdin, sys.stdout, sys.stderr)


def test_works_as_expected(mocker, command_streams):
    mocker.patch("sys.stdout.write")
    result = PwdCommand().run([], command_streams)

    assert result == 0
    sys.stdout.write.assert_called_once_with(Environment().get("PWD") + "\n")
