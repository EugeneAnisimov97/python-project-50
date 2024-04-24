import itertools
from gendiff.constants import ADDED, DELETED, UNCHANGED, CHANGED, INTERIOR, DELETE, ADD, NONE, SEPARATOR  # noqa: E501


def to_str(value, spaces_count=2):
    if value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, dict):
        spaces = (spaces_count + 4) * SEPARATOR
        lines = ['{']
        for key, val in value.items():
            lines.append(f"{spaces}{NONE}{key}: {to_str(val, spaces_count + 4)}")  # noqa: E501
        result = itertools.chain(lines, [(spaces_count + 2) * SEPARATOR + '}'])
        string = '\n'.join(result)
        return string
    return f"{value}"


def make_stylish_format(diff, count_space=2):  # noqa: C901
    spaces = count_space * SEPARATOR
    corr_diff = ['{']
    for item in diff:
        key = item.get('key')
        old_value = to_str(item.get("old_value"), count_space)
        new_value = to_str(item.get("new_value"), count_space)
        status = item.get('status')
        if status == ADDED:
            corr_diff.append(f'{spaces}{ADD}{key}: {new_value}')
        elif status == DELETED:
            corr_diff.append(f'{spaces}{DELETE}{key}: {old_value}')
        elif status == UNCHANGED:
            corr_diff.append(f'{spaces}{NONE}{key}: {new_value}')
        elif status == CHANGED:
            corr_diff.append(f'{spaces}{DELETE}{key}: {old_value}')
            corr_diff.append(f'{spaces}{ADD}{key}: {new_value}')
        elif status == INTERIOR:
            corr_diff.append(f'{spaces}{NONE}{key}: {make_stylish_format(item.get("children"), count_space + 4)}')  # noqa: E501
    result = itertools.chain(corr_diff, [(count_space - 2) * SEPARATOR + '}'])
    return '\n'.join(result)
