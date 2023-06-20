#!/usr/bin/python3
"""This is command line interpreter"""
import cmd
import re
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """This interpretor interprets few commands
    to create, recreate, update, show, and to accept
    variable number of argumets. The default functionality
    of the cmd module is overriden to interprete some
    commands not having defult structrue of cmd module.
    """

    prompt = "(hbnb) "

    __classNames = [
            "BaseModel",
            "User",
            "State",
            "City",
            "Place",
            "Amenity",
            "Review"]

    def precmd(self, line):
        """Overriding defult functionality of precmd method"""
        match = re.search(r"^(\w+)\.(\w+)(?:\(([\S|\s]*)\))$", line)
        if match:
            arg = line.split()
            className, command, args = match.groups()
            args = args.replace('"', "")

            if "," in args:
                if match := re.search(r"(\S+), (\S+), (\S+)", args):
                    arg1 = match.group(1).replace('"', "")
                    arg2 = match.group(2).replace('"', "")
                    arg3 = match.group(3).replace('"', "")
                    line = "{} {} {} {} {}".format(
                            command, className, arg1, arg2, arg3
                            )
                elif match := re.search(r"\.", line):
                    args = [line[: match.span()[0]], line[match.span()[1]:]]
                    match = re.search(r"\(", args[1])
                    command = [
                            args[1][: match.span()[0]],
                            args[1][match.span()[1]:]
                            ]
                    if match := re.search(r'"(.*?)\", (.*)\)', command[1]):
                        _id = match.group(1)
                        _dict = match.group(2).replace("'", '"')
                        line = "{} {} {} .{}".format(
                                command[0], args[0], _id, _dict
                                )
            else:
                line = "{} {} {}".format(command, className, args)
        return cmd.Cmd.precmd(self, line)

    def do_create(self, line):
        """To create instances"""
        arg = line.split()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.__classNames:
            print("** class doesn't exist **")
        else:
            print(eval(arg[0])().id)
            storage.save()

    def do_show(self, line):
        """To show insatances"""
        from_fileClass = storage.all()
        arg = line.split()

        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.__classNames:
            print("** class doesn't exist **")
        elif len(arg) < 2:
            print("** instance id missing **")
        elif "{}.{}".format(arg[0], arg[1]) not in from_fileClass:
            print("** no instance found **")
        else:
            print(from_fileClass[arg[0] + "." + arg[1]])

    def do_destroy(self, line):
        """To destroy instances"""
        from_fileClass = storage.all()
        arg = line.split()

        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.__classNames:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg[0], arg[1]) not in from_fileClass:
            print("** no instance found **")
        else:
            del from_fileClass[arg[0] + "." + arg[1]]
            storage.save()

    def do_all(self, arg):
        #Prints all the instances
        try:
            arguments = arg.split()
            objects = storage.all()
            # let us first check if a class name exists
            if arguments and arguments[0] not in HBNBCommand.__classNames:
                print("** class doesn't exist **")
                return
            if arguments:
                new_obj = [
                    str(obj)
                    for obj in objects.values()
                    if arguments[0] == type(obj).__name__
                ]
            elif len(arguments) == 0:
                new_obj = [str(obj) for obj in objects.values()]

            print(new_obj)

        except Exception as e:
            print(e)

    def do_count(self, line):
        """To count instances of the same class"""
        from_fileClass = storage.all()
        arg = line.split()
        total = 0

        if len(arg) == 1:
            for key, val in from_fileClass.items():
                className, id = key.split(".")
                if arg[0] == className:
                    total += 1
            print(total)

    def do_update(self, line):
        """To update instances"""
        from_fileClass = storage.all()
        arg = line.split()

        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.__classNames:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg[0], arg[1]) not in from_fileClass:
            print("** no instance found **")
        elif len(arg) == 2:
            print("** attribute name missing **")
        elif len(arg) == 3:
            print("** value missing **")
        elif len(arg) > 4:
            if "{" in line:
                _parse = line.split(".")
                obj_dict = from_fileClass
                _dict = {key: obj_dict[key].to_dict() for key in obj_dict}
                for key, val in _dict.items():
                    if key == "{}.{}".format(arg[0], arg[1]):
                        _to_dict = json.loads(_parse[1])
                        val = {**val, **_to_dict}
                        className = val["__class__"]
                        storage.new(eval(className)(**val))
                        storage.save()
        else:
            obj_dict = from_fileClass
            _dict = {key: obj_dict[key].to_dict() for key in obj_dict}
            for key, val in _dict.items():
                if key == "{}.{}".format(arg[0], arg[1]):
                    val[arg[2]] = arg[3]
                    className = val["__class__"]
                    storage.new(eval(className)(**val))
                    storage.save()

    def emptyline(self):
        """Overriding emptyline method"""
        return False

    def do_quit(self, line):
        """Quit command to exit the program"""
        exit()

    def do_EOF(self, line):
        """EOF to exit the program"""
        print()
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
