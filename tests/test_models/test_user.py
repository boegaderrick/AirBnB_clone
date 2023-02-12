#!/usr/bin/python3
"""This module contains tests for the User class"""
from models.user import User
from unittest import TestCase
from time import sleep


class TestUser(TestCase):
    """Defines tests for the User class of AirBnB clone"""
    def test_1(self):
        """Tests inheritance from BaseModel class"""
        u = User()
        self.assertTrue(hasattr(u, 'id'))
        self.assertTrue(hasattr(u, 'created_at'))
        self.assertTrue(hasattr(u, 'updated_at'))
        self.assertEqual(36, len(u.id))
        sleep(1.1)
        u.first_name = 'jane'
        u.save()
        delta = (u.updated_at - u.created_at).total_seconds()
        self.assertGreater(delta, 0)
