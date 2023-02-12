#!/usr/bin/python3
"""This module contains the FileStorage class unit tests"""

from unittest import TestCase
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(TestCase):
    """FileStorage class test class definition"""
    def test_1(self):
        """Performs tests on the FileStorage class"""
        b = BaseModel()
        f = FileStorage()
        f.all()
        #self.assertTrue(b in f.all().values())
