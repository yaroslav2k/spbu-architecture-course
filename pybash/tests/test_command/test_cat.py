import pytest
from pybash.command import CatCommand


def test_single_existing_file(text_file):
    f, content = text_file
    command = CatCommand("cat")
    result = command.run([str(f)])
    assert result == (content, 0)


def test_single_absent_file():
    command = CatCommand("cat")
    result = command.run(["absent_file"])
    assert result == ("cat: absent_file: No such file or directory\n", 1)


def test_multiple_existing_files(text_file):
    f, content = text_file
    command = CatCommand("cat")
    result = command.run([str(f), str(f), str(f)])
    assert result == (content+content+content, 0)


def test_multiple_absent_files():
    command = CatCommand("cat")
    result = command.run(["absent_file", "yet_absent_file"])
    assert result == ("cat: absent_file: No such file or directory\n"
                      "cat: yet_absent_file: No such file or directory\n", 1)

def test_muxture_absent_present_files(text_file):
    f, content = text_file
    command = CatCommand("cat")
    result = command.run([str(f), "absent_file", str(f)])
    assert result == (content +
                      "cat: absent_file: No such file or directory\n" +
                       content, 1)
