#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel():
    ''' a base class for other classes '''

    def __init__(self, *args, **kwargs):
        '''
        initializes the values
        '''
        if kwargs:
            dtf = '%Y-%m-%dT%H:%M:%S.%f'
            k_dict = kwargs.copy()
            del k_dict["__class__"]
            for key in k_dict:
                if ("created_at" == key or "updated_at" == key):
                    k_dict[key] = datetime.strptime(k_dict[key], dtf)
            self.__dict__ = k_dict
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        '''
        updates the public instance attribute updated_at
        with the current datetime
        '''
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        '''
        returns a dictionary containing all keysvalues
        of __dict__ of the instance
        '''
        dic = {}
        dic["__class__"] = self.__class__.__name__
        for k, v in self.__dict__.items():
            if isinstance(v, (datetime, )):
                dic[k] = v.isoformat()
            else:
                dic[k] = v
        return dic
