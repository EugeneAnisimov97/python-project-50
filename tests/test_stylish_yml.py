from gendiff.generate_diff import generate_diff


def test_stylish_yml():
    with (open('tests/fixtures/resultstylish.txt', 'r') as test):
        resoult_test = test.read()
    assert generate_diff('tests/fixtures/file1nested.yml', 'tests/fixtures/file2nested.yml') == resoult_test  # noqa: E501
