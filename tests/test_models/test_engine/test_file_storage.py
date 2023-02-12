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
        self.assertTrue(b in f.all().values())
        temp = b.to_dict().copy()
        del b
        k = BaseModel(**temp)
        self.assertEqual(temp, k.to_dict())
        m = FileStorage()
        self.assertEqual(m.all(), f.all())

    def test_2(self):
        """Tests models defined in FileStorage class"""
        b = BaseModel()
        f = FileStorage()
        b.name = 'new york'
        f.new(b)
        f.save()
        self.assertTrue(b in f.all().values())
        temp = b.id
        del b
        f.reload()
        self.assertTrue(f'BaseModel.{temp}' in f.objects)
