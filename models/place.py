#!/usr/bin/python3
"""This module contains Place class of AirBnB"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Place class definition"""
    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = int

    def __init__(self, *args, **kwargs):
        """Place object constructor"""
        super().__init__(*args, **kwargs)
