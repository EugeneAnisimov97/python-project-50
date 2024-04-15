from gendiff.formatters.stylish import make_stylish_format

def get_format(diff, formatter):
    if formatter == 'stylish':
        return make_stylish_format(diff)
    