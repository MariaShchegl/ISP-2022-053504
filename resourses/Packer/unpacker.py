import builtins
import types
import importlib
from resourses.Packer import constants

class UnPacker:

    def recover(self, obj_dict):
        try:
            rec_type = obj_dict["type"]
        except:
            return
        if rec_type in constants.primitives_str:
            if rec_type == "int":
                return int(obj_dict["data"])
            if rec_type == "float":
                return float(obj_dict["data"])
            if rec_type == "bool":
                return bool(obj_dict["data"])
            if rec_type == "str":
                return str(obj_dict["data"])

        elif rec_type in constants.collects_str:
            if rec_type == "dict":
                rec_dict = {key: self.recover(val) for key, val in obj_dict["data"].items()}
                if "type" in rec_dict.keys() and "data" in rec_dict.keys():
                    return self.recover(rec_dict["data"])
                return rec_dict

            if rec_type == "list":
                return [self.recover(elem) for elem in obj_dict["data"]]
            if rec_type == "tuple":
                rec_list = [self.recover(elem) for elem in obj_dict["data"]]
                return tuple(rec_list)
            if rec_type == "set":
                rec_list = [self.recover(elem) for elem in obj_dict["data"]]
                return set(rec_list)
            if rec_type == "frozenset":
                rec_list = [self.recover(elem) for elem in obj_dict["data"]]
                return frozenset(rec_list)

        if rec_type in constants.bytes_obj_str:
            if rec_type == "bytes":
                return bytes(obj_dict["data"])
            if rec_type == "bytearray":
                return bytearray(obj_dict["data"])

        if rec_type == "codeobject":
            rec_obj = self.recover_codeobject(self.recover(obj_dict["data"]))
            return rec_obj

        if rec_type == "class":
            rec_obj = self.recover_class(self.recover(obj_dict["data"]))
            return rec_obj

        if rec_type == "function":
            rec_obj = self.recover_func(self.recover(obj_dict["data"]))
            return rec_obj

        if rec_type == "builtinfunction":
            rec_obj = self.recover_builtinfunc(self.recover(obj_dict["data"]))
            return rec_obj

        if rec_type == "celltype":
            rec_obj = types.CellType()
            rec_obj.cell_contents = self.recover(obj_dict["data"])
            return rec_obj

        if rec_type == "instance":
            rec_obj = self.recover_instance(self.recover(obj_dict["data"]))
            return rec_obj

    def recover_class(self, obj_dict):
        rec_obj = type(obj_dict["__name__"],
                       obj_dict["__bases__"],
                       obj_dict["__dict__"])
        return rec_obj

    def recover_instance(self, obj_dict):
        class_nam = obj_dict["class"]
        rec_obj = class_nam()
        for key, attr in obj_dict["dict"].items():
            setattr(rec_obj, key, attr)
        return rec_obj

    def recover_codeobject(self, obj_dict):
        code_obj = types.CodeType(
            obj_dict["co_argcount"],
            obj_dict["co_posonlyargcount"],
            obj_dict["co_kwonlyargcount"],
            obj_dict["co_nlocals"],
            obj_dict["co_stacksize"],
            obj_dict["co_flags"],
            obj_dict["co_code"],
            obj_dict["co_consts"],
            obj_dict["co_names"],
            obj_dict["co_varnames"],
            obj_dict["co_filename"],
            obj_dict["co_name"],
            obj_dict["co_firstlineno"],
            obj_dict["co_lnotab"],
            obj_dict["co_freevars"],
            obj_dict["co_cellvars"],
        )
        return code_obj

    def recover_func(self, obj_dict):
        attrs = obj_dict["attributes"]
        rec_obj = types.FunctionType(
            code=attrs["__code__"],
            globals=obj_dict["__globals__"],
            name=attrs["__name__"],
            argdefs=attrs["__defaults__"],
            closure=attrs["__closure__"],
        )
        return rec_obj

    def recover_builtinfunc(self, obj_dict):
        builtins.__dict__[obj_dict["module"]] = importlib.import_module(obj_dict["module"])
        module = importlib.import_module(obj_dict["module"])
        rec_obj = getattr(module, obj_dict["attributes"]["__name__"])
        return rec_obj
