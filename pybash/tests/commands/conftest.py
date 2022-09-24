import pytest


@pytest.fixture(scope="session")
def text_file(tmp_path_factory):
    content = "Hello world!\n12f13q3vvae\n\n{asfaf\ta34 r3\n"
    file_name = "a.txt"
    f = tmp_path_factory.mktemp("data") / file_name
    f.touch()
    f.write_text(content)

    return str(f), content


@pytest.fixture(scope="session")
def empty_text_file(tmp_path_factory):
    content = ""
    file_name = "empty.txt"
    f = tmp_path_factory.mktemp("data") / file_name
    f.touch()
    f.write_text(content)

    return str(f), content
