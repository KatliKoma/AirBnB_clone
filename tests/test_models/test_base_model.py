#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    Test the BaseModel class.
    """

    def test_instance_creation(self):
        """Test the creation of a BaseModel instance and its attributes."""
        instance = BaseModel()
        self.assertTrue(hasattr(instance, "id"))
        self.assertTrue(hasattr(instance, "created_at"))
        self.assertTrue(hasattr(instance, "updated_at"))
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)
        self.assertEqual(str, type(instance.id))

    def test_str_method(self):
        """Test that the str method has the correct output."""
        instance = BaseModel()
        expected = "[BaseModel] ({}) {}".format(instance.id, instance.__dict__)
        self.assertEqual(expected, str(instance))

    def test_save_method(self):
        """Test the save method updates 'updated_at' and persists changes."""
        instance = BaseModel()
        old_updated_at = instance.updated_at
        instance.save()
        self.assertNotEqual(old_updated_at, instance.updated_at)

    def test_to_dict_method(self):
        """Test the to_dict method returns the correct dictionary."""
        instance = BaseModel()
        instance_dict = instance.to_dict()
        self.assertEqual(instance_dict['__class__'], 'BaseModel')
        self.assertEqual(instance_dict['id'], instance.id)
        self.assertIsInstance(instance_dict['created_at'], str)
        self.assertIsInstance(instance_dict['updated_at'], str)


if __name__ == "__main__":
    unittest.main()
