#!/usr/bin/python3
"""
This script defines the BaseModel class, the foundational class for all models in our project.
"""
import uuid
from datetime import datetime
import models

class BaseModel:
    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.
        If 'kwargs' is provided, it populates the instance with the key-value pairs in 'kwargs',
        converting 'created_at' and 'updated_at' to datetime objects if necessary.
        Otherwise, it sets default values for 'id', 'created_at', and 'updated_at'.
        """

def __init__(self, *args, **kwargs) -> None:

        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    pass
                elif key != "created_at" and key != "updated_at":
                    self.__dict__[key] = value
                else:
                    self.__dict__[key] = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
        else:
            models.storage.new(self)

    def __str__(self) -> str:
        """[Changing the str method expected output to :
        [<class name>] (<self.id>) <self.__dict__>]

        Returns:
            str: [description with the information changed]
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """[Function that updates the update_date]
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """[Function that returns an specific information about the class
        in a dict]

        Returns:
            [dict]: [The atttributes with the format required]
        """
        copy = self.__dict__.copy()
        copy["__class__"] = self.__class__.__name__
        copy["created_at"] = self.created_at.isoformat()
        copy["updated_at"] = self.updated_at.isoformat()
        return copy
