#!/usr/bin/python3
"""This module implements the User class of AirBnB clone"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class definition"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        """User class object constructor"""
        super().__init__(*args, **kwargs)
