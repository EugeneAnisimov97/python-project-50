from gendiff.constants import ADDED, DELETED, UNCHANGED, CHANGED, INTERIOR


def get_added(key, value):
    return {'status': ADDED,
            'key': key,
            'new_value': value}


def get_deleted(key, value):
    return {'status': DELETED,
            'key': key,
            'old_value': value}


def get_unchanged(key, value):
    return {'status': UNCHANGED,
            'key': key,
            'new_value': value}


def get_changed(key, value1, value2):
    return {'status': CHANGED,
            'key': key,
            'old_value': value1,
            'new_value': value2}


def get_interior(key, value1, value2):
    return {'status': INTERIOR,
            'key': key,
            'children': generate(value1, value2)}


def generate(data1, data2):
    diff = []
    keys = data1.keys() | data2.keys()
    keys_added = data1.keys() - data2.keys()
    keys_deleted = data2.keys() - data1.keys()
    for key in sorted(keys):
        value1 = data1.get(key)
        value2 = data2.get(key)
        if key in keys_deleted:
            diff.append(get_added(key, value2))
        elif key in keys_added:
            diff.append(get_deleted(key, value1))
        elif isinstance(value1, dict) and isinstance(value2, dict):
            diff.append(get_interior(key, value1, value2))
        elif value1 != value2:
            diff.append(get_changed(key, value1, value2))
        else:
            diff.append(get_unchanged(key, value1))
    return diff
