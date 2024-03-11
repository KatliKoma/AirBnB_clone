#!/usr/bin/python3
"""Defines the User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """class for the management of user objects"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
