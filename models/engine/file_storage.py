#!/usr/bin/python3
import json
from models.base_model import BaseModel

class FileStorage:
    __file_path = "file.json"
    __objects = {}
    
    def new(self, obj):
        """
        Adds a new object to the storage dictionary.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj
    
    def save(self):
        """
        Serializes __objects to the JSON file (__file_path).
        """
        obj_dict = {obj_id: obj.to_dict() for obj_id, obj in self.__objects.items()}
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
    
    def all(self, cls=None):
        """
        Returns a dictionary of all objects.
        Optionally, if a class (cls) is specified, returns only objects of that class.
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
