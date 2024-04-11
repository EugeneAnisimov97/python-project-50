from gendiff.generate_diff import generate_diff


def test_yaml():
    assert generate_diff('tests/fixtures/filepath1.yml', 'tests/fixtures/filepath2.yml') == '{\n  - follow: false\n    host: hexlet.io\n  - proxy: 123.234.53.22\n  - timeout: 50\n  + timeout: 20\n  + verbose: true\n}'  # noqa: E501
