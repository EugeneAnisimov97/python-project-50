from gendiff.parser import load_correct_file
from gendiff.diff_tree import generate
from gendiff.formatters.choice_format import get_format


def generate_diff(file1, file2, formatter='stylish'):    # poetry run gendiff tests/fixtures/file1nested.json tests/fixtures/file2nested.json poetry run gendiff tests/fixtures/file1nested.yml tests/fixtures/file2nested.yml  # noqa: E501
    data1, data2 = load_correct_file(file1, file2)
    diff = generate(data1, data2)
    return get_format(diff, formatter)
