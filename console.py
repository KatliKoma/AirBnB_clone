#!/usr/bin/python3
"""Defines the HBnB console."""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse(arg):
    """Parse command arguments."""
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter."""
    
    prompt = "(hbnb) "
    __classes = {"BaseModel", "User", "State", "City", "Place", "Amenity", "Review"}

    def do_quit(self, arg):
        """Quit command to exit the program."""
        print("Exiting the program.")
        return True  # Returning True exits the cmdloop

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print("Exiting the program.")
        return True  # Returning True exits the cmdloop

    def emptyline(self):
        """An empty line + ENTER or an empty line + spaces + ENTER shouldn’t execute anything."""
        pass  # Do nothing

    def do_help(self, arg):
        """Help command to display available commands."""
        if arg:
            # Check if there's a specific command to provide help for
            try:
                func = getattr(self, 'do_' + arg)
            except AttributeError:
                print(f"No help on {arg}")
                return
            doc = func.__doc__
            if doc:
                print(doc)
            else:
                print(f"No help on {arg}")
        else:
            # List available commands
            print("Documented commands (type help <topic>):")
            print("=========================================")
            cmd.Cmd.do_help(self, arg)

    # Additional command methods can be added here


if __name__ == "__main__":
    HBNBCommand().cmdloop()
