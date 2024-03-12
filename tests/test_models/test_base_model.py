#!/usr/bin/python3
import unittest
import models
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def test_instance_creation(self):
        """Test the creation of a BaseModel instance and its attributes."""
        instance = BaseModel()
        self.assertTrue(hasattr(instance, "id"))
        self.assertTrue(hasattr(instance, "created_at"))
        self.assertTrue(hasattr(instance, "updated_at"))


if __name__ == "__main__":
    unittest.main()
