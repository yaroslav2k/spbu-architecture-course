from pybash.parser import Parser


def perform(value):
    return Parser().parse(value)


# TODO: Add human-readable function names.
def test_1():
    expected_input = "cat abc.txt data.json"
    expected_output = ("cat", ["abc.txt", "data.json"])

    assert perform(expected_input) == expected_output


def test_2():
    expected_input = "cat"
    expected_output = ("cat", [])

    assert perform(expected_input) == expected_output


def test_3():
    expected_input = "1cat"
    expected_output = ("1cat", [])

    assert perform(expected_input) == expected_output


def test_4():
    expected_input = "./executable"
    expected_output = ("./executable", [])

    assert perform(expected_input) == expected_output


def test_5():
    expected_input = "./executable foo bar"
    expected_output = ("./executable", ["foo", "bar"])

    assert perform(expected_input) == expected_output


def test_6():
    expected_input = "./executable 'foo' bar"
    expected_output = ("./executable", ["foo", "bar"])

    assert perform(expected_input) == expected_output


def test_7():
    expected_input = './executable foo "bar"'
    expected_output = ("./executable", ["foo", "bar"])

    assert perform(expected_input) == expected_output


def test_8():
    expected_input = "./executable 'foo' \"bar\""
    expected_output = ("./executable", ["foo", "bar"])

    assert perform(expected_input) == expected_output


def test_9():
    expected_input = "executable ''"
    expected_output = ("executable", [""])


def test_10():
    expected_input = "a=b"
    expected_output = ("assign", ["a", "b"])

    assert perform(expected_input) == expected_output


def test_11():
    expected_input = "foo=bar"
    expected_output = ("assign", ["foo", "bar"])

    assert perform(expected_input) == expected_output
