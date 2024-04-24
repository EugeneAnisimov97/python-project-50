import json


def make_json_format(diff):
    return json.dumps(diff, indent=4)
