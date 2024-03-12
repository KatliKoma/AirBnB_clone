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

    def do_create(self, line):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id."""
        if not line:
            print("** class name missing **")
            return
        try:
            args = shlex.split(line)
            if args[0] in HBNBCommand.class_dict:
                new_instance = HBNBCommand.class_dict[args[0]]()
                new_instance.save()
                print(new_instance.id)
            else:
                print("** class doesn't exist **")
        except Exception as e:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of
        an instance based on the class name and id."""
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] in HBNBCommand.class_dict:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in storage.all():
                    print(storage.all()[key])
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id."""
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] in HBNBCommand.class_dict:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in storage.all():
                    del storage.all()[key]
                    storage.save()
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

        def do_all(self, self):
        """
        all - show all list of json objects
        -----------------------------------------------------
        available models:
        - BaseModel
        - Amenity
        - City
        - Place
        - Review
        - User
        - State
        -----------------------------------------------------
        @ usage - > <data> <model> {ex: all BaseModel}
        """
        aux_list = []
        with open('file.json', 'r') as jsonfile:
            tmp_dictionary = loads(jsonfile.read())
        for key, value in tmp_dictionary.items():
            tmp_str = str(key + ' ' + str(value))
            aux_list.append(tmp_str)
        if len(arg) == 0:
            print(aux_list)
        else:
            if arg not in classes:
                print("** class doesn't exist **")
                return 0
            else:
                print(aux_list)
    def do_update(self, line):
        """Updates an instance based on the class
        name, id, attribute name and value."""
        args = shlex.split(line)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] in HBNBCommand.class_dict:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in storage.all():
                    if len(args) > 2:
                        if len(args) > 3:
                            setattr(storage.all()[key], args[2], args[3])
                            storage.all()[key].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def default(self, line):
        """Handle custom commands like <class name>.all()."""
        args = line.split(".")
        if len(args) > 1:
            if args[1] == "all()":
                self.do_all(args[0])



if __name__ == '__main__':
    HBNBCommand().cmdloop()
