import uuid
from datetime import datetime


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
            self.created_at = datetime.fromisoformat(
                    kwargs.get("created_at", self.created_at.isoformat())
                    )
            self.updated_at = datetime.fromisoformat(
                    kwargs.get("updated_at", self.updated_at.isoformat())
                    )

    def __str__(self):
        """
        Returns the string representation of the BaseModel instance.
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            ", ".join([f"{key}: {value}" for key,
                       value in self.__dict__.items()])
        )

    def save(self):
        """
        Updates 'updated_at' with the current
        datetime and attempts to save to storage.
        """
        self.updated_at = datetime.now()
        try:
            models.storage.save(self)
        except AttributeError:
            print("Storage instance has no 'save' method.")
        except Exception as e:
            print(f"An error occurred while saving: {e}")

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of the instance.
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        if hasattr(self, 'created_at') else 'None'
        rdict["updated_at"] = self.updated_at.isoformat()
        if hasattr(self, 'updated_at') else 'None'
        rdict["__class__"] = self.__class__.__name__
        return rdict
