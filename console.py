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
    """Parse the arguments string to a list."""
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if not curly_braces:
        if not brackets:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            ret_list = [i.strip(",") for i in lexer]
            ret_list.append(brackets.group())
            return ret_list
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        ret_list = [i.strip(",") for i in lexer]
        ret_list.append(curly_braces.group())
        return ret_list

class HBNBCommand(cmd.Cmd):
    """HolbertonBnB command interpreter.

    Attributes:
        prompt (str): The command prompt string.
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
        """Overrides the empty line behavior to do nothing."""
        pass

    def default(self, arg):
        """Fallback method for unrecognized commands."""
        cmd_map = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match:
            args_list = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", args_list[1])
            if match:
                command = [args_list[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in cmd_map:
                    call = "{} {}".format(args_list[0], command[1])
                    return cmd_map[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Exits the console."""
        return True

    def do_EOF(self, arg):
        """Exits the console on EOF signal."""
        print("")
        return True

    def do_create(self, arg):
        """Creates a new instance of a given class and prints its id."""
        args_list = parse(arg)
        if not args_list:
            print("** class name missing **")
        elif args_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(args_list[0])().id)
            storage.save()

    def do_show(self, arg):
        """Displays the string representation of an instance based on its class and id."""
        args_list = parse(arg)
        obj_dict = storage.all()
        if not args_list:
            print("** class name missing **")
        elif args_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args_list) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args_list[0], args_list[1]) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(args_list[0], args_list[1])])

    def do_destroy(self, arg):
        """Deletes an instance based on its class name and id."""
        args_list = parse(arg)
        obj_dict = storage.all()
        if not args_list:
            print("** class name missing **")
        elif args_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args_list) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args_list[0], args_list[1]) not in obj_dict.keys():
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(args_list[0], args_list[1])]
            storage.save()

    def do_all(self, arg):
        """Displays all instances of a given class, or if no class is specified, all objects."""
        args_list = parse(arg)
        if args_list and args_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            obj_list = []
            for obj in storage.all().values():
                if args_list and args_list[0] == obj.__class__.__name__:
                    obj_list.append(obj.__str__())
                elif not args_list:
                    obj_list.append(obj.__str__())
            print(obj_list)

    def do_count(self, arg):
        """Counts the number of instances of a given class."""
        args_list = parse(arg)
        count = 0
        for obj in storage.all().values():
            if args_list[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute."""
        args_list = parse(arg)
        obj_dict = storage.all()

        if not args_list:
            print("** class name missing **")
            return False
        if args_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(args_list) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(args_list[0], args_list[1]) not in obj_dict.keys():
            print("** no instance found **")
            return False
        if len(args_list) == 2:
            print("** attribute name missing **")
            return False
        if len(args_list) == 3:
            print("** value missing **")
            return False

        obj = obj_dict["{}.{}".format(args_list[0], args_list[1])]
        if len(args_list) == 4:
            setattr(obj, args_list[2], eval(args_list[3]))
        elif type(eval(args_list[3])) == dict:
            for k, v in eval(args_list[3]).items():
                setattr(obj, k, v)
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
