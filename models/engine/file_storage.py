#!/usr/bin/python3
"""
<<<<<<< HEAD
Module for serializing and deserializing data
"""
=======
This module defines a FileStorage class to serialize and
deserialize instances to and from a JSON file.
"""

>>>>>>> 4c1159023a190abcac2f837c9c37b71989072777
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
<<<<<<< HEAD
    """
    FileStorage class for storing data
    """
    __file_path = "file.json"
=======
    __file_path = 'file.json'
>>>>>>> 4c1159023a190abcac2f837c9c37b71989072777
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
<<<<<<< HEAD
        """
         Sets an object in the __objects dictionary with a key of 
         <obj class name>.id.
        """
        obj_cls_name = obj.__class__.__name__
        key = "{}.{}".format(obj_cls_name, obj.id)
        FileStorage.__objects[key] = obj


    def all(self):
        """
        Returns the __objects dictionary. 
        """
        return  FileStorage.__objects


    def save(self):
        """
        Sets the __objects dictionary into 
        JSON format and saves it to the file specified by __file_path.
        """
        objs_all = FileStorage.__objects

        obj_dict = {}

        for obj in objs_all.keys():
            obj_dict[obj] = objs_all[obj].to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        Deserializes the JSON file
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                try:
                    obj_dict = json.load(file)

                    for key, value in obj_dict.items():
                        class_name, obj_id = key.split('.')

                        cls = eval(class_name)
                        instance = cls(**value)
                        FileStorage.__objects[key] = instance
                except Exception:
                    pass
=======
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
>>>>>>> 4c1159023a190abcac2f837c9c37b71989072777
