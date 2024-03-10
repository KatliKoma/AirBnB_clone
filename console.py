#!/usr/bin/python3
"""This script defines the HolbertonBnB command-line console."""

# Import necessary libraries and modules
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
    # Parse arguments to handle different types of inputs like curly braces or brackets
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            return [i.strip(",") for i in lexer] + [brackets.group()]
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        return [i.strip(",") for i in lexer] + [curly_braces.group()]

class HBNBCommand(cmd.Cmd):
    """Implements the command interpreter for the HolbertonBnB console.

    Attributes:
        prompt (str): The command-line prompt text.
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """Handles the case of an empty input line."""
        pass

    def default(self, arg):
        """Specifies the default action for unrecognized commands."""
        command_mapping = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match:
            arg_list = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", arg_list[1])
            if match:
                command = [arg_list[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in command_mapping:
                    call = "{} {}".format(arg_list[0], command[1])
                    return command_mapping[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Exits the console when 'quit' command is issued."""
        return True

    def do_EOF(self, arg):
        """Ends the console session when an EOF signal is received."""
        print("")
        return True

    def do_create(self, arg):
        """Creates a new instance of a specified class and prints its ID."""
        arg_list = parse(arg)
        if not arg_list:
            print("** class name missing **")
        elif arg_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(arg_list[0])().id)
            storage.save()

    def do_show(self, arg):
        """Displays the details of a specific class instance given its ID."""
        arg_list = parse(arg)
        all_objects = storage.all()
        if not arg_list:
            print("** class name missing **")
        elif arg_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_list[0], arg_list[1]) not in all_objects:
            print("** no instance found **")
        else:
            print(all_objects["{}.{}".format(arg_list[0], arg_list[1])])

    def do_destroy(self, arg):
        """Deletes a class instance specified by its ID."""
        arg_list = parse(arg)
        all_objects = storage.all()
        if not arg_list:
            print("** class name missing **")
        elif arg_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_list[0], arg_list[1]) not in all_objects.keys():
            print("** no instance found **")
        else:
            del all_objects["{}.{}".format(arg_list[0], arg_list[1])]
            storage.save()

    def do_all(self, arg):
        """Displays all instances of a class, or all instances if no class is specified."""
        arg_list = parse(arg)
        if arg_list and arg_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            instances_list = [str(obj) for obj in storage.all().values() if not arg_list or obj.__class__.__name__ == arg_list[0]]
            print(instances_list)

    def do_count(self, arg):
        """Counts the number of instances of a specified class."""
        arg_list = parse(arg)
        count = sum(1 for obj in storage.all().values() if obj.__class__.__name__ == arg_list[0])
        print(count)

    def do_update(self, arg):
        """Updates an instance based on class name and ID by adding or updating attribute (key/value)."""
        arg_list = parse(arg)
        all_objects = storage.all()

        if not arg_list:
            print("** class name missing **")
            return False
        if arg_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(arg_list) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(arg_list[0], arg_list[1]) not in all_objects.keys():
            print("** no instance found **")
            return False
        if len(arg_list) == 2:
            print("** attribute name missing **")
            return False
        if len(arg_list) == 3:
            try:
                assert type(eval(arg_list[2])) != dict  # Ensure it's not a dictionary
            except NameError:
                print("** value missing **")
                return False

        # Update logic for both direct attributes and dictionary updates
        obj = all_objects["{}.{}".format(arg_list[0], arg_list[1])]
        if len(arg_list) == 4:
            setattr(obj, arg_list[2], eval(arg_list[3]) if arg_list[2] in obj.__class__.__dict__ else arg_list[3])
        elif isinstance(eval(arg_list[2]), dict):
            for k, v in eval(arg_list[2]).items():
                setattr(obj, k, eval(v) if k in obj.__class__.__dict__ else v)
        storage.save()
