#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from models import storage

class TestSaveReloadBaseModel(unittest.TestCase):
    def test_save_reload(self):
        # Test saving and reloading BaseModel instances
        # Create a new BaseModel instance
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89

        # Save the BaseModel instance
        my_model.save()

        # Reload all objects from the storage
        storage.reload()

        # Retrieve the reloaded BaseModel instance
        reloaded_objs = storage.all()

        # Check if the reloaded object is present and matches the original
        self.assertIn(my_model.id, reloaded_objs)
        reloaded_model = reloaded_objs[my_model.id]
        self.assertEqual(my_model.name, reloaded_model.name)
        self.assertEqual(my_model.my_number, reloaded_model.my_number)

if __name__ == '__main__':
    unittest.main()
