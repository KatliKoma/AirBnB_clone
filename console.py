#!/usr/bin/python3
import cmd
from models import storage
from models.base_model import BaseModel
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    classes = {
        "BaseModel": BaseModel,
        "Place": Place,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Review": Review
    }

    def do_create(self, arg):
        args = arg.split()
        if not arg:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        obj = self.classes[args[0]]()
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        all_objs = storage.all(self.classes[args[0]])
        key = f"{args[0]}.{args[1]}"
        if key in all_objs:
            print(all_objs[key])
        else:
            print("** no instance found **")

    # Implement do_all, do_destroy, and do_update similarly, checking for class existence and handling errors appropriately.

if __name__ == '__main__':
    HBNBCommand().cmdloop()
