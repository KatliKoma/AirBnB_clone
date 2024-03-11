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
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())  # Generate a unique ID for each new instance.
        self.created_at = datetime.utcnow()  # Record the time of creation.
        self.updated_at = datetime.utcnow()  # Set the time of last update to now.
        
        # Check if 'kwargs' was provided to set instance attributes.
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue  # Skip the '__class__' key.
                elif key in ("created_at", "updated_at"):
                    # Convert string datetime to a datetime object.
                    setattr(self, key, datetime.strptime(value, time_format))
                else:
                    # Set other attributes directly.
                    setattr(self, key, value)

        # Register the new instance with the storage mechanism.
        models.storage.new(self)

    def save(self):
        """
        Updates 'updated_at' with the current time and signals the storage mechanism to save the instance.
        """
        self.updated_at = datetime.utcnow()  # Update the time of last update.
        models.storage.save()  # Save the instance.

    def to_dict(self):
        """
        Returns a dictionary representation of the instance, including the instance's class name
        and converting 'created_at' and 'updated_at' to string format.
        """
        inst_dict = self.__dict__.copy()  # Create a copy of the instance's dictionary.
        inst_dict["__class__"] = self.__class__.__name__  # Add the class name.
        # Convert 'created_at' and 'updated_at' to ISO format strings.
        inst_dict["created_at"] = self.created_at.isoformat()
        inst_dict["updated_at"] = self.updated_at.isoformat()

        return inst_dict  # Return the modified dictionary.

    def __str__(self):
        """
        Returns a string representation of the instance, including the class name, id, and attributes.
        """
        class_name = self.__class__.__name__  # Get the name of the class.
        # Format the string representation.
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

# Example code to demonstrate how to use the BaseModel class.
if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My_First_Model"
    my_model.my_number = 89
    print(my_model.id)
    print(my_model)
    print(type(my_model.created_at))
    print("--")
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

    print("--")
    my_new_model = BaseModel(**my_model_json)
    print(my_new_model.id)
    print(my_new_model)
    print(type(my_new_model.created_at))

    print("--")
    print(my_model is my_new_model)
