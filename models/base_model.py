#!/usr/bin/python3
"""
Contains the BaseModel class
"""

import uuid
from datetime import datetime
import models

class BaseModel:
    """
    The BaseModel class from which future classes will be derived
    """

    def __init__(self, *args, **kwargs):
        """
        Initialization of the base model
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        String representation of the BaseModel class
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the attribute 'updated_at' with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of the instance
        """
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = my_dict['created_at'].isoformat()
        my_dict['updated_at'] = my_dict['updated_at'].isoformat()
        return my_dict
