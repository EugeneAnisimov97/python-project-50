import json
import os
import itertools


def to_str(value):
    if isinstance(value, bool):
        if value:
            return f'true'
        else:
            return f'false'
    return value


def generate_diff(file1, file2):    #gendiff 'tests/fixtures/file1.json' 'tests/fixtures/file2.json'
    with (
        open(file1, 'r') as file1,
        open(file2, 'r') as file2,
    ):
        data1 = json.load(file1)
        data2 = json.load(file2)
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
        result[-1] = '}'
        return '\n'.join(result)
    