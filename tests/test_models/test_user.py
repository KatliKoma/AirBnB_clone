#!/usr/bin/python3
import unittest
from models.user import User

class TestUser(unittest.TestCase):
    def test_user_attributes(self):
        user = User()
        user.email = "test@example.com"
        user.password = "password"
        user.first_name = "FirstName"
        user.last_name = "LastName"
        self.assertEqual(user.email, "test@example.com")
        # Continue with other attribute tests

if __name__ == '__main__':
    unittest.main()
