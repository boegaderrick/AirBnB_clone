#!/usr/bin/python3
"""AirBnB BaseClass unittest module"""

import unittest
from models.base_model import BaseModel


class TestBaseClass(unittest.TestCase):
    """BaseModel tests class"""
    def test_1(self):
        n = BaseModel()
        self.assertEqual(len(n.id), 36)
