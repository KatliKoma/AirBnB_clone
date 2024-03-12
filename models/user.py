#!/usr/bin/python3
"""
Defines the user class.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Class user handles the user's information
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
