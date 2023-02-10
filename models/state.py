#!/usr/bin/python3
"""This module implements the state class of AirBnB clone"""
from models.base_model import BaseModel


class State(BaseModel):
    """State class definition"""
    name = ''

    def __init__(self, *args, **kwargs):
        """State object instantiation"""
        super().__init__(*args, **kwargs)
