from serializer.ser_factory import ser_factory


class Serializer:
    def __init__(self, path="", ser_nam='json'):
        self._path = path
        self.ser_name = ser_nam
        self.factory = ser_factory.SerFactory(self._path)
        self.serializer = self.factory.create_serializer(self.ser_name)

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, path):
        self._path = path
        self.factory = ser_factory.SerFactory(self._path)

    @property
    def ser_nam(self):
        return self.ser_name

    @ser_nam.setter
    def ser_nam(self, ser_nam):
        self.ser_name = ser_nam
        self.serializer = self.factory.create_serializer(self.ser_name)

    def dump(self, obj):
        self.serializer.dump(obj)

    def dumps(self, obj):
        return self.serializer.dumps(obj)

    def load(self):
        return self.serializer.load()

    def loads(self, obj_str):
        return self.serializer.loads(obj_str)