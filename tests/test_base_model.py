#!/usr/bin/python3
"""Unittest for BaseModel"""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Test cases for BaseModel class"""


    def test_init(self):
        """Test the __init__ method of BaseModel"""
        # Test when creating a new instance without passing arguments
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertTrue(hasattr(model, 'id'))
        self.assertTrue(hasattr(model, 'created_at'))
        self.assertTrue(hasattr(model, 'updated_at'))

        # Test when creating a new instance passing arguments
        created_at = datetime(2022, 3, 10, 12, 30, 0)
        updated_at = datetime(2022, 3, 10, 12, 35, 0)
        model = BaseModel(
            id="test_id",
            created_at=created_at,
            updated_at=updated_at
        )
        self.assertEqual(model.id, "test_id")
        self.assertEqual(model.created_at, created_at)
        self.assertEqual(model.updated_at, updated_at)

    def test_save(self):
        """Test the save method of BaseModel"""
        # Test that updated_at attribute is updated after save
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(model.updated_at, old_updated_at)

    def test_to_dict(self):
        """Test the to_dict method of BaseModel"""
        # Test the to_dict method returns the expected dictionary
        model = BaseModel()
        model_dict = model.to_dict()

        self.assertIsInstance(model_dict, dict)
        self.assertIn('__class__', model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)

    def test_str(self):
        """Test the __str__ method of BaseModel"""
        # Test the string representation of the model
        model = BaseModel()
        model_str = str(model)
        expected_str = f"[BaseModel] ({model.id}) {model.__dict__}"
        self.assertEqual(model_str, expected_str)
