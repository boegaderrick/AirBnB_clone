#!/usr/python3
"""Test suite for the Review class of AirBnB"""

from models.review import Review
from unittest import TestCase


class TestReview(TestCase):
    """Test class for the Review class"""
    def test_1(self):
        """Tests attributes of the Review class"""
        r = Review()
        self.assertFalse(r.id.isspace())
        self.assertTrue(r.place_id == '')
        self.assertTrue(type(r.user_id) is str)
        self.assertFalse(len(r.text) > 0)
