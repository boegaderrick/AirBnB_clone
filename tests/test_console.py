#!/usr/bin/python3
"""This module contains a test class for AirBnB console testing"""

from unittest import TestCase
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO


class TestHBNBCommand(TestCase):
    """AirBnB console test class"""
    def test_1(self):
        """Tests output of the help command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            string = " Prints string representation of instance specified\n\
        USAGE: show [ClassName] [id]\n"
            output = f.getvalue()
            self.assertEqual(string, output)

    def test_2(self):
        """Tests output of 'no command + enter' or emptyline"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("")
            string = ''
            output = f.getvalue()
            self.assertEqual(string, output)

    def test_3(self):
        """Tests the quit and EOF commands"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            self.assertEqual('', f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
            self.assertEqual('\n', f.getvalue())
