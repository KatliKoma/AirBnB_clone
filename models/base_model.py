#!/usr/bin/python3
"""
Module: base_model
Contains a class that defines common attributes and methods for other classes
"""
from datetime import datetime
from models import storage
import uuid


class BaseModel:
    """Base class for other classes"""

    def __init__(self, *args, **kwargs):
        """
        Initializes the object's attributes.
        """
        if kwargs:
            date_format = '%Y-%m-%dT%H:%M:%S.%f'
            kwargs_copy = kwargs.copy()
            del kwargs_copy["__class__"]
            for key in kwargs_copy:
                if ("created_at" == key or "updated_at" == key):
                    kwargs_copy[key] = datetime.strptime(kwargs_copy[key], date_format)
            self.__dict__ = kwargs_copy
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Prints in "[<class name>] (<self.id>) <self.__dict__>" format
        """
        return ('[{}] ({}) {}'.format(
            self.__class__.__name__,
            self.id,
            self.__class__.__dict__))

    def save(self):
        """
        Updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()
        
    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__
        """

        dictionary = self.__dict__.copy()
        dictionary["__class__"] = type(self).___name__
        dictionary["created_at"] = dictionary["created_at"].isoformat()
        dictionary["updated_at"] = dictionary["updated_at"].isoformat()

    def to_json(self):
        """
        Returns a JSON containing all keys and values
        of __dict__ of the instance
        """
        my_json = self.__dict__.copy()
        my_json.update({"created_at": self.created_at.strftime(self.date_format)})
        my_json.update({"__class__": str(self.__class__.__name__)})
        if hasattr(self, "updated_at"):
            my_json.update({"updated_at": self.updated_at.strftime(self.date_format)})
        return my_json
