import sys
import pytest
from unittest.mock import call

from pybash.commands import CommandStreams, WcCommand


@pytest.fixture
def command_streams():
    return CommandStreams(sys.stdin, sys.stdout, sys.stderr)


def test_empty_file(mocker, command_streams, empty_text_file):
    mocker.patch("sys.stdout.write")
    file_name, _ = empty_text_file
    arguments = [file_name]

    result = WcCommand().run(arguments, command_streams)
    sys.stdout.write.assert_called_once_with(f"0 0 0 {file_name}" + "\n")
    assert result == 0


def test_single_file(mocker, command_streams, text_file):
    mocker.patch("sys.stdout.write")
    file_name, _ = text_file
    arguments = [file_name]

    result = WcCommand().run(arguments, command_streams)
    sys.stdout.write.assert_called_once_with(f"4 6 40 {file_name}\n")
    assert result == 0


def test_absent_file(mocker, command_streams):
    mocker.patch("sys.stdout.write")
    file_name = "absent_file"
    arguments = [file_name]

    result = WcCommand().run(arguments, command_streams)
    sys.stdout.write.assert_called_once_with(
        f"wc: {file_name}: No such file or directory\n"
    )
    assert result == 1


def test_multiple_existing_files(mocker, command_streams, text_file):
    mocker.patch("sys.stdout.write")
    file_name, _ = text_file
    arguments = [file_name, file_name]

    result = WcCommand().run(arguments, command_streams)
    sys.stdout.write.assert_has_calls(
        [
            call(f"4 6 40 {file_name}\n"),
            call(f"4 6 40 {file_name}\n"),
            call("8 12 80 total\n"),
        ]
    )
    assert result == 0


def test_multiple_absent_files(mocker, command_streams):
    mocker.patch("sys.stdout.write")
    arguments = ["absent", "absent2"]

    result = WcCommand().run(arguments, command_streams)
    sys.stdout.write.assert_has_calls(
        [
            call(f"wc: absent: No such file or directory\n"),
            call("wc: absent2: No such file or directory\n"),
            call("0 0 0 total\n"),
        ]
    )
    assert result == 1


def test_mixture_absent_existing_files(mocker, command_streams, text_file):
    mocker.patch("sys.stdout.write")
    file_name, _ = text_file
    arguments = [file_name, "absent", "absent2"]

    result = WcCommand().run(arguments, command_streams)
    sys.stdout.write.assert_has_calls(
        [
            call(f"4 6 40 {file_name}\n"),
            call(f"wc: absent: No such file or directory\n"),
            call("wc: absent2: No such file or directory\n"),
            call("4 6 40 total\n"),
        ]
    )
    assert result == 1


def test_single_folder(mocker, command_streams, text_file):
    mocker.patch("sys.stdout.write")
    f, _ = text_file
    arguments = [f.parent]
    result = WcCommand().run(arguments, command_streams)
    sys.stdout.write.assert_has_calls(
        [call(f"wc: {f.parent}: Is a directory\n"), call(f"0 0 0 {f.parent}\n")]
    )
    assert result == 1


def test_mixture_folder_file(mocker, command_streams, text_file):
    mocker.patch("sys.stdout.write")
    f, _ = text_file
    arguments = [f, f.parent]
    result = WcCommand().run(arguments, command_streams)
    sys.stdout.write.assert_has_calls(
        [
            call(f"4 6 40 {f}\n"),
            call(f"wc: {f.parent}: Is a directory\n"),
            call(f"0 0 0 {f.parent}\n"),
            call("4 6 40 total\n"),
        ]
    )
    assert result == 1


def test_file_no_permissions(mocker, command_streams, no_permissions_file):
    mocker.patch("sys.stdout.write")
    f, _ = no_permissions_file
    arguments = [f]
    result = WcCommand().run(arguments, command_streams)
    sys.stdout.write.assert_called_once_with(f"wc: {f}: Permission denied\n")
    assert result == 1
