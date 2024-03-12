#!/usr/bin/python
"""This module defines an Amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Class for the management of Amenity objects
    

    Attributes:
        name (str): name of amenity.
    """

    name = ""
