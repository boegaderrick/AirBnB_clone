#!/usr/bin/python3
"""This modules implements the Amenity class of AirBnB clone"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class definition"""
    name = ''

    def __init__(self, *args, **kwargs):
        """Object constructor"""
        super().__init__(*args, **kwargs)
