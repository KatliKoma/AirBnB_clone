#!/usr/bin/python3
"""
This module defines the BaseModel class.
"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance."""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Return the string representation of the BaseModel instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update updated_at with the current
        datetime and save the instance."""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return a dictionary containing all keys/values of the instance."""
        my_dict = dict(self.__dict__)
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict
