from gendiff.formatters.stylish import make_stylish_format
from gendiff.formatters.plain import make_plain


def get_format(diff, formatter):
    if formatter == 'stylish':
        return make_stylish_format(diff)
    if format == 'plain':
        return make_plain(diff)