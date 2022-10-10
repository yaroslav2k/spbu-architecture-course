import sys
import pytest
from unittest.mock import call

from pybash.commands import CommandStreams, GrepCommand


@pytest.fixture
def file_A(tmp_path_factory):
    content = "Hello world!\npython\nfixture\nhello WorLD\nTeMp"
    file_name = "grep_a.txt"
    f = tmp_path_factory.mktemp("data") / file_name
    f.touch()
    f.write_text(content)

    return f, content


@pytest.fixture
def file_B(tmp_path_factory):
    content = "goodbye cruel world!\nempty\nlove to the world\n"
    file_name = "grep_b.txt"
    f = tmp_path_factory.mktemp("data") / file_name
    f.touch()
    f.write_text(content)

    return f, content


@pytest.fixture
def command_streams():
    return CommandStreams(sys.stdin, sys.stdout, sys.stderr)


def test_single_pattern_single_file_no_params(mocker, command_streams, file_A):
    mocker.patch("sys.stdout.write")
    f, _ = file_A

    arguments = ["temp", str(f)]
    result = GrepCommand().run(arguments, command_streams)
    sys.stdout.write.assert_not_called()
    assert result == 1

    arguments = ["TeMp", str(f)]
    result = GrepCommand().run(arguments, command_streams)
    sys.stdout.write.assert_called_once_with(f"TeMp\n")
    assert result == 0


def test_absent_file(mocker, command_streams):
    mocker.patch("sys.stdout.write")

    arguments = ["temp", "absent"]
    result = GrepCommand().run(arguments, command_streams)
    sys.stdout.write.assert_called_once_with(
        "grep: absent: No such file or directory\n"
    )
    assert result == 2


def test_single_pattern_multiple_files_no_params(
    mocker, command_streams, file_A, file_B
):
    mocker.patch("sys.stdout.write")
    fA, _ = file_A
    fB, _ = file_B
    arguments = ["world", str(fA), str(fB)]
    result = GrepCommand().run(arguments, command_streams)
    sys.stdout.write.assert_has_calls(
        [
            call(f"{fA}:Hello world!\n"),
            call(f"{fB}:goodbye cruel world!\n"),
            call(f"{fB}:love to the world\n"),
        ]
    )
    assert result == 0


def test_single_pattern_single_file_w_param(mocker, command_streams, file_A):
    mocker.patch("sys.stdout.write")
    f, _ = file_A
    arguments = ["-w", "hell", str(f)]
    result = GrepCommand().run(arguments, command_streams)
    sys.stdout.write.assert_not_called()
    assert result == 1

    arguments = ["-w", "hello", str(f)]
    result = GrepCommand().run(arguments, command_streams)
    sys.stdout.write.assert_called_once_with(f"hello WorLD\n")
    assert result == 0


def test_single_pattern_single_file_i_param(mocker, command_streams, file_A):
    mocker.patch("sys.stdout.write")
    f, _ = file_A
    arguments = ["-i", "HELLO wOrld", str(f)]
    result = GrepCommand().run(arguments, command_streams)
    sys.stdout.write.assert_has_calls(
        [
            call("Hello world!\n"),
            call("hello WorLD\n"),
        ]
    )
    assert result == 0


def test_single_pattern_single_file_A_param(mocker, command_streams, file_A):
    mocker.patch("sys.stdout.write")
    f, _ = file_A
    arguments = ["-A", "1", "-i", "HELLO wOrld", str(f)]
    result = GrepCommand().run(arguments, command_streams)
    sys.stdout.write.assert_has_calls(
        [
            call("Hello world!\n"),
            call("python\n"),
            call("--\n"),
            call("hello WorLD\n"),
            call("TeMp\n"),
        ]
    )
    assert result == 0


def test_single_pattern_multiple_files_A_param(mocker, command_streams, file_A, file_B):
    mocker.patch("sys.stdout.write")
    fA, _ = file_A
    fB, _ = file_B
    arguments = ["-A", "1", "-i", "world", str(fA), str(fB)]
    result = GrepCommand().run(arguments, command_streams)
    sys.stdout.write.assert_has_calls(
        [
            call(f"{fA}:Hello world!\n"),
            call(f"{fA}:python\n"),
            call("--\n"),
            call(f"{fA}:hello WorLD\n"),
            call(f"{fA}:TeMp\n"),
            call("--\n"),
            call(f"{fB}:goodbye cruel world!\n"),
            call(f"{fB}:empty\n"),
            call(f"{fB}:love to the world\n"),
        ]
    )
    assert result == 0


def test_multiple_patterns_multiple_files_w_param(mocker, command_streams, file_A, file_B):
    mocker.patch("sys.stdout.write")
    fA, _ = file_A
    fB, _ = file_B
    arguments = ["-w", "Hell|ruel", str(fA), str(fB)]
    result = GrepCommand().run(arguments, command_streams)
    sys.stdout.write.assert_not_called()
    assert result == 1

    arguments = ["-w", "Hello|cruel", str(fA), str(fB)]
    result = GrepCommand().run(arguments, command_streams)
    sys.stdout.write.assert_has_calls(
        [
            call(f"{fA}:Hello world!\n"),
            call(f"{fB}:goodbye cruel world!\n"),
        ]
    )
    assert result == 0
