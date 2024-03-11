#!/usr/bin/python3
"""Console module."""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from shlex import split


class_names = {
    "BaseModel": BaseModel,
    "User": User,
    "Place": Place,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Review": Review
}


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print('')
        return True

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, and prints the id."""
        if not arg:
            print("** class name missing **")
            return
        try:
            args = split(arg)
            if args[0] in class_names:
                new_instance = class_names[args[0]]()
                new_instance.save()
                print(new_instance.id)
            else:
                print("** class doesn't exist **")
        except Exception as e:
            print(e)

    def do_show(self, arg):
        """Prints the string representation of an
        instance based on the class name and id."""
        args = split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in class_names:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        all_objs = storage.all()
        if key in all_objs:
            print(all_objs[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in class_names:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        all_objs = storage.all()
        if key in all_objs:
            del all_objs[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all
        instances based or not on the class name."""
        args = split(arg)
        all_objs = storage.all()
        obj_list = []
        for key, value in all_objs.items():
            if not arg or args[0] == value.__class__.__name__:
                obj_list.append(str(value))
        if not arg or args[0] in class_names:
            print(obj_list)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Updates an instance based on the class
        name and id by adding or updating attribute."""
        args = split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in class_names:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        setattr(all_objs[key], args[2], args[3].strip('"\''))
        all_objs[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
