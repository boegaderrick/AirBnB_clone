#!/usr/bin/python3
"""Module contains review class of AirBnB clone"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class definition"""
    place_id = ''
    user_id = ''
    text = ''

    def __init__(self, *args, **kwargs):
        """Review class object constructor"""
        super().__init__(*args, **kwargs)
