#!/usr/bin/python3
<<<<<<< HEAD
"""
Defines the user class.
"""
=======
"""Defines the User class."""
>>>>>>> 85b301cfb134e90a7648ac36833d226afb5da6df
from models.base_model import BaseModel


class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
