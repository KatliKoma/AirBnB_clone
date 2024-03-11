#!/usr/bin/python3
"""Defines the BaseModel class for the HBnB project."""
import models
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """Acts as the foundational class for the HBnB project's models."""

    def __init__(self, *args, **kwargs):
        """Constructs a new instance of BaseModel.

        Parameters:
            *args (any): Arguments without keywords, not utilized here.
            **kwargs (dict): Key-value pairs for initializing object attributes.
        """
        datetime_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if kwargs:
            for key, value in kwargs.items():
                if key in ("created_at", "updated_at"):
                    self.__dict__[key] = datetime.strptime(value, datetime_format)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def save(self):
        """Records the current time as the updated_at attribute value and saves the model."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Generates a dictionary representation of the BaseModel instance.

        This includes a '__class__' key with the object's class name.
        """
        dict_representation = self.__dict__.copy()
        dict_representation["created_at"] = self.created_at.isoformat()
        dict_representation["updated_at"] = self.updated_at.isoformat()
        dict_representation["__class__"] = self.__class__.__name__
        return dict_representation

    def __str__(self):
        """Generates the string representation of the BaseModel instance."""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
