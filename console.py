#!/usr/bin/python3
"""Command interpreter for the AirBnB clone project"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = "(hbnb) "

    def do_create(self, arg):
        """Creates a new instance of BaseModel"""
        if not arg:
            print("** class name missing **")
            return

        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        if not arg:
            print("** class name missing **")
            return

        try:
            class_name, instance_id = arg.split()
            objects = storage.all()
            key = class_name + "." + instance_id
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")
        except ValueError:
            print("** instance id missing **")
        except KeyError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return

        try:
            class_name, instance_id = arg.split()
            objects = storage.all()
            key = class_name + "." + instance_id
            if key in objects:
                del objects[key]
                storage.save()
            else:
                print("** no instance found **")
        except ValueError:
            print("** instance id missing **")
        except KeyError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Prints all string representations of all instances"""
        objects = storage.all()
        if arg:
            try:
                objects_list = [str(objects[obj]) for obj in objects if type(objects[obj]).__name__ == arg]
                print(objects_list)
                return
            except NameError:
                print("** class doesn't exist **")

        objects_list = [str(objects[obj]) for obj in objects]
        print(objects_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return

        try:
            args = arg.split()
            class_name = args[0]
            instance_id = args[1]
            attribute_name = args[2]
            attribute_value = args[3]
            objects = storage.all()
            key = class_name + "." + instance_id
            if key not in objects:
                print("** no instance found **")
                return

            instance = objects[key]
            setattr(instance, attribute_name, attribute_value)
            instance.save()
        except ValueError:
            print("** instance id missing **")
        except IndexError:
            print("** attribute name missing **")
        except KeyError:
            print("** class doesn't exist **")
        except AttributeError:
            print("** value missing **")

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
