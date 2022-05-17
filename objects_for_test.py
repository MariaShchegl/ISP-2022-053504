import math
string = "Jormungand"
int1 = 1488
float1 = 1.09
bool1 = True
bytes1 = bytes(b'd\x01S\x00')
bytearr1 = bytearray(bytes1)
builtinfunc1 = len
list1 = ['a', 2, 3.0, False]
set1 = {1, 'b', 3.0, True}
frozenset1 = frozenset(list1)
tpl1 = tuple(list1)
dict1 = {'first_key': 1, 'second_key': 'sec_val'}


class JustClass:
    def __init__(self):
        self.a = 'a'
        self.b = 1


class B:
    pass


class MultClass(JustClass, B):
    pass


obj1 = JustClass()


def hello():
    return 'Hello, world!'


exp_hello = 'Hello, world!'
name = 'Maria'


def say_hello():
    global name
    return 'Hello, ' + name


exp_say_hello = 'Hello, Timophei'
json_file = 'json_file.json'
yaml_file = 'yaml_file.yaml'
toml_file = 'toml_file.toml'


def add(a, b):
    return a + b


exp_add = 5
power = lambda num, p: num ** p
exp_power = 8
