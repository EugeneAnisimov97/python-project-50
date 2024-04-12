from gendiff.parsing import to_txt


def to_str(value):
    if isinstance(value, bool):
        if value:
            return 'true'
        else:
            return 'false'
    return value


def generate_diff(file1, file2):    # gendiff 'tests/fixtures/file1.json' 'tests/fixtures/file2.json' gendiff 'tests/fixtures/filepath1.yml' 'tests/fixtures/filepath2.yml'  # noqa: E501
    data1, data2 = to_txt(file1, file2)
    result = ['{']
    keys = data1.keys() | data2.keys()
    for key in sorted(keys):
        if key not in data1:
            result.append(f'  + {key}: {to_str(data2[key])}')
        elif key not in data2:
            result.append(f'  - {key}: {to_str(data1[key])}')
        elif data1[key] != data2[key]:
            result.append(f'  - {key}: {to_str(data1[key])}')
            result.append(f'  + {key}: {to_str(data2[key])}')
        else:
            result.append(f'    {key}: {to_str(data2[key])}')
    result.append('}')
    return '\n'.join(result)
