from gendiff.constants import ADDED, DELETED, CHANGED, INTERIOR


def to_str(value):
    '''Getting the string form of a value'''
    if value is None:
        return 'null'
    if isinstance(value, bool) or value == 0:
        return str(value).lower()
    if isinstance(value, (dict, list)):
        return '[complex value]'
    return f"'{value}'"


def make_plain(diff, ways=''):
    '''Generating file change lines'''
    key = diff.get('key')
    old_value = to_str(diff.get("old_value"))
    new_value = to_str(diff.get("new_value"))
    status = diff.get('status')
    correct_way = f"{ways}.{key}" if ways else key
    if status == ADDED:
        line = f"Property '{correct_way}' was added with value: {new_value}"
    elif status == DELETED:
        line = f"Property '{correct_way}' was removed"
    elif status == CHANGED:
        line = f"Property '{correct_way}' was updated. From {old_value} to {new_value}"  # noqa: E501
    elif status == INTERIOR:
        line = make_plain_format(diff.get("children"), correct_way)
    else:
        line = None
    return line


def make_plain_format(diff, ways=''):
    result = []
    for item in diff:
        correct_value = make_plain(item, ways)
        if correct_value is not None:
            result.append(correct_value)
    return '\n'.join(result)
