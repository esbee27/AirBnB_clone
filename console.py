#!/usr/bin/python3
"""A command line interpreter"""

import cmd
from models.user import User

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
    
    def do_create(self, arg):
        """ New istance of user will be created,
        saved into engine, only id will be printed """
        if not arg:
            print("** class name is missing**")
        elif arg != "User":
            new_user = User()
            new_user.save()
            print(new_user.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] != "User":
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = f"User.{args[1]}"
            if key not in models.storage.all():
                print("** no instance found **")
            else:
                print(models.storage.all()[key])


    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] != "User":
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = f"User.{args[1]}"
            if key not in models.storage.all():
                print("** no instance found **")
            else:
                del models.storage.all()[key]
                models.storage.save()


    def do_all(self, arg):
        """Prints all string representations of all instances"""
        if arg and arg != "User":
            print("** class doesn't exist **")
        else:
            objects = models.storage.all()
            print([str(obj) for obj in objects.values()])


    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] != "User":
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = f"User.{args[1]}"
            if key not in models.storage.all():
                print("** no instance found **")
            else:
                obj = models.storage.all()[key]
                setattr(obj, args[2], args[3])
                obj.save()

if __name__ == '__main__':
        HBNBCommand().cmdloop()
