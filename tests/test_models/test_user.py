#!/usr/bin/python3
"""This module contains tests for the User class"""
from models.user import User
from unittest import TestCase
from time import sleep
from datetime import datetime


class TestUser(TestCase):
    """Defines tests for the User class of AirBnB clone"""
    def test_1(self):
        """Tests inheritance from BaseModel class"""
        u = User()
        self.assertTrue(hasattr(u, 'id'))
        self.assertTrue(hasattr(u, 'created_at'))
        self.assertTrue(type(u.created_at) is datetime)
        self.assertTrue(hasattr(u, 'updated_at'))
        self.assertTrue(type(u.updated_at) is datetime)
        self.assertEqual(36, len(u.id))
        sleep(1.1)
        u.first_name = 'jane'
        u.save()
        delta = (u.updated_at - u.created_at).total_seconds()
        self.assertGreater(delta, 0)

    def test_2(self):
        """Tests User class attributes"""
        u = User()
        self.assertEqual(u.email, '')
        self.assertEqual(u.password, '')
        self.assertEqual(u.first_name, '')
        self.assertEqual(u.last_name, '')
        u.email = 'email@mail.com'
        u.password = 'password'
        u.first_name = 'jane'
        u.last_name = 'doe'
        self.assertEqual(u.email, 'email@mail.com')
        self.assertEqual(u.password, 'password')
        self.assertEqual(u.first_name, 'jane')
        self.assertEqual(u.last_name, 'doe')
