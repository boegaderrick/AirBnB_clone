#!/usr/bin/python3
"""This module implements the city class of AirBnB clone"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class definition"""
    state_id = ''
    name = ''

    def __init__(self, *args, **kwargs):
        """City object constructor"""
        super().__init__(*args, **kwargs)
