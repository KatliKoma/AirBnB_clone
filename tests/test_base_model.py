#!/usr/bin/python3
"""Unit tests for BaseModel class"""

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class"""

    def test_init(self):
        """Test the __init__ method of BaseModel"""
        model = BaseModel()
        self.assertTrue(hasattr(model, 'id'))
        self.assertTrue(hasattr(model, 'created_at'))
        self.assertTrue(hasattr(model, 'updated_at'))

    def test_save(self):
        """Test the save method of BaseModel"""
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(old_updated_at, model.updated_at)

    def test_to_dict(self):
        """Test the to_dict method of BaseModel"""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertTrue('id' in model_dict)
        self.assertTrue('created_at' in model_dict)
        self.assertTrue('updated_at' in model_dict)

if __name__ == '__main__':
    unittest.main()
