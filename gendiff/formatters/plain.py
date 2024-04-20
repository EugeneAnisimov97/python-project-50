def to_str(value):
    if value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, (dict, list)):
        return '[complex value]'
    return f"'{value}'"


def make_plain_format(diff, ways=''):
    key = diff['key']
    old_value = to_str(diff.get("old_value"))
    new_value = to_str(diff.get("new_value"))
    status = diff['status']
    correct_way = f"{ways}.{key}" if ways else key
    if status == 'added':
        return f"Property '{correct_way}' was added with value: {new_value}"
    if status == 'deleted':
        return f"Property '{correct_way}' was removed"
    if status == 'changed':
        return f"Property '{correct_way}' was updated. From {old_value} to {new_value}"  # noqa: E501
    if status == 'interior':
        return make_plain(diff.get("children"), correct_way)
    else:
        return None


def make_plain(diff, ways=''):
    result = []
    for item in diff:
        correct_value = make_plain_format(item, ways)
        if correct_value is not None:
            result.append(correct_value)
    return '\n'.join(result)