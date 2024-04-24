from gendiff.differ import generate_diff


def test_plain():
    with (open('tests/fixtures/resultplain.txt', 'r') as test):
        resoult_test = test.read()
    assert generate_diff('tests/fixtures/file1nested.json', 'tests/fixtures/file2nested.json', 'plain') == resoult_test  # noqa: E501
