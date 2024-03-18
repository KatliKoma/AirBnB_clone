#!/usr/bin/python3
<<<<<<< HEAD
"""
<<<<<<< HEAD
Module for serializing and deserializing data
"""
=======
This module defines a FileStorage class to serialize and
deserialize instances to and from a JSON file.
"""

>>>>>>> 4c1159023a190abcac2f837c9c37b71989072777
=======
>>>>>>> f17482d4eb02993a8549bbf6fb6f63f22afbda83
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
<<<<<<< HEAD
    """
    FileStorage class for storing data
    """
    __file_path = "file.json"
=======
    __file_path = 'file.json'
>>>>>>> 4c1159023a190abcac2f837c9c37b71989072777
=======
    __file_path = "file.json"
>>>>>>> f17482d4eb02993a8549bbf6fb6f63f22afbda83
    __objects = {}

    def new(self, obj):
<<<<<<< HEAD
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
=======
        """
        Adds a new object to the storage dictionary.
        """
>>>>>>> f17482d4eb02993a8549bbf6fb6f63f22afbda83
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (__file_path).
        """
        obj_dict = {obj_id: obj.to_dict()
                    for obj_id, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """
        Deserializes the JSON file (__file_path) to __objects.
        """
        try:
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
            for obj_id, obj_data in obj_dict.items():
                class_name = obj_data["__class__"]
                # Ensure that the class exists and is imported
                self.__objects[obj_id] = eval(class_name)(**obj_data)
        except FileNotFoundError:
            pass
<<<<<<< HEAD
<<<<<<< HEAD
>>>>>>> 4c1159023a190abcac2f837c9c37b71989072777
=======
    
=======

>>>>>>> 96ecc9068ed1f3dcaa2d491984b55a9d5b0c7720
    def all(self, cls=None):
        """
        Returns a dictionary of all objects.
        Optionally, if a class (cls) is specified,
        returns only objects of that class.
        """
        if cls is None:
            return self.__objects
        else:
            class_objects = {}
            for key, obj in self.__objects.items():
                if isinstance(obj, cls):
                    class_objects[key] = obj
            return class_objects

    def get(self, cls_name, obj_id):
        """
        Retrieves one object based on its class name and id.

        Args:
            cls_name (str): The name of the class.
            obj_id (str): The unique id of the object.

        Returns:
            The matching object if found, otherwise None.
        """
        key = f"{cls_name}.{obj_id}"
        return self.__objects.get(key, None)
<<<<<<< HEAD

>>>>>>> f17482d4eb02993a8549bbf6fb6f63f22afbda83
=======
>>>>>>> 96ecc9068ed1f3dcaa2d491984b55a9d5b0c7720
