from gendiff.generate_diff import generate_diff


def test_json():
    with (open('tests/fixtures/resultnoinner.txt', 'r') as test):
        resoult_test = test.read()
    assert generate_diff('tests/fixtures/filepath1.yml', 'tests/fixtures/filepath2.yml') == resoult_test  # noqa: E501
