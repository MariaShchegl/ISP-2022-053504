import objects_for_test as ot
from resourses import own_serializer as ser
import unittest
import math

class SerializerTester(unittest.TestCase):

    def __init__(self, method):
        super().__init__(method)
        self.json_serializer = ser.Serializer(ot.json_file,'json')
        self.yaml_serializer = ser.Serializer(ot.yaml_file, 'yaml')
        self.toml_serializer = ser.Serializer(ot.toml_file, 'toml')

    def test_str(self):
        json_obj = self.json_serializer.loads(self.json_serializer.dumps(ot.string))
        yaml_obj = self.yaml_serializer.loads(self.yaml_serializer.dumps(ot.string))
        toml_obj = self.toml_serializer.loads(self.toml_serializer.dumps(ot.string))

        self.assertEqual(json_obj, ot.string)
        self.assertEqual(yaml_obj, ot.string)
        self.assertEqual(toml_obj, ot.string)

    def test_int(self):
        json_obj = self.json_serializer.loads(self.json_serializer.dumps(ot.int1))
        toml_obj = self.toml_serializer.loads(self.toml_serializer.dumps(ot.int1))
        yaml_obj = self.yaml_serializer.loads(self.yaml_serializer.dumps(ot.int1))

        self.assertEqual(json_obj, ot.int1)
        self.assertEqual(toml_obj, ot.int1)
        self.assertEqual(yaml_obj, ot.int1)

    def test_float(self):
        json_obj = self.json_serializer.loads(self.json_serializer.dumps(ot.float1))
        toml_obj = self.toml_serializer.loads(self.toml_serializer.dumps(ot.float1))
        yaml_obj = self.yaml_serializer.loads(self.yaml_serializer.dumps(ot.float1))

        self.assertEqual(json_obj, ot.float1)
        self.assertEqual(toml_obj, ot.float1)
        self.assertEqual(yaml_obj, ot.float1)

    def test_bool(self):
        json_obj = self.json_serializer.loads(self.json_serializer.dumps(ot.bool1))
        toml_obj = self.toml_serializer.loads(self.toml_serializer.dumps(ot.bool1))
        yaml_obj = self.yaml_serializer.loads(self.yaml_serializer.dumps(ot.bool1))

        self.assertEqual(json_obj, ot.bool1)
        self.assertEqual(toml_obj, ot.bool1)
        self.assertEqual(yaml_obj, ot.bool1)

    def test_bytes(self):
        json_obj = self.json_serializer.loads(self.json_serializer.dumps(ot.bytes1))
        toml_obj = self.toml_serializer.loads(self.toml_serializer.dumps(ot.bytes1))
        yaml_obj = self.yaml_serializer.loads(self.yaml_serializer.dumps(ot.bytes1))

        self.assertEqual(json_obj, ot.bytes1)
        self.assertEqual(toml_obj, ot.bytes1)
        self.assertEqual(yaml_obj, ot.bytes1)

    def test_bytearray(self):
        json_obj = self.json_serializer.loads(self.json_serializer.dumps(ot.bytearr1))
        toml_obj = self.toml_serializer.loads(self.toml_serializer.dumps(ot.bytearr1))
        yaml_obj = self.yaml_serializer.loads(self.yaml_serializer.dumps(ot.bytearr1))

        self.assertEqual(json_obj, ot.bytearr1)
        self.assertEqual(toml_obj, ot.bytearr1)
        self.assertEqual(yaml_obj, ot.bytearr1)

    def test_builtin(self):
        json_obj = self.json_serializer.loads(self.json_serializer.dumps(ot.builtinfunc1))
        toml_obj = self.toml_serializer.loads(self.toml_serializer.dumps(ot.builtinfunc1))
        yaml_obj = self.yaml_serializer.loads(self.yaml_serializer.dumps(ot.builtinfunc1))

        self.assertEqual(json_obj, ot.builtinfunc1)
        self.assertEqual(toml_obj, ot.builtinfunc1)
        self.assertEqual(yaml_obj, ot.builtinfunc1)

    def test_set(self):
        json_obj = self.json_serializer.loads(self.json_serializer.dumps(ot.set1))
        yaml_obj = self.yaml_serializer.loads(self.yaml_serializer.dumps(ot.set1))
        toml_obj = self.toml_serializer.loads(self.toml_serializer.dumps(ot.set1))

        self.assertEqual(json_obj, ot.set1)
        self.assertEqual(yaml_obj, ot.set1)
        self.assertEqual(toml_obj, ot.set1)

    def test_frozenset(self):
        json_obj = self.json_serializer.loads(self.json_serializer.dumps(ot.frozenset1))
        yaml_obj = self.yaml_serializer.loads(self.yaml_serializer.dumps(ot.frozenset1))
        toml_obj = self.toml_serializer.loads(self.toml_serializer.dumps(ot.frozenset1))

        self.assertEqual(json_obj, ot.frozenset1)
        self.assertEqual(yaml_obj, ot.frozenset1)
        self.assertEqual(toml_obj, ot.frozenset1)

    def test_tuple(self):
        json_obj = self.json_serializer.loads(self.json_serializer.dumps(ot.tpl1))
        yaml_obj = self.yaml_serializer.loads(self.yaml_serializer.dumps(ot.tpl1))
        toml_obj = self.toml_serializer.loads(self.toml_serializer.dumps(ot.tpl1))

        self.assertEqual(json_obj, ot.tpl1)
        self.assertEqual(yaml_obj, ot.tpl1)
        self.assertEqual(toml_obj, ot.tpl1)

    def test_list(self):
        json_obj = self.json_serializer.loads(self.json_serializer.dumps(ot.list1))
        yaml_obj = self.yaml_serializer.loads(self.yaml_serializer.dumps(ot.list1))
        toml_obj = self.toml_serializer.loads(self.toml_serializer.dumps(ot.list1))

        self.assertEqual(json_obj, ot.list1)
        self.assertEqual(yaml_obj, ot.list1)
        self.assertEqual(toml_obj, ot.list1)

    def test_simple_dicts(self):
        json_obj = self.json_serializer.loads(self.json_serializer.dumps(ot.dict1))
        yaml_obj = self.yaml_serializer.loads(self.yaml_serializer.dumps(ot.dict1))
        toml_obj = self.toml_serializer.loads(self.toml_serializer.dumps(ot.dict1))

        self.assertEqual(json_obj, ot.dict1)
        self.assertEqual(yaml_obj, ot.dict1)
        self.assertEqual(toml_obj, ot.dict1)

    def test_simple_object(self):
        json_obj = self.json_serializer.loads(self.json_serializer.dumps(ot.obj1))
        yaml_obj = self.yaml_serializer.loads(self.yaml_serializer.dumps(ot.obj1))
        toml_obj = self.toml_serializer.loads(self.toml_serializer.dumps(ot.obj1))

        self.assertEqual(json_obj.a, ot.obj1.a)
        self.assertEqual(json_obj.b, ot.obj1.b)
        self.assertEqual(yaml_obj.a, ot.obj1.a)
        self.assertEqual(yaml_obj.b, ot.obj1.b)
        self.assertEqual(toml_obj.a, ot.obj1.a)
        self.assertEqual(yaml_obj.b, ot.obj1.b)

    def test_classes(self):
        json_obj = self.json_serializer.loads(self.json_serializer.dumps(ot.MultClass))
        yaml_obj = self.yaml_serializer.loads(self.yaml_serializer.dumps(ot.MultClass))
        toml_obj = self.toml_serializer.loads(self.toml_serializer.dumps(ot.MultClass))

        self.assertEqual(json_obj.__bases__[0].__name__, ot.MultClass.__bases__[0].__name__)
        self.assertEqual(yaml_obj.__bases__[0].__name__, ot.MultClass.__bases__[0].__name__)
        self.assertEqual(toml_obj.__bases__[0].__name__, ot.MultClass.__bases__[0].__name__)
        self.assertEqual(json_obj.__bases__[1].__name__, ot.MultClass.__bases__[1].__name__)
        self.assertEqual(yaml_obj.__bases__[1].__name__, ot.MultClass.__bases__[1].__name__)
        self.assertEqual(toml_obj.__bases__[1].__name__, ot.MultClass.__bases__[1].__name__)

    def test_simple_function(self):
        json_obj = self.json_serializer.loads(self.json_serializer.dumps(ot.hello))
        yaml_obj = self.yaml_serializer.loads(self.yaml_serializer.dumps(ot.hello))
        toml_obj = self.toml_serializer.loads(self.toml_serializer.dumps(ot.hello))

        self.assertEqual(json_obj(), ot.exp_hello)
        self.assertEqual(yaml_obj(), ot.exp_hello)
        self.assertEqual(toml_obj(), ot.exp_hello)

    def test_functions_with_global_variable(self):
        json_obj = self.json_serializer.loads(self.json_serializer.dumps(ot.say_hello))
        toml_obj = self.toml_serializer.loads(self.toml_serializer.dumps(ot.say_hello))
        yaml_obj = self.yaml_serializer.loads(self.yaml_serializer.dumps(ot.say_hello))

        self.assertEqual(json_obj(), ot.exp_say_hello)
        self.assertEqual(toml_obj(), ot.exp_say_hello)
        self.assertEqual(yaml_obj(), ot.exp_say_hello)

    def test_function_with_parameters(self):
        json_obj = self.json_serializer.loads(self.json_serializer.dumps(ot.add))
        yaml_obj = self.yaml_serializer.loads(self.yaml_serializer.dumps(ot.add))
        toml_obj = self.toml_serializer.loads(self.toml_serializer.dumps(ot.add))

        self.assertEqual(json_obj(2, 3), ot.exp_add)
        self.assertEqual(yaml_obj(2, 3), ot.exp_add)
        self.assertEqual(toml_obj(2, 3), ot.exp_add)

    def test_file_io(self):
        self.json_serializer.dump(ot.add)
        self.toml_serializer.dump(ot.add)
        self.yaml_serializer.dump(ot.add)
        json_obj = self.json_serializer.load()
        toml_obj = self.toml_serializer.load()
        yaml_obj = self.yaml_serializer.load()

        self.assertEqual(json_obj(2, 3), ot.exp_add)
        self.assertEqual(toml_obj(2, 3), ot.exp_add)
        self.assertEqual(yaml_obj(2, 3), ot.exp_add)

    def test_lambda(self):
        json_obj = self.json_serializer.loads(self.json_serializer.dumps(ot.power))
        toml_obj = self.toml_serializer.loads(self.toml_serializer.dumps(ot.power))
        yaml_obj = self.yaml_serializer.loads(self.yaml_serializer.dumps(ot.power))

        self.assertEqual(json_obj(2, 3), ot.exp_power)
        self.assertEqual(toml_obj(2, 3), ot.exp_power)
        self.assertEqual(yaml_obj(2, 3), ot.exp_power)