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
        lines = []
        for key, val in value.items():
            formatted_value = to_str(val, spaces_count + 4)
            lines.append(f"{spaces}{NONE}{key}: {formatted_value}")
        line = '\n'.join(lines)
        return line
    return f'{value}'


def make_stylish_format(diff, count_space=2):
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
        elif status == 'charged':
            corr_diff.append(f'{spaces}{DELETE}{key}: {old_value}')
            corr_diff.append(f'{spaces}{ADD}{key}: {new_value}')
        elif status == 'interior':
            corr_diff.append(f'{spaces}{NONE}{key}: {make_stylish_format(i['children'], count_space + 4)}')
    corr_diff.append('}')
    string = '\n'.join(corr_diff)
    
    return string
    

# def to_str(value):
#     if isinstance(value, bool):
#         if value:
#             return 'true'
#         else:
#             return 'false'
#     return value


# def get_added(key, value):
#     return {'status': 'added',
#             'key': key,
#             'new_value': value}
    
    
# def get_deleted(key, value):
#     return {'status': 'deleted',
#             'key': key,
#             'old_value': value}
    
    
# def get_unchanged(key, value):
#     return {'status': 'unchanged',
#             'key': key,
#             'value': value}
    
    
# def get_changed(key, value1, value2):
#     return {'status': 'changed',
#             'key': key,
#             'new_value': value1,
#             'old_value': value2}
    
    
# def get_interior(key, value1, value2):
#     return {'status': 'interior',
#             'key': key,
#             'children': generate(value1, value2)}


# def generate(data1, data2):
#     diff = []
#     keys = data1.keys() | data2.keys()
#     for key in sorted(keys):
#         value1 = data1.get(key)
#         value2 = data2.get(key)
#         if key not in data1:
#             diff.append(get_added(key, value2))
#         elif key not in data2:
#             diff.append(get_deleted(key,value1))
#         elif data1[key] != data2[key]:
#             diff.append(get_unchanged(key, value1, value2))
#         elif isinstance(data1, dict) and isinstance(data2, dict):
#             diff.append(get_interior(key, value1, value2))
#         else:
#             diff.append(get_unchanged(key, value1))
#     return diff