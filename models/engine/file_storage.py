#!/usr/bin/python3
"""
This module defines a FileStorage class to serialize and
deserialize instances to and from a JSON file.
"""

import json
from models.base_model import BaseModel

class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Adds obj to the __objects dictionary."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file specified by __file_path."""
        obj_dict = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects, if file exists."""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                obj_dict = json.load(f)
            for obj in obj_dict.values():
                cls_name = obj['__class__']
                del obj['__class__']
                self.new(eval(cls_name)(**obj))
        except FileNotFoundError:
            pass
