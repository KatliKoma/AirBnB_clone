#!/usr/bin/python3
"""Defines unittests for models/user.py."""
import os
import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """Unittests for testing the User class."""

    @classmethod
    def setUpClass(cls):
        """User testing setup.
        Creates a new instance of User.
        """
        cls.user = User()
        cls.user.email = "user@example.com"
        cls.user.password = "password"
        cls.user.first_name = "John"
        cls.user.last_name = "Doe"

    @classmethod
    def tearDownClass(cls):
        """User testing teardown.
        Deletes the instance and attempts to remove the file if it exists.
        """
        del cls.user
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_instance(self):
        """Test if the created instance is indeed a User object."""
        self.assertIsInstance(self.user, User)

    def test_inheritance(self):
        """Test if User inherits from BaseModel."""
        self.assertTrue(issubclass(type(self.user), BaseModel))

    def test_attributes(self):
        """Test if User instance has the necessary
        attributes and correct values."""
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))
        self.assertEqual(self.user.email, "user@example.com")
        self.assertEqual(self.user.password, "password")
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")

    def test_to_dict(self):
        """Test conversion of object attributes to dictionary for json."""
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict["email"], "user@example.com")
        self.assertEqual(user_dict["__class__"], "User")
        self.assertTrue("created_at" in user_dict)
        self.assertTrue("updated_at" in user_dict)


if __name__ == "__main__":
    unittest.main()
