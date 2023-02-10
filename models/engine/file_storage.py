#!/usr/bin/python3
"""Container for FileStorage class which handles storage of AirBnB objects"""
import json


class FileStorage:
    """File storage class to handle serialization and deserialization"""
    __file_path = 'file.json'
    __objects = {}

    def __init__(self):
        """Object instantiation method"""
        pass

    @property
    def objects(self):
        """Returns the private attribute 'objects'"""
        return self.__objects

    def all(self):
        """Returns dictionary containing all stored objects"""
        return self.__objects

    def new(self, obj):
        """Updates __objects attr with obj"""
        key = f'{type(obj).__name__}.{obj.id}'
        self.__objects.update({key: obj})
        self.save()

    def save(self):
        """Serializes and stores objects in JSON file and format"""
        with open(self.__file_path, mode='w', encoding='utf-8') as file:
            d = {}
            for key in self.__objects.keys():
                d.update({key: self.__objects[key].to_dict()})
            json.dump(d, file)

    def reload(self):
        """Deserializes stored objects from a JSON file"""
        try:
            with open(self.__file_path, mode='r', encoding='utf-8') as file:
                # from models.base_model import BaseModel
                f = json.load(file)
                for key in f.keys():
                    class_name = self.my_classes(f[key]['__class__'])
                    n = class_name(**f[key])
                    self.__objects.update({key: n})
        except (FileNotFoundError, ValueError):
            pass

    def my_classes(self, class_name=''):
        """Checks if class specified in 'class_name' exists
        returns class if it exists or None if it doesn't"""
        if class_name is None or len(class_name) < 1:
            print("** class name missing **")
            return None
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        class_dict = {'BaseModel': BaseModel, 'User': User, 'State': State,
                      'City': City, 'Amenity': Amenity, 'Place': Place,
                      'Review': Review}
        if class_name in class_dict:
            return class_dict[class_name]
        print("** class doesn't exist **")
        return None
