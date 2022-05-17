"""Класс содержит метод для создания нового сериализатора."""
from serializers import json_serializer as js
from serializers import toml_serializer as ts
from serializers import yaml_serializer as ys
 
 
"""Класс для создания нового сериализатора."""
class SerFactory:
    def __init__(self, path: str):
        self.path = path

    def create_serializer(self, extension="json"):
        if extension.lower() == "json":
            return js.JsonSerializer(self.path) # названия других методов
        elif extension.lower() == "toml":
            return ts.TomlSerializer(self.path)
        elif extension.lower() == "yaml":
            return ys.YamlSerializer(self.path)

