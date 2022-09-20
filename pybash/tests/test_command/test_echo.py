import pytest
from pybash.command import EchoCommand

command = EchoCommand()


def test_single_parameter():
    assert ("Hello world!\n", 0) == command.run(["Hello world!"])


def test_multiple_parameters():
    assert ("Hello world! 123 asdaf\n", 0) == command.run(
        ["Hello world!", "123", "asdaf"]
    )


def test_zero_parameters():
    assert ("\n", 0) == command.run([])
