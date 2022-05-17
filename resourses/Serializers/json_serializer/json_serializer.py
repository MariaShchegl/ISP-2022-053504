from resourses.Packer import packer, unpacker
from Serializers.json_serializer.json_serializer import json_pars as json


class JsonSerializer:
    def __init__(self, path: str):
        self.path = path
        self.packer = packer.Packer()
        self.recover = unpacker.UnPacker()

    def dump(self, obj: object):
        packed_obj = self.packer.pack_to_object(obj)
        with open(self.path, "w") as file:
            json.dump(packed_obj, fp=file)

    def dumps(self, obj: object):
        packed_obj = self.packer.pack_obj(obj)
        result_string = json.dumps(packed_obj)
        return result_string

    def load(self):
        rec_obj = {}
        with open(self.path, "r") as file:
            rec_obj = json.load(file)
        obj = self.recover.recover(rec_obj)
        return obj

    def loads(self, obj_str: str):
        rec_obj = json.loads(obj_str)
        obj = self.recover.recover(rec_obj)
        return obj
