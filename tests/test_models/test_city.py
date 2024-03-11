#!/usr/bin/python3
"""Defines unittests for models/city.py."""
import os
import models
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """Unittests for testing the City class."""

    @classmethod
    def setUpClass(cls):
        """City testing setup.
        Creates a new instance of City.
        """
        cls.city = City()
        cls.city.name = "San Francisco"
        cls.city.state_id = "CA"

    @classmethod
    def tearDownClass(cls):
        """City testing teardown.
        Deletes the instance and attempts to remove the file if it exists.
        """
        del cls.city
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_instance(self):
        """Test if the created instance is indeed a City object."""
        self.assertIsInstance(self.city, City)

    def test_inheritance(self):
        """Test if City inherits from BaseModel."""
        self.assertTrue(issubclass(type(self.city), BaseModel))

    def test_attributes(self):
        """Test if City instance has the necessary attributes."""
        self.assertTrue(hasattr(self.city, "id"))
        self.assertTrue(hasattr(self.city, "created_at"))
        self.assertTrue(hasattr(self.city, "updated_at"))
        self.assertTrue(hasattr(self.city, "name"))
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertEqual(self.city.name, "San Francisco")
        self.assertEqual(self.city.state_id, "CA")

    def test_to_dict(self):
        """Test conversion of object attributes to dictionary for json."""
        city_dict = self.city.to_dict()
        self.assertEqual(city_dict["name"], "San Francisco")
        self.assertEqual(city_dict["__class__"], "City")
        self.assertEqual(city_dict["state_id"], "CA")
        self.assertTrue("created_at" in city_dict)
        self.assertTrue("updated_at" in city_dict)


if __name__ == "__main__":
    unittest.main()
