import sys
import pytest

from pybash.command import CommandStreams, LsCommand

command = LsCommand()


@pytest.fixture
def command_streams():
    return CommandStreams(sys.stdin, sys.stdout, sys.stderr)


def test_too_many_arguments(mocker, command_streams):
    mocker.patch("sys.stdout.write")

    arguments = ["..", "aboba"]
    result = command.run(arguments, command_streams)

    sys.stdout.write.assert_called_once_with('Too many arguments for ls-command\n')
    assert result == -1

def test_invalid_path(mocker, command_streams):
    mocker.patch("sys.stdout.write")

    arguments = ["aboba"]
    result = command.run(arguments, command_streams)

    sys.stdout.write.assert_called_once_with("Path doesn't exist\n")
    assert result == -1

def test_correct(mocker, command_streams):
    mocker.patch("sys.stdout.write")

    arguments = ["../doc"]
    result = command.run(arguments, command_streams)
    sys.stdout.write.assert_called_once_with("assets\nsolution.pdf\numl-class-diagram.png\n")
    assert result == 0
