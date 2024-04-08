import json


def generate_diff(file1, file2):
    with (
        open(file1, 'r') as file1,
        open(file2, 'r') as file2,
    ):
        text_from_file1 = json.load(open(file1))
        text_from_file2 = json.load(open(file2))
    