#!/usr/bin/python3
"""Defines unittests for models/place.py."""
import os
import unittest
from models.base_model import BaseModel
from models.place import Place

class TestPlace(unittest.TestCase):
    """Unittests for testing the Place class."""

    @classmethod
    def setUpClass(cls):
        """Place testing setup.
        Creates a new instance of Place.
        """
        cls.place = Place()
        cls.place.name = "My little house"
        cls.place.city_id = "0001"
        cls.place.user_id = "0001"
        cls.place.description = "A cozy cottage"
        cls.place.number_rooms = 2
        cls.place.number_bathrooms = 1
        cls.place.max_guest = 4
        cls.place.price_by_night = 100
        cls.place.latitude = 37.773972
        cls.place.longitude = -122.431297
        cls.place.amenity_ids = ["001", "002"]

    @classmethod
    def tearDownClass(cls):
        """Place testing teardown.
        Deletes the instance and attempts to remove the file if it exists.
        """
        del cls.place
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_instance(self):
        """Test if the created instance is indeed a Place object."""
        self.assertIsInstance(self.place, Place)

    def test_inheritance(self):
        """Test if Place inherits from BaseModel."""
        self.assertTrue(issubclass(type(self.place), BaseModel))

    def test_attributes(self):
        """Test if Place instance has the necessary attributes and correct values."""
        self.assertTrue(hasattr(self.place, "name"))
        self.assertTrue(hasattr(self.place, "city_id"))
        self.assertTrue(hasattr(self.place, "user_id"))
        self.assertTrue(hasattr(self.place, "description"))
        self.assertTrue(hasattr(self.place, "number_rooms"))
        self.assertTrue(hasattr(self.place, "number_bathrooms"))
        self.assertTrue(hasattr(self.place, "max_guest"))
        self.assertTrue(hasattr(self.place, "price_by_night"))
        self.assertTrue(hasattr(self.place, "latitude"))
        self.assertTrue(hasattr(self.place, "longitude"))
        self.assertTrue(hasattr(self.place, "amenity_ids"))
        self.assertEqual(self.place.name, "My little house")
        self.assertEqual(self.place.city_id, "0001")
        self.assertEqual(self.place.user_id, "0001")
        self.assertEqual(self.place.description, "A cozy cottage")
        self.assertEqual(self.place.number_rooms, 2)
        self.assertEqual(self.place.number_bathrooms, 1)
        self.assertEqual(self.place.max_guest, 4)
        self.assertEqual(self.place.price_by_night, 100)
        self.assertEqual(self.place.latitude, 37.773972)
        self.assertEqual(self.place.longitude, -122.431297)
        self.assertEqual(self.place.amenity_ids, ["001", "002"])

if __name__ == "__main__":
    unittest.main()
