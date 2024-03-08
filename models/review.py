#!/usr/bin/python3
"""This modue define a Review class"""
import BaseModel


class Review(BaseModel):
    """class for the management of review objects"""

    place_id = ""
    user_id = ""
    text = ""
