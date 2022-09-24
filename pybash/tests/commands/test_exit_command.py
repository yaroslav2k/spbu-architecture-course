import sys
import pytest

from pybash.commands import CommandStreams, ExitCommand
from pybash.custom_exceptions import UserExitException


@pytest.fixture
def command_streams():
    return CommandStreams(sys.stdin, sys.stdout, sys.stderr)


def test_raises_expected_exception(command_streams):
    with pytest.raises(UserExitException):
        ExitCommand().run([], command_streams)
