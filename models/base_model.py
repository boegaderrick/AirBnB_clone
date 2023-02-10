#!/usr/bin/python3
"""This module contains the base class for AirBnB clone"""
from datetime import datetime
from uuid import uuid4
from models import storage


class BaseModel:
    """AirBnB clone base class"""
    id = ''
    created_at = datetime
    updated_at = datetime

    def __init__(self, *args, **kwargs):
        """BaseModel object instantiation"""
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at' or key == 'updated_at':
                    self.__dict__[key] = datetime.fromisoformat(value)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Returns informal string representation of object"""
        return (f'[{type(self).__name__}] ({self.id}) {self.__dict__}')

    def save(self):
        """This method edits updated_at attr when necessary"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns __dict__ that includes __class__ pair"""
        class_name = type(self).__name__
        new = {'__class__': class_name}
        new.update(self.__dict__)
        new['created_at'] = datetime.isoformat(new['created_at'])
        new['updated_at'] = datetime.isoformat(new['updated_at'])
        return new
