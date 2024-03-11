#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    """A command interpreter for AirBnB clone."""

    prompt = '(hbnb) ' # Custom prompt

    def do_quit(self, arg):
        """Quit command to exit the program."""
        print("Exiting the program.")
        return True # Returning True exits the cmdloop

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print("Exiting the program.")
        return True # Returning True exits the cmdloop

    def emptyline(self):
        """An empty line + ENTER shouldn’t execute anything."""
        pass # Do nothing

    def do_help(self, arg):
        """Help command to display available commands."""
        if arg:
            # Check if there's a specific command to provide help for
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
            # List available commands
            print("Documented commands (type help <topic>):")
            print("=========================================")
            cmd.Cmd.do_help(self, arg)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
