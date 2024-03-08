# In tests/test_models.py

import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_create_instance(self):
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)

    def test_attribute_access(self):
        obj = BaseModel()
        obj.name = "Test Object"
        self.assertEqual(obj.name, "Test Object")

    def test_to_dict(self):
        obj = BaseModel()
        obj.name = "Test Object"
        obj_dict = obj.to_dict()
        self.assertEqual(obj_dict['name'], "Test Object")

    def test_from_dict(self):
    data =
        {
                'name': "Test Object",
                'id': "123"
        }
        obj = BaseModel(**data)
        self.assertEqual(obj.name, "Test Object")
        self.assertEqual(obj.id, "123")

if __name__ == '__main__':
    unittest.main()
