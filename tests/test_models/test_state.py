#!/usr/bin/python3
"""This module contains tests for the State class of AirBnB"""

from models.state import State
from unittest import TestCase


class TestState(TestCase):
    """This class defines test methods for the State class"""
    def test_1(self):
        """Tests State class attributes"""
        s = State()
        self.assertTrue(len(s.name) == 0)
        self.assertTrue(type(s.name) is str)
