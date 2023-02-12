#!/usr/bin/python3
"""AirBnB BaseClass unittest module"""

import unittest
from models.base_model import BaseModel
import datetime
import time


class TestBaseClass(unittest.TestCase):
    """BaseModel tests class"""
    def test_1(self):
        """Performs tests on BaseModel class"""
        n = BaseModel()
        delta = (n.updated_at - n.created_at).total_seconds()
        self.assertIsInstance(n.__str__(), str)
        self.assertTrue('__class__' in n.to_dict())
        self.assertTrue(hasattr(n, 'id'))
        self.assertEqual(len(n.id), 36)
        self.assertAlmostEqual(delta, 0, places=4)
        time.sleep(1.1)
        n.save()
        delta = (n.updated_at - n.created_at).total_seconds()
        self.assertGreater(delta, 1)
