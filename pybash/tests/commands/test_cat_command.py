import sys
import pytest
from unittest.mock import call

from pybash.command import CommandStreams, CatCommand


@pytest.fixture
def command_streams():
    return CommandStreams(sys.stdin, sys.stdout, sys.stderr)


def test_single_existing_file(mocker, text_file, command_streams):
    mocker.patch("sys.stdout.write")

    f, content = text_file
    command = CatCommand()
    result = command.run([str(f)], command_streams)

    sys.stdout.write.assert_called_once_with(content)
    assert result == 0


def test_single_absent_file(mocker, command_streams):
    mocker.patch("sys.stdout.write")

    command = CatCommand()
    result = command.run(["absent_file"], command_streams)

    sys.stdout.write.assert_called_once_with(
        "cat: absent_file: No such file or directory\n"
    )
    assert result == 1


def test_multiple_existing_files(mocker, text_file, command_streams):
    mocker.patch("sys.stdout.write")

    f, content = text_file
    command = CatCommand()
    result = command.run([str(f), str(f), str(f)], command_streams)

    sys.stdout.write.assert_has_calls([call(content), call(content), call(content)])
    assert result == 0


def test_multiple_absent_files(mocker, command_streams):
    mocker.patch("sys.stdout.write")

    command = CatCommand()
    result = command.run(["absent_file", "yet_another_absent_file"], command_streams)

    sys.stdout.write.assert_has_calls(
        [
            call("cat: absent_file: No such file or directory\n"),
            call("cat: yet_another_absent_file: No such file or directory\n"),
        ]
    )
    assert result == 1


def test_muxture_absent_present_files(mocker, text_file, command_streams):
    mocker.patch("sys.stdout.write")

    f, content = text_file
    command = CatCommand()
    result = command.run([str(f), "absent_file", str(f)], command_streams)

    sys.stdout.write.assert_has_calls(
        [
            call(content),
            call("cat: absent_file: No such file or directory\n"),
            call(content),
        ]
    )
    assert result == 1
