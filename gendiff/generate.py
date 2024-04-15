def to_str(value):
    if isinstance(value, bool):
        if value:
            return 'true'
        else:
            return 'false'
    return value


def get_added(key, value):
    return {'status': 'added',
            'key': key,
            'new_value': value}
    
    
def get_deleted(key, value):
    return {'status': 'deleted',
            'key': key,
            'old_value': value}
    
    
def get_unchanged(key, value):
    return {'status': 'unchanged',
            'key': key,
            'new_value': value}
    
    
def get_changed(key, value1, value2):
    return {'status': 'changed',
            'key': key,
            'new_value': value1,
            'old_value': value2}
    
    
def get_interior(key, value1, value2):
    return {
            'status': 'interior',
            'key': key,
            'children': generate(value1, value2)
            }


def generate(data1, data2):
    diff = []
    keys = data1.keys() | data2.keys()
    for key in sorted(keys):
        value1 = data1.get(key)
        value2 = data2.get(key)
        if key not in data1:
            diff.append(get_added(key, value2))
        elif key not in data2:
            diff.append(get_deleted(key,value1))
        elif data1[key] != data2[key]:
            diff.append(get_changed(key, value1, value2))
        elif isinstance(value1, dict) and isinstance(value2, dict):
            diff.append(get_interior(key, value1, value2))
        else:
            diff.append(get_unchanged(key, value1))
    return diff



# def generate_different(value, replacer = ' ', spaces_count = 2):
#     def iter_(corrent_value, deep):
#         if not isinstance(corrent_value, dict):
#             return str(corrent_value)
#         deeps = deep + spaces_count
#         deep_line = deeps * replacer
#         lines = []
#         for key, value in corrent_value.items():
#             lines.append(f'{deep_line}{key}: {iter_(value, deeps)}')
#         result = itertools.chain("{", lines, [replacer * deep + "}"])
#         return '\n'.join(result)