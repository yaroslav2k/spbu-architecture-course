import sys
import pytest
import subprocess

from unittest.mock import call, ANY

from pybash.command import CommandStreams, ExternalCommand
from pybash.environment import Environment
from pybash.custom_exceptions import UnknownCommandException


@pytest.fixture
def command_streams():
    return CommandStreams(sys.stdin, sys.stdout, sys.stderr)


def test_is_external():
    assert ExternalCommand().is_external() == True


def test_run_successful_result(mocker, command_streams):
    arguments = ["python", "-c", "print(1)"]
    mocker.patch(
        "subprocess.run",
        return_value=subprocess.CompletedProcess(args=arguments, returncode=0),
    )
    result = ExternalCommand().run(arguments, command_streams)

    assert result == 0
    subprocess.run.assert_called_once_with(
        arguments, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, env=ANY, cwd=Environment().get('PWD'),
    )
    assert isinstance(subprocess.run.call_args[1]["env"], dict)


def test_run_failure_result(mocker, command_streams):
    arguments = ["python", "-c", "print(1)"]
    mocker.patch(
        "subprocess.run",
        return_value=subprocess.CompletedProcess(args=arguments, returncode=1),
    )
    result = ExternalCommand().run(arguments, command_streams)

    assert result == 1
    subprocess.run.assert_called_once_with(
        arguments, stdin=sys.stdin, stdout=sys.stdout, stderr=sys.stderr, env=ANY, cwd=Environment().get('PWD'),
    )
    assert isinstance(subprocess.run.call_args[1]["env"], dict)


def test_raises_expected_exception(mocker, command_streams):
    arguments = ["python4", "-c", "print(1)"]
    mocker.patch("subprocess.run", side_effect=FileNotFoundError())

    with pytest.raises(UnknownCommandException):
        ExternalCommand().run(arguments, command_streams)
