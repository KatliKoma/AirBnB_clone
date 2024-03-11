#!/usr/bin/python3
import uuid
from datetime import datetime
import models
from collections import OrderedDict

def time_conversor(obj):
    """ Define time conversor
        that return new time object
    """
    if type(obj) in [datetime]:
        obj = obj.strftime('%Y-%m-%dT%H:%M:%S.%f')
    return datetime.strptime(obj, "%Y-%m-%dT%H:%M:%S.%f")

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
        self.__dict__.update({
            "created_at": time_conversor(self.created_at),
            "updated_at": time_conversor(self.updated_at),
        })
        return "[{:s}] ({:s}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def __repr__(self):
        """ Define method repr that return
            string representation
        """
        return "[{:s}] ({:s}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)


    def save(self):
        """
        method that updates the public instance attribute updated_at
        with the current datetime
         """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of the instance."""
        dictionary = OrderedDict()
        dictionary['my_number'] = self.my_number if hasattr(self, 'my_number') else 0
        dictionary['name'] = self.name if hasattr(self, 'name') else ""
        dictionary['__class__'] = self.__class__.__name__
        dictionary['updated_at'] = self.updated_at.isoformat()
        dictionary['id'] = self.id
        dictionary['created_at'] = self.created_at.isoformat()
        return dictionary
