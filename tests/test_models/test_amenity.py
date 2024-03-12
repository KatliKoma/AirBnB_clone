#!/usr/bin/python3
"""
Module for Amenity class unittest
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenity_instantiation(unittest.TestCase):
    """
    Unittests for testing instantiation of the Amenity class.
    """
    def setUp(self):
        try:
            os.rename("file.json", "tmp.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp.json", "file.json")
        except FileNotFoundError:
            pass

    def test_no_args_instantiates(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_new_instance_stored(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_if_is_public_class_attribute(self):
        amenity0 = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", amenity0.__dict__)

    def test_amenities_unique_ids(self):
        amenity0 = Amenity()
        amenity1 = Amenity()
        self.assertNotEqual(amenity0.id, amenity1.id)

    def test_two_amenities_created_at(self):
        amenity0 = Amenity()
        sleep(0.05)
        amenity1 = Amenity()
        self.assertLess(amenity0.created_at, amenity0.created_at)

    def test_two_amenities_updated_at(self):
        amenity0 = Amenity()
        sleep(0.05)
        amenity1 = Amenity()
        self.assertLess(amenity0.updated_at, amenity1.updated_at)

    def test_str_representation(self):
        my_date = datetime.today()
        my_date_rep = repr(my_date)
        amenity0 = Amenity()
        amenity0.id = "777777"
        amenity0.created_at = amenity0.updated_at = my_date
        amenity_str = amenity0.__str__()
        self.assertIn("[Amenity] (777777)", amenity_str)
        self.assertIn("'id': '777777'", amenity_str)
        self.assertIn("'created_at': " + my_date_rep, amenity_str)
        self.assertIn("'updated_at': " + my_date_rep, amenity_str)

    def test_unused_args(self):
        amenity0 = Amenity(None)
        self.assertNotIn(None, amenity0.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """
        instantiation with kwargs test method
        """
        my_date = datetime.today()
        my_iso_date = my_date.isoformat()
        amenity0 = Amenity(id="777", created_at=my_iso_date, updated_at=my_date_iso)
        self.assertEqual(amenity0.id, "777")
        self.assertEqual(amenity0.created_at, my_date)
        self.assertEqual(amenity0.updated_at, my_date)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)

class TestAmenity_save(unittest.TestCase):
    """
    Unittests for save method of the Amenity class.
    """

    def setUp(self):
        try:
            os.rename("file.json", "tmp.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp.json", "file.json")
        except FileNotFoundError:
            pass

    def test_save_one(self):
        amenity0 = Amenity()
        sleep(0.05)
        first_updated_at = amenity0.updated_at
        amenity0.save()
        self.assertLess(first_updated_at, amenity0.updated_at)

    def test_saves_two(self):
        amenity0 = Amenity()
        sleep(0.05)
        first_updated_at = amenity0.updated_at
        amenity0.save()
        second_updated_at = amenity1.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        amenity0.save()
        self.assertLess(second_updated_at, amenity0.updated_at)

    def test_save_with_arg(self):
        amenity0 = Amenity()
        with self.assertRaises(TypeError):
            amenity0.save(None)

    def test_save_updates_file(self):
        amenity0 = Amenity()
        amenity0.save()
        amenity_id = "Amenity." + amenity1.id
        with open("file.json", "r") as f:
            self.assertIn(amenity_id, f.read())


class TestAmenity_to_dict(unittest.TestCase):
    """
    Unittests for to_dict method of the Amenity class.
    """
    def setUp(self):
        try:
            os.rename("file.json", "tmp.json")
        except FileNotFoundError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass
        try:
            os.rename("tmp.json", "file.json")
        except FileNotFoundError:
            pass

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Amenity().to_dict()))

    def test_if_contains_correct_keys(self):
        amenity0 = Amenity()
        self.assertIn("id", amenity0.to_dict())
        self.assertIn("__class__", amenity0.to_dict())
        self.assertIn("created_at", amenity0.to_dict())
        self.assertIn("update_at", amenity0.to_dict())

    def test_with_added_attributes(self):
        amenity0 = Amenity()
        amenity0.middle_name = "Johnson"
        amenity0.my_number = 777
        self.assertEqual("Johnson", amenity0.middle_name)
        self.assertIn("my_number", amenity0.to_dict())

    def test_datetime_attributes_as_strs(self):
        amenity0 = Amenity()
        dict_amenity = amenity0.to_dict()
        self.assertEqual(str, type(dict_amenity["id"]))
        self.assertEqual(str, type(dict_amenity["created_at"]))
        self.assertEqual(str, type(dict_amenity["updated_at"]))

    def test_to_dict_output(self):
        my_date = datetime.today()
        amenity0 = Amenity()
        amenity0.id = "777777"
        amenity0.created_at = amenity0.updated_at = my_date
        to_dict = {
            'id': '777777',
            '__class__': 'Amenity',
            'created_at': my_date.isoformat(),
            'updated_at': my_date.isoformat(),
        }
        self.assertDictEqual(amenity0.to_dict(), to_dict)

    def test_to_dict_difference(self):
        amenity0 = Amenity()
        self.assertNotEqual(amenity0.to_dict(), amenity0.__dict__)

    def test_to_dict_arg(self):
        amenity0 = Amenity()
        with self.assertRaises(TypeError):
            amenity0.to_dict(None)


if __name__ == "__main__":
    unittest.main()
