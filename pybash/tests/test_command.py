import pytest

from pybash.command import *


def perform(argument):
    return Command.build(argument)


# .build
def test_echo_argument():
    assert type(perform("echo")) == EchoCommand


def test_cat_argument():
    assert type(perform("cat")) == CatCommand


def test_assign_argument():
    assert type(perform("__internal_assign")) == AssignCommand


def test_wc_argument():
    assert type(perform("wc")) == WcCommand


def test_pwd_argument():
    assert type(perform("pwd")) == PwdCommand


def test_exit_argument():
    assert type(perform("exit")) == ExitCommand


def test_external_command():
    assert type(perform("python")) == ExternalCommand
