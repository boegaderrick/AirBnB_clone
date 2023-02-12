#!/usr/bin/python3
"""Test suite for the Place class of AirBnB"""

from models.place import Place
from unittest import TestCase


class TestPlace(TestCase):
    """Test class for the Place class definition"""
    def test_1(self):
        """Tests Place class attributes"""
        p = Place()
        self.assertTrue(p.city_id == '')
        self.assertTrue(p.user_id == '')
        self.assertTrue(p.name == '')
        self.assertTrue(type(p.description) is str)
        self.assertTrue(type(p.number_rooms) is int)
        self.assertEqual(p.number_bathrooms, 0)
        p.number_bathrooms = 4
        self.assertTrue(p.number_bathrooms == 4)
        self.assertTrue(type(p.max_guest) is int)
        self.assertTrue(type(p.price_by_night) is int)
        self.assertEqual(p.latitude, 0.0)
        self.assertEqual(p.longitude, 0.0)
        self.assertTrue(type(p.amenity_ids) is list)
