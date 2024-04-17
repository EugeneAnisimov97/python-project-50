from gendiff.parsing import load_correct_file
from gendiff.generate import generate
from gendiff.formatters.choice_format import get_format


def generate_diff(file1, file2, formatter='stylish'):    # poetry run gendiff tests/fixtures/file1.json tests/fixtures/file2.json gendiff 'tests/fixtures/filepath1.yml' 'tests/fixtures/filepath2.yml'  # noqa: E501
    data1, data2 = load_correct_file(file1, file2)
    diff = generate(data1, data2)
    return get_format(diff, formatter)
