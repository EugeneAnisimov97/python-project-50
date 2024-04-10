import json
import os
import itertools


def generate_diff(file1, file2):    #gendiff 'tests/files/file1.json' 'tests/files/file2.json'
    with (
        open(file1, 'r') as file1,
        open(file2, 'r') as file2,
    ):
        data1 = json.load(file1)
        data2 = json.load(file2)
        items = []
        # keys = data1.keys() | data2.keys()
        for key, value in data1.items():
            if key in data2:
                if data1[key] == data2[key]:
                    items.append(f'  {key}: {value}')
                else:
                    items.append(f'+ {key}: {value}')
                    items.append(f'- {key}: {data2[key]}')
            else:
                items.append(f'- {key}: {value}')
        for key, value in data2.items():
            if key not in data1:
                items.append(f'+ {key}: {value}')
        result = itertools.chain('{', items, '}')
        return '\n'.join(result)