#!/usr/bin/python3

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


class HBNBdata(cmd.Cmd):
    '''
        Command Line Class
    '''
    prompt = "(hbnb) "
    classDict = {
        "BaseModel": BaseModel,
        "User": User,
        "City": City,
        "State": State,
        "Review": Review,
        "Amenity": Amenity,
        "Place": Place
    }

    def default(self, line):
        '''
            Method that checks if the input contains dot, if false
            print the message error
        '''

        if '.' not in line:
            return cmd.Cmd.default(self, line)

    def onecmd(self, line):
        '''
        Every command given will pass for this :)
        '''
        if '.' in line and line.split(' ')[0] not in actions:
            parsed = line.split('.')
            if pre_method(parsed):
                if parsed[1] == "all()":
                    pre_all(parsed)
                elif parsed[1] == "count()":
                    pre_count(parsed)
                elif pre_parse(parsed[1])[0] == "show":
                    if pre_parse(parsed[1])[1] == '':
                        return cmd.Cmd.default(self, line)
                    else:
                        pre_show(parsed[0], pre_parse(parsed[1]))
                elif pre_parse(parsed[1])[0] == "destroy":
                    if pre_parse(parsed[1])[1] == '':
                        return cmd.Cmd.default(self, line)
                    else:
                        pre_destroy(parsed[0], pre_parse(parsed[1]))
                elif pre_parse(parsed[1])[0] == "update":
                    if pre_parse(parsed[1])[1] == '':
                        return cmd.Cmd.default(self, line)
                    else:
                        pre_update(parsed[0], pre_parse(parsed[1], True))
            else:
                return cmd.Cmd.default(self, line)

        return cmd.Cmd.onecmd(self, line)

    def do_create(self, args):
        """
        Create - Create new model of a class
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
        @ usage - > <data> <model> {ex: create BaseModel}

        """
        if len(args) < 2:
            print('** class name missing **')
        else:
            try:
                new = eval(args)()
                new.save()
                print(new.id)
            except (NameError, SyntaxError):
                print("** class doesn't exist **")
                pass

    def do_show(self, args):
        """
        show - show Python object representation of json object
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
        @ usage - > <data> <model> <id> {ex: show BaseModel 123asd1272bn28dn}
        """
        tmp_dictionary = {}
        parsed = args.split(' ')
        if parsed == ['']:
            print('** class name missing **')
        elif len(parsed) == 1:
            print('** instance id missing *')
        if len(parsed) == 2:
            instancia, instance_id = parsed[0], parsed[1]
            with open('file.json', 'r') as jsonfile:
                tmp_dictionary = loads(jsonfile.read())
            key = instancia + '.' + instance_id
            try:
                new_ins = eval(instancia)
            except Exception:
                print("** class doesn't exist **")
                return 0
            try:
                new_ins = eval(instancia)(**tmp_dictionary[key])
                print(new_ins)
            except Exception:
                print('** no instance found **')
                return 0
        else:
            pass

    def do_all(self, arg):
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

    def do_destroy(self, args):
        """
        destroy - destroy all list of json objects
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
        @ usage - > <data> <model> {ex: destroy BaseModel}
        """
        tmp_dictionary = {}
        parsed = args.split(' ')
        if parsed == ['']:
            print('** class name missing **')
        elif len(parsed) == 1:
            print('** instance id missing *')
        if len(parsed) == 2:
            instancia, instance_id = parsed[0], parsed[1]
            tmp_dictionary = models.storage.all()
            tmp_keys = list(tmp_dictionary.keys())
            key = instancia + '.' + instance_id
            if instancia not in classes:
                print("** class doesn't exist **")
                return 0

            if key not in tmp_keys:
                print('** no instance found **')
                return 0
            if key in tmp_dictionary:
                del tmp_dictionary[key]
                models.storage.save()

    def do_update(self, arg):
        'Updates an instance based on the class name and id'
        args = parse(arg)
        objects = models.storage.all()
        if not args:
            print("** class name missing **")
            return 0
        elif args[0] not in classes:
            print("** class doesn't exist **")
            return 0
        elif len(args) < 2:
            print("** instance id missing **")
            return 0
        elif len(args) < 3:
            print("** attribute name missing **")
            return 0
        elif len(args) < 4:
            print("** value missing **")
            return 0

        key = "{}.{}".format(args[0], args[1])
        try:
            objects[key].__dict__[args[2]] = args[3]
            models.storage.save()
        except Exception:
            print("** no instance found **")
            return 0

    def do_quit(self, args):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, args):
        """
        Quit command to exit the program
        """
        return True

    def emptyline(self):
        """
        Dont do any action
        """
        pass

    def do_help(self, arg):
        """Help command to display available commands."""
        if arg:
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
            print("Documented commands (type help <topic>):")
            print("=========================================")
            cmd.Cmd.do_help(self, arg)


def parse(arg):
    """
    Parse arguments and split by space
    """
    return tuple(shlex.split(arg))


if __name__ == '__main__':
    interprete = HBNBdata()
    interprete.cmdloop()
