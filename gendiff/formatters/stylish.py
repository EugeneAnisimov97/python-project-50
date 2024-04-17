import itertools

SEPARATOR = " "
ADD = '+ '
DELETE = '- '
NONE = '  '


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
    return f'{value}'


def make_stylish_format(diff, count_space=2):  # noqa: C901
    spaces = count_space * SEPARATOR
    corr_diff = ['{']
    for i in diff:
        key = i['key']
        old_value = to_str(i.get("old_value"), count_space)
        new_value = to_str(i.get("new_value"), count_space)
        status = i['status']
        if status == 'added':
            corr_diff.append(f'{spaces}{ADD}{key}: {new_value}')
        elif status == 'deleted':
            corr_diff.append(f'{spaces}{DELETE}{key}: {old_value}')
        elif status == 'unchanged':
            corr_diff.append(f'{spaces}{NONE}{key}: {new_value}')
        elif status == 'changed':
            corr_diff.append(f'{spaces}{DELETE}{key}: {old_value}')
            corr_diff.append(f'{spaces}{ADD}{key}: {new_value}')
        elif status == 'interior':
            corr_diff.append(f'{spaces}{NONE}{key}: {make_stylish_format(i["children"], count_space + 4)}')  # noqa: E501
    result = itertools.chain(corr_diff, [(count_space - 2) * SEPARATOR + '}'])
    string = '\n'.join(result)
    return string
