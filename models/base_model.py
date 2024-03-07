#!/usr/bin/python3
"""This script serves as a base model"""

import uuid

class BaseModel:

    """Parent class from which other classes will inherit"""

    def __init__(self, *args, **kwargs):
        """Sets up the instance attributes

        Args:
        - **kwargs: dictionary of keyword arguments
        - * args: list or arguments
        """

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.str_time(
                            kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "update_at":
                    self.__dict__["updated_at"] = datetime.str_time(
                            kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
            else:
                self.id = str(uuid.uuid4())
                self.created_at = datetime.now()
                self.updated_at = datetime.now()
                storage.new(self)

                def save(self):
                    """Updates the 'updated_at' attribute of the instance"""
                    
                    self.updated_at = datetime.now()

                def __str__(self):
                    """Returns the official string representation"""

                def to_dict(self):
                    """Returns dict containing key-value pairs stored in the instance."""
                    my_dict["created_at"] = my_dict["created_at"].isoformat()
                    my_dict["updated_at"] = my_dict["updated_at"].isoformat()
                    return my_dict
