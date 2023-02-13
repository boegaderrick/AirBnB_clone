#!/usr/bin/python3
"""This module contains a test class for AirBnB console testing"""

from unittest import TestCase
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO


class TestHBNBCommand(TestCase):
    """AirBnB console test class"""
    def test_advanced_all(self):
        """Tests advanced all command <class_name>.all()"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.all()")
            output = f.getvalue()[:-1]
            self.assertTrue(output.startswith('['))
            self.assertTrue(output.endswith(']'))

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.all()")
            output = f.getvalue()[:-1]
            self.assertTrue(output.startswith('['))
            self.assertTrue(output.endswith(']'))

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.all()")
            output = f.getvalue()[:-1]
            self.assertTrue(output.startswith('['))
            self.assertTrue(output.endswith(']'))

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.all()")
            output = f.getvalue()[:-1]
            self.assertTrue(output.startswith('['))
            self.assertTrue(output.endswith(']'))

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.all()")
            output = f.getvalue()[:-1]
            self.assertTrue(output.startswith('['))
            self.assertTrue(output.endswith(']'))

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.all()")
            output = f.getvalue()[:-1]
            self.assertTrue(output.startswith('['))
            self.assertTrue(output.endswith(']'))

    def test_advanced_count(self):
        """Tests advanced count command <class_name>.count()"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.count()")
            output = f.getvalue()[:-1]
            self.assertTrue(output.isnumeric())
            self.assertGreater(int(output), -1)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.count()")
            output = f.getvalue()[:-1]
            self.assertTrue(output.isnumeric())
            self.assertGreater(int(output), -1)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("state.count()")
            output = f.getvalue()[:-1]
            self.assertEqual(output, "*** Unknown syntax: state.count()")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.count()")
            output = f.getvalue()[:-1]
            self.assertTrue(output.isnumeric())
            self.assertGreater(int(output), -1)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.count()")
            output = f.getvalue()[:-1]
            self.assertTrue(output.isnumeric())
            self.assertGreater(int(output), -1)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.count()")
            output = f.getvalue()[:-1]
            self.assertTrue(output.isnumeric())
            self.assertGreater(int(output), -1)

    def test_advanced_show(self):
        """Tests advanced show command <class_name>.show()"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.show('78786-78787')")
            output = f.getvalue()[:-1]
            self.assertEqual(output, "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.show('78786-78787')")
            output = f.getvalue()[:-1]
            self.assertEqual(output, "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.show('78786-78787')")
            output = f.getvalue()[:-1]
            self.assertEqual(output, "** no instance found **")

        # with patch('sys.stdout', new=StringIO()) as f:
        #    HBNBCommand().onecmd("Review.show('78786-78787')")
        #    output = f.getvalue()[:-1]
        #    self.assertEqual(output, "** no instance found **")

    def test_advanced_destroy(self):
        """Tests advanced destroy command <class_name>.destroy()"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.destroy('78786-78787')")
            output = f.getvalue()[:-1]
            self.assertEqual(output, "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.destroy('78786-78787')")
            output = f.getvalue()[:-1]
            self.assertEqual(output, "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.destroy('78786-78787')")
            output = f.getvalue()[:-1]
            self.assertEqual(output, "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.destroy('78786-78787')")
            output = f.getvalue()[:-1]
            self.assertEqual(output, "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.destroy('78786-78787')")
            output = f.getvalue()[:-1]
            self.assertEqual(output, "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.destroy('78786-78787')")
            output = f.getvalue()[:-1]
            self.assertEqual(output, "** no instance found **")

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.destroy('78786-78787')")
            output = f.getvalue()[:-1]
            self.assertEqual(output, "** no instance found **")

    def test_advanced_update(self):
        """Tests advancec update command <class_name>.update('id')"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("BaseModel.create()")
            output = '"' + f.getvalue()[:-1] + '"'

        with patch('sys.stdout', new=StringIO()) as f:
            _dict = {'name': 'jay', 'age': 2, 'pet': 'dog', 'car': 'dodge'}
            HBNBCommand().onecmd(f"BaseModel.update({output}, {_dict})")
            out = f.getvalue()[:-1]
            self.assertTrue(len(out) == 0)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"BaseModel.update({output}, {{'sex': 'M'}})")
            out = f.getvalue()[:-1]
            self.assertEqual('', out)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.create()")
            output = '"' + f.getvalue()[:-1] + '"'

        with patch('sys.stdout', new=StringIO()) as f:
            _dict = {'name': 'jay', 'age': 2, 'pet': 'dog', 'car': 'dodge'}
            HBNBCommand().onecmd(f"State.update({output}, {_dict})")
            out = f.getvalue()[:-1]
            self.assertTrue(len(out) == 0)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"State.update({output}, {{'sex': 'male'}})")
            out = f.getvalue()[:-1]
            self.assertEqual('', out)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.create()")
            output = '"' + f.getvalue()[:-1] + '"'

        with patch('sys.stdout', new=StringIO()) as f:
            _dict = {'name': 'jay', 'age': 2, 'pet': 'dog', 'car': 'dodge'}
            HBNBCommand().onecmd(f"City.update({output}, {_dict})")
            out = f.getvalue()[:-1]
            self.assertTrue(len(out) == 0)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"City.update({output}, {{'sex': 'male'}})")
            out = f.getvalue()[:-1]
            self.assertEqual('', out)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.create()")
            output = '"' + f.getvalue()[:-1] + '"'

        with patch('sys.stdout', new=StringIO()) as f:
            _dict = {'name': 'jay', 'age': 2, 'pet': 'dog', 'car': 'dodge'}
            HBNBCommand().onecmd(f"Amenity.update({output}, {_dict})")
            out = f.getvalue()[:-1]
            self.assertTrue(len(out) == 0)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Amenity.update({output}, {{'sex': 'M'}})")
            out = f.getvalue()[:-1]
            self.assertEqual('', out)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.create()")
            output = '"' + f.getvalue()[:-1] + '"'

        with patch('sys.stdout', new=StringIO()) as f:
            _dict = {'name': 'jay', 'age': 2, 'pet': 'dog', 'car': 'dodge'}
            HBNBCommand().onecmd(f"Review.update({output}, {_dict})")
            out = f.getvalue()[:-1]
            self.assertTrue(len(out) == 0)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Review.update({output}, {{'sex': 'male'}})")
            out = f.getvalue()[:-1]
            self.assertEqual('', out)

    def test_advanced(self):
        """Tests advanced commands (example: User.destroy("78787-88678")"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.all()")
            output = f.getvalue()[:-1]
            self.assertTrue(output.startswith('['))
            self.assertTrue(output.endswith(']'))

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.count()")
            output = f.getvalue()[:-1]
            self.assertTrue(output.isnumeric)
            self.assertTrue(int(output) > -1)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.create()")
            output = f.getvalue()[:-1]
            self.assertEqual(36, len(output))

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Amenity.show({output})")
            out = f.getvalue()[:-1]
            self.assertTrue(out.startswith('['))
            self.assertTrue(out.endswith('}'))

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Amenity.destroy({output})")
            output = f.getvalue()[:-1]
            self.assertTrue(len(output) == 0)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.create()")
            output = '"' + f.getvalue()[:-1] + '"'

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"User.update({output}, 'name', 'ron')")
            out = f.getvalue()[:-1]
            self.assertTrue(len(out) == 0)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"User.show({output})")
            out = f.getvalue()[:-1]
            string = "'name': 'ron'"
            self.assertTrue(string in out)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.create()")
            output = '"' + f.getvalue()[:-1] + '"'

        with patch('sys.stdout', new=StringIO()) as f:
            _dict = {'name': 'jay', 'age': 2, 'pet': 'dog', 'car': 'dodge'}
            HBNBCommand().onecmd(f"Place.update({output}, {_dict})")
            out = f.getvalue()[:-1]
            self.assertTrue(len(out) == 0)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Place.update({output}, {{'sex': 'male'}})")
            out = f.getvalue()[:-1]
            self.assertEqual('', out)

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"Place.show({output})")
            out = f.getvalue()[:-1]
            self.assertTrue(all(i in out for i in _dict.keys()))
            self.assertTrue(all(str(i) in out for i in _dict.values()))

    def test_help(self):
        """Tests output of the help command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            output = f.getvalue()
            string = "\nDocumented commands (type help <topic>):\n\
========================================\n\
EOF  all  count  create  destroy  help  quit  shell  show  update\n\n"
            self.assertEqual(string, output)

        # help count
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help count")
            output = f.getvalue()
            string = "Displays the count of instances of a specified \
class in storage\n\
        USAGE: count [ClassName]\n\
        USAGE: <ClassName>.count()\n\
        EXMPL: count BaseModel\n\
             : BaseModel.count()\n"
            self.assertEqual(string, output)

        # help update
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help update")
            output = f.getvalue()
            string = "Updates instance specified by Class and id\n\
        USAGE: update <ClassName> <id> <attribute name> <attribute value>\n"
            self.assertEqual(string, output)

        # help show
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help show")
            help_show = " Prints string representation of instance specified\n\
        USAGE: show [ClassName] [id]\n"
            output = f.getvalue()
            self.assertEqual(help_show, output)

        # help all
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help all")
            output = f.getvalue()
            string = "Prints list of string representation of stored objects\n\
        USAGE: all [ClassName] - for all instances of specified class\n\
        USAGE: all - for all instances of all classes\n"

        # help destroy
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help destroy")
            output = f.getvalue()
            string = " Destroys/deletes instance/object specified\n\
        USAGE: destroy [ClassName] [id]\n"
            self.assertEqual(string, output)

        # help create
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
            output = f.getvalue()
            string = "Creates a new instance of a class\n\
        USAGE: create [ClassName]\n"
            self.assertEqual(string, output)

        # help quit
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            output = f.getvalue()
            string = 'Quit command to exit the program\n'
            self.assertEqual(string, output)

        # help EOF
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
            output = f.getvalue()
            string = 'Exits the program\n\
        USAGE: ctrl^d\n\
        USAGE: EOF\n        \n'
            self.assertEqual(string, output)

    def test_count(self):
        """Tests the count command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count User")
            output = f.getvalue()[:-1]
            self.assertTrue(output.isnumeric())
            self.assertTrue(int(output) > -1)

    def test_update(self):
        """Tests the update command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update City 99898")
            self.assertEqual('** no instance found **\n', f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
            obj = f.getvalue()[:-1]

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update city {obj}")
            self.assertEqual('** class doesn\'t exist **\n', f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update City {obj}")
            self.assertEqual('** attribute name missing **\n', f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update City {obj} name")
            self.assertEqual('** value missing **\n', f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"update City {obj} name derrick")
            self.assertEqual('', f.getvalue())

    def test_all(self):
        """Tests the all command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
            output = f.getvalue()[:-1]
            self.assertTrue(output.startswith('['))
            self.assertTrue(output.endswith(']'))

    def test_destroy(self):
        """Tests the destroy command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            obj = f.getvalue()[:-1]

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy User {obj}")
            self.assertEqual('', f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"destroy User {obj}")
            self.assertEqual('** no instance found **\n', f.getvalue())

    def test_show(self):
        """Tests the show command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User")
            string = '** instance id missing **\n'
            self.assertEqual(string, f.getvalue())

    def test_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            string = '** class name missing **\n'
            self.assertEqual(string, f.getvalue())
            print(f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            self.assertEqual(37, len(f.getvalue()))

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            self.assertEqual(37, len(f.getvalue()))

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            self.assertEqual(37, len(f.getvalue()))

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
