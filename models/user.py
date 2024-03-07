#!/usr/bin/python3
"""This module defines a User class"""
import BaseModel


class User(BaseModel):
    """class for the management of user objects"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
