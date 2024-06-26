from gendiff.parser import parse_file
from gendiff.diff_tree import generate
from gendiff.formatters import get_format


def generate_diff(file1, file2, formatter='stylish'):
    '''Uploading a file to a user with the selected format'''
    data1 = parse_file(file1)
    data2 = parse_file(file2)
    diff = generate(data1, data2)
    return get_format(diff, formatter)
