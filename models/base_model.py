#!/usr/bin/python3
"""Defines the BaseModel class for HBnB (Holberton BnB) project."""

import uuid
from datetime import datetime
import models

class BaseModel:
    """Represents a base model with common attributes and methods for HBnB project."""

    def __init__(self, *args, **kwargs):
        """
        Initializes a new BaseModel instance.
        
        Attributes are set with the current datetime if not provided via kwargs.
        The id attribute is assigned a unique UUID string value.
        If kwargs is provided, it overrides default attributes except for __class__.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key in ("created_at", "updated_at"):
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        else:
            models.storage.new(self)

    def __str__(self):
        """Returns a string representation of the BaseModel instance."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the updated_at attribute to the current datetime."""
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of the instance.
        
        Adds the class name with the key '__class__'.
        Formats created_at and updated_at to ISO format strings.
        """
        dict_rep = self.__dict__.copy()
        dict_rep["__class__"] = self.__class__.__name__
        dict_rep["created_at"] = self.created_at.isoformat()
        dict_rep["updated_at"] = self.updated_at.isoformat()
        return dict_rep
