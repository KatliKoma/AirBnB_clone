#!/usr/bin/python3
"""
This module defines the BaseModel class which serves as the base class
for all other models in our project. It includes common attributes and
methods that will be inherited by other model classes.
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """
    The BaseModel class from which future classes will be derived.
    It defines common attributes/methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a new BaseModel instance.
        Args:
            *args (unused): Arguments (unused in this implementation).
            **kwargs (dict): Key/value pairs of attributes for initialization.
        """
        if kwargs:
            self._set_attributes_from_kwargs(kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)

    def _set_attributes_from_kwargs(self, kwargs):
        """
        Set attributes for an instance
        based on a dictionary of key-value pairs.
        Args:
            kwargs (dict): A dictionary of
            key-value pairs to set as attributes.
        """
        for key, value in kwargs.items():
            if key in ['created_at', 'updated_at']:
                # Convert datetime from string to datetime object
                value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
            if key != '__class__':
                setattr(self, key, value)

    def __str__(self):
        """
        Return the string representation of the BaseModel instance.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        Updates 'updated_at' with the current datetime and saves the instance.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of the instance.
        This method will be the first piece of
        the serialization/deserialization process.
        """
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        # Convert datetime objects to strings in ISO format
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict
