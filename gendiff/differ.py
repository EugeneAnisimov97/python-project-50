from gendiff.parser import load_correct_file
from gendiff.diff_tree import generate
from gendiff.formatters import get_format


def generate_diff(file1, file2, formatter='stylish'):
    data1, data2 = load_correct_file(file1, file2)
    diff = generate(data1, data2)
    return get_format(diff, formatter)
