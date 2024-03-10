#!/usr/bin/python3
"""Defines unit tests for models/base_model.py.

Unit test classes:
    BaseModelTest_Instantiation
    BaseModelTest_SaveMethod
    BaseModelTest_ToDictMethod
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel


class BaseModelTest_Instantiation(unittest.TestCase):
    """Unit tests for testing instantiation of BaseModel."""

    def test_no_arguments_creates_instance(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_instance_in_storage(self):
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_id_is_str_public_attribute(self):
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_public_datetime_attribute(self):
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_public_datetime_attribute(self):
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_unique_ids_for_different_instances(self):
        base_model_1 = BaseModel()
        base_model_2 = BaseModel()
        self.assertNotEqual(base_model_1.id, base_model_2.id)

    def test_different_created_at_for_new_instances(self):
        base_model_1 = BaseModel()
        sleep(0.05)
        base_model_2 = BaseModel()
        self.assertLess(base_model_1.created_at, base_model_2.created_at)

    def test_different_updated_at_for_new_instances(self):
        base_model_1 = BaseModel()
        sleep(0.05)
        base_model_2 = BaseModel()
        self.assertLess(base_model_1.updated_at, base_model_2.updated_at)

    def test_string_representation(self):
        datetime_now = datetime.today()
        datetime_repr = repr(datetime_now)
        base_model = BaseModel()
        base_model.id = "123456"
        base_model.created_at = base_model.updated_at = datetime_now
        str_base_model = base_model.__str__()
        self.assertIn("[BaseModel] (123456)", str_base_model)
        self.assertIn("'id': '123456'", str_base_model)
        self.assertIn("'created_at': " + datetime_repr, str_base_model)
        self.assertIn("'updated_at': " + datetime_repr, str_base_model)

    def test_unused_arguments(self):
        base_model = BaseModel(None)
        self.assertNotIn(None, base_model.__dict__.values())

    def test_instantiation_with_kwargs(self):
        datetime_now = datetime.today()
        datetime_iso = datetime_now.isoformat()
        base_model = BaseModel(id="345", created_at=datetime_iso, updated_at=datetime_iso)
        self.assertEqual(base_model.id, "345")
        self.assertEqual(base_model.created_at, datetime_now)
        self.assertEqual(base_model.updated_at, datetime_now)

    def test_instantiation_with_None_kwargs_raises_error(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_args_and_kwargs(self):
        datetime_now = datetime.today()
        datetime_iso = datetime_now.isoformat()
        base_model = BaseModel("12", id="345", created_at=datetime_iso, updated_at=datetime_iso)
        self.assertEqual(base_model.id, "345")
        self.assertEqual(base_model.created_at, datetime_now)
        self.assertEqual(base_model.updated_at, datetime_now)


class BaseModelTest_SaveMethod(unittest.TestCase):
    """Unit tests for testing the save method of BaseModel."""

    @classmethod
    def setUpClass(cls):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_single_save_method_call(self):
        base_model = BaseModel()
        sleep(0.05)
        initial_updated_at = base_model.updated_at
        base_model.save()
        self.assertLess(initial_updated_at, base_model.updated_at)

    def test_multiple_save_method_calls(self):
        base_model = BaseModel()
        sleep(0.05)
        initial_updated_at = base_model.updated_at
        base_model.save()
        after_first_save = base_model.updated_at
        self.assertLess(initial_updated_at, after_first_save)
        sleep(0.05)
        base_model.save()
        self.assertLess(after_first_save, base_model.updated_at)

    def test_save_method_with_argument_raises_error(self):
        base_model = BaseModel()
        with self.assertRaises(TypeError):
            base_model.save(None)

    def test_save_updates_file_storage(self):
        base_model = BaseModel()
        base_model.save()
        base_model_id = "BaseModel." + base_model.id
        with open("file.json", "r") as file:
            self.assertIn(base_model_id, file.read())


class BaseModelTest_ToDictMethod(unittest.TestCase):
    """Unit tests for testing the to_dict method of BaseModel."""

    def test_to_dict_returns_dictionary(self):
        base_model = BaseModel()
        self.assertTrue(dict, type(base_model.to_dict()))

    def test_to_dict_contains_correct_keys(self):
        base_model = BaseModel()
        self.assertIn("id", base_model.to_dict())
        self.assertIn("created_at", base_model.to_dict())
        self.assertIn("updated_at", base_model.to_dict())
        self.assertIn("__class__", base_model.to_dict())

    def test_to_dict_includes_added_attributes(self):
        base_model = BaseModel()
        base_model.name = "Holberton"
        base_model.my_number = 98
        base_model_dict = base_model.to_dict()
        self.assertIn("name", base_model_dict)
        self.assertIn("my_number", base_model_dict)

    def test_to_dict_converts_datetime_to_str(self):
        base_model = BaseModel()
        base_model_dict = base_model.to_dict()
        self.assertEqual(str, type(base_model_dict["created_at"]))
        self.assertEqual(str, type(base_model_dict["updated_at"]))

    def test_to_dict_output_matches_expected_dict(self):
        datetime_now = datetime.today()
        base_model = BaseModel()
        base_model.id = "123456"
        base_model.created_at = base_model.updated_at = datetime_now
        expected_dict = {
            'id': '123456',
            '__class__': 'BaseModel',
            'created_at': datetime_now.isoformat(),
            'updated_at': datetime_now.isoformat()
        }
        self.assertDictEqual(base_model.to_dict(), expected_dict)

    def test_difference_between_to_dict_and___dict__(self):
        base_model = BaseModel()
        self.assertNotEqual(base_model.to_dict(), base_model.__dict__)

    def test_to_dict_with_argument_raises_error(self):
        base_model = BaseModel()
        with self.assertRaises(TypeError):
            base_model.to_dict(None)


if __name__ == "__main__":
    unittest.main()
