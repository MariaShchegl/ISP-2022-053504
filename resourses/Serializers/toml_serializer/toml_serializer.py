from serializer.pack_recover import pack_obj, recover_obj
import pytoml as toml


class TomlSerializer:
    def __init__(self, path: str):
        self.path = path
        self.packer = pack_obj.PackObj()
        self.recover = recover_obj.RecoverObj()

    def dump(self, obj: object):
        packed_obj = self.packer.pack_obj(obj)
        with open(self.path, "w") as file:
            toml.dump(packed_obj, file)

    def dumps(self, obj: object):
        rec_obj = self.packer.pack_obj(obj)
        result_string = toml.dumps(rec_obj)
        return result_string

    def load(self):
        rec_obj = {}
        with open(self.path, "r") as file:
            rec_obj = toml.load(file)
        obj = self.recover.recover(rec_obj)
        return obj

    def loads(self, obj_str: str):
        packed_obj = toml.loads(obj_str)
        obj = self.recover.recover(packed_obj)
        return obj
