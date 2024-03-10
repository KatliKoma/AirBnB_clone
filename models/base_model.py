#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
from typing import Any, Dict
from models import storage


class BaseModel:
    ''' Base class for other classes '''

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        '''
        Initializes the BaseModel instance.

        If keyword arguments (kwargs) are provided, it checks for special keys
        like "created_at" and "updated_at". If found, it converts their string
        representations into datetime objects.

        If no keyword arguments are provided, it initializes id with a unique
        identifier, and created_at and updated_at with the current datetime.
        It also adds the new instance to the storage.
        '''
        if kwargs:
            dt_format = '%Y-%m-%dT%H:%M:%S.%f'
            kwargs_copy = kwargs.copy()
            class_name = kwargs_copy.pop('__class__', None)
            for key, value in kwargs_copy.items():
                if key in ("created_at", "updated_at"):
                    kwargs_copy[key] = datetime.strptime(value, dt_format)
            self.__dict__.update(kwargs_copy)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self) -> None:
        '''
        Updates the public instance attribute
        updated_at with the current datetime.
        Saves the instance using the storage mechanism.
        '''
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self) -> Dict[str, Any]:
        '''
        Returns a dictionary containing
        all keys and values of __dict__ of the instance.

        For datetime objects, it converts them to ISO format strings.
        '''
        serialized_data: Dict[str, Any] = {
            "__class__": self.__class__.__name__,
        }
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                serialized_data[key] = value.isoformat()
            else:
                serialized_data[key] = value
        return serialized_data
