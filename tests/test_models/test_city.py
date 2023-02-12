#!/usr/bin/python3
"""Test suite for the City class of AirBnB"""

from models.city import City
from unittest import TestCase


class TestCity(TestCase):
    """City class test suites definition"""
    def test_1(self):
        """Test method for the class attributes"""
        c = City()
        self.assertTrue(len(c.id) == 36)
        self.assertTrue(c.state_id == '')
        self.assertTrue(c.name == '')
