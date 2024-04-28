import pytest
import json
from gendiff.parser import parse_file


@pytest.mark.parametrize('input_file,expected_result', [
    (
        'tests/fixtures/file1nested.json', 'tests/fixtures/file1nested_result.json'  # noqa: E501
    ),
    (
        'tests/fixtures/file2nested.yml', 'tests/fixtures/file2nested_result.json'  # noqa: E501
    )
])
def test_parser(input_file, expected_result):
    with (
        open(expected_result, 'r') as expected_output
    ):
        output = expected_output.read()
        loaded_file = parse_file(input_file)
        assert loaded_file == json.loads(output)


def test_unsupported_format():
    with pytest.raises(ValueError):
        parse_file("tests/fixtures/filepath2.txt")
