#!/usr/bin/python3
""" This module implements a command interpreter for AirBnB clone"""
import cmd
import os
from models.__init__ import storage


class HBNBCommand(cmd.Cmd):
    """AirBnB command interpreter class definition"""
    prompt = '(hbnb) '

    def __init__(self, completekey='tab', stdin=None, stdout=None):
        """Object constructor method"""
        super().__init__(completekey, stdin, stdout)

    def onecmd(self, line):
        """Override for the Cmd.onecmd method to cater for unique commands.
        If a unique command is passed it is handled accordingly.
        Cmd.onecmd is called either way.
        """
        if len(line) < 1 or line is None:
            return super().onecmd(line)

        if line[0].isupper() and all(i in line for i in '.()'):
            cmd = line[line.index('.')+1:line.index('(')]
            class_name = line[:line.index('.')]
            args = line[line.index('(')+1:line.index(')')]
            if len(args) > 0 and ', ' in args:
                import ast
                args = ast.literal_eval(args)
                if type(args[1]) is dict:
                    _id = args[0]
                    for key, value in args[1].items():
                        if type(value) is str and ' ' in value:
                            value = '"' + value + '"'
                        else:
                            value = str(value)
                        line = ' '.join((cmd, class_name, _id, key, value))
                        ret = super().onecmd(line)
                    return ret
                if type(args[2]) is str and ' ' in args[2]:
                    temp = '"' + args[2] + '"'
                    string = ' '.join(args[i] for i in range(2))
                    string += ' ' + temp
                else:
                    string = ' '.join(str(i) for i in args)
            else:
                if args.startswith('"'):
                    start = args.index('"') + 1
                    string = args[start:args.index('"', start)]
                else:
                    string = args
            line = cmd + ' ' + class_name + ' ' + string
            return super().onecmd(line)
        else:
            return super().onecmd(line)

    def do_count(self, args):
        """Displays the count of instances of a specified class in storage
        USAGE: count [ClassName]
        USAGE: <ClassName>.count()
        EXMPL: count BaseModel
             : BaseModel.count()"""
        if storage.my_classes(args) is None:
            return
        _dict = storage.objects
        count = sum([1 for key in _dict.keys() if key.startswith(args)])
        print(count)

    def do_update(self, args):
        """Updates instance specified by Class and id
        USAGE: update <ClassName> <id> <attribute name> <attribute value>"""
        temp = args.rsplit()[:4]
        class_name = temp[0] if len(temp) > 0 else None
        obj_id = temp[1] if len(temp) > 1 else None
        attr = temp[2] if len(temp) > 2 else None
        if len(temp) > 3:
            if temp[3].startswith('"'):
                start = args.index('"')
                end = args.index('"', start+1)
                value = args[start+1:end]
            else:
                value = temp[3]
        else:
            value = None

        if storage.my_classes(class_name) is None:
            return
        foo = f'{class_name} {obj_id}' if obj_id is not None else class_name
        obj = self.get_obj(foo)
        if obj is None:
            return
        if attr is None:
            print("** attribute name missing **")
            return
        if value is None:
            print("** value missing **")
            return
        if hasattr(obj, attr):
            a_type = type(getattr(obj, attr))
            value = a_type(value)
        setattr(obj, attr, value)
        obj.save()

    def do_all(self, args):
        """Prints list of string representation of stored objects
        USAGE: all [ClassName] - for all instances of specified class
        USAGE: all - for all instances of all classes"""
        if len(args) > 0 and storage.my_classes(args) is None:
            return
        obj_strs = []
        for key in storage.objects.keys():
            if len(args) < 1:
                obj_strs.append(storage.objects[key].__str__())
            else:
                if key.startswith(args):
                    obj_strs.append(storage.objects[key].__str__())
        print(obj_strs)

    def do_destroy(self, args):
        """ Destroys/deletes instance/object specified
        USAGE: destroy [ClassName] [id]"""
        obj = self.get_obj(args)
        if obj is None:
            return
        for key, value in storage.objects.items():
            if value is obj:
                del storage.objects[key]
                storage.save()
                return

    def get_obj(self, args):
        """Retrieves object from storage"""
        class_name, obj_id, args = self.parseline(args)
        if storage.my_classes(class_name) is None:
            return
        if len(obj_id) < 1:
            print("** instance id missing **")
            return
        obj_key = f'{class_name}.{obj_id}'
        storage.reload()
        if obj_key in storage.objects:
            return storage.objects[obj_key]
        else:
            print("** no instance found **")

    def do_show(self, args):
        """ Prints string representation of instance specified
        USAGE: show [ClassName] [id]"""
        obj = self.get_obj(args)
        if obj is not None:
            print(obj)

    def do_create(self, args):
        """Creates a new instance of a class
        USAGE: create [ClassName]"""
        class_name = storage.my_classes(args)
        if class_name is not None:
            new_class = class_name()
            new_class.save()
            print(new_class.id)

    def do_shell(self, args):
        """Provides shell functionalities within interpreter
        USAGE: shell [shell commands & arguments]
        EXMPL: shell ls -l"""
        os.system(args)

    def do_EOF(self, args):
        """Exits the program
        USAGE: ctrl^d
        USAGE: EOF
        """
        print()
        return True

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Overrides the Cmd class method functionalities"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
