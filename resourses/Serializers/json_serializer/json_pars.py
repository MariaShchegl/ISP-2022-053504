def dumps(obj: object):
    return encode(obj)


def dump(obj: object, fp=""):
    formate_obj = encode(obj)
    fp.write(formate_obj)


def loads(string: str):
    return decode(string)


def load(fp=""):
    buffer = fp.read()
    return decode(buffer)


def encode(obj: object):
    formate_obj = []
    if isinstance(obj, dict):
        formate_obj.append('{')
        tmp = {}
        while (obj.keys()):
            key, value = obj.popitem()
            tmp[key] = value
        obj = tmp
        while (obj.keys()):
            key, value = obj.popitem()
            if not isinstance(key, str):
                raise KeyError('Key must be a string')
            else:
                formate_obj.append(encode(key))
                formate_obj.append(': ')
                formate_obj.append(encode(value))
                if (obj.keys()):
                    formate_obj.append(', ')
        formate_obj.append('}')
    if isinstance(obj, list):
        formate_obj.append('[')
        obj.reverse()
        while (obj):
            value = obj.pop()
            formate_obj.append(encode(value))
            if (obj):
                formate_obj.append(', ')
        formate_obj.append(']')
    if (isinstance(obj, int) or isinstance(obj, float)) and not isinstance(obj, bool):
        formate_obj.append(obj)
    if obj in (True, False, None):
        if obj is True:
            formate_obj.append('true')
        if obj is False:
            formate_obj.append('false')
        if obj is None:
            formate_obj.append('null')
    if isinstance(obj, str):
        formate_obj.append('"')
        formate_obj.append(obj)
        formate_obj.append('"')
    return ''.join(str(elem) for elem in formate_obj)


def decode(string: str):
    return deform(string)[0]


def deform(string: str):
    ptr = 0
    while ptr < len(string):
        if string[ptr] == ' ' or string[ptr] == '\n':
            ptr += 1
            continue
        if string[ptr] == '{':
            ptr += 1
            result = deform_dict(string[ptr:])
            ptr += result[1]
            return result[0], ptr
        if string[ptr] == '[':
            ptr += 1
            result = deform_list(string[ptr:])
            ptr += result[1]
            return result[0], ptr
        if string[ptr] == '"':
            ptr += 1
            result = deform_str(string[ptr:])
            ptr += result[1]
            return result[0], ptr
        if ptr != len(string) - 1:
            if string[ptr] == '-' and string[ptr + 1].isnumeric():
                ptr += 1
                result = deform_nums(string[ptr:])
                ptr += result[1]
                return -1 * result[0], ptr
        if string[ptr].isnumeric():
            result = deform_nums(string[ptr:])
            ptr += result[1]
            return result[0], ptr
        if string[ptr: ptr + 5] == 'false':
            ptr += 5
            return False, ptr
        if string[ptr: ptr + 4] == 'true':
            ptr += 4
            return True, ptr
        if string[ptr: ptr + 4] == 'null':
            ptr += 4
            return None, ptr
        ptr += 1
    return None, ptr


def deform_dict(string: str):
    obj = {}
    ptr = 0
    while ptr < len(string):
        char = string[ptr]
        if string[ptr] == ' ' or string[ptr] == '\n':
            ptr += 1
            continue
        if string[ptr] == '}':
            ptr += 1
            break
        result = deform(string[ptr:])
        key = result[0]
        ptr += result[1]
        ptr = string.find(':', ptr) + 1
        result = deform(string[ptr:])
        obj[key] = result[0]
        ptr += result[1]
    return obj, ptr


def deform_list(string: str):
    obj = []
    ptr = 0
    while ptr < len(string):
        if string[ptr] == ' ' or string[ptr] == '\n':
            ptr += 1
            continue
        if string[ptr] == ']':
            ptr += 1
            break
        result = deform(string[ptr:])
        obj.append(result[0])
        ptr += result[1]
    return obj, ptr


def deform_str(string: str):
    obj = ""
    ptr = 0
    while ptr < len(string):
        if string[ptr] == '"':
            ptr += 1
            break
        obj += string[ptr]
        ptr += 1
    return obj, ptr


def deform_nums(string: str):
    obj = ""
    ptr = 0
    num_type = int
    while ptr < len(string):
        if not ptr == len(string) - 1:
            if string[ptr] == '.' and string[ptr + 1].isnumeric():
                num_type = float
                obj += string[ptr]
                ptr += 1
                continue
        if not string[ptr].isnumeric():
            break
        obj += string[ptr]
        ptr += 1
    if num_type is int:
        obj = int(obj)
    else:
        obj = float(obj)
    return obj, ptr
