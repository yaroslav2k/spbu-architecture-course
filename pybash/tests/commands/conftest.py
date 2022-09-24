import pytest


@pytest.fixture(scope="session")
def text_file(tmp_path_factory):
    content = "Hello world!"
    file_name = "a.txt"
    f = tmp_path_factory.mktemp("data") / file_name
    f.touch()
    f.write_text(content)

    return f, content
