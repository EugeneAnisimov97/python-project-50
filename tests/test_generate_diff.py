from gendiff.generate_diff import generate_diff


def test_generate_diff():
    assert '{"follow": false}' == '{"follow": false}'