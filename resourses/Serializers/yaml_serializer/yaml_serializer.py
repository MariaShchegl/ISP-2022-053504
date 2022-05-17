from serializer.pack_recover import pack_obj, recover_obj
from io import StringIO
import yaml


class YamlSerializer:
    def __init__(self, path: str):
        self.path = path
        self.packer = pack_obj.PackObj()
        self.recover = recover_obj.RecoverObj()

    def dump(self, obj: object):
        packed_obj = self.packer.pack_obj(obj)
        with open(self.path, "w") as file:
            yaml.safe_dump(packed_obj, file)

    def dumps(self, obj: object):
        packed_obj = self.packer.pack_obj(obj)
        result_string = yaml.safe_dump(packed_obj)
        return result_string

    def load(self):
        rec_obj = {}
        with open(self.path, "r") as file:
            rec_obj = yaml.safe_load(file)
        obj = self.recover.recover(rec_obj)
        return obj

    def loads(self, obj_str: str):
        str_stream = StringIO(obj_str)
        rec_obj = yaml.safe_load(str_stream)
        obj = self.recover.recover(rec_obj)
        return obj
