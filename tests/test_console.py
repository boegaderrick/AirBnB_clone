#!/usr/bin/python3
"""This module contains a test class for AirBnB console testing"""

from unittest import TestCase
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO


class TestHBNBCommand(TestCase):
    """AirBnB console test class"""
    def test_help_show(self):
        """Tests output of the help command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            string = " Prints string representation of instance specified\n\
        USAGE: show [ClassName] [id]\n"
            output = f.getvalue()
            self.assertEqual(string, output)

    def test_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            string = '** class name missing **\n'
            self.assertEqual(string, f.getvalue())
            print(f.getvalue())

        #with patch('sys.stdout', new=StringIO()) as f:
        #    HBNBCommand().onecmd("create BaseModel")
        #    self.assertEqual(36, len(f.getvalue()))


    def test_no_command(self):
        """Tests output of 'no command + enter' or emptyline"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("")
            string = ''
            output = f.getvalue()
            self.assertEqual(string, output)

    def test_quit_EOF(self):
        """Tests the quit and EOF commands"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            self.assertEqual('', f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
            self.assertEqual('\n', f.getvalue())
