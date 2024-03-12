#!/usr/bin/python3
"""Console module for the HBNB project."""

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import shlex  # For splitting the command line input

class HBNBCommand(cmd.Cmd):
    """HBNB command interpreter."""
    prompt = '(hbnb) '
    
    # Mapping class names to class types
    class_dict = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review,
    }

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print()
        return True

    def emptyline(self):
        """Do nothing on an empty line."""
        pass

    # The methods do_create, do_show, do_destroy, do_all, do_update, and default
    # are already well-implemented in your script to handle the respective commands.

if __name__ == '__main__':
    HBNBCommand().cmdloop()
