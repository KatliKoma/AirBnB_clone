#!/usr/bin/python3
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    Defines all common attributes/methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of BaseModel.
        """
        self.id = str(uuid.uuid4())
        self.created_at = self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    setattr(self, key, value)
            if 'created_at' in kwargs:
                self.created_at = datetime.fromisoformat(kwargs['created_at'])
            if 'updated_at' in kwargs:
                self.updated_at = datetime.fromisoformat(kwargs['updated_at'])

        def __str__(self):
            return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """
        method that updates the public instance attribute updated_at
        with the current datetime
         """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        dictionary = self.__dict__.copy()
        dictionary['__class__'] = self.__class__.__name__
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
