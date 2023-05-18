#!/usr/bin/python3
"""Defines unittests for console.py."""
import os
import sys
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch
import console
import pycodestyle


class_names = [
            "BaseModel",
            "User",
            "State",
            "City",
            "Place",
            "Review"
            ]

class_list = [
            "BaseModel",
            "User",
            "State",
            "City",
            "Place",
            "Review"
            ]

class TestHBNBCommand_prompting(unittest.TestCase):
    """Unittests for testing prompting of the HBNB command interpreter."""

    def test_prompt_string(self):
        self.assertEqual("(hbnb)", HBNBCommand.prompt)

    def test_empty_line(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", output.getvalue().strip())

class TestHBNBCommand_exit(unittest.TestCase):
    """ unnittests for EOF and quit """
    def test_eof(self):
        """ test EOF method """
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("EOF")
        self.assertEqual("\n", output.getvalue())
        self.assertTrue(HBNBCommand().onecmd("EOF"))

    def test_quit(self):
        """ test for the quit method """
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("EOF")
        self.assertEqual("\n", output.getvalue())
        self.assertTrue(HBNBCommand().onecmd("quit"))

class TestHBNBCommand_doc_style(unittest.TestCase):
    """ unittests for pycodestyle and documentation"""
    def test_console_conformity_pycode(self):
        """Tests console.py's adherence to pycodestyle."""
        pycode = pycodestyle.StyleGuide(quiet=True)
        res = pycode.check_files(['console.py'])
        self.assertEqual(res.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_console_module_docstring(self):
        """Tests existence of console.py module docstring"""
        self.assertIsNot(console.__doc__, None,
                         "console.py needs a docstring")
        self.assertTrue(len(console.__doc__) >= 1,
                        "console.py needs a docstring")

class TestHBNBCommand_help(unittest.TestCase):
    """Unittests for testing help messages of the HBNB command interpreter."""

    def test_help_quit(self):
        h = "Quit command to exit the program"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help_create(self):
        h = "Creates a new instance of BaseModel"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help_EOF(self):
        h = "Hit ctrl+D (EOF) to exit the program"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help_show(self):
        h = "Prints the string representation of an instance"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help show"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help_destroy(self):
        h = "Deletes an instance based on the class name and id"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help destroy"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help_all(self):
        h = "Prints all string representation of all instances"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help_count(self):
        h = "Retrieves the number of instances of a class"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help count"))
            self.assertEqual(h, output.getvalue().strip())

    def test_help_update(self):
        h = "Updates an instance based on the class name and id"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("help update"))
            self.assertEqual(h.strip(), output.getvalue().strip())

    def test_help(self):
        """Tests help command."""
        with patch('sys.stdout', new=StringIO()) as output:
            HBNBCommand().onecmd("help")
        h  = """
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

"""

class TestHBNBCommand_create(unittest.TestCase):
    """ unittest for the create method """
    def test_error1(self):
        """ class name missing error """
        h = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create")
        self.assertEqual(h, output.getvalue().strip())

    def test_error2(self):
        """ class does not exist """
        h = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create MyModel")
        self.assertEqual(h, output.getvalue().strip())


    def test_create_basemodel(self):
        """ test the do_create method """
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create BaseModel")
        key = "BaseModel.{}".format(output.getvalue().strip())
        self.assertIn(key, storage.all())

    def test_create_user(self):
        """ test the do_create method """
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create User")
        key = "User.{}".format(output.getvalue().strip())
        self.assertIn(key, storage.all())

    def test_create_city(self):
        """ test the do_create method """
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create City")
        key = "City.{}".format(output.getvalue().strip())
        self.assertIn(key, storage.all())

    def test_create_state(self):
        """ test the do_create method """
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create State")
        key = "State.{}".format(output.getvalue().strip())
        self.assertIn(key, storage.all())

    def test_create_place(self):
        """ test the do_create method """
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Place")
        key = "Place.{}".format(output.getvalue().strip())
        self.assertIn(key, storage.all())

    def test_create_amenity(self):
        """ test the do_create method """
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Amenity")
        key = "Amenity.{}".format(output.getvalue().strip())
        self.assertIn(key, storage.all())

    def test_create_review(self):
        """ test the do_create method """
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("create Review")
        key = "Review.{}".format(output.getvalue().strip())
        self.assertIn(key, storage.all())

class TestHBNBCommand_show(unittest.TestCase):
    """ unittests for the show method """
    def test_error1(self):
        """ class name missing error """
        h = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("show")
        self.assertEqual(h, output.getvalue().strip())
        h = "*** Unknown syntax: .show()"
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd(".show()")
        self.assertEqual(h, output.getvalue().strip())

    def test_error2(self):
        """ class does not exist """
        h = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("show MyModel")
        self.assertEqual(h, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            line = HBNBCommand().precmd("MyModel.show()")
            HBNBCommand().onecmd(line)
        self.assertEqual(h, output.getvalue().strip())

    def test_error3(self):
        """ instance id missing """
        h = "** instance id missing **"
        for class_name in class_list:
            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("show {}".format(class_name))
            self.assertEqual(h, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                line = HBNBCommand().precmd("{}.show()".format(class_name))
                HBNBCommand().onecmd(line)
            self.assertEqual(h, output.getvalue().strip())

    def test_error4(self):
        """ no instance found """
        h = "** no instance found **"
        for class_name in class_list:
            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("show {} somerandomid".format(class_name))
            self.assertEqual(h, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                line = HBNBCommand().precmd("{}.show(somerandomid)".format(class_name))
                HBNBCommand().onecmd(line)
            self.assertEqual(h, output.getvalue().strip())

    def test_show_instance(self):
        """ test if it shows the specified instance"""
        for class_name in class_list:
            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("create {}".format(class_name))
            obj_id = output.getvalue().strip()
            obj = storage.all()["{}.{}".format(class_name, obj_id)]
            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("show {} {}".format(class_name, obj_id))
            self.assertEqual(obj.__str__(), output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                line = HBNBCommand().precmd("{}.show({})".format(class_name, obj_id))
                HBNBCommand().onecmd(line)
            self.assertEqual(obj.__str__(), output.getvalue().strip())

class TestHBNBCommand_destroy(unittest.TestCase):
    """ unittests for the show method """
    def test_error1(self):
        """ class name missing error """
        h = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("destroy")
        self.assertEqual(h, output.getvalue().strip())
        h = "*** Unknown syntax: .destroy()"
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd(".destroy()")
        self.assertEqual(h, output.getvalue().strip())

    def test_error2(self):
        """ class does not exist """
        h = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            HBNBCommand().onecmd("destroy MyModel")
        self.assertEqual(h, output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            line = HBNBCommand().precmd("MyModel.destroy()")
            HBNBCommand().onecmd(line)
        self.assertEqual(h, output.getvalue().strip())

    def test_error3(self):
        """ instance id missing """
        h = "** instance id missing **"
        for class_name in class_list:
            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("destroy {}".format(class_name))
            self.assertEqual(h, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                line = HBNBCommand().precmd("{}.destroy()".format(class_name))
                HBNBCommand().onecmd(line)
            self.assertEqual(h, output.getvalue().strip())

    def test_error4(self):
        """ no instance found """
        h = "** no instance found **"
        for class_name in class_list:
            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("destroy {} somerandomid".format(class_name))
            self.assertEqual(h, output.getvalue().strip())
            with patch("sys.stdout", new=StringIO()) as output:
                line = HBNBCommand().precmd("{}.destroy(somerandomid)".format(class_name))
                HBNBCommand().onecmd(line)
            self.assertEqual(h, output.getvalue().strip())

    def test_destroy_instance(self):
        """ test if it shows the specified instance"""
        for class_name in class_list:
            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("create {}".format(class_name))
            obj_id = output.getvalue().strip()
            obj = storage.all()["{}.{}".format(class_name, obj_id)]
            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("destroy {} {}".format(class_name, obj_id))
            self.assertEqual("", output.getvalue().strip())
            self.assertNotIn("{}.{}".format(class_name, obj_id), storage.all())
            with patch("sys.stdout", new=StringIO()) as output:
                HBNBCommand().onecmd("create {}".format(class_name))
            obj_id = output.getvalue().strip()
            obj = storage.all()["{}.{}".format(class_name, obj_id)]
            with patch("sys.stdout", new=StringIO()) as output:
                line = HBNBCommand().precmd("{}.destroy({})".format(class_name, obj_id))
                HBNBCommand().onecmd(line)
            self.assertEqual("", output.getvalue().strip())
            self.assertNotIn("{}.{}".format(class_name, obj_id), storage.all())

class TestHBNBCommand_all(unittest.TestCase):
    #Testing all method in the console

    @classmethod
    def setUp(self):
        try:
            file_name = "file.json"
            temp_file = "temp.json"

            # renaming the file to preserve the data
            os.rename(file_name, temp_file)
        except IOError:
            pass

        # setting up __objects to tests
        FileStorage.__objects = {}

        # Creating instances for each class for testing pupose
        for class_name in class_names:
            with patch("sys.stdout", new=StringIO()) as f:
                HBNBCommand().onecmd("create {}".format(class_name))
    
    @classmethod
    def tearDown(self):
        try:
            # Removing the file having the previous test content
            os.remove("file.json")
        except IOError:
            pass

        try:
            # Restoring the file.json to its original state
            os.rename("temp.json", "file.json")
            # incase 'temp.json' exist(though it won't exist!)
            os.remove("temp.json")
        except IOError:
            pass

    def test_all_error1(self):
        s = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as f:
            # Ex: all xyz (xyz is just random word)
            HBNBCommand().onecmd("all xyz")
            self.assertEqual(s, f.getvalue().strip())

        with patch("sys.stdout", new=StringIO()) as f:
            # Ex: xyz.all()
            HBNBCommand().onecmd("xyz.all()")
            self.assertEqual(s, f.getvalue().strip())

    def test_all_class(self):
        for class_name in class_names:
            with patch("sys.stdout", new=StringIO()) as f:
                # handling the method in this form (Ex: all User)
                HBNBCommand().onecmd(f"all {class_name}")

            with patch("sys.stdout", new=StringIO()) as f:
                # handling the method in thid form(Ex: User.all())
                HBNBCommand().onecmd(f"{class_name}.all()")
                for _dict in f.keys:
                    # Using split method we get the name of a class
                    _cls = _dict.split()[0][1:-1]

                    # checking if the class exist
                    assertEqual(_cls, f"{class_name}")

                # This for loop iterates over the return values of all method
                for _dict in f.keys:
                    # Using split method we get the name of a class
                    _cls = _dict.split()[0][1:-1]

                    # checking if the class exist
                    assertEqual(_cls, f"{class_name}")

                    for ch_class in class_names:
                        if ch_class != class_name:
                            self.assertNotIn("{}".format(ch_class), output.getvalue().strip())
