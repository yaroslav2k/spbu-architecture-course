import sys
import pytest
from unittest.mock import call

from pybash.command import CommandStreams, EchoCommand

command = EchoCommand()


@pytest.fixture
def command_streams():
    return CommandStreams(sys.stdin, sys.stdout, sys.stderr)


def test_single_parameter(mocker, command_streams):
    mocker.patch("sys.stdout.write")

    arguments = ["Hello world!"]
    result = command.run(arguments, command_streams)

    sys.stdout.write.assert_called_once_with(arguments[0] + "\n")
    assert result == 0


def test_multiple_parameters(mocker, command_streams):
    mocker.patch("sys.stdout.write")

    arguments = ["Hello world!", "123", "asdaf"]
    result = command.run(arguments, command_streams)

    sys.stdout.write.assert_called_once_with(" ".join(arguments) + "\n")
    assert result == 0


def test_zero_parameters(mocker, command_streams):
    mocker.patch("sys.stdout.write")

    result = command.run([], command_streams)

    sys.stdout.write.assert_called_once_with("\n")
    assert result == 0
