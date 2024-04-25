import pytest
from gendiff.differ import generate_diff


def get_result_stylish():
    with (
        open('tests/fixtures/resultstylish.txt', 'r') as stylish
    ):
            return stylish.read()


def get_result_plain():
    with (
        
        open('tests/fixtures/resultplain.txt', 'r') as plain
    ):
            return plain.read()


def get_result_json():
    with (
        open('tests/fixtures/resultjson.json', 'r') as json
    ):
            return json.read()


@pytest.mark.parametrize('format, expected_result', [
    (
        'stylish', get_result_stylish()
    ),
    (
        'plain', get_result_plain()
    ),
    (
        'json', get_result_json()
    )
    
])
def test_formats(format, expected_result):
    result = generate_diff('tests/fixtures/file1nested.json', 'tests/fixtures/file2nested.json', format)  # noqa: E501
    assert result == expected_result
