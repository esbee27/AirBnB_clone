#!/usr/bin/python3
"""A command line interpreter"""

import cmd
import models
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.amenity import Amenity


class HBNBCommand(cmd.Cmd):
    """The command class that inherits from the imported cmd module"""
    prompt = "(hbnb) "
    classes = {
        "User": User,
        "City": City,
        "Place": Place,
        "State": State,
        "Amenity": Amenity
    }

    def do_EOF(self, arg):
        """Handles end of file"""
        return True

    def do_quit(self, arg):
        """Returns true when user exits"""
        return True

    def emptyline(self):
        """Executes nothing if nothing is passed"""
        pass

    def do_create(self, arg):
        """Creates a new instance of the specified class"""
        if not arg:
            print("** class name missing **")
        elif arg not in self.classes:
            print("** class doesn't exist **")
        else:
            new_instance = self.classes[arg]()
            models.storage.new(new_instance)
            models.storage.save()
            print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key not in models.storage.all():
                print("** no instance found **")
            else:
                print(models.storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key not in models.storage.all():
                print("** no instance found **")
            else:
                del models.storage.all()[key]
                models.storage.save()

    def do_all(self, arg):
        """Prints all string representations of all instances of a specified class"""
        if arg and arg not in self.classes:
            print("** class doesn't exist **")
        else:
            objects = models.storage.all()
            if arg:
                objects = {k: v for k, v in objects.items() if k.startswith(arg + '.')}
            print([str(obj) for obj in objects.values()])

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute"""
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key not in models.storage.all():
                print("** no instance found **")
            else:
                obj = models.storage.all()[key]
                setattr(obj, args[2], args[3])
                obj.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()

