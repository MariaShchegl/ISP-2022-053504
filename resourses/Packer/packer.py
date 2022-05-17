import inspect
from types import CodeType, FunctionType,BuiltinFunctionType, CellType
import builtins
import importlib
from resourses.Packer import constants as cs


class Packer:

    def __init__(self):
        self.mod=importlib.import_module(__name__)#  импортирm сериализатора как библиотеку


    def packed(self, obj):
        pack_to_dict = {}
        type_obj = type(obj)

        if type_obj in cs.primitives:
            if isinstance(obj, int):
                pack_to_dict["type"] = "int"
            elif isinstance(obj, float):
                pack_to_dict["type"] = "float"
            elif isinstance(obj, bool):
                pack_to_dict["type"] = "bool"
            elif isinstance(obj, str):
                pack_to_dict["type"] = "str"
                pack_to_dict["data"] = obj

        elif type_obj in cs.collects:
             
            if isinstance(obj,dict):
                pack_to_dict["type"]="dict"
                pack_to_dict["data"]={key:self.pack_obj(val) for key, val in obj.items()}
            
            else:
                if isinstance(obj, list):
                    pack_to_dict["type"] = "list"
                elif isinstance(obj, tuple):
                    pack_to_dict["type"] = "tuple"
                elif isinstance(obj, list):
                    pack_to_dict["type"] = "set"
                elif isinstance(obj, set):
                    pack_to_dict["type"] = "set"
                elif isinstance(obj, frozenset):
                    pack_to_dict["type"] = "frozenset"
                    pack_to_dict["data"] = [self.pack_obj(el) for el in obj]              

        elif type_obj in cs.bytes_obj:
            if isinstance(obj, bytes):
                pack_to_dict["type"] = "bytes"
            if isinstance(obj, bytearray): 
                pack_to_dict["type"] = "bytearray"
                pack_to_dict["data"] = [byte for byte in obj]

        elif isinstance(obj, CodeType):
            pack_to_dict["type"] = "codeobject"
            pack_to_dict["data"] = self.pack_obj(self.get_coattrs(obj))
            
        elif isinstance(obj, FunctionType):
            pack_to_dict["type"] = "function"
            pack_to_dict["data"] = self.pack_obj(self.pack_func(obj))
            
        elif isinstance(obj, BuiltinFunctionType):
            pack_to_dict["type"] = "builtinfunction"
            pack_to_dict["data"] = self.pack_obj(self.pack_builtinfunc(obj))
            
        elif isinstance(obj,CellType):
            pack_to_dict["type"] = "celltype"
            pack_to_dict["data"] = self.pack_obj(obj.cell_contents)        
    
           
        elif isinstance(obj, type):
            pack_to_dict["type"] = "class"
            pack_to_dict["data"] = self.pack_obj(self.pack_class(obj))
            
        elif self.is_class_instance(obj):
            pack_to_dict["type"] = "instance"
            pack_to_dict["data"] = self.pack_obj(self.pack_instance(obj))

        return pack_to_dict


    def packed_function(self,obj):
        pack_to_dict = {}
        attrs = {}
            
        obj_attrs = {"__name__": obj.__qualname__,
                     "__defaults__": obj.__defaults__,
                     "__closure__": obj.__closure__,
                     "__code__": obj.__code__}
        self.get_globs(obj, attrs)
        pack_to_dict["__globals__"] = attrs
        pack_to_dict["attributes"] = obj_attrs
        return pack_to_dict


    def get_globs(self, obj, globs):
        if hasattr(obj, '__code__'):
            code_obj = obj.__code__
            for constant in code_obj.co_consts:
                self.get_globs(constant, globs)
            for coname in code_obj.co_names:
                if coname in obj.__globals__.keys() and coname != obj.__name__:
                    globs[coname] = obj.__globals__[coname]
                elif coname in dir(builtins):
                    globs[coname] = getattr(builtins, coname)

    def get_coattrs(self, obj):
        co_attrs = {}
        for key in dir(obj):
            if key.startswith("co_"):
                value = obj.__getattribute__(key)
                co_attrs[key] = value
                
        return co_attrs
    
    def pack_builtinfunc(self, obj):
        pack_to_dict = {"type": "builtinfunction",
                      "module": obj.__module__,
                      "attributes": {"__name__": obj.__name__}}

        return pack_to_dict
    
    def pack_class(self, obj):
        
        pack_to_dict = {"__name__": obj.__name__,
                      "__bases__": tuple([base for base in obj.__bases__ if base is not object]),
                      "__dict__": dict(obj.__dict__)}
        
        return pack_to_dict

    def pack_instance(self, obj):
        pack_to_dict = {"class": obj.__class__,
                      "dict": obj.__dict__}

        return pack_to_dict

    def is_class_instance(self, obj):
        if not hasattr(obj, "__dict__") or inspect.isroutine(obj) \
                or inspect.isclass(obj) or inspect.ismodule(obj) \
                or not hasattr(obj, '__module__'):
            return False
        else:
            mod = importlib.import_module(obj.__module__)
            if obj.__class__.__name__ not in \
                    dict(inspect.getmembers(mod, inspect.isclass)):
                return False
            else:
                return True 


         