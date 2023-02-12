#!/usr/bin/python3
"""Test suite for the Amenity class"""

from models.amenity import Amenity
from unittest import TestCase
from datetime import datetime


class TestAmenity(TestCase):
    """Amenity class test class definition"""
    def test_1(self):
        """Tests the attributes of the Amenity class"""
        a = Amenity()
        self.assertTrue(hasattr(a, 'name'))
        self.assertTrue(a.name == '')
        self.assertTrue(type(a.created_at) is datetime)
        self.assertTrue(type(a.id) is str)
        self.assertTrue(len(a.id) == 36)
