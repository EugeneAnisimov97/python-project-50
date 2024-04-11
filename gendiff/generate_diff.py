from gendiff.parsing import to_txt


def generate_diff(file1, file2):    # gendiff 'tests/fixtures/file1.json' 'tests/fixtures/file2.json' gendiff 'tests/fixtures/filepath1.yml' 'tests/fixtures/filepath2.yml'  # noqa: E501
    return to_txt(file1, file2)
