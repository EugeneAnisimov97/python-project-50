def to_str(value):
    if value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, (dict, list)):
        return '[complex value]'
    return f"'{value}'"


def make_plain(diff, ways=''):
    key = diff.get('key')
    old_value = to_str(diff.get("old_value"))
    new_value = to_str(diff.get("new_value"))
    status = diff.get('status')
    correct_way = f"{ways}.{key}" if ways else key
    if status == 'added':
        line = f"Property '{correct_way}' was added with value: {new_value}"
    elif status == 'deleted':
        line = f"Property '{correct_way}' was removed"
    elif status == 'changed':
        line = f"Property '{correct_way}' was updated. From {old_value} to {new_value}"  # noqa: E501
    elif status == 'interior':
        line =  make_plain_format(diff.get("children"), correct_way)
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
