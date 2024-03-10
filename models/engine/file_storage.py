#!/usr/bin/python3
"""
Module for managing serialization and deserialization of data
"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.city import City


class FileStorage:
    """
    FileStorage class manages storage, serialization, and deserialization of data
    """
    __file_path = "file.json"

    __objects = {}

    def save(self):
        """
        Serializes the objects dictionary into JSON format and saves it to the specified file.
        """
        all_objects = FileStorage.__objects

        object_dict = {}

        for obj_key, obj_value in all_objects.items():
            object_dict[obj_key] = obj_value.to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(object_dict, file)

    def reload(self):
        """
        Deserializes the JSON file and restores the objects dictionary.
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                try:
                    object_dict = json.load(file)

                    for key, value in object_dict.items():
                        class_name, obj_id = key.split('.')
                        cls = eval(class_name)
                        instance = cls(**value)
                        FileStorage.__objects[key] = instance
                except Exception:
                    pass

    def new(self, obj):
        """
        Adds a new object to the objects dictionary.
        """
        class_name = obj.__class__.__name__
        key = "{}.{}".format(class_name, obj.id)
        FileStorage.__objects[key] = obj

    def all(self):
        """
        Returns the objects dictionary.
        """
        return FileStorage.__objects
