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
            HBNBCommand().onecmd("help emptyline")

            self.assertTrue(f.getvalue().strip())

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
