#!/usr/bin/python3
"""
Console module for AirBnB clone project.
"""

import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    classes = {
        "BaseModel": BaseModel,

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

    def do_create(self, arg):
        """Creates a new instance of BaseModel,
        saves it to the JSON file, and prints the ID."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        obj = self.classes[args[0]]()
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        """Shows the details of a specific
        instance of a class based on its ID."""
        args = arg.split()
        if len(args) < 2:
            print("** class name missing **"
                  if len(args) == 0 else "** instance id missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        obj = storage.get(args[0], args[1])
        if obj:
            print(obj)
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representations of
        all instances based or not on the class name."""
        args = arg.split()
        if len(args) > 0 and args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        all_objs = storage.all()
        for obj_id, obj in all_objs.items():
            if not args or obj.__class__.__name__ == args[0]:
                print(obj)

    def do_update(self, arg):
        """Updates an instance based on the class
        name and id by adding or updating attribute."""
        args = arg.split(" ")
        if len(args) < 4:
            print("** class name missing **" if len(args) == 0 else
                  "** instance id missing **" if len(args) == 1 else
                  "** attribute name missing **" if len(args) == 2 else
                  "** value missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        obj_id = args[1]
        attribute_name = args[2]
        value = args[3].strip('"')

        try:
            value = int(value)
        except ValueError:
            try:
                value = float(value)
            except ValueError:
                pass

        obj = storage.get(args[0], obj_id)
        if not obj:
            print("** no instance found **")
            return

        setattr(obj, attribute_name, value)
        obj.save()

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = arg.split()
        if len(args) < 2:
            print("** class name missing **"
                  if len(args) == 0 else "** instance id missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        key = f"{args[0]}.{args[1]}"
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_count(self, cls_name):
        """Counts the number of instances of a class."""
        count = 0
        for obj in storage.all().values():
            if obj.__class__.__name__ == cls_name:
                count += 1
        print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
