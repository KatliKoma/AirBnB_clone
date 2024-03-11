#!/usr/bin/python3
"""Defines unittests for models/state.py."""
import os
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """Unittests for testing the State class."""

    @classmethod
    def setUpClass(cls):
        """State testing setup.
        Creates a new instance of State.
        """
        cls.state = State()
        cls.state.name = "California"

    @classmethod
    def tearDownClass(cls):
        """State testing teardown.
        Deletes the instance and attempts to remove the file if it exists.
        """
        del cls.state
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_instance(self):
        """Test if the created instance is indeed a State object."""
        self.assertIsInstance(self.state, State)

    def test_inheritance(self):
        """Test if State inherits from BaseModel."""
        self.assertTrue(issubclass(type(self.state), BaseModel))

    def test_attributes(self):
        """Test if State instance has the necessary
        attributes and correct values."""
        self.assertTrue(hasattr(self.state, "id"))
        self.assertTrue(hasattr(self.state, "created_at"))
        self.assertTrue(hasattr(self.state, "updated_at"))
        self.assertTrue(hasattr(self.state, "name"))
        self.assertEqual(self.state.name, "California")


if __name__ == "__main__":
    unittest.main()
