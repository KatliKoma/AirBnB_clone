#!/usr/bin/ppython3
import json
from models.base_model import BaseModel

class FileStorage:
    """Class for serializing and deserializing instances to/from JSON file"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(new_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as f:
                objects_dict = json.load(f)
                for key, value in objects_dict.items():
                    class_name, obj_id = key.split(".")
                    self.__objects[key] = eval(class_name)(**value)
        except FileNotFoundError:
            pass
