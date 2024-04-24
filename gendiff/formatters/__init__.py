from gendiff.formatters.stylish import make_stylish_format
from gendiff.formatters.plain import make_plain_format
from gendiff.formatters.json import make_json_format


def get_format(diff, formatter):
    if formatter == 'stylish':
        return make_stylish_format(diff)
    if formatter == 'plain':
        return make_plain_format(diff)
    if formatter == 'json':
        return make_json_format(diff)
