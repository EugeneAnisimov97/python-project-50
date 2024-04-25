import pytest
from gendiff.differ import generate_diff


@pytest.mark.parametrize('file1, file2, format, expected_result', [
    (
        'tests/fixtures/file1nested.json', 'tests/fixtures/file2nested.json', 'stylish', 'tests/fixtures/resultstylish.txt'  # noqa: E501
    ),
    (
        'tests/fixtures/file1nested.json', 'tests/fixtures/file2nested.json', 'plain', 'tests/fixtures/resultplain.txt'  # noqa: E501
    ),
    (
        'tests/fixtures/file1nested.json', 'tests/fixtures/file2nested.json', 'json', 'tests/fixtures/resultjson.json'  # noqa: E501
    )
])
def test_formats(file1, file2, format, expected_result):
    with (
        open(expected_result, 'r') as expected_output
    ):
        output = expected_output.read()
        result = generate_diff(file1, file2, format)
        assert result == output
