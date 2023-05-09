#!/usr/bin/python3
""" Testing the console using patch """


import os
from console import HBNBCommand
from models import storage
import unittest
from unittest.mock import patch
from io import StringIO


class test_console(unittest.TestCase):
    """ Checking the working of the console """
    
    def test_eof(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")

            s = 'EOF to exit the program'
            self.assertEqual(s, f.getvalue().strip())

    def test_quit(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")

            s = 'Quit command to exit the program'
            self.assertEqual(s, f.getvalue().strip())

    def test_emptyline(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd(""))
            self.assertEqual("", f.getvalue().strip())

    def test_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")

            s = 'To create instances'
            self.assertEqual(s, f.getvalue().strip())

    def test_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")

            s = 'To show insatances'
            self.assertEqual(s, f.getvalue().strip())

    def test_destroy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help destroy")

            s = 'To destroy instances'
            self.assertEqual(s, f.getvalue().strip())

    def test_all(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help all")

            s = 'Usage: lists all the instances'
            self.assertEqual(s.strip(), f.getvalue().strip())

    def test_update(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help update")

            s = 'To update instances'
            self.assertEqual(s, f.getvalue().strip())

    def test_count(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help count")

            s = 'To count instances of the same class'
            self.assertEqual(s, f.getvalue().strip())


class test_create(unittest.TestCase):
    """ Checking for 'create' method """
    
    def test_class_name_missing(self):
        s = '** class name missing **'
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual(s.strip(), f.getvalue().strip())

    def test_class_name_not_exist(self):
        s = "** class doesn't exist **"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create xyz")
            self.assertEqual(s.strip(), f.getvalue().strip())

    def test_creating_base_model(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            self.assertLess(0, len(f.getvalue().strip()))
            self.assertEqual(type(f.getvalue()), str)
            key = 'BaseModel' + '.' + f.getvalue().strip()
            self.assertIn(key, storage.all())

    def test_creating_user(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            self.assertLess(0, len(f.getvalue().strip()))
            self.assertEqual(type(f.getvalue()), str)
            key = 'User' + '.' + f.getvalue().strip()
            self.assertIn(key, storage.all())

    def test_creating_city(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
            self.assertLess(0, len(f.getvalue().strip()))
            self.assertEqual(type(f.getvalue()), str)
            key = 'City' + '.' + f.getvalue().strip()
            self.assertIn(key, storage.all())

    def test_creating_state(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            self.assertLess(0, len(f.getvalue().strip()))
            self.assertEqual(type(f.getvalue()), str)
            key = 'State' + '.' + f.getvalue().strip()
            self.assertIn(key, storage.all())

    def test_creating_review(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            self.assertLess(0, len(f.getvalue().strip()))
            self.assertEqual(type(f.getvalue()), str)
            key = 'Review' + '.' + f.getvalue().strip()
            self.assertIn(key, storage.all())

    def test_creating_amenity(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            self.assertLess(0, len(f.getvalue().strip()))
            self.assertEqual(type(f.getvalue()), str)
            key = 'Amenity' + '.' + f.getvalue().strip()
            self.assertIn(key, storage.all())

    def test_creating_place(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            self.assertLess(0, len(f.getvalue().strip()))
            self.assertEqual(type(f.getvalue()), str)
            key = 'Place' + '.' + f.getvalue().strip()
            self.assertIn(key, storage.all())
