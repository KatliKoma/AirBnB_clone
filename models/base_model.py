#!/usr/bin/python3
"""Defines the BaseModel class for the HBnB project."""
import models
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """Acts as the foundational class for models in the HBnB project."""

    def __init__(self, *args, **kwargs):
        """Initializes a new instance of BaseModel.

        Parameters:
            *args (any): Unused positional arguments.
            **kwargs (dict): Keyword arguments to initialize object attributes.
                             If provided, it sets each key-value as an attribute,
                             except for '__class__'. Also, it converts 'created_at'
                             and 'updated_at' from strings to datetime objects.
                             If not provided, it initializes 'id', 'created_at',
                             and 'updated_at' attributes with default values.
        """
        datetime_format = "%Y-%m-%dT%H:%M:%S.%f"
        
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        value = datetime.strptime(value, datetime_format)
                    setattr(self, key, value)

    def save(self):
        """Updates 'updated_at' with the current datetime and saves the instance."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of the instance.

        This method will add a '__class__' key to the dictionary,
        representing the class name of the object.
        """
        dict_repr = self.__dict__.copy()
        dict_repr["created_at"] = self.created_at.isoformat()
        dict_repr["updated_at"] = self.updated_at.isoformat()
        dict_repr["__class__"] = self.__class__.__name__
        return dict_repr

    def __str__(self):
        """Returns the string representation of the BaseModel instance."""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
