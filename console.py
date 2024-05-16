#!/usr/bin/python3
"""A command line interpreter"""

import cmd


class HBNBCommand(cmd.Cmd):
    """The command class that inherites from the imported cmd module"""
    prompt = "(hbnb) "

    def do_EOF(self, arg):
        """Handlesnendnof file"""
        return True
    def do_quit(self, arg):
        """Returns true when user exits"""
        return True
    def emptyline(self):
        """Executes nothing if nothing is passed"""
        pass
if __name__ == '__main__':
        HBNBCommand().cmdloop()
