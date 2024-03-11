#!/usr/bin/python3
"""
console.py module
"""
import cmd
import shlex
import ast
import models
from models.base_model import BaseModel
# Note: no need to import FileStorage if __objects is called
# from models.storage
# Reminder: models.storage is the instance of FileStorage
# from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    defines the "entry point of the command interpreter"
    """

    prompt = '(hbnb) '
    className = {'BaseModel': BaseModel,
                 'User': User,
                 'State': State,
                 'City': City,
                 'Amenity': Amenity,
                 'Place': Place,
                 'Review': Review}

    def do_create(self, arg):

        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.className.keys():
            print("** class doesn't exist **")
        else:
            obj = HBNBCommand.className[arg]()
            HBNBCommand.className[arg].save(obj)
            print(obj.id)

    def do_show(self, arg):

        if not arg:
            print("** class name missing **")
            return
        args = shlex.split(arg)
        if args[0] not in HBNBCommand.className.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0]+'.'+args[1] not in models.storage\
                                              ._FileStorage__objects.keys():
            print("** no instance found **")
        else:
            print(models.storage._FileStorage__objects[args[0]+'.'+args[1]])

    def do_destroy(self, arg):

        if not arg:
            print("** class name missing **")
            return
        args = shlex.split(arg)
        if args[0] not in HBNBCommand.className.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0]+'.'+args[1] not in models.storage\
                                              ._FileStorage__objects.keys():
            print("** no instance found **")
        else:
            del models.storage._FileStorage__objects[args[0]+'.'+args[1]]
            models.storage.save()

    def do_all(self, arg):

        if not arg:
            list_objs = []
            for key, obj in models.storage._FileStorage__objects.items():
                list_objs.append(str(obj))
            if len(list_objs) > 0:
                print(list_objs)
        else:
            if arg not in HBNBCommand.className.keys():
                print("** class doesn't exist **")
            else:
                list_objs = []
                for key, obj in models.storage._FileStorage__objects.items():
                    if arg == key.split('.')[0]:
                        list_objs.append(str(obj))
                if len(list_objs) > 0:
                    print(list_objs)

    def default(self, arg):
        """Default command that handles class cmds: <class name>.func()"""

        args = arg.split('.', 1)

        if args[0] in HBNBCommand.className.keys():
            if args[1].strip('()') == 'all':
                self.do_all(args[0])
            elif args[1].strip('()') == 'count':
                self.obj_count(args[0])
            elif args[1].split('(')[0] == 'show':
                self.do_show(args[0]+' '+args[1].split('(')[1].strip(')'))
            elif args[1].split('(')[0] == 'destroy':
                self.do_destroy(args[0]+' '+args[1].split('(')[1].strip(')'))
            elif args[1].split('(')[0] == 'update':
                arg0 = args[0]
                if ', ' not in args[1]:
                    arg1 = args[1].split('(')[1].strip(')')
                    self.do_update(arg0+' '+arg1)
                elif ', ' in args[1] and\
                     '{' in args[1] and ':' in args[1]:
                    arg1 = args[1].split('(')[1].strip(')').split(', ', 1)[0]
                    attr_dict = ast.literal_eval(args[1].split('(')[1]
                                                 .strip(')').split(', ', 1)[1])

                    for key, value in attr_dict.items():
                        self.do_update(arg0+' '+arg1+' '+key+' '+str(value))
                elif ', ' in args[1] and\
                     len(args[1].split('(')[1].strip(')').split(', ')) == 2:
                    arg1 = args[1].split('(')[1].strip(')').split(', ')[0]
                    arg2 = args[1].split('(')[1].strip(')').split(', ')[1]
                    self.do_update(arg0+' '+arg1+' '+arg2)
                elif ', ' in args[1] and\
                     len(args[1].split('(')[1].strip(')').split(', ')) >= 3:
                    print(args[1])
                    arg1 = args[1].split('(')[1].strip(')').split(', ')[0]
                    print(arg1)
                    arg2 = args[1].split('(')[1].strip(')').split(', ')[1]
                    print(arg2)
                    arg3 = args[1].split('(')[1].strip(')').split(', ')[2]
                    print(arg3)
                    self.do_update(arg0+' '+arg1+' '+arg2+' '+arg3)
            else:
                print('*** Unknown syntax: {}'.format(arg))
        else:
            print("** class doesn't exist **")

    @staticmethod
    def obj_count(arg):

        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.className.keys():
            print("** class doesn't exist **")
        else:
            counter = 0
            for key, obj in models.storage._FileStorage__objects.items():
                if arg == key.split('.')[0]:
                    counter += 1
            print(counter)

    def do_update(self, arg):

        if not arg:
            print("** class name missing **")
            return
        args = shlex.split(arg)

        if args[0] not in HBNBCommand.className.keys():
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif args[0]+'.'+args[1] not in models.storage\
                                              ._FileStorage__objects.keys():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            obj = models.storage._FileStorage__objects[args[0]+'.'+args[1]]
            if args[2] in obj.__dict__.keys():
                try:
                    if args[3].isdigit():
                        args[3] = int(args[3])
                    elif args[3].replace('.', '', 1).isdigit():
                        args[3] = float(args[3])
                except AttributeError:
                    pass
                setattr(obj, args[2], args[3])
            else:
                try:
                    if args[3].isdigit():
                        args[3] = int(args[3])
                    elif args[3].replace('.', '', 1).isdigit():
                        args[3] = float(args[3])
                except AttributeError:
                    pass
                setattr(obj, args[2], args[3])
            HBNBCommand.className[args[0]].save(obj)

    def do_quit(self, arg):

        return True

    def do_EOF(self, arg):

        return True

    def emptyline(self):

        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
