from gendiff.generate_diff import generate_diff


def test_json():
    with (open('tests/fixtures/resultyesinner.txt', 'r') as test):
        resoult_test = test.read()
    assert generate_diff('tests/fixtures/file1nested.json', 'tests/fixtures/file2nested.json') == resoult_test  # noqa: E501
