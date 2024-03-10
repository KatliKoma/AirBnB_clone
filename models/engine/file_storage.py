#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Defines a storage system for serializing and deserializing instances.

    Attributes:
        __file_path (str): Path to the file where objects are stored.
        __objects (dict): Dictionary storing all objects by <class name>.<id>.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary of stored objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Adds an object to the storage dictionary."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Converts the dictionary of objects to a JSON file."""
        with open(FileStorage.__file_path, 'w') as f:
            json.dump({key: obj.to_dict() for key, obj in FileStorage.__objects.items()}, f)

    def reload(self):
        """Loads the JSON file to the objects dictionary, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                objects = json.load(f)
                for obj_data in objects.values():
                    class_name = obj_data["__class__"]
                    del obj_data["__class__"]
                    self.new(eval(class_name)(**obj_data))
        except FileNotFoundError:
            pass
