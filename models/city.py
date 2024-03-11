#!/usr/bin/python3
"""This module defines a City class"""

from models.base_model import BaseModel


class City(BaseModel):
    """Class for the management of city objects"""

    state_id = ""
    name = ""
