#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    intro = '(hbnb) '
    prompt = '(hbnb) '
    file = None

    def do_EOF(self, arg):
        'Exit the command shell'
        return True

    def do_quit(self, arg):
        'Quit the command shell'
        return True

    def do_help(self, arg):
        'List available commands with "help" or detailed help with "help cmd"'
        super().do_help(arg)

    def emptyline(self):
        'Do nothing on empty input line'
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
