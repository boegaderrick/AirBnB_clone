#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

"""n = BaseModel()
n = User()
n = State()
n = City()
n = Amenity()
n = Place()
n = Review()"""

for key, value in storage.objects.items():
    print(value)
