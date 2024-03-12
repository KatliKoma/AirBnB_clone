#!/usr/bin/python3
import uuid
from datetime import datetime
import models


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
        self.id = str(uuid.uuid4())
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, time_format))
                else:
                    setattr(self, key, value)

        models.storage.new(self)

    def __str__(self):
        """ """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)


if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My_First_Model"
    my_model.my_number = 89
    print(my_model.id)
    print(my_model)
    print(type(my_model.created_at))
    print("__")
    my_json_model = my_model.to_dict()
    print(my_json_model)
    print("JSON of m_model:")
    for key inmy_json_model.keys():
        print("\t{}: ({}) - {}".format(key, type(my_json_model[key]))

        print("--")
        new_model = BaseModel(**my_json_model)
        print(new_model.id)
        print(type(new_model.created_at))

        print("--")
        print(my_model is new_model)

    def save(self):
        """
        method that updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all
        keys/values of __dict__
        """
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updatet_at.isoformat()

        return dictionary
