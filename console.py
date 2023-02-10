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

    def do_update(self, args):
        """Updates instance specified by Class and id
        USAGE: update <ClassName> <id> <attribute name> <attribute value>"""
        temp = args.rsplit()[:4]
        class_name = temp[0] if len(temp) > 0 else None
        obj_id = temp[1] if len(temp) > 1  else None
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
        name_id = f'{class_name} {obj_id}' if obj_id is not None else class_name
        obj = self.get_obj(name_id)
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
        storage.save()

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
        """Handles the EOF condition"""
        print()
        return True

    def do_quit(self, args):
        """Ends the program when the command 'quit' is received"""
        return True

    def emptyline(self):
        """Overrides the Cmd class method functionalities"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
