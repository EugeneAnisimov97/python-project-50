import json
import yaml
import os


def to_json(file1, file2):
    with (
        open(file1, 'r') as file1,
        open(file2, 'r') as file2,
    ):
        data1 = json.load(file1)
        data2 = json.load(file2)
        return data1, data2


def to_yaml(file1, file2):
    with (
        open(file1, 'r') as file1,
        open(file2, 'r') as file2,
    ):
        data1 = yaml.safe_load(file1)
        data2 = yaml.safe_load(file2)
        return data1, data2


def load_correct_file(file1, file2):
    ext_file1 = os.path.splitext(file1)[1]
    ext_file2 = os.path.splitext(file2)[1]
    if ext_file1 and ext_file2 == '.json':
        return to_json(file1, file2)
    elif ext_file1 and ext_file2 in ['.yml', '.yaml']:
        return to_yaml(file1, file2)
    else:
        return 'Files of different resolutions'
