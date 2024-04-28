import json
import yaml
import os


def get_content(file):
    '''Reading file'''
    with (
        open(file, 'r') as file
    ):
        return file.read()


def parse_file(file):
    '''Retrieving file content'''
    ext_file = os.path.splitext(file)[1]
    if ext_file == '.json':
        return json.loads(get_content(file))
    if ext_file in ['.yml', '.yaml']:
        return yaml.safe_load(get_content(file))
    raise ValueError(f'{ext_file} unsupported. Supported formats: json and yml')
