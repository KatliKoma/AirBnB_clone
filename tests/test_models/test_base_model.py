#!/usr/bin/python3
"""
Unittest module for BaseModel
"""
import unittest
import os
from models.base_model import BaseModel



class TestBaseModel(unittest.TestCase):
    """
    Unittest for the BaseModel
    """

    def init_test(self):
        """
        Test for init
        """
        my_model = BaseModel()

        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)

    def str_test(self):
        """
        Test for string representation
        """
        my_model = BaseModel()

        self.assertTrue(str(my_model).startswith('[BaseModel]'))

        self.assertIn(my_model.id, str(my_model))

        self.assertIn(str(my_model.__dict__), str(my_model))


if __name__ == "__main__":
    unittest.main()

    def to_dict_test(self):
        """
        Test for to_dict
        """
        my_model = BaseModel()

        my_dict_model = my_model.to_dict()

        self.assertIsInstance(my_dict_model, dict)
        self.assertIsInstance(my_dict_model['id'], my_model.id)
        self.assertIsInstance(my_dict_model['created_at'], my_model.created_at.isoformat())
        self.assertIsInstance(my_dict_model['updated_at'], my_model.updated_at.isoformat())
        self.assertIsInstance(my_dict_model["__class__"], 'BaseModel')

    def test_save(self):
        """
        Test for the save method
        """
        my_model = BaseModel()

        initial_updated_at = my_model.updated_at
        current_updated_at = my_model.save()

        self.assertNotEqual(initial_updated_at, current_updated_at)
