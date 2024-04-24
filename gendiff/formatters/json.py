import json


def make_json_format(diff):
    '''Output in structured json format'''
    return json.dumps(diff, indent=4)
